class Solution:
    def countDigitOne(self, n: int) -> int:
        counter = 0
        learnedUntil = [1]
        pos = 0
        shortcut = [0]
        step = 1
        
        i = 1
        
        while i < n+1:
            if i + step > n+1:
                pos -= 1
                step = learnedUntil[pos]
                continue
            
            num = i//learnedUntil[pos]
            num = str(num)
            for c in num:
                if c == "1":
                    if(i >= 10 and pos > 0):
                        counter += 1 * learnedUntil[pos]
                    else:
                        counter += 1
            if i != n:         
                counter += shortcut[pos]
                
            i += step
            
            if i == learnedUntil[pos]*10:
                shortcut.append(counter)
                learnedUntil.append(learnedUntil[pos]*10)
                pos += 1
                step = learnedUntil[pos]
        return counter    
