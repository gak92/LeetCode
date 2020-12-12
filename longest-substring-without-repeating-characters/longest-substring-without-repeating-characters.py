class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        win_strt = 0        # initialize start pointer to first character
        win_end = 0         # initialize end pointer to first character
        max_len = 0         # count length of longest substring
        uniq = set()        # create an empty set
​
        while(win_end < len(s)):                    # run loop until reach end of string
            if (s[win_end] not in uniq):            # check current character if not set
                uniq.add(s[win_end])                # add it into set
                max_len = max(max_len, len(uniq))   # get len of set and save maximum one
                win_end +=1                         # move end pointer one character
            else:
                uniq.remove(s[win_strt])            # if character in set then remove it
                win_strt += 1                       # move start pointer one character
​
        return max_len                              # at end return length of longes substring
​
