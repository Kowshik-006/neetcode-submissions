class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # operators = {'+', '-', '*', '/'}

        # for i in range(len(tokens)):
        #     if tokens[i] in operators:
        #         operand_1 = int(tokens[i-2])
        #         operand_2 = int(tokens[i-1])
        #         result = 0
        #         if tokens[i] == '+':
        #             result = operand_1 + operand_2
        #         elif tokens[i] == '-':
        #             result = operand_1 - operand_2
        #         elif tokens[i] == '*':               
        #             result == operand_1 * operand_2
        #         else:
        #             result == operand_1 // operand_2
                
        #         tokens = tokens[:i-2] + [str(result)] + tokens[i+1:]
        # return tokens[-1]

        while len(tokens) > 1:
            for i in range(len(tokens)):
                if tokens[i] in "+-*/":
                    a = int(tokens[i-2])
                    b = int(tokens[i-1])
                    if tokens[i] == '+':
                        result = a + b
                    elif tokens[i] == '-':
                        result = a - b
                    elif tokens[i] == '*':
                        result = a * b
                    elif tokens[i] == '/':
                        result = int(a / b)
                    tokens = tokens[:i-2] + [str(result)] + tokens[i+1:]
                    break
        return int(tokens[0])