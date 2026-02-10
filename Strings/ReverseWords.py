class ReverseOfStrings:
    def StringReverser(self,s):
        words = s.split()
        return " ".join(words[::-1])
    

a = ReverseOfStrings()
b = a.StringReverser('Aditya The Software Developer')
print(b)