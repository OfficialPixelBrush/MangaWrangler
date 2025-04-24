from pypdf import PdfReader, PdfWriter

# Input and output file paths
input_path = "arc_001_unfuckt.pdf"
output_path_front = "reversed_front.pdf"
output_path_back = "reversed_back.pdf"

# Read the original PDF
reader = PdfReader(input_path)
writer_front = PdfWriter()
writer_back = PdfWriter()

n = int(len(reader.pages))

if (n%4!=0):
    print(f"Page number not divisible by four (is {n}!")
    exit()

for k in range(1,int(n/4)+1,1):
    # Frontside
    a = 2*k-1
    b = n - 2*k + 2
    # Backside
    c = n - 2*k + 1
    d = 2*k

    #print([k*4,k*4+1,k*4+2,k*4+3])
    print([b-1,a-1])

    # Apply new mapping
    writer_front.add_page(reader.pages[b-1])
    writer_front.add_page(reader.pages[a-1])
    writer_back.add_page(reader.pages[d-1])
    writer_back.add_page(reader.pages[c-1])

# Write the new PDF
with open(output_path_front, "wb") as f:
    writer_front.write(f)

with open(output_path_back, "wb") as f:
    writer_back.write(f)

#print(f"Reversed PDF saved to '{output_path}'")