<h1 align = "center">B. Can you solve Arithmatic Expressions?</h1>
<h4 align = "center">time limit per test: 1 second</h4>
<h4 align = "center">memory limit per test: 256 megabytes</h4>
<br>
Can you solve arithmetic expressions with your programming knowledge? Let's find it out. You will be given some arithmetic expressions, and you have to solve them.
<b><h3>Input</h3></b>
The first line will contain a number <b>T</b> (1≤T≤1000) representing the number of test cases. Then for each test case, you will be given an arithmetic expression. Please see the sample input 
below. It is guaranteed that the numbers inside the arithmetic expression will be between <b>1</b> and <b>1000</b>.
<b><h3>Output</h3></b>
For each test case, you have to print the result. Look at the sample output for reference. <br><br>
<b>Important Note:</b> Your answer might contain floating point numbers, and in that case, your answer doesn't have to be exactly equal to the actual answer. For example, if your answer is 
<b>20.250000001</b> and the judge's solution is <b>20.25</b>, your answer will still be considered correct. As long as it is really close to the correct solution, your solution will be considered 
correct. Formally speaking, if your solution is x, and the judge's solution is y, then as long as <b>|x−y|≤10<sup>−6</sup></b>, your solution will be correct. In the above example, your solution 
was <b>20.250000001</b> and the judge's solution was <b>20.25</b>. If you take the difference of these two numbers, they are smaller than 10<sup>−6</sup>. Similarly, if the judge's solution is 
<b>19.0000000000</b> and your solution is <b>19</b>, it is still correct, as the difference is <b>0</b>, which is less than <b>10<sup>−6</sup></b>.
<h3>Example</h3>

<table>
  <tr>
    <th>input</th>
  </tr>
  <tr>
    <td>
<pre>
15
calculate 67 + 41
calculate 85 / 5
calculate 13 - 56
calculate 99 - 95
calculate 3 / 10
calculate 12 * 19
calculate 14 - 6
calculate 3 * 88
calculate 45 * 68
calculate 81 - 0
calculate 77 + 40
calculate 8 * 84
calculate 73 - 22
calculate 85 - 86
calculate 28 * 58
</pre>
    </td>
  </tr>
  <tr>
    <th>output</th>
  </tr>
  <tr>
    <td>
<pre style="color: red;">
108.000000
17.000000
-43.000000
4.000000
0.300000
228.000000
8.000000
264.000000
3060.000000
81.000000
117.000000
672.000000
51.000000
-1.000000
1624.000000
</pre>
    </td>
  </tr>
</table>
