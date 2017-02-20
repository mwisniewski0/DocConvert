import doc_type
import doc_element
import doc_entry
import xml.etree.ElementTree as ElementTree

class XmlDoc(doc_type.DocumentationType):
    def __init__(self, max_line_length=90):
        self.max_line_length = max_line_length

    def generate_from_entry(self, entry, indent):
        pass

    @staticmethod
    def lstrip_split(text, whitespace="\n\r\t "):
        index_of_non_whitespace = 0
        for c in text:
            if c not in whitespace:
                break
            index_of_non_whitespace += 1

        return (text[:index_of_non_whitespace], text[index_of_non_whitespace:])

    def convert_entries_in_file(self, path, new_doctype):
        with open(path, "r") as input:
            output = ""

            current_entry_xml = None
            for line in input:
                # strip the newline if it is there
                if len(line) > 0 and line[-1] == "\n":
                    line = line[:-1]

                (indent, content) = self.lstrip_split(line)
                if content.startswith("///"):
                    if current_entry_xml is None:
                        current_entry_xml = ""
                    current_entry_xml += content[3:]
                else:
                    if current_entry_xml is not None:
                        elements = []

                        # add implied root:
                        current_entry_xml = "<root>" + current_entry_xml + "</root>"
                        tree = ElementTree.fromstring(current_entry_xml)
                        current_entry_xml = None

                        if tree.text.strip() != "":
                            elements.append(doc_element.SummaryElement(tree.text))
                        for node in tree:
                            if node.tag == "summary":
                                elements.append(doc_element.BriefElement(node.text))
                            if node.tag == "param":
                                elements.append(doc_element.ParamElement(node.attrib['name'], node.text))
                            if node.tag == "returns":
                                elements.append(doc_element.ReturnElement(node.text))
                            if node.tag == "exception":
                                elements.append(doc_element.ExceptElement(node.attrib['cref'], node.text))

                        output += "\n" + new_doctype.generate_from_entry(doc_entry.DocEntry(elements), indent)

                    output += "\n" + line

            # skip the first newline
            return output[1:]