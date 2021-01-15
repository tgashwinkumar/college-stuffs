# Print all positive numbers in a given range

start = int(input("Enter the start value: "))
end = int(input("Enter the end value: "))
if start <= 0: start = 1
lst = [x for x in range(start, end+1)]
print("The positive numbers in the list are ", lst)