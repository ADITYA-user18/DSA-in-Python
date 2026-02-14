class longestPrefixer:
    def LongestPrefixerInArray(self,str):
        n = len(str)

        first = str[0]

        for i in range(1,n):
            while not str[i].startswith(first):
                first = first[:-1]

            if first == "":
                return ""
        return first
    
a = longestPrefixer()
b = a.LongestPrefixerInArray(["flower", "flow", "flight"])
print(b)