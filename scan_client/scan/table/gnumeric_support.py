"""
Gnumeric table reader

@author: Kay Kasemir
"""

import logging
import gzip
import xml.etree.ElementTree as ET

logger = logging.getLogger("GnumericSupport")

class GnumericReader(object):

    @classmethod
    def findWithoutNamespace(cls, element, desired_tag):
        """Dumb search for child by tag, ignoring potential namespace prefix"""
        for child in element:
            tag = child.tag
            pos = tag.rfind('}')
            if pos > 0:
                tag = tag[pos+1:]
            if tag == desired_tag:
                return child
        return None
    
    @classmethod
    def read(cls, filename):
        """Read a gnumeric file into a basic table, [ [ cell00, cell01 ], [ cell10, cell11 ] ]
        """
        f = gzip.open(filename)
        gnumeric = f.read()
        f.close()
        
        root = ET.fromstring(gnumeric)
        
        # ET.dump(root)
        
        if not "gnumeric" in root.tag:
            raise Exception("Expected GNUMERIC document, got %s" % root.tag)
        
        sheets = GnumericReader.findWithoutNamespace(root, "Sheets")
        if sheets is None:
            raise Exception("Cannot locate Sheets")
        sheet = GnumericReader.findWithoutNamespace(sheets, "Sheet")
        if sheet is None:
            raise Exception("Cannot locate Sheets/Sheet")

        # Locate table size        
        size = GnumericReader.findWithoutNamespace(sheet, "MaxRow")
        if size is None:
            raise Exception("Cannot locate Sheets/Sheet/MaxRow")
        rows = int(size.text) + 1
 
        size = GnumericReader.findWithoutNamespace(sheet, "MaxCol")
        if size is None:
            raise Exception("Cannot locate Sheets/Sheet/MaxCol")
        cols = int(size.text) + 1
 
        logger.debug("Size: %d rows, %d cols" % (rows, cols))

        # Create empty table, because cells will only provide
        # data for non-empty cells, and maybe in random order
        table = []
        for r in range(rows):
            row = []
            for c in range(cols):
                row.append("")
            table.append(row)
        
        cells = GnumericReader.findWithoutNamespace(sheet, "Cells")
        if cells is None:
            raise Exception("Cannot locate Sheets/Sheet/Cells")
        
        for cell in cells:
            row = int(cell.attrib['Row'])
            col = int(cell.attrib['Col'])
            val = cell.text
            logger.debug("Cell (%d, %d): %s" % (row, col, val))
            table[row][col] = val
            
        # Trim empty trailing columns
        while cols > 0:
            for col in range(cols-1, 0, -1):
                for row in range(rows):
                    if len(table[row][col].strip()) > 0:
                        return table
                # Remove rightmost table column
                cols -= 1
                for row in table:
                    del row[cols]
        
        return table

if __name__ == "__main__":
    import sys
    if len(sys.argv) <= 1:
        print "Usage: Gnumeric file.gnumeric"
    else:
        for file in sys.argv[1:]:
            print ("========= %s ===========" % file)
            # logging.basicConfig(level=logging.NOTSET)
            table = GnumericReader.read(file)
            header = table[0]
            rows = table[1:]
            print "Header: ", header
            print "Rows: ", rows
