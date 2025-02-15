from pydantic import BaseModel, Field
from typing import Optional


class BrowserOptions(BaseModel):
    window_size: Optional[str] = Field(None, description="Размер окна браузера")
    incognito: bool = Field(False, description="Режим инкогнито")


class Config(BaseModel):
    browser: str = Field(..., pattern="^(chrome|firefox)$", description="Тип браузера (chrome/firefox)")
    base_url: str = Field(..., description="Базовый URL для DemoQA")
    browser_options: BrowserOptions
    wait_time: int = Field(10, gt=0, description="Время ожидания")
    logger_level: str = Field("INFO", pattern="^(DEBUG|INFO|WARNING|ERROR|CRITICAL)$",
                              description="Уровень логирования")
    data_path: Optional[str] = Field(None, description="Путь к тестовым данным")
