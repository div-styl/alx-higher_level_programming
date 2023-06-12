#include <Python.h>
#include <stdio.h>

void print_python_list_info(PyObject *p)
{
    Py_ssize_t s, meme, i;
    PyObject *item;

    s = PyList_Size(p);
    meme = ((PyListObject *)p)->allocated;

    printf("[*] Size of the Python List = %ld\n", s);
    printf("[*] Allocated = %ld\n", meme);

    for (i = 0; i < s; i++)
    {
        item = PyList_GetItem(p, i);
        printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
    }
}
