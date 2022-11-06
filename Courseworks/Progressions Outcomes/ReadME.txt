# Predict-Progression-Outcome

This program was developed for my Computer Science course work in my first semester in University using Python.
The code predicts the progression outcomes of the students at the end of each academic year based on 3 inputted value by the user: Pass, Defer & Fail.
Based on the 3 inputted values the outcomes will be one of these: Progress, Progress (module trailer), Do not Progress - module retriever or Exclude.
The code only accept integers values and the numbers must be in the range 0, 20, 40, 60, 80, 100 and 120.

The progression outcome is given if:
1. Progress: Pass = 120, Defer = 0 & Fail = 0
2. Progress (module trailer): Pass = 100, Defer + Fail = 20
3. Do not Progress - module retriever: Pass < 100, Defer <= 120 & Fail <= 60
4. Exclude: Pass <= 40, Defer <= 40 & Fail >= 80

The program loops allowing the user to predict the progression outcomes for multiple students. If the user enters 'q' the loop is broken, otherwise if they enter 'y' the loop will stil function.

After the loop is broken a Histogram will be outputted to the user with the number of the credits and the progression outcome for each student, together with the total number of the progression outcomes represented in this format '(Progression outcome) N : * x N' where N represent how many time that outcome has been repeated.

The output is shown in the format mentioned above or in a list in Part 2, or together with the student ID in Part 4. Part 3 display the same values written in a text file, while in the loop, which are then read and outputted once the loop is broken.
