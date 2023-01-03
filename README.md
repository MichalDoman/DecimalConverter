# DecimalConverter (own project)

___
### How it works:

This app converts any decimal number into an equivalent in any other numeral system. When the script is run, the user
needs to input a number, and a numeral system to which to convert it. The display of the outcome depends on the given
numeral system. For numeral bases lower than 10, it looks the following way:

```
-----------------------------------
 Welcome to the Decimal Converter!
-----------------------------------
*** Type in a decimal (and natural) number to be converted: 100
Choose a natural number (greater than 1) as the base of the numeral system,
to which you want to convert (e.g. '2' for binary): 2

"1 100 100"
```

However, in case that the numeral base is greater than 10, I have changed the display to exclude introducing new
characters or letters for digits greater than 9, therefore, displaying every numeral system is possible. In the example
below, a number 1000 is displayed in a numeral system with a base of 12. The interpretation is as follows: 6 x 12^2 + 11
x 12^1 + 4 x 12^0.

```
*** Type in a decimal (and natural) number to be converted: 1000
Choose a natural number (greater than 1) as the base of the numeral system,
to which you want to convert (e.g. '2' for binary): 12

"06 ; 11 ; 04"
```