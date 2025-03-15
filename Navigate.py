>>> def navigate_file():
...     try:
...         filename = input("Enter the filename: ")
...         with open(filename, 'r') as file:
...             lines = file.readlines()
...             except FileNotFoundError:
...                 print("Error: File not found.")
...                 return
...
  File "<python-input-0>", line 6
    except FileNotFoundError:
    ^^^^^^
SyntaxError: invalid syntax
>>> num_lines = len(lines)
Traceback (most recent call last):
  File "<python-input-1>", line 1, in <module>
    num_lines = len(lines)
                    ^^^^^
NameError: name 'lines' is not defined
>>> print(f"The file contains {num_lines} lines.")
Traceback (most recent call last):
  File "<python-input-2>", line 1, in <module>
    print(f"The file contains {num_lines} lines.")
                               ^^^^^^^^^
NameError: name 'num_lines' is not defined
>>> while True:
...     try:
...         line_number = int(input("Enter a line number (0 to quit): "))
...         if line_number == 0:
...             print("Exiting program.")
...             break
...              if 1 <= line_number <= num_lines:
...                  print(lines[line_number - 1].strip())
...                  continue
...                  print("Invalid line number. Please enter a number within the valid range.")
...                  except ValueError:
...                      print("Invalid input. Please enter a valid number.")
...
  File "<python-input-3>", line 7
    if 1 <= line_number <= num_lines:
IndentationError: unexpected indent
>>> if __name__ == "__main__":
...     navigate_file()
...
Traceback (most recent call last):
  File "<python-input-4>", line 2, in <module>
    navigate_file()
    ^^^^^^^^^^^^^
NameError: name 'navigate_file' is not defined
>>>
