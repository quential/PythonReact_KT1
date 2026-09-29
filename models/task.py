from pydantic import BaseModel, field_validator


class Category(BaseModel):
    name: str
    color: str

class Task(BaseModel):
    id: int
    title: str
    description: str
    is_completed: bool = False
    category: Category
    internal_note: str | None = None

    @field_validator('title')
    def check_title_lenght(cls, value: str) -> str:
        if len(value) < 3:
            raise ValueError('Заголовок должен содержать минимум 3 символа!')
        return value

class TaskOut(BaseModel):
    id: int
    title: str
    description: str
    is_completed: bool
    category: Category





# class Category:
#     def __init__(self, name: str, color: str):
#         self.name = name
#         self.color = color
#
# class Task:
#     def __init__(self, title: str, description: str, is_completed: bool, category: Category):
#         self.title = title
#         self.description = description
#         self.is_completed = is_completed
#         self.category = category