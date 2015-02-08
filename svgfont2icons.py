#!/usr/bin/env python

"""SVG Font-to-SVG Images Converter.
"""

SVG_ICON_TEMPLATE = """<?xml version="1.0" encoding="utf-8"?>
<!-- Generator: Adobe Illustrator 17.0.2, SVG Export Plug-In . SVG Version: 6.00 Build 0)  -->
<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">
<svg version="1.1" id="Layer_1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px"
   width="1200px" height="1200px" viewBox="0 0 1200 1200" xml:space="preserve">
<path d="{{ icon_path }}" transform="scale(1,-1) translate(0,-1200)"/>
</svg>
"""

import os
import sys
import argparse
from xml.etree import ElementTree


def main(arguments):

    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('svg_font_file', help="Input file", type=argparse.FileType('r'))

    args = parser.parse_args(arguments)

    data = args.svg_font_file.read()
    xml_doc = ElementTree.fromstring(data)

    if not os.path.exists('icons'):
        os.makedirs('icons')

    for glyph_node in xml_doc.findall('{http://www.w3.org/2000/svg}defs/{http://www.w3.org/2000/svg}font/{http://www.w3.org/2000/svg}glyph'):
        glyph_name = glyph_node.get('glyph-name')
        glyph_path = glyph_node.get('d')
        if glyph_name and glyph_path:
            print glyph_name
            icon_file = open(os.path.join('icons', glyph_name + '.svg'), 'w')
            icon_content = SVG_ICON_TEMPLATE.replace('{{ icon_path }}', glyph_path)
            icon_file.write(icon_content)
            icon_file.close()

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))