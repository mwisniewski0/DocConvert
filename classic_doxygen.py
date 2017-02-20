import doc_type
import doc_entry
import doc_element


class ClassicDoxygen(doc_type.DocumentationType):
    def __init__(self, star_count=60, max_line_length=90):
        if star_count < 1:
            raise ValueError("There needs to be at least one star")

        if max_line_length < 1:
            raise ValueError("Each line needs to be at least one character long")
        self.star_count = star_count
        self.max_line_length = max_line_length

    def generate_from_entry(self, entry, indent):
        # TODO: if needed optimize the string concats
        stars = "*" * self.star_count
        entry_text = ""
        prefix = indent + " * "

        # scan for full summary first
        for el in entry.doc_elements:
            if type(el) is doc_element.SummaryElement:
                entry_text += el.text + "\n"

        # then for everything else
        for el in entry.doc_elements:
            if type(el) is doc_element.BriefElement:
                entry_text += "\\brief " + el.text + "\n"
            elif type(el) is doc_element.ParamElement:
                entry_text += "\\param " + el.name + " " + el.description + "\n"
            elif type(el) is doc_element.ExceptElement:
                entry_text += "\\exception " + el.type + " " + el.description + "\n"
            elif type(el) is doc_element.ReturnElement:
                entry_text += "\\return " + el.text + "\n"

        # remove the last newline
        if entry_text[-1] == "\n":
            entry_text = entry_text[:-1]

        output = indent + "/" + stars + "\n"
        output += "\n".join(self.break_line(entry_text, prefix, self.max_line_length)) + "\n"
        output += indent + " " + stars + "/"

        return output

    def convert_entries_in_file(self, path, new_doctype):
        pass