#include <stdio.h>
#include <stdlib.h>
#include <Python.h>

/**
 * print_python_list_info - Printing some basic info about Python lists
 * @p: the PyObject
 *
 * Return: nothing return
 */

void print_python_list_info(PyObject *p)
{
PyObject *item;
PyListObject *list = (PyListObject *)p;
int k, the_size, allocs;

the_size = Py_SIZE(p);
allocs = list->allocated;
printf("[*] Size of the Python List = %d\n", the_size);
printf("[*] Allocated = %d\n", allocs);

for (k = 0; k < the_size; k++)
{
item =  PyList_GetItem(p, k);
printf("Element %d: %s\n", k, Py_TYPE(item)->tp_name);
}
}
