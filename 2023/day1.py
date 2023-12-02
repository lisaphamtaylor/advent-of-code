"""
--- Day 1: Trebuchet?! ---
https://adventofcode.com/2023/day/1
Something is wrong with global snow production, and you've been selected to take a look. The Elves have even given you a map; on it, they've used stars to mark the top fifty locations that are likely to be having problems.

You've been doing this long enough to know that to restore snow operations, you need to check all fifty stars by December 25th.

Collect stars by solving puzzles. Two puzzles will be made available on each day in the Advent calendar; the second puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!

You try to ask why they can't just use a weather machine ("not powerful enough") and where they're even sending you ("the sky") and why your map looks mostly blank ("you sure ask a lot of questions") and hang on did you just say the sky ("of course, where do you think snow comes from") when you realize that the Elves are already loading you into a trebuchet ("please hold still, we need to strap you in").

As they're making the final adjustments, they discover that their calibration document (your puzzle input) has been amended by a very young Elf who was apparently just excited to show off her art skills. Consequently, the Elves are having trouble reading the values on the document.

The newly-improved calibration document consists of lines of text; each line originally contained a specific calibration value that the Elves now need to recover. On each line, the calibration value can be found by combining the first digit and the last digit (in that order) to form a single two-digit number.

For example:

1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
In this example, the calibration values of these four lines are 12, 38, 15, and 77. Adding these together produces 142.

Consider your entire calibration document. What is the sum of all of the calibration values?
"""
# --- Part One ---

# opening file and reading lines of data and saving to list
data = open('day1_input.txt').read().split('\n')

def sum_first_last_digit(line):
    '''returns sum of first and last numeric digit in input line'''
    # initializing line_num str to hold all line digits
    line_num = ''
    # iterating over each character in line
    for char in line:
        # if character is digit, add to line_num
        if char.isdigit():
            line_num += char
        
    # return 2 digit int of first and last digit in line_num
    return int(line_num[0]+line_num[-1])

def sum_data_lines(dataset):
    '''returns sum of first and last numeric digit of each line in dataset'''
    # initializing sum
    sum = 0

    # iterating over each line of data
    for line in dataset:
        # run sum_first_last_digit in each line and add value to sum
        sum += sum_first_last_digit(line)
        
    return sum

print(f'Part 1 answer: {sum_data_lines(data)}')     # sum = 54708

"""--- Part Two ---
https://adventofcode.com/2023/day/1#part2
Your calculation isn't quite right. It looks like some of the digits are actually spelled out with letters: one, two, three, four, five, six, seven, eight, and nine also count as valid "digits".

Equipped with this new information, you now need to find the real first and last digit on each line. For example:

two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
In this example, the calibration values are 29, 83, 13, 24, 42, 14, and 76. Adding these together produces 281.

What is the sum of all of the calibration values?"""
# --- Part Two ---
# create digit dictionary to translate digit words into ints
digit_dict = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4', 
    'five': '5',
    'six': '6',
    'seven': '7', 
    'eight': '8',
    'nine': '9'
}

def sum_first_last_w_words(dataset):
    '''returns sum of first and last digit--word or int---of each line in dataset'''
    # initializing sum
    total_sum = 0
    
    # iterating over each line of data
    for line in dataset:
        # check to see if line contains any digit words
        while any(word_digit in line for word_digit in digit_dict.keys()):
            # if word_digit, replace with string of int
            for word_digit in digit_dict.keys():
                if word_digit in line:
                    line = line.replace(word_digit, digit_dict[word_digit])
        line_sum = sum_first_last_digit(line)
        total_sum += line_sum
        print(line, sum_first_last_digit(line), total_sum)
    
    return total_sum

print(f'Part 2 answer: {sum_first_last_w_words(data)}')