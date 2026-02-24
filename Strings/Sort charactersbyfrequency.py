class SortCharactersByFrequency:
    def SortByFrequency(self,s):

        freq = {}
        result = []

        for ch in s:
            if ch not in freq:
                freq[ch] = 1
            else:
                freq[ch]+=1

        sorted_char_array = sorted(freq.items(), key=lambda x:(-x[1],x[0]))

        for i in range(len(sorted_char_array)):
            result.append(sorted_char_array[i][0])

        return result
    
a = SortCharactersByFrequency()
b = a.SortByFrequency('trees')
print(b)
        