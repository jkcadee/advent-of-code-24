# lists are the same size
# nothing against sorting them
# ummm do merge sort for fun i guess but i could do that later :3

l1 = []
l2 = []

def read_txt() -> None:
    file = open("day_01/p1_input.txt", "r")
    num_list = file.readlines()
    for v in num_list:
        line = v.split()
        l1.append(int(line[0]))
        l2.append(int(line[1]))

    l1.sort()
    l2.sort()

    file.close()

def solution_part1() -> int:
    total_distance = 0

    for i in range(len(l1)):        
        total_distance += abs(l1[i] - l2[i])
    
    return total_distance

def solution_part2() -> int:
    sim_score = 0

    for v in l1:
        l2_total = len([i for i in range(len(l2)) if l2[i] == v])
        sim_score += v * l2_total

    return sim_score

def main():
    read_txt()
    print(solution_part1())
    print(solution_part2())

if __name__ == "__main__":
    main()