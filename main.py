class library:
  def __init__ (self, signupTime, booksPerDay, books):
    self.signupTime = signupTime
    self.books = books
    self.booksPerDay = booksPerDay

def getScore(books, libBooks):
  score = 0
  for i in range(len(libBooks)):
    score += books[libBooks[i]]
  return score

numBooks, numLibraries, numDays = map(int,input().split())

books = list(map(int, input().split()))

listOfTuples = []
setBooks = set()
libs = []

## Put the libraries in a dictionary using the score as the key
for i in range(numLibraries):
  libNumBooks, libSignupTime, libBooksPerDay = map(int,input().split())
  libBooks = list(map(int, input().split()))
  score = getScore(books, libBooks)
  libBooks = set(libBooks)
  listOfTuples.append((libNumBooks/libBooksPerDay, score, i))
  libs.append(library(libSignupTime,libBooksPerDay,libBooks))

l = len(listOfTuples)
count = 0

out = []


while numDays >= 0 and len(listOfTuples) > 0:
 # print(listOfTuples)
  count+=1
  m = max(listOfTuples)
  listOfTuples.remove(m)
  for s in libs[m[2]].books:
    setBooks.add(s)
  out.append(str(m[2]) + " " + str(len(libs[m[2]].books)))
  string = ""
  for b in libs[m[2]].books:
    string.append(b, end = " ")
  for j in range(len(listOfTuples)):
    newBooks = libs[listOfTuples[j][2]].books - setBooks
    newBooksPerDay = len(newBooks)/libs[listOfTuples[j][2]].booksPerDay
    score = getScore(books, list(newBooks))
    listOfTuples[j] = ((newBooksPerDay, score, listOfTuples[j][2]))
    libs[listOfTuples[j][2]] = library(libs[listOfTuples[j][2]].signupTime,libs[listOfTuples[j][2]].booksPerDay,newBooks)
  numDays -= libs[m[2]].signupTime
  
print(count)
for i in out:
  print(i)