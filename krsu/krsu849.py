text = input()  
first_char = text[0]  
last_char = text[-1]   
last_two_char = text[-2:]  
def find_last_vowel(text):
    vowels = "АEIOUY"  # Список гласных (русский алфавит)
    
    # Проходим по тексту с конца
    for char in reversed(text):
        if char in vowels:
            return char
    return None  # Если гласных нет, возвращаем None

last_vowel = find_last_vowel(text)
print(last_vowel)


# print(last_two_char) 
# ####### UNDUU
# # А (а), E (е), I (и), O (о), U(у), Y (ы)
# if first_char  == "2" and (last_char == "E" or last_char == "I"):
#     print(text[2:]+"NIN")
# elif first_char  == "2" and (last_char == "A" or last_char == "Y"):
#     print(text[2:]+"NYN")
# elif first_char  == "2" and (last_char == "O" or last_char == "U"):
#     print(text[2:]+"NUN")
# elif first_char  == "3" and (last_char == "A" or last_char == "Y" or last_char == "U"):
#     print(text[2:]+"GA")
# elif first_char  == "3" and (last_char == "E" or last_char == "I"):
#     print(text[2:]+"GE")
# elif first_char  == "3" and last_char == "O":
#     print(text[2:]+"GO")    
# elif first_char  == "4" and (last_char == "A" or last_char == "Y"):
#     print(text[2:]+"NY")
# elif first_char  == "4" and (last_char == "E" or last_char == "I"):
#     print(text[2:]+"NI")
# elif first_char  == "4" and (last_char == "O" or last_char == "U"):
#     print(text[2:]+"NU") 
# elif first_char  == "5" and (last_char == "A" or last_char == "U" or last_char == "Y"):
#     print(text[2:]+"DA")
# elif first_char  == "5" and (last_char == "E" or last_char == "I"):
#     print(text[2:]+"DE")
# elif first_char  == "5" and last_char == "O":
#     print(text[2:]+"DO") 
# elif first_char  == "6" and (last_char == "A" or last_char == "U" or last_char == "Y"):
#     print(text[2:]+"DAN")
# elif first_char  == "6" and (last_char == "E" or last_char == "I"):
#     print(text[2:]+"DEN")
# elif first_char  == "6" and last_char == "O":
#     print(text[2:]+"DON")       

# ######  UNSUZ
# # B, D, G, K, L, M, N, P, R, S, T

# ######22222222
# elif first_char  == "2" and ((last_two_char == "AB" or last_two_char == "YB" or 
#                             last_two_char == "AD" or last_two_char == "YD" or 
#                             last_two_char == "AG" or last_two_char == "YG" or 
#                             last_two_char == "AN" or last_two_char == "YN" or 
#                             last_two_char == "AL" or last_two_char == "YL" or 
#                             last_two_char == "AM" or last_two_char == "YM" or 
#                             last_two_char == "AR" or last_two_char == "YR")or 
#                             last_char == "B" or last_char == "D" or last_char == "G" or
#                             last_char == "N" or last_char == "L" or last_char == "M"or last_char == "R"):
#     print(text[2:]+"DYN")

# elif first_char  == "2" and ((last_two_char == "AK" or last_two_char == "YK" or 
#                             last_two_char == "AP" or last_two_char == "YP" or 
#                             last_two_char == "AS" or last_two_char == "YS" or 
#                             last_two_char == "AT" or last_two_char == "YT")or 
#                             last_char == "K" or last_char == "P" or last_char == "S" or
#                             last_char == "T"):
#     print(text[2:]+"TYN")

# elif first_char  == "2" and (last_two_char == "OB" or last_two_char == "UB" or 
#                             last_two_char == "OD" or last_two_char == "UD" or 
#                             last_two_char == "OG" or last_two_char == "UG" or 
#                             last_two_char == "ON" or last_two_char == "UN" or 
#                             last_two_char == "OL" or last_two_char == "UL" or 
#                             last_two_char == "OM" or last_two_char == "UM" or 
#                             last_two_char == "OR" or last_two_char == "UR"):
#     print(text[2:]+"DUN")

