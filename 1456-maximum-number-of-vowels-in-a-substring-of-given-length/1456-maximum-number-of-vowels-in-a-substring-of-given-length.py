class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        
        vowels = {'a', 'e', 'i', 'o', 'u'}
        count = 0

        # Count vowels in the first window
        for i in range(k):
            if s[i] in vowels:
                count += 1

        ans = count

        # Slide the window
        for i in range(k, len(s)):
            #element that is leaving
            if s[i - k] in vowels:
                count -= 1
            #element that is going to be added up
            if s[i] in vowels:
                count += 1

            ans = max(ans, count)

        return ans