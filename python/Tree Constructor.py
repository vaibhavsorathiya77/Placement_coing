# Input: ["A-B", "A-C", "B-D"]
# Output: True

# Input: ["A-B", "A-C", "B-D", "B-E", "B-F"]
# Output: False


input =  ["A-B", "A-C", "B-D", "B-E", "B-F"]

parent_count={}
child_count = {}

for s in input:
    parent,child = s.split('-')

    if parent in parent_count:
        parent_count[parent] +=1
    else:
        parent_count[parent] =1
    if child in child_count:
        child_count[child] += 1
    else:
        child_count[child] = 1
    if parent_count[parent]>2 or child_count[child]>1:
        print(False)
        break
else:
    print(True)