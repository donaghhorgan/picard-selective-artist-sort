PLUGIN_NAME = 'Artist Sorting'
PLUGIN_AUTHOR = 'Donagh Horgan'
PLUGIN_DESCRIPTION = 'Sorts artists whose names begin with "The".'
PLUGIN_VERSION = "1.01"
PLUGIN_API_VERSIONS = ["0.12", "0.15"]

from picard.metadata import register_album_metadata_processor
from picard.metadata import register_track_metadata_processor
    
def add_albumartistsort(tagger, metadata, release):    
    try:
        artist = metadata["albumartist"]
    except:
        try:
            artist = metadata["artist"]
        except:
            artist = None
    
    if artist:
        if len(artist) > 4 and artist[0:4].lower() == 'the ':
            artistsort = artist[4:] + ", " + artist[0:3]
        else:
            artistsort = artist
        
        metadata["albumartistsort"] = artistsort

def add_artistsort(tagger, metadata, release, track):    
    try:
        artist = metadata["artist"]
    except:
        try:
            artist = metadata["albumartist"]
        except:
            artist = None
    
    if artist:
        if len(artist) > 4 and artist[0:4].lower() == 'the ':
            artistsort = artist[4:] + ", " + artist[0:3]
        else:
            artistsort = artist
        
        metadata["artistsort"] = artistsort

register_album_metadata_processor(add_albumartistsort)
register_track_metadata_processor(add_artistsort)
