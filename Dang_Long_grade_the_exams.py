import pandas as pd
import numpy as np
import re

while True:
    # Try to open an existing file:
    try:
        filename = input("Enter a class file to grade (i.e. class1 for class1.txt): ")
        
        with open(filename + '.txt') as f:
            print(f'Successfully opened {filename }.txt','**** ANALYZING ****\n',sep='\n\n')
            list_lines = f.read().splitlines()

        valid_list = [] # List containing valid lines
        valid_lines = 0 # Variable used for storing total valid lines
        invalid_lines = 0 # # Variable used for storing total invalid lines
        list_score = [] # List containing student's scores

        answer_keys = ['B', 'A', 'D', 'D', 'C', 'B', 'D', 'A', 'C', 'C', 'D', 'B', 'A', 'B', 'A', 'C', 'B', 'D', 'A', 'C', 'A', 'A', 'B', 'D', 'D']

        # Check every line in file and convert them to lists:
        for strline in list_lines:
            line = strline.split(',')

            # Check if lines have valid student's ID numbers and total of elements:
            if len(line) == 26 and re.match(r'N\d{8}', line[0]): # Using match method from regular expression module to check student's ID numbers
                valid_lines += 1
                valid_list.append(line)
            elif len(line) != 26:
                print(f'Invalid line of data: does not contain exactly 26 values:\n{strline}\n')
                invalid_lines +=1
            elif not re.match(r'N\d{8}', line[0]):
                print(f'Invalid line of data: N# is invalid:\n{strline}\n')
                invalid_lines +=1

       
        # Calculate the grade and create a result file for every input class:
        with open('results/'+filename + '_grades.txt', 'w') as r:
            
            for answer_list in valid_list:
                score = 0
                for answer, key in zip(answer_list[1:],answer_keys):        
                    if answer == key:
                        score += 4
                    elif answer == '':
                        pass
                    elif answer != key:
                        score -=1
                list_score.append(score)
                r.write(f'{answer_list[0]},{score}\n')  
                
        # Report the results:
        if invalid_lines == 0:
            print('No errors found!')
            
        print('\n**** REPORT ****\n',
              f'Total valid lines of data: {valid_lines}',
              f'Total invalid lines of data: {invalid_lines}\n', sep = '\n')
        print(f'Mean (average) score: {np.mean(list_score):.2f}',
              f'Highest score: {np.max(list_score)}',
              f'Lowest score: {np.min(list_score)}',
              f'Range of scores: {np.max(list_score)-np.min(list_score)}',
              f'Median score: {np.median(list_score)}\n',
              f'Please open results folder to see student\'s grades of {filename}!',
              '\n>>> ================================ RESTART ================================\n>>>',
              sep = '\n')
        
    # If file didn't exist, print out "File cannot be found!"    
    except FileNotFoundError:
        print('\nFile cannot be found!\n')