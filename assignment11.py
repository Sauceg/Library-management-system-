#open files
list_of_files = ['books.txt','students.txt','borrowers.txt','returns.txt']
print('These are list of files: ', list_of_files)
books_filename = input("Enter filename for books:")
students_filename = input("Enter filename for students:")
borrowers_filename = input("Enter filename for borrowers:")
returns_filename = input("Enter filename for returns:")

books = open(books_filename, "r").read().splitlines()
students = open(students_filename, "r").read().splitlines()
borrowers = open(borrowers_filename, "r").read().splitlines()
returns = open(returns_filename, "r").read().splitlines()

def bookData(books):
    bookIdData = {}
    for i in range(len(books)):
        books[i] = books[i].split("#")
        bookIdData[books[i][0]] = books[i][1:] 
        
    return bookIdData

#this function returns a list of all classes and a dictionary of student data indexed by student_id 
def studentData(students):
    classes = []
    student_id_data = {}
    
    for i in range(len(students)):
        students[i] = students[i].split(",")
        student_id_data[students[i][0]] = students[i][1:] 
        if students[i][2] not in classes:
            classes.append(students[i][2])
        
    return classes, student_id_data


def borrowersData(borrowers):
    booksBorrowed = []
    borrowerIdData = {}
    for i in range(len(borrowers)):
        borrowers[i] = borrowers[i].split(";")
        bookId = borrowers[i][0]
        booksBorrowed.append(bookId)
        borrowerIdData[bookId] = borrowers[i][1:]
        
        
    return borrowerIdData


def returnsData(returns):
    booksReturned = []
    returnIdData = {}
    for i in range(len(returns)):
        returns[i] = returns[i].split(";")
        bookId = returns[i][0]
        booksReturned.append(bookId)
        returnIdData[bookId] = returns[i][1:]
        
        
    return returnIdData

def getClasses(students):
    classes = []

def format_date(string):
    list_of_months= ['Jan ', 'Feb ', 'Mar ','Apr ','May ','Jun ','Jul ','Aug ', 'Sep ', 'Oct ','Nov ','Dec ']
    counter = 0
    year = ' 20'+string[:counter+2]
    month = list_of_months[int(string[counter+2:counter+4]) -1]
    day = string[counter+4:]+','
    date = month+ day +year
    return date 

def buildTable1(books_not_returned, students, books, class_name):
    table1 = []
    total_books = 0
    for book in books_not_returned:
        student_id = books_not_returned[book][0]
        student_name = students[student_id][0]
        student_class = students[student_id][1]
        book_title = books[book][0]
        due_date = format_date(books_not_returned[book][2])
        if student_class == class_name:
            table1.append([student_name, book_title, due_date])
            total_books += 1
            
    printTable1(table1, total_books)
    
def printTable1(table1, total_books):
    lines = '+' + ('-'*16) + '+' + ('-'*37)+ '+'+ ('-'*14) + '+'
    header = lines + '\n| student name'+ ' '*(16-len(' student name')) + '| book' + ' '*(37-len(' book')) + '| due date' + ' '*(14-len(' due date'))+'|\n' + lines
    print(header)
    for entry in table1:
        print('| '+ entry[0]+ ' '*(15-len(entry[0])) + '| '+entry[1][0:36] + ' '*(36-len(entry[1])) + '| '+ entry[2] + ' '*(13-len(entry[2]))+'|')
    print(lines)
    print("|" + ' Total Books' + ' '*(54-len(' Total Books')) +'|'+ ' '*(13-len(str(total_books)))+ str(total_books) + ' |')
    print(lines)     


def buildTable2(books, students, books_returned, class_name):
    table2 = []
    total_book_cost = 0
    for book_id in books_returned:
        state = books_returned[book_id][2]
        if int(state) == 1:
            student_id = books_returned[book_id][0]
            student_name = students[student_id][0]
            student_class = students[student_id][1]
            book_cost = books[book_id][2]
            if student_class == class_name:
                table2.append([student_name, book_cost])
                total_book_cost += float(book_cost)
                
    printTable2(table2, total_book_cost)
       

def printTable2(table2, total_book_cost):
    table2 = [["Bill Bryson", "15.67"]]
    line = '+' + ('-'*16) + '+' + ('-'*10)+ '+'
    header = line + '\n| student name'+ ' '*(16-len(' student name')) + '| due' +  ' '*(10-len(' due')) + '|\n' + line
    print(header)
    for entry in table2:
        print('| '+ entry[0] + ' '*(15-len(entry[0])) + '| '+ ' '*(7-len(str(entry[1])))+ "$"+ str(entry[1]) + ' |')   
    
    print( '+' + ('-'*16) + '+' + ('-'*10)+ '+')
    print('| Total Due' + ' '*(16-len(' Total Due')) + '|'+ ' '*(8-len(str(total_book_cost)))+ "$"+ str(total_book_cost) + ' |')
    print( '+' + ('-'*16) + '+' + ('-'*10)+ '+\n')    
  

classes,student_id_data = studentData(students)
book_id_data = bookData(books)
books_borrowed = borrowersData(borrowers)
books_returned = returnsData(returns)
books_not_returned = {book_id:value for book_id,value in books_borrowed.items() if book_id not in books_returned}
##classes = ["3B"]
for class_name in classes:
    print("Class: {0}".format(class_name))
    #build table 1
    buildTable1(books_not_returned, student_id_data, book_id_data, class_name)
    
    #build table 2
    buildTable2(book_id_data , student_id_data, books_returned, class_name)
    







  

  
  
  
  
  
  
  
  
  
  






