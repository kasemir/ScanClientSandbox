
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
       @param completion: Await completion?
       @param readback: False to not check any readback.
                        True to wait for readback from the 'device',
                        or name of specific readback different from 'device'.
       @param tolerance: Readback tolerance
       @param timeout: Timeout in seconds, used for completion and readback check
    """
    def __init__(self, device, value, completion=False, readback=False, tolerance=0.1, timeout=0.0):
        self.device = device
        self.value = value
        self.completion = completion
        self.readback = readback
        self.tolerance = tolerance
        self.timeout = timeout

    def genXML(self):
        xml = ET.Element("set")
        ET.SubElement(xml, "device").text = self.device
        ET.SubElement(xml, "value").text = str(self.value)
        need_timeout = False
        if self.completion:
            ET.SubElement(xml, "completion").text = "true"
            need_timeout = True
        if self.readback:
            ET.SubElement(xml, "wait").text = "true"
            ET.SubElement(xml, "readback").text = self.device if self.readback == True else self.readback
            ET.SubElement(xml, "tolerance").text = str(self.tolerance)
            need_timeout = True
        if need_timeout  and  self.timeout > 0:
            ET.SubElement(xml, "timeout").text = str(self.timeout)
        return ET.tostring(xml)
        
    def __repr__(self):
        info = "Set \'%s\' = %s" % (self.device, str(self.value))
        if self.completion:
            info += " with completion in %f sec" % self.timeout
        if self.readback:
            rdbk_device = self.device if self.readback == True else self.readback
            info += " (wait for %s to match +-%f in %f sec" % (rdbk_device, self.tolerance, self.timeout)
        return info