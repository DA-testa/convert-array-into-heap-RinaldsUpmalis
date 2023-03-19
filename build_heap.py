# python3

def check(data, current, swaps):
    n = len(data)
    current_index = current
    left_index = 2 * current + 1
    right_index = 2 * current + 2

    if left_index < n and data[left_index] < data[current_index]:
        current_index = left_index
    if right_index < n and data[right_index] < data[current_index]:
        current_index = right_index
    if current != current_index:
        data[current], data[current_index] = data[current_index], data[current]
        swaps.append((current, current_index))
        check(data, current_index, swaps)

def build_heap(data):
    swaps = []
    n = len(data)

    if (n % 2) == 0:
        current = (n - 2)//2
    else:
        current = (n - 1)//2

    while current>=0:
        check(data, current, swaps)
        current= current-1

    # TODO: Creat heap and heap sort
    # try to achieve  O(n) and not O(n2)


    return swaps


def main():
    
    text = input()
    n=0
    if text[0]=="I":
        n=int(input())
        data = list(map(int, input().split()))
    elif text[0]=="F":
        filename = "tests/"
        filename = filename + input()
        if filename[-1] == 'a':
            return
        with open(filename, 'r') as file:
            text = file.read()
            #lines = text.split('\n')
            n = int(text[0])
            data = list(map(int, text[1].split()))
    assert len(data) == n

    # print(compute_height(n, parents))

    # TODO : add input and corresponding checks
    # add another input for I or F 
    # first two tests are from keyboard, third test is from a file


    # input from keyboard
    #n = int(input())
    #data = list(map(int, input().split()))

    # checks if lenght of data is the same as the said lenght
    # assert len(data) == n

    # calls function to assess the data 
    # and give back all swaps
    swaps = build_heap(data)

    # TODO: output how many swaps were made, 
    # this number should be less than 4n (less than 4*len(data))


    # output all swaps
    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
