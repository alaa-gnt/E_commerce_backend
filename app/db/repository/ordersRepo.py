from .base import BaseRepository
from app.db.models.orders import Order
from app.db.schema.orders import OrderCreate, OrderUpdate

class OrdersRepository(BaseRepository):
    def create_order(self, order_data: OrderCreate):
        newOrder = Order(**order_data.model_dump(exclude_none=True, exclude={'items'}))

        self.session.add(instance=newOrder)
        self.session.commit()
        self.session.refresh(instance=newOrder)

        return newOrder
    
    def get_order_by_id(self, order_id: int):
        order = self.session.query(Order).filter_by(id=order_id).first()
        return order
    
    def get_all_orders(self, page: int = 1, page_size: int = 10):
        offset = (page - 1) * page_size

        orders = (self.session.query(Order)
                 .order_by(Order.id)
                 .limit(page_size)
                 .offset(offset)
                 .all())
        
        return orders
    
    def update_order_by_id(self, order_id: int, order_data: OrderUpdate):
        order = self.session.query(Order).filter(Order.id == order_id).first()
        if not order:
            return None
        
        update_data = order_data.model_dump(exclude_none=True)

        for key, value in update_data.items():
            setattr(order, key, value)
        
        self.session.commit()
        self.session.refresh(order)
        return order
    
    def delete_order(self, order_id: int):
        order = self.session.query(Order).filter(Order.id == order_id).first()
        if not order:
            return None
        
        self.session.delete(order)
        self.session.commit()
        return order
    
    def get_orders_by_user_id(self, user_id: int, page: int = 1, page_size: int = 10):
        offset = (page - 1) * page_size

        orders = (self.session.query(Order)
                 .filter(Order.user_id == user_id)
                 .order_by(Order.created_at.desc())
                 .limit(page_size)
                 .offset(offset)
                 .all())
        
        return orders
    
    def get_orders_by_status(self, status: str, page: int = 1, page_size: int = 10):
        offset = (page - 1) * page_size

        orders = (self.session.query(Order)
                 .filter(Order.status == status)
                 .order_by(Order.created_at.desc())
                 .limit(page_size)
                 .offset(offset)
                 .all())
        
        return orders
