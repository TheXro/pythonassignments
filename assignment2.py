# Task 1: Reverse the contents of file1.txt
with open('file1.txt', 'r') as f1:
    data1 = f1.read().strip().split(',')
    reversed_data1 = ','.join(data1[::-1])

with open('file1_reversed.txt', 'w') as f1_reversed:
    f1_reversed.write(reversed_data1)

# Task 2: Convert all the numbers in file2.txt to text
def number_to_text(number):
    number_map = {
        '0': 'zero', '1': 'one', '2': 'two', '3': 'three', '4': 'four',
        '5': 'five', '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine'
    }
    return ' '.join([number_map[char] for char in number if char in number_map])

with open('file2.txt', 'r') as f2:
    data2 = f2.read()

converted_data2 = number_to_text(data2)

with open('file2_converted.txt', 'w') as f2_converted:
    f2_converted.write(converted_data2)

# Task 3: Prepare a dictionary from file3.txt
with open('file3.txt', 'r') as f3:
    data3 = f3.read().strip().split('\n\n')

student_dict = {}
for entry in data3:
    lines = entry.split('\n')
    roll = lines[0].split(': ')[1]
    name = lines[1].split(': ')[1]
    section = lines[2].split(': ')[1]
    semester = lines[3].split(': ')[1]
    student_dict[roll] = {'Name': name, 'Section': section, 'Semester': semester}

print(student_dict)
