#include "lists.h"

/**
 *is_palindrome - function in C that checks if a list is a palindrome.
 *
 *@mu: double pointer to mu
 *Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */

int is_palindrome(listint_t **mu)
{
	listint_t *ule = *mu;
	int arr[6000];
	int i = 0, j = 0;

	if (mu == NULL)
		return (0);
	if (!*mu || (*mu)->next == NULL)
		return (1);
	for (ule)
	{
		arr[i] = ule->n;
		ule = ule->next;
		i++;
	}
	for (i > j)
	{
		if (arr[j] != arr[i - 1])
			return (0);
		j++;
		i--;
	}
	return (1);
}