from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result_dict = defaultdict(list)

        for string in strs:
            character_list = [0] * 26
            for char in string:
                character_list[ord(char) - ord("a")] += 1
            
            key = tuple(character_list)
            result_dict[key].append(string)

        return list(result_dict.values())
    
    
        