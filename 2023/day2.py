"""--- Day 2: Cube Conundrum ---
https://adventofcode.com/2023/day/2
You're launched high into the atmosphere! The apex of your trajectory just barely reaches the surface of a large island floating in the sky. You gently land in a fluffy pile of leaves. It's quite cold, but you don't see much snow. An Elf runs over to greet you.

The Elf explains that you've arrived at Snow Island and apologizes for the lack of snow. He'll be happy to explain the situation, but it's a bit of a walk, so you have some time. They don't get many visitors up here; would you like to play a game in the meantime?

As you walk, the Elf shows you a small bag and some cubes which are either red, green, or blue. Each time you play this game, he will hide a secret number of cubes of each color in the bag, and your goal is to figure out information about the number of cubes.

To get information, once a bag has been loaded with cubes, the Elf will reach into the bag, grab a handful of random cubes, show them to you, and then put them back in the bag. He'll do this a few times per game.

You play several games and record the information from each game (your puzzle input). Each game is listed with its ID number (like the 11 in Game 11: ...) followed by a semicolon-separated list of subsets of cubes that were revealed from the bag (like 3 red, 5 green, 4 blue).

For example, the record of a few games might look like this:

Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
In game 1, three sets of cubes are revealed from the bag (and then put back again). The first set is 3 blue cubes and 4 red cubes; the second set is 1 red cube, 2 green cubes, and 6 blue cubes; the third set is only 2 green cubes.

The Elf would first like to know which games would have been possible if the bag contained only 12 red cubes, 13 green cubes, and 14 blue cubes?

In the example above, games 1, 2, and 5 would have been possible if the bag had been loaded with that configuration. However, game 3 would have been impossible because at one point the Elf showed you 20 red cubes at once; similarly, game 4 would also have been impossible because the Elf showed you 15 blue cubes at once. If you add up the IDs of the games that would have been possible, you get 8.

Determine which games would have been possible if the bag had been loaded with only 12 red cubes, 13 green cubes, and 14 blue cubes. What is the sum of the IDs of those games?
"""
# --- Part One ---
import re

# opening input file and reading lines of data and saving to list
data = open('day2_input.txt').read().split('\n')
# data = ['Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green',
# 'Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue',
# 'Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red',
# 'Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red',
# 'Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green']

# initializing regex for each color and saving to list
green_regex = re.compile(r'green$')
red_regex = re.compile(r'red$')
blue_regex = re.compile(r'blue$')

regex_list = [green_regex, red_regex, blue_regex]
def part_1():
    '''returns sum of game numbers that are possible given max number of cubes for each color'''
    # sets max number of cubes for each color
    green_max = 13
    red_max = 12
    blue_max = 14

    # initializing set to hold game numbers that are possible
    game_set = set()

    for game in data:
        # splitting game into list of color sets
        color_sets = re.split(':|;|,', game)

        # getting game number and adding to set
        game_count = int(re.findall(r'\d+', color_sets[0])[0])
        # print(game_count)
        game_set.add(game_count)

        # iterating over each color
        for regex in regex_list:
            # grabbing color of set
            color = regex.pattern[:-1]
            
            # iterating over each color set, ignoring the game number
            for i in range(1, len(color_sets)):
                # grabbing color set so we can check number of cubes
                color_set = color_sets[i]

                # checking color set if game is still valid
                if game_count in game_set and re.search(regex, color_set):
                    # grabbing number of cubes
                    num = re.findall(r'\d+', color_set)

                    # checking number of cubes against max
                    if color == 'green':
                        if int(num[0]) > green_max:
                            # print(f'Game {game_count} not possible on {color}')
                            game_set.remove(game_count)
                            break
                    elif color == 'red':
                        if int(num[0]) > red_max:
                            # print(f'Game {game_count} not possible on {color}')
                            game_set.remove(game_count)
                            break
                    elif color == 'blue':
                        if int(num[0]) > blue_max:
                            # print(f'Game {game_count} not possible on {color}')
                            game_set.remove(game_count)
                            break

    # adding all valid game numbers left in set
    print(f'Day 2-Part 1 Answer: {sum(game_set)}')     # sum = 2331
part_1()

"""--- Part Two ---
https://adventofcode.com/2023/day/2#part2
The Elf says they've stopped producing snow because they aren't getting any water! He isn't sure why the water stopped; however, he can show you how to get to the water source to check it out for yourself. It's just up ahead!

As you continue your walk, the Elf poses a second question: in each game you played, what is the fewest number of cubes of each color that could have been in the bag to make the game possible?

Again consider the example games from earlier:

Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
In game 1, the game could have been played with as few as 4 red, 2 green, and 6 blue cubes. If any color had even one fewer cube, the game would have been impossible.
Game 2 could have been played with a minimum of 1 red, 3 green, and 4 blue cubes.
Game 3 must have been played with at least 20 red, 13 green, and 6 blue cubes.
Game 4 required at least 14 red, 3 green, and 15 blue cubes.
Game 5 needed no fewer than 6 red, 3 green, and 2 blue cubes in the bag.
The power of a set of cubes is equal to the numbers of red, green, and blue cubes multiplied together. The power of the minimum set of cubes in game 1 is 48. In games 2-5 it was 12, 1560, 630, and 36, respectively. Adding up these five powers produces the sum 2286.

For each game, find the minimum set of cubes that must have been present. What is the sum of the power of these sets?
"""

def part_2():
    '''returns sum of power of minimum set of cubes for each game'''
    # initializing list to hold power number of each game
    power_list = [0] * len(data)

    for game in data:
        print(f'Game {data.index(game)}')
        # splitting game into list of color sets
        color_sets = re.split(':|;|,', game)
        # initiating power number for game
        power_num = 1

        # iterating over each color
        for regex in regex_list:
            # initiating min number of cubes
            min_number = None
                
            # iterating over each color set, ignoring the game number
            for i in range(1, len(color_sets)):
                # grabbing color set so we can check number of cubes
                color_set = color_sets[i]

                # checking color set if game is still valid
                if re.search(regex, color_set):
                    # grabbing number of cubes
                    num = int(re.findall(r'\d+', color_set)[0])

                    # checking number of cubes against min
                    if min_number == None:
                        min_number = num
                    else:
                        min_number = max(min_number, num)
            print(min_number)
            power_num *= min_number
        # print(power_num)
        power_list[data.index(game)] = power_num

    print(f'Day 2-Part 2 Answer: {sum(power_list)}')
part_2()