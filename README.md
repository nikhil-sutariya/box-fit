<h1>Introduction</h1>

<p>You want to send your friend a box with different things. Each thing you put inside the box has such 
parameters as index number, weight and cost.  
The box has a weight limit. Your goal is to determine which things to put into the box so that the total 
weight is less than or equal to the box limit and the total cost is as large as possible.  
You would prefer to send a box which weighs less in case there is more than one box with the same 
price. </p>

<h3>Input sample</h3>
<p>Your API should accept as its only argument a path to a filename. The input file contains several lines. 
Each line is one test case. Each line contains the weight that the box can take (before the colon) and the 
list of items you need to choose.  
Each item is enclosed in parentheses where the 1st number is a item’s index number, the 2nd is its 
weight and the 3rd is its cost.<br><br>
<b>E.g.</b><br>
81 : (1,53.38,€45) (2,88.62,€98) (3,78.48,€3) (4,72.30,€76) (5,30.18,€9) (6,46.34,€48)<br>
8 : (1,15.3,€34)<br>
75 : (1,85.31,€29) (2,14.55,€74) (3,3.98,€16) (4,26.24,€55) (5,63.69,€52) (6,76.25,€75) (7,60.02,€74)<br>
(8,93.18,€35) (9,89.95,€78)<br>
56 : (1,90.72,€13) (2,33.80,€40) (3,43.15,€10) (4,37.97,€16) (5,46.81,€36) (6,48.77,€79) (7,81.80,€45)<br>
(8,19.36,€79) (9,6.76,€64) </p><br>
 
<p><h3>Output sample</h3>
For each set of items that you put into a box provide a new row in the output string (items’ index 
numbers are separated by comma).<br><br>
<b>E.g.</b> <br>
4  <br>
-  <br>
2,7  <br>
8,9<br>
</p>

<h3>Constraints</h3>
<p>You should write a class conceptserve.box.packfit with a static API method named pack.  
This method accepts the absolute path to a test file as a String. The test file will be in UTF-8 format. The 
pack method returns the solution as a String.  
Your method should throw an conceptserve.exception.APIException if incorrect parameters are being 
passed. </p>

<h3>Additional constraints:</h3> 
<p>1. Max weight that a package can take is ≤ 100  <br>
2. There might be up to 15 items you need to choose from  <br>
3. Max weight and cost of an item is ≤ 100  </p><br>
