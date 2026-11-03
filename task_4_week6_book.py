def search_book (books_file) :
    print ("searching ...")
    section = ""
    book = "book:\n"
    with open (books_file, "r") as file :
        for line in file :
            if line.startswith("Section:") :
                section += line
            else :
                book += line
        print ("Searching done")
        return f"{section}\n\n{book}"


def save (file_path, data) :
    print ("saving ...")
    with open (file_path, "w") as file :
        file.write(data)
        print ("done")


def run_task4 () :
    data = search_book("Books.txt")
    save ("section-books.txt", data)


if __name__ == "__main__":
        run_task4()



