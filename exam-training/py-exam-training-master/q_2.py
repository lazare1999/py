# ამოცანა 2.
# აირჩიეთ myfunc() ფუნქციის სწორი დეკლარაცია, რათა წარმატებით შევასრულოთ ფუნქციის გამოძახბები:
# myfunc(2, 7, 67)
# myfunc(10, 20)
#
# A. def myfunc(**kwargs)
# B. არა, პითონში ეს შეუძლებელია
# C. Def myfunc(args*)
# D. def myfunc(*data)


def myfunc(*data):
    print(data)


myfunc(2, 7, 67)
myfunc(10, 20)
