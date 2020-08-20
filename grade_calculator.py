from tkinter import*
import tkinter.ttk as ttk
import tkinter.messagebox as messagebox

# < Initial steps >
root = Tk()
root.title("Grade Calculator")
root.geometry("480x740+450+30")

# Title 
titleLabel = Label(root, text = "Grade Calculator")
titleLabel.config(font = ("Arial", 20))
titleLabel.pack(side = "top")
######################################################
# < Menu > 
menu = Menu(root)

fileMenu = Menu(menu, tearoff = 0)
fileMenu.add_command(label = "Quit", command = root.quit)
menu.add_cascade(label = "File", menu = fileMenu) # add filemenu to the overall menu tab
root.config(menu = menu) # apply the menu tab on the program
######################################################
# < Variables >
category = "" # Name of this Category
averageGrade = 0 # points earned for THIS single category
categoryGrades = [0] # points earned for each categories
finalGrade = 0 # Overall(Final) grade for this course

#####################################################################################
# < Methods >
# get the name of the assignment category / method for OK button
def getCategoryName():
    assignmentFrame.config(text = "Grades obtained on " + categorybox.get())
    global category
    category = categorybox.get()

# Check if the category name was given
def checkStep1():
    if len(category) > 0:
        return True
    else:
        return False

# method for delete button
def deleteScore(): # delete a score that is selected from the list if pressed
    if checkStep1():
        for i in range (0, gradelistbox.size()):
            if gradelistbox.curselection() == (i,):
                gradelistbox.delete(i)
    else :
        messagebox.showinfo("Missing Category Name", "Fill out the Category Name First.")

# method for add button
def addScore(): # add the new score on the list 
    if checkStep1():
        if newScoreEntry.get().lower().islower():
            messagebox.showinfo("Invalid Score Input", "Put in only number")
            newScoreEntry.delete(0, END) # Clear the message box
        elif newScoreEntry.get() == "": # If the user does not put in anything 
            messagebox.showinfo("Invalid Score Input", "Put in your score")
            newScoreEntry.delete(0, END) # Clear the message box
        elif 0 > float(newScoreEntry.get()) or float(newScoreEntry.get()) > 100 : # If the user input score is invalid 
            messagebox.showinfo("Invalid Score Input", "Score has to be inbetween 0 and 100")
            newScoreEntry.delete(0, END) # Clear the message box
        else :
            gradelistbox.insert(END, newScoreEntry.get()) # Insert user input grade on the list
            newScoreEntry.delete(0, END) # Clear the message box
    else:
        messagebox.showinfo("Missing Category Name", "Fill out the Category Name First.")

# method for calculate button
def calculateScore():
    if (checkStep1()):
        totalscore = 0
        for i in range (0, gradelistbox.size()):
            totalscore += float(gradelistbox.get(i))

        if (weightEntry.get().lower().islower()):
            messagebox.showinfo("Invalid Weight Input", "Put in only number")
            weightEntry.delete(0, END) # delete the weight box
        elif (weightEntry.get() == ""):
            messagebox.showinfo("Invalid Weight Input", "Put in category percentage weight")
            weightEntry.delete(0, END)
        elif 0 > float(weightEntry.get()) or float(weightEntry.get()) > 100:
            messagebox.showinfo("Invalid Weight Input", "Percentage weight has to be inbetween 0 - 100 %")
            weightEntry.delete(0, END)
        else :
            global averageGrade
            averageGrade = round((totalscore / gradelistbox.size()) * (float(weightEntry.get()) / 100), 2) # Calculate average points earned for this course
            pointsEarned.config(text = str(averageGrade) + "pts earned")
    else:
        messagebox.showinfo("Missing Category Name", "Fill out the Category Name First.")
    

# Saves the points earned to add altogether later
def saveScore(category, averageGrade, finalGrade, categoryGrades):
    if gradelistbox.size() > 0: # If the user has finished calculating points earned for one category
        categoryGrades.append(averageGrade) # add the points to the list to be calculated later
        allCategories.insert(END, category + ": " + str(averageGrade) + " pts.") # add the <earned point> to the list
        updateScore(finalGrade, categoryGrades) # Update the final grade label as new points are added

        # Reset everything
        averageGrade = 0 # Reset the category grade
        category = "" # Reset the category name
        gradelistbox.delete(0, gradelistbox.size()) # Reset the grade list
        weightEntry.delete(0, END) # Clear the percentage
        categorybox.delete(0, END) # Clear the category name 
    

# Update the final grade label on the bottom 
def updateScore(finalGrade, categoryGrades):
    for i in range(0, len(categoryGrades)):
        finalGrade += categoryGrades[i]
    finalGradeLabel.config(text = "Your Final Grade for this Course: " + str(finalGrade))


#####################################################################################
# < Frames >
#----------------------------------------- Step 1 Area
categoryFrame = LabelFrame(root, text = "Step 1. Put in info", height = 3, bd = 5)
categoryFrame.config(font = ("Arial", 12))



