
Pandas Dataframe
1. Write a Pandas program to get the powers of an array values element-wise.
Note: First array elements raised to powers from second array
Sample data: {'X':[78,85,96,80,86], 'Y':[84,94,89,83,86],'Z':[86,97,96,72,83]}

2. Write a Pandas program to create and display a DataFrame from a specified dictionary data which has the index labels.
Sample Python dictionary data and list labels:
exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
Expected Output:
attempts name qualify score 
a 1 Anastasia yes 12.5 
b 3 Dima no 9.0
.... i 2 Kevin no 8.0 
j 1 Jonas yes 19.0 
Click me to see the sample solution

3. Write a Pandas program to display a summary of the basic information about a specified DataFrame and its data.
Sample Python dictionary data and list labels:
exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
Expected Output:
Summary of the basic information about this DataFrame and its data:
<class 'pandas.core.frame.DataFrame'>
Index: 10 entries, a to j
Data columns (total 4 columns):
.... dtypes: float64(1), int64(1), object(2)
memory usage: 400.0+ bytes
None 


4. Write a Pandas program to get the first 3 rows of a given DataFrame.
Sample Python dictionary data and list labels:
exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
Expected Output:
First three rows of the data frame:
attempts name qualify score 
a 1 Anastasia yes 12.5
b 3 Dima no 9.0 
c 2 Katherine yes 16.5


5. Write a Pandas program to select the 'name' and 'score' columns from the following DataFrame.
Sample Python dictionary data and list labels:
exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
Expected Output:
Select specific columns:
name score 
a Anastasia 12.5 
b Dima 9.0 
c Katherine 16.5
... h Laura NaN 
i Kevin 8.0 
j Jonas 19.0


6. Write a Pandas program to select the specified columns and rows from a given data frame. Go to the editor
Sample Python dictionary data and list labels:
Select 'name' and 'score' columns in rows 1, 3, 5, 6 from the following data frame.
exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
Expected Output:
Select specific columns and rows:
name score 
b Dima 9.0 
d James NaN 
f Michael 20.0 
g Matthew 14.5 
Click me to see the sample solution

7. Write a Pandas program to select the rows where the number of attempts in the examination is greater than 2. Go to the editor
Sample Python dictionary data and list labels:
exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
Expected Output:
Select specific columns and rows:
name score 
b Dima 9.0 
d James NaN 
f Michael 20.0 
Click me to see the sample solution

8. Write a Pandas program to count the number of rows and columns of a DataFrame. Go to the editor
Sample Python dictionary data and list labels:
exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
Expected Output:
Number of Rows: 10 
Number of Columns: 4
Click me to see the sample solution

9. Write a Pandas program to select the rows where the score is missing, i.e. is NaN. Go to the editor
Sample Python dictionary data and list labels:
exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
Expected Output:
Rows where score is missing:
attempts name qualify score
d 3 James no NaN
h 1 Laura no NaN
Click me to see the sample solution

10. Write a Pandas program to select the rows the score is between 15 and 20 (inclusive). Go to the editor
Sample Python dictionary data and list labels:
exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
Expected Output:
Rows where score between 15 and 20 (inclusive):
attempts name qualify score 
c 2 Katherine yes 16.5 
f 3 Michael yes 20.0 
j 1 Jonas yes 19.0 
Click me to see the sample solution

11. Write a Pandas program to select the rows where number of attempts in the examination is less than 2 and score greater than 15. Go to the editor
Sample Python dictionary data and list labels:
exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
Expected Output:
Rows where score between 15 and 20 (inclusive):
attempts name qualify score 
c 2 Katherine yes 16.5 
j 1 Jonas yes 19.0 
Click me to see the sample solution

12. Write a Pandas program to change the score in row 'd' to 11.5. Go to the editor
Sample Python dictionary data and list labels:
exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
Expected Output:
Change the score in row 'd' to 11.5: 
attempts name qualify score
a 1 Anastasia yes 12.5
b 3 Dima no 9.0
c 2 Katherine yes 16.5
... 
i 2 Kevin no 8.0 
j 1 Jonas yes 19.0 
Click me to see the sample solution

