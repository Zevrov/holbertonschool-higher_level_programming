#include "lists.h"
/**
 * check_cycle - checks for a cycle in a linked list
 * @list: pointer to the start of the list
 *
 * Return: 1 if there is a cycle, 0 if not
 */
int check_cycle(listint_t *list)
{
	listint_t *slow, *fast;

	if (list == NULL || list->next == NULL)
		return (0);
	slow = list;
	fast = list->next;
	while (fast != NULL)
	{
		if (fast == slow)
			return (1);
		fast = fast->next;
		if (fast == NULL)
			break;
		if (fast == slow)
			return (1);
		fast = fast->next;
		slow = slow->next;
	}
	return (0);
}
