import sys
input = sys.stdin.readline

score = int(input())

print('A' if 90 <= score and score <= 100 else 'B' if 80 <= score else 'C' if 70 <= score else 'D' if 60 <= score else 'F')

# if 90 <= score <= 100:
#     print("A")
# elif 80 <= score < 90:
#     print("B")
# elif 70 <= score < 80:
#     print("C")
# elif 60 <= score < 70:
#     print("D")
# else:
#     print("F")