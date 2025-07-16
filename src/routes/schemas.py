from pydantic import BaseModel, Field


class ProductModel(BaseModel):
  price: int
  n_items_in_stock: int
  category: str  # TODO: Create enum class for categories
  name: str
  id: int
