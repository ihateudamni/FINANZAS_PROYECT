from sqlmodel import Relationship, SQLModel, Field
from typing import Optional
from datetime import date 
# Importamos Item de forma relativa para el tipo de la relación


class GastoBase(SQLModel):
    tipo_gasto : str = Field(index=True)
    cantidad_gasto: float = Field()
    fecha_gasto: date = Field(default_factory=date.today)
    descripcion: Optional[str] = None

class GastoCreateIn(SQLModel):
    tipo_gasto: str = Field()
    cantidad_gasto: float =Field()
    fecha_gasto: Optional[date] = Field(default_factory=date.today)

class GastoUpdateIn(SQLModel):
    tipo_gasto: Optional[str] = None
    cantidad_gasto: Optional[float] = None
    fecha_gasto: Optional[date] = None
    descripcion: Optional[str] = None

class GastoRead(SQLModel):
    id: int = Field()
    tipo_gasto: str = Field()
    cantidad_gasto: float = Field()
    fecha_gasto: date = Field()
    descripcion: Optional[str] = None
    usuario_id: int

class Gasto(GastoBase, table = True):
    id: Optional[int] = Field(default=None, primary_key=True)
    usuario_id: Optional[int] = Field(default=None, foreign_key="item.id")
    
    usuario: Optional["Item"] = Relationship(back_populates="gastos")