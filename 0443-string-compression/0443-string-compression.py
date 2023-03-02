class Solution:
    def compress(self, chars: List[str]) -> int:
        s = ""
        i = 0
        j = 1
        s+=chars[i]
        frq = 1
        while j < len(chars):

            if chars[i] == chars[j]:
                frq += 1

            if chars[i]!= chars[j]:
                if frq>1:
                    s+= str(frq)
                i = j
                s+=chars[i]
                frq = 1
            if j == len(chars)-1:
                if frq>1:
                    s+= str(frq)
            j+=1
        chars.clear()
        for _ in s:
            chars.append(_)
        return len(chars)
                