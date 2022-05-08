import Lab2

print("Test_Lab2")


def test_get_user_input():
    result = []
    input_string = "1, 2, 3, 4, 5, 6, 7, 8"
    test_arr = [1, 2, 3, 4, 5, 6, 7, 8]

    result = Lab2.get_user_input(input_string)

    assert (result == test_arr)


def test_calc_average_temperature():
    result = 0
    input_array = [1, 2, 3, 4, 5, 6, 7, 8]
    test_result = 4.5

    result = Lab2.calc_average_temperature(input_array)

    assert (result == test_result)
