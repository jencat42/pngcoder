#!/usr/bin/env python3
import argparse
import logging
import sys
import wave
import struct


def main():
    sample_rate = 8000
    FORMAT = '[%(asctime)-15s][%(levelname)s]: %(message)s'
    logging.basicConfig(format=FORMAT)
    logger = logging.getLogger('wavcoder')
    logger.setLevel("INFO")

    parser = argparse.ArgumentParser()
    parser.add_argument("--quiet", "-q", help="Quiet mode", action='store_true')
    parser.add_argument("--decode", "-d", help="If passed, source file will be decoded from WAV", action='store_true')
    parser.add_argument("--samplerate", "-s", help="Sample rate. Default: 8000", required=False, default=sample_rate, type=int)
    parser.add_argument("--channels", "-c", help="Number of channels. Default: 1", required=False, default=1, type=int)
    parser.add_argument("input_file", help="Source file")
    parser.add_argument("output_file", help="Destination file")
    args = parser.parse_args()

    if args.quiet:
        logger.setLevel("ERROR")

    infile = args.input_file
    outfile = args.output_file
    decode = args.decode
    sample_rate = args.samplerate

    if not decode:
        logger.info("Reading input file...")

        try:
            with open(infile, 'rb') as _if:
                data = _if.read()
                audio = bytearray(data)
        except Exception as e:
            print(e)
            sys.stderr.write("Error: Cannot read input file")
            sys.exit(1)


        wav_file = wave.open(outfile, "w")
        nchannels = args.channels
        sample_width = 1
        nframes = len(audio)
        comptype = "NONE"
        compname = "not compressed"
        wav_file.setparams((nchannels, sample_width, sample_rate, nframes, comptype, compname))

        logger.info("Generating WAV...")

        for sample in audio:
            smp = int(sample)
            wav_file.writeframes(struct.pack('B', smp))

        wav_file.close()
        logger.info("Done")
    else:
        try:
            wav_file = wave.open(infile, "r")
        except:
            sys.stderr.write("Error: Cannot read input file")
            sys.exit(1)
        frames = wav_file.readframes(wav_file.getnframes())
        data = bytes(bytearray([x for x in frames]))
        with open(outfile, 'wb') as of:
            of.write(data)
        logger.info("Decoded successfully")


if __name__ == "__main__":
    main()
