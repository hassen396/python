num_list = [33, 42, 5, 66, 77, 22, 16, 79, 36, 62, 78, 43, 88, 39, 53, 67, 89, 11]
for i, item in enumerate(num_list):
    if i == 5:
        continue
    else:
        print(f"index {i}: {item}")

print("\nthe while ...........\n")
# The while loop
i = 0
while i < len(num_list):
    print(f"index {i}: {num_list[i]}")
    i = i + 1