13. Write a Pandas program to calculate the sum of the examination attempts by the students. Go to the editor
Sample Python dictionary data and list labels:
exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
Expected Output:
Sum of the examination attempts by the students:
19 
Click me to see the sample solution

14. Write a Pandas program to calculate the mean score for each different student in DataFrame. Go to the editor
Sample Python dictionary data and list labels:
exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
Expected Output:
Mean score for each different student in data frame: 
13.5625 
Click me to see the sample solution

15. Write a Pandas program to append a new row 'k' to data frame with given values for each column. Now delete the new row and return the original DataFrame. Go to the editor
Sample Python dictionary data and list labels:
exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
Values for each column will be:
name : "Suresh", score: 15.5, attempts: 1, qualify: "yes", label: "k"
Expected Output:
Append a new row:
Print all records after insert a new record:
attempts name qualify score
a 1 Anastasia yes 12.5
b 3 Dima no 9.0
......
j 1 Jonas yes 19.0
k 1 Suresh yes 15.5
Delete the new row and display the original rows:
attempts name qualify score
a 1 Anastasia yes 12.5
b 3 Dima no 9.0
........
i 2 Kevin no 8.0
j 1 Jonas yes 19.0 
Click me to see the sample solution

16. Write a Pandas program to sort the DataFrame first by 'name' in descending order, then by 'score' in ascending order. Go to the editor
Sample Python dictionary data and list labels:
exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
Values for each column will be:
name : "Suresh", score: 15.5, attempts: 1, qualify: "yes", label: "k"
Expected Output:
Sort the data frame first by 'name' in descending order, then by 'score' in ascending order: 
attempts name qualify score 
a 1 Anastasia yes 12.5
b 3 Dima no 9.0
..... 
i 2 Kevin no 8.0 
j 1 Jonas yes 19.0 
Click me to see the sample solution

17. Write a Pandas program to replace the 'qualify' column contains the values 'yes' and 'no' with True and False. Go to the editor
Sample Python dictionary data and list labels:
exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
Expected Output:
Replace the 'qualify' column contains the values 'yes' and 'no' with T
rue and False: 
attempts name qualify score 
a 1 Anastasia True 12.5 
b 3 Dima False 9.0 
...... 
i 2 Kevin False 8.0 
j 1 Jonas True 19.0 
Click me to see the sample solution

18. Write a Pandas program to change the name 'James' to 'Suresh' in name column of the DataFrame. Go to the editor
Sample Python dictionary data and list labels:
exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
Expected Output:
Change the name 'James' to \?Suresh\?:
attempts name qualify score
a 1 Anastasia yes 12.5 
b 3 Dima no 9.0
....... 
i 2 Kevin no 8.0
j 1 Jonas yes 19.0
Click me to see the sample solution

19. Write a Pandas program to delete the 'attempts' column from the DataFrame. Go to the editor
Sample Python dictionary data and list labels:
exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
Expected Output:
Delete the 'attempts' column from the data frame: 
name qualify score
a Anastasia yes 12.5 
b Dima no 9.0 
..... 
i Kevin no 8.0
j Jonas yes 19.0 
Click me to see the sample solution

20. Write a Pandas program to insert a new column in existing DataFrame. Go to the editor
Sample Python dictionary data and list labels:
exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
Expected Output:
New DataFrame after inserting the 'color' column 
attempts name qualify score color
a 1 Anastasia yes 12.5 Red
b 3 Dima no 9.0 Blue
....... 
i 2 Kevin no 8.0 Green 
j 1 Jonas yes 19.0 Red
Click me to see the sample solution

21. Write a Pandas program to iterate over rows in a DataFrame. Go to the editor
Sample Python dictionary data and list labels:
exam_data = [{'name':'Anastasia', 'score':12.5}, {'name':'Dima','score':9}, {'name':'Katherine','score':16.5}]
Expected Output:
Anastasia 12.5
Dima 9.0 
Katherine 16.5
Click me to see the sample solution

