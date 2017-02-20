class DocElement:
    """
    A part of a documentation entry (e.g. parameter, returns, etc.).
    Purely abstract.
    """

    def __init__(self):
        pass


class ReturnElement(DocElement):
    """
    Represents a return element in a documentation entry
    """

    def __init__(self, text):
        self.text = text


class SummaryElement(DocElement):
    """
    Represents a full summary element in a documentation entry
    """

    def __init__(self, text):
        self.text = text


class BriefElement(DocElement):
    """
    Represents a brief summary element in a documentation entry
    """

    def __init__(self, text):
        self.text = text


class ParamElement(DocElement):
    """
    Represents a parameter element in a documentation entry
    """

    def __init__(self, name, description):
        self.name = name
        self.description = description


class ExceptElement(DocElement):
    """
    Represents a return element in a documentation entry
    """

    def __init__(self, type, description):
        self.type = type
        self.description = description