
>>> filename = input("Enter the input file name: ")
Enter the input file name: encrypt.py
>>> filename = input("Enter the input file name: ")
Enter the input file name: encrypt.py.txt
>>> outfile = input("Enter the output file name: ")
Enter the output file name: decrypt.py.txt
>>> try:
...     with open(filename, 'r') as f, open(outfile, 'w')
...     as w:
...         for line in f:
...             w.write(line)
...             except FileNotFoundError:
...                 print(filename + " does not exists!")
...
  File "<python-input-3>", line 2
    with open(filename, 'r') as f, open(outfile, 'w')
                                                     ^
SyntaxError: expected ':'
>>> print(filename + " does not exists!")
encrypt.py.txt does not exists!
