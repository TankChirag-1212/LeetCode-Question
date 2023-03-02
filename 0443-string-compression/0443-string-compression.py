class Solution:
    def compress(self, chars: List[str]) -> int:
        s = ""
        prev = chars[0]
        prevFreq = 1
        
        for i in range(1, len(chars)):
            if chars[i] == prev:
                prevFreq += 1
                
            else:
                s += prev
                if prevFreq > 1:
                    s += str(prevFreq)
                prev = chars[i]
                prevFreq = 1
            
        s += prev
        if prevFreq > 1:
            s += str(prevFreq)
        
        chars.clear()
        for _ in s:
            chars.append(_)
        return len(chars)
                