
import unittest
from scan.commands import *

# These tests compare the XML as strings, even though for example
# both "<comment><text>Hello</text></comment>"
# and "<comment>\n  <text>Hello</text>\n</comment>"
# would be acceptable XML representations.
# Changes to the XML could result in the need to update the tests.
class CommandTest(unittest.TestCase):
    def testXML(self):
        # Basic comment
        cmd = Comment("Hello")
        print cmd
        self.assertEqual(cmd.genXML(), "<comment><text>Hello</text></comment>")

        # Check proper escape of "less than"
        cmd = Comment("Check for current < 10")
        print cmd
        self.assertEqual(cmd.genXML(), "<comment><text>Check for current &lt; 10</text></comment>")

        # Basic set
        cmd = Set("some_device", 3.14)
        print cmd
        self.assertEqual(cmd.genXML(), "<set><device>some_device</device><value>3.14</value></set>")

        # .. more options
        cmd = Set("some_device", 3.14, completion=True)
        print cmd
        self.assertEqual(cmd.genXML(), "<set><device>some_device</device><value>3.14</value><completion>true</completion></set>")

        cmd = Set("some_device", 3.14, completion=True, timeout=5.0)
        print cmd
        self.assertEqual(cmd.genXML(), "<set><device>some_device</device><value>3.14</value><completion>true</completion><timeout>5.0</timeout></set>")

        cmd = Set("some_device", 3.14, completion=True, readback=True, tolerance=1, timeout=10.0)
        print cmd
        self.assertEqual(cmd.genXML(), "<set><device>some_device</device><value>3.14</value><completion>true</completion><wait>true</wait><readback>some_device</readback><tolerance>1</tolerance><timeout>10.0</timeout></set>")

        cmd = Set("some_device", 3.14, completion=True, readback="some_device.RBV", tolerance=1, timeout=10.0)
        print cmd
        self.assertEqual(cmd.genXML(), "<set><device>some_device</device><value>3.14</value><completion>true</completion><wait>true</wait><readback>some_device.RBV</readback><tolerance>1</tolerance><timeout>10.0</timeout></set>")


if __name__ == "__main__":
    unittest.main()