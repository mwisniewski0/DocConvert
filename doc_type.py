import abc


class DocumentationType(metaclass=abc.ABCMeta):
    """
    Class responsible for representing different styles of documentation
    """

    def __init__(self):
        pass

    @abc.abstractmethod
    def generate_from_entry(self, entry, indent):
        pass

    @abc.abstractmethod
    def convert_entries_in_file(self, path, new_doctype):
        pass

    @staticmethod
    def split_with_newline(text, whitespace="\n\r  ", newline="\n"):
        """
        Splits a string on whitespaces and counts the occurrences of newline after
        the specified word
        :param text: text to be split
        :param whitespace: whitespace characters to be split on
        :param newline: the newline character to be counted
        :return: a list of tuples: (word, count of newlines)
        """

        elements = []
        element = ""
        new_line_count = 0
        move_to_next = False

        for ch in text:
            if ch in whitespace:
                move_to_next = True
                if ch in newline:
                    new_line_count += 1
            else:
                if move_to_next:
                    if len(element) > 0 or new_line_count > 0:
                        elements.append((element, new_line_count))
                        element = ""
                        move_to_next = False
                        new_line_count = 0
                element += ch
        if len(element) > 0 or new_line_count > 0:
            elements.append((element, new_line_count))

        return elements

    @staticmethod
    def break_line(text, prefix, max_length):
        words = DocumentationType.split_with_newline(text)
        if len(words) <= 0:
            return []

        lines = []
        curr_line = prefix[:] + words[0][0]
        prev_newlines = words[0][1]

        for (word, newline_count) in words[1:]:
            if prev_newlines > 0:
                lines.append(curr_line)
                lines += [prefix[:]] * (prev_newlines - 1)
                curr_line = prefix[:] + word
            else:
                if len(curr_line) + len(word) > max_length:
                    lines.append(curr_line)
                    curr_line = prefix[:] + word
                else:
                    curr_line += " " + word
            prev_newlines = newline_count

        lines.append(curr_line)
        lines += [prefix[:]] * prev_newlines

        return lines