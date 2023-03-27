#include <stdio.h>
#include "lists.h"
#include <stdlib.h>

int is_palindrome(listint_t **head)
{
	struct listint_s *ptr;
	int n, iter;
	int current_n;
	int array[200];
	char word_reverse;

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
		*(array + (n - 1)) = ptr->n;	
		n++;
	}
	for (iter = n - 1; iter >= n; iter--)
	{
		*(word_reverse+iter) = *(array+iter);
	}

	return (1);
}
