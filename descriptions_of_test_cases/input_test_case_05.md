# Test Case 5

## Description
Using improper dollar amounts and currency names multiple times

## Inputs
```
1: "dogecoin"
2: "25"
3: "WUT"
4: "Bucks"
5: "34.7"
6: "USA"
7: "25.5"
8: "GBP"
```

## Expected Input Prompts
```
1: "Enter an amount in US dollars: "
2: "Please enter a target currency (e.g., EUR, GBP): "
```

## Expected Printed Messages
```
1: "dogecoin is not a valid number. Please try again."
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
14: "WUT is not a valid currency. Please try again."
15: "Bucks is not a valid number. Please try again."
16: "USA is not a valid currency. Please try again."
17: "25.50 USD is equal to 20.66 GBP"
```

## Example Output **(combined Inputs, Input Prompts, and Printed Messages)**
```
Enter an amount in US dollars: dogecoin
dogecoin is not a valid number. Please try again.
Enter an amount in US dollars: 25
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

Please enter a target currency (e.g., EUR, GBP): WUT
WUT is not a valid currency. Please try again.
Enter an amount in US dollars: Bucks
Bucks is not a valid number. Please try again.
Enter an amount in US dollars: 34.7
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

Please enter a target currency (e.g., EUR, GBP): USA
USA is not a valid currency. Please try again.
Enter an amount in US dollars: 25.5
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

Please enter a target currency (e.g., EUR, GBP): GBP
25.50 USD is equal to 20.66 GBP
```
