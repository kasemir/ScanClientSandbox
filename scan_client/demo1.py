"""Demo 1
   
   Simplest way to import 'everything'
"""
from scan import *

client = ScanClient()
cmds = [
    Comment("Hello"),
    Comment("World"),
    Set("voltage", 13.4)
]

client.submit(cmds)
