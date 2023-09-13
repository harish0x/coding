def is_pangram(string):
    
    string = string.lower()
    
    char_set = set(string.replace(" ", ""))
    
return len(char_set) == 26


input_string = "We promptly judged antique ivory buckles for the next prize"
result = is_pangram(input_string)
if result:
    print("The input is a pangram.")
else:
    print("The input is not a pangram.")
