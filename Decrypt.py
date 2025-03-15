>>> codedText = input("Enter the coded text: ")
Enter the coded text: Lipps${svph%
>>> distanceValue = int(input("Enter the distance value: "))
Enter the distance value: 4
>>> result = ""
>>> for ch in codedText:
...     result += chr(ord(ch)-distanceValue)
...
>>> print("" + result)
Hello world!
>>> print("" + result)
Hello world!
>>>
