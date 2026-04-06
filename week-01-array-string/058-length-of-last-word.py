def lengthOfLastWord(s: str) -> int:
    chars = s.split()
    rs = len(chars[-1])
    return rs