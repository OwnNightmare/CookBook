lines_in_first_part = 0
with open('story_one.txt', encoding='utf8') as first_part:
    for line in first_part:
        lines_in_first_part += 1
print(lines_in_first_part)

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
