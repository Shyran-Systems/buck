from __future__ import absolute_import, division, print_function, unicode_literals

import os
import sys

from tools import impl


parser = impl.argparser()

parser.add_argument("-o", dest="output_dir", action=impl.StripQuotesAction)

(options, args) = parser.parse_known_args()

binary = args[0]
output_dir = os.path.join(options.output_dir, "Contents", "Resources", "DWARF")
os.makedirs(output_dir)
output_file = os.path.join(output_dir, os.path.basename(binary))

with open(output_file, "w") as output:
    output.write("dsymutil:\n")
    with open(binary, "r") as binfile:
        output.write(binfile.read())

sys.exit(0)