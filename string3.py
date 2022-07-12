def my_find_function(string_1, string_2):
    for i in range(len(string_1)-len(string_2)+1):
        for j in range(len(string_2)):
            if string_1[i+j] == string_2[j]:
                the_first_index = i
            else:
                the_first_index = 'string 1-i mej string 2-@ chka'
                break
        if the_first_index == i:
            break
    return the_first_index

def my_rfind_function(string_1, string_2):
    the_last_index = -1
    for i in range(len(string_1)-len(string_2)+1):
        for j in range(len(string_2)):
            if string_1[i+j] == string_2[j]:
                index = i
            else:
                index = 'string 1-i mej string 2-@ chka'
                break
        if index == i:
            the_last_index = i
    if the_last_index != -1:
        return the_last_index
    else:
        return index

def my_count_function(string_1, string_2):
    c = 0
    i = 0
    while i <= len(string_1)-len(string_2)+1:
        for j in range(len(string_2)):
            if string_1[i+j] == string_2[j]:
                index = i
            else:
                index = -1
                break
        if index == i:
            c += 1
            i += len(string_2)
        else:
            i += 1
    return c

def my_replace_function(string_1, string_2, string_3):
    if string_2 != string_3:
        i = 0
        new_string = ''
        while i <= len(string_1)-len(string_2)+1:
            for j in range(len(string_2)):
                if string_1[i+j] == string_2[j]:
                    index = i
                else:
                    index = -1
                    break
            if index == i:
                new_string += string_3
                i += len(string_2)
            else:
                new_string += string_1[i]
                i += 1
        for i in range(i, len(string_1)):
            new_string += string_1[i]
    return new_string

def my_upper_function(string_1):
    new_string = ''
    for i in range(len(string_1)):
        if 97 <= ord(string_1[i]) <= 122:
            new_string += chr(ord(string_1[i]) - 32)
        else:
            new_string += string_1[i]
    return new_string

def my_lower_function(string_1):
    new_string = ''
    for i in range(len(string_1)):
        if 65 <= ord(string_1[i]) <= 90:
            new_string += chr(ord(string_1[i]) + 32)
        else:
            new_string += string_1[i]
    return new_string

def my_isdigit_function(string_1):
    b = True
    for symbol in string_1:
        if 48 <= ord(symbol) <= 57:
            pass
        else:
            b = False
            break
    return b

def my_isalpha_function(string_1):
    b = True
    for symbol in string_1:
        if 65 <= ord(symbol) <= 90 or 97 <= ord(symbol) <= 122:
            pass
        else:
            b = False
            break
    return b

string_1 = input('mutqagreq string 1-@: ')
string_2 = input('mutqagreq string 2-@: ')
string_3 = input('mutqagreq string 3-@ string 2-in poxarinelu hamar: ')

print('\narajin index@: ', my_find_function(string_1, string_2))
print('verjin index@: ', my_rfind_function(string_1, string_2))
print('qanak@ teqstum:', my_count_function(string_1, string_2))
print('popoxvac teqst@: ', my_replace_function(string_1, string_2, string_3))
print('teqst@ mecatarerov: ', my_upper_function(string_1))
print('teqst@ poqratarerov: ', my_lower_function(string_1))
print('bolor simvolner@ tver en?: ', my_isdigit_function(string_1))
print('bolor simvolner@ tarer en?: ', my_isalpha_function(string_1))
