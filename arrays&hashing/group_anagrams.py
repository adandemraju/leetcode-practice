'''
Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.
An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

Example 1:
Input: strs = ["act","pots","tops","cat","stop","hat"]
Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]

Example 2:
Input: strs = ["x"]
Output: [["x"]]

Example 3:
Input: strs = [""]
Output: [[""]]
'''

from ast import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #use freq list as key
        #create hashmap for groups of anagrams
        #return tuple

        res = defaultdict(list)

        for s in strs:
            freq = [0] * 26
            for c in s:
                freq[ord(c)-ord('a')] += 1

            res[tuple(freq)].append(s)

        return list(res.values())