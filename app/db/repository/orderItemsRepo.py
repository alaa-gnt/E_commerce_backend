from .base import BaseRepository
from app.db.models.order_items import Order_item
from app.db.schema.order_items import OrderItemCreate

class OrderItemsRepository(BaseRepository):
    def create_order_item(self, order_item_data: OrderItemCreate, order_id: int, price: float):
        newOrderItem = Order_item(
            order_id=order_id,
            product_id=order_item_data.product_id,
            quantity=order_item_data.quantity,
            price=price
        )

        self.session.add(instance=newOrderItem)
        self.session.commit()
        self.session.refresh(instance=newOrderItem)

        return newOrderItem
    
    def get_order_item_by_id(self, order_item_id: int):
        order_item = self.session.query(Order_item).filter_by(id=order_item_id).first()
        return order_item
    
    def get_all_order_items(self, page: int = 1, page_size: int = 10):
        offset = (page - 1) * page_size

        order_items = (self.session.query(Order_item)
                      .order_by(Order_item.id)
                      .limit(page_size)
                      .offset(offset)
                      .all())
        
        return order_items
    
    def update_order_item_by_id(self, order_item_id: int, update_data: dict):
        order_item = self.session.query(Order_item).filter(Order_item.id == order_item_id).first()
        if not order_item:
            return None

        for key, value in update_data.items():
            setattr(order_item, key, value)
        
        self.session.commit()
        self.session.refresh(order_item)
        return order_item
    
    def delete_order_item(self, order_item_id: int):
        order_item = self.session.query(Order_item).filter(Order_item.id == order_item_id).first()
        if not order_item:
            return None
        
        self.session.delete(order_item)
        self.session.commit()
        return order_item
    
    def get_order_items_by_order_id(self, order_id: int):
        order_items = self.session.query(Order_item).filter_by(order_id=order_id).all()
        return order_items
    
    def get_order_items_by_product_id(self, product_id: int, page: int = 1, page_size: int = 10):
        offset = (page - 1) * page_size

        order_items = (self.session.query(Order_item)
                      .filter(Order_item.product_id == product_id)
                      .order_by(Order_item.id)
                      .limit(page_size)
                      .offset(offset)
                      .all())
        
        return order_items
