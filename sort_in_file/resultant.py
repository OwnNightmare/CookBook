class File:
    new_str_sign = '\n'

    def __init__(self, name):
        self.content = ''
        self.length = 0
        self.name = name

    def reading(self, mode='r', buffering=1, encoding='utf8'):
        with open(self.name, mode, buffering, encoding) as file:
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
    second_file = File('file_two.txt')
    third_file = File('story_three.txt')
    files = [third_file, first_file, second_file]
    return files


def perform_files(files):
    if type(files) == list:
        for file in files:
            file.reading()
        for file in sorted(files):
            print(file.name)
            print(file.length)
            print(file.content)


perform_files(assign_files())