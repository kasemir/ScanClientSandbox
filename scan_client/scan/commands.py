

class Comment(object):
    """Command to add comment"""
    def __init__(self, text):
        self.text = text
        
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
        
    def __repr__(self):
        return "Set \'%s\' = %s" % (self.device, str(self.value))