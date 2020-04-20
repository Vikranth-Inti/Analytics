Pandas Data Series [15 exercises with solution]
1. Write a Python program to create and display a one-dimensional array-like object containing an array of data using Pandas module. Go to the editor
Click me to see the sample solution

2. Write a Python program to convert a Panda module Series to Python list and it's type. Go to the editor
Click me to see the sample solution

3. Write a Python program to add, subtract, multiple and divide two Pandas Series. Go to the editor
Sample Series: [2, 4, 6, 8, 10], [1, 3, 5, 7, 9]
Click me to see the sample solution

4. Write a Python program to get the largest integer smaller or equal to the division of the inputs. Go to the editor 
Sample Series: [2, 4, 6, 8, 10], [1, 3, 5, 7, 9]
Click me to see the sample solution

5. Write a Python program to convert a dictionary to a Pandas series. Go to the editor 
Sample Series: 
Original dictionary:
{'a': 100, 'b': 200, 'c': 300, 'd': 400, 'e': 800}
Converted series:
a 100
b 200
c 300
d 400
e 800
dtype: int64 
Click me to see the sample solution

6. Write a Python program to convert a NumPy array to a Pandas series. Go to the editor 
Sample Series: 
NumPy array:
[10 20 30 40 50]
Converted Pandas series:
0 10
1 20
2 30
3 40
4 50
dtype: int64 
Click me to see the sample solution

7. Write a Python program to change the data type of given a column or a Series. Go to the editor 
Sample Series: 
Original Data Series:
0 100
1 200
2 python
3 300.12
4 400
dtype: object
Change the said data type to numeric:
0 100.00
1 200.00
2 NaN
3 300.12
4 400.00
dtype: float64
Click me to see the sample solution

8. Write a Python Pandas program to convert the first column of a DataFrame as a Series. Go to the editor 
Sample Output: 
Original DataFrame
col1 col2 col3
0 1 4 7
1 2 5 5
2 3 6 8
3 4 9 12
4 7 5 1
5 11 0 11
1st column as a Series:
0 1
1 2
2 3
3 4
4 7
5 11
Name: col1, dtype: int64
<class 'pandas.core.series.Series'>
Click me to see the sample solution

9. Write a Pandas program to convert a given Series to an array. Go to the editor 
Sample Output: 
Original Data Series:
0 100
1 200
2 python
3 300.12
4 400
dtype: object
Series to an array
['100' '200' 'python' '300.12' '400']
Click me to see the sample solution

10. Write a Pandas program to convert Series of lists to one Series. Go to the editor 
Sample Output: 
Original Series of list
0 [Red, Green, White]
1 [Red, Black]
2 [Yellow]
dtype: object
One Series
0 Red
1 Green
2 White
3 Red
4 Black
5 Yellow
dtype: object
Click me to see the sample solution

11. Write a Pandas program to sort a given Series. Go to the editor 
Sample Output: 
Original Data Series: 0 100
1 200
2 python
3 300.12
4 400
dtype: object
0 100
1 200
3 300.12
4 400
2 python
dtype: object
Click me to see the sample solution

12. Write a Pandas program to add some data to an existing Series. Go to the editor 
Sample Output: 
Original Data Series:
0 100
1 200
2 python
3 300.12
4 400
dtype: object
Data Series after adding some data:
0 100
1 200
2 python
3 300.12
4 400
0 500
1 php
dtype: object
Click me to see the sample solution

13. Write a Pandas program to create a subset of a given series based on value and condition. Go to the editor 
Sample Output: 
Original Data Series:
0 0
1 1
2 2
3 3
4 4
5 5
6 6
7 7
8 8
9 9
10 10
dtype: int64
Subset of the above Data Series:
0 0
1 1
2 2
3 3
4 4
5 5
dtype: int64
Click me to see the sample solution

14. Write a Pandas program to change the order of index of a given series. Go to the editor 
Sample Output: 
Original Data Series:
A 1
B 2
C 3
D 4
E 5
dtype: int64
Data Series after changing the order of index:
B 2
A 1
C 3
D 4
E 5
dtype: int64
Click me to see the sample solution

15. Write a Pandas program to create the mean and standard deviation of the data of a given Series. Go to the editor 
Sample Output: 
Original Data Series:
0 1
1 2
2 3
3 4
4 5
5 6
6 7
7 8
8 9
9 5
10 3
dtype: int64
Mean of the said Data Series:
4.81818181818
Standard deviation of the said Data Series:
2.52262489555
Click me to see the sample solution
