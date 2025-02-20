#### Assignment 8
# Currency Converter
You’ll be writing a python program to practice error handling in 2 different ways: exception handling, and defensive programming. Normally, we don't care about the exact process you write your programs in, but in this case the point of this assignment is to recognize the difference between 2 different styles of error handling. So you're going to write the same program in 2 different ways. You have 2 .py files: `a08_currency_converter_exceptions.py` and `a08_currency_converter_defensive.py`. In the first, you'll use exception handling (using `try` and `except` statements) while in the other you'll use defensive programming (no `try` or `except` allowed, you'll just use if statements instead). Make sure to follow the instructions closely to make sure you get all of the points in the automated tests.

In both files, the user will enter an amount of money in US dollars, and the program will convert that into another currency using the exchange rates provided below. The program should handle any errors caused during entry of the data and accessing the dictionary and continually ask for valid entry until one is provided. 

## Libraries Required:
- none

## Custom Functions Required:
- None, but feel free to make any functions you want if you think it makes your program easier to write.

## Provided Code:
- See the starting files for a dictionary that you'll need to reference. If you accidentally delete it, here it is again:
    - ```
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

## Error Handling for `a08_currency_converter_exceptions.py`

The point of this assignment is to practice properly handling errors. In `a08_currency_converter_exceptions.py` there are 2 specific exceptions that I want you to handle by using try/except. If you do this correctly, there is no need for this file to have any if statements. In fact, one of the automated tests will check that there are no if statements in this file. If you're not sure how to accomplish this without if statements, reach out to the TAs.

### Improper dollar amount
You need to handle a `ValueError` exception, which would occur when trying to convert the amount of US Dollars into a `float`. This error would occur during step 1 of the logical flow. 
- If an invalid value for a float is entered, you should handle the exception and print out: 
    - `<dollar input> is not a valid number. Please try again.` 
        - Note, you may or may not run into trouble including the `<dollar input>` that the user entered in the error message that you print out. Figuring that out is one of the little challenges of this assignment.
    - Then, restart gathering inputs from the start. You should continually ask for a dollar amount until a proper one is provided.

### Improper currency key
You also need to catch a `KeyError` exception, which would occur when trying to access the `conversion_rates` dictionary with an input that doesn’t match a key in the dictionary (during step 3-4 of the logical flow). That means that when you
- To get a `KeyError`exception to naturally raise, you MUST use code like this:
    - `specific_conversion_rate = conversion_rates[currency]`
      - The individual variable names can be whatever you want, but you must directly access the dictionary using square brackets. You CANNOT use the .get() function to get the conversion rate, like `conversion_rates.get(currency)`. Normally, you could do this any way you want on an assignment, but we want the program to trigger a specific Exception (a `KeyError`) that will only happen if we try to access the dictionary using square brackets. The point of this assignment is to practice using try/except. You will lose points if you use .get() or another way of grabbing the value in the `a08_currency_converter_exceptions.py` file.
- When an invalid value for a currency is entered, you should handle the exception and print out: 
  - `<entered currency variable> is not a valid currency. Please try again.`
    - For example, `BLABLA is not a valid currency. Please try again.`
  - Then, restart gathering inputs from the VERY BEGINNING, meaning ask for a dollar amount again.
    - Please don't write it so that you only ask for a currency again. That is a great idea, but I wrote the automated tests to assume the user would start from the very beginning, so just code it that way even if you'd prefer to do it another way. 


## Error Handling for `a08_currency_converter_defensive.py`
In `a08_currency_converter_defensive.py` you cannot have and `try`/`except` statements, and no exceptions should be raised. Instead, you should use several if statements to ensure the no errors occur

### Improper dollar amount
You need to check if the input from the user can be a valid `float` before converting it. Try using the `.isdigit()` function.
- `.isdigit()` works with strings, like `dollar_amount.isdigit()` and returns `True` if the string only has numbers in it. Note, however, that this function doesn't recognize decimal numbers as being digits, so `30.5` would return as `False`. You can get around this by combining it with `.replace()` to get rid of the decimal when checking if it is a digit. For example, `dollar_amount.replace(".", "").isdigit()` will return `True` with a number like `30.5`. The automated tests don't check for negative numbers, but if you want to make it work with negative numbers, feel free to try.
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

## Example Output
This is an example of proper inputs provided, so no exceptions are thrown:


This is an example of catching both a ValueError and KeyError exception:


## Rubric
This assignment contains the automated tests listed below. The tests will ignore spacing, capitalization, and punctuation, but you will fail the tests if you spell something wrong or calculate something incorrectly.

After this table, see the Test Cases table below to see what inputs will be run for each of the tests below. To receive points for a test, the test must pass each of the individual test cases.

<table border="1" style="width: 100%; text-align: center;">
<thead style="text-align: center;">
    <tr>
        <th style="text-align: center;">Test</th>
        <th style="text-align: center;">Test Cases Used </th>
        <th style="text-align: center;">Description</th>
        <th style="text-align: center;">Points</th>
    </tr>
</thead>
<tbody>
        <tr style="text-align: left">
        <td>1. Input Prompts</td>
        <td>1-4</td>
        <td>All the these tests are expecting 2 <code>input()</code> prompts to be present in your code (that may be called multiple times depending on what the user inputs). You must use <code>input()</code> to ask the user the following prompts, depending on the input the user provides:
        <ul>
          <li><code>Enter an amount in US dollars:  </code></li>
          <li><code>Please enter a target currency (e.g., EUR, GBP): </code></li>
        </ul>
        </td>
        <td>10</td>
    </tr>
        <tr>
    <tr style="text-align: left">
        <td>2. Printed Messages</td>
        <td>1-4</td>
        <td>Your printed output must contain these phrases, but order doesn't matter. Some test cases won't produce all of these printed messages, so just check the test cases table below this if you fail during a specific test case. You will not be docked if you print out any extra statements not included here:
          <ul>
            <li><code>Foreign currencies available for conversion are:</code></li>
            <li><code>&lt;dollar amount, rounded to 2nd decimal&gt; USD is equal to &lt;foreign currency amount, rounded to 2nd decimal&gt; &lt;foreign currency abbreviation&gt;</code></li>
            <li><code>AUD</code></li>
            <li><code>CAD</code></li>
            <li><code>CHF</code></li>
            <li><code>CNY</code></li>
            <li><code>EUR</code></li>
            <li><code>GBP</code></li>
            <li><code>INR</code></li>
            <li><code>JPY</code></li>
            <li><code>MXN</code></li>
            <li><code>NZD</code></li>
            <li><code>SEK</code></li>
            <li><code>"&lt;invalid dollar amount&gt;" is not a valid number. Please try again.</code></li>
            <li><code>"&lt;invalid currency input&gt;" is not a valid currency. Please try again.</code></li>
          </ul>        
        </td>
        <td>20</td>
    </tr>
    <tr>
        <td>3. Value Error Raised</td>
        <td>1-4</td>
        <td style="text-align: left">
            Test cases 2 & 4 should raise and handle a ValueError (since they provide an invalid dollar amount) and test cases 1 & 3 should NOT raise a ValueError (since they provide a valid dollar amount).
        </td>
        <td>25</td>
    </tr>
    <tr>
        <td>4. Key Error Raised</td>
        <td>1-4</td>
        <td style="text-align: left">
            Test cases 3 & 4 should raise and handle a KeyError (since they provide an invalid currency abbreviation) and test cases 1 & 2 should NOT raise a KeyError (since they provide a valid currency abbreviation).
        </td>
        <td>25</td>
    </tr>
    <tr>
        <td>5. General Exception Handler Present</td>
        <td>None</td>
        <td style="text-align: left">Your code must include at a general exception handler, meaning:
        <ul>
          <li><code>except Exception</code></li>
        </ul>
        </td>
        <td>15</td>
    </tr>
        <tr>
        <td>6. Sufficient Comments</td>
        <td>None</td>
        <td style="text-align: left">Your code must include at least <code>7</code> comments. You can use any form of commenting:
        <ul>
          <li><code>#</code></li> 
          <li><code>''' '''</code></li>
          <li><code>""" """</code></li>
        </ul>
        </td>
        <td>5</td>
    </tr>
    <tr>
        <td colspan="3">Total Points</td>
        <td>100</td>
  </tr>
</tbody>
</table>

<br><br>

## Test Cases Summary
<table>
  <tr>
    <th>Test Case Description</th>
    <th>Inputs</th>
  </tr>
  <tr>
    <td><a href="#testcase1">1: Correct amount, correct currency</a></td>
    <td><ul>
  <li><code>100</code></li>
  <li><code> mxn  </code> (with extra spaces and lowercased)</li>
</ul></td>
  </tr>
  <tr>
    <td><a href="#testcase2">2: Invalid dollar amounts, valid currency</a></td>
    <td><ul>
  <li><code>bla bla</code></li>
  <li><code>lol wut</code></li>
  <li><code>250</code></li>
  <li><code>EUR</code></li>
</ul></td>
  </tr>
  <tr>
    <td><a href="#testcase3">3: Valid dollar amount, invalid currency</a></td>
    <td><ul>
  <li><code>515</code></li>
  <li><code>LOL</code></li>
  <li><code>ROFL</code></li>
  <li><code>GBP</code></li>
</ul></td>
  </tr>
  <tr>
    <td><a href="#testcase4">4: Invalid dollar amount, invalid currency</a></td>
    <td><ul>
  <li><code>make that bag</code></li>
  <li><code>3000</code></li>
  <li><code>idk</code></li>
  <li><code>AUD</code></li>
</ul></td>
  </tr>
</table>

<h3 id="testcase1">Test Case 1 Details - Correct amount, correct currency</h3>

<table>
  <tr>
    <th>Requirement</th>
    <th>Components</th>
  </tr>
  <tr>
    <td>Inputs</td>
    <td><ul>
  <li><code>100</code></li>
  <li><code>MXN</code></li>
</ul></td>
  </tr>
  <tr>
    <td>Input Prompts</td>
    <td><ul>
  <li><code>Enter an amount in US dollars:</code></li>
  <li><code>Please enter a target currency (e.g., EUR, GBP):</code></li>
</ul></td>
  </tr>
  <tr>
    <td>Invalid Input Prompts</td>
    <td></td>
  </tr>
  <tr>
    <td>Printed Messages</td>
    <td><ul>
  <li><code>Foreign currencies available for conversion are:</code></li>
  <li><code>EUR</code></li>
  <li><code>GBP</code></li>
  <li><code>JPY</code></li>
  <li><code>INR</code></li>
  <li><code>AUD</code></li>
  <li><code>CAD</code></li>
  <li><code>CHF</code></li>
  <li><code>CNY</code></li>
  <li><code>SEK</code></li>
  <li><code>NZD</code></li>
  <li><code>MXN</code></li>
  <li><code>100.00 USD is equal to 1800.00 MXN</code></li>
</ul></td>
  </tr>
  <tr>
    <td>Invalid Printed Messages</td>
    <td><ul>
  <li><code>"IDK" is not a valid currency. Please try again.</code></li>
  <li><code>3000.00 USD is equal to 4440.00 AUD</code></li>
  <li><code>"ROFL" is not a valid currency. Please try again.</code></li>
  <li><code>"LOL" is not a valid currency. Please try again.</code></li>
  <li><code>"bla bla" is not a valid number. Please try again.</code></li>
  <li><code>"lol wut" is not a valid number. Please try again.</code></li>
  <li><code>515.00 USD is equal to 417.15 GBP</code></li>
  <li><code>"make that bag" is not a valid number. Please try again.</code></li>
  <li><code>250.00 USD is equal to 232.50 EUR</code></li>
</ul></td>
  </tr>
</table>

<h4>Example Ouput:</h4>

```
Enter an amount in US dollars: 100
Foreign currencies available for conversion are:
EUR GBP JPY INR AUD CAD CHF CNY SEK NZD MXN

Please enter a target currency (e.g., EUR, GBP):  mxn 
100.00 USD is equal to 1800.00 MXN
```

<h3 id="testcase2">Test Case 2 Details - Invalid dollar amounts, valid currency</h3>

<table>
  <tr>
    <th>Requirement</th>
    <th>Components</th>
  </tr>
  <tr>
    <td>Inputs</td>
    <td><ul>
  <li><code>bla bla</code></li>
  <li><code>lol wut</code></li>
  <li><code>250</code></li>
  <li><code>EUR</code></li>
</ul></td>
  </tr>
  <tr>
    <td>Input Prompts</td>
    <td><ul>
  <li><code>Enter an amount in US dollars:</code></li>
  <li><code>Please enter a target currency (e.g., EUR, GBP):</code></li>
</ul></td>
  </tr>
  <tr>
    <td>Invalid Input Prompts</td>
    <td></td>
  </tr>
  <tr>
    <td>Printed Messages</td>
    <td><ul>
  <li><code>"bla bla" is not a valid number. Please try again.</code></li>
  <li><code>"lol wut" is not a valid number. Please try again.</code></li>
  <li><code>Foreign currencies available for conversion are:</code></li>
  <li><code>EUR</code></li>
  <li><code>GBP</code></li>
  <li><code>JPY</code></li>
  <li><code>INR</code></li>
  <li><code>AUD</code></li>
  <li><code>CAD</code></li>
  <li><code>CHF</code></li>
  <li><code>CNY</code></li>
  <li><code>SEK</code></li>
  <li><code>NZD</code></li>
  <li><code>MXN</code></li>
  <li><code>250.00 USD is equal to 232.50 EUR</code></li>
</ul></td>
  </tr>
  <tr>
    <td>Invalid Printed Messages</td>
    <td><ul>
  <li><code>"IDK" is not a valid currency. Please try again.</code></li>
  <li><code>3000.00 USD is equal to 4440.00 AUD</code></li>
  <li><code>"ROFL" is not a valid currency. Please try again.</code></li>
  <li><code>100.00 USD is equal to 1800.00 MXN</code></li>
  <li><code>515.00 USD is equal to 417.15 GBP</code></li>
  <li><code>"make that bag" is not a valid number. Please try again.</code></li>
  <li><code>"LOL" is not a valid currency. Please try again.</code></li>
</ul></td>
  </tr>
</table>

<h4>Example Ouput:</h4>

```
Enter an amount in US dollars: bla bla

"bla bla" is not a valid number. Please try again.

Enter an amount in US dollars: lol wut

"lol wut" is not a valid number. Please try again.

Enter an amount in US dollars: 250
Foreign currencies available for conversion are:
EUR GBP JPY INR AUD CAD CHF CNY SEK NZD MXN

Please enter a target currency (e.g., EUR, GBP): EUR
250.00 USD is equal to 232.50 EUR
```

<h3 id="testcase3">Test Case 3 Details - Valid dollar amount, invalid currency</h3>

<table>
  <tr>
    <th>Requirement</th>
    <th>Components</th>
  </tr>
  <tr>
    <td>Inputs</td>
    <td><ul>
  <li><code>515</code></li>
  <li><code>LOL</code></li>
  <li><code>ROFL</code></li>
  <li><code>GBP</code></li>
</ul></td>
  </tr>
  <tr>
    <td>Input Prompts</td>
    <td><ul>
  <li><code>Enter an amount in US dollars:</code></li>
  <li><code>Please enter a target currency (e.g., EUR, GBP):</code></li>
</ul></td>
  </tr>
  <tr>
    <td>Invalid Input Prompts</td>
    <td></td>
  </tr>
  <tr>
    <td>Printed Messages</td>
    <td><ul>
  <li><code>Foreign currencies available for conversion are:</code></li>
  <li><code>EUR</code></li>
  <li><code>GBP</code></li>
  <li><code>JPY</code></li>
  <li><code>INR</code></li>
  <li><code>AUD</code></li>
  <li><code>CAD</code></li>
  <li><code>CHF</code></li>
  <li><code>CNY</code></li>
  <li><code>SEK</code></li>
  <li><code>NZD</code></li>
  <li><code>MXN</code></li>
  <li><code>"LOL" is not a valid currency. Please try again.</code></li>
  <li><code>"ROFL" is not a valid currency. Please try again.</code></li>
  <li><code>515.00 USD is equal to 417.15 GBP</code></li>
</ul></td>
  </tr>
  <tr>
    <td>Invalid Printed Messages</td>
    <td><ul>
  <li><code>"IDK" is not a valid currency. Please try again.</code></li>
  <li><code>3000.00 USD is equal to 4440.00 AUD</code></li>
  <li><code>100.00 USD is equal to 1800.00 MXN</code></li>
  <li><code>"bla bla" is not a valid number. Please try again.</code></li>
  <li><code>"lol wut" is not a valid number. Please try again.</code></li>
  <li><code>"make that bag" is not a valid number. Please try again.</code></li>
  <li><code>250.00 USD is equal to 232.50 EUR</code></li>
</ul></td>
  </tr>
</table>

<h4>Example Ouput:</h4>

```
Enter an amount in US dollars: 515
Foreign currencies available for conversion are:
EUR GBP JPY INR AUD CAD CHF CNY SEK NZD MXN

Please enter a target currency (e.g., EUR, GBP): LOL

"LOL" is not a valid currency. Please try again.

Foreign currencies available for conversion are:
EUR GBP JPY INR AUD CAD CHF CNY SEK NZD MXN

Please enter a target currency (e.g., EUR, GBP): ROFL

"ROFL" is not a valid currency. Please try again.

Foreign currencies available for conversion are:
EUR GBP JPY INR AUD CAD CHF CNY SEK NZD MXN

Please enter a target currency (e.g., EUR, GBP): GBP
515.00 USD is equal to 417.15 GBP
```

<h3 id="testcase4">Test Case 4 Details - Invalid dollar amount, invalid currency</h3>

<table>
  <tr>
    <th>Requirement</th>
    <th>Components</th>
  </tr>
  <tr>
    <td>Inputs</td>
    <td><ul>
  <li><code>make that bag</code></li>
  <li><code>3000</code></li>
  <li><code>idk</code></li>
  <li><code>AUD</code></li>
</ul></td>
  </tr>
  <tr>
    <td>Input Prompts</td>
    <td><ul>
  <li><code>Enter an amount in US dollars:</code></li>
  <li><code>Please enter a target currency (e.g., EUR, GBP):</code></li>
</ul></td>
  </tr>
  <tr>
    <td>Invalid Input Prompts</td>
    <td></td>
  </tr>
  <tr>
    <td>Printed Messages</td>
    <td><ul>
  <li><code>"make that bag" is not a valid number. Please try again.</code></li>
  <li><code>Foreign currencies available for conversion are:</code></li>
  <li><code>EUR</code></li>
  <li><code>GBP</code></li>
  <li><code>JPY</code></li>
  <li><code>INR</code></li>
  <li><code>AUD</code></li>
  <li><code>CAD</code></li>
  <li><code>CHF</code></li>
  <li><code>CNY</code></li>
  <li><code>SEK</code></li>
  <li><code>NZD</code></li>
  <li><code>MXN</code></li>
  <li><code>"IDK" is not a valid currency. Please try again.</code></li>
  <li><code>3000.00 USD is equal to 4440.00 AUD</code></li>
</ul></td>
  </tr>
  <tr>
    <td>Invalid Printed Messages</td>
    <td><ul>
  <li><code>"ROFL" is not a valid currency. Please try again.</code></li>
  <li><code>100.00 USD is equal to 1800.00 MXN</code></li>
  <li><code>"bla bla" is not a valid number. Please try again.</code></li>
  <li><code>"lol wut" is not a valid number. Please try again.</code></li>
  <li><code>515.00 USD is equal to 417.15 GBP</code></li>
  <li><code>"LOL" is not a valid currency. Please try again.</code></li>
  <li><code>250.00 USD is equal to 232.50 EUR</code></li>
</ul></td>
  </tr>
</table>

<h4>Example Ouput:</h4>

```
Enter an amount in US dollars: make that bag

"make that bag" is not a valid number. Please try again.

Enter an amount in US dollars: 3000
Foreign currencies available for conversion are:
EUR GBP JPY INR AUD CAD CHF CNY SEK NZD MXN

Please enter a target currency (e.g., EUR, GBP): idk

"IDK" is not a valid currency. Please try again.

Foreign currencies available for conversion are:
EUR GBP JPY INR AUD CAD CHF CNY SEK NZD MXN

Please enter a target currency (e.g., EUR, GBP): AUD
3000.00 USD is equal to 4440.00 AUD
```

