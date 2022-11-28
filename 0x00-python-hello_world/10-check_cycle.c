#include "lists.h"
/**
 * print_listint - Prints the elements of a list
 * @h: Pointer to the head of list
 *
 * Return: Number of nodes
 */
size_t print_listint(const listint_t *h)
{
    const listint_t *current;
    unsigned int n; /* number of nodes */

    current = h;
    n = 0;
    while (current != NULL)
    {
        printf("%i\n", current->n);
        current = current->next;
        n++;
    }

    return (n);
}

/**
 * add_nodeint - Adds a new node at the beginning of a listint_t list
 * @head: Points to a pointer of the start of the list
 * @n: AN integer
 *
 * Return: Address of a new element
 */
listint_t *add_nodeint(listint_t **head, const int n)
{
    listint_t *new;

    new = malloc(sizeof(listint_t));
    if (new == NULL)
        return (NULL);

    new->n = n;
    new->next = *head;
    *head = new;

    return (new);
}

/**
 * free_listint - Frees the listint_t list
 * @head: Points to the list that is about to be freed
 *
 * Return: void
 */
void free_listint(listint_t *head)
{
    listint_t *current;

    while (head != NULL)
    {
        current = head;
        head = head->next;
        free(current);
    }
}
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
