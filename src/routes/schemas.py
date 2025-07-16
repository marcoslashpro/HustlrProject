from pydantic import BaseModel, Field

from uuid import uuid4, UUID

class ProductModel(BaseModel):
  price: int
  n_items_in_stock: int
  category: str  # TODO: Create enum class for categories
  name: str
  id: UUID = Field(default=uuid4(), init_var=False)
