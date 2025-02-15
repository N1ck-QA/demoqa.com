from pydantic import BaseModel, EmailStr, Field


class TestData(BaseModel):
    first_name: str = Field(..., description="Имя пользователя")
    last_name: str = Field(..., description="Фамилия пользователя")
    email: EmailStr = Field(..., description="Электронная почта")
    age: int = Field(..., gt=0, description="Возраст (должен быть положительным)")
    salary: int = Field(..., ge=0, description="Зарплата (не может быть отрицательной)")
    department: str = Field(..., description="Отдел, в котором работает пользователь")
