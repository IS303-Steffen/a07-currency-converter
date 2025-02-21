# Test Case 1

## Description
Valid input for dollars and currency

## Inputs
```
1: "100"
2: "MXN"
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
13: "100.00 USD is equal to 1800.00 MXN"
```

## Example Output **(combined Inputs, Input Prompts, and Printed Messages)**
```
Enter an amount in US dollars: 100
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

Please enter a target currency (e.g., EUR, GBP): MXN
100.00 USD is equal to 1800.00 MXN
```
