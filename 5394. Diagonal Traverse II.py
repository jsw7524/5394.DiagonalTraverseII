class Solution(object):
    def findDiagonalOrder(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        dictLevel={}
        for row in range(len(nums)):
            for col in range(len(nums[row])):
                if row+col not in dictLevel:
                    dictLevel[row+col]=[nums[row][col]]
                else:
                    dictLevel[row + col].append(nums[row][col])
        answer=[]
        for lvl in dictLevel.items():
            lvl[1].reverse()
            answer+=lvl[1]
        return answer


sln=Solution()
assert [1,4,2,7,5,3,8,6,9]==sln.findDiagonalOrder(nums = [[1,2,3],[4,5,6],[7,8,9]])
assert [1,6,2,8,7,3,9,4,12,10,5,13,11,14,15,16]==sln.findDiagonalOrder(nums = [[1,2,3,4,5],[6,7],[8],[9,10,11],[12,13,14,15,16]])
assert [1,4,2,5,3,8,6,9,7,10,11]==sln.findDiagonalOrder(nums = [[1,2,3],[4],[5,6,7],[8],[9,10,11]])
assert [1,2,3,4,5,6]==sln.findDiagonalOrder(nums = [[1,2,3,4,5,6]])