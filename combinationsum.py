from itertools import combinations_with_replacement
class Solution:

    def combinationSum(self, candidates, target):
        possible_combinations = []
        for i in range(1,len(candidates)+8):
            for j in combinations_with_replacement(candidates,i):
                if sum(j)==target:
                    possible_combinations.append(j)      
        return possible_combinations

