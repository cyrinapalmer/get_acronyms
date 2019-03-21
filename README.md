# get_acronyms
Fetches a list of unique acronyms from a PluralSight transcript

Notes:
- because PluralSight requires a paid subscription, traditional web scraping techniques don't allow access to the transcripts, so this program requires the transcripts to be stored in a variable. In this example, the transcripts are saved as a string in a separate file called pluralsight_transcripts.py, which is imported at the beginning of the script.
- this program also includes automated formatting to put each acronym into a Bootstrap 4.0 HTML descriptive list, which is copied onto the clipboard so it can be easily pasted elsewhere.
- it will also open a Wikipedia tab for each acronym for easy research. There are over 400 acronyms in this example, so do not run this unless you are ready for this request
