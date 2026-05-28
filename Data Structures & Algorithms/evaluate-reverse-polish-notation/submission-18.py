class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {'+', '-', '*', '/'}
        stack = []

        for token in tokens:
            if token in operators:
                operand_2 = stack.pop()
                operand_1 = stack.pop()

                if token == "+":
                    stack.append(operand_1 + operand_2)
                elif token == "-":
                    stack.append(operand_1  - operand_2)
                elif token == "*":
                    stack.append(operand_1 * operand_2)
                else:
                    stack.append(int(float(operand_1) / operand_2))

            else:
                stack.append(int(token))

        return stack[-1]