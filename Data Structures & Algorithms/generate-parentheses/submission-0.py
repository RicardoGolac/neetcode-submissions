class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []


        def backTrack(openN, closedN):
            if openN == closedN == n: # N = 1, O = 1, C = 1
                res.append("".join(stack))
                return
            if openN < n: # N = 1, O = 0, C = 0
                stack.append("(")
                backTrack(openN + 1, closedN)
                stack.pop()
            if closedN < openN: # N = 1, O = 1, C = 0
                stack.append(")")
                backTrack(openN, closedN + 1)
                stack.pop()

        backTrack(0,0)
        return res
        