#usage:  python3 programname.py save <keyword> - Saves clipboard to keyword. 
#        python3 programname.py <keyword> - Loads keyword to clipboard. 
#        python3 programname.py list - Loads all keywords to clipboard.


import shelve, sys, pyperclip

mcbShelf = shelve.open('mcb')

#save clipboard content
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()
    print(f"Clipboard content saved under the keyword '{sys.argv[2]}'.")
    
elif len(sys.argv) == 2:
    #list keywords and load content 
    if sys.argv[1].lower() == 'list':
        keywords= list(mcbShelf.keys())
        pyperclip.copy(str(keywords))
        print(f"Keywords copied to clipboard: {keywords}")
    elif sys.argv[1] in mcbShelf:
        content = mcbShelf[sys.argv[1]]
        pyperclip.copy(mcbShelf[sys.argv[1]])   
        print(f"Content for keyword '{sys.argv[1]}' copied to clipboard.")
        print(f"Content: {content}")
    else:
        print(f"No content found for keyword '{sys.argv[1]}'.")    
mcbShelf.close()
