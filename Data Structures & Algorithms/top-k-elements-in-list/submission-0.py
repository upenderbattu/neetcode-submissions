from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        most_frequent_num = count.most_common(k)
        return [element for element , frequency in most_frequent_num]

