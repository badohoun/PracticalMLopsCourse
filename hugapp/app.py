import hug
import json 

# Load Data 
with open("books.json") as f:
    data = json.load(f)

# API
@hug.get('/api/v1/books')
@hug.local()
def get_books():
    """Show All Books"""
    return {"results":data}

@hug.get('/api/v1/books/fields')
def get_book(title:hug.types.text):
    """Get Book By Title"""
    book = [ book for book in data if book["title"] == title ]
    return {"results": book}

if __name__ == '__main__':
    get_books.interface.cli()