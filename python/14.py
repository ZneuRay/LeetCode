class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        if len(strs[0]) == 0:
            return ""
        i = 0
        while i < len(strs[0]):
            c = strs[0][i]
            for j, str in enumerate(strs):
                if len(str) == i:
                    return str[:i]
                if c != str[i]:
                    return str[:i]
            i = i + 1
        return strs[0]