# installing pywhatkit for converison
import pywhatkit
# Enter The Name Of File With Extension Or Provide Path Of File With '\\'
file = input("Enter The File Name Which You Want To Convert:")
# This will Take Your File In Read Form
a = open(file, 'r', errors="ignore", encoding='utf-8')
# IT Read File AS Stirng
str = a.read()
# Here By using  pywhatkit.text_to_handwriting Function You will Get output File In Image You Can Also Play And Edit with RGB Values
pywhatkit.text_to_handwriting(str, 'output.png', rgb=[0, 255, 0])
# You can Also give input directly
second_file = input("Enter The Content In File And See Magic =")
pywhatkit.text_to_handwriting(second_file, rgb=[0, 255, 0])       # it will your output
print("Operation Done Successfully")
