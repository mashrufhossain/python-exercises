'''
Excercise 10.2 from Coursera Py4E Specialization - Data Structures: 

Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. 
You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
Once you have accumulated the counts for each hour, print out the counts, sorted by hour.
'''

name = input("Enter file:")
if len(name) < 1:
    name = "/Users/mashrufhossain/Desktop/Seed of Life 2.0/JTC/VS Code Projects/Completed Python Excercises/mbox-short.txt"
handle = open(name)

counts = {}

for line in handle:
    if line.startswith("From "):
        words = line.split()
        time = words[5]
        hour = time.split(":")[0]
        counts[hour] = counts.get(hour, 0) + 1

for hour, count in sorted(counts.items()):
    print (hour, count)
