            # Question 3 // Soru 3

#            WHat is the largest prime factor of the number 600851475143

#            600851475143 sayısının en büyük asal bölenini = ?


# import math

# def prime_check(x):
#     is_prime = True

#     for i in range(2,int(math.sqrt(x) + 1)):
#         if x %i == 0:
#             is_prime = False
#             continue
#     return is_prime

# number = 600851475143


# biggest_prime = 1

# for i in range(2, int(math.sqrt(number))):
#     if number %i == 0 and prime_check(i):
#         biggest_prime = i

# print(biggest_prime)


        # I found this answer on youtube:
n = 600851475143
i = 2

while i*i < n:
    if n %i == 0:
        n /=i 
    i +=1 

print(n)
