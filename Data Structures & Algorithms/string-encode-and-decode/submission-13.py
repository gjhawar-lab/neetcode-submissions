class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join(f"{len(s)}#{s}" for s in strs)

            
    def decode(self, s: str) -> List[str]:
        decoded_list = []
        i = 0

        while i < len(s):
            # find first # from i
            j = s.index("#", i)
            # length is everything before that # till now
            length = int(s[i:j])
            # go to first posn after the #
            i = j+1
            # thats where actual string is
            decoded_list.append(s[i:i+length])
            # move i to the right position
            i += length

        return decoded_list

