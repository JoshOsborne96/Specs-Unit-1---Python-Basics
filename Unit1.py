# Project Part 1:

noun = "python"
adjective ="awesome"

sentence = f"I believe that {noun} is {adjective}"

print(sentence)

book_name = "The Odyssey"
author = " Homer"

book_author = book_name + " by" + author
print (book_author)

book_sentence = f"{book_name} was written by {author}."

print(book_sentence)

publication_year = 1614

book_price = 10.99

is_awesome = True

print(type(is_awesome))



#-------------------------------------------------------------------------------------------

#Project Part 2: 

### Step 1 - Lists ###

# Fill in this list with several authors you are a fan of. At least 7 or 8 should do.
my_authors = ["F. Scott Fitzgerald", "J.K. Rowling", "Suzanne Collins", "Mark Twain", "George Orwell", "Ray Bradbury", "Agatha Christie"]

# Now let's add a new author to the end with the .append() method. Type your code below.

my_authors.append("Homer")

print(my_authors)

# Now let's remove an element in the list

my_authors.remove("Ray Bradbury")

print(my_authors)

# Example: my_authors.remove("H.G. Wells")

# Now access an element by it's index. (Remember it indexes start at 0.)

print(my_authors[4])

# Example: my_authors[2]


# Now slice the list.

print(my_authors[2:4])
# Example: my_authors[1:4]


### Step 2 - Tuples ###

# Create your tuple below. Assign it to a variable name you can reference later in the exercise.

my_tuple = ["F. Scott Fitzgerald", "J.K. Rowling", "Suzanne Collins", "Mark Twain", "George Orwell"]

print(my_tuple)
# Example: my_author_tuple = ("F. Scott Fitzgerald", "J.K. Rowling", "Ernest Hemingway", "Emily Dickenson", "George Orwell", "Ray Bradbury")


### Step 3 - Sets ###

# Create a set with your authors.

my_authors_set = {"F. Scott Fitzgerald", "J.K. Rowling", "Suzanne Collins", "Mark Twain", "George Orwell", "Ray Bradbury", "Agatha Christie"}
# Example: my_author_set = {"F. Scott Fitzgerald", "J.K. Rowling", "Ernest Hemingway", "Emily Dickenson", "George Orwell", "Ray Bradbury"}


my_authors_set.add("Charlotte Bronte")

print(my_authors_set)

# Code here
# Example: my_author_set.add("J.R.R. Tolkien")


# Try adding the same author again, and be sure to print your set.

my_authors_set.add("Charlotte Bronte")

print(my_authors_set)
# Example: my_author_set.add("J.R.R. Tolkien")



### Step 4 - For Loops ###

# Create a for-loop for each of the data-structures above.

for name in my_authors:
  print(name)

for name in my_tuple:
  print(name)

for name in my_authors_set:
  print(name)
# Example:

# for book in my_authors:
    # print(book)

# for book in my_authors_tuple:
    # print(book)

# for book in my_authors_set:
    # print(book)

#-------------------------------------------------------------------------------------------

#Project Part 3:

my_book = {
    "title": "The Hunger Games",
    "author": "Suzanne Collins",
    "year": 2008,
    "rating": 4.32,
    "pages": 374,
}

# Follow the instructions in this part of the project. Define and flesh out your function below, which should accept a dictionary as an argument when called, and return a string of the info in that book-dictionary in a user-friendly readable format.

def book_pars(book_dictionary):
  
  dictionary_sentence = f"{book_dictionary['title']} by {book_dictionary['author']} has a rating of {book_dictionary['rating']}. It was published in the year {book_dictionary['year']} and has {book_dictionary['pages']} pages."
  return dictionary_sentence
  

print(book_pars(my_book))



# Once you are finished with that function, create several more functions which return individual pieces of information from the book.

def title_pars(book_dictionary):
  title_return = book_dictionary["title"]
  return title_return
  
print(title_pars(my_book))

def author_pars(book_dictionary):
  author_return = book_dictionary["author"]
  return author_return

print(author_pars(my_book))

