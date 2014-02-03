PLUGIN_NAME = 'Artist Sorting'
PLUGIN_AUTHOR = 'Donagh Horgan'
PLUGIN_DESCRIPTION = 'Sort artists with names beginning with "The" only.'
PLUGIN_VERSION = "1.0"
PLUGIN_API_VERSIONS = ["0.12", "0.15"]

from picard.metadata import register_album_metadata_processor
    
def add_artistsort(tagger, metadata, release):    
    try:
        artist = metadata["albumartist"]
    except:
        try:
            artist = metadata["albumartist"]
        except:
            artist = ""
    
    if len(artist) > 4 and artist[0:4].lower() == 'the ':
        artistsort = artist[4:] + ", " + artist[0:3]
    else:
        artistsort = artist
    
    metadata["artistsort"] = artistsort
    metadata["albumartistsort"] = artistsort

register_album_metadata_processor(add_artistsort)
