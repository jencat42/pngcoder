#!/usr/bin/env python3
import argparse
import logging
import math
import sys
from pathlib import Path
from PIL import Image

FORMAT = '[%(asctime)-15s][%(levelname)s]: %(message)s'
logging.basicConfig(format=FORMAT)
logger = logging.getLogger('pngcoder')
logger.setLevel("INFO")


parser = argparse.ArgumentParser()
parser.add_argument("--quiet", "-q", help="Quiet mode", action='store_true')
parser.add_argument("--verbose", "-v", help="If passed, a message will be shown for each row of image decoding", action='store_true')
parser.add_argument("--decode", "-d", help="If passed, source file will be decoded", action='store_true')
parser.add_argument("input_file", help="Source file")
parser.add_argument("output_file", help="Destination file")
args = parser.parse_args()

if args.verbose and args.quiet:
    sys.stderr.write("Cannot use --quiet with --verbose")
    sys.exit(1)
if args.verbose:
    logger.setLevel("DEBUG")
if args.quiet:
    logger.setLevel("ERROR")

infile = args.input_file
outfile = args.output_file
decode = args.decode

if not decode:
    logger.info("Reading input file...")

    try:
        with open(infile, 'rb') as _if:
            data = _if.read()
    except:
        sys.stderr.write("Error: Cannot read input file")
        sys.exit(1)

    chunks = []
    current_chunk = []

    logger.info("Splitting on chunks...")

    for byte in bytearray(data):
        if len(current_chunk) == 3:
            chunks.append(current_chunk)
            current_chunk = []
        current_chunk.append(byte)

    while len(current_chunk) < 3:
        current_chunk.append(0)

    chunks.append(current_chunk)

    square_size = math.ceil(math.sqrt(len(chunks)))

    img = Image.new('RGB', (square_size, square_size))

    x = 0
    y = 0

    logger.info("Generating image...")

    for c in chunks:
        img.putpixel((x, y), tuple(c))
        x += 1
        if x == square_size:
            logger.debug(f"Row {y} generated")
            y += 1
            x = 0

    logger.info("Saving file...")

    try:
        img.save(outfile)
        enc_size = Path(outfile).stat().st_size
        logger.info(f"Initial size: {len(data)}, encoded size: {enc_size}")
        img.close()
    except:
        sys.stderr.write("Error: Cannot save output image")
else:
    logger.info("Reading image...")

    try:
        im = Image.open(infile)
    except:
        sys.stderr.write("Error: The input file provided is not a valid image")
        sys.exit(1)

    if im.size[0] != im.size[1]:
        sys.stderr.write("Error: The image provided is not valid, it must be square at least")
        sys.exit(1)

    square_size = im.size[0]
    pix = im.load()
    binary = bytearray()

    logger.info("Decoding image...")
    for y in range(square_size):
        for x in range(square_size):
            p = pix[x, y]
            for b in p:
                binary.append(b)

    im.close()
    binary = binary.rstrip(b"\0")

    try:
        with open(outfile, 'wb') as of:
            of.write(binary)
    except:
        sys.stderr.write("Error: Cannot open destination file for write")
        sys.exit(1)
