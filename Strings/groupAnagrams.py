class Solution(object):
    def groupAnagrams(self, strs):
        
        dicter = {}

        for word in strs:
            key = "".join(sorted(word))

            if key not in dicter:
                dicter[key] = []
            dicter[key].append(word)

        return dicter.values()
        
        