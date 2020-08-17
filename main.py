from position_reader import PositionReader
import argparse


PARSER = argparse.ArgumentParser()
PARSER.add_argument("filename", type=str)
ARGS = PARSER.parse_args()

READER = PositionReader(ARGS.filename)
DATA = READER.get_pos()
print(DATA)
