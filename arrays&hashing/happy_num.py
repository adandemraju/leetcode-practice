class Solution:
    def isHappy(self, n: int) -> bool:
        #digits keep squaring till the sum = 1
        #ex. 19 => 1^2 + 9^2 = 82
            # 82 => 8^2 + 2^2 = 68
            # 68 => 6^2 + 8^2 = 100
            # 100 => 1^2 + 0^2 + 0^2 = 1
        #loops endlessly
            #if loops endlessly on 1 => happy
            #if loops to prev number not 1 => not happy 
                #basically checking if we hit the same number again => set


        seen = set() #tracks numbers we have seen so far

        while n not in seen and n != 1: #while we dont have a duplicate number
            seen.add(n)
            n = self.sumOfSquares(n)
        
        return n == 1 #ran into duplicate number that was not 1 => unhappy
        
    def sumOfSquares(self, n: int) -> int:
        output = 0
        while n > 0:
            n,digit = divmod(n,10)
            output += digit**2