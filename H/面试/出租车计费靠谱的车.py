import sys

line = sys.stdin.readline().strip()
correct = 0
for c in line:
    digit = int(c)
    if digit > 4:
        digit -= 1
    correct = correct * 9 + digit
print(correct)
