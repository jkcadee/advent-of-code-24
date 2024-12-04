input_matrix = [
    #[7, 6, 4, 2, 1],    
    #[1, 2, 7, 8, 9],
    #[9, 7, 6, 2, 1],
    #[1, 3, 2, 4, 5],
    #[8, 6, 4, 4, 1],
    #[1, 3, 6, 7, 9]
]

def read_txt() -> None:
    file = open("day_02/p2_input.txt", "r")
    num_list = file.readlines()
    for v in num_list:
        line = v.split()
        ln = [int(n) for n in line]
        input_matrix.append(ln)

    file.close()

def check_if_asc_or_dsc_correctly(v1, v2) -> bool:
    return True if v1 < v2 else False

def solution_part1() -> int:
    safe_reports = 0
    
    for item in input_matrix:
        ascending = True
        is_safe = True
        if item[0] > item[1]:
            ascending = False
        for index in range(len(item) - 1):
            if check_if_asc_or_dsc_correctly(item[index], item[index + 1]) == ascending:
                if abs(item[index] - item[index + 1]) > 3 or abs(item[index] - item[index + 1]) < 1:
                    is_safe = False
                    break
            else:
                is_safe = False
                break
        if is_safe:
            safe_reports += 1
    
    return safe_reports

def p_sign(num):
    if num == 0 or num == -0:
        return 0
    elif num > 0:
        return 1
    else:
        return -1

def check_for_safety(num_list):
    sign = p_sign(num_list[1] - num_list[0])
    is_broken = False
    if sign == 0:
        return False
    else:
        asc_list = [n * sign for n in num_list]
        pre = asc_list[0]
        for i in range(1, len(asc_list)):
            if not (asc_list[i] > pre and asc_list[i] <= pre + 3):
                is_broken = True
                break
            pre = asc_list[i]
    return not is_broken

def solution_part2() -> int:
    safe_reports = 0

    for item in input_matrix:
        if check_for_safety(item):
            safe_reports += 1
        else:
            for i in range(len(item)):
                if check_for_safety([item[n] for n in range(len(item)) if n != i]):
                    safe_reports += 1
                    break

    return safe_reports               


def main():
    read_txt()
    print(solution_part1())
    print(solution_part2())

if __name__ == "__main__":
    main()