22. Write a Pandas program to get list from DataFrame column headers. Go to the editor
Sample Python dictionary data and list labels:
exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
Expected Output:
['attempts', 'name', 'qualify', 'score']
Click me to see the sample solution

23. Write a Pandas program to rename columns of a given DataFrame Go to the editor
Sample data:
Original DataFrame
col1 col2 col3
0 1 4 7
1 2 5 8
2 3 6 9
New DataFrame after renaming columns:
Column1 Column2 Column3
0 1 4 7
1 2 5 8
2 3 6 9
Click me to see the sample solution

24. Write a Pandas program to select rows from a given DataFrame based on values in some columns. Go to the editor
Sample data:
Original DataFrame
col1 col2 col3
0 1 4 7
1 4 5 8
2 3 6 9
3 4 7 0
4 5 8 1
Rows for colum1 value == 4
col1 col2 col3
1 4 5 8
3 4 7 0
Click me to see the sample solution

25. Write a Pandas program to change the order of a DataFrame columns. Go to the editor
Sample data:
Original DataFrame
col1 col2 col3
0 1 4 7
1 4 5 8
2 3 6 9
3 4 7 0
4 5 8 1
After altering col1 and col3
col3 col2 col1
0 7 4 1
1 8 5 4
2 9 6 3
3 0 7 4
4 1 8 5
Click me to see the sample solution

26. Write a Pandas program to add one row in an existing DataFrame. Go to the editor
Sample data:
Original DataFrame
col1 col2 col3
0 1 4 7
1 4 5 8
2 3 6 9
3 4 7 0
4 5 8 1
After add one row:
col1 col2 col3
0 1 4 7
1 4 5 8
2 3 6 9
3 4 7 0
4 5 8 1
5 10 11 12
Click me to see the sample solution

27. Write a Pandas program to write a DataFrame to CSV file using tab separator. Go to the editor
Sample data:
Original DataFrame
col1 col2 col3
0 1 4 7
1 4 5 8
2 3 6 9
3 4 7 0
4 5 8 1
Data from new_file.csv file:
col1\tcol2\tcol3
0 1\t4\t7
1 4\t5\t8
2 3\t6\t9
3 4\t7\t0
4 5\t8\t1
Click me to see the sample solution

28. Write a Pandas program to count city wise number of people from a given of data set (city, name of the person). Go to the editor
Sample data:
city Number of people
0 California 4
1 Georgia 2
2 Los Angeles 4 
Click me to see the sample solution

29. Write a Pandas program to delete DataFrame row(s) based on given column value. Go to the editor
Sample data:
Original DataFrame
col1 col2 col3
0 1 4 7
1 4 5 8
2 3 6 9
3 4 7 0
4 5 8 1
New DataFrame
col1 col2 col3
0 1 4 7
2 3 6 9
3 4 7 0
4 5 8 1
Click me to see the sample solution

30. Write a Pandas program to widen output display to see more columns. Go to the editor
Sample data:
Original DataFrame
col1 col2 col3
0 1 4 7
1 4 5 8
2 3 6 9
3 4 7 0
4 5 8 1
Click me to see the sample solution

31. Write a Pandas program to select a row of series/dataframe by given integer index. Go to the editor
Sample data:
Original DataFrame
col1 col2 col3
0 1 4 7
1 4 5 8
2 3 6 9
3 4 7 0
4 5 8 1
Index-2: Details
col1 col2 col3
2 3 6 9
Click me to see the sample solution

32. Write a Pandas program to replace all the NaN values with Zero's in a column of a dataframe. Go to the editor
Sample data:
Original DataFrame
attempts name qualify score
0 1 Anastasia yes 12.5
1 3 Dima no 9.0
2 2 Katherine yes 16.5
3 3 James no NaN
4 2 Emily no 9.0
5 3 Michael yes 20.0
6 1 Matthew yes 14.5
7 1 Laura no NaN
8 2 Kevin no 8.0
9 1 Jonas yes 19.0
New DataFrame replacing all NaN with 0:
attempts name qualify score
0 1 Anastasia yes 12.5
1 3 Dima no 9.0
2 2 Katherine yes 16.5
3 3 James no 0.0
4 2 Emily no 9.0
5 3 Michael yes 20.0
6 1 Matthew yes 14.5
7 1 Laura no 0.0
8 2 Kevin no 8.0
9 1 Jonas yes 19.0
Click me to see the sample solution

