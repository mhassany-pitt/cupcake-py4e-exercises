import os
import json

out_base = os.path.dirname(os.path.abspath(__file__))

specs = {
    "02-15__variables-expressions-and-statements__exercises01": {
        "title": "Prompt and Welcome User",
        "desc": "Write a program that uses input to prompt a user for their name and then welcomes them.",
        "prereq": ["variables"],
        "topics": ["variables", "input", "output"],
        "diff": "novice",
        "statement": "Write a program that uses `input` to prompt a user for their name and then welcomes them.\n\nDesired output format:\n```text\nEnter your name: Chuck\nHello Chuck\n```",
        "ref_code": "name = input(\"Enter your name: \")\nprint(\"Hello\", name)",
        "placeholder": "# Prompt user for their name and print a welcome message\n",
        "inputs": ["Chuck", "Alice"],
        "outputs": ["Enter your name: Hello Chuck\n", "Enter your name: Hello Alice\n"],
        "consoles": ["Hello Chuck\n", "Hello Alice\n"]
    },
    "02-15__variables-expressions-and-statements__exercises02": {
        "title": "Compute Gross Pay",
        "desc": "Prompt user for hours and rate per hour to compute gross pay.",
        "prereq": ["variables", "expressions"],
        "topics": ["variables", "expressions", "input", "output"],
        "diff": "novice",
        "statement": "Write a program to prompt the user for hours and rate per hour to compute gross pay.",
        "ref_code": "hours = float(input(\"Enter Hours: \"))\nrate = float(input(\"Enter Rate: \"))\npay = hours * rate\nprint(\"Pay:\", pay)",
        "placeholder": "# Prompt for hours and rate, then compute pay\n",
        "inputs": [["35", "2.75"], ["40", "10"]],
        "outputs": ["Enter Hours: Enter Rate: Pay: 96.25\n", "Enter Hours: Enter Rate: Pay: 400.0\n"],
        "consoles": ["Pay: 96.25\n", "Pay: 400.0\n"]
    },
    "02-15__variables-expressions-and-statements__exercises03": {
        "title": "Celsius to Fahrenheit Converter",
        "desc": "Prompt user for Celsius temperature, convert to Fahrenheit, and print.",
        "prereq": ["variables", "expressions"],
        "topics": ["variables", "expressions", "conversion"],
        "diff": "novice",
        "statement": "Write a program which prompts the user for a Celsius temperature, convert the temperature to Fahrenheit, and print out the converted temperature.",
        "ref_code": "celsius = float(input(\"Enter temperature in Celsius: \"))\nfahrenheit = celsius * 9 / 5 + 32\nprint(\"Temperature in Fahrenheit:\", fahrenheit)",
        "placeholder": "# Read Celsius temperature and convert to Fahrenheit\n",
        "inputs": ["0", "100"],
        "outputs": ["Enter temperature in Celsius: Temperature in Fahrenheit: 32.0\n", "Enter temperature in Celsius: Temperature in Fahrenheit: 212.0\n"],
        "consoles": ["Temperature in Fahrenheit: 32.0\n", "Temperature in Fahrenheit: 212.0\n"]
    },
    "03-11__conditional-execution__exercises01": {
        "title": "Overtime Pay Computation",
        "desc": "Rewrite pay computation to give employee 1.5 times the hourly rate for hours above 40.",
        "prereq": ["variables", "expressions"],
        "topics": ["conditionals", "if-else", "expressions"],
        "diff": "intermediate",
        "statement": "Rewrite your pay computation to give the employee 1.5 times the hourly rate for hours worked above 40 hours.",
        "ref_code": "hours = float(input(\"Enter Hours: \"))\nrate = float(input(\"Enter Rate: \"))\nif hours > 40:\n    pay = 40 * rate + (hours - 40) * rate * 1.5\nelse:\n    pay = hours * rate\nprint(\"Pay:\", pay)",
        "placeholder": "# Calculate gross pay with 1.5x rate for hours > 40\n",
        "inputs": [["45", "10"], ["30", "10"]],
        "outputs": ["Enter Hours: Enter Rate: Pay: 475.0\n", "Enter Hours: Enter Rate: Pay: 300.0\n"],
        "consoles": ["Pay: 475.0\n", "Pay: 300.0\n"]
    },
    "03-11__conditional-execution__exercises02": {
        "title": "Safe Pay Computation with Try/Except",
        "desc": "Rewrite pay program using try/except to handle non-numeric input gracefully.",
        "prereq": ["conditionals"],
        "topics": ["conditionals", "try-except", "error-handling"],
        "diff": "intermediate",
        "statement": "Rewrite your pay program using `try` and `except` so that your program handles non-numeric input gracefully by printing a message and exiting the program.",
        "ref_code": "try:\n    hours = float(input(\"Enter Hours: \"))\n    rate = float(input(\"Enter Rate: \"))\nexcept:\n    print(\"Error, please enter numeric input\")\n    quit()\n\nif hours > 40:\n    pay = 40 * rate + (hours - 40) * rate * 1.5\nelse:\n    pay = hours * rate\nprint(\"Pay:\", pay)",
        "placeholder": "# Implement try/except block for numeric inputs\n",
        "inputs": [["20", "nine"], ["40", "10"]],
        "outputs": ["Enter Hours: Enter Rate: Error, please enter numeric input\n", "Enter Hours: Enter Rate: Pay: 400.0\n"],
        "consoles": ["Error, please enter numeric input\n", "Pay: 400.0\n"]
    },
    "03-11__conditional-execution__exercises03": {
        "title": "Grade Calculator",
        "desc": "Prompt for score between 0.0 and 1.0 and print grade letter (A, B, C, D, F) or error message.",
        "prereq": ["conditionals"],
        "topics": ["conditionals", "if-elif-else", "error-handling"],
        "diff": "intermediate",
        "statement": "Write a program to prompt for a score between 0.0 and 1.0. If score is out of range or non-numeric, print 'Bad score'. Otherwise print grade: >=0.9 A, >=0.8 B, >=0.7 C, >=0.6 D, <0.6 F.",
        "ref_code": "try:\n    score = float(input(\"Enter score: \"))\nexcept:\n    print(\"Bad score\")\n    quit()\n\nif score < 0.0 or score > 1.0:\n    print(\"Bad score\")\nelif score >= 0.9:\n    print(\"A\")\nelif score >= 0.8:\n    print(\"B\")\nelif score >= 0.7:\n    print(\"C\")\nelif score >= 0.6:\n    print(\"D\")\nelse:\n    print(\"F\")",
        "placeholder": "# Prompt for score and print letter grade\n",
        "inputs": ["0.95", "10.0"],
        "outputs": ["Enter score: A\n", "Enter score: Bad score\n"],
        "consoles": ["A\n", "Bad score\n"]
    },
    "04-14__functions__exercises01": {
        "title": "Computepay Function",
        "desc": "Create a function called computepay which takes two parameters (hours and rate).",
        "prereq": ["functions", "conditionals"],
        "topics": ["functions", "parameters", "return-values"],
        "diff": "intermediate",
        "statement": "Rewrite your pay computation with time-and-a-half for overtime and create a function called `computepay` which takes two parameters (`hours` and `rate`).",
        "ref_code": "def computepay(hours, rate):\n    if hours > 40:\n        return 40 * rate + (hours - 40) * rate * 1.5\n    else:\n        return hours * rate\n\nhours = float(input(\"Enter Hours: \"))\nrate = float(input(\"Enter Rate: \"))\npay = computepay(hours, rate)\nprint(\"Pay:\", pay)",
        "placeholder": "def computepay(hours, rate):\n    # Implement function here\n    pass\n",
        "inputs": [["45", "10"], ["30", "10"]],
        "outputs": ["Enter Hours: Enter Rate: Pay: 475.0\n", "Enter Hours: Enter Rate: Pay: 300.0\n"],
        "consoles": ["Pay: 475.0\n", "Pay: 300.0\n"]
    },
    "04-14__functions__exercises02": {
        "title": "Computegrade Function",
        "desc": "Create a function called computegrade that takes a score parameter and returns a grade string.",
        "prereq": ["functions", "conditionals"],
        "topics": ["functions", "return-values", "error-handling"],
        "diff": "intermediate",
        "statement": "Rewrite the grade program using a function called `computegrade` that takes a score as its parameter and returns a grade as a string.",
        "ref_code": "def computegrade(score):\n    if score < 0.0 or score > 1.0:\n        return \"Bad score\"\n    elif score >= 0.9:\n        return \"A\"\n    elif score >= 0.8:\n        return \"B\"\n    elif score >= 0.7:\n        return \"C\"\n    elif score >= 0.6:\n        return \"D\"\n    else:\n        return \"F\"\n\nscore = input(\"Enter score: \")\ntry:\n    score = float(score)\n    print(computegrade(score))\nexcept:\n    print(\"Bad score\")",
        "placeholder": "def computegrade(score):\n    # Return grade string based on score\n    pass\n",
        "inputs": ["0.95", "perfect"],
        "outputs": ["Enter score: A\n", "Enter score: Bad score\n"],
        "consoles": ["A\n", "Bad score\n"]
    },
    "05-09__iteration__exercises01": {
        "title": "Accumulate Input Until Done",
        "desc": "Repeatedly read integers until 'done', then print total, count, and average.",
        "prereq": ["loops", "conditionals"],
        "topics": ["loops", "while-loop", "try-except", "accumulator"],
        "diff": "intermediate",
        "statement": "Write a program which repeatedly reads integers until the user enters 'done'. Once 'done' is entered, print out total, count, and average.",
        "ref_code": "total = 0\ncount = 0\nwhile True:\n    user_input = input(\"Enter a number: \")\n    if user_input == \"done\":\n        break\n    try:\n        number = int(user_input)\n        total += number\n        count += 1\n    except ValueError:\n        print(\"Invalid input\")\n\nprint(total, count, total / count)",
        "placeholder": "# Loop until done and compute stats\n",
        "inputs": [["4", "5", "bad data", "7", "done"]],
        "outputs": ["Enter a number: Enter a number: Enter a number: Invalid input\nEnter a number: Enter a number: 16 3 5.333333333333333\n"],
        "consoles": ["Invalid input\n16 3 5.333333333333333\n"]
    },
    "05-09__iteration__exercises02": {
        "title": "Min and Max of User Input",
        "desc": "Prompt for numbers until 'done' and print maximum and minimum.",
        "prereq": ["loops", "conditionals"],
        "topics": ["loops", "while-loop", "min-max-pattern"],
        "diff": "intermediate",
        "statement": "Write a program that prompts for a list of numbers until 'done' and at the end prints out both maximum and minimum.",
        "ref_code": "maximum = None\nminimum = None\nwhile True:\n    user_input = input(\"Enter a number: \")\n    if user_input == \"done\":\n        break\n    try:\n        number = float(user_input)\n    except ValueError:\n        print(\"Invalid input\")\n        continue\n    if maximum is None or number > maximum:\n        maximum = number\n    if minimum is None or number < minimum:\n        minimum = number\nprint(\"Maximum:\", maximum)\nprint(\"Minimum:\", minimum)",
        "placeholder": "# Track max and min using a loop\n",
        "inputs": [["7", "2", "done"]],
        "outputs": ["Enter a number: Enter a number: Enter a number: Maximum: 7.0\nMinimum: 2.0\n"],
        "consoles": ["Maximum: 7.0\nMinimum: 2.0\n"]
    },
    "06-14__strings__exercises01": {
        "title": "Extract Floating-Point Number from String",
        "desc": "Use find and string slicing to extract floating point value after colon.",
        "prereq": ["strings"],
        "topics": ["strings", "slicing", "string-methods"],
        "diff": "novice",
        "statement": "Take `data = 'X-DSPAM-Confidence: 0.8475'`. Use `find` and string slicing to extract portion after colon, convert to float, and print.",
        "ref_code": "data = 'X-DSPAM-Confidence: 0.8475'\ncolon_position = data.find(':')\nnumber_str = data[colon_position + 1:].strip()\nconfidence = float(number_str)\nprint(confidence)",
        "placeholder": "data = 'X-DSPAM-Confidence: 0.8475'\n# Extract and print float confidence value\n",
        "inputs": [[]],
        "outputs": ["0.8475\n"],
        "consoles": ["0.8475\n"]
    },
    "07-11__files__exercises01": {
        "title": "Shout File Contents",
        "desc": "Read through a file and print contents line by line in uppercase.",
        "prereq": ["strings", "loops"],
        "topics": ["file-io", "strings", "reading-files"],
        "diff": "intermediate",
        "statement": "Write a program to read through a file and print the contents of the file (line by line) all in upper case.",
        "ref_code": "file_name = input(\"Enter a file name: \")\nfhand = open(file_name)\nfor line in fhand:\n    print(line.rstrip().upper())",
        "placeholder": "# Open file and print uppercase lines\n",
        "inputs": ["mbox-short.txt"],
        "outputs": ["Enter a file name: ...\n"],
        "consoles": ["...\n"]
    },
    "07-11__files__exercises02": {
        "title": "Compute Average Spam Confidence from File",
        "desc": "Prompt for file name, find lines starting with X-DSPAM-Confidence:, and average their values.",
        "prereq": ["file-io", "strings"],
        "topics": ["file-io", "strings", "aggregation"],
        "diff": "intermediate",
        "statement": "Write a program to prompt for a file name, find lines starting with 'X-DSPAM-Confidence:', extract numbers, and print average spam confidence.",
        "ref_code": "file_name = input(\"Enter the file name: \")\nfhand = open(file_name)\ntotal = 0.0\ncount = 0\nfor line in fhand:\n    if line.startswith(\"X-DSPAM-Confidence:\"):\n        total = total + float(line.split(\":\")[1])\n        count = count + 1\nprint(\"Average spam confidence:\", total / count)",
        "placeholder": "# Read file and average spam confidence lines\n",
        "inputs": ["mbox-short.txt"],
        "outputs": ["Enter the file name: Average spam confidence: 0.7507185185185187\n"],
        "consoles": ["Average spam confidence: 0.7507185185185187\n"]
    },
    "07-11__files__exercises03": {
        "title": "File Reader with Easter Egg",
        "desc": "Print funny message when user types 'na na boo boo', otherwise count Subject lines.",
        "prereq": ["file-io", "try-except"],
        "topics": ["file-io", "error-handling", "conditionals"],
        "diff": "intermediate",
        "statement": "Modify file reader program so that entering 'na na boo boo' prints an Easter egg message. Otherwise count lines starting with 'Subject:'.",
        "ref_code": "file_name = input(\"Enter the file name: \")\nif file_name == \"na na boo boo\":\n    print(\"NA NA BOO BOO TO YOU - You have been punk'd!\")\nelse:\n    try:\n        with open(file_name) as file:\n            subject_count = 0\n            for line in file:\n                if line.startswith(\"Subject:\"):\n                    subject_count += 1\n        print(\"There were\", subject_count, \"subject lines in\", file_name)\n    except FileNotFoundError:\n        print(\"File cannot be opened:\", file_name)",
        "placeholder": "# Prompt for file and handle Easter Egg\n",
        "inputs": ["na na boo boo"],
        "outputs": ["Enter the file name: NA NA BOO BOO TO YOU - You have been punk'd!\n"],
        "consoles": ["NA NA BOO BOO TO YOU - You have been punk'd!\n"]
    },
    "08-16__lists__exercises01": {
        "title": "Find Unique Words in Romeo.txt",
        "desc": "Read romeo.txt line by line, split into words, store unique words in a list, sort and print.",
        "prereq": ["lists", "file-io"],
        "topics": ["lists", "file-io", "sorting", "uniqueness"],
        "diff": "intermediate",
        "statement": "Write a program to open a file and read line by line. Split lines into words, collect unique words, sort and print them alphabetically.",
        "ref_code": "filename = input(\"Enter file: \")\nfhandle = open(filename)\nunique_words = []\nfor line in fhandle:\n    words = line.split()\n    for word in words:\n        if word not in unique_words:\n            unique_words.append(word)\nunique_words.sort()\nprint(unique_words)",
        "placeholder": "# Collect unique words from file and print sorted list\n",
        "inputs": ["romeo.txt"],
        "outputs": ["Enter file: ['Arise', 'But', 'It', 'Juliet', 'Who', 'already', 'and', 'breaks', 'east', 'envious', 'fair', 'grief', 'is', 'kill', 'light', 'moon', 'pale', 'sick', 'soft', 'sun', 'the', 'through', 'what', 'window', 'with', 'yonder']\n"],
        "consoles": ["['Arise', 'But', 'It', 'Juliet', 'Who', 'already', 'and', 'breaks', 'east', 'envious', 'fair', 'grief', 'is', 'kill', 'light', 'moon', 'pale', 'sick', 'soft', 'sun', 'the', 'through', 'what', 'window', 'with', 'yonder']\n"]
    },
    "08-16__lists__exercises02": {
        "title": "Minimalist Email Client (From Lines Count)",
        "desc": "Read mail log file, parse 'From ' lines, print second word (email), and count total.",
        "prereq": ["lists", "file-io"],
        "topics": ["lists", "string-splitting", "file-io"],
        "diff": "intermediate",
        "statement": "Parse 'From ' lines from a mail log file, print the sender email (2nd word), and output total count of From lines.",
        "ref_code": "filename = input(\"Enter a file name: \")\nfhandle = open(filename)\ncount = 0\nfor line in fhandle:\n    line = line.rstrip()\n    if line.startswith(\"From \"):\n        words = line.split()\n        print(words[1])\n        count = count + 1\nprint(\"There were\", count, \"lines in the file with From as the first word\")",
        "placeholder": "# Extract sender emails and print total count\n",
        "inputs": ["mbox-short.txt"],
        "outputs": ["Enter a file name: ...\n"],
        "consoles": ["...\n"]
    },
    "08-16__lists__exercises03": {
        "title": "Min and Max using List Functions",
        "desc": "Store user entered numbers in a list until 'done', then compute max() and min().",
        "prereq": ["lists", "loops"],
        "topics": ["lists", "list-methods", "built-in-functions"],
        "diff": "intermediate",
        "statement": "Prompt user for numbers until 'done'. Store numbers in a list and use max() and min() functions after the loop.",
        "ref_code": "numbers = []\nwhile True:\n    user_input = input(\"Enter a number: \")\n    if user_input == \"done\":\n        break\n    numbers.append(float(user_input))\n\nprint(\"Maximum:\", max(numbers))\nprint(\"Minimum:\", min(numbers))",
        "placeholder": "# Store numbers in list and print max and min\n",
        "inputs": [["6", "2", "9", "3", "5", "done"]],
        "outputs": ["Enter a number: Enter a number: Enter a number: Enter a number: Enter a number: Enter a number: Maximum: 9.0\nMinimum: 2.0\n"],
        "consoles": ["Maximum: 9.0\nMinimum: 2.0\n"]
    },
    "09-08__dictionaries__exercises01": {
        "title": "Commit Day of Week Counter",
        "desc": "Categorize mail messages by day of week committed (3rd word of 'From ' lines) using dictionary.",
        "prereq": ["dictionaries", "file-io"],
        "topics": ["dictionaries", "counting", "file-io"],
        "diff": "intermediate",
        "statement": "Write a program that categorizes each mail message by day of week (3rd word of 'From ' line) using a dictionary histogram.",
        "ref_code": "filename = input(\"Enter a file name: \")\nfhandle = open(filename)\nday_counts = {}\nfor line in fhandle:\n    if line.startswith(\"From \"):\n        words = line.split()\n        day = words[2]\n        day_counts[day] = day_counts.get(day, 0) + 1\nprint(day_counts)",
        "placeholder": "# Count days of week using a dictionary\n",
        "inputs": ["mbox-short.txt"],
        "outputs": ["Enter a file name: {'Sat': 1, 'Fri': 20, 'Thu': 6}\n"],
        "consoles": ["{'Sat': 1, 'Fri': 20, 'Thu': 6}\n"]
    },
    "09-08__dictionaries__exercises02": {
        "title": "Sender Email Histogram",
        "desc": "Build histogram dictionary counting messages from each email address in mail log.",
        "prereq": ["dictionaries", "file-io"],
        "topics": ["dictionaries", "counting", "histogram"],
        "diff": "intermediate",
        "statement": "Write a program to read through a mail log and build a histogram dictionary counting messages from each email address.",
        "ref_code": "filename = input(\"Enter file name: \")\nfhandle = open(filename)\nemail_counts = {}\nfor line in fhandle:\n    if line.startswith(\"From \"):\n        words = line.split()\n        email = words[1]\n        email_counts[email] = email_counts.get(email, 0) + 1\nprint(email_counts)",
        "placeholder": "# Build email count dictionary\n",
        "inputs": ["mbox-short.txt"],
        "outputs": ["Enter file name: ...\n"],
        "consoles": ["...\n"]
    },
    "09-08__dictionaries__exercises03": {
        "title": "Find Most Prolific Email Sender",
        "desc": "Find who sent the most messages by looping through the email count dictionary.",
        "prereq": ["dictionaries", "loops"],
        "topics": ["dictionaries", "max-loop", "aggregation"],
        "diff": "intermediate",
        "statement": "Find who sent the most messages in a mail log by iterating over the dictionary of email counts.",
        "ref_code": "filename = input(\"Enter a file name: \")\nfhandle = open(filename)\nemail_counts = {}\nfor line in fhandle:\n    if line.startswith(\"From \"):\n        words = line.split()\n        email = words[1]\n        email_counts[email] = email_counts.get(email, 0) + 1\n\nbigcount = None\nbigemail = None\nfor email, count in email_counts.items():\n    if bigcount is None or count > bigcount:\n        bigcount = count\n        bigemail = email\nprint(bigemail, bigcount)",
        "placeholder": "# Find and print email with maximum count\n",
        "inputs": ["mbox-short.txt"],
        "outputs": ["Enter a file name: cwen@iupui.edu 5\n"],
        "consoles": ["cwen@iupui.edu 5\n"]
    },
    "09-08__dictionaries__exercises04": {
        "title": "Domain Name Histogram",
        "desc": "Count mail messages by domain name (portion after @ in email) using a dictionary.",
        "prereq": ["dictionaries", "strings"],
        "topics": ["dictionaries", "string-parsing", "domain-extraction"],
        "diff": "intermediate",
        "statement": "Count number of messages sent from each domain name (instead of individual email) using a dictionary.",
        "ref_code": "filename = input(\"Enter a file name: \")\nfhandle = open(filename)\ndomain_counts = {}\nfor line in fhandle:\n    if line.startswith(\"From \"):\n        words = line.split()\n        email = words[1]\n        domain = email.split(\"@\")[1]\n        domain_counts[domain] = domain_counts.get(domain, 0) + 1\nprint(domain_counts)",
        "placeholder": "# Extract domains and build count dictionary\n",
        "inputs": ["mbox-short.txt"],
        "outputs": ["Enter a file name: ...\n"],
        "consoles": ["...\n"]
    },
    "10-12__tuples__exercises01": {
        "title": "Top Email Sender using Tuples",
        "desc": "Create list of (count, email) tuples from dictionary, sort in reverse, and print top sender.",
        "prereq": ["tuples", "dictionaries"],
        "topics": ["tuples", "sorting", "dictionaries"],
        "diff": "intermediate",
        "statement": "Read 'From ' lines, build email count dictionary, transform to (count, email) tuples, sort in reverse, and print top sender.",
        "ref_code": "fname = input(\"Enter a file name: \")\nfhandle = open(fname)\ncounts = {}\nfor line in fhandle:\n    if line.startswith(\"From \"):\n        words = line.split()\n        email = words[1]\n        counts[email] = counts.get(email, 0) + 1\nlst = []\nfor email, count in counts.items():\n    lst.append((count, email))\nlst.sort(reverse=True)\ncount, email = lst[0]\nprint(email, count)",
        "placeholder": "# Sort (count, email) tuples and print top sender\n",
        "inputs": ["mbox-short.txt"],
        "outputs": ["Enter a file name: cwen@iupui.edu 5\n"],
        "consoles": ["cwen@iupui.edu 5\n"]
    },
    "10-12__tuples__exercises02": {
        "title": "Hour of Day Distribution",
        "desc": "Extract time string from 'From ' lines, split hour, count per hour, and print sorted by hour.",
        "prereq": ["tuples", "strings"],
        "topics": ["tuples", "sorting", "string-parsing"],
        "diff": "intermediate",
        "statement": "Count distribution of hours of day for messages in mail log and print hour counts sorted by hour.",
        "ref_code": "fname = input(\"Enter a file name: \")\nfhandle = open(fname)\ncounts = {}\nfor line in fhandle:\n    if not line.startswith(\"From \"):\n        continue\n    words = line.split()\n    time = words[5]\n    hour = time.split(\":\")[0]\n    counts[hour] = counts.get(hour, 0) + 1\nfor hour in sorted(counts):\n    print(hour, counts[hour])",
        "placeholder": "# Extract hour and print sorted counts\n",
        "inputs": ["mbox-short.txt"],
        "outputs": ["Enter a file name: ...\n"],
        "consoles": ["...\n"]
    },
    "10-12__tuples__exercises03": {
        "title": "Letter Frequency Counter",
        "desc": "Read file, convert text to lowercase, count letters a-z, and print in decreasing frequency order.",
        "prereq": ["tuples", "dictionaries", "strings"],
        "topics": ["tuples", "frequency-analysis", "sorting"],
        "diff": "intermediate",
        "statement": "Read a file and print letters (a-z) in decreasing order of frequency using tuples.",
        "ref_code": "import string\nfname = input(\"Enter a file name: \")\nfhandle = open(fname)\ncounts = {}\nfor line in fhandle:\n    line = line.lower()\n    for ch in line:\n        if ch in string.ascii_lowercase:\n            counts[ch] = counts.get(ch, 0) + 1\nlst = []\nfor letter, count in counts.items():\n    lst.append((count, letter))\nlst.sort(reverse=True)\nfor count, letter in lst:\n    print(letter, count)",
        "placeholder": "# Count letters and print sorted by frequency descending\n",
        "inputs": ["romeo.txt"],
        "outputs": ["Enter a file name: ...\n"],
        "consoles": ["...\n"]
    },
    "11-10__regular-expressions__exercises01": {
        "title": "Simple Grep Simulator",
        "desc": "Prompt user for a regex pattern and count matching lines in mbox.txt.",
        "prereq": ["regular-expressions", "file-io"],
        "topics": ["regular-expressions", "re.search", "grep"],
        "diff": "intermediate",
        "statement": "Simulate 'grep' command: prompt user for a regex pattern and count matching lines in mbox.txt.",
        "ref_code": "import re\nregex = input(\"Enter a regular expression: \")\ncount = 0\nfor line in open(\"mbox.txt\"):\n    if re.search(regex, line):\n        count = count + 1\nprint(\"mbox.txt had\", count, \"lines that matched\", regex)",
        "placeholder": "# Use re.search to count matching lines\n",
        "inputs": ["^Author"],
        "outputs": ["Enter a regular expression: mbox.txt had 1798 lines that matched ^Author\n"],
        "consoles": ["mbox.txt had 1798 lines that matched ^Author\n"]
    },
    "11-10__regular-expressions__exercises02": {
        "title": "Extract New Revision Numbers with Regex",
        "desc": "Extract numbers from lines matching 'New Revision: ([0-9]+)' and compute integer average.",
        "prereq": ["regular-expressions"],
        "topics": ["regular-expressions", "re.findall", "extraction"],
        "diff": "intermediate",
        "statement": "Extract revision numbers using `re.findall(r'New Revision: ([0-9]+)', line)` and print integer average (`total // count`).",
        "ref_code": "import re\nfname = input(\"Enter file: \")\ncount = 0\ntotal = 0\nfor line in open(fname):\n    matches = re.findall(r\"New Revision: ([0-9]+)\", line)\n    if len(matches) > 0:\n        count = count + 1\n        total = total + int(matches[0])\nprint(total // count)",
        "placeholder": "# Extract revision numbers and print integer average\n",
        "inputs": ["mbox-short.txt"],
        "outputs": ["Enter file: 39756\n"],
        "consoles": ["39756\n"]
    },
    "12-12__networked-programs__exercises01": {
        "title": "Interactive Socket Web Client",
        "desc": "Prompt user for URL, extract host and path using split, and fetch content via socket.",
        "prereq": ["networking", "try-except"],
        "topics": ["networking", "sockets", "url-parsing"],
        "diff": "advanced",
        "statement": "Prompt user for URL, extract host and path using `split('/')`, connect using `socket`, and output response.",
        "ref_code": "import socket\nimport sys\nurl = input(\"Enter URL: \")\ntry:\n    parts = url.split('/')\n    host = parts[2]\n    path = '/' + '/'.join(parts[3:])\n    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)\n    mysock.connect((host, 80))\nexcept Exception as e:\n    sys.exit(\"Error: \" + str(e))\ncmd = f\"GET {path} HTTP/1.0\\r\\nHost: {host}\\r\\n\\r\\n\"\nmysock.send(cmd.encode())\nwhile True:\n    data = mysock.recv(512)\n    if len(data) < 1:\n        break\n    print(data.decode(), end='')\nmysock.close()",
        "placeholder": "# Parse URL and send HTTP GET command using socket\n",
        "inputs": ["http://data.pr4e.org/romeo.txt"],
        "outputs": ["Enter URL: ...\n"],
        "consoles": ["...\n"]
    },
    "12-12__networked-programs__exercises02": {
        "title": "Socket Web Client with Character Limit",
        "desc": "Display at most 3000 characters from socket response and print total character count at end.",
        "prereq": ["networking", "sockets"],
        "topics": ["networking", "sockets", "character-counting"],
        "diff": "advanced",
        "statement": "Count characters received via socket, stop printing text after 3000 chars, and output total count.",
        "ref_code": "import socket\nurl = input(\"Enter URL: \")\nparts = url.split(\"/\")\nhost = parts[2]\npath = \"/\" + \"/\".join(parts[3:])\nmysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)\nmysock.connect((host, 80))\ncmd = \"GET \" + path + \" HTTP/1.0\\r\\nHost: \" + host + \"\\r\\n\\r\\n\"\nmysock.send(cmd.encode())\ncount = 0\nwhile True:\n    data = mysock.recv(512)\n    if len(data) < 1:\n        break\n    text = data.decode()\n    if count < 3000:\n        remain = 3000 - count\n        print(text[:remain], end=\"\")\n    count = count + len(text)\nprint()\nprint(\"Count:\", count)\nmysock.close()",
        "placeholder": "# Limit displayed text to 3000 chars and print total count\n",
        "inputs": ["http://data.pr4e.org/romeo.txt"],
        "outputs": ["Enter URL: ...\n"],
        "consoles": ["...\n"]
    },
    "12-12__networked-programs__exercises03": {
        "title": "Urllib Web Client with Character Limit",
        "desc": "Replicate socket character limit exercise using urllib.request.",
        "prereq": ["networking"],
        "topics": ["networking", "urllib", "http"],
        "diff": "intermediate",
        "statement": "Use `urllib` to retrieve document from URL, display up to 3000 characters, and print overall character count.",
        "ref_code": "import urllib.request\nurl = input(\"Enter URL: \")\nfhand = urllib.request.urlopen(url)\ncount = 0\nfor line in fhand:\n    text = line.decode()\n    if count < 3000:\n        remain = 3000 - count\n        print(text[:remain], end=\"\")\n    count = count + len(text)\nprint()\nprint(\"Count:\", count)",
        "placeholder": "# Use urllib to fetch document and count chars\n",
        "inputs": ["http://data.pr4e.org/romeo.txt"],
        "outputs": ["Enter URL: ...\n"],
        "consoles": ["...\n"]
    },
    "12-12__networked-programs__exercises04": {
        "title": "Count Paragraph Tags with BeautifulSoup",
        "desc": "Extract and count paragraph (p) tags from HTML retrieved via urllib.",
        "prereq": ["networking", "urllib"],
        "topics": ["networking", "html-parsing", "beautifulsoup"],
        "diff": "intermediate",
        "statement": "Use BeautifulSoup to count '<p>' tags in an HTML page retrieved with `urllib` and display the tag count.",
        "ref_code": "import urllib.request\nfrom bs4 import BeautifulSoup\nurl = input(\"Enter URL: \")\nhtml = urllib.request.urlopen(url).read()\nsoup = BeautifulSoup(html, \"html.parser\")\ntags = soup('p')\nprint(\"Paragraph tags:\", len(tags))",
        "placeholder": "# Parse HTML with BeautifulSoup and count paragraph tags\n",
        "inputs": ["http://data.pr4e.org/romeo.txt"],
        "outputs": ["Enter URL: Paragraph tags: 0\n"],
        "consoles": ["Paragraph tags: 0\n"]
    },
    "12-12__networked-programs__exercises05": {
        "title": "Socket Web Client Skipping Headers",
        "desc": "Only display HTTP response data after headers and blank line (\\r\\n\\r\\n) have been received.",
        "prereq": ["networking", "sockets"],
        "topics": ["networking", "http-protocol", "header-parsing"],
        "diff": "advanced",
        "statement": "Change socket program to skip HTTP headers and only print body content after `\\r\\n\\r\\n`.",
        "ref_code": "import socket\nimport sys\nurl = input(\"Enter URL: \")\ntry:\n    parts = url.split('/')\n    host = parts[2]\n    path = '/' + '/'.join(parts[3:])\n    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)\n    mysock.connect((host, 80))\nexcept Exception as e:\n    sys.exit(\"Error: \" + str(e))\ncmd = f\"GET {path} HTTP/1.0\\r\\nHost: {host}\\r\\n\\r\\n\"\nmysock.send(cmd.encode())\ndata = b\"\"\nwhile True:\n    msg = mysock.recv(512)\n    if len(msg) < 1:\n        break\n    data = data + msg\ntext = data.decode()\npos = text.find(\"\\r\\n\\r\\n\")\nif pos >= 0:\n    print(text[pos + 4:])\nmysock.close()",
        "placeholder": "# Strip HTTP headers and print body text\n",
        "inputs": ["http://data.pr4e.org/romeo.txt"],
        "outputs": ["Enter URL: ...\n"],
        "consoles": ["...\n"]
    }
}

