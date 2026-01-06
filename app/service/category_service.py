from app.db.repository.categoriesRepo import CategoriesRepository
from app.db.schema.categories import CategoryCreate, CategoryUpdate
from app.db.models.categories import Category


class CategoriesService:
    def __init__(self, repo: CategoriesRepository):
        self.repo = repo

    def create_category(self, category_data: CategoryCreate):
        return self.repo.create_category(category_data)
    
    def update_category(self, category_id: int, category_data: CategoryUpdate):
        return self.repo.update_category_by_id(category_id, category_data)
    
    def get_category_by_id(self, category_id: int):
        return self.repo.get_category_by_id(category_id)
    
    def get_all_categories(self, page: int = 1, page_size: int = 10):
        return self.repo.get_all_categories(page=page, page_size=page_size)
    
    def delete_category(self, category_id: int):
        return self.repo.delete_category(category_id)
