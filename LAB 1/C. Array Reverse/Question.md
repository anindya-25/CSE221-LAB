<h1 align = "center">C. Array Reverse</h1>
<h4 align = "center">time limit per test: 1 second</h4>
<h4 align = "center">memory limit per test: 256 megabytes</h4>
<br>
You are given an array of N integers. Your task is to reverse the array and print the last K integers from the reversed array.
<b><h3>Input</h3></b>
The first line contains two integers N (1≤N≤10<sup>6</sup>) and K (1≤K≤N) — the number of elements in the array and the value K.<br><br>
The second line contains N integers separated by spaces a<sub>1</sub>,a<sub>2</sub>,a<sub>3</sub>…a<sub>n</sub> (1 ≤ a<sub>i</sub> ≤ 10<sup>6</sup>) — the elements of the array.
<b><h3>Output</h3></b>
Print K space separated integers as described in the statement.
<h3>Example</h3>
<table>
  <tr>
    <th>input</th>
  </tr>
  <tr>
    <td>
<pre>
5 3
5 6 7 8 9
</pre>
    </td>
  </tr>
  <tr>
    <th>output</th>
  </tr>
  <tr>
    <td>
<pre style="color: red;">
7 6 5 
</pre>
    </td>
  </tr>
</table>
<table>
  <tr>
    <th>input</th>
  </tr>
  <tr>
    <td>
<pre>
8 5
20 8 9 3 10 7 100 12
</pre>
    </td>
  </tr>
  <tr>
    <th>output</th>
  </tr>
  <tr>
    <td>
<pre style="color: red;">
10 3 9 8 20
</pre>
    </td>
  </tr>
</table>
