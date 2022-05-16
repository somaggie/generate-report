# generate-report
 takes a sample Amazon Spending report and gives back a cleaned version
I created this project as a part of a class I took this past semester, Spring 2022.
---
 How I solved this problem.

After reading the problem, I first started looking at the python documentation to look for methods that could possibly benefit me. I came across the readlines() method and looked into more information on the split() method to see how I could possibly use these to my advantage. I also saw information on exception handling on the python docs which I used to my advantage here. 

Then I started to break the problem into pieces. first was opening and reading the file in a way that I could easily manipulate the pieces. I used the readlines() method for this since it will save the file as a list of strings. I split the massive and ugly list up using the split() method and saved this as my contentList. I choose to make the contentList a variable in the class since every time a file would be open it would need this but it would be different for each instance of the class. 

The next step was to find a way to get only the information I wanted from the list. I noticed the order ID, UNSPSC code, and purchase price were 1, 5, and 7 in the lists respectively. I added each to their own list since it would help me present the information nicely when I go to write to the new clean report.

Next it was time to write to the new file. I used a for loop based on the length of the order ID since that was the leading information. I looped through each list, order ID, UNSPSC code, and purchase price, so each entry would be formatted neatly. the newlines were also saved into the content list so this is where I used the exception handling to handle the index error. I figured this was safe since it was a simple index error. After this I closed my file.
---
What I learned:
*reading files in python
*writing files in python
*closing files in python
*using classes
*using lists
*using lists methods
*python excceptions
*general file organization 
