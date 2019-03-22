my_model = genanki.Model(
    1544700531,
    'Simple Model',
    fields=[
        {'name': 'Acronym'},
        {'name': 'Stands_For'},
        {'name': 'Desc'}
    ],
    templates=[
        {
            'name': 'Card 1',
            'qfmt': '{{Acronym}}',
            'afmt': '{{FrontSide}}<hr id="answer">{{Stands_For}}<hr id="answer">{{Desc}}',
        },
    ]
)

my_deck = genanki.Deck(
    1459472549,
    'Acronyms'
)

for i in range(len(acronym_list.acro)):
    my_note = genanki.Note(
        model=my_model,
        fields=[acronym_list.acro[i], acronym_list.stands_for[i], acronym_list.desc[i]]
    )

    my_deck.add_note(my_note)

genanki.Package(my_deck).write_to_file('C:\\Users\\cyrin\\Documents\\AnkiDecks\\comptia_acronyms.apkg')
