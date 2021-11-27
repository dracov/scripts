import csv
import xml.dom.minidom

#files open
# open the file in the write mode
f = open(r'C:\Users\aldmendo\Documents\scripts\newFile.csv', 'w',newline='')
#open file and read lines
temp = open(r'C:\Users\aldmendo\Documents\temp\to_Raspberry\nes_roms.txt','r').read().split('\n')
temp2 = xml.dom.minidom.parse(r'C:\Users\aldmendo\Documents\temp\to_Raspberry\NintendoEntertainmentSystem.xml');

#Variables Def
oldnames= []
newnames= []
row = []
#Fill information with good names

games = temp2.getElementsByTagName("game")
for game in games:
     newnames.append(game.getAttribute("name"))

#add and remove the .nes
for i in temp:
    oldnames.append(i.replace('.nes',''))

# create the csv writer 
writer = csv.writer(f)
# write a row to the csv file

header=['old_name','new_name','Found']
writer.writerow(header)

#Review if oldnames is inside the newname so we can write the goodline
for oldname in oldnames:
    for newname in newnames:
        if oldname in newnames:
           row=[oldname,newname,'Y']
        else:
           row=[oldname,'notfound','N']
    writer.writerow(row)

# close the file
f.close()



'''
s = "This be a string"
if s.find("is") == -1:
    print("No 'is' here!")
else:
    print("Found 'is' in the string.")

'''