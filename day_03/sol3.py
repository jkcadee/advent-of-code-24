import re
import math

def read_txt() -> None:
    file = open("day_03/p3_input.txt", "r")
    parse_str = file.read()
    file.close()
    return parse_str

def solution_part1(parse_str):
    regex = r"mul\([0-9]{1,3},[0-9]{1,3}\)"
    total_sum = 0
    res = re.findall(regex, parse_str)
    
    for v in res:
        nums = re.findall(r'\d+', v)
        l = [int(i) for i in nums]
        total_sum += math.prod(l)

    return total_sum

def solution_part2(parse_str):
    regex = r"(?:mul\(([0-9]{1,3}),([0-9]{1,3})\)|do(?:n't)?\(\))"
    total_sum = 0
    res = re.findall(regex, parse_str)
    
    print(res)
    do_add = True
    sum_do = 0
    for v in res:
        if v[0] == '':
            sum_do += 1
            if sum_do % 2 == 0:
                do_add = True
                continue
            else:
                do_add = False
                continue
        if do_add: 
            l = [int(i) for i in v]
            total_sum += math.prod(l)
    
    return total_sum

def main():
    #p_string = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5)"
    p_string = read_txt()
    #print(solution_part1(p_string))
    print(solution_part2(p_string))

if __name__ == "__main__":
    main()