from .base import BaseRepository
from app.db.models.products import Product
from app.db.schema.products import ProductCreate, ProductUpdate

class ProductsRepository(BaseRepository):
    def create_product(self, product_data: ProductCreate):
        newProduct = Product(**product_data.model_dump(exclude_none=True))

        self.session.add(instance=newProduct)
        self.session.commit()
        self.session.refresh(instance=newProduct)

        return newProduct
    
    def get_product_by_id(self, product_id: int):
        product = self.session.query(Product).filter_by(id=product_id).first()
        return product
    
    def get_all_products(self, page: int = 1, page_size: int = 10):
        offset = (page - 1) * page_size

        products = (self.session.query(Product)
                   .order_by(Product.id)
                   .limit(page_size)
                   .offset(offset)
                   .all())
        
        return products
    
    def update_product_by_id(self, product_id: int, product_data: ProductUpdate):
        product = self.session.query(Product).filter(Product.id == product_id).first()
        if not product:
            return None
        
        update_data = product_data.model_dump(exclude_none=True)

        for key, value in update_data.items():
            setattr(product, key, value)
        
        self.session.commit()
        self.session.refresh(product)
        return product
    
    def delete_product(self, product_id: int):
        product = self.session.query(Product).filter(Product.id == product_id).first()
        if not product:
            return None
        
        self.session.delete(product)
        self.session.commit()
        return product
    
    def get_products_by_category(self, category_id: int, page: int = 1, page_size: int = 10):
        offset = (page - 1) * page_size

        products = (self.session.query(Product)
                   .filter(Product.category_id == category_id)
                   .order_by(Product.id)
                   .limit(page_size)
                   .offset(offset)
                   .all())
        
        return products
    
    def search_products_by_name(self, name: str, page: int = 1, page_size: int = 10):
        offset = (page - 1) * page_size

        products = (self.session.query(Product)
                   .filter(Product.name.ilike(f"%{name}%"))
                   .order_by(Product.id)
                   .limit(page_size)
                   .offset(offset)
                   .all())
        
        return products
