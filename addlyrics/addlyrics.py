#!/usr/bin/env python
from __future__ import print_function

import sys
import argparse

from getlyrics.getlyrics import get_lyrics
import mutagen.id3


def main():
    parser = argparse.ArgumentParser(prog="addlyrics")
    parser.add_argument("filename", help="Filename of mp3 file to add lyrics")
    parser.add_argument("term", help="Search term, passed to getlyrics")
    parser.add_argument("-i", "--index", help="Song index, passed to getlyrics", type=int)
    parser.add_argument("--lang", help="Three letter code from ISO 639-2. Defaults to 'eng'", default="eng")
    parser.add_argument("--desc", help="Description of lyrics. Defaults to 'Lyrics from azlyrics.com'", default="Lyrics from azlyrics.com")
    args = parser.parse_args()
    try:
        lyric = get_lyrics(args.term, index=args.index)
    except KeyboardInterrupt:
        print('', file=sys.stderr)
        return 130
    USLT = mutagen.id3.USLT(3, args.lang, args.desc, lyric)
    track = mutagen.id3.ID3(args.filename)
    track.add(USLT)
    track.save()
    return 0


if __name__ == "__main__":
    sys.exit(main())
