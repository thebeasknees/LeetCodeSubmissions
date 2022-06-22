open_parenthesis = ["[", "{", "(",]
closed_parenthesis = ["]", "}", ")"]

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i in open_parenthesis:
                stack.append(i)
            elif i in closed_parenthesis:
                position = closed_parenthesis.index(i)
                if((len(stack) > 0) and (open_parenthesis[position] == stack[len(stack) - 1])):
                    stack.pop()
                else:
                    return False
        if len(stack) == 0:
            return True
        else:
            return False