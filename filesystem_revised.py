class FileSystem:
    def __init__(self):
        self.root = Directory("/")

    def create_directory(self, path):
        second_last_node, last_node_name = self._get_node_and_name(path)
        new_directory = Directory(last_node_name)
        second_last_node.add_node(new_directory)

    def create_file(self, path, contents):
        second_last_node, last_node_name = self._get_node_and_name(path)
        new_file = File(last_node_name)
        new_file.write_contents(contents)
        second_last_node.add_node(new_file)

    def read_file(self, path):
        second_last_node, last_node_name = self._get_node_and_name(path)
        if last_node_name not in second_last_node.children:
            raise ValueError
        return second_last_node.children[last_node_name].contents

    def delete_directory_or_file(self, path):
        second_last_node, last_node_name = self._get_node_and_name(path)
        if last_node_name not in second_last_node.children:
            raise ValueError
        second_last_node.delete_node(last_node_name)

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
        current_node = self.root
        for node_name in node_names:
            if not isinstance(current_node, Directory):
                raise ValueError
            if not node_name in current_node.children:
                raise ValueError
            current_node = current_node.children[node_name]
        return current_node

    def _get_node_and_name(self, path):
        self._validate_path(path)
        names_in_path = path.split("/")
        names_in_path.pop(0)
        last_node_name = names_in_path.pop(-1)
        second_last_node = self._find_bottom_node(names_in_path)
        if not isinstance(second_last_node, Directory):
            raise ValueError
        return second_last_node, last_node_name


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
