class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen_map = {}

        for letter in s:
            if letter in seen_map:
                seen_map[letter] = seen_map[letter] + 1
            else:
                seen_map[letter] = 1

        for letter in t:
            if letter not in seen_map:
                return False
            seen_map[letter] = seen_map[letter] - 1

        return all(v == 0 for v in seen_map.values())