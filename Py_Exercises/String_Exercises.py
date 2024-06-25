#1.Cut(slice) out the first word of Coding For All string.
company = "Coding For All"
first_word = company.split()[0]
print(first_word)



#2.Check if Coding For All string contains a word Coding using the method index, find or other methods

company = "coding For All"
if company.find("Coding") !=-1:
    print("The word 'Coding' is found in the string.")
else:
    print("The word 'Coding' is not found in the string.")


    company = "Coding For All"
if "Coding" in company:
    print("The word 'Coding' is found in the string.")
else:
    print("The word 'Coding' is not found in the string.")


   #3 Replace the word coding in the string 'Coding For All' to Python.
company = "Coding For All"
new_company = company.replace("Coding", "Python")
print(new_company)



#4.Change Python for Everyone to Python for All using the replace method or other methods.
original_string = "Python for Everyone"
new_string = original_string.replace("Everyone", "All")
print(new_string)


#5.Split the string 'Coding For All' using space as the separator (split()) .
company = "Coding For All"
words = company.split(" ")
print(words)


#6."Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
companies = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
company_list = companies.split(", ")
print(company_list)


#7.What is the character at index 0 in the string Coding For All
company = "Coding For All"
char_at_index_0 = company[0]
print(char_at_index_0)


#8.What is the last index of the string Coding For All.
company = "Coding For All"
last_index = len(company) - 1
print(last_index)

#9. What character is at index 10 in "Coding For All" string.
company = "Coding For All"
char_at_index_10 = company[10]
print(char_at_index_10)

#10.Create an acronym or an abbreviation for the name 'Python For Everyone'.
phrase = "Python For Everyone"
words = phrase.split()
acronym = "".join([word[0] for word in words])
print(acronym)

#11.Use index to determine the position of the first occurrence of C in Coding For All.
company = "Coding For All"
position = company.index('C')
print(position)

#12.Use index to determine the position of the first occurrence of F in Coding For All
company = "Coding For All"
position = company.index('F')
print(position)

#13.Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction.
sentence = "You cannot end a sentence with because because because is a conjunction."
position = sentence.index("because")
print(position)

sentence = "You cannot end a sentence with because because because is a conjunction."
position = sentence.find("because")
print(position)

#14.Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
sentence = "You cannot end a sentence with because because because is a conjunction."
position = sentence.rindex("because")
print(position)


#15.Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'.
sentence = "You cannot end a sentence with because because because is a conjunction."
start_index = sentence.index("because because because")
end_index = start_index + len("because because because")
sliced_sentence = sentence[:start_index] + sentence[end_index:]
print(sliced_sentence)


#16.Find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'.
sentence = "You cannot end a sentence with because because because is a conjunction."
position = sentence.find("because")
print(position)

#17.Does ''Coding For All' start with a substring Coding?
company = "Coding For All"
starts_with_coding = company.startswith("Coding")
print(starts_with_coding)

'''
#18.Which one of the following variables return True when we use the method isidentifier():
30DaysOfPython
thirty_days_of_python
'''
var1 = "30DaysOfPython"
var2 = "thirty_days_of_python"

print(var1.isidentifier())  # Check if var1 is a valid identifier
print(var2.isidentifier())  # Check if var2 is a valid identifier

#18.The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
joined_libraries = "  # ".join(libraries)
print(joined_libraries)
'''
#19.Use the new line escape sequence to separate the following sentences.
I am enjoying this challenge.
I just wonder what is next.
'''
sentence1 = "I am enjoying this challenge."
sentence2 = "I just wonder what is next."
combined_sentence = sentence1 + "\n" + sentence2
print(combined_sentence)

'''
#20.Use a tab escape sequence to write the following lines.
Name      Age     Country   City
Asabeneh  250     Finland   Helsinki
'''
line1 = "Name\tAge\tCountry\tCity"
line2 = "Asabeneh\t250\tFinland\tHelsinki"
print(line1)
print(line2)

'''
#21.Use the string formatting method to display the following:
radius = 10
area = 3.14 * radius ** 2
The area of a circle with radius 10 is 314 meters square.
'''
radius = 10
area = 3.14 * radius ** 2

# Using f-string for string formatting
print(f"The area of a circle with radius {radius} is {area} square meters.")


'''
#22.Make the following using string formatting methods:
8 + 6 = 14
8 - 6 = 2
8 * 6 = 48
8 / 6 = 1.33
8 % 6 = 2
8 // 6 = 1
8 ** 6 = 262144
'''
# Multiplication
multiplication = 8 * 6
print(f"8 * 6 = {multiplication}")

# Division
division = 8 / 6
print(f"8 / 6 = {division:.2f}")  # Displaying up to 2 decimal places

# Modulus
modulus = 8 % 6
print(f"8 % 6 = {modulus}")

# Floor Division
floor_division = 8 // 6
print(f"8 // 6 = {floor_division}")

# Exponentiation
exponentiation = 8 ** 6
print(f"8 ** 6 = {exponentiation}")










