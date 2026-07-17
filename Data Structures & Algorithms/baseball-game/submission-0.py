class Solution:
    def calPoints(self, operations: List[str]) -> int:
        records = []
        for i in range(len(operations)):
            val = operations[i]

            if val == "+":
                rec = records[len(records)-1] + records[len(records)-2]
            elif val == "D":
                rec = records[len(records)-1]*2
            elif val == "C":
                records.pop()
                continue
            else:
                rec = int(val)

            records.append(rec)
        
        return sum(records)

        