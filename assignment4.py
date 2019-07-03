
import sys
file_source = sys.argv[1]
rows_and_columns = []
score = 0
game = True
count = 0
first = True
thevalue = 0

open_file = open(file_source,"r")
for line_in_file in open_file:
    colomns = []
    splited_columns = line_in_file.split()
    for splited_argument in splited_columns:
        colomns.append(splited_argument)
    rows_and_columns.append(colomns)
open_file.close()

def print_board():
    for readed_rows in rows_and_columns:
        for readed_columns in readed_rows:
            print(readed_columns+" ",end="")
        print("")
    print("\nYour score is:",score)

def crash_move(x,y,z):
    global count,first,game,thevalue
    thevalue = z
    if x > 0 and x < len(rows_and_columns)-1:
        if y > 0 and y < len(rows_and_columns[x])-1:
            val_of_this = z
            top_of_this = rows_and_columns[x-1][y]
            left_of_this = rows_and_columns[x][y-1]
            bot_of_this = rows_and_columns[x+1][y]
            right_of_this = rows_and_columns[x][y+1]
            if first:
                if val_of_this==top_of_this or val_of_this == right_of_this or val_of_this==left_of_this or val_of_this == bot_of_this:
                    rows_and_columns[x][y]= " "
                    count+=1
                    first = False
                    if val_of_this==top_of_this:
                        crash_move(x-1,y,z)
                    if val_of_this==bot_of_this:
                        crash_move(x+1,y,z)
                    if val_of_this==left_of_this:
                        crash_move(x,y-1,z)
                    if val_of_this==right_of_this:
                        crash_move(x,y+1,z)
                else:
                    game = False
            else:
                if rows_and_columns[x][y].strip()!="" and rows_and_columns[x][y].strip()!=" ":
                    count+=1
                rows_and_columns[x][y]= " "
                first = False
                if val_of_this==top_of_this:
                    crash_move(x-1,y,z)
                if val_of_this==bot_of_this:
                    crash_move(x+1,y,z)
                if val_of_this==left_of_this:
                    crash_move(x,y-1,z)
                if val_of_this==right_of_this:
                    crash_move(x,y+1,z)
        elif y == len(rows_and_columns[x])-1:
            val_of_this = z
            top_of_this = rows_and_columns[x-1][y]
            left_of_this = rows_and_columns[x][y-1]
            bot_of_this = rows_and_columns[x+1][y]
            if first:
                if val_of_this==top_of_this or val_of_this==left_of_this or val_of_this == bot_of_this:
                    rows_and_columns[x][y]= " "
                    count+=1
                    first = False
                    if val_of_this==top_of_this:
                        crash_move(x-1,y,z)
                    if val_of_this==bot_of_this:
                        crash_move(x+1,y,z)
                    if val_of_this==left_of_this:
                        crash_move(x,y-1,z)
                else:
                    game = False
            else:
                if rows_and_columns[x][y].strip()!="" and rows_and_columns[x][y].strip()!=" ":
                    count+=1
                rows_and_columns[x][y]= " "
                first = False
                if val_of_this==top_of_this:
                    crash_move(x-1,y,z)
                if val_of_this==bot_of_this:
                    crash_move(x+1,y,z)
                if val_of_this==left_of_this:
                    crash_move(x,y-1,z)
        elif y == 0:
            val_of_this = z
            top_of_this = rows_and_columns[x-1][y]
            right_of_this = rows_and_columns[x][y+1]
            bot_of_this = rows_and_columns[x+1][y]

            if first:
                if val_of_this==top_of_this or val_of_this==right_of_this or val_of_this == bot_of_this:
                    rows_and_columns[x][y]= " "
                    count+=1
                    first = False
                    if val_of_this==top_of_this:
                        crash_move(x-1,y,z)
                    if val_of_this==bot_of_this:
                        crash_move(x+1,y,z)
                    if val_of_this==right_of_this:
                        crash_move(x,y+1,z)
                else:
                    game = False
            else:
                if rows_and_columns[x][y].strip()!="" and rows_and_columns[x][y].strip()!=" ":
                    count+=1
                rows_and_columns[x][y]= " "
                first = False
                if val_of_this==top_of_this:
                    crash_move(x-1,y,z)
                if val_of_this==bot_of_this:
                    crash_move(x+1,y,z)
                if val_of_this==right_of_this:
                    crash_move(x,y+1,z)

    elif x == len(rows_and_columns)-1:
        if y > 0 and y < len(rows_and_columns[x])-1:
            val_of_this = z
            top_of_this = rows_and_columns[x-1][y]
            right_of_this = rows_and_columns[x][y+1]
            left_of_this = rows_and_columns[x][y-1]
            if first:
                if val_of_this==top_of_this or val_of_this==right_of_this or val_of_this == left_of_this:
                    rows_and_columns[x][y]= " "
                    count+=1
                    first = False
                    if val_of_this==top_of_this:
                        crash_move(x-1,y,z)
                    if val_of_this==left_of_this:
                        crash_move(x,y-1,z)
                    if val_of_this==right_of_this:
                        crash_move(x,y+1,z)
                else:
                    game = False
            else:
                if rows_and_columns[x][y].strip()!="" and rows_and_columns[x][y].strip()!=" ":
                    count+=1
                rows_and_columns[x][y]= " "
                first = False
                if val_of_this==top_of_this:
                    crash_move(x-1,y,z)
                if val_of_this==left_of_this:
                    crash_move(x,y-1,z)
                if val_of_this==right_of_this:
                    crash_move(x,y+1,z)
        elif y == len(rows_and_columns[x])-1:
            val_of_this = z
            top_of_this = rows_and_columns[x-1][y]
            left_of_this = rows_and_columns[x][y-1]
            if first:
                if val_of_this==top_of_this or val_of_this == left_of_this:
                    rows_and_columns[x][y]= " "
                    count+=1
                    first = False
                    if val_of_this==top_of_this:
                        crash_move(x-1,y,z)
                    if val_of_this==left_of_this:
                        crash_move(x,y-1,z)
                else:
                    game = False
            else:
                if rows_and_columns[x][y].strip()!="" and rows_and_columns[x][y].strip()!=" ":
                    count+=1
                rows_and_columns[x][y]= " "
                first = False
                if val_of_this==top_of_this:
                    crash_move(x-1,y,z)
                if val_of_this==left_of_this:
                    crash_move(x,y-1,z)
        elif y == 0:
            val_of_this = z
            top_of_this = rows_and_columns[x-1][y]
            right_of_this = rows_and_columns[x][y+1]

            if first:
                if val_of_this==top_of_this or val_of_this == right_of_this:
                    rows_and_columns[x][y]= " "
                count+=1
                first = False
                if val_of_this==top_of_this:
                    crash_move(x-1,y,z)
                if val_of_this==right_of_this:
                    crash_move(x,y+1,z)
                else:
                    game = False
            else:
                if rows_and_columns[x][y].strip()!="" and rows_and_columns[x][y].strip()!=" ":
                    count+=1
                rows_and_columns[x][y]= " "
                first = False
                if val_of_this==top_of_this:
                    crash_move(x-1,y,z)
                if val_of_this==right_of_this:
                    crash_move(x,y+1,z)
    elif x == 0:
        if y > 0 and y < len(rows_and_columns[x])-1:
            val_of_this = z
            bot_of_this = rows_and_columns[x+1][y]
            right_of_this = rows_and_columns[x][y+1]
            left_of_this = rows_and_columns[x][y-1]
            if first:
                if val_of_this==bot_of_this or val_of_this==right_of_this or val_of_this == left_of_this:
                    rows_and_columns[x][y]= " "
                    count+=1
                    first = False
                    if val_of_this==bot_of_this:
                        crash_move(x+1,y,z)
                    if val_of_this==left_of_this:
                        crash_move(x,y-1,z)
                    if val_of_this==right_of_this:
                        crash_move(x,y+1,z)
                else:
                    game = False
            else:
                if rows_and_columns[x][y].strip()!="" and rows_and_columns[x][y].strip()!=" ":
                    count+=1
                rows_and_columns[x][y]= " "
                first = False
                if val_of_this==bot_of_this:
                    crash_move(x+1,y,z)
                if val_of_this==left_of_this:
                    crash_move(x,y-1,z)
                if val_of_this==right_of_this:
                    crash_move(x,y+1,z)
        elif y == len(rows_and_columns[x])-1:
            val_of_this = z
            bot_of_this = rows_and_columns[x+1][y]
            left_of_this = rows_and_columns[x][y-1]
            if first:
                if val_of_this==bot_of_this or val_of_this == left_of_this:
                    rows_and_columns[x][y]= " "
                    count+=1
                    first = False
                    if val_of_this==bot_of_this:
                        crash_move(x+1,y,z)
                    if val_of_this==left_of_this:
                        crash_move(x,y-1,z)
                else:
                    game = False
            else:
                if rows_and_columns[x][y].strip()!="" and rows_and_columns[x][y].strip()!=" ":
                    count+=1
                rows_and_columns[x][y]= " "
                first = False
                if val_of_this==bot_of_this:
                    crash_move(x+1,y,z)
                if val_of_this==left_of_this:
                    crash_move(x,y-1,z)
        elif y == 0:
            val_of_this = z
            bot_of_this = rows_and_columns[x+1][y]
            right_of_this = rows_and_columns[x][y+1]
            if first:
                if val_of_this==bot_of_this or val_of_this == right_of_this:
                    rows_and_columns[x][y]= " "
                    count+=1
                    first = False
                    if val_of_this==bot_of_this:
                        crash_move(x+1,y,z)
                    if val_of_this==right_of_this:
                        crash_move(x,y+1,z)
                else:
                    game = False
            else:
                if rows_and_columns[x][y].strip()!="" and rows_and_columns[x][y].strip()!=" ":
                    count+=1
                rows_and_columns[x][y]= " "
                first = False
                if val_of_this==bot_of_this:
                    crash_move(x+1,y,z)
                if val_of_this==right_of_this:
                    crash_move(x,y+1,z)

