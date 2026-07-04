class Solution:
    
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagrams = []
        for s in strs:
            sd = {} 
            for i in s:
                sd[i] = sd.get(i,0)+1
            anagrams.append((s,sd))

        # print(anagrams)
        results = []
        unique_anagrams = []
        for i in anagrams:
            within = False
            for j in range(len(results)):
                if unique_anagrams[j] == i[1]:
                    within = True
                    results[j].append(i[0])
                    break
            

            if not within:
                results.append([i[0]])
                unique_anagrams.append(i[1])
        return results 