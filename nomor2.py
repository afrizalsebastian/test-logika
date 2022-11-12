import re

result = []
text = input("")

regex = "(?i)(sang gajah|serigala|harimau)"     #regex pattern untuk dicari pada text
match = re.findall(regex, text)                 #Menemukan semua pattern pada text

for i in range(len(match)):                     #Mendisplay semua pattern yang ditemukan
    if(i ==  len(match) - 1):
        print(match[i].lower())
    else:
        print(match[i].lower(), "- ", end="")