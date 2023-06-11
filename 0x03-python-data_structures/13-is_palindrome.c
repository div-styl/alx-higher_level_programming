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
  listint_t *ptr1, *ptr2;

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
  ptr1 = *head;
  ptr2 = slow;

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
