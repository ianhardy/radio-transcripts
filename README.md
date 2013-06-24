radio-transcripts
=================

radioscraper.py scrapes transcripts from [WAMU's](http://wamu.org/) website for (non-commercial!) research purposes.

## Usage

Run the scraper in a directory that does not contain directories called 'corpus' or 'transcript\_collection'. Change  the constants to reflect the details of the target show. URL\_STEM should not include the trailing '/'.

**Important**: the scrapetranscripturls() function needs to be changed as well. Change the first `url[##:##]` to return only the date of the show, and the second `url[##:##]` to return the first few letters of the show title without any '/''s.

Example:

    >>>url = 'http://thekojonnamdishow.org/shows/2013-06-10/tale-two-sequesters/transcript'

    >>>url[35:45]
    '2013-06-10'

    >>>url[46:50]
    'tale'

The result will be a corpus directory with clean files including only words spoken on the broadcast, and a transcript\_collection directory with files that include show title, speaker names, and timestamps.
