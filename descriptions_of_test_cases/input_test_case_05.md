# Test Case 5

## Description
Using improper dollar amounts and currency names multiple times

## Inputs
The inputs below (without the quotes) will be entered one by one each time an `input()` function is found in your code.
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

## Example Output
This is what your terminal should look like if you use the inputs above when running your code.
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
