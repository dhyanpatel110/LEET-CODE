# LEET_CODE
[![GitHub last commit](https://img.shields.io/github/last-commit/dhyanpatel110/LEET_CODE)](https://github.com/dhyanpatel110/LEET_CODE/commits/master)
[![GitHub repo size](https://img.shields.io/github/repo-size/dhyanpatel110/LEET_CODE)](https://github.com/dhyanpatel110/LEET_CODE/archive/master.zip)


| # | Title | Solution | Difficulty |Basic idea (One line) |
|---| ----- | -------- | ---------- |--------------------- |
| 1 | [Two Sum](https://leetcode.com/problems/two-sum/) | [Python](https://github.com/dhyanpatel110/LEET_CODE/blob/master/python/001_Two_Sum.py)|Easy| |
| 2 | [Add Two Numbers](https://leetcode.com/problems/add-two-numbers/) | [Python](https://github.com/dhyanpatel110/LEET_CODE/blob/master/python/002_Add_Two_Numbers.py)|Medium | |
| 3 | [Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/) | [Python](https://github.com/qiyuangong/leetcode/blob/master/python/003_Longest_Substring_Without_Repeating_Characters.py)| Medium | |
| 4 | [Median of Two Sorted Arrays](https://leetcode.com/problems/median-of-two-sorted-arrays/) | [Python](https://github.com/qiyuangong/leetcode/blob/master/python/004_Median_of_Two_Sorted_Arrays.py)|	Hard | |
| 5 | [Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/) | [Python](https://github.com/qiyuangong/leetcode/blob/master/python/005_Longest_Palindromic_Substring.py)|	Medium | |
| 6 | [Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/) | [Python](https://github.com/qiyuangong/leetcode/blob/master/python/005_Longest_Palindromic_Substring.py) [Java](https://github.com/qiyuangong/leetcode/blob/master/java/005_Longest_Palindromic_Substring.java) | [Background knowledge](http://en.wikipedia.org/wiki/Longest_palindromic_substring)<br>1. DP if s[i]==s[j] and P[i+1, j-1] then P[i,j]<br>2. A palindrome can be expanded from its center<br>3. Manacher algorithm|
| 7 | [Reverse Integer](https://leetcode.com/problems/reverse-integer/) | [Python](https://github.com/qiyuangong/leetcode/blob/master/python/007_Reverse_Integer.py) [Java](https://github.com/qiyuangong/leetcode/blob/master/java/007_Reverse_Integer.java) | Overflow when the result is greater than 2147483647 or less than -2147483648.
| 8 | [String to Integer (atoi)](https://leetcode.com/problems/string-to-integer-atoi/) | [Python](https://github.com/qiyuangong/leetcode/blob/master/python/008_String_to_Integer(atoi).py) [Java](https://github.com/qiyuangong/leetcode/blob/master/java/008_String_to_Integer(atoi).java) | Overflow, Space, and negative number |
| 9 | [Palindrome Number](https://leetcode.com/problems/palindrome-number/) | [Python](https://github.com/qiyuangong/leetcode/blob/master/python/009_Palindrome_Number.py) [Java](https://github.com/qiyuangong/leetcode/blob/master/java/009_Palindrome_Number.java) | Get the len and check left and right with 10^len, 10 |
| 10 | [Palindrome Number](https://leetcode.com/problems/palindrome-number/) | [Python](https://github.com/qiyuangong/leetcode/blob/master/python/009_Palindrome_Number.py) [Java](https://github.com/qiyuangong/leetcode/blob/master/java/009_Palindrome_Number.java) | Get the len and check left and right with 10^len, 10 |
| 11 | [Container With Most Water](https://leetcode.com/problems/container-with-most-water/) | [Python](https://github.com/qiyuangong/leetcode/blob/master/python/011_Container_With_Most_Water.py) [Java](https://github.com/qiyuangong/leetcode/blob/master/java/011_Container_With_Most_Water.java) | 1. Brute Force, O(n^2) and O(1)<br>2. Two points, O(n) and O(1)  |
| 12 | [Integer to Roman](https://leetcode.com/problems/integer-to-roman/) | [Python](https://github.com/qiyuangong/leetcode/blob/master/python/012_Integer_to_Roman.py) [Java](https://github.com/qiyuangong/leetcode/blob/master/java/012_Integer_to_Roman.java) | [Background knowledge](http://www.rapidtables.com/convert/number/how-number-to-roman-numerals.htm) Just like 10-digit number, divide and minus |
| 13 | [Roman to Integer](https://leetcode.com/problems/roman-to-integer/) | [Python](https://github.com/qiyuangong/leetcode/blob/master/python/013_Roman_to_Integer.py) | Add all curr, if curr > prev, then need to subtract 2 * prev |
| 14 | [Palindrome Number](https://leetcode.com/problems/palindrome-number/) | [Python](https://github.com/qiyuangong/leetcode/blob/master/python/009_Palindrome_Number.py) [Java](https://github.com/qiyuangong/leetcode/blob/master/java/009_Palindrome_Number.java) | Get the len and check left and right with 10^len, 10 |
| 15 | [3Sum](https://leetcode.com/problems/3sum/) | [Python](https://github.com/qiyuangong/leetcode/blob/master/python/015_3Sum.py) | 1. Sort and O(n^2) search with three points <br>2. Multiple Two Sum (Problem 1) |
| 16 | [3Sum Closest](https://leetcode.com/problems/3sum-closest/) | [Python](https://github.com/qiyuangong/leetcode/blob/master/python/016_3Sum_Closest.py) | Sort and Multiple Two Sum check abs|
| 17 | [Palindrome Number](https://leetcode.com/problems/palindrome-number/) | [Python](https://github.com/qiyuangong/leetcode/blob/master/python/009_Palindrome_Number.py) [Java](https://github.com/qiyuangong/leetcode/blob/master/java/009_Palindrome_Number.java) | Get the len and check left and right with 10^len, 10 |
| 18 | [4Sum](https://leetcode.com/problems/4sum/) | [Python](https://github.com/qiyuangong/leetcode/blob/master/python/018_4Sum.py) | The same as 3Sum, but we can merge pairs with the same sum |
| 19 | [Remove Nth Node From End of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list/) | [Python](https://github.com/qiyuangong/leetcode/blob/master/python/019_Remove_Nth_Node_From_End_of_List.py) [Java](https://github.com/qiyuangong/leetcode/blob/master/java/019_Remove_Nth_Node_From_End_of_List.java) | 1. Go through list and get length, then remove length-n, O(n) and O(n)<br>2. Two pointers, first pointer goes to n position, then move both pointers until reach tail, O(n) and O(n) |
| 20 | [Valid Parentheses](https://leetcode.com/problems/valid-parentheses/) | [Python](https://github.com/qiyuangong/leetcode/blob/master/python/020_Valid_Parentheses.py) | 1. Stack<br>2. Replace all parentheses with '', if empty then True |
| 21 | [Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/) | [Python](https://github.com/qiyuangong/leetcode/blob/master/python/021_Merge_Two_Sorted_Lists.py) | Add a dummy head, then merge two sorted list in O(m+n) |
| 22 | [Palindrome Number](https://leetcode.com/problems/palindrome-number/) | [Python](https://github.com/qiyuangong/leetcode/blob/master/python/009_Palindrome_Number.py) [Java](https://github.com/qiyuangong/leetcode/blob/master/java/009_Palindrome_Number.java) | Get the len and check left and right with 10^len, 10 |
| 23 | [Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/) | [Python](https://github.com/qiyuangong/leetcode/blob/master/python/023_Merge_k_Sorted_Lists.py) | 1. Priority queue O(nk log k)<br>2. Binary merge O(nk log k)|  |
| 24 | [Swap Nodes in Pairs](https://leetcode.com/problems/swap-nodes-in-pairs/) | [Python](https://github.com/qiyuangong/leetcode/blob/master/python/024_Swap_Nodes_in_Pairs.py) | Add a dummy and store the prev |
| 25 | [Palindrome Number](https://leetcode.com/problems/palindrome-number/) | [Python](https://github.com/qiyuangong/leetcode/blob/master/python/009_Palindrome_Number.py) [Java](https://github.com/qiyuangong/leetcode/blob/master/java/009_Palindrome_Number.java) | Get the len and check left and right with 10^len, 10 |
| 26 | [Palindrome Number](https://leetcode.com/problems/palindrome-number/) | [Python](https://github.com/qiyuangong/leetcode/blob/master/python/009_Palindrome_Number.py) [Java](https://github.com/qiyuangong/leetcode/blob/master/java/009_Palindrome_Number.java) | Get the len and check left and right with 10^len, 10 |
| 27 | [Palindrome Number](https://leetcode.com/problems/palindrome-number/) | [Python](https://github.com/qiyuangong/leetcode/blob/master/python/009_Palindrome_Number.py) [Java](https://github.com/qiyuangong/leetcode/blob/master/java/009_Palindrome_Number.java) | Get the len and check left and right with 10^len, 10 |
| 28 | [Implement strStr()](https://leetcode.com/problems/implement-strstr/) | [Python](https://github.com/qiyuangong/leetcode/blob/master/python/028_Implement_strStr().py) | 1. O(nm) comparison <br>2. KMP |
| 29 | [Palindrome Number](https://leetcode.com/problems/palindrome-number/) | [Python](https://github.com/qiyuangong/leetcode/blob/master/python/009_Palindrome_Number.py) [Java](https://github.com/qiyuangong/leetcode/blob/master/java/009_Palindrome_Number.java) | Get the len and check left and right with 10^len, 10 |
| 30 | [Palindrome Number](https://leetcode.com/problems/palindrome-number/) | [Python](https://github.com/qiyuangong/leetcode/blob/master/python/009_Palindrome_Number.py) [Java](https://github.com/qiyuangong/leetcode/blob/master/java/009_Palindrome_Number.java) | Get the len and check left and right with 10^len, 10 |
| 31 | [Palindrome Number](https://leetcode.com/problems/palindrome-number/) | [Python](https://github.com/qiyuangong/leetcode/blob/master/python/009_Palindrome_Number.py) [Java](https://github.com/qiyuangong/leetcode/blob/master/java/009_Palindrome_Number.java) | Get the len and check left and right with 10^len, 10 |
| 32 | [Palindrome Number](https://leetcode.com/problems/palindrome-number/) | [Python](https://github.com/qiyuangong/leetcode/blob/master/python/009_Palindrome_Number.py) [Java](https://github.com/qiyuangong/leetcode/blob/master/java/009_Palindrome_Number.java) | Get the len and check left and right with 10^len, 10 |
| 33 | [Palindrome Number](https://leetcode.com/problems/palindrome-number/) | [Python](https://github.com/qiyuangong/leetcode/blob/master/python/009_Palindrome_Number.py) [Java](https://github.com/qiyuangong/leetcode/blob/master/java/009_Palindrome_Number.java) | Get the len and check left and right with 10^len, 10 |
| 34 | [Palindrome Number](https://leetcode.com/problems/palindrome-number/) | [Python](https://github.com/qiyuangong/leetcode/blob/master/python/009_Palindrome_Number.py) [Java](https://github.com/qiyuangong/leetcode/blob/master/java/009_Palindrome_Number.java) | Get the len and check left and right with 10^len, 10 |
| 35 | [Search Insert Position](https://leetcode.com/problems/search-insert-position/) | [Python](https://github.com/qiyuangong/leetcode/blob/master/python/035_Search_Insert_Position.py) | Binary Search |
| 36 | [Palindrome Number](https://leetcode.com/problems/palindrome-number/) | [Python](https://github.com/qiyuangong/leetcode/blob/master/python/009_Palindrome_Number.py) [Java](https://github.com/qiyuangong/leetcode/blob/master/java/009_Palindrome_Number.java) | Get the len and check left and right with 10^len, 10 |
| 37 | [Palindrome Number](https://leetcode.com/problems/palindrome-number/) | [Python](https://github.com/qiyuangong/leetcode/blob/master/python/009_Palindrome_Number.py) [Java](https://github.com/qiyuangong/leetcode/blob/master/java/009_Palindrome_Number.java) | Get the len and check left and right with 10^len, 10 |
| 38 | [Palindrome Number](https://leetcode.com/problems/palindrome-number/) | [Python](https://github.com/qiyuangong/leetcode/blob/master/python/009_Palindrome_Number.py) [Java](https://github.com/qiyuangong/leetcode/blob/master/java/009_Palindrome_Number.java) | Get the len and check left and right with 10^len, 10 |
| 39 | [Palindrome Number](https://leetcode.com/problems/palindrome-number/) | [Python](https://github.com/qiyuangong/leetcode/blob/master/python/009_Palindrome_Number.py) [Java](https://github.com/qiyuangong/leetcode/blob/master/java/009_Palindrome_Number.java) | Get the len and check left and right with 10^len, 10 |
| 40 | [Palindrome Number](https://leetcode.com/problems/palindrome-number/) | [Python](https://github.com/qiyuangong/leetcode/blob/master/python/009_Palindrome_Number.py) [Java](https://github.com/qiyuangong/leetcode/blob/master/java/009_Palindrome_Number.java) | Get the len and check left and right with 10^len, 10 |
| 41 | [Palindrome Number](https://leetcode.com/problems/palindrome-number/) | [Python](https://github.com/qiyuangong/leetcode/blob/master/python/009_Palindrome_Number.py) [Java](https://github.com/qiyuangong/leetcode/blob/master/java/009_Palindrome_Number.java) | Get the len and check left and right with 10^len, 10 |
| 42 | [Palindrome Number](https://leetcode.com/problems/palindrome-number/) | [Python](https://github.com/qiyuangong/leetcode/blob/master/python/009_Palindrome_Number.py) [Java](https://github.com/qiyuangong/leetcode/blob/master/java/009_Palindrome_Number.java) | Get the len and check left and right with 10^len, 10 |
| 43 | [Palindrome Number](https://leetcode.com/problems/palindrome-number/) | [Python](https://github.com/qiyuangong/leetcode/blob/master/python/009_Palindrome_Number.py) [Java](https://github.com/qiyuangong/leetcode/blob/master/java/009_Palindrome_Number.java) | Get the len and check left and right with 10^len, 10 |
| 44 | [Palindrome Number](https://leetcode.com/problems/palindrome-number/) | [Python](https://github.com/qiyuangong/leetcode/blob/master/python/009_Palindrome_Number.py) [Java](https://github.com/qiyuangong/leetcode/blob/master/java/009_Palindrome_Number.java) | Get the len and check left and right with 10^len, 10 |
| 45 | [Palindrome Number](https://leetcode.com/problems/palindrome-number/) | [Python](https://github.com/qiyuangong/leetcode/blob/master/python/009_Palindrome_Number.py) [Java](https://github.com/qiyuangong/leetcode/blob/master/java/009_Palindrome_Number.java) | Get the len and check left and right with 10^len, 10 |
| 46 | [Permutations](https://leetcode.com/problems/permutations/) | [Python](https://github.com/qiyuangong/leetcode/blob/master/python/046_Permutations.py) | 1. Python itertools.permutations<br>2. DFS with swapping, O(n^2) and O(n^2)<br>3. iteratively generate n-permutations with (n-1)-permutations, O(n^3) and O(n^2) |
| 47 | [Permutations II](https://leetcode.com/problems/permutations-ii/) | [Python](https://github.com/qiyuangong/leetcode/blob/master/python/047_Permutations_II.py) | 1. DFS with swapping, check duplicate, O(n^2) and O(n^2)<br>2. iteratively generate n-permutations with (n-1)-permutations, O(n^3) and O(n^2) |
| 48 | [Palindrome Number](https://leetcode.com/problems/palindrome-number/) | [Python](https://github.com/qiyuangong/leetcode/blob/master/python/009_Palindrome_Number.py) [Java](https://github.com/qiyuangong/leetcode/blob/master/java/009_Palindrome_Number.java) | Get the len and check left and right with 10^len, 10 |
| 49 | [Palindrome Number](https://leetcode.com/problems/palindrome-number/) | [Python](https://github.com/qiyuangong/leetcode/blob/master/python/009_Palindrome_Number.py) [Java](https://github.com/qiyuangong/leetcode/blob/master/java/009_Palindrome_Number.java) | Get the len and check left and right with 10^len, 10 |
| 50 | [Palindrome Number](https://leetcode.com/problems/palindrome-number/) | [Python](https://github.com/qiyuangong/leetcode/blob/master/python/009_Palindrome_Number.py) [Java](https://github.com/qiyuangong/leetcode/blob/master/java/009_Palindrome_Number.java) | Get the len and check left and right with 10^len, 10 |
| 51 | [Palindrome Number](https://leetcode.com/problems/palindrome-number/) | [Python](https://github.com/qiyuangong/leetcode/blob/master/python/009_Palindrome_Number.py) [Java](https://github.com/qiyuangong/leetcode/blob/master/java/009_Palindrome_Number.java) | Get the len and check left and right with 10^len, 10 |
| 52 | [Palindrome Number](https://leetcode.com/problems/palindrome-number/) | [Python](https://github.com/qiyuangong/leetcode/blob/master/python/009_Palindrome_Number.py) [Java](https://github.com/qiyuangong/leetcode/blob/master/java/009_Palindrome_Number.java) | Get the len and check left and right with 10^len, 10 |
| 53 | [Maximum Subarray](https://leetcode.com/problems/maximum-subarray/) | [Python](https://github.com/qiyuangong/leetcode/blob/master/python/053_Maximum_Subarray.py) | 1. Recursion, O(nlgn), O(lgn)<br> 2. Bottom-up DP, O(n) and O(n)<br>3. Bottom-up DP, f(x) = max(f(x-1)+A[x], A[x]), f(x) = max(f(x-1)+A[x], A[x]),O(n) and O(1) |
| 54 | [Spiral Matrix](https://leetcode.com/problems/spiral-matrix/) | [Python](https://github.com/qiyuangong/leetcode/blob/master/python/054_Spiral_Matrix.py) | O(nm) 1. Turn in the corner and loop<br>2. (0, 1) -> (1, 0) -> (0, -1) -> (-1, 0) |
| 55 | [Palindrome Number](https://leetcode.com/problems/palindrome-number/) | [Python](https://github.com/qiyuangong/leetcode/blob/master/python/009_Palindrome_Number.py) [Java](https://github.com/qiyuangong/leetcode/blob/master/java/009_Palindrome_Number.java) | Get the len and check left and right with 10^len, 10 |
| 56 | [Palindrome Number](https://leetcode.com/problems/palindrome-number/) | [Python](https://github.com/qiyuangong/leetcode/blob/master/python/009_Palindrome_Number.py) [Java](https://github.com/qiyuangong/leetcode/blob/master/java/009_Palindrome_Number.java) | Get the len and check left and right with 10^len, 10 |
| 57 | [Palindrome Number](https://leetcode.com/problems/palindrome-number/) | [Python](https://github.com/qiyuangong/leetcode/blob/master/python/009_Palindrome_Number.py) [Java](https://github.com/qiyuangong/leetcode/blob/master/java/009_Palindrome_Number.java) | Get the len and check left and right with 10^len, 10 |
| 58 | [Palindrome Number](https://leetcode.com/problems/palindrome-number/) | [Python](https://github.com/qiyuangong/leetcode/blob/master/python/009_Palindrome_Number.py) [Java](https://github.com/qiyuangong/leetcode/blob/master/java/009_Palindrome_Number.java) | Get the len and check left and right with 10^len, 10 |
| 59 | [Palindrome Number](https://leetcode.com/problems/palindrome-number/) | [Python](https://github.com/qiyuangong/leetcode/blob/master/python/009_Palindrome_Number.py) [Java](https://github.com/qiyuangong/leetcode/blob/master/java/009_Palindrome_Number.java) | Get the len and check left and right with 10^len, 10 |
| 60 | [Palindrome Number](https://leetcode.com/problems/palindrome-number/) | [Python](https://github.com/qiyuangong/leetcode/blob/master/python/009_Palindrome_Number.py) [Java](https://github.com/qiyuangong/leetcode/blob/master/java/009_Palindrome_Number.java) | Get the len and check left and right with 10^len, 10 |
| 61 | [Palindrome Number](https://leetcode.com/problems/palindrome-number/) | [Python](https://github.com/qiyuangong/leetcode/blob/master/python/009_Palindrome_Number.py) [Java](https://github.com/qiyuangong/leetcode/blob/master/java/009_Palindrome_Number.java) | Get the len and check left and right with 10^len, 10 |
| 62 | [Unique Paths](https://leetcode.com/problems/unique-paths/) | [Python](https://github.com/qiyuangong/leetcode/blob/master/python/062_Unique_Paths.py) | 1. Bottom-up DP, dp[i][j] = dmap[i-1][j] + dmap[i][j-1], O(mn) and O(mn)<br>2. Combination (m+n-2, m-1) |
| 63 | [Unique Paths II](https://leetcode.com/problems/unique-paths-ii/) | [Python](https://github.com/qiyuangong/leetcode/blob/master/python/063_Unique_Paths_II.py) | Bottom-up DP, dp[i][j] = dmap[i-1][j] + dmap[i][j-1] (if block, then 0), O(mn) and O(mn) |
| 64 | [Palindrome Number](https://leetcode.com/problems/palindrome-number/) | [Python](https://github.com/qiyuangong/leetcode/blob/master/python/009_Palindrome_Number.py) [Java](https://github.com/qiyuangong/leetcode/blob/master/java/009_Palindrome_Number.java) | Get the len and check left and right with 10^len, 10 |
| 65 | [Valid Number](https://leetcode.com/problems/valid-number/) | [Python](https://github.com/qiyuangong/leetcode/blob/master/python/065_Valid_Number.py) | 1. strip leading and tailing space, then check float using exception, check e using split <br>2. check is number split by . or e, note that number after e may be negative |
| 66 | [Plus One](https://leetcode.com/problems/plus-one/) | [Python](https://github.com/qiyuangong/leetcode/blob/master/python/066_Plus_One.py) | Check if current digit == 9. |
| 67 | [Palindrome Number](https://leetcode.com/problems/palindrome-number/) | [Python](https://github.com/qiyuangong/leetcode/blob/master/python/009_Palindrome_Number.py) [Java](https://github.com/qiyuangong/leetcode/blob/master/java/009_Palindrome_Number.java) | Get the len and check left and right with 10^len, 10 |
| 68 | [Palindrome Number](https://leetcode.com/problems/palindrome-number/) | [Python](https://github.com/qiyuangong/leetcode/blob/master/python/009_Palindrome_Number.py) [Java](https://github.com/qiyuangong/leetcode/blob/master/java/009_Palindrome_Number.java) | Get the len and check left and right with 10^len, 10 |
| 69 | [Palindrome Number](https://leetcode.com/problems/palindrome-number/) | [Python](https://github.com/qiyuangong/leetcode/blob/master/python/009_Palindrome_Number.py) [Java](https://github.com/qiyuangong/leetcode/blob/master/java/009_Palindrome_Number.java) | Get the len and check left and right with 10^len, 10 |
| 70 | [Climbing Stairs](https://leetcode.com/problems/climbing-stairs/) | [Python](https://github.com/qiyuangong/leetcode/blob/master/python/070_Climbing_Stairs.py) | Bottom-up DP, dp[i] = dp[i - 2] + dp[i- 1] <br>1. O(n) and O(n)<br>2. Only two variables are needed, O(n) and O(1) |
| 71 | [Palindrome Number](https://leetcode.com/problems/palindrome-number/) | [Python](https://github.com/qiyuangong/leetcode/blob/master/python/009_Palindrome_Number.py) [Java](https://github.com/qiyuangong/leetcode/blob/master/java/009_Palindrome_Number.java) | Get the len and check left and right with 10^len, 10 |
| 72 | [Edit Distance](https://leetcode.com/problems/edit-distance/) | [Python](https://github.com/qiyuangong/leetcode/blob/master/python/072_Edit_Distance.py) | [Background](https://en.wikipedia.org/wiki/Edit_distance)<br> 1. DP O(n^2) space<br>2. DP O(n) space |
| 73 | [Palindrome Number](https://leetcode.com/problems/palindrome-number/) | [Python](https://github.com/qiyuangong/leetcode/blob/master/python/009_Palindrome_Number.py) [Java](https://github.com/qiyuangong/leetcode/blob/master/java/009_Palindrome_Number.java) | Get the len and check left and right with 10^len, 10 |
| 74 | [Palindrome Number](https://leetcode.com/problems/palindrome-number/) | [Python](https://github.com/qiyuangong/leetcode/blob/master/python/009_Palindrome_Number.py) [Java](https://github.com/qiyuangong/leetcode/blob/master/java/009_Palindrome_Number.java) | Get the len and check left and right with 10^len, 10 |
| 75 | [Palindrome Number](https://leetcode.com/problems/palindrome-number/) | [Python](https://github.com/qiyuangong/leetcode/blob/master/python/009_Palindrome_Number.py) [Java](https://github.com/qiyuangong/leetcode/blob/master/java/009_Palindrome_Number.java) | Get the len and check left and right with 10^len, 10 |
| 76 | [Palindrome Number](https://leetcode.com/problems/palindrome-number/) | [Python](https://github.com/qiyuangong/leetcode/blob/master/python/009_Palindrome_Number.py) [Java](https://github.com/qiyuangong/leetcode/blob/master/java/009_Palindrome_Number.java) | Get the len and check left and right with 10^len, 10 |
| 77 | [Palindrome Number](https://leetcode.com/problems/palindrome-number/) | [Python](https://github.com/qiyuangong/leetcode/blob/master/python/009_Palindrome_Number.py) [Java](https://github.com/qiyuangong/leetcode/blob/master/java/009_Palindrome_Number.java) | Get the len and check left and right with 10^len, 10 |
| 78 | [Subsets](https://leetcode.com/problems/subsets/) | [Python](https://github.com/qiyuangong/leetcode/blob/master/python/078_Subsets.py) | 1. DFS Recursion, O(2^n) and O(2^n)<br>2. Recursion on a binary number, O(2^n) and O(2^n)<br>3. Sort and iteratively generate n subset with n-1 subset, O(n^2) and O(2^n)|
| 79 | [Palindrome Number](https://leetcode.com/problems/palindrome-number/) | [Python](https://github.com/qiyuangong/leetcode/blob/master/python/009_Palindrome_Number.py) [Java](https://github.com/qiyuangong/leetcode/blob/master/java/009_Palindrome_Number.java) | Get the len and check left and right with 10^len, 10 |
| 80 | [Palindrome Number](https://leetcode.com/problems/palindrome-number/) | [Python](https://github.com/qiyuangong/leetcode/blob/master/python/009_Palindrome_Number.py) [Java](https://github.com/qiyuangong/leetcode/blob/master/java/009_Palindrome_Number.java) | Get the len and check left and right with 10^len, 10 |
| 81 | [Palindrome Number](https://leetcode.com/problems/palindrome-number/) | [Python](https://github.com/qiyuangong/leetcode/blob/master/python/009_Palindrome_Number.py) [Java](https://github.com/qiyuangong/leetcode/blob/master/java/009_Palindrome_Number.java) | Get the len and check left and right with 10^len, 10 |
| 82 | [Palindrome Number](https://leetcode.com/problems/palindrome-number/) | [Python](https://github.com/qiyuangong/leetcode/blob/master/python/009_Palindrome_Number.py) [Java](https://github.com/qiyuangong/leetcode/blob/master/java/009_Palindrome_Number.java) | Get the len and check left and right with 10^len, 10 |
| 83 | [Palindrome Number](https://leetcode.com/problems/palindrome-number/) | [Python](https://github.com/qiyuangong/leetcode/blob/master/python/009_Palindrome_Number.py) [Java](https://github.com/qiyuangong/leetcode/blob/master/java/009_Palindrome_Number.java) | Get the len and check left and right with 10^len, 10 |
| 84 | [Palindrome Number](https://leetcode.com/problems/palindrome-number/) | [Python](https://github.com/qiyuangong/leetcode/blob/master/python/009_Palindrome_Number.py) [Java](https://github.com/qiyuangong/leetcode/blob/master/java/009_Palindrome_Number.java) | Get the len and check left and right with 10^len, 10 |
| 85 | [Palindrome Number](https://leetcode.com/problems/palindrome-number/) | [Python](https://github.com/qiyuangong/leetcode/blob/master/python/009_Palindrome_Number.py) [Java](https://github.com/qiyuangong/leetcode/blob/master/java/009_Palindrome_Number.java) | Get the len and check left and right with 10^len, 10 |
| 86 | [Palindrome Number](https://leetcode.com/problems/palindrome-number/) | [Python](https://github.com/qiyuangong/leetcode/blob/master/python/009_Palindrome_Number.py) [Java](https://github.com/qiyuangong/leetcode/blob/master/java/009_Palindrome_Number.java) | Get the len and check left and right with 10^len, 10 |
| 87 | [Palindrome Number](https://leetcode.com/problems/palindrome-number/) | [Python](https://github.com/qiyuangong/leetcode/blob/master/python/009_Palindrome_Number.py) [Java](https://github.com/qiyuangong/leetcode/blob/master/java/009_Palindrome_Number.java) | Get the len and check left and right with 10^len, 10 |
| 88 | [Palindrome Number](https://leetcode.com/problems/palindrome-number/) | [Python](https://github.com/qiyuangong/leetcode/blob/master/python/009_Palindrome_Number.py) [Java](https://github.com/qiyuangong/leetcode/blob/master/java/009_Palindrome_Number.java) | Get the len and check left and right with 10^len, 10 |
| 89 | [Palindrome Number](https://leetcode.com/problems/palindrome-number/) | [Python](https://github.com/qiyuangong/leetcode/blob/master/python/009_Palindrome_Number.py) [Java](https://github.com/qiyuangong/leetcode/blob/master/java/009_Palindrome_Number.java) | Get the len and check left and right with 10^len, 10 |
| 90 | [Subsets II](https://leetcode.com/problems/subsets-ii/) | [Python](https://github.com/qiyuangong/leetcode/blob/master/python/090_Subsets_II.py) | 1. DFS Recursion with duplicate check, O(2^n) and O(2^n)<br>2. Recursion on a binary number, O(2^n) and O(2^n)<br>3. Sort and iteratively generate n subset with n-1 subset, note that if nums[index] == nums[index - 1] then generate from last end to curr end, O(n^2) and O(2^n) |
| 91 | [Subsets II](https://leetcode.com/problems/subsets-ii/) | [Python](https://github.com/qiyuangong/leetcode/blob/master/python/090_Subsets_II.py) | 1. DFS Recursion with duplicate check, O(2^n) and O(2^n)<br>2. Recursion on a binary number, O(2^n) and O(2^n)<br>3. Sort and iteratively generate n subset with n-1 subset, note that if nums[index] == nums[index - 1] then generate from last end to curr end, O(n^2) and O(2^n) |
| 92 | [Subsets II](https://leetcode.com/problems/subsets-ii/) | [Python](https://github.com/qiyuangong/leetcode/blob/master/python/090_Subsets_II.py) | 1. DFS Recursion with duplicate check, O(2^n) and O(2^n)<br>2. Recursion on a binary number, O(2^n) and O(2^n)<br>3. Sort and iteratively generate n subset with n-1 subset, note that if nums[index] == nums[index - 1] then generate from last end to curr end, O(n^2) and O(2^n) |
| 93 | [Subsets II](https://leetcode.com/problems/subsets-ii/) | [Python](https://github.com/qiyuangong/leetcode/blob/master/python/090_Subsets_II.py) | 1. DFS Recursion with duplicate check, O(2^n) and O(2^n)<br>2. Recursion on a binary number, O(2^n) and O(2^n)<br>3. Sort and iteratively generate n subset with n-1 subset, note that if nums[index] == nums[index - 1] then generate from last end to curr end, O(n^2) and O(2^n) |
| 94 | [Binary Tree Inorder Traversal](https://leetcode.com/problems/binary-tree-inorder-traversal/) | [Python](https://github.com/qiyuangong/leetcode/blob/master/python/094_Binary_Tree_Inorder_Traversal.py) | 1. Recursion, O(n) and O(1)<br>2. Stack and check isinstance(curr, TreeNode), O(n) and O(n)<br>3. Stack and check left and right, O(n) and O(n) |
| 95 | [Subsets II](https://leetcode.com/problems/subsets-ii/) | [Python](https://github.com/qiyuangong/leetcode/blob/master/python/090_Subsets_II.py) | 1. DFS Recursion with duplicate check, O(2^n) and O(2^n)<br>2. Recursion on a binary number, O(2^n) and O(2^n)<br>3. Sort and iteratively generate n subset with n-1 subset, note that if nums[index] == nums[index - 1] then generate from last end to curr end, O(n^2) and O(2^n) |
| 96 | [Subsets II](https://leetcode.com/problems/subsets-ii/) | [Python](https://github.com/qiyuangong/leetcode/blob/master/python/090_Subsets_II.py) | 1. DFS Recursion with duplicate check, O(2^n) and O(2^n)<br>2. Recursion on a binary number, O(2^n) and O(2^n)<br>3. Sort and iteratively generate n subset with n-1 subset, note that if nums[index] == nums[index - 1] then generate from last end to curr end, O(n^2) and O(2^n) |
| 97 | [Subsets II](https://leetcode.com/problems/subsets-ii/) | [Python](https://github.com/qiyuangong/leetcode/blob/master/python/090_Subsets_II.py) | 1. DFS Recursion with duplicate check, O(2^n) and O(2^n)<br>2. Recursion on a binary number, O(2^n) and O(2^n)<br>3. Sort and iteratively generate n subset with n-1 subset, note that if nums[index] == nums[index - 1] then generate from last end to curr end, O(n^2) and O(2^n) |
| 98 | [Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/) | [Python](https://github.com/qiyuangong/leetcode/blob/master/python/098_Validate_Binary_Search_Tree.py) | 1. Stack O(n) and O(n)<br>2. Recursion O(n) and O(n) |
| 99 | [Subsets II](https://leetcode.com/problems/subsets-ii/) | [Python](https://github.com/qiyuangong/leetcode/blob/master/python/090_Subsets_II.py) | 1. DFS Recursion with duplicate check, O(2^n) and O(2^n)<br>2. Recursion on a binary number, O(2^n) and O(2^n)<br>3. Sort and iteratively generate n subset with n-1 subset, note that if nums[index] == nums[index - 1] then generate from last end to curr end, O(n^2) and O(2^n) |
| 100 | [Subsets II](https://leetcode.com/problems/subsets-ii/) | [Python](https://github.com/qiyuangong/leetcode/blob/master/python/090_Subsets_II.py) | 1. DFS Recursion with duplicate check, O(2^n) and O(2^n)<br>2. Recursion on a binary number, O(2^n) and O(2^n)<br>3. Sort and iteratively generate n subset with n-1 subset, note that if nums[index] == nums[index - 1] then generate from last end to curr end, O(n^2) and O(2^n) |
