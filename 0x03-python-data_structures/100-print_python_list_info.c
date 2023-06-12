#include <Python.h>
#include <stdio.h>

void print_python_list_info(PyObject *p)
{
    Py_ssize_t s, meme, d;
    PyObject *i;

    size = PyList_Size(p);
    alloc = ((PyListObject *)p)->allocated;

    printf("[*] Size of the Python List = %ld\n", s);
    printf("[*] Allocated = %ld\n", meme);

    for (d = 0; d < s; d++)
    {
        i = PyList_GetItem(p, d);
        printf("Element %ld: %s\n", d, Py_TYPE(i)->tp_name);
    }
}
