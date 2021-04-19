with open("sample.1", encoding='ISO-8859-15') as file_1:                #open sample.1 and assign each line as element in list data_1
    data_1 = file_1.readlines()
with open("sample.2", encoding='ISO-8859-15') as file_2:                #open sample.2 and assign each line as element in list data_2
    data_2 = file_2.readlines()
with open("sample.3", encoding='ISO-8859-15') as file_3:                #open sample.3 and assign each line as element in list data_3
    data_3 = file_3.readlines()
with open("sample.4", encoding='ISO-8859-15') as file_4:                #open sample.4 and assign each line as element in list data_4
    data_4 = file_4.readlines()
with open("sample.5", encoding='ISO-8859-15') as file_5:                #open sample.5 and assign each line as element in list data_5
    data_5 = file_5.readlines()
with open("sample.6", encoding='ISO-8859-15') as file_6:                #open sample.6 and assign each line as element in list data_6
    data_6 = file_6.readlines()
with open("sample.7", encoding='ISO-8859-15') as file_7:                #open sample.7 and assign each line as element in list data_7
    data_7 = file_7.readlines()
with open("sample.8", encoding='ISO-8859-15') as file_8:                #open sample.8 and assign each line as element in list data_8
    data_8 = file_8.readlines()
with open("sample.9", encoding='ISO-8859-15') as file_9:                #open sample.9 and assign each line as element in list data_9
    data_9 = file_9.readlines()
with open("sample.10", encoding='ISO-8859-15') as file_10:              #open sample.10 and assign each line as element in list data_10
    data_10 = file_10.readlines()

array_1 = [data_2, data_3, data_4, data_5, data_6, data_7, data_8, data_9, data_10]
array_2 = [data_1, data_3, data_4, data_5, data_6, data_7, data_8, data_9, data_10]
array_3 = [data_1, data_2, data_4, data_5, data_6, data_7, data_8, data_9, data_10]
array_4 = [data_1, data_2, data_3, data_5, data_6, data_7, data_8, data_9, data_10]
array_5 = [data_1, data_2, data_3, data_4, data_6, data_7, data_8, data_9, data_10]             #creating 2-D lists for each data file
array_6 = [data_1, data_2, data_3, data_4, data_5, data_7, data_8, data_9, data_10]             #the array number corresponds to which list number the contents will be compared with
array_7 = [data_1, data_2, data_3, data_4, data_5, data_6, data_8, data_9, data_10]             #data_1 will be cross checked with data_2, data_3, data_4, ... data_10
array_8 = [data_1, data_2, data_3, data_4, data_5, data_6, data_7, data_9, data_10]             #same will be done for data_1 through data_10
array_9 = [data_1, data_2, data_3, data_4, data_5, data_6, data_7, data_8, data_10]             #each data list will be compared to all other data lists within these arrays
array_10 = [data_1, data_2, data_3, data_4, data_5, data_6, data_7, data_8, data_9]
array_full = [data_1, data_2, data_3, data_4, data_5, data_6, data_7, data_8, data_9, data_10]          #this 2-D list will be used at the end, it contains a 2-D list of all 10 data lists 

longest_length = 1              #defining an arbitrary value for initial longest length strand
longest_strings = []            #creating empty list for the longest identical strings within each loop

for file_1_data in data_1:              #for loop that temporarily defines the first line of characters in data_1 as variable file_1_data
    for i in range(9):                  #for loop to be repeated 9 times that will look at every element in the 1st element of array_1 through every element in the 9th element of array_1
        if file_1_data in array_1[i]:               #conditional statement; checks if current string file_1_data appears anywhere within specified list inside array_1 list
            if len(file_1_data) > longest_length:   #conditional statement; if match has been found, checks if the length of that identical string is greater than the current value of the longest length
                longest_string1 = file_1_data       #if both conditions are satisfied, assigns new value to both longest_length and longest_string1
                longest_length = len(file_1_data)   #NOTE: longest_string1 is not the longest identical string of all, it's only the longest identical string found in data_1 and somewhere else
                longest_strings.append(longest_string1)     #add the longest identical string to list called longest_strings

for file_2_data in data_2:          #above process is repeated for data_2 through data_10
    for i in range(9):
        if file_2_data in array_2[i]:
            if len(file_2_data) > longest_length:
                longest_string2 = file_2_data
                longest_length = len(file_2_data)
                longest_strings.append(longest_string2)

for file_3_data in data_3:
    for i in range(9):
        if file_3_data in array_3[i]:
            if len(file_3_data) > longest_length:
                longest_string3 = file_3_data
                longest_length = len(file_3_data)
                longest_strings.append(longest_string3)

for file_4_data in data_4:
    for i in range(9):
        if file_4_data in array_4[i]:
            if len(file_4_data) > longest_length:
                longest_string4 = file_4_data
                longest_length = len(file_4_data)
                longest_strings.append(longest_string4)

for file_5_data in data_5:
    for i in range(9):
        if file_5_data in array_5[i]:
            if len(file_5_data) > longest_length:
                longest_string5 = file_5_data
                longest_length = len(file_5_data)
                longest_strings.append(longest_string5)

for file_6_data in data_6:
    for i in range(9):
        if file_6_data in array_6[i]:
            if len(file_6_data) > longest_length:
                longest_string6 = file_6_data
                longest_length = len(file_6_data)
                longest_strings.append(longest_string6)
                
for file_7_data in data_7:
    for i in range(9):
        if file_7_data in array_7[i]:
            if len(file_7_data) > longest_length:
                longest_string7 = file_7_data
                longest_length = len(file_7_data)
                longest_strings.append(longest_string7)

for file_8_data in data_8:
    for i in range(9):
        if file_8_data in array_8[i]:
            if len(file_8_data) > longest_length:
                longest_string8 = file_8_data
                longest_length = len(file_8_data)
                longest_strings.append(longest_string8)

for file_9_data in data_9:
    for i in range(9):
        if file_9_data in array_9[i]:
            if len(file_9_data) > longest_length:
                longest_string9 = file_9_data
                longest_length = len(file_9_data)
                longest_strings.append(longest_string9)

for file_10_data in data_10:
    for i in range(9):
        if file_10_data in array_10[i]:
            if len(file_10_data) > longest_length:
                longest_string10 = file_10_data
                longest_length = len(file_10_data)
                longest_strings.append(longest_string10)        #longest_strings is a list of the longest strings between each data file and somewhere else
                                                                #longest_length is the length of the longest identical string we need
print(longest_length)                                           #print length of longest identical string to console

for i in range(len(longest_strings)):               #for loop that will run the following sequence for every element in the list longest_strings
    if len(longest_strings[i]) == longest_length:   #conditional statement; if the length of one of those strings is the same as the longest length, that is the longest string
        longest_string = longest_strings[i]         #creating new variable longest_string
        
print("Located in...")
for i in range(10):                             #for loop that will run the following sequence for each list of data in array_full
    if longest_string in array_full[i]:         #conditional statement; if longest_string is found in the specified list in the array_full_list, then program will execute the following commands
        file_location = i + 1                   #data files are numbered in order 1-10, so the first position in array_full is sample 1, etc. File location is i + 1 since i starts at 0
        line_location = array_full[i].index(longest_strings[-1])        #find the line position where the string pops up with index command
        print("Sample", file_location, "Line number", line_location + 1)        #prints file number and line number each time conditional statement above is satisfied
        
        
