class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        res = {}
        for i in range(len(score)):
            count = 0
            for j in range(len(score)):
                if score[i] < score[j] and i!=j:
                    count +=1
                res[score[i]] = count+1

        result = []
        for key,value in res.items():
            if value == 1:
                result.append("Gold Medal")
            elif value == 2:
                result.append("Silver Medal")
            elif value == 3:
                result.append("Bronze Medal")
            else:
                result.append(str(value)) 
        return result                   



        