def get_fibonacci(x):
    if x == 0 or x == 1:
        return x
    else:
        return get_fibonacci(x-2) + get_fibonacci(x-1)

def clear_board():
    if len(rows_and_columns)>0:
        will_delete = []
        for i in range(len(rows_and_columns[0])):
            val_count = 0
            for j in range(len(rows_and_columns)):
                val = rows_and_columns[j][i]
                val = val.strip()
                if val == "" or val == " ":
                    val_count += 1
            if len(rows_and_columns) == val_count:
                will_delete.append(i)
        will_delete.reverse()
        for i in will_delete:
            for j in range(len(rows_and_columns)):
                try:
                    rows_and_columns[j].pop(i)
                except IndexError:
                    pass
        for i in range(0,len(rows_and_columns[0])):
            for j in range(0,len(rows_and_columns)):
                for z in range(0,len(rows_and_columns)-1):
                    val_now = rows_and_columns[z][i]
                    val_after = rows_and_columns[z+1][i]
                    if val_after.strip() == "" or val_after.strip() == " ":
                        rows_and_columns[z][i] = val_after
                        rows_and_columns[z+1][i] = val_now
        keepit = []
        for i in range(len(rows_and_columns)):
            count_now = 0
            for j in range(len(rows_and_columns[i])):
                if rows_and_columns[i][j].strip()=="" or rows_and_columns[i][j].strip()==" ":
                    count_now+=1
            if count_now==len(rows_and_columns[i]):
                keepit.append(i)
        keepit.reverse()
        for q in keepit:
            rows_and_columns.pop(q)

