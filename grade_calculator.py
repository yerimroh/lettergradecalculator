from tkinter import*
import tkinter.ttk as ttk

# initial steps
root = Tk()
root.title("Grade Calculator")
root.geometry("480x740")

# Title 
titleLabel = Label(root, text = "Grade Calculator")
titleLabel.config(font = ("Arial", 15))
titleLabel.pack(side = "top")
######################################################
# Menu
menu = Menu(root)

fileMenu = Menu(menu, tearoff = 0)
fileMenu.add_command(label = "Quit", command = root.quit)
menu.add_cascade(label = "File", menu = fileMenu) # add filemenu to the overall menu tab
root.config(menu = menu) # apply the menu tab on the program

######################################################
# Ask for Assignment Category Information

categoryFrame = Frame(root)
categoryFrame.pack(side = "top", fill = "both", expand = True)

# ask for the name
question1 = Label(categoryFrame, text = "What type of assignment is this?")
question1.pack(side = "left")

# <Entry Box>
def clickClear(event): # clear entry box when clicked
    answerbox1.delete(0, END) # delete everything in the box

answerbox1 = Entry(categoryFrame, width = 32) # Create Entry box
answerbox1.insert(END, "e.g) Exam, Project, Attendance, etc.") # initial label to begin with
answerbox1.bind("<1>", clickClear) # Bind with the clickClear method
answerbox1.pack(side = "right")

# get the name of the assignment category
category = ""
def getCategoryName(category):
    category = answerbox1.get()
    

btn1 = Button(categoryFrame, text = "OK", command = getCategoryName(category))
btn1.pack(side = "bottom")

#######################################################
# <Assighment Frame>
averageGrade = 0

subjectFrame = Frame(root)
subjectFrame.pack(side = "bottom", fill = "both", expand = True)

# individual assignment grades(keep them in a list)
subgrades = ["", "", "", "", ""] # initial given 5

# <Assignment Frame>
assignmentFrame = Frame(subjectFrame)
assignmentFrame.pack(fill = "both", expand = True)

# <Weight Percentage Entry>
percentEntry = Entry(subjectFrame, width = 28)
percentEntry.insert(END, "Percent weight of this category") # initial label to begin with

# Method used to eliminate the inital instruction
def clickClear2(event): # clear entry box when clicked
    percentEntry.delete(0, END) # delete everything in the box

percentEntry.bind("<1>", clickClear2) # Bind with the clickClear method
percentEntry.pack(side = "left")

percentLabel = Label(subjectFrame, text = "%")
percentLabel.pack(side = "left")

# <Average Points>
averagePoint = Label(subjectFrame, text = str(averageGrade) + "pts earned")
averagePoint.pack(side = "right")


########################################################
# overall GPA Frame
finalFrame = Frame(root)
finalFrame.pack(side = "bottom", fill = "both", expand = True)




#######################################################
root.mainloop()