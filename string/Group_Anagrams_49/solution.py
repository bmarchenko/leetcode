from typing import List

"""
49. Group Anagrams

https://leetcode.com/problems/group-anagrams/
Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:

All inputs will be in lowercase.
The order of your output does not matter.

"""


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for st in strs:
            st_set = tuple(sorted(st))
            if st_set in res:
                res[st_set].append(st)
            else:
                res[st_set] = [st]
        return res.values()
