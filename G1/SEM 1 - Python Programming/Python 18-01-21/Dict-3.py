from collections import OrderedDict

element = OrderedDict([('a', 1)])
dct = OrderedDict([('b', 2), ('c', 3), ('d', '4')])
print("The original dict is", str(dct))
dct = OrderedDict(list(element.items()) + list(dct.items()))
print("The result dict is", str(dct))