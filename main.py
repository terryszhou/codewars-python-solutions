# # # CONVERT NUMBER TO REVERSED ARRAY OF DIGITS
# # MY SOLVE
# def digitize(n):
#     lis_n = list(str(n))
#     lis_n.reverse()
#     lis_n = list(map(int, lis_n))
#     return lis_n

# # BEST SOLVE
# def digitize(n):
#     return map(int, str(n)[::-1])

# digitize(348597)

# # EQUIVALENT IN JAVASCRIPT
# const digitize = (n) => {
#   return n.toString().split("").reverse().map(e => parseInt(e))
# }

# digitize(348597)

# # # WHAT'S THE REAL FLOOR?
# # MY SOLVE
# def get_real_floor(n):
#     if (n > 0 and n <= 13):
#         return n - 1
#     elif (n > 13):
#         return n - 2
#     else:
#         return n

# # BEST SOLVE
# def get_real_floor(n):
#     if n <= 0: return n
#     if n < 13: return n-1
#     if n > 13: return n-2

# print(get_real_floor(-1))

# # # THE WIDE-MOUTHED FROG!
# # MY SOLVE
# def mouth_size(animal):
#     if (animal.lower() == "alligator"):
#         return "small"
#     else:
#         return "wide"

# # BEST SOLVE
# def mouth_size(animal):
#     return "small" if animal.lower() == "alligator" else "wide"

# print(mouth_size("ALLIGATOR"))

# # MY JS SOLVE
# const mouth_size = (animal) => {
#     if (animal.toLowerCase() === "alligator") {
#         return "small"
#     } else {
#         return "wide"
#     }
# }

# # BEST JS SOLVE
# const mouth_size = (animal) => {
#     return animal.toLowerCase() === "alligator" ? "small" : "wide"
# }

# # # SQUARE EVERY DIGIT
# # MY SOLVE
# def square_digits(num):
#     answer = map(lambda num: int(num) ** 2, str(num))
#     join_answer = "".join(map(str, answer))
#     return int(join_answer)

# # BEST SOLVE
# def square_digits(num):
#     ret = ""
#     for x in str(num):
#         ret += str(int(x)**2)
#     return int(ret)

# print(square_digits(9119))

# # MY JS SOLVE
# const squareDigits = (num) => {
#     let answer = num.toString().split("").map(e => {
#         return parseInt(e*e)
#     })
#     return parseInt(answer.join(""))
# }

# console.log(squareDigits(9119))

# # # MUMBLING
# # MY SOLVE
# def accum(s):
#     def find_ind(n):
#         return s.index(n)
#     map_s = list(map(lambda s: s + (s * find_ind(s)), s))
#     cap_s = list(map(lambda map_s: map_s.capitalize(), map_s))
#     return "-".join(cap_s)

# print(accum("HbideVbxncC"))

# # # HIGHEST AND LOWEST
# # MY SOLVE
# def high_and_low(numbers):
#     list_num = list(map(int, numbers.split()))
#     answer = f"{max(list_num)} {min(list_num)}"
#     return str(answer)

# print(high_and_low("1 2 3 4 5"))

# # BEST SOLVE
# def high_and_low(numbers): #z.
#     nn = [int(s) for s in numbers.split(" ")]
#     return "%i %i" % (max(nn),min(nn))

# # # LIST FILTERING
# # MY SOLVE
# def filter_list(l):
#     answer_list = []
#     for i in l:
#         if type(i) == int:
#             answer_list.append(i)
#     return answer_list

# # BEST SOLVE
# def filter_list(l):
#     return [i for i in l if not isinstance(i, str)]

# # # COUNT THE DIVISORS OF A NUMBER
# # MY SOLVE
# def divisors(n):
#     answer = []
#     for i in range(1, n + 1):
#         if n % i == 0:
#             answer.append(i)
#     return len(answer)

# # BEST SOLVE
# def divisors(n):
#     return  len([l_div for l_div in range(1, n + 1) if n % l_div == 0])

# print(divisors(4))

# # MY JS SOLVE
# function getDivisorsCnt(n){
#    let x = []
#    for (i = n; i >= 1; i--) {
#       x.push(i)
#    }
#   let y = x.map(e => {
#     if (n % e === 0) {
#       return e
#     }
#   }).filter(e => {
#     return e !== undefined
#   })
#   return y.length
# }

