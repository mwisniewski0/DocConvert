import classic_doxygen as cd
import xml_doc as xd
import os


dox = cd.ClassicDoxygen()
xml = xd.XmlDoc()

if not os.path.exists("converted"):
    os.mkdir("converted")

root = "."
for file in os.listdir(root):
    if file.endswith(".h") or file.endswith(".cpp"):
         path = os.path.join(root, file)
         out = open("converted/" + file, "w")
         out.write(xml.convert_entries_in_file(path, dox))
         out.close()
