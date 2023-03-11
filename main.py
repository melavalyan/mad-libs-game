import random

template = int(input('Please choose a template (1, 2, or 3): '))
if template not in [1, 2, 3]:
    template = random.choice([1, 2, 3])
    print("Template index is:", template)


def generate_story1():          # template1

    number = input("Enter a number: ")
    measure_of_time = input(
        "Enter a measure of time (e.g. days, weeks, months): ")
    mode_of_transportation = input("Enter a mode of transportation: ")
    adjective = input("Enter an adjective: ")
    adjective2 = input("Enter another adjective: ")
    noun = input("Enter a noun: ")
    color = input("Enter a color: ")
    part_of_body = input("Enter a body part: ")
    verb = input("Enter a verb: ")
    number2 = input("Enter a number: ")
    noun2 = input("Enter a noun: ")
    noun3 = input("Enter a noun: ")
    part_of_body2 = input("Enter a body part: ")
    noun4 = input("Enter a noun: ")
    adjective3 = input("Enter an adjective: ")
    silly_word = input("Enter a silly word: ")

    story = f'''
    It was about {number} {measure_of_time} ago when I arrived at the hospital in a {mode_of_transportation}. 
    The hospital is a/an {adjective} place, there are a lot of {adjective2} {noun} here. 
    There are nurses here who have {color} {part_of_body}. If someone wants to come into my room I told them 
    that they have to (verb) first. I’ve decorated my room with {number2} {noun2}. Today I talked to a doctor and 
    they were wearing a {noun3} on their {part_of_body2}. I heard that all doctors {verb} {noun4} every day for 
    breakfast. The most {adjective3} thing about being in the hospital is the {silly_word} {noun} ! 
    '''

    print(story)


def generate_story2():          # template2

    person_name = input("Enter a person's name: ")
    noun = input("Enter a noun: ")
    adjective = input("Enter an adjective (feeling): ")
    verb = input("Enter a verb: ")
    adjective2 = input("Enter another adjective (feeling): ")
    animal = input("Enter an animal: ")
    verb2 = input("Enter a verb (ending in 'ing'): ")
    color = input("Enter a color: ")
    verb_ing = input("Enter a verb (ending in 'ing'): ")
    adverb = input("Enter an adverb (ending in 'ly'): ")
    number = input("Enter a number: ")
    measure_of_time = input(
        "Enter a measure of time (e.g. days, weeks, months): ")
    silly_word = input("Enter a silly word: ")
    noun2 = input("Enter a noun: ")

    story = f'''
    This weekend I am going camping with {person_name}. I packed my lantern, sleeping bag,
    and {noun}. I am so {adjective} to {verb} in a tent. I am {adjective2} we might see a(n)
    {animal}, I hear they’re kind of dangerous. While we’re camping, we are going to hike, fish, and {verb2}. I
    have heard that the {color} lake is great for {verb_ing}. Then we will {adverb} hike
    through the forest for {number} {measure_of_time}. If I see a {color} {animal} while hiking, I am going to bring
    it home as a pet! At night we will tell {number} {silly_word} stories and roast {noun2} around the campfire!!
    '''

    print(story)


def generate_story3():          # template3

    person_name = input("Enter a person's name: ")
    adjective = input("Enter an adjective: ")
    color = input("Enter a color: ")
    animal = input("Enter an animal: ")
    place = input("Enter a place: ")
    adjective2 = input("Enter an adjective: ")
    magical_creature = input(
        "Enter a plural magical creature (e.g. unicorns): ")
    adjective3 = input("Enter an adjective: ")
    magical_creature2 = input(
        "Enter another plural magical creature (e.g. fairies): ")
    room_in_a_house = input("Enter a room in a house: ")
    noun = input("Enter a noun: ")
    noun2 = input("Enter a noun: ")
    noun_plural1 = input("Enter a plural noun: ")
    adjective4 = input("Enter an adjective: ")
    noun_plural2 = input("Enter another plural noun: ")
    number = input("Enter a number: ")
    measure_of_time = input(
        "Enter a measure of time (e.g. days, weeks, months): ")
    verb_ing = input("Enter a verb ending in -ing: ")
    adjective5 = input("Enter an adjective: ")
    noun5 = input("Enter a noun: ")

    story = f'''
    Dear {person_name}, I am writing to you from a {adjective} castle in an enchanted forest. I
    found myself here one day after going for a ride on a {color} {animal} in {place}. There are {adjective2}
    {magical_creature} and {adjective3} {magical_creature2} here! In the {room_in_a_house} there is a pool full
    of {noun}. I fall asleep each night on a {noun2} of {noun_plural1} and dream of {adjective4} {noun_plural2}. It
    feels as though I have lived here for {number} {measure_of_time}. I hope one day you can visit, although the
    only way to get here now is {verb_ing} on a {adjective5} {noun5}!!
    '''

    print(story)


if template == 1:
    generate_story1()
elif template == 2:
    generate_story2()
elif template == 3:
    generate_story3()
