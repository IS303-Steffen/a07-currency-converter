# Test Case 4

## Description
Using an improper currency name

## Inputs
```
1: "6000"
2: "HELLO"
3: "6000"
4: "INR"
```

## Expected Input Prompts
```
1: "Enter an amount in US dollars: "
2: "Please enter a target currency (e.g., EUR, GBP): "
```

## Expected Printed Messages
```
1: "Foreign currencies available for conversion are: "
2: "EUR"
3: "GBP"
4: "JPY"
5: "INR"
6: "AUD"
7: "CAD"
8: "CHF"
9: "CNY"
10: "SEK"
11: "NZD"
12: "MXN"
13: "HELLO is not a valid currency. Please try again."
14: "6000.00 USD is equal to 495000.00 INR"
```

## Example Output **(combined Inputs, Input Prompts, and Printed Messages)**
```
Enter an amount in US dollars: 6000
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

Please enter a target currency (e.g., EUR, GBP): HELLO
HELLO is not a valid currency. Please try again.
Enter an amount in US dollars: 6000
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

Please enter a target currency (e.g., EUR, GBP): INR
6000.00 USD is equal to 495000.00 INR
```
