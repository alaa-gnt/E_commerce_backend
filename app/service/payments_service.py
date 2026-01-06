from app.db.repository.paymentsRepo import PaymentsRepository
from app.db.schema.payments import PaymentCreate, PaymentUpdate
from app.db.models.payments import Payment


class PaymentsService:
    def __init__(self, repo: PaymentsRepository):
        self.repo = repo

    def create_payment(self, payment_data: PaymentCreate):
        return self.repo.create_payment(payment_data)
    
    def process_payment(self, payment_id: int):
        payment_data = PaymentUpdate(status="processing")
        return self.repo.update_payment_by_id(payment_id, payment_data)
    
    def verify_payment(self, payment_id: int):
        payment_data = PaymentUpdate(status="completed")
        return self.repo.update_payment_by_id(payment_id, payment_data)
    
    def update_payment_status(self, payment_id: int, status: str):
        payment_data = PaymentUpdate(status=status)
        return self.repo.update_payment_by_id(payment_id, payment_data)
    
    def refund_payment(self, payment_id: int):
        payment_data = PaymentUpdate(status="refunded")
        return self.repo.update_payment_by_id(payment_id, payment_data)
    
    def get_payment_by_id(self, payment_id: int):
        return self.repo.get_payment_by_id(payment_id)
    
    def get_payment_by_order(self, order_id: int):
        return self.repo.get_payment_by_order_id(order_id)
