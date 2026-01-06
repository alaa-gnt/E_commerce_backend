from app.db.repository.orderItemsRepo import OrderItemsRepository
from app.db.repository.productsRepo import ProductsRepository
from app.db.schema.order_items import OrderItemCreate, OrderItemUpdate
from app.db.models.order_items import Order_item


class OrderItemsService:
    def __init__(self, order_items_repo: OrderItemsRepository, products_repo: ProductsRepository):
        self.order_items_repo = order_items_repo
        self.products_repo = products_repo

    def add_item_to_order(self, order_id: int, item_data: OrderItemCreate):
        product = self.products_repo.get_product_by_id(item_data.product_id)
        
        if not product:
            raise ValueError("Product not found")
            price = product.price * item_data.quantity
        
        return self.order_items_repo.create_order_item(item_data, order_id, price)

    def update_item_quantity(self, order_id: int, item_id: int, new_quantity: int):
        order_item = self.order_items_repo.get_order_item_by_id(item_id)
        
        if not order_item:
            raise ValueError("Order item not found")
        
        if order_item.order_id != order_id:
            raise ValueError("Order item does not belong to this order")
        
        product = self.products_repo.get_product_by_id(order_item.product_id)
        if not product:
            raise ValueError("Product not found")
        
        new_price = product.price * new_quantity
        update_data = OrderItemUpdate(quantity=new_quantity, price=new_price)
        
        return self.order_items_repo.update_order_item_by_id(item_id, update_data)

    def remove_item_from_order(self, order_id: int, item_id: int):
        order_item = self.order_items_repo.get_order_item_by_id(item_id)
        
        if not order_item:
            raise ValueError("Order item not found")
        
        if order_item.order_id != order_id:
            raise ValueError("Order item does not belong to this order")
        
        return self.order_items_repo.delete_order_item(item_id)

    def get_items_by_order(self, order_id: int):
        return self.order_items_repo.get_order_items_by_order_id(order_id)

    def get_order_item_by_id(self, item_id: int):
        return self.order_items_repo.get_order_item_by_id(item_id)