33. Write a Pandas program to convert index in a column of the given dataframe. Go to the editor
Sample data:
Original DataFrame
attempts name qualify score
0 1 Anastasia yes 12.5
1 3 Dima no 9.0
2 2 Katherine yes 16.5
3 3 James no NaN
4 2 Emily no 9.0
5 3 Michael yes 20.0
6 1 Matthew yes 14.5
7 1 Laura no NaN
8 2 Kevin no 8.0
9 1 Jonas yes 19.0
After converting index in a column:
index attempts name qualify score
0 0 1 Anastasia yes 12.5
1 1 3 Dima no 9.0
2 2 2 Katherine yes 16.5
3 3 3 James no NaN
4 4 2 Emily no 9.0
5 5 3 Michael yes 20.0
6 6 1 Matthew yes 14.5
7 7 1 Laura no NaN
8 8 2 Kevin no 8.0
9 9 1 Jonas yes 19.0
Hiding index:
index attempts name qualify score
0 1 Anastasia yes 12.5
1 3 Dima no 9.0
2 2 Katherine yes 16.5
3 3 James no NaN
4 2 Emily no 9.0
5 3 Michael yes 20.0
6 1 Matthew yes 14.5
7 1 Laura no NaN
8 2 Kevin no 8.0
9 1 Jonas yes 19.0
Click me to see the sample solution

34. Write a Pandas program to set a given value for particular cell in  DataFrame using index value. Go to the editor
Sample data:
Original DataFrame
attempts name qualify score
0 1 Anastasia yes 12.5
1 3 Dima no 9.0
2 2 Katherine yes 16.5
3 3 James no NaN
4 2 Emily no 9.0
5 3 Michael yes 20.0
6 1 Matthew yes 14.5
7 1 Laura no NaN
8 2 Kevin no 8.0
9 1 Jonas yes 19.0
Set a given value for particular cell in the DataFrame
attempts name qualify score
0 1 Anastasia yes 12.5
1 3 Dima no 9.0
2 2 Katherine yes 16.5
3 3 James no NaN
4 2 Emily no 9.0
5 3 Michael yes 20.0
6 1 Matthew yes 14.5
7 1 Laura no NaN
8 2 Kevin no 10.2
9 1 Jonas yes 19.0
Click me to see the sample solution

35. Write a Pandas program to count the NaN values in one or more columns in DataFrame. Go to the editor
Sample data:
Original DataFrame
attempts name qualify score
0 1 Anastasia yes 12.5
1 3 Dima no 9.0
2 2 Katherine yes 16.5
3 3 James no NaN
4 2 Emily no 9.0
5 3 Michael yes 20.0
6 1 Matthew yes 14.5
7 1 Laura no NaN
8 2 Kevin no 8.0
9 1 Jonas yes 19.0
Number of NaN values in one or more columns:
2
Click me to see the sample solution

36. Write a Pandas program to drop a list of rows from a specified DataFrame. Go to the editor
Sample data:
Original DataFrame
col1 col2 col3
0 1 4 7
1 4 5 8
2 3 6 9
3 4 7 0
4 5 8 1
New DataFrame after removing 2nd & 4th rows:
col1 col2 col3
0 1 4 7
1 4 5 8
3 4 7 0
Click me to see the sample solution

37. Write a Pandas program to reset index in a given DataFrame. Go to the editor
Sample data:
Original DataFrame
attempts name qualify score
0 1 Anastasia yes 12.5
1 3 Dima no 9.0
2 2 Katherine yes 16.5
3 3 James no NaN
4 2 Emily no 9.0
5 3 Michael yes 20.0
6 1 Matthew yes 14.5
7 1 Laura no NaN
8 2 Kevin no 8.0
9 1 Jonas yes 19.0
After removing first and second rows
attempts name qualify score
2 2 Katherine yes 16.5
3 3 James no NaN
4 2 Emily no 9.0
5 3 Michael yes 20.0
6 1 Matthew yes 14.5
7 1 Laura no NaN
8 2 Kevin no 8.0
9 1 Jonas yes 19.0
Reset the Index:
index attempts name qualify score
0 2 2 Katherine yes 16.5
1 3 3 James no NaN
2 4 2 Emily no 9.0
3 5 3 Michael yes 20.0
4 6 1 Matthew yes 14.5
5 7 1 Laura no NaN
6 8 2 Kevin no 8.0
7 9 1 Jonas yes 19.0

