from django.core.exceptions import ValidationError

from django_forms_part_two.web.models import Todo


def validate_max_todos_per_person(assignee):
    if assignee.todo_set.count() >= Todo.MAX_TODO_CONT_PER_PERSON:
        raise ValidationError(f'{assignee} already has max todos assigned.')

    return assignee

# If we put it in the model we will receive model object.
# def validate_max_todos_per_person2(todo: Todo):
#     todo.assignee
#     if assignee.todo_set.count() >= Todo.MAX_TODO_CONT_PER_PERSON:
#         raise ValidationError(f'{assignee} already has max todos assigned.')
#
#     return assignee
