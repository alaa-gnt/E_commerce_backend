from .base import BaseRepository
from app.db.models.categories import Category
from app.db.schema.categories import CategoryCreate

class CategoriesRepository(BaseRepository):
    def create_category(self, category_data: CategoryCreate):
        newCategory = Category(**category_data.model_dump(exclude_none=True))

        self.session.add(instance=newCategory)
        self.session.commit()
        self.session.refresh(instance=newCategory)

        return newCategory
    
    def get_category_by_id(self, category_id: int):
        category = self.session.query(Category).filter_by(id=category_id).first()
        return category
    
    def get_all_categories(self, page: int = 1, page_size: int = 10):
        offset = (page - 1) * page_size

        categories = (self.session.query(Category)
                     .order_by(Category.id)
                     .limit(page_size)
                     .offset(offset)
                     .all())
        
        return categories
    
    def update_category_by_id(self, category_id: int, category_data: CategoryCreate):
        category = self.session.query(Category).filter(Category.id == category_id).first()
        if not category:
            return None
        
        update_data = category_data.model_dump(exclude_none=True)

        for key, value in update_data.items():
            setattr(category, key, value)
        
        self.session.commit()
        self.session.refresh(category)
        return category
    
    def delete_category(self, category_id: int):
        category = self.session.query(Category).filter(Category.id == category_id).first()
        if not category:
            return None
        
        self.session.delete(category)
        self.session.commit()
        return category
    
    def get_categories_by_parent_id(self, parent_id: int):
        categories = self.session.query(Category).filter_by(parent_id=parent_id).all()
        return categories
