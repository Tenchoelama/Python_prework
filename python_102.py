#Question 1
def greetings(user_name):
    return print("hello"+user_name.upper())

greetings("Frodo")

#Question 2
def first_odds():
    for numbers in range(1, 101):
        if numbers % 2 != 0:
           print(numbers)
first_odds()


#Question 3 
def max_num_in_list(a_list):
    
   max = a_list[0]
   for x in a_list:
        if x > max:
            max = x
        return max

print(max_num_in_list([1,2,3, -10,5]))

#Question 4
def is_leap_year(a_year):
    '''Checks if given year is a leap year'''
    if (a_year % 4 == 0) and (a_year % 100 != 0):
        return True
    elif (a_year % 400 == 0):
        return True
    else:
        return False
print(is_leap_year(2022))

#Question 5
def is_consecutive(a_list):
    if sorted(a_list) == list(range((min(a_list)), (max(a_list) +1))):
        return True
    else:
        return False