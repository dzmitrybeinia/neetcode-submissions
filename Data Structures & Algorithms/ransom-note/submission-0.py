class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        note_freq = [0] * 26
        for ch in ransomNote:
            note_freq[ord(ch) - ord('a')] += 1
        
        magazine_freq = [0] * 26
        for ch in magazine:
            magazine_freq[ord(ch) - ord('a')] += 1
        
        for i in range(0, 26):
            if note_freq[i] > magazine_freq[i]:
                return False
        return True