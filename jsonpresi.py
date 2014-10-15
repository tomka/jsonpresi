#!/usr/bin/env python
#
# Usage: ./jsonpresi.py input.json outputfolder
from __future__ import print_function

import sys
import json
import os

def create_html(title, text, next_page=None):
    pclick = "location.href='%s'" % next_page if next_page else ""
    return '''
    <html>
        <head>
            <link rel="stylesheet" type="text/css" href="style.css">
        </head>
        <body>
            <h1>%s</h1>
            <p onclick="%s">%s</p>
        </body>
    </html>
    ''' % (title, pclick, text)

def create_css():
    return """
    body {
        font-family: sans-serif;
    }
    h1 {
        font-size: 2.0em;
    }
    p {
        font-size: 1.5em;
    }
    """

def create_presentation(inputfile, outputfolder):
    try:
        data = json.load(inputfile)
    except ValueError as e:
        raise ValueError("Error while reading input data: " + str(e))

    if 'slides' not in data:
        raise ValueError("No slides property in input data found")

    # Write slides
    n_slides = len(data['slides'])
    for n, slide in enumerate(data['slides']):
        if 'title' not in slide:
            raise ValueError("No title property in slide %s" % n)
        if 'text' not in slide:
            raise ValueError("No text property in slide %s" % n)
        next_page = "%s.html" % (n+1) if n < n_slides -1 else None
        html = create_html(slide['title'], slide['text'], next_page)
        slidefile = open(os.path.join(outputfolder, "%s.html" % n), 'w')
        print(html, file=slidefile)
        slidefile.close()

    # Write a sample style file
    stylefile = open(os.path.join(outputfolder, "style.css"), 'w')
    print(create_css(), file=stylefile)
    stylefile.close()

if __name__ == "__main__":
    try:
        if len(sys.argv) < 3:
            raise ValueError("Need two arguments: inputfile and outputfolder")
        # Get arguments
        inputfilename = sys.argv[1]
        outputfolder = sys.argv[2]

        inputfile = open(inputfilename)

        if not os.access(outputfolder, os.W_OK):
            raise IOError("Cannot write to output folder")

        print("Input file: " + inputfilename)
        print("Output folder: " + outputfolder)
        create_presentation(inputfile, outputfolder)
    except Exception as e:
        print("An error occured: " + str(e))
    finally:
        if inputfile:
            inputfile.close()
