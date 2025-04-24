import os
import sys
from pypdf import PdfReader, PdfWriter
import argparse
from pathlib import Path

parser = argparse.ArgumentParser(
                    prog='MangaWrangler',
                    description='A utility script for reordering comic pages for printing')

parser.add_argument('filename')
parser.add_argument('-o', '--output',
                    help="Output filename/location")
parser.add_argument('-r', '--reverse',
                    action='store_true',
                    help="Reverse the order of the pages")
#parser.add_argument('-s', '--split',
#                    action='store_true',
#                    help="Seperate the front and back pages into separate files")
parser.add_argument('-v', '--verbose',
                    action='store_true',
                    help="Shows progress messages")
args = parser.parse_args()

# Input and output file paths
input_path = args.filename
output_path = str(Path(input_path).with_suffix("")) + "_mw"
if (args.output != None and args.output != ""):
    output_path = str(Path(args.output).with_suffix(""))

output_path_front = output_path + "_front.pdf"
output_path_back = output_path + "_back.pdf"

# Read the original PDF
reader = PdfReader(input_path)
pages = reader.pages
if (args.reverse):
    pages = list(reversed(pages))
writer_front = PdfWriter()
writer_back = PdfWriter()

n = int(len(pages))

if (n%4 != 0):
    print(f"Page number not divisible by four (is {n}!")
    exit()

def print_progress_bar(progress, total, length=20):
    percent = progress / total
    bar = '=' * int(length * percent) + '-' * (length - int(length * percent))
    sys.stdout.write(f'\r[{bar}] {int(percent * 100)}%')
    sys.stdout.flush()

if (args.verbose):
    print("Sorting pages...")

for k in range(1,int(n/4)+1,1):
    # Frontside
    a = 2*k-1
    b = n - 2*k + 2
    # Backside
    c = n - 2*k + 1
    d = 2*k

    #print([k*4,k*4+1,k*4+2,k*4+3])
    #print([b-1,a-1])

    # Apply new mapping
    writer_front.add_page(pages[b-1])
    writer_front.add_page(pages[a-1])
    writer_back.add_page(pages[d-1])
    writer_back.add_page(pages[c-1])
    if args.verbose:
        print_progress_bar(k,int(n/4))

if (args.verbose):
    print("")
    
# Write the new PDF
if args.verbose:
    print(f"Writing Front to {os.path.basename(output_path_front)}...")
with open(output_path_front, "wb") as f:
    writer_front.write(f)

if args.verbose:
    print(f"Writing Back to {os.path.basename(output_path_back)}...")
with open(output_path_back, "wb") as f:
    writer_back.write(f)

if args.verbose:
    print(f"Finished rewriting!")