def year_pars(book_dictionary):
  year_return = book_dictionary["year"]
  return year_return

print(year_pars(my_book))

def rating_pars(book_dictionary):
  rating_return = book_dictionary["rating"]
  return rating_return

print(rating_pars(my_book))

def pages_pars(book_dictionary):
  pages_return = book_dictionary["pages"]
  return pages_return

print(pages_pars(my_book))

# Finally, create at least three new functions that might be useful as we expand our home library app. Perhaps thing of a way you could accept additional arguments when the function is called? Also, imagine you have a list filled with dictionaries like above.

def novel_function(book_dicitonary):
  if book_dicitonary["pages"] > 200:
    print("This book is a novel")
  else:
    print("This book is too short to be a novel")

novel_function(my_book)

def rating_function(book_dictionary):
  if book_dictionary["rating"] > 3.5:
    print("This is a great book!")
  else:
    None

rating_function(my_book)

def age_function(book_dictionary):
  age = 2022 - book_dictionary["year"]
  age_sentence = f'This book is {age} years old.'
  return age_sentence

print(age_function(my_book))


#------------------------------------------------------------------------------------------------------------------------

#Project Part 4:

### Step 1 - 2

## Create five input statements to gather user's book they want to input to the system. After that be sure to turn it into a function.
def create_new_book(book_dictionary):
  title = input("What's a title of a book you enjoy? - ")
  author = input("Who is the author of this book? - ")
  year = int(input("In what year was this book published? - "))
  rating = float(input("On a scale from 1-5, what do you rate this book? - "))
  pages = int(input("How many pages does this book contain? - "))


  return book_dictionary



### Step 2 - Type conversion

## Now convert the proper data-types front strings to either floats or ints depending on what it is. Feel free to comment out your old function so you don't get an error, or copy/paste and give it a new name.

# Code here



### Step 3 - Error handling

## Now take your previous function, and handle potential errors should the user type an answer that doesn't convert data-type properly.
# def create_new_book2():
#     title = input("What is the title of the book you would like to add? - ")
#     author = input("Who is the author of the book you would like to add? - ")
#     try:
#         year = int(input("In what year was this book published? - "))
#     except:
#         year = int(input("Please type a number? Example: 1996 - "))
#     try:
#         rating = float(input("On a scale from 1-5, what do you rate this book? - "))
#     except:
#         rating = int(input("Please type a number? - "))
#     try:
#         pages = int(input("How many pages does this book contain? - "))
#     except:
#         pages = int(input("Please type a number? - "))

#     book_dictionary = {
#         "title": title,
#         "author": author,
#         "year": year,
#         "rating": rating,
#         "pages": pages }

#     return book_dictionary

# create_new_book2()


### Step 4 - 5

## Now create a main menu function that gives the user options. Handle their choices with if/elif/else statements.
# books_library = [
# {
#     "title": "The Odyessy",
#     "author": "Homer",
#     "year": 1614,
#     "rating": 4,
#     "pages": 384
# },
# {
#     "title": "The Fault in Our Stars",
#     "author": "John Green",
#     "year": 2012,
#     "rating": 3,
#     "pages": 313
# },
# {
#     "title": "Animal Farm",
#     "author": "George Orwell",
#     "year": 1945,
#     "rating": 3.7,
#     "pages": 112
# }]

# def print_all_books(list_of_books):

#     print("Current library")

#     for book in list_of_books:
#         title = book["title"]
#         author = book["author"]
#         year = book["year"]
#         rating = book["rating"]
#         pages = book["pages"]

#         print(f"Title: {title}, Author: {author}, Year: {year}, Rating: {rating}, Pages: {pages}")


# def main_menu(books_library):

#     active = True

#     while active:
#         option = input("""
# Please select an option below
# Option 1: To add a book. 
# Option 2: Display all books. 
# Option 3: Exit menu. - 
#         """)

#         if option == "1":
#             books_library.append(create_new_book())
#         elif option == "2":
#             print_all_books(books_library)
#         elif option == "3":
#           print("Have a nice day!")
#           active = False
#         else:
#           print("Please type a valid menu option")

