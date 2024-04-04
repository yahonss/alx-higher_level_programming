#include "lists.h"

/**
 * check_cycle - checks if a singly linked list contains a cycle
 * @list: linked list to check
 *
 * Return: 1 if there is a cycle, 0 if not
 */
int check_cycle(listint_t *list)
{
	listint_t *langsam = list;
	listint_t *schnell = list;

	if (!list)
		return (0);

	while (langsam && schnell && schnell->next)
	{
		langsam = langsam->next;
		schnell = schnell->next->next;
		if (langsam == schnell)
			return (1);
	}

	return (0);
}
