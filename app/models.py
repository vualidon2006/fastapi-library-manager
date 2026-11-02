from pydantic import BaseModel, Field

class BookBase(BaseModel):
    isbn: str = Field(pattern=r"^\d{13}$", examples=["9786040000011"]) # Đúng 13 chữ số, duy nhất
    title: str = Field(min_length=1, max_length=200)                  # Từ 1 đến 200 ký tự, bắt buộc
    author: str = Field(min_length=1, max_length=100)                 # Từ 1 đến 100 ký tự, bắt buộc
    year: int = Field(ge=1900, le=2100)                             # Từ năm 1900 đến 2100
    quantity: int = Field(default=1, ge=0)                          # >= 0, mặc định là 1

class BookCreate(BookBase):
    pass

class BookUpdate(BaseModel):
    isbn: str | None = Field(default=None, pattern=r"^\d{13}$")
    title: str | None = Field(default=None, min_length=1, max_length=200)
    author: str | None = Field(default=None, min_length=1, max_length=100)
    year: int | None = Field(default=None, ge=1900, le=2100)
    quantity: int | None = Field(default=None, ge=0)

class BookOut(BookBase):
    id: int