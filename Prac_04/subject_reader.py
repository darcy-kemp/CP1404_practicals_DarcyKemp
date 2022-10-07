"""CP1404 | prac_04 subject reader | Darcy Kemp
Reading stings from a file and splitting them for processing
"""

FILENAME = "subject_data.txt"


def main():
    data = get_data()
    data = format_data(data)
    print(data)


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME)
    output_list = []
    i = 0
    for line in input_file:
        print(line)  # See what a line looks like
        print(repr(line))  # See what a line really looks like
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        print(parts)  # See what the parts look like (notice the integer is a string)
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        print(parts)  # See if that worked
        print("----------")
        output_list += [0]
        output_list[i] = parts
        i += 1
    input_file.close()
    return output_list


def format_data(data):
    formatted_data = ""
    for i in range(0, len(data), 1):
        subject_data = data[i]
        formatted_data += str(subject_data[0]) + " is taught by " + str(subject_data[1]) + " and has " + str(subject_data[2]) + " students \n"
    return formatted_data


main()
