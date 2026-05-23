class Solution:
    #Bucket sort
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dict = {}

        for num in nums:
            freq_dict[num] = freq_dict.get(num, 0) + 1


        buckets = [[] for i in range(len(nums)+1)]   

        for num, count in freq_dict.items():
            buckets[count].append(num)

        result = []
        for i in range(len(buckets)-1, 0, -1):
            for num in buckets[i]:
                result.append(num)

                if len(result) == k:
                    return result

        #sorted_keys = sorted(freq_dict.keys(), key=lambda x: freq_dict[x], reverse=True)
        #return sorted_keys[:k]
