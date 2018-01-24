"""
Write a function to find the longest common prefix string amongst an array of strings.
"""

def longestCommonPrefix(strs):
    if len(strs) == 0:
        return ''
    cpre = strs[0]
    for onestr in strs[1:]:
        i = 0
        while i < len(cpre) and i < len(onestr) and cpre[i] == onestr[i]:
            i = i + 1
        cpre = cpre[:i]

    return cpre

def main():
	print longestCommonPrefix(["1abc","abcd","ab"])
	print longestCommonPrefix(["abc","abcd","ab"])

if __name__=='__main__':
	main()