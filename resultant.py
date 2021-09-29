class File:
    new_str_sign = '\n'

    def __init__(self, name, path='sort_in_file/'):
        self.content = ''
        self.length = 0
        self.name = name
        self.path = path

    def reading(self, mode='r', buffering=1, encoding='utf8'):
        with open(self.path + self.name, mode, buffering, encoding) as file:
            for line in file:
                self.content += f"{line.rstrip()}{File.new_str_sign}"
                self.length += 1
        self.content = self.content.rstrip()

    def __gt__(self, other):
        return self.length > other.length

    def __lt__(self, other):
        return self.length < other.length

    def __eq__(self, other):
        return self.length == other.length


def assign_files():
    first_file = File('story_one.txt')
    second_file = File('story_two.txt')
    third_file = File('story_three.txt')
    files = [third_file, first_file, second_file]
    return files


def read_and_write(read_from, write_to, mode='a', buffering=1, encoding='utf8'):
    if type(read_from) == list:
        for file in read_from:
            file.reading()
        for file in sorted(read_from):
            with open(write_to, mode, buffering, encoding) as writing_in:
                writing_in.write(file.name + '\n')
                writing_in.write(str(file.length) + '\n')
                writing_in.write(file.content + '\n')
        print(f'file {writing_in.name} was written')
    elif type(read_from) == File:
        read_from.reading()
        with open(write_to, mode, buffering, encoding) as writing_in:
            writing_in.write(read_from.name + '\n')
            writing_in.write(str(read_from.length) + '\n')
            writing_in.write(read_from.content + '\n')
        print(f'file {writing_in.name} was written')


def clear_file(path, mode='w'):
    with open(path, mode) as cleared_file:
        cleared_file.write('')


clear_file('sort_in_file/United.txt')
read_and_write(assign_files(), 'sort_in_file/United.txt')