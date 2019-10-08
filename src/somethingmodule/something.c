#include <Python.h>

static PyObject* doit(PyObject* self)
{
   return Py_BuildValue("s", "Bajja");
}

static char something_docs[] =
   "something module\n";

static PyMethodDef something_funcs[] = {
   {"doit", 
     (PyCFunction)doit,
     METH_NOARGS,
     something_docs},
   {NULL}
};

static struct PyModuleDef somethingmodule = {
    PyModuleDef_HEAD_INIT,
    "something",   /* name of module */
    something_docs, /* module documentation, may be NULL */
    -1,       /* size of per-interpreter state of the module,
                 or -1 if the module keeps state in global variables. */
    something_funcs
};

PyMODINIT_FUNC PyInit_something(void)
{
    return PyModule_Create(&somethingmodule);
}
