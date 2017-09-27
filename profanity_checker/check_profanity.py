import urllib

def read_text():
    quotes = open("/Users/josepho/Desktop/new_file.txt")
    # opens the file using open and assigns that to the quotes
    contents_of_file = quotes.read()
    # reads the contents of the file assigned to quotes and assigns it to contents_of_file 
    # print(contents_of_file)
    quotes.close()
    # closes the text file that was assigned to quotes
    check_profanity(contents_of_file)
    # checks the contents in contents_of_file for profanity using check_profanity
    
def check_profanity(text_to_check):
    # opens a connection to the website using the urlopen method within urllib module and assigns it to connection
    connection = urllib.urlopen("http://www.wdylike.appspot.com/?q="+text_to_check)
    # reads the value passed from the connection and text_to_check and assigns it to output 
    output = connection.read()
    # print(output)
    connection.close()
    if "true" in output:
        print("Profanity alert!!!")
    elif "false" in output:
        print("no fucking profanity here")
    else:
        print("could not scan the document properly")
    
read_text() 
