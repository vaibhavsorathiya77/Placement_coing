# Input: "acc?7??sss?3rr1??????5"
# Output: True

# Input: "aa6?9"
# Output: False
s = "acc?7??sss?3rr1??????5"

question_mark =0
previous_digit = None
found = False

for w in s:
    if w.isdigit():
        digit = int(w)
        if previous_digit is not None:
            if previous_digit + digit ==10:
                if question_mark ==3:
                    found = True
                else:
                    print(False)
                    break
        previous_digit = digit
        question_mark = 0
    elif w == "?":
        question_mark+=1

print(found)