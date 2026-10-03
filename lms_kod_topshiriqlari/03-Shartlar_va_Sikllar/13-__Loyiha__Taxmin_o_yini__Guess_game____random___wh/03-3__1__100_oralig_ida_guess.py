# Yashirin son = 42
# Kiritilgan son kichik bo‘lsa "Low", katta bo‘lsa "High", teng bo‘lsa "Correct".
import sys
for line in sys.stdin:
    n = int(line)
    print("High" if n > 42 else "Low" if n < 42 else "Correct")
    if n == 42:
        break