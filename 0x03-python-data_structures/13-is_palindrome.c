#include <stdio.h>
#include "lists.h"

int is_palindrome(listint_t **head)
{
	struct listint_s *ptr;
	int n;

	if (*head == NULL)
	{
		return (1);
	}

	ptr = *head;
	n = 1;
	while (ptr != NULL)
	{
		printf("%d\n", ptr->n);
		ptr = ptr->next;
		n++;
	}
	return (1);
}
