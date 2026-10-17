import requests

def get_random_book_info():
    url = "https://api.freeapi.app/api/v1/public/books/book/random"
    info = requests.get(url)
    data = info.json()

    if data ["success"] and "data" in data:
        book_info = data["data"]
        title = book_info["volumeInfo"]["title"]
        author = book_info["volumeInfo"]["authors"]
        Online_link = book_info["accessInfo"]["webReaderLink"]
        return title, author, Online_link
    else:
        raise Exception("Failed to fetch Book Info")

def main():
    try:
        title, author, Online_link = get_random_book_info()
        print(f"Book Title: {title} \nAuthor Name: {author} \nOnline Link: {Online_link}")
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()




