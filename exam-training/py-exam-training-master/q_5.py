# მოცემული გაქვთ რიცხვებისაგან შემდგარი სია (List)
# aList = [10, 20, 30, 40, 50, 60, 70, 80]
# მოიყვანეთ ორი განსხვავებული მაგალითი აღნიშნული სიიდან ბოლო 2 ელემენტის პოვნის.
from itertools import islice


def last_two_1(ls):
    num_elements = 2
    print(ls[-num_elements:])


def last_two_2(ls):
    res = list(islice(reversed(ls), 0, 2))
    res.reverse()
    print(res)


last_two_1([10, 20, 30, 40, 50, 60, 70, 80])
last_two_2([10, 20, 30, 40, 50, 60, 70, 80])
