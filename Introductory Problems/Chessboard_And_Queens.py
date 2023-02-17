# Reading input for blocked locations
def count_solutions():
    blocked_locations = [[c == '*' for c in input()]for _ in range(8)]
    solutions = []

    def is_safe(slate):
        if slate:
            current_queen = slate[len(slate) - 1]
            # is the current queen in the block location?
            if blocked_locations[len(slate) - 1][current_queen]:
                return False

            for prev_idx in range(len(slate) - 2, -1, -1):
                prev_queen = slate[prev_idx]
                # Is the prev queen in same location as col queen
                if current_queen == prev_queen:
                    return False
                # Is the prev queen in the same diagonal as the current queen
                row_diff = len(slate) - 1 - prev_idx
                col_diff = abs(current_queen - prev_queen)
                if row_diff == col_diff:
                    return False

        return True

    def helper(idx, chess_board_size, slate):
        # back tracking case
        if not is_safe(slate):
            return

        # base case
        if idx == chess_board_size:
            solutions.append(1)
            return

        # recursive case
        for col in range(0, chess_board_size, 1):
            slate.append(col)
            helper(idx + 1, chess_board_size, slate)
            slate.pop(len(slate) - 1)

    helper(0, 8, [])
    print(len(solutions))


count_solutions()