Click me to see the sample solution

38. Write a Pandas program to devide a DataFrame in a given ratio.Go to the editor
Sample data:
Original DataFrame:
0 1
0 0.316147 -0.767359
1 -0.813410 -2.522672
2 0.869615 1.194704
3 -0.892915 -0.055133
4 -0.341126 0.518266
5 1.857342 1.361229
6 -0.044353 -1.205002
7 -0.726346 -0.535147
8 -1.350726 0.563117
9 1.051666 -0.441533
70% of the said DataFrame:
0 1
8 -1.350726 0.563117
2 0.869615 1.194704
5 1.857342 1.361229
6 -0.044353 -1.205002
3 -0.892915 -0.055133
1 -0.813410 -2.522672
0 0.316147 -0.767359
30% of the said DataFrame:
0 1
4 -0.341126 0.518266
7 -0.726346 -0.535147
9 1.051666 -0.441533
Click me to see the sample solution

39. Write a Pandas program to combining two series into a DataFrame. Go to the editor
Sample data:
Data Series:
0 100
1 200
2 python
3 300.12
4 400
dtype: object
0 10
1 20
2 php
3 30.12
4 40
dtype: object
New DataFrame combining two series:
0 1
0 100 10
1 200 20
2 python php
3 300.12 30.12
4 400 40
Click me to see the sample solution

40. Write a Pandas program to shuffle a given DataFrame rows. Go to the editor
Sample data:
Original DataFrame:
attempts name qualify score
0 1 Anastasia yes 12.5
1 3 Dima no 9.0
2 2 Katherine yes 16.5
3 3 James no NaN
4 2 Emily no 9.0
5 3 Michael yes 20.0
6 1 Matthew yes 14.5
7 1 Laura no NaN
8 2 Kevin no 8.0
9 1 Jonas yes 19.0
New DataFrame:
attempts name qualify score
5 3 Michael yes 20.0
0 1 Anastasia yes 12.5
9 1 Jonas yes 19.0
6 1 Matthew yes 14.5
7 1 Laura no NaN
1 3 Dima no 9.0
3 3 James no NaN
4 2 Emily no 9.0
8 2 Kevin no 8.0
2 2 Katherine yes 16.5

Click me to see the sample solution

41. Write a Pandas program to convert DataFrame column type from string to datetime.
Go to the editor
Sample data:
String Date:
0 3/11/2000
1 3/12/2000
2 3/13/2000
dtype: object
Original DataFrame (string to datetime):
0
0 2000-03-11
1 2000-03-12
2 2000-03-13
Click me to see the sample solution

42. Write a Pandas program to rename a specific column name in a given DataFrame. Go to the editor
Sample data:
Original DataFrame
col1 col2 col3
0 1 4 7
1 2 5 8
2 3 6 9
New DataFrame after renaming second column:
col1 Column2 col3
0 1 4 7
1 2 5 8
2 3 6 9
Click me to see the sample solution

43. Write a Pandas program to get a list of a specified column of a DataFrame. Go to the editor
Sample data:
Powered by 
Original DataFrame
col1 col2 col3
0 1 4 7
1 2 5 8
2 3 6 9
Col2 of the DataFrame to list:
[4, 5, 6]
Click me to see the sample solution

44. Write a Pandas program to create a DataFrame from a Numpy array and specify the index column and column headers. Go to the editor
Sample Output:
Column1 Column2 Column3
Index1 0 0.0 0.0
Index2 0 0.0 0.0
Index3 0 0.0 0.0
.........
Index12 0 0.0 0.0
Index13 0 0.0 0.0
Index14 0 0.0 0.0
Index15 0 0.0 0.0
Click me to see the sample solution

