from fastapi import APIRouter, HTTPException

from src.routes.models import db_conn, session, Product, select, insert
from src.routes.schemas import ProductModel

from uuid import UUID


products_router = APIRouter(prefix='/products', tags=['Products'])


@products_router.post('')
async def add_new_product(product: ProductModel):
  try:
    with db_conn() as conn:
      conn.execute(insert(Product).values(**product.model_dump()))
      conn.commit()
  except Exception as e:
    raise HTTPException(
      detail=f'Something went wrong while inserting {product} into the database: {str(e)}',
      status_code=500
    )

  return f"Product {product} added successfully!"


@products_router.get('', response_model=list[ProductModel])
async def get_products(category: str | None = None):
  if category:
    result = get_product_by_category(category)

    if result is None:
      raise HTTPException(
        detail=f"No Items found for category: {category}",
        status_code=404
      )
    return result

  else: 
    with db_conn() as conn:
      return conn.execute(select(Product)).all()


@products_router.get('/{id}', response_model=ProductModel)
async def get_product_by_id(id: UUID):
  with db_conn() as conn:
    result = conn.execute(select(Product).where(Product.id == id)).first()

  if not result:
    raise HTTPException(
      detail=f"No product found with id: {id}",
      status_code=404
    )

  return result


def get_product_by_category(category: str):
  with db_conn() as conn:
    result = conn.execute(select(Product).where(Product.category == category))

  return result