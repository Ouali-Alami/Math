def IsDivisbleByThree(x) -> bool:
    # A number is divisble by three if the sum of its digits is divisible by 3 
    # For example 12345 = 1+2+3+4+5 = 15 then 1+5 = 6 then 6 is a single digit then 6 is divisible by 3
    # this example make me feel there is an even faster way for the particulary case of the sum of the i from 0 to x, to dig....
    # for this alogrithm to be useful you must imperatively convert the number into a string in order 
    # to obtain each digit otherwise it is strictly useless
    #the time complexity will be even worse because you will apply the modulo on each of the digits of the number
    # we can apply the same algorithm for the divider 9
    number = str(x)
    sum = 0
    for digit in number:
        sum += int(digit)
    if(sum > 10):
        return IsDivisbleByThree(sum)
    else:
        return sum % 3 == 0
    # its the first step , to dig... the congruence and another tips for the criteria of divisibility by 7 ....
    # sources:
    # https://www.youtube.com/watch?v=BByKm1u16qs (congruence)
    # https://www.youtube.com/watch?v=c51T2kZpkS4 (divisble by 7)
    # https://www.youtube.com/watch?v=OY-NA5MjcCc (arithmetic)
  


