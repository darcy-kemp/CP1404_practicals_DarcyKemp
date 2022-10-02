"""CP1404 | prac_03 Files | Darcy Kemp
Reading and writing to multiple files in one task
"""

total = 0

out_file = open("name.txt", 'w')
user_name = input("Please enter your name: ")
print(f"{user_name}", file=out_file)
out_file.close()

in_file = open("name.txt", 'r')
text = in_file.read()
print(f"Your name is: {text}")
in_file.close()


in_file = open("numbers.txt", 'r')
total += int(in_file.readline())
total += int(in_file.readline())
print(f"Sum of the first two numbers is: {total}")
in_file.close()

total = 0

in_file = open("numbers.txt", 'r')
for line in in_file:
    total += int(line)
print(f"The sum of the numbers in numbers.txt is: {total}")
in_file.close()
