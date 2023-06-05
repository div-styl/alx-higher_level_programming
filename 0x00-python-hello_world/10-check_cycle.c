#include "lists.h"
/**
 * check_cycle - func check if the signl linked list has a check_cycle
 * @list: list to be checked
 * Return: 0 or 1
 */ 
int check_cycle(listint_t *list)
{
  listint_t *slow = list;
  listint_t *thunder = list;

  if (list == NULL || list->next == NULL)
    return (0);
  for (;thunder != NULL && thunder->next != NULL;)
  {
    slow = slow->next;
    thunder = thunder->next->next;
    if (slow == thunder)
      return (1);
  }
  return (0);
}

