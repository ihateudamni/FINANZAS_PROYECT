from __future__ import annotations
from sqlmodel import Relationship, SQLModel, Field
from typing import Optional, List
from .inversion import Inversion 
from .gasto import Gasto


# --- 1. ItemBase: Base para la DB (incluye rol por defecto) ---
class ItemBase(SQLModel):
    nombre: str = Field()
    correo: str = Field()
    contraseña: str = Field()
    # Campo de rol controlado por el sistema
    rol: str = Field(default="user") 

# --- 2. ItemCreateIn: Modelo de ENTRADA para la creación (EXCLUYE 'rol') ---
class ItemCreateIn(SQLModel):
    nombre: str = Field()
    correo: str = Field()
    contraseña: str = Field()

# --- 3. ItemUpdateIn: Modelo de ENTRADA para la actualización (Todos opcionales) ---
class ItemUpdateIn(SQLModel):
    nombre: Optional[str] = None
    correo: Optional[str] = None
    contraseña: Optional[str] = None
    # Permitir la actualización del rol, pero solo será usado por el admin
    rol: Optional[str] = None

# --- 4. ItemCreateOut: Modelo de SALIDA (excluye 'contraseña') ---
class ItemCreateOut(SQLModel):
    id: Optional[int] = Field(default=None)
    nombre: str = Field()
    correo: str = Field()
    rol: str = Field()

    # 🔑 Se mantienen las cadenas de texto (correcto para SQLModel)
class Item(ItemBase, table=True, extend_existing=True): 
    id: Optional[int] = Field(default=None, primary_key=True)

    # 🎯 USAR LA CLASE DIRECTA (SIN COMILLAS)
    inversiones: List[Inversion] = Relationship(back_populates="usuario")
    gastos: List[Gasto] = Relationship(back_populates="usuario")