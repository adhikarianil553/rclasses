# numbers = () array
# numbers = [] list 



# inbuilt method (function)


numbers = []

print(numbers)

numbers.append(1)
print(numbers)
numbers.append(3)
print(numbers)

print(min(numbers))
# len(# list ko name pass garney) = lenthght of the list return garxa
# max(number) number bhney list ko maximum
# avg(number) number bhney list ko average 

min = 100
max = 100
sum = 0
count =0 
for n in numbers:
    count = count + 1
    if n<min:
        min = n
    elif max < n:
        max = n
    sum = sum + n

avg = sum / count
print(f'Maximum: {max} ,Min: {min} ,Avg: {avg}')