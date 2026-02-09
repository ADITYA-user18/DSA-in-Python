class RemoveParenthesis:
    def BracketRemover(self,s):
        result = []
        depth = 0

        for ch in s:
            if ch == '(':
                if depth > 0:
                    result.append(ch)
                depth += 1
            else:
                depth -= 1
                if depth > 0:
                    result.append(ch)

        return "".join(result)
    
a = RemoveParenthesis()
b = a.BracketRemover('(()())')
print(b)