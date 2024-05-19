

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def buildTreeF(self, pre: list[int], ino: list[int]):

        root_val = pre[0]
        ind = ino.index(root_val)

        A = (ind == 0)
        B = (ind == len(ino) - 1)

        if A and B:
            re_ch_ino = []
            re_ch_pre = []
            re_on_ino = []
            re_on_pre = []
            return root_val, re_ch_ino, re_ch_pre, re_on_ino, re_on_pre
        elif A and not B:
            re_ch_ino = []
            re_ch_pre = []
            re_on_ino = ino[1:]
            re_on_pre = pre[1:]
            return root_val, re_ch_ino, re_ch_pre, re_on_ino, re_on_pre
        elif not A and B:
            re_ch_ino = ino[:-1]
            re_ch_pre = pre[1:]
            re_on_ino = []
            re_on_pre = []
            return root_val, re_ch_ino, re_ch_pre, re_on_ino, re_on_pre
        else:
            re_ch_ino = ino[:ind]
            re_ch_pre = pre[1:ind + 1]
            re_on_ino = ino[ind + 1:]
            re_on_pre = pre[ind + 1:]
            return root_val, re_ch_ino, re_ch_pre, re_on_ino, re_on_pre

    def buildTree(self, preorder: list[int], inorder: list[int]):
        def B(pre, ino):
            if not pre:
                return None
            res = self.buildTreeF(pre, ino)
            l = B(res[2], res[1])
            r = B(res[4], res[3])
            return TreeNode(res[0], l, r)
        return B(preorder, inorder)
        

    def minCostClimbingStairs(self, cost: list[int]) -> int:

        i = len(cost)
        cost.append(0)
        
        def f(i, cost, memo={}):
            if i in memo:
                return memo[i]
            if i == 1 or i == 0:
                return cost[i]
            memo[i] = cost[i] + min(f(i - 1, cost), f(i - 2, cost))
            return memo[i]
            
        return f(i, cost)
    
    def minCostClimbingStairs1(self, cost: list[int]) -> int:
        cost.append(0)
        for i in range(len(cost) - 3, -1, -1):
            cost[i] += min(cost[i + 1], cost[i + 2])
        return min(cost[0], cost[1])

	# def minCostClimbingStairs1(self, cost: List[int]) -> int:
	# 	cur = 0 
	# 	dp0 = cost[0]
	# 	if len(cost) >= 2:
	# 		dp1 = cost[1]

	# 	for i in range(2, len(cost)):
	# 		cur = cost[i] + min(dp0, dp1)
	# 		dp0 = dp1
	# 		dp1 = cur

	# 	return min(dp0, dp1)
		

    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if head is None:
            return 
        temp1 = head
        temp2 = head
        if temp1.val != val:
            temp1 = temp1.next
        else:
            temp1 = temp2 = head = temp1.next
        while temp1:
            if temp1.val == val:
                temp1 = temp1.next
            else:
                temp2, temp1 = temp2.next, temp1.next
        return head

    def fib(self, N: int) -> int:
        """25 16.3"""
        dp_0, dp_1 = 0, 1
        for i in range(N):
            dp_0, dp_1 = dp_1, dp_1 + dp_0
        return dp_0
    
    def fib_map(self, n: int, memo={}) -> int:
        """39 16.2"""
        if n in memo:
            return memo[n]
        if n == 0:
            return 0
        if n <= 2:
            return 1
        memo[n] = self.fib_map(n - 1, memo) + self.fib_map(n - 2, memo)
        return memo[n]

    def countMatches(self, items: list[list[str]], ruleKey: str, ruleValue: str) -> int:
        count = 0
        m = {"type": 0, "color": 1, "name": 2}
        for i in items:
            if ruleValue == i[m[ruleKey]]:
                count += 1
        return count
        
    def decompressRLElist(self, nums: list[int]) -> list[int]:
        rel, i = [], 0
        while len(nums) > 2 * i + 1:
            rel += nums[2 * i] * [nums[2 * i + 1]]
            i += 1
        return rel

    def minCostClimbingStairs1(self, cost: list[int]) -> int:
        cur = 0 
        dp0 = cost[0]
        if len(cost) >= 2:
            dp1 = cost[1]

        for i in range(2, len(cost)):
            cur = cost[i] + min(dp0, dp1)
            dp0 = dp1
            dp1 = cur

        return min(dp0, dp1)
    
    def numberOfEmployeesWhoMetTarget(self, hours: list[int], target: int) -> int:
        count = 0
        for i in hours:
            if i >= target:
                count += 1
        return count

    def leftRightDifference(self, nums: list[int]) -> list[int]:
        rs, ls, ans = sum(nums), 0, []
        for i in nums:
            rs -= i 
            ans.append(abs(ls - rs))
            ls += i
        return ans

    def isSubsequence(self, s: str):

        def a(top: set, s: str) -> set:
            res = set()
            for e in top:
                res.add(s + e)
            return {s, *top, *res}
            
        # s --> "ahbgdc"
        uzunlik = len(s) - 1  # uzunlik --> 6
        def f(i, s):
            if i == 1:
                return {s[0], s[1], s[1] + s[0]}
            top = f(i - 1, s)
            return a(top, s[i])
        
        return f(uzunlik, s[::-1])
    
    def maxRepeating(self, sequence: str, word: str) -> int:
        M = [len(sequence) * [0] for _ in range(len(word))]
        

        for index_word, element_word in enumerate(word):

            for index_sequence, element_sequence in enumerate(sequence):
                
                if element_word == element_sequence:
                    M[index_word][index_sequence] = 1
                
        sanagich = 0      
        for index_m, element_m in enumerate(M[0]):
            if element_m == 1:
                i = 0
                j = index_m

                diagonal = []
                while i < len(word) and j < len(sequence):
                    if M[i][j] == 1:
                        diagonal.append(True)
                    else:
                        diagonal.append(False)
                    i += 1
                    j += 1
                if all(diagonal):
                    sanagich += 1
        return sanagich
    

    def fib(self, n: int) -> int:
        if n < 2:
            return n
        return self.fib(n - 1) + self.fib(n - 2)

    # 93
    def restoreIpAddresses(self, s: str) -> list[str]:
        ans = []
        leng = len(s)
        def B(temp, ex, ind):
            if ex==4:
                ans.append(temp[:-1])
                return
            y = leng - ind
            z = (4 - (ex + 1)) * 3
            for x in range(1, 4):
                if (y - x <= z) and (y - x >= 0):
                    a = s[ind:ind+x]
                    b = int(a)
                    if x == 2 and 10 > b:
                        continue
                    if x == 3 and 100 > b:
                        continue
                    if x == 3:
                        if int(a) <= 255:
                            B(temp+a+".",ex+1,ind+x)
                    else:
                        
                        a = s[ind : ind + x]+"."
                        B(temp+a, ex+1,ind+x)
        B("", 0,0)
        return ans
                    
        
        

        

      
        

def main() -> None:
    solution_object = Solution()
    sequence = "aaabaaaabaaabaaaabaaaabaaaabaaaaba"
    word = "aaaba"

    natija = solution_object.maxRepeating(sequence, word)

    print(natija)

if __name__ == "__main__":
    main()
