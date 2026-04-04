def longestCommonPrefix(strs: list[str]) -> str:
    for j in range(len(strs[0])):
        for i in range(1, len(strs)):
            if j >= len(strs[i]) or strs[i][j] != strs[0][j]:
                return strs[0][:j]
    return strs[0]