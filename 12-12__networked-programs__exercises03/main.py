import urllib.request
url = input("Enter URL: ")
fhand = urllib.request.urlopen(url)
count = 0
for line in fhand:
    text = line.decode()
    if count < 3000:
        remain = 3000 - count
        print(text[:remain], end="")
    count = count + len(text)
print()
print("Count:", count)
