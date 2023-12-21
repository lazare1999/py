# Dictionary
dictionary = {52: "E", 126: "A", 134: "B", 188: "C", 189: "D"}
for key, value in dictionary.items():
    print(key)
    print(value)

# list
l = [1, 3, 5, 7, 9]
# with index
for index, item in enumerate(l):
    print(item, " at index ", index)

# without index
for item in l:
    print(item)
