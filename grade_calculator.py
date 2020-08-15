from tkinter import*
import tkinter.ttk as ttk
import tkinter.messagebox as messagebox

# initial steps
root = Tk()
root.title("Grade Calculator")
root.geometry("480x740+450+30")

# Title 
titleLabel = Label(root, text = "Grade Calculator")
titleLabel.config(font = ("Arial", 20))
titleLabel.pack(side = "top")
######################################################
# Menu
menu = Menu(root)

fileMenu = Menu(menu, tearoff = 0)
fileMenu.add_command(label = "Quit", command = root.quit)
menu.add_cascade(label = "File", menu = fileMenu) # add filemenu to the overall menu tab
root.config(menu = menu) # apply the menu tab on the program

######################################################
# --- < Variable > ---
# Ask for Assignment Category Information
category = ""

# --- <Category Frame> ---
categoryFrame = LabelFrame(root, text = "Step 1. Put in info")
categoryFrame.config(font = ("Arial", 12))
categoryFrame.pack(side = "top", fill = "both", expand = True, pady = 5)

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
def getCategoryName(category):
    category = answerbox1.get()
    
# OK Button
btn1 = Button(categoryFrame, text = "OK", padx = 5, pady = 5, command = getCategoryName(category))
btn1.pack(side = "bottom")

#######################################################
''' Subject Frame: assignmentFrame > labelFrame > btnFrame '''

# --- < Variables > ---
# Average grade calculated
averageGrade = 0 # initial value


# ---0. <Subject Frame> ---
subjectFrame = LabelFrame(root, text = "Step 2. Enter the grades you got from each assignment.")
subjectFrame.config(font = ("Arial", 12))
subjectFrame.pack(side = "top", fill = "both", expand = True, pady = 5)


# ---1. <Assignment Frame> ---
assignmentFrame = LabelFrame(subjectFrame, text = "Grades obtained:")
assignmentFrame.pack(side = "top", fill = "both", expand = True)

# List of things
scrollbar = Scrollbar(assignmentFrame) # scrollbar for this list
scrollbar.pack(side = "right", fill = "y")

gradelistbox = Listbox(assignmentFrame, selectmode = "extended", height = 0, yscrollcommand = scrollbar.set)
gradelistbox.pack(side = "left", fill = "both", expand = True)
scrollbar.config(command = gradelistbox.yview)


# --- 1.5 <Other Info Frame> ---
infoFrame = Frame(subjectFrame)
infoFrame.pack(side = "top", fill = "x", expand = True)

# Get Percentage Weight for this Category
scoreEntryLabel = Label(infoFrame, text = "Weight for this Category(%) :")
scoreEntryLabel.pack(side = "left")

newScoreEntry = Entry(infoFrame, width = 20)
newScoreEntry.pack(side = "left", ipady = 4)

# Get Each individual score(s)
scoreEntryLabel = Label(infoFrame, text = "Add Score :")
scoreEntryLabel.pack(side = "left")

newScoreEntry = Entry(infoFrame, width = 20)
newScoreEntry.pack(side = "left", ipady = 4)



# 2. --- <Button Frame> + Entry to add new score ---
btnFrame = Frame(subjectFrame)
btnFrame.pack(side = "top", fill = "x", expand = True)

# methods for the button
def deleteScore():
    print(gradelistbox.curselection())
    for i in range (0, gradelistbox.size()):
        if gradelistbox.curselection() == (i,):
            gradelistbox.delete(i)

def addScore():
    if newScoreEntry.get().lower().islower():
        messagebox.showinfo("Invalid Input", "Put in only number")
        newScoreEntry.delete(0, END) # Clear the message box
    elif newScoreEntry.get() == "": # If the user does not put in anything 
        messagebox.showinfo("Invalid Input", "Put in your score")
        newScoreEntry.delete(0, END) # Clear the message box
    elif 0 > float(newScoreEntry.get()) or float(newScoreEntry.get()) > 100 : # If the user input score is invalid 
        messagebox.showinfo("Invalid Input", "Score has to be inbetween 0 and 100")
        newScoreEntry.delete(0, END) # Clear the message box
    else :
        gradelistbox.insert(END, newScoreEntry.get()) # Insert user input grade on the list
        newScoreEntry.delete(0, END) # Clear the message box


def calculateScore():
    pass

# Calculate Button
calculateBtn = Button(btnFrame, text = "Calculate", padx = 5, pady = 5, command = calculateScore)
calculateBtn.pack(side = "right", padx = 3)

# Delete Button
deleteBtn = Button(btnFrame, text = "Delete", padx = 5, pady = 5, command = deleteScore)
deleteBtn.pack(side = "right", padx = 3)

# Save Button
saveBtn = Button(btnFrame, text = "Add", padx = 5, pady = 5, command = addScore)
saveBtn.pack(side = "right", padx = 3)




# --- 3. <Label Frame> ---
labelFrame = Frame(subjectFrame)
labelFrame.pack(side = "top", fill = "both", expand = True)

# <Average Points>
averagePoint = Label(labelFrame, text = str(averageGrade) + "pts earned") # shows the score
averagePoint.config(font = ("Arial", 12))
averagePoint.pack(side = "right")


########################################################
# --- <overall GPA Frame> ---
finalFrame = LabelFrame(root, text = "Step 3. Get your final average grade for this subject.")
finalFrame.config(font = ("Arial", 12))
finalFrame.pack(side = "bottom", fill = "both", expand = True)



#######################################################
root.mainloop()