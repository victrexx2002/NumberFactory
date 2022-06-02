from ast import For
from email.utils import format_datetime
from gettext import find
from lib2to3.pytree import convert
from math import remainder
import math
from operator import index, indexOf
import sys
from unicodedata import decimal
from decimal import Decimal

if len(sys.argv) < 2:
    print ("No number provided")
    quit()

number_input = sys.argv[1]
def even(number_input) :
    number= float(number_input)
    if number%2 ==0 :
        return(number_input + ' is even')
    elif number%2 ==1 :
        return(number_input + '  is odd')
    else :
        return(number_input + ' is not an integer')
    

def integer_string(number_input) :
    numberstring = str(number_input)
    if '.' in numberstring :
        integerString = numberstring[0 : numberstring.index('.')]
        return integerString
    else : 
        return numberstring[0 : ]


def decimal_string(number_input) :
    if '.' in number_input :
        decimalString = number_input[number_input.index('.')+1 : ]
        return decimalString
    else :
        return ""



def integer_precision() :
    integerPrecision = len(integer_string(number_input))
    return integerPrecision


def decimal_precision() :
    decimalPrecision = len(decimal_string(number_input))
    return decimalPrecision



def precision() :
    return integer_precision() + decimal_precision() 



def formatted_string(number_input) :
    return ("{:,}".format(float(number_input)))
    


def prime_number(number_input) :
    if '.' in number_input :
        return False 
    number = int(number_input)
    if number == 1 :
        return False
    elif number == 2 :
        return True
    else :
        for i in range(2, number, 1) :
            if number % i == 0 :
                return False
        
    return True




def numberbaseconverter(number_input , n):
    if '.' in number_input:
        splitttt = number_input.split('.')
        integer_part = int(splitttt[0])
        decimal_part = float('.' + splitttt[1])
        converted_integer_list = []
        converted_decimal_list = []
        hexadecimal_list = {
            'A' : 10,
            'B' : 11,
            'C' : 12,
            'D': 13,
            'E' : 14,
            'F' : 15
        }
        alphabet_list = list(hexadecimal_list.keys())
        number_list = list(hexadecimal_list.values())
        def integertobase(integer_part, n) :
            answer = divmod(integer_part, n)
            if answer[1] in number_list:
                position = number_list.index(answer[1])
                converted_integer_list.append(alphabet_list[position])
                if answer[0] == 0 :
                    return converted_integer_list
                else :
                    integertobase(answer[0], n)
            else :
                converted_integer_list.append(answer[1])
                if answer[0] == 0 :
                    return converted_integer_list
                else :
                    integertobase(answer[0], n)
                return converted_integer_list
        integertobase(integer_part, n)
        def floattobase(decimal_part, n):
            r = decimal_part*n
            answer = math.floor(r)
            remainder = Decimal(r) % 1
            if answer in number_list:
                position = number_list.index(answer)
                converted_decimal_list.append(alphabet_list[position])
                if len(converted_decimal_list) > 5 :
                    return converted_decimal_list
                else :
                    floattobase(remainder, n)   
            else :
                converted_decimal_list.append(answer)
                if len(converted_decimal_list) > 5 :
                    return converted_decimal_list
                else :
                    floattobase(remainder, n)
            return converted_decimal_list
        floattobase(decimal_part,n)

        converted_integer_list.reverse()
        return ("".join(map(str, converted_integer_list))) + '.' +(''.join(map(str, converted_decimal_list)))
    else :
        integer_part = int(number_input)
        hexadecimal_list = {
            'A' : 10,
            'B' : 11,
            'C' : 12,
            'D': 13,
            'E' : 14,
            'F' : 15
        }
        alphabet_list = list(hexadecimal_list.keys())
        number_list = list(hexadecimal_list.values())
        converted_integer_list = []
        def integertobase(integer_part, n) :
            answer = divmod(integer_part, n)
            if answer[1] in number_list:
                position = number_list.index(answer[1])
                converted_integer_list.append(alphabet_list[position])
                if answer[0] == 0 :
                    return converted_integer_list
                else :
                    integertobase(answer[0], n)
            else :
                converted_integer_list.append(answer[1])
                if answer[0] == 0 :
                    return converted_integer_list
                else :
                    integertobase(answer[0], n)
                return converted_integer_list
        integertobase(integer_part, n)
        converted_integer_list.reverse()
        return ("".join(map(str, converted_integer_list)))
        

