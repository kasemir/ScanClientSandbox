
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
        self.assertEqual(cmd.genXML(), "<comment><text>Hello</text></comment>")

        # Check proper escape of "less than"
        cmd = Comment("Check for current < 10")
        self.assertEqual(cmd.genXML(), "<comment><text>Check for current &lt; 10</text></comment>")

        # Basic comment
        cmd = Set("some_device", 3.14)
        self.assertEqual(cmd.genXML(), "<set><device>some_device</device><value>3.14</value></set>")


if __name__ == "__main__":
    unittest.main()