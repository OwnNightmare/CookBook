lines_in_first_part = 0
with open('story_one.txt', encoding='utf8') as first_part:
    for line in first_part:
        lines_in_first_part += 1

lines_in_second_part = 0
with open('story_two.txt', encoding='utf8') as second_part:
    for line in second_part:
        lines_in_second_part += 1


lines_in_third_part = 0
content_third = ''
with open('story_three.txt', encoding='utf8') as third_part:
    for line in third_part:
        content_third += line
        lines_in_third_part += 1
    name_third = third_part.name


with open('United.txt', 'w', encoding='utf8') as united:
    united.write(name_third + '\n')
    united.write(str(lines_in_third_part) + '\n')
    united.write(content_third)


class File:

    def __init__(self, name):
        self.content = ''
        self.length = 0
        self.name = name

    def reading(self, mode='r', buffering=1, encoding='utf8'):
        with open(self.name, mode, buffering, encoding) as file:
            for line_ in file:
                self.content += line_
                self.length += 1

first_file = File('story_one.txt')
second_file = File('story_two.txt')
second_file.reading()
print(second_file.content)
print(second_file.name)
print(second_file.length)
