# Pearl Yu, CSCI 3320 Data Structures - Assignment #2

def precedence(op):
    # Check operator precedence using PEMDAS order

    # If operator is ^ it is of highest precedence
    if(op == '^'):
        return 1
    # If operator is * or / it is of second-highest precedence
    if(op == '*' or op == '/'):
        return 2
    # If operator is + or - it is of last precedence
    else:
        return 3

def is_operator(c):
    # Check if the character is an operator
    if c == '+' or c == '–' or c == '*' or c == '/' or c == '^':
        return True
    else:
        return False

def infix_to_postfix(expression):
    # 'op_stack' and 'result' are stacks implemented with list
    op_stack = []
    result = []

    # 'prev_was_op' tracks of the previous character was an operator; for example, it will help detect bad cases where we have 3+*2
    prev_was_op = True

    # 'in_block', 'depth', and 'block' help keep track of parentheses
    in_block = False # 'in_block' tracks if we are in a parentheses block, for example, (2+...
    depth = 0
    block = ""

    # 'ct' keeps track of our index
    ct = 0

    # Convert infix expression to postfix expression(using recursion if there are parentheses)
    for c in expression:
        # Increase 'ct' by 1
        ct = ct + 1

        # If in a parentheses block
        if in_block:
            # Check if we have reached matching parentheses, and update depth
            if c == ')':
                depth -= 1
            elif c == '(':
                depth += 1

            # If we have reached matching parentheses, recursively call our function
            if depth == 0:
                result += infix_to_postfix(block)

                # Reset our variables and continue
                in_block = False
                prev_was_op = False
                block = ""
                continue
            
            # If we have not reached matching parentheses, add current character to our block and continue
            block += c
            continue

        # If we are not in a block and see a '(' character, start a new block
        if c == '(':
            in_block = True
            depth = 1
            continue
        
        # Otherwise, we are not in a block and do not see a '(' character

        # If c is a number
        if(not is_operator(c)):
            # Append c onto our 'result' stack
            result.append(c)

        # If c is an operator, 'op_stack'(which keeps track of a stack of our operators) is not empty, and the precedence of the previous operator in op_stack is higher than the current operator(for example if we are at character '+' in the expression '3*4+8')
        if(is_operator(c) and len(op_stack) and precedence(c) > precedence(op_stack[len(op_stack) - 1])):
            # Then add the operators one by one from 'op_stack' to the 'result' stack
            while(len(op_stack)):
                result.append(op_stack.pop())

        # Catch if there are errors
        if(not (is_operator(c) or ('0' <= c and c <= '9'))):
            # If c is not an operator or a number (we handle parentheses during the recursion, so we don't need to worry about '(' or ')') then we show error by returning -1
            return -1
        elif(is_operator(c) and (ct == len(expression) or prev_was_op)):
            # If c is an operator and this is the final character of our expression, OR if c is an operator and so was the previous character, then we show error by returning -2
            return -2

        # If c is a character
        if(is_operator(c)):
            # Append c to the 'op_stack' for operators, and update 'prev_was_op' if c is an operator
            op_stack.append(c)
            prev_was_op = True
        else:
            prev_was_op = False
    
    # At the end of iterating through all 'c' in 'expression', if there are still operators left in 'op_stack', then add them to 'result'
    while(len(op_stack)):
        result.append(op_stack.pop())

    # Return the 'result' stack; we don't use a string right now because appending characters takes too much time
    return result
    

def evaluate_postfix(expression):    
    # Evaluate the postfix expression

    # Use one stack of integers
    stack = []

    # Iterate over each character 'c' in expression
    for c in expression:
        if(is_operator(c)):
            # If 'c' is an operator, check last two integers in stack
            b = stack.pop()
            a = stack.pop()

            # Depending on what operator 'c' is, replace the last two integers in the stack with their...
            if(c == '+'):
                # ... sum
                stack.append(a + b)
            elif(c == '–'):
                # ... difference
                stack.append(a - b)
            elif(c == '*'):
                # ... product
                stack.append(a * b)
            elif(c == '/'):
                # ... quotient
                stack.append(a / b)
            elif(c == '^'):
                # ... or the power of the first number to the second number
                stack.append(pow(a, b))
        else:
            # Otherwise, if 'c' is a number, then we append it to the stack 
            stack.append(int(c))

    # Return the remaining integer in 'stack'; there should only be one number remaining in 'stack' at this point
    return int(stack.pop())

def main():
    while True:
        expression = input("Input: ")

        # If user does not give any expression, they want to terminate the program so we break
        if not expression:
            break

        # Convert infix to postfix
        postfix = infix_to_postfix(expression)

        # If 'infix_to_postfix' returned an error, then show the user what the error is, and continue
        if postfix == -1:
            print("only numbers are available.")
            continue
        elif postfix == -2:
            print("invalid inputs")
            continue

        # Otherwise, if we do not have an error, convert postfix to a String
        postfix = ''.join(postfix)

        print("postfix:", postfix)
        # Evaluate the postfix expression
        result = evaluate_postfix(postfix)
        print("Output:", result)

if __name__ == "__main__":
    main()