def is_end():
    nb = 0
    for i in range(len(rows_and_columns)):
        for j in range(len(rows_and_columns[i])-1):
            thisval = rows_and_columns[i][j]
            nextval = rows_and_columns[i][j+1]
            thisval = thisval.strip()
            nextval = nextval.strip()
            if thisval == nextval:
                if thisval !="" and thisval!=" ":
                    nb+=1
    if len(rows_and_columns) > 0:
        for i in range(len(rows_and_columns[0])):
            for j in range(len(rows_and_columns)-1):
                thisval = rows_and_columns[j][i]
                botval = rows_and_columns[j+1][i]
                thisval.strip()
                botval.strip()
                if thisval == botval:
                    if thisval !="" and thisval !=" ":
                        nb+=1
    if nb==0:
        return True
    else:
        return False

def next_move():
    get_row_and_column = input("\nPlease enter a row and column number: ")
    split_get_row_and_column = get_row_and_column.split()
    get_row = int(split_get_row_and_column[0])-1
    get_column = int(split_get_row_and_column[1])-1
    if ((rows_and_columns[get_row])[get_column]==" "):
        print("\nPlease enter a correct size!")
        next_move()
    else:
        crash_move(get_row,get_column,rows_and_columns[get_row][get_column])
print_board()

while True:
    game=True
    first = True
    count = 0
    try:
        next_move()
    except IndexError:
        print("The Cell is out of bound")
    will_add = int(thevalue) * int(get_fibonacci(count))
    score+=will_add
    clear_board()
    print_board()
    end_control = is_end()
    if end_control:
        print_board()
        print("\nGame Over")
        break
    if game==False:
        print("\nTry Again")
