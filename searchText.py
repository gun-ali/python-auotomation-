# this program opens all .txt files in a folder and searches for any line 
# that matches a user-supplied regular expression
import re, os, sys, glob

if len(sys.argv) >= 3 : 
    if os.path.exists(sys.argv[1]):
        os.chdir(sys.argv[1])
        textRegex = re.compile(sys.argv[2])
        txt_files = glob.glob("*.txt")
        
        for txtfile in txt_files:
            with open(txtfile,'r') as file:
                content = file.read()
                matchedtexts = textRegex.findall(content)
            
            for match in matchedtexts:
                print(f"Found in {txtfile}: {match}")        
    else:
        print("the file path do not exist")        
else:   
    print("USAGE: python3 programname.py /path/you/want/to/search REGEX")


     