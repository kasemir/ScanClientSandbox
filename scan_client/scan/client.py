

class ScanClient(object):
    
    def submit(self, commands):
        print "Submitting scan:"
        print ", ".join([ str(cmd) for cmd in commands ])