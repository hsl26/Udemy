#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

with open("Day24/Mail Merge Project Start/Input/Names/invited_names.txt") as name_file:
    name_list = name_file.readlines()   

with open("Day24/Mail Merge Project Start/Input/Letters/starting_letter.txt", "r") as letter_file:
    letter = letter_file.read()
    for name in name_list:
        stripped_name = name.strip()
        new_letter = letter.replace('[name]', stripped_name)
        with open(f"Day24/Mail Merge Project Start/Output/ReadyToSend/to_{stripped_name}.txt", mode="x") as completed_letter:
            completed_letter.write(new_letter)
    
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp