#include "lists.h"
/**
* reverselist - reverse the list
*@head: the head of the list
* Return: void
*/
void reverselist(listint_t **head)
{
	listint_t *past = NULL, *futur = NULL, *presence = *head;

	while (presence != NULL)
	{
		futur = presence->next;
		presence->next = past;
		past = presence;
		presence = futur;
	}
	*head = past;
}
/**
* is_palindrome - function check if the list is palindrome
*@head: the head of the list
*Return: either 0 or 1
*/
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head, *fast = *head;
	listint_t *prev = NULL;

	if (*head == NULL || (*head)->next == NULL)
		return (1); /* check if the list is empty */
	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		prev = slow;
		slow = slow->next;
	}
	prev->next = NULL;
	reverselist(&slow);
	listint_t *ptr1 = *head;
	listint_t *ptr2 = slow;

	while (ptr1 != NULL && ptr2 != NULL)
	{
		if (ptr1->n != ptr2->n)
		{
			reverselist(&slow);
			prev->next = slow;
			return (0);
		}
		ptr1 = ptr1->next;
		ptr2 = ptr2->next;
	}
	reverselist(&slow);
	prev->next = slow;
	return (1);
}
/*-----------------------------*/
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
 * add_nodeint_end - adds a new node at the end of a listint_t list
 * @head: pointer to pointer of first node of listint_t list
 * @n: integer to be included in new node
 * Return: address of the new element or NULL if it fails
 */
listint_t *add_nodeint_end(listint_t **head, const int n)
{
    listint_t *new;
    listint_t *current;

    current = *head;

    new = malloc(sizeof(listint_t));
    if (new == NULL)
        return (NULL);

    new->n = n;
    new->next = NULL;

    if (*head == NULL)
        *head = new;
    else
    {
        while (current->next != NULL)
            current = current->next;
        current->next = new;
    }

    return (new);
}

/**
 * free_listint - frees a listint_t list
 * @head: pointer to list to be freed
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