# elif first_char  == "2" and (last_two_char == "OK" or last_two_char == "UK" or 
#                             last_two_char == "OP" or last_two_char == "UP" or 
#                             last_two_char == "OS" or last_two_char == "US" or 
#                             last_two_char == "OT" or last_two_char == "UT"):
#     print(text[2:]+"TUN")

# elif first_char  == "2" and (last_two_char == "EB" or last_two_char == "IB" or 
#                             last_two_char == "ED" or last_two_char == "ID" or 
#                             last_two_char == "EG" or last_two_char == "IG" or 
#                             last_two_char == "EN" or last_two_char == "IN" or 
#                             last_two_char == "EL" or last_two_char == "IL" or 
#                             last_two_char == "EM" or last_two_char == "IM" or 
#                             last_two_char == "ER" or last_two_char == "IR"):
#     print(text[2:]+"DIN")

# elif first_char  == "2" and (last_two_char == "EK" or last_two_char == "IK" or 
#                             last_two_char == "EP" or last_two_char == "IP" or 
#                             last_two_char == "ES" or last_two_char == "IS" or 
#                             last_two_char == "ET" or last_two_char == "IT"):
#     print(text[2:]+"TIN")

# ###33333333333
# elif first_char  == "3" and ((last_two_char == "AB" or last_two_char == "YB" or last_two_char == "UB" or
#                             last_two_char == "AD" or last_two_char == "YD" or last_two_char == "UD" or
#                             last_two_char == "AG" or last_two_char == "YG" or last_two_char == "UG" or
#                             last_two_char == "AN" or last_two_char == "YN" or last_two_char == "UN" or
#                             last_two_char == "AL" or last_two_char == "YL" or last_two_char == "UL" or 
#                             last_two_char == "AM" or last_two_char == "YM" or last_two_char == "UM" or
#                             last_two_char == "AR" or last_two_char == "YR" or last_two_char == "UR")or 
#                             last_char == "B" or last_char == "D" or last_char == "G" or
#                             last_char == "N" or last_char == "L" or last_char == "M"or last_char == "R"):
#     print(text[2:]+"GA")

# elif first_char  == "3" and ((last_two_char == "AK" or last_two_char == "YK" or last_two_char == "UK" or
#                             last_two_char == "AP" or last_two_char == "YP" or last_two_char == "UP" or
#                             last_two_char == "AS" or last_two_char == "YS" or last_two_char == "US" or
#                             last_two_char == "AT" or last_two_char == "YT" or last_two_char == "UT")or
#                             last_char == "K" or last_char == "P" or last_char == "S" or
#                             last_char == "T"):
#     print(text[2:]+"KA")

# elif first_char  == "3" and (last_two_char == "EB" or last_two_char == "IB" or 
#                             last_two_char == "EG" or last_two_char == "IG" or 
#                             last_two_char == "EN" or last_two_char == "IN" or
#                             last_two_char == "EL" or last_two_char == "IL" or 
#                             last_two_char == "ER" or last_two_char == "IR" or 
#                             last_two_char == "EM" or last_two_char == "IM"):
#     print(text[2:]+"GE")

# elif first_char  == "3" and (last_two_char == "ET" or last_two_char == "IT" or 
#                             last_two_char == "ES" or last_two_char == "IS" or 
#                             last_two_char == "EK" or last_two_char == "IK"):
#     print(text[2:]+"KE")    

# elif first_char  == "3" and (last_two_char == "OB" or 
#                             last_two_char == "OD" or  
#                             last_two_char == "OG" or  
#                             last_two_char == "ON" or  
#                             last_two_char == "OL" or  
#                             last_two_char == "OM" or  
#                             last_two_char == "OR"):
#     print(text[2:]+"GO")

