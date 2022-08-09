from tika import parser # pip install tika

raw = parser.from_file('./pdf/3.pdf')
print(raw['content'])