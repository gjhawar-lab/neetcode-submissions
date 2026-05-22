class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        seen_map = {}

        for letter in s:
            seen_map[letter] = seen_map.get(letter, 0) + 1

        for letter in t:
            if letter not in seen_map:
                return False
            seen_map[letter] = seen_map.get(letter, 0) - 1

        return all(v == 0 for v in seen_map.values())