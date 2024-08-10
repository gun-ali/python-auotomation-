import re
import pyperclip
# find phone numbers(for Turkey) and emails from the copied text to clipboard
text = pyperclip.paste()
# Improved regex pattern for Turkish phone numbers
PhoneNumberRegex = re.compile(r'''
    0?                  #Optional leading zero
    [\s-]?              #Optional space or dash separator
    \(?\d{3}\)?         #Area code with optional parentheses 
    [\s-]?              #Optional space or dash separator
    \d{3}               #first part of local number
    [\s-]?              #Optional space or dash separator
    \d{2}               #second part of local number
    [\s-]?              #Optional space or dash separator
    \d{2}               #last part of local number   
''',re.VERBOSE)

# Improved regex pattern for email  
emailRegex = re.compile(r'''
    [\w.-]+                   #username part
    @                         #@ symbol
    [\w.-]+                   #domain name part
    \.[a-zA-z]{2,}            #top level domain
''',re.VERBOSE)

match4email = emailRegex.findall(text)
match4number = PhoneNumberRegex.findall(text)

for i, email in enumerate(match4email, start=1):
    print(f'{i}. email: {email}')
    
print("-"*40)    
for i, number in enumerate(match4number, start=1):
    print(f'{i}. Phone number: {number}')

