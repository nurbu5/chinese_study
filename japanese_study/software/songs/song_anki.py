import genanki

DECK_ID = 1371224683
DECK_NAME = "Songs and Poems"
JAPANESE_ENGLISH_SEPARATOR = "\n==========\n"

note_model = genanki.Model(1700099766,
                           'Song or Poem',
                           fields=[{'name': 'Order'},
                                   {'name': 'English Translation'},
                                   {'name': 'English Lyric Before'},
                                   {'name': 'English Lyric After'},
                                   {'name': 'Japanese Translation'},
                                   {'name': 'Japanese Lyric Before'},
                                   {'name': 'Japanese Lyric After'},
                                   {'name': 'Song'}],
                           templates=[{'name': 'English Lyrics',
                                       'qfmt': open('en_front.html', 'r').read(),
                                       'afmt': open('en_back.html', 'r').read()},
                                      {'name': 'Japanese Lyrics',
                                       'qfmt': open('jp_front.html', 'r').read(),
                                       'afmt': open('jp_back.html', 'r').read()}])

def main():
    filename = input("File Name: ")

    f = open("data/" + filename, "r")

    if f.mode == 'r':
        contents = f.read()
        deck = getDeck()

        addNotes(contents, deck, getSongName(filename))
        generatePackage(deck, filename)

def getDeck():
    return genanki.Deck(DECK_ID, DECK_NAME)

def getSongName(filename):
    if filename.endswith('.txt'):
        filename = filename[:-4]
    return filename

def generateNote(deck, data):
    note = genanki.Note(model=note_model, fields=[data['Order'],
                                                  data['English Translation'],
                                                  data['English Lyric Before'],
                                                  data['English Lyric After'],
                                                  data['Japanese Translation'],
                                                  data['Japanese Lyric Before'],
                                                  data['Japanese Lyric After'],
                                                  data['Song']])
    deck.add_note(note)

def addNotes(contents, deck, song_name):
    lyrics = contents.strip().split(JAPANESE_ENGLISH_SEPARATOR)
    japanese_lyrics = lyrics[0].split('\n\n')
    english_lyrics = lyrics[1].split('\n\n')
    num_blocks = len(japanese_lyrics)
    for i in range(num_blocks):
        note_data = {'Song': song_name, 'Order': str(i+1)}
        note_data['English Translation'] = english_lyrics[i]
        note_data['Japanese Translation'] = japanese_lyrics[i]
        if i > 0:
            note_data['English Lyric Before'] = english_lyrics[i - 1]
            note_data['Japanese Lyric Before'] = japanese_lyrics[i - 1]
        else:
            note_data['English Lyric Before'] = ''
            note_data['Japanese Lyric Before'] = ''
        if i < (num_blocks - 1):
            note_data['English Lyric After'] = english_lyrics[i + 1]
            note_data['Japanese Lyric After'] = japanese_lyrics[i + 1]
        else:
            note_data['English Lyric After'] = ''
            note_data['Japanese Lyric After'] = ''
        generateNote(deck, note_data)

def generatePackage(deck, filename):
    output_file = filename
    if output_file.endswith('.txt'):
        output_file = filename[:-4]
    genanki.Package(deck).write_to_file('anki-files/' + output_file + '.apkg')

if __name__== "__main__":
    main()

