#include "lists.h"
/**
 *is_palindrome -function to check palind
 * @head: head of list
 * Return: 0 if not palindome 1 if it is
 */
int is_palindrome(listint_t **head)
{
	if (head == NULL || *head == NULL)
		return (1);
	return(rev_palind(head, *head));
}

/**
 * rev_palind - function to know if palind
 * @head: headlist
 * @end: end list
 */
int rev_palind(listint_t **head, listint_t *end)
{
	if (end == NULL)
		return (1);
	if (rev_palind(head, end->next) && (*head)->n == end->n)
	{
		*head = (*head)->next;
		return (1);
	}
	return (0);
}
