with open("inputs/1.txt") as file:
    calibration_document = file.readlines()


def word_to_num(word):
    mapping = {
        "zero": "0",
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }
    for key in mapping.keys():
        if key in word:
            return mapping[key]
    return None


sum_cal_val_2 = 0
for line in calibration_document:
    cal_value = []
    cal_chars_start = []
    cal_chars_end = []

    for char in line.strip():
        if char.isdigit():
            cal_value.append(char)
            break
        cal_chars_start.append(char)
        num = word_to_num("".join(cal_chars_start))
        if num:
            cal_value.append(num)
            cal_chars_start = []
            break

    for char in line[::-1].strip():
        if char.isdigit():
            cal_value.append(char)
            break
        cal_chars_end.insert(0, char)
        num = word_to_num("".join(cal_chars_end))
        if num:
            cal_value.append(num)
            cal_chars_end = []
            break

    sum_cal_val_2 += int("".join(cal_value))

print(sum_cal_val_2)