# # # FIND THE SMALLEST INTEGER IN THE ARRAY
# # MY SOLVE
# def find_smallest_int(arr):
#     return min(arr)

# print(find_smallest_int([34, 15, 88, 2]))

# # # COMPLEMENTARY DNA
# # MY SOLVE
# def DNA_strand(dna):
#     answer = []
#     for i in dna:
#         if (i == "A"): answer.append("T")
#         elif (i == "T"): answer.append("A")
#         elif (i == "G"): answer.append("C")
#         elif (i == "C"): answer.append("G")
#     return "".join(answer)

# # BEST SOLVE 1
# import string
# def DNA_strand(dna):
#     return dna.translate(string.maketrans("ATCG","TAGC"))

# # BEST SOLVE 2
# pairs = {'A':'T','T':'A','C':'G','G':'C'}
# def DNA_strand(dna):
#     return ''.join([pairs[x] for x in dna])

# print(DNA_strand("ATTGC"))

# # # COUNTING SHEEP...
# # MY SOLVE
# def count_sheeps(sheep):
#     count = 0
#     for i in sheep:
#         if i == True:
#             count += 1
#     return count

# # BEST SOLVE
# def count_sheeps(arrayOfSheeps):
#     return arrayOfSheeps.count(True)

# print(count_sheeps([True,  True,  True,  False,
#   True,  True,  True,  True ,
#   True,  False, True,  False,
#   True,  False, False, True ,
#   True,  True,  True,  True ,
#   False, False, True,  True]))

# # # DESCENDING ORDER
# # MY SOLVE
# def descending_order(num):
#     list_num = str(num)
#     list_num.sort(reverse=True)
#     return int("".join(list_num))

# # BEST SOLVE
# def Descending_Order(num):
#     return int("".join(sorted(str(num), reverse=True))) 

# # # FACTORIAL
# # MY SOLVE
# def factorial(n):
#     answer = 1
#     if n < 0 or n > 12:
#         raise ValueError
#     else:
#         for i in range(1, n + 1):
#             answer *= i
#     return answer

# # BEST SOLVE
# def factorial(n):
#     if n < 0 or n > 12:
#         raise ValueError
#     return 1 if n <= 1 else n*factorial(n-1)

# # # MY JS SOLVE
# # const factorial = (n) => {
# #   answer = 1
# #   if (n < 0 || n > 12) {
# #     throw RangeError("Must be between 0 and 12!")
# #   } else {
# #     for (i = 1; i <= n; i++) {
# #       answer = answer * i
# #     }
# #   }
# #   return answer
# # }

# # # BEST JS SOLVE
# # function factorial(n) {
# #   if (n < 0 || n > 12)
# #     throw new RangeError();
# #   return n <= 1 ? 1 : n * factorial(n - 1);
# # }

# print(factorial(13))

# # # FIZZ BUZZ
# # MY SOLVE IS BEST SOLVE!
# def fizzbuzz(n):
#     n_list = []
#     for i in range(1, n + 1):
#         if i % 3 == 0 and i % 5 == 0:
#             n_list.append("FizzBuzz")
#         elif i % 3 == 0:
#             n_list.append("Fizz")
#         elif i % 5 == 0:
#             n_list.append("Buzz")
#         else: 
#             n_list.append(i)
#     return n_list

# # CLEVER SOLVE
# def fizzbuzz(n):
#     return ['Fizz'*(not i%3) + 'Buzz'*(not i%5) or i for i in range(1, n+1)]

# print(fizzbuzz(5))

# # MY JS SOLVE
# const fizzbuzz = (n) => {
#     let nArr = []
#     let fizzArr = []
#     for (i = 1; i <= n; i++) {
#         nArr.push(i)
#     }
#     for (i = 0; i < nArr.length; i++) {
#         if (nArr[i] % 3 === 0 && nArr[i] % 5 === 0) {
#         fizzArr.push("FizzBuzz")
#         } else if (nArr[i] % 3 === 0) {
#         fizzArr.push("Fizz")
#         } else if (nArr[i] % 5 === 0) {
#         fizzArr.push("Buzz")
#         } else {
#         fizzArr.push(nArr[i])
#         }
#     }
#     return fizzArr
# }