#----------------------------------------- Step 2 Area
# 0. <Subject Frame> / contains components on step 2 area
subjectFrame = LabelFrame(root, text = "Step 2. Enter the grades you got from each assignment.", height = 20, bd = 5)
subjectFrame.config(font = ("Arial", 12))

# 1. <Assignment Frame> / Contains the list for individual assignment grades
assignmentFrame = LabelFrame(subjectFrame, text = "Grades obtained on" + category)

# 2. <Additional information Frame> / Contains and stores the percentage weight and total points earned for one category
infoFrame = Frame(subjectFrame)

# 3. <Button Frame> / contains the buttons 
btnFrame = Frame(subjectFrame)

# 4. <Label Frame> / contains the label that reflects the final points earned for this category.
labelFrame = Frame(subjectFrame)



#----------------------------------------- Step 3 Area
# Bottom Frame
finalFrame = LabelFrame(root, text = "Step 3. Get your final average grade for this subject.", height = 20, bd = 5)
finalFrame.config(font = ("Arial", 12))

##########################################################################################################
# < Components >
#----------------------------------------- Step 1 Area
# First Question
question1 = Label(categoryFrame, text = "What type of assignment is this?\ne.g) Exam, Project, Attendance, etc.")

# Entry box to store the category name(type)
categorybox = Entry(categoryFrame, width = 32) # Create Entry box
# OK Button
btn1 = Button(categoryFrame, text = "OK", padx = 5, pady = 5, command = getCategoryName)



#----------------------------------------- Step 2 Area
scrollbar1 = Scrollbar(assignmentFrame) # scrollbar for this list
gradelistbox = Listbox(assignmentFrame, selectmode = "single", height = 0, yscrollcommand = scrollbar1.set) # the list to store points

weightEntryLabel = Label(infoFrame, text = "Weight for this Category(%) :") # label to give out instruction
weightEntry = Entry(infoFrame, width = 20) # entry box to store the percentage weight of this category

newScoreEntryLabel = Label(infoFrame, text = "Add Score :") # label to give out instruction 2
newScoreEntry = Entry(infoFrame, width = 20) # entry box to get the user input for individual assignment grade

# Buttons
calculateBtn = Button(btnFrame, text = "Calculate", padx = 5, pady = 5, command = calculateScore)
deleteBtn = Button(btnFrame, text = "Delete", padx = 5, pady = 5, command = deleteScore)
addBtn = Button(btnFrame, text = "Add", padx = 5, pady = 5, command = addScore)
saveBtn = Button(btnFrame, text = "Save Points Earned", padx = 5, pady = 5, command = lambda: saveScore(category, averageGrade, finalGrade, categoryGrades))

# Total points earned 
pointsEarned = Label(labelFrame, text = str(averageGrade) + "pts earned") # shows the score
pointsEarned.config(font = ("Arial", 12))



#----------------------------------------- Step 3 Area
scrollbar2 = Scrollbar(finalFrame) # Scrollbar that will bind to allCategories box
allCategories = Listbox(finalFrame, height = 5, yscrollcommand = scrollbar2.set) # listbox used to list out all categories

finalGradeLabel = Label(root, text = "Your Final Grade for this Course: " + str(averageGrade)) # label used to show the FINAL grade for this COURSE


############################################################################################
# < Packing >
# ----------------------------------------- Step 1 Area
categoryFrame.pack(side = "top", fill = "both", expand = True, pady = 5)
question1.pack(side = "left")
categorybox.pack(side = "right")
btn1.pack(side = "bottom")


#----------------------------------------- Step 2  Area
subjectFrame.pack(side = "top", fill = "both", expand = True, pady = 5)

# 1.--- <Assignment Frame> ---
assignmentFrame.pack(side = "top", fill = "both", expand = True)
scrollbar1.pack(side = "right", fill = "y")

gradelistbox.pack(side = "left", fill = "both", expand = True) # assignment grade list
scrollbar1.config(command = gradelistbox.yview)

# 2. --- <Information Frame> ---
infoFrame.pack(side = "top", fill = "x", expand = True) 

weightEntryLabel.pack(side = "left")
weightEntry.pack(side = "left", ipady = 4)
newScoreEntryLabel.pack(side = "left")
newScoreEntry.pack(side = "left", ipady = 4)

# 3. --- <Button Frame> + Entry to add new score ---
btnFrame.pack(side = "top", fill = "x", expand = True)

# Save Button
saveBtn.pack(side = "left", padx = 3)
# Calculate Button
calculateBtn.pack(side = "right", padx = 3)
# Delete Button
deleteBtn.pack(side = "right", padx = 3)
# Add Button
addBtn.pack(side = "right", padx = 3)

# 3. --- <Label Frame> ---
labelFrame.pack(side = "top", fill = "both", expand = True)
pointsEarned.pack(side = "right")



#----------------------------------------- Step 3 Area #####
finalFrame.pack(side = "top", fill = "both", expand = True)

# Listbox to show all different categories that is saved
allCategories.pack(side = "left", fill = "both", expand = True)
# Bind scrollbar2 to allCategories
scrollbar2.config(command = allCategories.yview)

# Last label to show the final grade of this course
finalGradeLabel.pack(side = "top")

#######################################################

root.mainloop()