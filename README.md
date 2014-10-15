jsonpresi
=========

Converts a JSON file to a set of HTML pages. Usage:

    ./jsonpresi.py input.json outputfolder

The JSON file is expected to be organized like this:

    {
      "slides": [
        {
           "title": "Title 1",
           "text": "Text 1"
        },
        {
           "title": "Title 2",
           "text": "Text 2"
        }
      ]
    }
