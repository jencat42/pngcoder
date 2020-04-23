# PNGCODER - Obfuscate any data
Encode any file to PNG image and vise versa, binary safe
### Warning! ###
**If the original file ends with one or more NUL control character, it will be removed after decoding back**

Usage:

```
pngcoder [--decode] [--quiet] [--verbose] input_file output_file

positional arguments:
  input_file     Source file
  output_file    Destination file

optional arguments:
  -h, --help     show this help message and exit
  --quiet, -q    Quiet mode
  --verbose, -v  If passed, a message will be shown for each row of image
                 decoding
  --decode, -d   If passed, source file will be decoded
```