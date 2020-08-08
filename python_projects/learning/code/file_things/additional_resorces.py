# Writing to / Creating new file
'''
newfile = open("newfile.txt", "w+") # w+ tell that we can write to the file

string = "This is the content that will be written to the text file. "

newfile.write(string)
print(f"\nCreated newfile and wrote desired text.")
'''
#JSON Stuff
import simplejson as json
import os

#check if file exists
if os.path.isfile("./ages.json") and os.stat("./ages.json").st_size != 0:
        #if there is a file, open it
    old_file = open("./ages.json", "r+")
        #read and load into python usable format
    data = json.loads(old_file.read())
    print("\nCurrent age is", data["age"], "-- adding a year.")
    data["age"] = data["age"] + 1
    print("New age is", data["age"])
else:
        #if there isnt a file, make it
    old_file = open("./ages.json", "w+")
    data = {"name": "Nick", "age": 20}
    print("\nNo file found, setting default age to", data["age"])

old_file.seek(0) #make new stuff write over old rather than append to the end
old_file.write(json.dumps(data)) #dump data into file
