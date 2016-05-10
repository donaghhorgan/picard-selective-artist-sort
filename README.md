# artistsort.py

An artist sorting plugin for MusicBrainz Picard that removes the definite article (i.e. "The") from artist sort names.

## Installation

To install the script, run Picard and select *Options* → *Options...* → *Plugins* → *Install plugin...* and select `artistsort.py`. Check the box next to the plugin to enable it.

## Usage

The plugin modifies track and album metadata by setting the `artistsort` and `albumartistsort` fields, respectively, to the artist's name without the prepended definite article.
