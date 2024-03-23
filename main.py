def calculate_rectangle_area(length, width):
    if length <= 0:
        return "Invalid length"
    elif width <= 0:
        return "Invalid width"
    else:
        area = length * width
        return area

# Các ca kiểm thử
test_cases = [
    (5, 4, 20),         # Chiều dài và chiều rộng hợp lệ
    (-5, 4, "Invalid length"),  # Chiều dài không hợp lệ
    (5, -4, "Invalid width"),   # Chiều rộng không hợp lệ
    (-5, -4, "Invalid length"), # Cả chiều dài và chiều rộng không hợp lệ
    (0, 4, "Invalid length"),   # Chiều dài là 0
    (0, 0, "Invalid length"),   # Cả chiều dài và chiều rộng là 0
    (5.5, 4.2, 23.1)             # Chiều dài và chiều rộng là số thực
]

# Kiểm thử từng ca và tính độ phủ C2
coverage = 0
for test_case in test_cases:
    length, width, expected_result = test_case
    result = calculate_rectangle_area(length, width)
    if result == expected_result:
        coverage += 1

# In kết quả độ phủ C2
total_test_cases = len(test_cases)
print(f"C2 coverage: {coverage}/{total_test_cases}")
