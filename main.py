#! python3
# takes input from code page and outputs only text transcript

import re, pyperclip, webbrowser, pluralsight_transcripts

# use ctrl-a to select code of transcript
# transcript code can be found here:
# https://app.pluralsight.com/learner/courses/(name of course)/transcript

code_input = pluralsight_transcripts.all

text_regex = re.compile(r'("text": ".*")')
text_found = text_regex.findall(code_input)
print(text_found)

full_text = ""
for each in text_found:
    text_only = each[9:-1]
    full_text += text_only

print(full_text)

# get acronyms

acronym_regex = re.compile(r'([A-Z]{2,8})')
acronyms_found = acronym_regex.findall(full_text)
print(acronyms_found)
print(len(acronyms_found))

unique_acronyms = []
for each in acronyms_found:
    if each not in unique_acronyms:
        unique_acronyms.append(each)

unique_acronyms.sort()
print(unique_acronyms)
print(len(unique_acronyms))

# lookup acronyms

for each in unique_acronyms:
    webbrowser.open("https://en.wikipedia.org/wiki/" + each)


# generate html. this code is to be inserted between the body tags of the html page

html = ""
for each in unique_acronyms:
    html += '''
    <dt class="col-sm-2">%s</dt>
    <dd class="col-sm-10">
        <p>Stands For This<br>
        - Some info about the term.</p>
    </dd>
    ''' % each

pyperclip.copy(html)
