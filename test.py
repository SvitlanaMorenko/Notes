from collections import UserDict

class Note:
    def __init__(self, title, note_body):
        self.title = title
        self.note_body = note_body
        self.tegs = []

    def add_teg(self, teg):
        self.tegs.append(teg)
    
    def __str__(self):
        return f"Note title: {self.title}, tegs: {'; '.join(p for p in self.tegs)}, note boby: {self.note_body}"
    
    def change_note(self, new_text):
        self.note_body = new_text
        
    def del_teg(self, teg):
        if teg in self.tegs:
            self.tegs.remove(teg)
            return 'mission complete'
        return 'teg is not found'
    
class Notebook(UserDict):
    
    def add_note(self, note):
        if isinstance(note, Note):
            self.data[note.title] = note
    
    def find_note(self, title):
        for note in self.data.values():
            if title in note.title:
                return note
    
    def find_note_teg(self, teg):
        res = None
        res = []
        for note in self.data.values():
            if teg in note.tegs:
                res.append(note)
        return res
    
    def search(self, query: str):
        results = []
        for note in self.data.values():
            if query.lower() in note.note_body.lower():
                results.append(note)
        return results
    
    def delete(self, title):
        self.pop(title, None)



notebook = Notebook()

song = Note('Jingle Bells', 'Dashing through the snow\nIn a one-horse open sleigh')
song.add_teg('christmas')
song.add_teg('fun')

notebook.add_note(song)

shop_list = Note('Presents','Sweets, Cups, Cards')
shop_list.add_teg('christmas')
shop_list.add_teg('presents')

notebook.add_note(shop_list)

dishes = Note('Dishes', 'Snow ball ice-cream, Sweet cups, Fruits')
dishes.add_teg('christmas')
dishes.add_teg('party')

notebook.add_note(dishes)

print(notebook)

for i in notebook.search('fru'):
    print(i)
    
for i in notebook.search('snow'):
    print(i)
    
notebook.delete('Presents')
print(notebook)


    
    
    

    















