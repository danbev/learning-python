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
You can see where a module is located by simply using print:
```python
print(qiskit)
```

### Package
A package groups modules. A regular package is usually implemented as a
directory containing an `__init__.py` file. When a package gets imported this
file is executed.
What gets exposed to a user when they import a package is controlled by the
`__init__.py~ file in the package.

Take a look at [example_package](src/example_package) and you'll find it has
a `__init__.py` that exposes one function from the one module (but does not
expose the second function in it). This can be used by:
```console
$ PYTHONPATH=./src python3
Python 3.7.3 (default, Jun 19 2019, 07:38:49)
[Clang 10.0.1 (clang-1001.0.46.4)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import example_package
>>> example_package.
example_package.one(  example_package.two(
>>> example_package.one()
one function
```
### Class

### Double Under(dunder)/Magic methods
There are methods that are named with double underscores, hence sometimes called
dunder methods. For example, we can implement class and add a method named 
`__getitem__` which will allow an instance of that class to access a member
using array index syntax, instance[index].

#### __str__
This is used when you pass an instance to `print`. An example can be found 
in [str.py](src/str.py).

So, how does this actually work. Lets try to debug this:
```console
$ python3 -m pdb src/str.py
(Pdb) longlist
  6  ->	    def __str__(self):
  7  	        return 'Something(name=' + self.name + ')'
(Pdb) bt
  /usr/local/Cellar/python/3.7.3/Frameworks/Python.framework/Versions/3.7/lib/python3.7/bdb.py(585)run()
-> exec(cmd, globals, locals)
  <string>(1)<module>()
  /Users/danielbevenius/work/python/learning-python/src/str.py(13)<module>()
-> print(s);
> /Users/danielbevenius/work/python/learning-python/src/str.py(6)__str__()
-> def __str__(self):
```
So that does not really help much, it only looks like we called our __str__
function straight away.


#### __repr__
This is used when you want to display information about the instance in the
REPL:
```console
$ PYTHONPATH=./src python3
>>> import str
>>> l = str.Something("bajja")
>>> l
Something(name=bajja)


#### __call__
This method allow us to make an instance callable. See [call.py](src/call.py) 
for an example.


### __main__.py
Adding a file name `__main__.py` to a directory allows you to run code in the
package by just using the directory name. This could also be a zip file which
might of more value.

```console
$ python3 src/example_package/
__main__.py: running example_package using the directory
```

### Documentation

```console
>>> help (call)
Help on module call:

NAME
    call

CLASSES
    builtins.object
        Something

    class Something(builtins.object)
     |  Some class documentation
     |
     |  Methods defined here:
     |
     |  __call__(self, msg)
     |      some method documentation
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |
     |  __dict__
     |      dictionary for instance variables (if defined)
     |
     |  __weakref__
     |      list of weak references to the object (if defined)

DATA
    s = <call.Something object>

FILE
    /Users/danielbevenius/work/python/learning-python/src/call.py

```
Help can be used on classes within a module as well:
```console
>>> help(call.Something)
```

### pass
You can use the `pass` statement if you don't want to implement something. For
example, I was looking for a way to implement a class but just having a name for
it (in a test/example that is). Using pass allowed this, [pass](src/pass.py) is
an example of using this.

### tokenize
```console
$ python3 -m tokenize -e src/pass.py
0,0-0,0:            ENCODING       'utf-8'
1,0-1,5:            NAME           'class'
1,6-1,15:           NAME           'Something'
1,15-1,16:          COLON          ':'
1,16-1,17:          NEWLINE        '\n'
2,0-2,4:            INDENT         '    '
2,4-2,8:            NAME           'pass'
2,8-2,9:            NEWLINE        '\n'
3,0-3,1:            NL             '\n'
4,0-4,0:            DEDENT         ''
4,0-4,1:            NAME           's'
4,2-4,3:            EQUAL          '='
4,4-4,13:           NAME           'Something'
4,13-4,14:          LPAR           '('
4,14-4,15:          RPAR           ')'
4,15-4,16:          NEWLINE        '\n'
5,0-5,5:            NAME           'print'
5,5-5,6:            LPAR           '('
5,6-5,7:            NAME           's'
5,7-5,8:            RPAR           ')'
5,8-5,9:            SEMI           ';'
5,9-5,10:           NEWLINE        '\n'
6,0-6,0:            ENDMARKER      ''
```

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

### Conda
Is a package/environment management system, like npm I guess.
This is the package manager for Anaconda.
This will use a virtual environment to allow for separation of versions. Note
that there is a `virtualenv/venv` built into Python 3.

To create a new virtual environment with a specific python version:
```console
conda create --name python3-env python=3.7 -y
```

To use this environemnt:
```console
$ conda activate python3-env
(python3-env) $
```
See what environments are available:
```console
$ conda info --envs
# conda environments:
#
base                  *  /anaconda3
Qiskitenv                /anaconda3/envs/Qiskitenv
python3-env              /anaconda3/envs/python3-env
```

Remove:
```console
$ conda remove --name pyton3-env --all


### virtualenv/venv


### Debugging
```console
$ python3 -m pdb source.py
```


### lint
I ran into the following issue:
```console
(Qiskitenv) $ pylint -rn test
Traceback (most recent call last):
  File "/Users/danielbevenius/miniconda3/envs/Qiskitenv/bin/pylint", line 10, in <module>
    sys.exit(run_pylint())
  File "/Users/danielbevenius/miniconda3/envs/Qiskitenv/lib/python3.7/site-packages/pylint/__init__.py", line 17, in run_pylint
    from pylint.lint import Run
  File "/Users/danielbevenius/miniconda3/envs/Qiskitenv/lib/python3.7/site-packages/pylint/lint.py", line 76, in <module>
    import astroid
  File "/Users/danielbevenius/miniconda3/envs/Qiskitenv/lib/python3.7/site-packages/astroid/__init__.py", line 166, in <module>
    __import__(module[:-3])
  File "/Users/danielbevenius/miniconda3/envs/Qiskitenv/lib/python3.7/site-packages/astroid/brain/brain_builtin_inference.py", line 15, in <module>
    import six
ModuleNotFoundError: No module named 'six'
```
But the module `six` was installed. Uninstaling and installing again worked:
```console
$ pip uninstall six
$ pip install six
```

### __init__.py
There are two types of packages in Python, regular and namespace packages.

A regular package is typically implemented as a directory containing an 
__init__.py file. When a regular package is imported, this __init__.py file
is implicitly executed, and the objects it defines are bound to names in the
package’s namespace. 


### qiskit
```console
$ conda activate python3-env
(python3-env) $ /anaconda3/envs/python3-env/bin/pip install qiskit
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


### disasemble
```console
$ PYTHONPATH=src python3
>>> import dis
>>> import disasemble
>>> dis.dis(disasemble.something)
  3           0 LOAD_GLOBAL              0 (print)
              2 LOAD_CONST               1 ('bajja')
              4 CALL_FUNCTION            1
              6 POP_TOP
              8 LOAD_CONST               0 (None)
             10 RETURN_VALUE
```

### lambda
An example can be found in [lambda.py](src/lambda.py). 
Notice that the only difference is the `<function <lambda> at ` compared to
`<function function_name at` for a normal function.
```console
<class 'function'>
  4           0 LOAD_GLOBAL              0 (print)
              2 LOAD_FAST                0 (s)
              4 CALL_FUNCTION            1
              6 RETURN_VALUE
<function <lambda> at 0x1081fc268>
```
This can be important to know when looking at a stack trace.

A lambda function can’t contain any statements. In a lambda function, statements
like return, pass, assert, or raise will raise a SyntaxError exception.


### Installing a package locally
```console
$ pip install .
```
A project can also be installed as `editable` using the `-e` option:
```console
$ pip install -e .
```

It should now be possible to use this package.

```console
$ python3 -m <package-name>
```

Another option might be to run the module directly:
```console
$ python3 ~/work/wasm/wasmtime-py/wasmtime/bindgen ../seedwing_policy-engine-component.wasm --out-dir dist
```


### kwargs
I came accross this when looking at [Dense class](https://keras.io/api/layers/core_layers/dense/)
and could not find one of the input parameters that I was using:
```python3
dense = Dense(units=1, input_shape=[1])
```
In this case `input_shape` is not part of the named parameters that the classes
constructor (is that the correct term in Python?) takes.

In python one can pass multiple parameter to a function using `*args`. An
example can be found in [args.py](./src/args.py). The `*` here is the
`unpacking` operator.

Now, `**kwargs` is similar to `*args` but allows for a dictionary (named values)
to be passed in.


### Running Tests

To run a single test, a file that may contain multiple tests) one can specify
the file as an argument:
```console
$ pytest -s tests/codegen/test_empty_import.py
```
The `-s` will print output and is the same as specifying:
```console
$ pytest --capture=no tests/codegen/test_empty_import.py
```

### mypy
Mypy is a static type-checking tool for Python. It analyzes Python programs and
provides static type checking, which means it checks the types of variables, 
function parameters, return values, and expressions at compile-time, without 
actually executing the code.

### flake8
Is like a linter and a static analysis tool (think Clippy).


### Create virtual environment with venv
```console
$ python3 -m venv tf 
```

## Activate the environment
```console
$ source tf/bin/activate
```

## Install requirements
```console
$ source tf/bin/activate
(tf) pip install -r requirements.txt
```

Run pip freeze to generate a requirements.txt file to check in.
```console
(tf) $ pip freeze > requirements.txt
```