45. Write a Pandas program to find the row for where the value of a given column is maximum. Go to the editor
Sample Output:
Original DataFrame
col1 col2 col3
0 1 4 7
1 2 5 8
2 3 6 12
3 4 9 1
4 7 5 11
Row where col1 has maximum value:
4
Row where col2 has maximum value:
3
Row where col3 has maximum value:
2
Click me to see the sample solution

46. Write a Pandas program to check whether a given column is present in a DataFrame or not. Go to the editor
Sample data:
Original DataFrame
col1 col2 col3
0 1 4 7
1 2 5 8
2 3 6 12
3 4 9 1
4 7 5 11
Col4 is not present in DataFrame.
Col1 is present in DataFrame.
Click me to see the sample solution

47. Write a Pandas program to get the specified row value of a given DataFrame. Go to the editor
Sample data:
Original DataFrame
col1 col2 col3
0 1 4 7
1 2 5 8
2 3 6 12
3 4 9 1
4 7 5 11
Value of Row
col1 1
col2 4
col3 7
Name: 0, dtype: int64
Value of Row4
col1 4
col2 9
col3 1
Name: 3, dtype: int64
Click me to see the sample solution

48. Write a Pandas program to get the datatypes of columns of a DataFrame. Go to the editor
Sample data:
Original DataFrame:
attempts name qualify score
0 1 Anastasia yes 12.5
1 3 Dima no 9.0
.......
8 2 Kevin no 8.0
9 1 Jonas yes 19.0
Data types of the columns of the said DataFrame:
attempts int64
name object
qualify object
score float64
dtype: object
Click me to see the sample solution

49. Write a Pandas program to append data to an empty DataFrame. Go to the editor
Sample data:
Original DataFrame: After appending some data: col1 col2 0 0 0 1 1 1 2 2 2 
Click me to see the sample solution

50. Write a Pandas program to sort a given DataFrame by two or more columns. Go to the editor
Sample data:
Original DataFrame:
attempts name qualify score
0 1 Anastasia yes 12.5 
1 3 Dima no 9.0
........
8 2 Kevin no 8.0
9 1 Jonas yes 19.0
Sort the above DataFrame on attempts, name:
attempts name qualify score
0 1 Anastasia yes 12.5
9 1 Jonas yes 19.0
7 1 Laura no NaN
6 1 Matthew yes 14.5
4 2 Emily no 9.0
2 2 Katherine yes 16.5
8 2 Kevin no 8.0
1 3 Dima no 9.0
3 3 James no NaN
5 3 Michael yes 20.0
Click me to see the sample solution

51. Write a Pandas program to convert the datatype of a given column (floats to ints). Go to the editor
Sample data:
Original DataFrame:
attempts name qualify score
0 1 Anastasia yes 12.50
1 3 Dima no 9.10
......
8 2 Kevin no 8.80
9 1 Jonas yes 19.13
Data types of the columns of the said DataFrame:
attempts int64
name object
qualify object
score float64
dtype: object
Now change the Data type of 'score' column from float to int:
attempts name qualify score
0 1 Anastasia yes 12
1 3 Dima no 9
2 2 Katherine yes 16
3 3 James no 12
4 2 Emily no 9
5 3 Michael yes 20
6 1 Matthew yes 14
7 1 Laura no 11
8 2 Kevin no 8
9 1 Jonas yes 19
Data types of the columns of the DataFrame now:
attempts int64
name object
qualify object
score int64
dtype: object
Click me to see the sample solution

52. Write a Pandas program to remove infinite values from a given DataFrame. Go to the editor
Sample data:
Original DataFrame:
0
0 1000.000000
1 2000.000000
2 3000.000000
3 -4000.000000
4 inf
5 -inf
Removing infinite values:
0
0 1000.0
1 2000.0
2 3000.0
3 -4000.0
4 NaN
5 NaN
Click me to see the sample solution

53. Write a Pandas program to insert a given column at a specific column index in a DataFrame. Go to the editor
Sample data:
Original DataFrame
col2 col3
0 4 7
1 5 8
2 6 12
3 9 1
4 5 11
New DataFrame
col1 col2 col3
0 1 4 7
1 2 5 8
2 3 6 12
3 4 9 1
4 7 5 11
Click me to see the sample solution

