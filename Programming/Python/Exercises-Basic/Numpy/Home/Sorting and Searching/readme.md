NumPy Sorting and Searching [8 exercises with solution]
[An editor is available at the bottom of the page to write and execute the scripts.]

1. Write a NumPy program to sort a given array of shape 2 along the first axis, last axis and on flattened array. Go to the editor
Expected Output:
Original array:
[[10 40]
[30 20]]
Sort the array along the first axis:
[[10 20]
[30 40]]
Sort the array along the last axis:
[[10 40]
[20 30]]
Sort the flattened array:
[10 20 30 40] 
Click me to see the sample solution

2. Write a NumPy program to create a structured array from given student name, height, class and their data types. Now sort the array on height. Go to the editor 
Sample Output:
Original array:
[(b'James', 5, 48.5 ) (b'Nail', 6, 52.5 ) (b'Paul', 5, 42.1 )
(b'Pit', 5, 40.11)]
Sort by height
[(b'Pit', 5, 40.11) (b'Paul', 5, 42.1 ) (b'James', 5, 48.5 )
(b'Nail', 6, 52.5 )]
Click me to see the sample solution

3. Write a NumPy program to create a structured array from given student name, height, class and their data types. Now sort by class, then height if class are equal. Go to the editor 
Expected Output:
Original array:
[(b'James', 5, 48.5 ) (b'Nail', 6, 52.5 ) (b'Paul', 5, 42.1 ) (b'Pit', 5, 40.11)]
Sort by age, then height if class are equal:
[(b'Pit', 5, 40.11) (b'Paul', 5, 42.1 ) (b'James', 5, 48.5 ) (b'Nail', 6, 52.5 )]
Click me to see the sample solution

4. Write a NumPy program to sort the student id with increasing height of the students from given students id and height. Print the integer indices that describes the sort order by multiple columns and the sorted data. Go to the editor 
Expected Output:
Sorted indices:
[4 0 5 3 6 1 2]
Sorted data:
1682 38.0
1023 40.0
5241 40.0
1671 41.0
4532 42.0
5202 42.0
6230 45.0

Click me to see the sample solution

5. Write a NumPy program to get the indices of the sorted elements of a given array. Go to the editor 
Expected Output:
Original array:
[1023 5202 6230 1671 1682 5241 4532]
Indices of the sorted elements of a given array:
[0 3 4 6 1 5 2]
Click me to see the sample solution

6. Write a NumPy program to sort a given complex array using the real part first, then the imaginary part. Go to the editor 
Note: "busday" default of Monday through Friday being valid days.
Sample Output:
Original array:
[(1+2j), (3-1j), (3-2j), (4-3j), (3+5j)]
Sorted a given complex array using the real part first, then the imaginary part.
[1.+2.j 3.-2.j 3.-1.j 3.+5.j 4.-3.j]
Click me to see the sample solution

7. Write a NumPy program to partition a given array in a specified position and move all the smaller elements values to the left of the partition, and the remaining values to the right, in arbitrary order (based on random choice). Go to the editor 
Sample output:
Original array:
[ 70 50 20 30 -11 60 50 40]
After partitioning on 4 the position:
[-11 30 20 40 50 50 60 70]
Click me to see the sample solution

8. Write a NumPy program to sort the specified number of elements from beginning of a given array. Go to the editor 
Sample output:
Original array:
[0.39536213 0.11779404 0.32612381 0.16327394 0.98837963 0.25510787 0.01398678 0.15188239 0.12057667 0.67278699]
Sorted first 5 elements:
[0.01398678 0.11779404 0.12057667 0.15188239 0.16327394 0.25510787 0.39536213 0.98837963 0.32612381 0.67278699]
Click me to see the sample solution
