# Rubric
Your grade is based on whether you pass the automated tests, listed below.

The tests will ignore spacing, capitalization, and punctuation, but you will fail the tests if you spell something wrong or calculate something incorrectly.



<table border="1" style="width: 100%; text-align: center;">
<thead>
    <tr>
        <th style="text-align: center;">Test</th>
        <th style="text-align: center;">Description</th>
        <th style="text-align: center;">Points</th>
    </tr>
</thead>
<tbody>
    <tr style="text-align: left">
        <td>1. Input Prompts - Exceptions File</td>
        <td>
        <b>Input test cases used:</b> 1-5<br><br>
        Your input prompts must be the same as the expected input prompts of each input test case. 
        <br>
        <br>
        See the <code>descriptions_ot_test_cases</code> folder for expected input prompts for each input test case.
        </td> 
        <td style="text-align: center">10</td>
    </tr>
    <tr style="text-align: left">
        <td>2. Input Prompts - Defensive File</td>
        <td>
        <b>Input test cases used:</b> 1-5<br><br>
        Your input prompts must be the same as the expected input prompts of each input test case. 
        <br>
        <br>
        See the <code>descriptions_ot_test_cases</code> folder for expected input prompts for each input test case.
        </td> 
        <td style="text-align: center">10</td>
    </tr>
    <tr style="text-align: left">
        <td>3. Printed Messages - Exceptions File</td>
        <td>
        <b>Input test cases used:</b> 1-5<br><br>
        Your printed output must be the same as the expected output of each input test case.
        <br>
        <br>
        See the <code>descriptions_of_test_cases</code> folder for expected printed messages for each input test case.       
        </td>
        <td style="text-align: center">10</td>
    </tr>
        <tr style="text-align: left">
        <td>4. Printed Messages - Defensive File</td>
        <td>
        <b>Input test cases used:</b> 1, 2, 4, 6<br><br>
        Your code must store the inputted friend names and hobbies in a dictionary variable, with the friend names as the key and the hobbies as the values. It doesn't matter what you call the variable.
        <br>
        <br>
        See the <code>descriptions_ot_test_cases</code> folder for inputs used in each test case to see what your dictionaries should hold.    
        </td>
        <td style="text-align: center">10</td>
    </tr>
    <tr style="text-align: left">
      <td>5. Value Error Raised - Exceptions File</td>
        <td>
        <b>Input test cases used:</b> 1-5<br><br>
        Your code needs to raise and handle a Value Error on input test cases 3 and 5, and not raise one on cases 1, 2, and 4.  
        </td>
        <td style="text-align: center">15</td>
    </tr>
    <tr style="text-align: left">
    <td>6. Key Error Raised - Exceptions File</td>
        <td>
        <b>Input test cases used:</b> 1-5<br><br>
        Your code needs to raise and handle a Key Error on input test cases 4 and 5, and not raise one on cases 1, 2, and 3.  
        </td>
        <td style="text-align: center">15</td>
    </tr>
    <tr style="text-align: left">
    <td>7. No if statements present - Exceptions File</td>
        <td>
        <b>Input test cases used:</b> None <br><br>
        Your exceptions file shouldn't have any if statements present in it. 
        </td>
        <td style="text-align: center">15</td>
    </tr>
    <tr style="text-align: left">
    <td>8. No try/except statements present - Defensive File</td>
        <td>
        <b>Input test cases used:</b> None <br><br>
        Your defensive file shouldn't have any try/except statements present in it. 
        </td>
        <td style="text-align: center">10</td>
    </tr>
    <tr style="text-align: left">
        <td>9. Sufficient Comments </td>
        <td>
        <b>Input test cases used:</b> None<br><br>
        Your code must include at least <code>10</code> comments. You can use any form of commenting:
        <ul>
          <li><code>#</code></li> 
          <li><code>''' '''</code></li>
          <li><code>""" """</code></li>
        </ul>
        </td>
        <td style="text-align: center">5</td>
    </tr>
    <tr>
        <td colspan="2">Total Points</td>
        <td>100</td>
  </tr>
</tbody>
</table>

## Test Cases
If you fail a test during a specific test case, see the `descriptions_of_test_cases` folder for the following:
<table border="1" style="width: 100%; text-align: left;">
  <tr>
    <th>Test Case</th>
    <th>Description</th>
  </tr>
  <tr>
    <td>Input Test Case 01</td>
    <td>Valid input for dollars and currency</td>
  </tr>
  <tr>
    <td>Input Test Case 02</td>
    <td>Valid inputs for dollar and currency, but with space before and after each input, as well as lowercased currency.</td>
  </tr>
  <tr>
    <td>Input Test Case 03</td>
    <td>Using an improper dollar amount</td>
  </tr>
  <tr>
    <td>Input Test Case 04</td>
    <td>Using an improper currency name</td>
  </tr>
  <tr>
    <td>Input Test Case 05</td>
    <td>Using improper dollar amounts and currency names multiple times</td>
  </tr>
</table>