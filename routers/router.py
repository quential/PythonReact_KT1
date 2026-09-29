from fastapi import APIRouter
from models.task import Category, Task, TaskOut

router = APIRouter(
    prefix="/tasks",
    tags=["tasks"]
)


@router.get("/list", response_model=list[TaskOut])
def get_task_list():
    return [
        Task(
            id=1,
            title="Выучить React",
            description="Следуя плану изучения учебного материала, проходить уроки и выполнять тесты",
            category=Category(name="Обучение", color="blue"),
            internal_note="мяу мяу"
        )
    ]

@router.post("/create")
def create_task(task: Task):
    return task

@router.get("/{task_id}", response_model=TaskOut)
def get_task(task_id: int):
    return Task(
        id=task_id,
        title=f"Задача №{task_id}",
        description="описание",
        category=Category(name="Обучение", color="blue"),
        internal_note="мяу"
    )
