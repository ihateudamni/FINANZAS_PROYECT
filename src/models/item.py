from sqlmodel import SQLModel, Field
from typing import Optional

class ItemBase(SQLModel):
    nombre: str = Field()
    correo: str = Field()
    contraseña: str = Field()
    # Field solo sirve para definir los detalles de una columna en la base de datos

class ItemCreateIn(ItemBase): ...


class ItemCreateOut(SQLModel):
    id: int = Field()


class Item(ItemBase, table= True):
    id: int = Field(primary_key=True)