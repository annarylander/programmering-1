#1
def first_value(l):
    return l[0]

#2
def last_value(l):
    return l[-1]

# 3
def calc(l, b, h):
    return (l * b * h)

#4
def upper(s):
    return s.upper()

def lower(s):
    return s.lower()

#5
def evens(n):
  if n % 2 == 0:
    return True
  else:
    return False


#6
def get_days(month):
  if month == "February":
    return 28
  elif month == "April" or month == "June" or month == "September" or month == "November":
    return 30
  else:
    return 31


#7
library = [
{
"author": "Bill Gates",
"title": "The Road Ahead",
"reading_status": True
},
{
"author": "Steve Jobs",
"title": "Walter Isaacson",
"reading_status": True
},
{
"author": "Suzanne Collins",
"title":  "Mockingjay: The Final Book of The Hunger Games",
"reading_status": False
}
]


def check_book(arr):
  for book in arr:
    if (book["reading_status"] == True):
      print("Du har läst", book["title"])


check_book(library)