# elif first_char  == "3" and (last_two_char == "OK" or 
#                             last_two_char == "OP" or  
#                             last_two_char == "OS" or  
#                             last_two_char == "OT"):
#     print(text[2:]+"KO")
# ##############4444444444444444444444
# elif first_char  == "4" and ((last_two_char == "AB" or last_two_char == "YB" or last_two_char == "UB" or
#                             last_two_char == "AD" or last_two_char == "YD" or last_two_char == "UD" or
#                             last_two_char == "AG" or last_two_char == "YG" or last_two_char == "UG" or
#                             last_two_char == "AN" or last_two_char == "YN" or last_two_char == "UN" or
#                             last_two_char == "AL" or last_two_char == "YL" or last_two_char == "UL" or 
#                             last_two_char == "AM" or last_two_char == "YM" or last_two_char == "UM" or
#                             last_two_char == "AR" or last_two_char == "YR" or last_two_char == "UR")or 
#                             last_char == "B" or last_char == "D" or last_char == "G" or
#                             last_char == "N" or last_char == "L" or last_char == "M"or last_char == "R"):
#     print(text[2:]+"DY")

# elif first_char  == "4" and ((last_two_char == "AK" or last_two_char == "YK" or last_two_char == "UK" or
#                             last_two_char == "AP" or last_two_char == "YP" or last_two_char == "UP" or
#                             last_two_char == "AS" or last_two_char == "YS" or last_two_char == "US" or
#                             last_two_char == "AT" or last_two_char == "YT" or last_two_char == "UT")or
#                             last_char == "K" or last_char == "P" or last_char == "S" or
#                             last_char == "T"):
#     print(text[2:]+"TY")

# elif first_char  == "4" and (last_two_char == "EB" or last_two_char == "IB" or 
#                             last_two_char == "EG" or last_two_char == "IG" or 
#                             last_two_char == "EN" or last_two_char == "IN" or
#                             last_two_char == "EL" or last_two_char == "IL" or 
#                             last_two_char == "ER" or last_two_char == "IR" or 
#                             last_two_char == "EM" or last_two_char == "IM"):
#     print(text[2:]+"DI")

# elif first_char  == "4" and (last_two_char == "ET" or last_two_char == "IT" or 
#                             last_two_char == "ES" or last_two_char == "IS" or 
#                             last_two_char == "EK" or last_two_char == "IK"):
#     print(text[2:]+"TI")    

# elif first_char  == "4" and (last_two_char == "OB" or 
#                             last_two_char == "OD" or  
#                             last_two_char == "OG" or  
#                             last_two_char == "ON" or  
#                             last_two_char == "OL" or  
#                             last_two_char == "OM" or  
#                             last_two_char == "OR"):
#     print(text[2:]+"DU")

# elif first_char  == "4" and (last_two_char == "OK" or 
#                             last_two_char == "OP" or  
#                             last_two_char == "OS" or  
#                             last_two_char == "OT"):
#     print(text[2:]+"TU")

# ##############55555555555555555555
# elif first_char  == "5" and ((last_two_char == "AB" or last_two_char == "YB" or last_two_char == "UB" or
#                             last_two_char == "AD" or last_two_char == "YD" or last_two_char == "UD" or
#                             last_two_char == "AG" or last_two_char == "YG" or last_two_char == "UG" or
#                             last_two_char == "AN" or last_two_char == "YN" or last_two_char == "UN" or
#                             last_two_char == "AL" or last_two_char == "YL" or last_two_char == "UL" or 
#                             last_two_char == "AM" or last_two_char == "YM" or last_two_char == "UM" or
#                             last_two_char == "AR" or last_two_char == "YR" or last_two_char == "UR")):# or 
#                             # last_char == "B" or last_char == "D" or last_char == "G" or
#                             # last_char == "N" or last_char == "L" or last_char == "M"or last_char == "R"*/):
#     print(text[2:]+"DA")

# elif first_char  == "5" and ((last_two_char == "AK" or last_two_char == "YK" or last_two_char == "UK" or
#                             last_two_char == "AP" or last_two_char == "YP" or last_two_char == "UP" or
#                             last_two_char == "AS" or last_two_char == "YS" or last_two_char == "US" or
#                             last_two_char == "AT" or last_two_char == "YT" or last_two_char == "UT")or
#                             last_char == "K" or last_char == "P" or last_char == "S" or
#                             last_char == "T"):
#     print(text[2:]+"KA")

