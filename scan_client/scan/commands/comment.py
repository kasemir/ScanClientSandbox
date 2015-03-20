
import xml.etree.ElementTree as ET

class Comment(object):
    """Command to add comment"""
    def __init__(self, text):
        self.text = text

    def genXML(self):
        xml = ET.Element("comment")
        ET.SubElement(xml, "text").text = self.text
        return ET.tostring(xml)
        
    def __repr__(self):
        return "Comment \'%s\'" % self.text

