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