#     main_menu(books_library)

#------------------------------------------------------------------------------------------------------------------------

#Project Part 5:

### Step 1 - Store data in a .txt

## This step's instructions explains how to use the open() function, to write and read info from a .txt file. Follow the instructions to create and call a function to add a book, based off of the previous dictionaries for our library, to the .txt file properly formatted with commas as separators.

def create_new_book(books_library):
    title = input("What is the title of the book you would like to add? - ")
    author = input("Who is the author of the book you would like to add? - ")
    try:
        year = int(input("In what year was this book published? - "))
    except:
        year = int(input("Please type a number? Example: 1996 - "))
    try:
        rating = float(input("On a scale from 1-5, what do you rate this book? - "))
    except:
        rating = int(input("Please type a number? - "))
    try:
        pages = int(input("How many pages does this book contain? - "))
    except:
        pages = int(input("Please type a number? - "))

    with open(books_library, 'a') as file:
      file.write(f"{title}, {author}, {year}, {rating}, {pages}\n")

### Step 2 - Read data from a .txt

## Now take your previously create function which prints info about all the books in your library, but gets the info from a list, and make it work by reading the information in your home library's .txt document. This will take some new logic, but you can do it.
def book_list_to_dictionary(books_library): 
  books_list = []

  with open(books_library, "r") as f:
    file = f.readlines()
    
    for line in file:
        title, author, year, rating, pages = line.split(", ")

        books_list.append({

        "title": title,
        "author": author,
        "year": int(year),
        "rating": float(rating),
        "pages": int(pages)

        })
  return books_list



# print(display_all_books())
# def print_book(library):
#     print(f"Title: {library["title"]}, Author: {author}, Year: {year}, Rating: {rating}, Pages: {pages}")


### Step 3 - if __name__ == "__main__":

## Wrap your main menu function call in an "if __name__ == '__main__':" statement to ensure it doesn't accidentally run if this file is imported as a module elsewhere.

# Code this at the bottom of the script


### Step 4 - Expand and refactor

## Now follow the instructions in this final step. Expand your project. Clean up the code. Make your application functional. Great job getting your first Python application finished!
def print_book(book):
  print(f"Title: {book['title']}, Author: {book['author']}, Year: {book['year']}, Rating: {book['rating']}, Pages: {book['pages']}")

def display_all_books(books_library):
  print("Here are all the books in your library:")
  for book in book_list_to_dictionary(books_library):
      print_book(book)

def get_longest_book(books_library):
  list = book_list_to_dictionary(books_library)
  return max(list, key=lambda x: int(x["pages"]))

def get_shortest_book(books_library):
  list = book_list_to_dictionary(books_library)
  return min(list, key=lambda x: int(x["pages"]))

def get_highest_rated(books_library):
  list = book_list_to_dictionary(books_library)
  return max(list, key=lambda x: int(x["rating"]))

def get_loweset_rated(books_library):
  list = book_list_to_dictionary(books_library)
  return min(list, key=lambda x: int(x["rating"]) )


def main_menu(books_library):

    active = True

    while active:
        option = input("""
Please select an option below
Option 1: Add a book 
Option 2: Display all books
Option 3: See longest book
Option 4: See shortest book
Option 5: See highest rated book(s)
Option 6: See lowest rated books(s)
Option 7: Exit menu -->
        """)


        if option == "1":
            create_new_book(books_library)
        elif option == "2":
            display_all_books(books_library)
        elif option == "3":
          print("Here is the longest book in your library:")
          print_book(get_longest_book(books_library))
        elif option == "4":
          print("Here is the shortest book in your library:")
          print_book(get_shortest_book(books_library))
        elif option == "5":
          print("Here is your highest rated book in your library:")
          print_book(get_highest_rated(books_library))
        elif option == "6":
          print("Here is your lowest rated book in your library:")
          print_book(get_loweset_rated(books_library))
        elif option == "7"  :
          print("Have a nice day!")
          active = False
        else:
          print("Please type a valid menu option")


if __name__ == "__main__":
    main_menu("library.txt")


  