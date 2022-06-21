class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        
        curr_str = strs[0]
        for i in range(1, len(strs)):
            temp_str = ""
            if len(curr_str) == 0:
                break
            for j in range(len(strs[i])):
                if j < len(curr_str) and curr_str[j] == strs[i][j]:
                    temp_str += curr_str[j]
                else:
                    break
            curr_str = temp_str
        return curr_str