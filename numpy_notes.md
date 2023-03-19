# Arrays are data structures

## Types of Arrays
### 1. scalar : 1D, no other dimension, so no horizontal or vertical orientation
### 2. matrix : 2D e.g. dataframe. Rows are first dimension, Column is second dimension
### 3. tensor : 3D or more 

<br>

## Numpy attributes
### 1. shape
<br>

### 2. dtype
dtype specification can be used during numpy constructor
```python
zero_int_array = np.zeros((3,2),dtype='int32')
```

### 3. type coercsion
If there are multiple data types type coercision will happen during numpy constructor
as np can only have one data type. string dataytpe will have dtype _U32_

In the following code float will get converted to integer
```python
np.array([45.67,True],dtype=np.int8)
```
Alternative way to do type coercision
```python
np.array([9,1.12,True]).astype('<U5')
```

## Numpy functions
### 1. flatten() : 
    convert multi-dimensional array to scalar (i.e.1D)
```python
array=np.array([[1,2],[5,6],[6,6]])
array.flatten() ==> array([1, 2, 5, 6, 6, 6])
```
### 2. reshape():
    change the shape e.g. convert 6 elements from (2,3) to (3,2)
```python
array=np.array([[1,2],[5,6],[6,6]])
array.reshape((1,6))
```
### 3. slicing:
    vector : use [r:c] format
    tensor : use [r:c,r:c] e.g. sudoku_game[3:6,2:4] will select a middle square
            from the overall sudoku 2D tensor

        Create an array of trunk diameters with even row indices from 50 to 100 
        inclusive

            every_other_diameter = tree_census[50:101:2,2]


### 4. sorting:
    np.sort(array,index=0) ; 1: row, 2:column
    sorted_trunk_diameters = np.sort(tree_census[:, 2])

    Cant do descending sort. To sort tensors specify column order:
    np.sort(a, order=['age', 'height'])