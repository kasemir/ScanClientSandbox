

class ScanClient(object):
    
    def submit(self, commands):
        print "Submitting scan:", ", ".join([ str(cmd) for cmd in commands ])