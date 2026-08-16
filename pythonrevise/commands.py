# git status -- this tells us whether we have files that git see as changed/new 
#git add . -- add all the new/changed files in the folder to staging area 
#staging area--

#HOW DO WE GET TO KNOW IF THE FILES ARE READY TO COMMIT?? -- the "new file" will be entered in green , which means git is ready to inlcude them in  a commit

#WHAT IS COMMIT??
#commit basically means save a copy of my current work with this message,,, commit does not upload to GitHub, it lives locally in our codespace


#THERE ARE 3 FILES A,B,C we do make changes to all the three files with out add. 

#now we do add A.py        now we are telling git that i want the changes i made in A.py to be included in my next commit so A.py moves into staging area 

#only after the previous step we do  git commit-m update A  : here in this step git takes whatever there is in staging area 

#WHY DO WE NEED THAT EXTRA  STEP OF STAGING?? because when we have made changes with 10 files but commit only 2 files , that staging area allows us to choose
# the file we wanna commit 
# 

def repeatingelement():
    marks=[]
    for i in range(5):
        x=int(input("enter the elements:"))
        marks.append(x)
    found=False
    for i in range(len(marks)):
        for j in range(i):
            if marks[i]==marks[j]:
                print(marks[i])
                found=True
                break
        if found:
            break
repeatingelement()
        
