"""
╔══════════════════════════════════════════════════════════════════╗
║ Built-in Python Data Types                                       ║
╟────────────────┬──────────────────────────────┬──────────────────╢
║ Type           │ Identifier                   │ Sample           ║
╟────────────────┼──────────────────────────────┼──────────────────╢
║ Text Type      │ str                          │         "string" ║
║ Numeric Types  │ int                          │                1 ║
║ Numeric Types  │ float                        │             2.34 ║
║ Numeric Types  │ complex                      │               1j ║
║ Sequence Types │ list                         │          [1,2,3] ║
║ Sequence Types │ tuple                        │          (4,5,6) ║
║ Sequence Types │ range                        │         range(5) ║
║ Mapping Type   │ dict                         │  {"a":1, "b": 2} ║
║ Set Types      │ set, frozenset               │        {0,1,2,3} ║
║ Boolean Type   │ bool                         │      True, False ║
║ Binary Types   │ bytes, bytearray, memoryview │                  ║
║ None Type      │ NoneType                     │             None ║
╚════════════════╧══════════════════════════════╧══════════════════╝
"""

string = "string"              # string
integer = 1                    # int
float = 2.3                    # float
complex = 1j                   # complex
list = [1,2,3]                 # list
tuple = (4,5,6)                # tuple
range = range(6)               # range
set = {0,1,2,3}                # set
frozenset = frozenset((1,2,3)) # frozenset
dictionary = {"a": 1, "b": 2}  # dict

print(
    type(string),
    type(integer),
    type(float),
    type(complex),
    type(list),
    type(tuple),
    type(range),
    type(set),
    type(frozenset),
    type(dictionary)
)
