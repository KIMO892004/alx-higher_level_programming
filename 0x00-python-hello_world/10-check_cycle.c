#include "lists.h"

/**
 * check_cycle - checking if a linked list contains a cycle
 * @list: link list to checking
 *
 * Return: 1 if the list has a cycle, 0 if it doesn't
 */
int check_cycle(listint_t *list)
{
	listint_t *k = list;
	listint_t *r = list;

	if (!list)
		return (0);

	while (k && r && r->next)
	{
		k = k->next;
		r = fast->next->next;
		if (k == r)
			return (1);
	}

	return (0);
}