numberbaseconverter(number_input, 16)
        

def numbertowords(n):


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


    def fractions(x):
        if float(x) == 0 :
            return
        number_string = str(x)
        result = 'point'
        for element in number_string:
            result += ' ' + words[ones_index + int(element)]
        return result
    

    def ones(x):
        return words[ones_index + int(x)]
    

    def tens(x):
        number_string = str(x)
        tens_digit = int(number_string[0:1])
        unit_digit = int(number_string[1])
        result = words[tens_index + tens_digit -2]
        if unit_digit > 0 :
            return ' '.join([result, ones(unit_digit)])

        return result
    
    
    def hundreds(x):
        number_string = str(x)
        hundreds_digit = int(number_string[0:1])
        tens_remainder = int(number_string[1:])
        result = ones(hundreds_digit) + ' ' + words[huns_index]
        if tens_remainder > 0 :
            if tens_remainder < 21 :
                return ' '.join([result, 'and', ones(tens_remainder)])
            else :
                return ' '.join([result, 'and', tens(tens_remainder)])
    
        return result


    def underThousands(x):
        import re
        if re.search("^1?[0-9]$", str(x)) :
            return ones(x)
                
        if re.search("^[2-9][0-9]$", str(x)) :
            return tens(x)
                
        if re.search("^[0-9][0-9][0-9]$", str(x)) :
            return hundreds(x)


    def overThousands(x):
        number_string = str(x)
        number_length = len(number_string)
        number_words_index = ((number_length-1)//3)-1
        thousands_index = number_length-2
        if number_words_index >= len(words) - mils_index :
            words_string = str(words).replace()
            txt ="this number is too big for me, consider adding to this list in the code \n words like {}" 
            return txt.format(words)
        mils_name = words[mils_index + number_words_index]
        right_length = ((number_length - 1)//3)*3
        left_length = number_length - right_length
        left_string = number_string[0 : left_length]
        right_string = number_string[-right_length : ]
        if int(left_string) > 0 :
            result = " ".join([underThousands(left_string), mils_name ])
            if int(right_string) > 999 :
                return ", ".join([ result, overThousands(right_string)])
        
            if int(right_string) > 99 :
                return ", ".join([ result, underThousands(right_string)])
        
            if int(right_string) > 0 :
                return ' '.join([ result, ' and ', underThousands(right_string)])
      
        return result


    def thousands_check(x) :
        if len(str(x)) < 4 :
            return underThousands(x)
        else :
            return overThousands(x) 
    
    
    number_string = str(n)
    position_of_point = number_string.find(decimal_separator)
    integer_part = number_string[0 : position_of_point]
    decimal_part = number_string[position_of_point + 1 :]
    if decimal_separator in number_string :
        return thousands_check(integer_part) + ' ' + fractions(decimal_part)
    else :
        return thousands_check(number_string)        
     

numberFactory = {
    'even' : even(number_input),
    'integer string' : integer_string(number_input),
    'decimal string' : decimal_string(number_input),
    'integer precision' : integer_precision(),
    'decimal precision' : decimal_precision(),
    'precision' : precision(),
    'formatted string' : formatted_string(number_input),
    'prime' : prime_number(number_input),
    'hexadecimal' : numberbaseconverter(number_input, 16),
    'number to words' : numbertowords(number_input)
}


print(numberFactory)
    
