class Solution(object):
    def isAnagram(self, s, t):
        # 1. Quick check: If lengths are different, they can't be anagrams
        if len(s) != len(t):
            return False
            
        char_counts = {}
        
        # 2. Build the tally using the first word 's'
        for char in s:
            if char in char_counts:
                char_counts[char] += 1
            else:
                char_counts[char] = 1
                
        # 3. Subtract from the tally using the second word 't'
        for char in t:
            if char in char_counts:
                char_counts[char] -= 1
            else:
                # If we see a letter in 't' that wasn't in 's', it's not an anagram
                return False
                
        # 4. Final check: If it's a perfect anagram, all counts should be exactly 0
        for count in char_counts.values():
            if count != 0:
                return False
                
        return True