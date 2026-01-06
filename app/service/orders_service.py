from app.db.repository.ordersRepo import OrdersRepository
from app.db.schema.orders import OrderCreate, OrderUpdate
from app.db.models.orders import Order


class OrdersService:
    def __init__(self, repo: OrdersRepository):
        self.repo = repo

    def create_order(self, order_data: OrderCreate):
        return self.repo.create_order(order_data)
    
    def get_order_by_id(self, order_id: int):
        return self.repo.get_order_by_id(order_id)
    
    def get_orders_paginated(self, page: int = 1, page_size: int = 10):
        return self.repo.get_all_orders(page=page, page_size=page_size)
    
    def update_order_status(self, order_id: int, status: str):
        order_data = OrderUpdate(status=status)
        return self.repo.update_order_by_id(order_id, order_data)
    
    def cancel_order(self, order_id: int):
        return self.update_order_status(order_id, status="cancelled")
