class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        opertors = "+-*/"

        for token in tokens:

            if token.lstrip('-').isdigit():
                stack.append(int(token))
            elif token in opertors:
                y = stack.pop()
                x = stack.pop()
                
                match token:
                    case "+":
                        stack.append(x+y)
                    case "-": 
                        stack.append(x-y)
                    case "*":
                        stack.append(x*y)
                    case "/":
                        stack.append(int(x/y))
        

        return stack[-1]

        