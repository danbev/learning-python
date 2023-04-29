## Viratual Environments


### venv
This is part of Python3.5 and above and I think this is the recommended way at
this point to create virtual environments. Before this externa packages/tools
were needed, at least that is my understanding.

So anytime I need to install a python dependency with pip consider using a
virtual environment.

#### Create
```console
$ python3 -m venv venv
```

#### Activate 
```console
$ source venv/bin/activate
(venv) $
```
Notice that the version of python and pip and the binaries in the venv:
```console
(venv) $ which python
/home/danielbevenius/work/python/learning-python/venv/bin/python
```

