import string
import psycopg2
import genanki

note_model = genanki.Model(14263,
                           'Chinese card',
                           fields=[{'name': 'Character'}, {'name': 'Pinyin'}, {'name': 'Definition'}],
                           templates=[{'name': 'Card 1',
                                       'qfmt': '{{Character}}',
                                       'afmt': '{{FrontSide}}<hr id="answer">Pinyin: {{Pinyin}}<br/>Meaning: {{Definition}}'}])

def main():
    filename = input("File Name: ")

    f = open("stories/" + filename, "r")

    if f.mode == 'r':
        contents = f.read()
        uniq_contents = list(set(contents))

        conn = psycopg2.connect(host="localhost", database="hanzidb", user="dawa")#user="dawa")
        cur = conn.cursor()

        deck = generateDeck(filename)

        for char in uniq_contents:
            data = getCharacterData(char, cur)
            if data != None:
                generateNote(deck, data)
        cur.close
        generatePackage(deck, filename)

def getCharacterData(char, cursor):
    cursor.execute('SELECT character, pinyin, definition FROM characters WHERE character = \'' + char + '\' AND definition IS NOT NULL')
    return cursor.fetchone()


def generateDeck(filename):
    deck_id = abs(hash(filename)) % (10 ** 7)
    if filename.endswith('.txt'):
        filename = filename[:-4]

    return genanki.Deck(deck_id, filename)

def generateNote(deck, data):
    note = genanki.Note(model=note_model, fields=[data[0], data[1], data[2]])
    deck.add_note(note)

def generatePackage(deck, filename):
    output_file = filename
    if output_file.endswith('.txt'):
        output_file = filename[:-4]
    genanki.Package(deck).write_to_file('anki-files/' + output_file + '.apkg')


if __name__== "__main__":
    main()