54. Write a Pandas program to convert a given list of lists into a Dataframe. Go to the editor
Sample data:
Original list of lists:
[[2, 4], [1, 3]]
New DataFrame
col1 col2
0 2 4
1 1 3
Click me to see the sample solution

55. Write a Pandas program to group by the first column and get second column as lists in rows. Go to the editor
Sample data:
Original DataFrame
col1 col2
0 C1 1
1 C1 2
2 C2 3
3 C2 3
4 C2 4
5 C3 6
6 C2 5
Group on the col1:
col1
C1 [1, 2]
C2 [3, 3, 4, 5]
C3 [6]
Name: col2, dtype: object
Click me to see the sample solution

56. Write a Pandas program to get column index from column name of a given DataFrame. Go to the editor
Sample Output:
Original DataFrame
col1 col2 col3
0 1 4 7
1 2 5 8
2 3 6 12
3 4 9 1
4 7 5 11
Index of 'col2'
1
Click me to see the sample solution

57. Write a Pandas program to count number of columns of a DataFrame. Go to the editor
Sample Output:
Original DataFrame
col1 col2 col3
0 1 4 7
1 2 5 8
2 3 6 12
3 4 9 1
4 7 5 11
Number of columns:
3
Click me to see the sample solution

58. Write a Pandas program to select all columns, except one given column in a DataFrame. Go to the editor
Sample Output:
Original DataFrame
col1 col2 col3
0 1 4 7
1 2 5 8
2 3 6 12
3 4 9 1
4 7 5 11
All columns except 'col3':
col1 col2
0 1 4
1 2 5
2 3 6
3 4 9
4 7 5
Click me to see the sample solution

59. Write a Pandas program to get first n records of a DataFrame. Go to the editor
Sample Output:
Original DataFrame
col1 col2 col3
0 1 4 7
1 2 5 5
2 3 6 8
3 4 9 12
4 7 5 1
5 11 0 11
First 3 rows of the said DataFrame':
col1 col2 col3
0 1 4 7
1 2 5 5
2 3 6 8
Click me to see the sample solution

60. Write a Pandas program to get last n records of a DataFrame. Go to the editor
Sample Output:
Original DataFrame
col1 col2 col3
0 1 4 7
1 2 5 5
2 3 6 8
3 4 9 12
4 7 5 1
5 11 0 11
Last 3 rows of the said DataFrame':
col1 col2 col3
3 4 9 12
4 7 5 1
5 11 0 11
Click me to see the sample solution

61. Write a Pandas program to get topmost n records within each group of a DataFrame. Go to the editor
Sample Output:
Original DataFrame
col1 col2 col3
0 1 4 7
1 2 5 5
2 3 6 8
3 4 9 12
4 7 5 1
5 11 0 11
topmost n records within each group of a DataFrame:
col1 col2 col3
5 11 0 11
4 7 5 1
3 4 9 12
col1 col2 col3
3 4 9 12
2 3 6 8
1 2 5 5
4 7 5 1
col1 col2 col3
3 4 9 12
5 11 0 11
2 3 6 8
Click me to see the sample solution

62. Write a Pandas program to remove first n rows of a given DataFrame. Go to the editor
Sample Output:
Original DataFrame
col1 col2 col3
0 1 4 7
1 2 5 5
2 3 6 8
3 4 9 12
4 7 5 1
5 11 0 11
After removing first 3 rows of the said DataFrame:
col1 col2 col3
3 4 9 12
4 7 5 1
5 11 0 11
Click me to see the sample solution

63. Write a Pandas program to remove last n rows of a given DataFrame. Go to the editor
Sample Output:
Original DataFrame
col1 col2 col3
0 1 4 7
1 2 5 5
2 3 6 8
3 4 9 12
4 7 5 1
5 11 0 11
After removing last 3 rows of the said DataFrame:
col1 col2 col3
0 1 4 7
1 2 5 5
2 3 6 8
Click me to see the sample solution
