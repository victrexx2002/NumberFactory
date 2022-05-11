number_input = input('what number do you want to convert to words?')
def numberToWords(number_input):
    # the french are a strange bunch, they swap these two, we will default to English here
    decimal_separator = '.'
    words = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 
        'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 
        'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty', 
        'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety',
        'hundred', 'thousand', 'million', 'billion', 'trillion', 
        'quadrillion', 'quintillion', 'sextillion']
    ones_index = 0   # all the single letter words start at index 0 to index 20
    tens_index = 20  # 2 letter number prefixes start here
    huns_index = 28  # the word hundred, kind of an odd man out
    mils_index = 29 # all the powers of 1000 start here keep adding to your hearts delight
    def fractions(number):
        if float(number) == 0 :
            return
        number_string = str(number)
        result = 'point'
        for x in number_string:
            result = ' '.join( result , words[ones_index + int(number_string[x])])
        return result
    
    def return_result(result):
        if float(fraction_string) > 0 :
            return ' '.join( result, fraction_result )
        else :
            return result


    def ones(number):
        return words[ones_index + int(number)]

    def tens(number):
        number_string = str(number)
        tens_digit = int(number_string[0:1])
        unit_digit = int(number_string[1])
        result = words[tens_index + tens_digit -2]
        if unit_digit > 0 :
            return ' '.join(result, ones(unit_digit))

        return result
    
    def hundreds(number):
        number_string = str(number)
        hundreds_digit = int(number_string[0:1])
        tens_remainder = int(number_string[1])
        result = ' '.join(ones(hundreds_digit), words[huns_index])
        if tens_remainder > 0 :
            if tens_remainder < 21 :
                return ' '.join(result, 'and', ones(tens_remainder))
            else :
                 return ' '.join( result, 'and', tens(tens_remainder))
    
        return result

    def thousands(number) :
        number_string = str(number)
        number_length = len(number_string)
        number_words_index = ((number_length-1)//3)-1
        if number_words_index >= len(words) - mils_index :
            words_string = str(words).replace()
            txt ="this number is too big for me, consider adding to this list in the code \n words like {}" 
            return txt.format(words)
        
        mils_name = words[mils_index + number_words_index]
        right_length = ((number_length - 1)//3)*3
        left_length = number_length - right_length
        left_string = int(number_string[0, left_length])
        right_string = number_string[-right_length : ]
        result = ' '.join(numberToWords(left_string), mils_name)
        
        if float(right_string) > 0 :
            if float(right_string) < 100 :
                return ' and '.join(result, numberToWords(right_string))
            else :
                return ', '.join(result, numberToWords(right_string))
            
        return result
    




    '''
    we have to first make sure that the input given is actually a number 
    if its not a number it should return an error but we want to give a reason

    '''
    if number_input.strip().isdigit():
        return x
    else:
        print("User input is not a number")
    

    
    '''
    next up we want to manipulate the number and avoid floating point or integer limitations for large numbers
    '''
    number_string = str(number_input)
    fraction_string = ''
    number_split_on_dot = number_string.split(decimal_separator)
    if decimal_separator in number_string :
        number_string = number_split_on_dot[0]
        fraction_string = number_split_on_dot[1]
    
    fraction_result = fractions(fraction_string)

    import re


    if re.search("^1?[0-9]$", str(number_string)) :
        return return_result(ones(number_string))
    
    if re.search("^[2-9][0-9]$", str(number_string)) :
        return return_result(tens(number_string))
    
    if re.search("^[0-9][0-9][0-9]$", str(number_string)) :
        return return_result(hundreds(number_string))
    
    if len(number_string) > 3 :
        return return_result(thousands(number_string))
        
        
print(numberToWords(number_input))
