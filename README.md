# MangaWrangler
A python script for rearranging Comics into a printable format for binding

Instead of manually rearranging your comics or mangas pages to be easily printable, e.g. with two pages on one piece of A4, you can just run a `.pdf` of your comic through this script.

# How to use
```bash
python3 ./mangaWrangler.py manga.pdf
```

For more help, use `-h`/`--help`
```bash
python3 ./mangaWrangler.py --help
```

### I keep on getting "Page number not divisible by four"!
For this format of comic to work, the number of comic pages needs to be cleanly divisible by four. If it isn't, add some blank filler pages where appropriate.

## How to print
First, print the **front PDF**, then take the printed batch of pages, flip them around, and print the still blank side with the **back PDF**.