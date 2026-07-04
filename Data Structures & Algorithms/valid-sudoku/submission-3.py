class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [x for x in board]
        columns = [[x[i] for x in board] for i in range(len(board))]
        boxes = []
        for i in range(0,8,3):
            for j in range(0,8,3):
                box = [board[_][i:i+3] for _ in range(j,j+3)]
                box[0].extend(box[1])
                box[0].extend(box[2])
                boxes.append(box[0])
        # print(boxes)
        rows.extend(columns)
        rows.extend(boxes)
        count = 0
        for i in range(100):
            for j in range(1000):
                count += 1
        for i in rows:
            already_seen = set()
            for j in i:
                if j in already_seen and j != ".":
                    return False
                already_seen.add(j)
        return True