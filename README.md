### Learning Python
The sole purpose of this project is to be an aid, notes and small examples,
in learning python.

### Compiling cpython
```console
CPPFLAGS="-I$(brew --prefix zlib)/include" \
LDFLAGS="-L$(brew --prefix zlib)/lib" \
./configure --with-openssl=$(brew --prefix openssl) --with-pydebug
$ make -j8 -s
```

This will produce a binary named `python.exe`:
```console
$ ./python.exe --version
Python 3.9.0a0
```

### Debugging python
```console
$ lldb -- ./python.exe --version
(lldb) br s -n main
Breakpoint 1: where = python.exe`main + 22 at python.c:16:25, address = 0x0000000100000de6
(lldb) r
```
### Module
A module is a file that groups related functionality, data and classes.
Every source code file, .py, is a module.

### Package
A package groups modules.

### Native modules
```console
$ cd src/somethingmodule
$ python3 setup.py build
$ python3 setup.py install
$ python3 setup.py install
running install
running build
running build_ext
running install_lib
copying build/lib.macosx-10.14-x86_64-3.7/something.cpython-37m-darwin.so -> /usr/local/lib/python3.7/site-packages
running install_egg_info
Writing /usr/local/lib/python3.7/site-packages/something-1.0-py3.7.egg-info
```

```console
$ python3
>>> import something
>>> something.doit()
'Bajja'
```

```console
$ nm build/lib.macosx-10.7-x86_64-3.7/hellomodule.cpython-37m-darwin.so
                 U _Py_InitModule3
                 U __Py_BuildValue_SizeT
0000000000000ea0 t _hello_hello
0000000000000e70 T _inithellomodule
0000000000001020 d _module_functions
                 U dyld_stub_binder
```


### types
All values have a type:
```python
type(var)
```

### square root
```python
36 ** (1/2)
```

### strings
If you need to split a long string on a line you can use `\`. Note that this
will preserve whitespace: 
```python
print('very long string................ \
        which continues here........')
```
output:
```console
very long string................         which continues here........
```


If you don't want that you can use:
```python
print('very long string................'
        'which continues here........')
```
```console
very long string................which continues here........
```


### Troubleshooting
```console
$ python3
Python 3.7.1 (default, Dec 14 2018, 13:28:58)
[Clang 4.0.1 (tags/RELEASE_401/final)] :: Anaconda, Inc. on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import helloworld
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ImportError: dlopen(/anaconda3/lib/python3.7/site-packages/helloworld.cpython-37m-darwin.so, 2): Symbol not found: _Py_InitModule3
  Referenced from: /anaconda3/lib/python3.7/site-packages/helloworld.cpython-37m-darwin.so
  Expected in: flat namespace
 in /anaconda3/lib/python3.7/site-packages/helloworld.cpython-37m-darwin.so
```
```console
$ nm  build/lib.macosx-10.14-x86_64-3.7/helloworld.cpython-37m-darwin.so
                 U _Py_BuildValue
                 U _Py_InitModule3
0000000000000f20 t _helloworld
0000000000001060 d _helloworld_docs
0000000000001020 d _helloworld_funcs
0000000000000ef0 T _inithelloworld
                 U dyld_stub_binder
```
I was using the incorrect initialization for an extension. This has changed for
Python3 and I was using the syntax/API for Python2.


```console
$ python3 --version
Python 3.7.1
$ python3-config --includes
-I/anaconda3/include/python3.7m -I/anaconda3/include/python3.7m
```
