with open("inputs/3.txt") as file:
    engine_schematic = file.readlines()

array_2d = [list(line.strip()) for line in engine_schematic]


def check_left_recursively(lookup_row, lookup_col, final_number, visited):
    if lookup_col < 0:
        return
    if array_2d[lookup_row][lookup_col].isdigit():
        visited[lookup_row][lookup_col] = True
        final_number.insert(0, array_2d[lookup_row][lookup_col])
        check_left_recursively(lookup_row, lookup_col - 1, final_number, visited)


def check_right_recursively(lookup_row, lookup_col, final_number, visited):
    if lookup_col >= len(array_2d[lookup_row]):
        return
    if array_2d[lookup_row][lookup_col].isdigit():
        visited[lookup_row][lookup_col] = True
        final_number.append(array_2d[lookup_row][lookup_col])
        check_right_recursively(lookup_row, lookup_col + 1, final_number, visited)


directions = [
    (-1, -1),
    (-1, 0),
    (-1, 1),
    (0, -1),
    (0, 1),
    (1, -1),
    (1, 0),
    (1, 1),
]  # 8 lookup directions
sum_parts = 0
sum_gear_rations = 0
visited = [[False for _ in row] for row in array_2d]
for row_idx in range(len(array_2d)):
    for col_idx in range(len(array_2d[row_idx])):
        if (
            not array_2d[row_idx][col_idx].isdigit()
            and array_2d[row_idx][col_idx] != "."
        ):
            gear_parts = []
            # Start search for numbers in any direction
            for d_row, d_col in directions:
                lookup_row, lookup_col = row_idx + d_row, col_idx + d_col
                final_number = []
                # Check engine schematic bounds
                if 0 <= lookup_row < len(array_2d) and 0 <= lookup_col < len(
                    array_2d[lookup_row]
                ):
                    if (
                        array_2d[lookup_row][lookup_col].isdigit()
                        and not visited[lookup_row][lookup_col]
                    ):
                        final_number.append(array_2d[lookup_row][lookup_col])
                        visited[lookup_row][lookup_col] = True
                        check_left_recursively(
                            lookup_row, lookup_col - 1, final_number, visited
                        )
                        check_right_recursively(
                            lookup_row, lookup_col + 1, final_number, visited
                        )

                        str_final_num = "".join(final_number)
                        if str_final_num.isdigit():
                            sum_parts += int(str_final_num)
                            if array_2d[row_idx][col_idx] == "*":
                                gear_parts.append(int(str_final_num))
            if len(gear_parts) == 2:
                sum_gear_rations += gear_parts[0] * gear_parts[1]

print(sum_parts)
print(sum_gear_rations)
