# PNGCODER - Obfuscate any data
Encode any file to PNG image or WAV and vise versa, binary safe
### Warning! ###
**When converting to PNG, if the original file ends with one or more NUL control character, it will be removed after decoding back**

Usage of pngcoder:

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

Usage of wavcoder:

```
wavcoder [-h] [--quiet] [--decode] [--samplerate SAMPLERATE] [--channels CHANNELS] input_file output_file

positional arguments:
  input_file            Source file
  output_file           Destination file

optional arguments:
  -h, --help            show this help message and exit
  --quiet, -q           Quiet mode
  --decode, -d          If passed, input file will be decoded from WAV
  --samplerate SAMPLERATE, -s SAMPLERATE
                        Sample rate. Default: 8000
  --channels CHANNELS, -c CHANNELS
                        Number of channels. Default: 1
```