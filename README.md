#### Assignment 8
# Currency Converter
You’ll be writing a python program to practice error handling in 2 different ways: exception handling, and defensive programming.

Normally, we don't care about the exact process you write your programs in, but in this case the point of this assignment is to recognize the difference between 2 different styles of error handling. So you're going to write the same program in 2 different ways. You have 2 .py files:
- `a08_currency_converter_exceptions.py`
- `a08_currency_converter_defensive.py`

In the first, you'll use exception handling (using `try` and `except` statements) while in the other you'll use defensive programming (no `try` or `except` allowed, you'll just use if statements instead). Make sure to follow the instructions closely to make sure you get all of the points in the automated tests.

In both files, the user will enter an amount of money in US dollars, and the program will convert that into another currency using the exchange rates provided below. The program should handle any errors caused during entry of the data and accessing the dictionary and continually ask for valid entry until one is provided. 

## Libraries Required:
- none

## Custom Functions Required:
None, but feel free to make any functions you want if you think it'll make your program easier to write.

## Provided Code:
See the starting files for a dictionary that you'll need to reference. If you accidentally delete it, here it is again:
 ```
conversion_rates = { 
  "EUR": 0.93, # Euro 
  "GBP": 0.81, # British Pound 
  "JPY": 133.0, # Japanese Yen 
  "INR": 82.5, # Indian Rupee 
  "AUD": 1.48, # Australian Dollar 
  "CAD": 1.36, # Canadian Dollar 
  "CHF": 0.92, # Swiss Franc 
  "CNY": 7.15, # Chinese Yuan 
  "SEK": 10.5, # Swedish Krona 
  "NZD": 1.62, # New Zealand Dollar 
  "MXN": 18.0, # Mexican Peso 
  } 
```
## Logical Flow (same for both .py files):
Both of your .py files are going to do the same basic logic, which is given below. After this section, descriptions for how each file should perform its error handling are given (for example, what happens if an improper dollar amount or currency is inputted). When first writing out your code, you can just assume that proper inputs will be given until you get to that point in the instructions.

### 1. Get a dollar amount from the user
Ask the user: 
- `Enter an amount in US dollars: `
  - Make sure that the code will work even if they enter extra spaces before or after the dollar currency. For example, `"30.5"` and `"  30.5  "` should both work.
- That amount should be converted to a float datatype.

### 2. Display available currencies
Then the program needs to print out all the currencies available to convert to, like this: 
- `Foreign currencies available for conversion are: `
- `EUR GBP JPY INR AUD CAD CHF CNY SEK NZD MXN`
  - You CANNOT just hardcode that string of currencies. You need to reference the dictionary I give you (e.g. if the dictionary were to ever have another currency added, your code should still work without you changing your print statement).
  - You can print the currency names all on one line or on separate lines, it doesn't matter. But you might find it a fun mini challenge to figure out how to get them to all print out on one line.

### 3. Get a target currency to convert to
Then the program will ask the user: 
- `Please enter a target currency (e.g., EUR, GBP): ` 
  - Make it so that even if the user enters a correctly spelled currency in lowercase or with extra space before or after, it would still work. For example, `"  eur  "` should be the same as `"EUR"`. Input test case 2 specifically will enter a lowercase input with extra spaces before and after, and that should be considered a valid input.

### 4. Convert dollars to the foreign currency
Your program should then convert the amount in US dollars to an amount in whatever currency was entered. 
- Do this by multiplying the amount of US dollars by the exchange rate listed in the provided `conversion_rates` dictionary.
- For example, if they entered `50` for the amount of dollars, and `EUR` for the currency, the converted amount would be: 
    - `50 * 0.93`, or `46.5`

### 5. Display the result
Then the program should print out a message with the original US amount and what it is equal to in the other currency (rounded to the second decimal), like this: 
- `<rounded dollar amount> USD is equal to <rounded foreign amount> <foreign currency abbreviation>`
- For example, `50.00 USD is equal to 46.50 EUR`
  - Depending on the way you round to the second decimal, it may display slightly differently, but the automated tests should work no matter which method you use for rounding.

## Error handling for the `exceptions.py` file

The point of this assignment is to practice properly handling errors. In `a08_currency_converter_exceptions.py` there are 2 specific exceptions that I want you to handle by using try/except. If you do this correctly, there is no need for this file to have any if statements. In fact, one of the automated tests will check that there are no if statements in this file. If you're not sure how to accomplish this without if statements, reach out to the TAs.

### Improper dollar amount
You need to handle a `ValueError` exception, which would occur when trying to convert the amount of US Dollars into a `float`. This error would occur during step 1 of the logical flow. 
- If an invalid value for a float is entered, you should handle the exception and print out: 
    - `<dollar input> is not a valid number. Please try again.` 
        - Note, you may or may not run into trouble including the `<dollar input>` that the user entered in the error message that you print out. Figuring that out is one of the little challenges of this assignment.
    - Then, restart gathering inputs from the start. You should continually ask for a dollar amount until a proper one is provided.

### Improper currency key
You also need to catch a `KeyError` exception, which would occur when trying to access the `conversion_rates` dictionary with an input that doesn’t match a key in the dictionary (during step 3-4 of the logical flow).
- To get a `KeyError`exception to naturally raise, you MUST use code like this:
    - `specific_conversion_rate = conversion_rates[currency]`
      - The individual variable names can be whatever you want, but you must directly access the dictionary using square brackets. You CANNOT use the .get() function to get the conversion rate, like `conversion_rates.get(currency)`. Normally, you could do this any way you want on an assignment, but we want the program to trigger a specific Exception (a `KeyError`) that will only happen if we try to access the dictionary using square brackets. The point of this assignment is to practice using try/except. You will lose points if you use .get() or another way of grabbing the value in the `a08_currency_converter_exceptions.py` file.
- When an invalid value for a currency is entered, you should handle the exception and print out: 
  - `<entered currency variable> is not a valid currency. Please try again.`
    - For example, `BLABLA is not a valid currency. Please try again.`
  - Then, restart gathering inputs from the VERY BEGINNING, meaning ask for a dollar amount again.
    - Please don't write it so that you only ask for a currency again. That is a great idea, but I wrote the automated tests to assume the user would start from the very beginning, so just code it that way even if you'd prefer to do it another way. 


## Error handling for the `defensive.py` file
In `a08_currency_converter_defensive.py` you cannot have and `try`/`except` statements, and no exceptions should be raised. Instead, you should use several if statements to ensure that no errors occur.

### Improper dollar amount
You need to check if the input from the user can be a valid `float` before converting it. Try using the `.isdigit()` function.
- `.isdigit()` works with strings, like `dollar_amount.isdigit()` and returns `True` if the string only has numbers in it. Note, however, that this function doesn't recognize decimal numbers as being digits, so `30.5` would return as `False`. You can get around this by combining it with `.replace()` to get rid of the decimal when checking if it is a digit. For example, `dollar_amount.replace(".", "").isdigit()` will return `True` with a number like `30.5`. The automated tests don't check for negative numbers, but if you want to make it work with negative numbers too, feel free to add that functionality.
- If an invalid value for a float is entered, you should print out: 
    - `<dollar input> is not a valid number. Please try again.`
      - For example, `three bucks is not a valid number. Please try again.`
    - Then, restart gathering inputs from the start. You should continually ask for a dollar amount until a proper one is provided.

### Improper currency key
You also need to ensure that the inputted currency actually exists in the `conversion_rates` dictionary. You might find the dictionary `.get()` function useful. You could also use `in` with an if statement. How you do it is up to you.
- When an invalid value for a currency is entered, you should print out: 
  - `<entered currency variable> is not a valid currency. Please try again.` 
    - For example, `three bucks is not a valid number. Please try again.`
  - Then, restart gathering inputs from the very beginning, meaning ask for a dollar amount again.
    - Please don't write it so that you only ask for a currency again. That is a great idea, but I wrote the automated tests to assume the user would start from the very beginning, so just code it that way even if you'd prefer to do it another way. 

When you finish, run the automated tests to make sure you pass all the tests and get full credit, and then push up your code to your GitHub repository.

## Note for future assignments
For any future assignment that requires you to handle a potential error, you can choose how to handle it according to whichever preference you have, whether that be with a defensive approach, exception handling, or a combination of the two, whichever you prefer.

## Grading Rubric
See the Rubric.md file. Remember to right click and select "Open Preview" to see it formatted so it is readable.

## Example Output
This is an example of proper inputs provided, so no exceptions are thrown:
```
Enter an amount in US dollars: 55.40
Foreign currencies available for conversion are: 
EUR GBP JPY INR AUD CAD CHF CNY SEK NZD MXN 
Please enter a target currency (e.g., EUR, GBP): JPY
55.40 USD is equal to 7368.20 JPY
```

This is an example of catching inputting invalid dollar and currency inputs:
```
Enter an amount in US dollars: invalid dollar
invalid dollar is not a valid number. Please try again.
Enter an amount in US dollars: 100
Foreign currencies available for conversion are: 
EUR GBP JPY INR AUD CAD CHF CNY SEK NZD MXN 
Please enter a target currency (e.g., EUR, GBP): LOL
LOL is not a valid currency. Please try again.
Enter an amount in US dollars: 100
Foreign currencies available for conversion are: 
EUR GBP JPY INR AUD CAD CHF CNY SEK NZD MXN 
Please enter a target currency (e.g., EUR, GBP): CHF
100.00 USD is equal to 92.00 CHF
```
