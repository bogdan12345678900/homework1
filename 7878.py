total_sum = 0
max_num = float('-inf')
min_num = float('inf')

while True:
    num = int(input("Введіть число: "))
    if num == 7:
        print("Good bye!")
        break
    total_sum += num
    if num > max_num:
        max_num = num
    if num < min_num:
        min_num = num

print(f"Сума: {total_sum}")
print(f"Максимум: {max_num}")
print(f"Мінімум: {min_num}")