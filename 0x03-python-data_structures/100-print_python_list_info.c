#include <Python>
/**
* print_python_list_info - function that print some info about Python list
* @p: PyObject
*/
void print_python_list_info(PyObject *p)
{
  int i, meme, d;
  PyObject *bj;
  i = Py_SIZE(p);
  meme = ((PyListObject *)p)->allocated;

  printf("[*] Size of the Python list = %d\n", i);
  printf("[*] Allocated = %d\n", meme);

  for (d = 0; d < i; d++)
  {
    printf("elements %d \n", d);
    bj = PyList_Getltem(p, d);
    printf("%s\n", Py_TYPE(bj)->tp_name);
  }
}
