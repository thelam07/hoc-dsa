def groupAnagrams(strs: list[str]) -> list[list[str]]:
    d = {}
    for i in strs:
        sorted_str = ''.join(sorted(i))
        if sorted_str in d:
            d[sorted_str].append(i)
        else:
            d[sorted_str] = [i]
    return list(d.values())