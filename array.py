
# ASSESSMENT 3.2
# LINEAR DATA STRUCTURE: ARRAY
# LAST NAME: DELA CUESTA

array = []

print("================================")
print("       ARRAY - DELA CUESTA")
print("================================")

# INSERTION
print("\nAdding letters to the array...")

for letter in "DELACUESTA":
    array.append(letter)

print("Array after insertion:", array)

# DELETION
print("\nRemoving letters from the array...")

while len(array) > 0:
    removed = array.pop(0)

    print("\nRemoved letter:", removed)
    print("Remaining array:", array)

print("\nArray is now EMPTY.")
print("================================")
