class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        score_sort = sorted(score, reverse = True)
        fin = []
        for i in range(len(score)):
            if score[i] == score_sort[0]:
                fin.append("Gold Medal")
            elif score[i] == score_sort[1]:
                fin.append("Silver Medal")
            elif score[i] == score_sort[2]:
                fin.append("Bronze Medal")
            else:
                fin.append(str(score_sort.index(score[i]) + 1))
        return fin