# Pandas

![[Pasted image 20260226123548.png]]
Pandas id fundamental high-level building block for data analysis.
## Library Highlights
- A fast and efficient **DataFrame** object for data manipulation with integrated indexing
- Tools for **reading and writing data** between in-memory data structures and different formats: CSV and text files, Microsoft Excel, SQL databases, and the fast HDF5 format
- - Intelligent **data alignment** and integrated handling of **missing data**: gain automatic label-based alignment in computations and easily manipulate messy data into an orderly form;

```python
import pandas as pd
```

## Pandas Data Structures

### Series
A Series id a one-dimentional array-like object containind a sequence of values (similar types to [[NumPy]] types) of the same type an assiociated array of data labels, called its *index*. The simplest Series is formed from an array of data:

```python
obj = pd.Series([4, 7, -5, 3])
```

### DataFrame
Represents a rectangular table of data and contains ordered named collection of columns, each of which can be a different value type (numeric, string ...). The DataFrame has both a row and column index.
```python
data = {"state": ["Ohio", "Ohio", "Ohio", "Nevada", "Nevada", "Nevada"], "year": [2000, 2001, 2002, 2001, 2002, 2003], "pop": [1.5, 1.7, 3.6, 2.4, 2.9, 3.2]} frame = pd.DataFrame(data)
```
Out:
```python
  state year pop 
0 Ohio 2000 1.5 
1 Ohio 2001 1.7 
2 Ohio 2002 3.6 
3 Nevada 2001 2.4 
4 Nevada 2002 2.9 
5 Nevada 2003 3.2
```

Main functions:
`.head()`/`.tail()` shows first/last five rows
`frame["state"]` taking particular **column**
`frame2.loc[1]/.iloc[2]`  taking particular **row**

Assigning value for all in column:
`frame["debt"] = 16.5`
`frame2["debt"] = np.arange(6.)`

Removing columns:
**del** `frame2["eastern"]`

If the nested dictionary is passed to the DataFrame, pandas will interpret the outer dictionary keys as the columns, and the inner keys as the row indices:

```python
populations = {"Ohio": {2000: 1.5, 2001: 1.7, 2002: 3.6},"Nevada": {2001: 2.4, 2002: 2.9}}
```
Out
```python
	Ohio Nevada 
2000 1.5 NaN 
2001 1.7 2.4 
2002 3.6 2.9
```
We can tranaspose it:
`frame3.T`
```python
	2000 2001 2002 
Ohio 1.5 1.7 3.6 
Nevada NaN 2.4 2.9
```


> [!WARNING]
> Note that transposing discards the column data types if the col‐ umns do not all have the same data type, so transposing and then transposing back may lose the previous type information. The col‐ umns become arrays of pure Python objects in this case.

Transforming to [[NumPy]]:
```python
frame3.to_numpy()
```
DataFrame’s to_numpy method returns the data contained in the DataFrame as a two-dimensional ndarray.

>[!NOTE]
>If the DataFrame’s columns are different data types, the data type of the returned array will be chosen to accommodate all of the columns. Ex. dtype=object

## Data Loading, Storage, and File Formats
### Reading and Writing Data in Text Format

Text and binary data loading functions in pandas (chosen):

| Function    | Description                                                                                              |
| ----------- | -------------------------------------------------------------------------------------------------------- |
| read_csv    | Load delimited data from a file, URL, or file-like object; use comma as default delimiter                |
| read_excel  | Read tabular data from an Excel XLS or XLSX file                                                         |
| read_sql    | Read the results of a SQL query (using SQLAlchemy)                                                       |
| read_xml    | Read a table of data from an XML file                                                                    |
| read_pickle | Read an object stored by pandas using the Python pickle format                                           |
| read_html   | Read all tables found in the given HTML document                                                         |
| read_json   | Read data from a JSON (JavaScript Object Notation) string representation, file, URL, or file-like object |
In this notes we will focus on CSV, excel and json format:
```csv
a,b,c,d,message 
1,2,3,4,hello 
5,6,7,8,world 
9,10,11,12,foo
```

Example file reading:
```python
df = pd.read_csv("examples/ex1.csv")

Out[1]: 
a b c d message 
0 1 2 3 4 hello 
1 5 6 7 8 world 
2 9 10 11 12 foo
```

You can allow pandas to assign default column names, or you can specify names yourself 
`, names=["a", "b", "c", "d", "message"]`.

The na_values option accepts a sequence of strings to add to the default list of strings recognized as missing `, na_values=["NULL"]`:
```python
something a b c d message 
0 one 1 2 3.0 4 NaN 
1 two 5 6 NaN 8 world 
2 three 9 10 11.0 12 foo
```
Some useful [[Pandas]] `read_csv` function arguments:

| Argument  | Description                                                                                                                                                                                                                                                          |
| --------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| sep       | **Character sequence** or **regular expression** to use to split fields in each row.                                                                                                                                                                                 |
| header    | Row number to use as column names; defaults to 0 (first row), but should be None if there is no header row.                                                                                                                                                          |
| nrows     | Number of rows to read from beginning of file (not counting the header)                                                                                                                                                                                              |
| iterator  | Return a TextFileReader object for reading the file piecemeal. This object can also be used with the with statement.                                                                                                                                                 |
| chunksize | For iteration, size of file chunks                                                                                                                                                                                                                                   |
| decimal   | Decimal separator in numbers (e.g., "." or ","); default is ".".                                                                                                                                                                                                     |
| thousands | Separator for thousands (e.g., "," or "."); default is None.                                                                                                                                                                                                         |
| engine    | CSV parsing and conversion engine to use; can be one of "c", "python", or "pyarrow". The default is "c", though the newer "pyarrow" engine can parse some files much faster. The "python" engine is slower but supports some features that the other engines do not. |



## Work with API's

## Datab
## Sources:
- Python-for-Data-Analysis
- [Pandas Docs](https://pandas.pydata.org/)