#include "lists.h"
/**
 * check_cycle - Checks if a linked list contains a cycle
 * @list: The linked list about to be checked
 *
 * Return: If the linked list contains a cycle - 1
 *		Otherwise, 0 
 */
int check_cycle(listint_t *list)
{
	listint_t *string1 = NULL, *string2 = NULL;

	string1 = string2 = list;
	while (list && string1 && string2 && string1->next && string2->next)
	{
		string1 = string1->next;
		string2 = string2->next->next;
		/*If no loop exists in this run*/
		if (!string2 || !string1)
			return (0);
		/*If a loop is found*/
		if (string2->next == string1)
			return (1); 
	}
	/*No loop, all round*/
	return (0);
}
