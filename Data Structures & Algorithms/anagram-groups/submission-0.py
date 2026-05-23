class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
            result = defaultdict(list)

            for word in strs:
                #sort each word and get sorted chars
                sorted_chars = sorted(word)

                #make it a word again
                sorted_word = "".join(sorted_chars)

                #add it to the dict
                result[sorted_word].append(word)

            return list(result.values())