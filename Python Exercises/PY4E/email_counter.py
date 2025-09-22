'''
Excercise 9.4 from Coursera Py4E Specialization - Data Structures: 

Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. 
The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. 
The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. 
After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.
'''

# Create shortcut to reach file path easily
fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "/Users/mashrufhossain/Desktop/Seed of Life 2.0/Columbia Business School JTC/VS Code Projects/Python Excercises/PY4E/mbox-short.txt"

# Create a handle to read the file
handle = open(fname)

# Create an empty dictionary to store email counts
counts = dict()

# Loop through each line in the file
for line in handle:
    # Create condition to check if line starts with "From "
    if line.startswith("From "):
        # Split the line into words
        words = line.split()
        # Extract the email address (second word)
        email = words[1]
        # Update the count for this email address in the dictionary
        counts[email] = counts.get(email, 0) + 1

    # Initialize variables to track the email with the highest count
    max_sender = None
    max_count = None

    # Loop through the dictionary using .items() to find the email with the highest count
    for sender, count in counts.items():
        # Compare current count with max_count
        if max_count is None or count > max_count:
            max_sender = sender
            max_count = count

# Print the email address with the highest count and the count itself
print(max_sender, max_count)

'''
Equivalent logic of .get() method:
if email in counts:
    counts[email] = counts[email] + 1
else:
    counts[email] = 1
'''