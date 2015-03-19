"""Demo 2
   
   Import into separate namespaces in case of
   conflicts with other libraries that one might use
"""
import scan.client as client
import scan.commands as cmd

client = client.ScanClient()
cmds = [
    cmd.Comment("Hello"),
    cmd.Comment("World"),
    cmd.Set("voltage", 13.4)
]

client.submit(cmds)
