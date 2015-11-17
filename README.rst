addlyrics
=========

Adds lyrics (via getlyrics) to mp3 file

Usage
-----

::

    usage: addlyrics [-h] [-i INDEX] [--lang LANG] [--desc DESC] filename term

    positional arguments:
      filename              Filename of mp3 file to add lyrics
      term                  Search term, passed to getlyrics

    optional arguments:
      -h, --help            show this help message and exit
      -i INDEX, --index INDEX
                Song index, passed to getlyrics
      --lang LANG           Three letter code from ISO 639-2. Defaults to 'eng'
      --desc DESC           Description of lyrics. Defaults to 'Lyrics from
                azlyrics.com'

Installation
------------

Via ``pip``:

::

    pip3 install addlyrics

Alternatively:

-  Clone the repository, ``cd addlyrics``
-  Run ``python3 setup.py install`` or ``pip3 install -e``
