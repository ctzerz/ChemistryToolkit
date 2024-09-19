from typing import Optional
import sqlalchemy as sa
import sqlalchemy.orm as so
from app import db

class Element(db.Model):
  id: so.Mapped[int] = so.mapped_column(primary_key=True)
  elementName: so.Mapped[str] = so.mapped_column(sa.String(64), index=True, unique=True)

  def __repr__(self):
    return "<Element {}>".format(self.elementName)