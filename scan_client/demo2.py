"""Demo 2
   
   Import into separate namespaces in case of
   name conflicts with other libraries
"""

# Assume you already have a 'Set' class.
# That would conflict with the scan.commands.Set
# if we simply used "from scan import *".
class Set(object):
    def __init__(self):
        pass

    def __str__(self):
        return "Can still use the 'other' set"

# By importing the scan tools into their own namespace...
import scan.client as client
import scan.commands as cmd

# .. you can use them ..
client = client.ScanClient()
cmds = [
    cmd.Comment("Hello"),
    cmd.Comment("World"),
    cmd.Set("voltage", 13.4)
]
client.submit(cmds)

# .. and not worry about clashing with other classes of the same name:
print Set()