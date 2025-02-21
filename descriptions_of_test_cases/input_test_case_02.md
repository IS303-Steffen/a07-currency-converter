# Test Case 2

## Description
Valid inputs for dollar and currency, but with space before and after each input, as well as lowercased currency.

## Inputs
```
1: "  30.5  "
2: " cny "
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
13: "30.50 USD is equal to 218.08 CNY"
```

## Example Output **(combined Inputs, Input Prompts, and Printed Messages)**
```
Enter an amount in US dollars:   30.5  
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

Please enter a target currency (e.g., EUR, GBP):  cny 
30.50 USD is equal to 218.08 CNY
```
