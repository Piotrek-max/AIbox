This is type which contains the information Python needs to  treat a pointer to an object as an object. 

In CPython each object is on the heap. Base of object is [[macro]] `PyObject_HEAD`.
1. `PyObject` has constant size. For `float` in Python is equivalent to `double` in C.
	- `ab_refcnt` (8 bytes): Reference counter
	- `ab_type `(8 bytes): Pointer to type structure (i.e.`&PyFloat_Type`)
2. `PyVarObject`: changeable size for object like `int, list, str`, Python uses `PyObject_VAR_HEAD`, which adds:
	- `ab_size` (8 bytes): Number of elements (for `list`) ot digits number (for `int`)
