from app.db.repository.productsRepo import ProductsRepository 
from app.db.schema.products import ProductCreate , ProductUpdate
from app.db.models.products import Product


class ProductsService:
    def __init__(self , repo : ProductsRepository):
        self.repo = repo 

    def create_product(self , product_data : ProductCreate):
        return self.repo.create_product(product_data)
    
    def get_product_by_id(self, product_id: int):
        return self.repo.get_product_by_id(product_id)
    
    def get_products_paginated(self, page: int = 1, page_size: int = 10):
        return self.repo.get_all_products(page=page, page_size=page_size)
    
    def update_product(self, product_id: int, product_data: ProductUpdate):
        return self.repo.update_product_by_id(product_id, product_data)
    
    def check_stock(self , product_id : int , quantity: int) -> bool:
        product = self.repo.get_product_by_id(product_id)

        if not product :
            return False
        return product.stock >= quantity
    
    def reduce_stock(self, product_id: int, quantity: int) -> Product:
        product = self.repo.get_product_by_id(product_id)

        if not product:
            raise ValueError("Product not found")
        
        if product.stock < quantity:
            raise ValueError("Not enough stock")
        
        product.stock -= quantity
        update_data = ProductUpdate(stock=product.stock)
        return self.repo.update_product_by_id(product_id, update_data)
    
    def increase_stock(self, product_id: int, quantity: int) -> Product:
        product = self.repo.get_product_by_id(product_id)

        if not product:
            raise ValueError("Product not found")
        
        product.stock += quantity
        update_data = ProductUpdate(stock=product.stock)
        return self.repo.update_product_by_id(product_id, update_data)