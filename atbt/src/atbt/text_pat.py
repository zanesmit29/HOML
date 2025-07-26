import re
def phone_number(text):
    if len(text) != 12:
        return False
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False
    return True

def main():
    # print(phone_number("123-456-7890"))  # True
    # print(phone_number("123-45-67890"))  # False
    # print(phone_number("123-4567-890"))  # False
    # print(phone_number("1234567890"))     # False
    # print(phone_number("123-456-78a0"))   # False

    # message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office number.'

    # for i in range(len(message)-11):
    #     segment = message[i:i+12]
    #     if phone_number(segment):
    #         print(f"Found phone number: {segment}")
    
    # for word in message.split():
    #     if phone_number(word):
    #         print(f"Found phone number: {word}")

    # phone_num_pattern_obj = re.compile(r'\d{3}-\d{3}-\d{4}')
    # match_obj1 = phone_num_pattern_obj.search(message)
    # match_obj2 = phone_num_pattern_obj.findall(message)
    # print(match_obj1.group())  # This will return the first match
    # print(match_obj1)  # This will return the match object
    # print(match_obj2)  # This will return a list of all matches
    # for match in match_obj2:
    #     print(f"Found phone number: {match}")

    ## Matching characters from alternate groups
    # pattern = re.compile(r'Cat(erpillar|astrophe|ch|egory)')
    # match = pattern.findall('The Catastrophe was a catch.')
    # print(match)

    ## Matching character classes and Negated character classes
    # vowel_pattern = re.compile(r'[aeiouAEIOU]')
    # match = vowel_pattern.findall('RoboCop eats BABY FOOD')
    # consonant_pattern = re.compile(r'[^aeiouAEIOU]')
    # match = consonant_pattern.findall('RoboCop eats BABY FOOD')
    # print(match)  # This will return a list of all vowels found in the string

    ## Matching with shorthand character classes
    # pattern = re.compile(r'\d+\s\w+')
    # match = pattern.findall('12 drummers, 11 pipers, 10 lords, 9 ladies dancing, 8 maids, 7 swans, 6 geese, 5 golden rings, 4 calling birds, 3 French hens, 2 turtle doves, 1 partridge.')
    # print(match)  # This will return a list of all matches

    ## Matching with the dot character
    # at_re = re.compile(r'.at')
    # match = at_re.findall('The cat sat on the mat.')
    # print(match)  # This will return a list of all matches

    ## Matching everything
    # name_pattern = re.compile(r'First name: (.*) Last name: (.*)')
    # name_match = name_pattern.search('First name: Al Last name: Sweigart')
    # print(name_match.group(1))  # This will return 'Al'
    # print(name_match.group(2))  # This will return 'Sweigart'

    ## Matching greedy and lazy patterns
    # lazy_pattern = re.compile(r'<.*?>') # This will match the shortest possible string between < and >
    # lazy_match = lazy_pattern.findall('<To serve humans> for dinner.>')
    # print(lazy_match)  # This will return a list of all matches
    # greedy_pattern = re.compile(r'<.*>') # This will match the longest possible string between < and >
    # greedy_match = greedy_pattern.findall('<To serve humans> for dinner.>')
    # print(greedy_match)  # This will return a list of all matches

    ## Matching optional patterns
    # pattern = re.compile(r'42!?') # This will match '42' followed by an optional '!'
    # match = pattern.search('The answer is 42!')
    # print(match.group())  # This will return '42!'
    # match2 = pattern.search('The answer is 42')
    # print(match2.group())  # This will return '42'
    pattern = re.compile(r'(\d{3}-)?\d{3}-\d{4}')  # This will match phone numbers with an optional area code
    match = pattern.search('Call me at 415-555-1011 tomorrow. 555-9999 is my office number.')
    print(match.group())  # This will return a list of all matches, including those with and without area codes


    ## Matching newlines
    # no_newline_re = re.compile(r'.*')
    # match = no_newline_re.search('Serve the public trust.\nProtect the innocent.\nUphold the law.')
    # print(match.group())  # This will return the first match, which does not include newlines

    # newline_re = re.compile(r'.*', re.DOTALL)
    # match = newline_re.search('Serve the public trust.\nProtect the innocent.\nUphold the law.')
    # print(match.group())  # This will return the entire string, including newlines




if __name__ == "__main__":
    main()