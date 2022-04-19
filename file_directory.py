class FileSystem:
    def __init__(self):
        self.root = Directory("/")

    def create_directory(self, path):
        self._validate_path(path)
        names_in_path = path.split("/")
        names_in_path.pop(0)
        number_of_names = len(names_in_path)
        current_node = self.root
        for index in range(number_of_names):
            current_node_name = names_in_path[index]
            if not index == number_of_names - 1:
                if not current_node_name in current_node.children:
                    raise ValueError
                if not isinstance(current_node.children[current_node_name], Directory):
                    raise ValueError
                current_node = current_node.children[current_node_name]

            else:
                if current_node_name in current_node.children:
                    raise ValueError
                current_node.add_node(Directory(current_node_name))

    def create_file(self, path, contents):
        self._validate_path(path)
        names_in_path = path.split("/")
        names_in_path.pop(0)
        number_of_names = len(names_in_path)
        current_node = self.root
        for index in range(number_of_names):
            current_node_name = names_in_path[index]
            if not index == number_of_names - 1:
                if not current_node_name in current_node.children:
                    raise ValueError
                if not isinstance(current_node.children[current_node_name], Directory):
                    raise ValueError
                current_node = current_node.children[current_node_name]
            else:
                if not current_node_name in current_node.children:
                    new_file = File(current_node_name)
                    new_file.write_contents(contents)
                    current_node.children[current_node_name] = new_file

    def read_file(self, path):
        self._validate_path(path)
        names_in_path = path.split("/")
        names_in_path.pop(0)
        number_of_names = len(names_in_path)
        current_node = self.root
        for index in range(number_of_names):
            current_node_name = names_in_path[index]
            if not index == number_of_names - 1:
                if not current_node_name in current_node.children:
                    raise ValueError
                if not isinstance(current_node.children[current_node_name], Directory):
                    raise ValueError
                current_node = current_node.children[current_node_name]
            else:
                if not current_node_name in current_node.children:
                    raise ValueError
                if isinstance(current_node.children[current_node_name], Directory):
                    raise ValueError
                return current_node.children[current_node_name].contents

    def delete_directory_or_file(self, path):
        self._validate_path(path)
        names_in_path = path.split("/")
        names_in_path.pop(0)
        number_of_names = len(names_in_path)
        current_node = self.root
        for index in range(number_of_names):
            current_node_name = names_in_path[index]
            if not index == number_of_names - 1:
                if not current_node_name in current_node.children:
                    raise ValueError
                if not isinstance(current_node.children[current_node_name], Directory):
                    raise ValueError
                current_node = current_node.children[current_node_name]
            else:
                if not current_node_name in current_node.children:
                    raise ValueError
                current_node.delete_node(current_node_name)

    def size(self):
        file_system_stack = [self.root]
        total_size = 0
        while len(file_system_stack) > 0:
            current_directory = file_system_stack.pop()
            for name in current_directory.children:
                node = current_directory.children[name]
                if isinstance(node, Directory):
                    file_system_stack.append(node)
                else:
                    total_size += len(node)
        return total_size

    def __str__(self):
        return f"*** FileSystem ***\n" + self.root.__str__() + "\n***"

    @staticmethod
    def _validate_path(path):
        if not path.startswith("/"):
            raise ValueError("Path should start with `/`.")

    def _find_bottom_node(self, node_names):
        number_of_names = len(node_names)
        current_node = self.root
        for index in range(number_of_names):
            current_node_name = node_names[index]
            if not index == number_of_names - 1:
                if not current_node_name in current_node.children:
                    raise ValueError
                if not isinstance(current_node.children[current_node_name], Directory):
                    raise ValueError
                current_node = current_node.children[current_node_name]

            else:
                return current_node.children[current_node_name]


class Node:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"{self.name} ({type(self).__name__})"


class Directory(Node):
    def __init__(self, name):
        super().__init__(name)
        self.children = {}

    def add_node(self, node):
        self.children[node.name] = node

    def delete_node(self, name):
        del self.children[name]

    def __str__(self):
        string = super().__str__()

        children_strings = []
        for child in list(self.children.values()):
            child_string = child.__str__().rstrip()
            children_strings.append(child_string)

        children_combined_string = indent("\n".join(children_strings), 2)
        string += "\n" + children_combined_string.rstrip()
        return string


class File(Node):
    def __init__(self, name):
        super().__init__(name)
        self.contents = ""

    def write_contents(self, contents):
        self.contents = contents

    def __len__(self):
        return len(self.contents)

    def __str__(self):
        return super().__str__() + f" | {len(self)} characters"


def indent(string, number_of_spaces):
    spaces = " " * number_of_spaces
    lines = string.split("\n")
    indented_lines = [spaces + line for line in lines]
    return "\n".join(indented_lines)
