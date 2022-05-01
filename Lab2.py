def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    num_list = get_user_input()
    print(calc_average_temperature(num_list))
    print(calc_min_max_temperature(num_list))

def display_main_menu():
    print("display_main_menu")
    print("Enter some numbers separated by commas(e.g.5,67,32)")

def get_user_input():
    input_num = input()
    list_input = input_num.split(",")
    float_list = [float(number) for number in list_input]

    return float_list

def calc_average_temperature(num_input):
    total = 0
    count = 0
    for number in num_input:
        count += 1

    for number in num_input:
        total = total + number

    ave = total / count

    return ave

def calc_min_max_temperature(num_input):
    smallest = largest = num_input[0]

    for i in num_input:
        if i > largest:
            largest = i

    for i in num_input:
        if i < smallest:
            smallest = i

    max_min_ = [smallest, largest]
    return max_min_ 

if __name__ == "__main__":
    main()