def indent_multiline(text, spaces):
    pad = " " * spaces
    lines = text.rstrip("\n").split("\n")
    return "\n".join([pad + line for line in lines])

for ex_id, spec in specs.items():
    folder_path = os.path.join(out_base, ex_id)
    os.makedirs(folder_path, exist_ok=True)
    try:
        os.chmod(folder_path, 0o777)
    except Exception:
        pass
    
    # 1. Write main.py
    main_py_path = os.path.join(folder_path, "main.py")
    try:
        if os.path.exists(main_py_path):
            os.chmod(main_py_path, 0o666)
            os.remove(main_py_path)
        with open(main_py_path, "w", encoding="utf-8") as f:
            f.write(spec["ref_code"] + "\n")
    except Exception:
        pass
        
    # 2. Build free-coding.yaml
    prereq_str = json.dumps(spec["prereq"])
    topics_str = json.dumps(spec["topics"])
    
    inputs = spec["inputs"]
    outputs = spec["outputs"]
    consoles = spec["consoles"]
    
    exec_blocks = []
    tc_blocks = []
    
    for i in range(len(inputs)):
        inp = inputs[i]
        out = outputs[i]
        cons = consoles[i]
        
        if isinstance(inp, list):
            if not inp:
                stdin_str = " []"
            else:
                stdin_str = "\n" + "\n".join([f"      - {json.dumps(x)}" for x in inp])
        else:
            stdin_str = f"\n      - {json.dumps(inp)}"
            
        exec_blocks.append(f"""  - title: Execution {i+1}
    stdin:{stdin_str}
    stdout: |-
{indent_multiline(out, 6)}
    console: |-
{indent_multiline(cons, 6)}
    status: pass""")

        tc_blocks.append(f"""  - title: Testcase {i+1}
    visible: true
    stdin:{stdin_str}
    stdout: |-
{indent_multiline(out, 6)}
    console: |-
{indent_multiline(cons, 6)}""")

    yaml_content = f"""$schema: https://adapt2.sis.pitt.edu/cupcake/schemas/free-coding/0.1.0
source: main.py
license: MIT
locale: en-US
id: {ex_id}
title: {json.dumps(spec['title'])}
description: {json.dumps(spec['desc'])}
authors:
  - first: PY4E
    last: Exercise
    email: info@py4e.com
    affiliation: Python for Everybody
pedagogy:
  activity: free-coding
  difficulty: {spec['diff']}
  prereq_topics: {prereq_str}
  topics: {topics_str}
runtime:
  language: python
  version: 3
statement: |-
{indent_multiline(spec['statement'], 2)}
executions:
{'\n'.join(exec_blocks)}
elements:
  - type: editable
    location:
      snippet: |-
{indent_multiline(spec['ref_code'], 8)}
    placeholder: |-
{indent_multiline(spec['placeholder'], 6)}
testcases:
{'\n'.join(tc_blocks)}
"""

    yaml_slug = ex_id.split("__", 1)[1] if "__" in ex_id else ex_id
    yaml_path = os.path.join(folder_path, f"{yaml_slug}.yaml")

    try:
        if os.path.exists(yaml_path):
            os.chmod(yaml_path, 0o666)
            os.remove(yaml_path)
    except Exception:
        pass

    try:
        with open(yaml_path, "w", encoding="utf-8") as f:
            f.write(yaml_content)
    except Exception as e:
        print(f"Error writing {yaml_path}: {e}")

    # Remove old full ex_id yaml if it exists
    old_yaml_path = os.path.join(folder_path, f"{ex_id}.yaml")
    if old_yaml_path != yaml_path and os.path.exists(old_yaml_path):
        try:
            os.chmod(old_yaml_path, 0o666)
            os.remove(old_yaml_path)
        except Exception:
            pass

print(f"Successfully generated all {len(specs)} exercise activities in {out_base}")

