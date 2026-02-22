## Common object stucture
All Python obects are extention of [[PyObject]] type.
CPython on start allocates small `int` type objects in range  $<-5,256>$  

### Memory usage
For 10 elements from range

|          | `Python Object` | `Numpy Array` | `PyTorch Tensor` |
| -------- |-----------------|---------------|------------------|
| Header   | 184 B           | 192 B         | 72 B             |
| Raw data | 464 B           | 80 B          | 80 B             |

