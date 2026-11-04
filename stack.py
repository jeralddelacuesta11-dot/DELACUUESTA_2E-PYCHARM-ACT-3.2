
# ASSESSMENT 3.2
# LINEAR DATA STRUCTURE: STACK
# LAST NAME: DELA CUESTA

stack = []

print("================================")
print("       STACK - DELA CUESTA")
print("================================")

# INSERTION (PUSH)
print("\nAdding letters to the stack...")

for letter in "DELACUESTA":
    stack.append(letter)

print("Stack after insertion:", stack)
print("TOP:", stack[-1])

# DELETION (POP)
print("\nRemoving letters from the stack...")

while len(stack) > 0:
    removed = stack.pop()

    print("\nPopped letter:", removed)
    print("Remaining stack:", stack)

    if len(stack) > 0:
        print("TOP:", stack[-1])
    else:
        print("TOP: EMPTY")

print("\nStack is now EMPTY.")
print("================================")
