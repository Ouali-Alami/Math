# A number is divisble by three if the sum of its digits is divisible by 3 
# For example 12345 = 1+2+3+4+5 = 15 then 1+5 = 6 then 6 is a single digit then 6 is divisible by 3
# this example make me feel there is an even faster way for the particulary case of the sum of the i from 0 to x, to dig....
# for this alogrithm to be useful you must imperatively convert the number into a string in order 
# to obtain each digit otherwise it is strictly useless
# the time complexity will be even worse because 
# you will apply the modulo on each of the numbers' digit
# we can apply the same algorithm for the divider 9
# source : 
def IsDivisbleByThree(x) -> bool:
    number = str(x)
    sum = 0
    for digit in number:
        sum += int(digit)
    if(sum > 10):
        return IsDivisbleByThree(sum)
    else:
        return sum % 3 == 0

# A ≡ B [N] <=> B = A + N*K <=> B-A = N*K put another way N divide( B - A) K times
# another way to tell A//N and B//N have the same remainder in Euclidean division
# cool there is already a method that tell if a number is divisble by 3...
# source : https://www.youtube.com/watch?v=BByKm1u16qs (congruence)    
def IsCongruentModThree(a , b) -> bool:
    return IsDivisbleByThree(b - a)


# todo : https://www.youtube.com/watch?v=c51T2kZpkS4 (divisble by 7)
# todo : https://math.univ-cotedazur.fr/~walter/L1_Arith/cours3.pdf
# todo : https://www.youtube.com/watch?v=OY-NA5MjcCc (arithmetic)
# todo: change to generic algorithm when u have all the tips...
  


