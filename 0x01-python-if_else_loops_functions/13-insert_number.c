#include "lists.h"
/*by div-styl*/
/**
 * insert_node - func add number to the list
 * @head: the head of list
 * @number: the numberto be add to the list
 * Return: the number within list
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *nwnode = *head;
	listint_t *nw = malloc(sizeof(listint_t));

	if (nw == NULL)
		return (NULL);

	nw->n = number;

	if (!nwnode || nwnode->n >= number)
	{
		nw->next = nwnode;
		*head = nw;
		return (nw);
	}

	for (; nwnode && nwnode->next && nwnode->next->n < number;)
		nwnode = nwnode->next;
	nw->next = nwnode->next;
	nwnode->next = nw;
return (nw);
}
