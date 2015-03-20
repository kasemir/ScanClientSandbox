
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


class Set(object):
    """Command to set a device to a value
       @param device: Device name
       @param value: Value
    """
    def __init__(self, device, value):
        self.device = device
        self.value = value

    def genXML(self):
        xml = ET.Element("set")
        ET.SubElement(xml, "device").text = self.device
        ET.SubElement(xml, "value").text = str(self.value)
        return ET.tostring(xml)
        
    def __repr__(self):
        return "Set \'%s\' = %s" % (self.device, str(self.value))