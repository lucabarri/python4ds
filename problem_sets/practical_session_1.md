# Practical Session 1

## Problem 1

### Problem 1.1

Write a program that,

1. Use a variable to represent a person's name,
2. Prints out a message in the following format: "Hello PERSON NAME, would you like to learn Python today?"

### Problem 1.2

Based on you last program, write a program that accepts a person's name as an input. Store the input in a variable and then print "Hello PERSON NAME, would you like to learn Python today?".

## Problem 2

### Problem 1.1

Google up a quotation you like. Write a program that prints the quotation from an author in the following template,

> Albert Camus once said, "One must image Sisyphus happy"

In this case, the author is "Albert Camus", and the quotation is "One must imagine Sisyphus happy".

### Problem 1.2

Repeat the previous exercise, while storing your author of choice in an variable called ```author```, and the quotation in a variable called ```quote```.

### Problem 1.3

Repeat the previous exercise, while receiving the author and quotation from an user.

### Problem 1.4

Repeat the previous exercise. After you receive the author and quotation, you should write the quotation into a file named "author.txt"

## Problem 3

Write a program that,

1. Read the file pi.txt in the folder "data".
2. The content of pi.txt should be stored in a variable called "pi".
3. Receives the birthday of someone on the format ddmmyy.
4. If this person's birthday is contained in the digits of the number pi, you should print "Congratulations, your birthday is in the digits of the number pi".
5. Otherwise, you should print "I am sorry, but your birthday is not contained on the digits of the number pi".

## Problem 4

### Problem 4.1

Write a program that has four variables,

1. The first variable, called ```val1``` stores a numeric value of your choice,
2. The second variable, called ```val2``` stores another numeric value of your choice.
3. The third variable, called ```selected_op```,  stores a string. This string is either ```"add"```, ```"multiply"```, ```"divide"``` or ```"subtract"```.
4. Then, your program checks which ```selected_op``` was chosen, and performs the selected operation.
5. The result should be stored in a fourth variable, called ```result```

Don't forget to print your result!

Here's an example of execution of your program:

```
var1 = 5
var2 = 8
selected_op = "add"

OUTPUT: result = 13
```

### Problem 4.2

Based on your last program, receive ```val1```, ```val2``` and ```selected_op``` from an user.

### Problem 4.3

Based on your last program, receive ```val1```, ```val2``` and ```selected_op``` from an user. Write the performed operation in a file called ```myoperation.txt``` in a mathematical form. For instance,

```
INPUT
val1 = 5
val2 = 8
selected_op = +

OUTPUT (on myoperation.txt)
5 + 8 = 13
```

### Problem 4.4

Think about what can go wrong in your program (which types of exceptions may be raised?). Implement a secure program that, whenever an user inputs invalid values or operations, the result in ```myoperation.txt``` indicates what happened.

```
INPUT
val1 = 5
val2 = 0
selected_op = /

OUTPUT (on myoperation.txt)
ERROR: Tried to divide by 0 (5 / 0), which is an invalid operation.
```