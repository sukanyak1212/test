#1. Declare an empty list
empty_list = []
print(empty_list)   

#2. Declare a list with more than 5 items
my_list = [1, 'apple', 3.14, True, None, [1, 2, 3]]
print(my_list)  #list with different data types

#3. Find the length of your list
my_list = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig']
length_of_list = len(my_list)
print(f'The length of the list is: {length_of_list}')



#4. Get the first item, the middle item and the last item of the list
my_list = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig']
first_item = my_list[0]
middle_index = len(my_list) // 2
if len(my_list) % 2 == 0:
    middle_item = my_list[middle_index - 1: middle_index + 1]
else:
    middle_item = my_list[middle_index]
last_item = my_list[-1]
print(f'First item: {first_item}')
print(f'Middle item: {middle_item}')
print(f'Last item: {last_item}')



#5. Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types = ['John', 29, 5.9, 'Single', '102,msr residency,4th Street,bengaluru']
print(mixed_data_types)


#6.Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
print(it_companies)


#7.Print the list using print()
it_companies = ['java', 'python', 'javaScript', 'html', 'css', 'sql']
print(it_companies)


#8.Print the number of companies in the list
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
number_of_companies = len(it_companies)
print(f'The number of companies in the list is: {number_of_companies}')



#9.Print the first, middle and last company
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
first_company = it_companies[0]
middle_index = len(it_companies) // 2
middle_company = it_companies[middle_index]
last_company = it_companies[-1]
print(f'First company: {first_company}')
print(f'Middle company: {middle_company}')
print(f'Last company: {last_company}')


#if it is even list
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle']
first_company = it_companies[0]
middle_index = len(it_companies) // 2
middle_companies = it_companies[middle_index - 1: middle_index + 1]
last_company = it_companies[-1]
print(f'First company: {first_company}')
print(f'Middle companies: {middle_companies}')
print(f'Last company: {last_company}')

#10.Print the list after modifying one of the companies
it_companies = ['Google', 'Microsoft', 'Apple', 'IBM', 'amazon', 'Oracle']
it_companies[0] = 'visa'
print(it_companies)

