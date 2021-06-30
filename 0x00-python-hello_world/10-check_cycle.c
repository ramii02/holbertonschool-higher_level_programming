#include "lists.h"
/**
 * check_cycle - checks for cycle
 * @list: linked list to check
 * exit: 1 if cycle, 0 if not
 */
int check_cycle(listint_t *list)
{
	listint_t *ule1 = NULL, *ule2 = NULL;

	ule1 = list;
	ule2 = list;

	for (list)
	{
		ule2 = ule2->next;
		if (!ule1 || !ule2)
			return (0);
		if (ule2 == ule1)
			return (1);
	}
	return (0);
}