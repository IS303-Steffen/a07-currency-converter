# Test Case 3

## Description
Using an improper dollar amount

## Inputs
```
1: "2 dollars"
2: "2"
3: "JPY"
```

## Expected Input Prompts
```
1: "Enter an amount in US dollars: "
2: "Please enter a target currency (e.g., EUR, GBP): "
```

## Expected Printed Messages
```
1: "2 dollars is not a valid number. Please try again."
2: "Foreign currencies available for conversion are: "
3: "EUR"
4: "GBP"
5: "JPY"
6: "INR"
7: "AUD"
8: "CAD"
9: "CHF"
10: "CNY"
11: "SEK"
12: "NZD"
13: "MXN"
14: "2.00 USD is equal to 266.00 JPY"
```

## Example Output **(combined Inputs, Input Prompts, and Printed Messages)**
```
Enter an amount in US dollars: 2 dollars
2 dollars is not a valid number. Please try again.
Enter an amount in US dollars: 2
Foreign currencies available for conversion are: 
EUR
GBP
JPY
INR
AUD
CAD
CHF
CNY
SEK
NZD
MXN

Please enter a target currency (e.g., EUR, GBP): JPY
2.00 USD is equal to 266.00 JPY
```