#11.Add an IT company to it_companies.
it_companies = ['visa', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle']
it_companies.append('amazon')
print(it_companies)


#12.Insert an IT company in the middle of the companies list
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle','Amazon']
new_company = 'visa'
middle_index = len(it_companies) // 2  # Calculate the middle index
it_companies.insert(middle_index, new_company)
print(it_companies)

#13.Change one of the it_companies names to uppercase (IBM excluded!)
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
for i in range(len(it_companies)):
    if it_companies[i] != 'IBM':
        it_companies[i] = it_companies[i].upper()
print(it_companies)

#14.Join the it_companies with a string '#;  '
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
joined_companies = '#;  '.join(it_companies)
print(joined_companies)

#15.Check if a certain company exists in the it_companies list.
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
company_to_check = 'Microsoft'
if company_to_check in it_companies:
    print(f'{company_to_check} exists in the list!')
else:
    print(f'{company_to_check} does not exist in the list.')

#16.Sort the list using sort() method
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
it_companies.sort()
print(it_companies)

#17.Reverse the list in descending order using reverse() method
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
it_companies.sort()
it_companies.reverse()
print(it_companies)

#18.Slice out the first 3 companies from the list
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
first_three_companies = it_companies[:3]   #slice out 3 companies
print(first_three_companies)


#18.1. Slice out the first 3 companies and print remaining items in list
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
first_three_companies = it_companies[:3]
remaining_companies = it_companies[3:]
print("Remaining companies:", remaining_companies)


#19.Slice out the last 3 companies from the list
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
last_three_companies = it_companies[-3:]
print(last_three_companies)

#20.Slice out the middle IT company or companies from the list
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
middle_index = len(it_companies) // 2
if len(it_companies) % 2 == 0:
    middle_companies = it_companies[middle_index - 1: middle_index + 1]   # Even number of companies: two middle companies
else:
    middle_companies = [it_companies[middle_index]]   # Odd number of companies: one middle company
print(middle_companies)


#21.Remove the first IT company from the list using pop()
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
it_companies.pop(0)   # Remove the first IT company
print(it_companies)


#21.1.Remove the first IT company from the list using del()
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
del it_companies[0]
print(it_companies)


#22.Remove the middle IT company or companies from the list
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
middle_index = len(it_companies) // 2
if len(it_companies) % 2 == 0:
    del it_companies[middle_index - 1: middle_index + 1]
else:
    del it_companies[middle_index]
print(it_companies)


#23.1. Remove the last IT company from the list using pop()
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
it_companies.pop()
print(it_companies)

#23.2.Remove the last IT company from the list using del()
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
del it_companies[-1]
print(it_companies)


#24.Remove all IT companies from the list
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
it_companies.clear()
print(it_companies)

#25.Destroy the IT companies list
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
del it_companies
try:
    print(it_companies)
except NameError:
    print("The it_companies list has been deleted.")

#26. Join the following lists:
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']


front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']
full_stack = front_end + back_end
print(full_stack)


#27.After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack. Then insert Python and SQL after Redux.
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']   
full_stack = front_end + back_end
index_after_redux = full_stack.index('Redux') + 1
full_stack.insert(index_after_redux, 'Python')
full_stack.insert(index_after_redux + 1, 'SQL')
print(full_stack)



#Exercises: Level 2

#1.The following is a list of 10 students ages:
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

#1.1. Sort the list and find the min and max age.

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
min_age = min(ages)
max_age = max(ages)
print("Sorted ages:", ages)
print("Minimum age:", min_age)
print("Maximum age:", max_age)


#1.2Add the min age and the max age again to the list
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
min_age = min(ages)   # Find the minimum and maximum age
max_age = max(ages)
ages.append(min_age)   # Add the min age and the max age again to the list
ages.append(max_age)
print(ages)


#1.3Find the median age (one middle item or two middle items divided by two)
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
n = len(ages)
if n % 2 == 0:
    median_age = (ages[n//2 - 1] + ages[n//2]) / 2    # If even, the median is the average of the two middle elements
else:
    median_age = ages[n//2]       # If odd, the median is the middle element
print("Median age:", median_age)

'''
#Question :ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
display sorted list using function()
'''
def sort_list(lst):
    lst.sort()
    return lst
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
sorted_ages = sort_list(ages.copy())
print(f"Sorted ages: {sorted_ages}")

#4.Find the average age (sum of all items divided by their number )
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
average_age = sum(ages) / len(ages)
print(f"Average age: {average_age}")

#5.Find the range of the ages (max minus min)
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
age_range = max(ages) - min(ages)
print(f"Range of ages: {age_range}")


#6.Compare the value of (min - average) and (max - average), use abs() method
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
min_age = min(ages)
max_age = max(ages)
average_age = sum(ages) / len(ages)      # Calculate the average age
min_average_diff = min_age - average_age   # Calculate the differences
max_average_diff = max_age - average_age
abs_min_average_diff = abs(min_average_diff)    # Use abs() method to get the absolute values
abs_max_average_diff = abs(max_average_diff)
print(f"Absolute difference between min and average: {abs_min_average_diff}")
print(f"Absolute difference between max and average: {abs_max_average_diff}")


#1.Find the middle country(ies) in the countries list
countries = ['China', 'India', 'USA', 'Indonesia', 'Pakistan','Afganistan']
num_countries = len(countries)   #calc num of countries
if num_countries % 2 == 0:     # Find the middle country (or countries)
    middle1 = countries[num_countries // 2 - 1]        # If even, there are two middle countries
    middle2 = countries[num_countries // 2]
    middle_countries = (middle1, middle2)
else:
    middle_countries = countries[num_countries // 2]    # If odd, there is one middle country
print(f"Middle country(ies): {middle_countries}")


#2.Divide the countries list into two equal lists if it is even if not one more country for the first half.
countries = ['China', 'India', 'USA', 'Indonesia', 'Pakistan', 'Bangladesh', 'Russia']
midpoint = (len(countries) + 1) // 2
first_half = countries[:midpoint]
second_half = countries[midpoint:]
print(f"First half: {first_half}")
print(f"Second half: {second_half}")

'''
for my reference
half_of_list=(len(countries)+1)//2  
print(half_of_list)
'''

#3.['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic countries.
countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
first, second, third, *scandic_countries = countries   # Unpack the first three countries and the rest as scandic countries
print(f"First country: {first}")
print(f"Second country: {second}")
print(f"Third country: {third}")
print(f"Scandic countries: {scandic_countries}")