# elif first_char  == "5" and (last_two_char == "EB" or last_two_char == "IB" or 
#                             last_two_char == "EG" or last_two_char == "IG" or 
#                             last_two_char == "EN" or last_two_char == "IN" or
#                             last_two_char == "EL" or last_two_char == "IL" or 
#                             last_two_char == "ER" or last_two_char == "IR" or 
#                             last_two_char == "EM" or last_two_char == "IM"):
#     print(text[2:]+"DE")

# elif first_char  == "5" and (last_two_char == "ET" or last_two_char == "IT" or 
#                             last_two_char == "ES" or last_two_char == "IS" or 
#                             last_two_char == "EK" or last_two_char == "IK"):
#     print(text[2:]+"TE")    

# elif first_char  == "5" and (last_two_char == "OB" or 
#                             last_two_char == "OD" or  
#                             last_two_char == "OG" or  
#                             last_two_char == "ON" or  
#                             last_two_char == "OL" or  
#                             last_two_char == "OM" or  
#                             last_two_char == "OR"):
#     print(text[2:]+"DO")

# elif first_char  == "5" and (last_two_char == "OK" or 
#                             last_two_char == "OP" or  
#                             last_two_char == "OS" or  
#                             last_two_char == "OT"):
#     print(text[2:]+"TO")

# ##########66666666666666666666
# elif first_char  == "6" and ((last_two_char == "AB" or last_two_char == "YB" or last_two_char == "UB" or
#                             last_two_char == "AD" or last_two_char == "YD" or last_two_char == "UD" or
#                             last_two_char == "AG" or last_two_char == "YG" or last_two_char == "UG" or
#                             last_two_char == "AN" or last_two_char == "YN" or last_two_char == "UN" or
#                             last_two_char == "AL" or last_two_char == "YL" or last_two_char == "UL" or 
#                             last_two_char == "AM" or last_two_char == "YM" or last_two_char == "UM" or
#                             last_two_char == "AR" or last_two_char == "YR" or last_two_char == "UR")or 
#                             last_char == "B" or last_char == "D" or last_char == "G" or
#                             last_char == "N" or last_char == "L" or last_char == "M"or last_char == "R"):
#     print(text[2:]+"DAN")

# elif first_char  == "6" and ((last_two_char == "AK" or last_two_char == "YK" or last_two_char == "UK" or
#                             last_two_char == "AP" or last_two_char == "YP" or last_two_char == "UP" or
#                             last_two_char == "AS" or last_two_char == "YS" or last_two_char == "US" or
#                             last_two_char == "AT" or last_two_char == "YT" or last_two_char == "UT")or
#                             last_char == "K" or last_char == "P" or last_char == "S" or
#                             last_char == "T"):
#     print(text[2:]+"TAN")

# elif first_char  == "6" and (last_two_char == "EB" or last_two_char == "IB" or 
#                             last_two_char == "EG" or last_two_char == "IG" or 
#                             last_two_char == "EN" or last_two_char == "IN" or
#                             last_two_char == "EL" or last_two_char == "IL" or 
#                             last_two_char == "ER" or last_two_char == "IR" or 
#                             last_two_char == "EM" or last_two_char == "IM"):
#     print(text[2:]+"DEN")

# elif first_char  == "6" and (last_two_char == "ET" or last_two_char == "IT" or 
#                             last_two_char == "ES" or last_two_char == "IS" or 
#                             last_two_char == "EK" or last_two_char == "IK"):
#     print(text[2:]+"TEN")    

# elif first_char  == "6" and (last_two_char == "OB" or 
#                             last_two_char == "OD" or  
#                             last_two_char == "OG" or  
#                             last_two_char == "ON" or  
#                             last_two_char == "OL" or  
#                             last_two_char == "OM" or  
#                             last_two_char == "OR"):
#     print(text[2:]+"DON")

# elif first_char  == "6" and (last_two_char == "OK" or 
#                             last_two_char == "OP" or  
#                             last_two_char == "OS" or  
#                             last_two_char == "OT"):
#     print(text[2:]+"TON")