# # BEST JS SOLVE
# function fizzbuzz(n) {
#     var i = 1, arr = [];
#     while(i <= n) {
#         var fizz = (i % 3 == 0);
#         var buzz = (i % 5 == 0);
#         if(fizz || buzz) {
#         arr.push((fizz?"Fizz":"") + (buzz?"Buzz":""));
#         }
#         else {
#         arr.push(i);
#         }
#         i++;
#     }
#     return arr;
# }

# var fizzify = fizzbuzz;

# # # LOOKING FOR A BENEFACTOR
# # MY SOLVE
# import math
# def new_avg(arr, newavg):
#     currentSum = 0

#     for i in arr:
#         currentSum += i

#     newDon = newavg * (len(arr) + 1) - currentSum

#     if newDon <= 0:
#         raise ValueError
#     else: 
#         return math.ceil(newDon)

# from math import ceil

# # BEST SOLVE
# def new_avg(arr, newavg):
#     value = int(ceil((len(arr)+1) * newavg - sum(arr)))
#     if value < 0:
#         raise ValueError
    
#     return value

# print(new_avg([14, 30, 5, 7, 9, 11, 15], 30))

# # # MIDDLE ME
# # MY SOLVE
# def middle_me(N, X, Y):
#     y_str = list("".join([Y]*N))
#     y_str.insert(N//2, X)

#     if N % 2 == 1:
#         return X
#     else:
#         return "".join(y_str)

# # BEST SOLVE
# def middle_me(N, X, Y): 
#     if N % 2 == 1: 
#         return X
#     else:
#         return Y * (N//2) + X + Y * (N//2)

# print(middle_me(10, "A", "*"))

# # # LEAP YEARS
# # MY SOLVE
# def isLeapYear(year):
#     if year % 400 == 0: 
#         return True
#     elif year % 100 == 0: 
#         return False
#     elif year % 4 == 0: 
#         return True
#     else: return False

# # BEST SOLVE
# def isLeapYear(year):
#     return (year % 100 != 0 and year % 4 == 0) or year % 400 == 0

# print(isLeapYear(1234))

# # # CLUB DOORMAN
# # MY SOLVE
# import string
# def pass_the_door_man(word): 
#     for i in word:
#         if i == word[word.index(i) + 1]:
#             return (string.ascii_lowercase.index(i) + 1)*3

# # BEST SOLVE
# def pass_the_door_man(word): 
#     for i in word:
#         if i*2 in word:
#             return (ord(i)-96) * 3

# print(pass_the_door_man("lettuce"))

# # # BATTLE OF THE CHARACTERS
# # MY SOLVE
# def battle(x, y):
#     x_list = []
#     y_list = []
#     for i in x:
#         x_list.append(ord(i.lower()) - 96)

#     for i in y:
#         y_list.append(ord(i.lower()) - 96)

#     if sum(x_list) > sum(y_list):
#         return x
#     elif sum(y_list) > sum(x_list):
#         return y
#     else:
#         return "Tie!"

# # BEST SOLVE
# def battle(x, y):
#     d={chr(i):c+1 for c,i in enumerate(range(65,91))}
#     a=sum(d[c] for c in x)
#     b=sum(d[c] for c in y)
#     return 'Tie!' if a==b else [y,x][a>b]

# print(battle("ONE", "NEO"))

# # # WEIGHT OF ITS CONTENTS
# # MY SOLVE
# import re
# import math
# def content_weight(bottle_weight, scale):
#     scale_num = int(re.search("\d+", scale).group())
#     patterns = ["larger", "smaller"]
#     scale_sign = ""

#     for pattern in patterns:
#         if re.search(pattern, scale):
#             scale_sign = pattern

#     if scale_sign == "larger":
#         return math.ceil(scale_num * (bottle_weight / (scale_num + 1)))
#     else:
#         return math.ceil(bottle_weight / (1/scale_num + 1) / scale_num)

# # BEST SOLVE
# def content_weight(bottle_weight, scale): 
#     a, _, c = scale.split(" ")
#     return bottle_weight * int(a) / (int(a) + 1) if c == "larger" else bottle_weight / (int(a) + 1)

# print(content_weight(120, "2 times smaller"))