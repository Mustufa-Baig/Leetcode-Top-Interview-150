class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []
        
        word_len = len(words[0])
        num_words = len(words)
        total_len = word_len * num_words
        
        target_counts = {}
        for w in words:
            target_counts[w] = target_counts.get(w, 0) + 1
            
        res = []
        
        for i in range(len(s) - total_len + 1):
            
            seen = {}
            j = 0
            while j < num_words:
                start = i + j * word_len
                word = s[start : start + word_len]
                
                if word not in target_counts:
                    break
                
                seen[word] = seen.get(word, 0) + 1
                
        
                if seen[word] > target_counts[word]:
                    break
                
                j += 1
            
            if j == num_words:
                res.append(i)
                
        return res
