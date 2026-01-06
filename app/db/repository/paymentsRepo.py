from .base import BaseRepository
from app.db.models.payments import Payment
from app.db.schema.payments import PaymentCreate

class PaymentsRepository(BaseRepository):
    def create_payment(self, payment_data: PaymentCreate):
        newPayment = Payment(**payment_data.model_dump(exclude_none=True))

        self.session.add(instance=newPayment)
        self.session.commit()
        self.session.refresh(instance=newPayment)

        return newPayment
    
    def get_payment_by_id(self, payment_id: int):
        payment = self.session.query(Payment).filter_by(id=payment_id).first()
        return payment
    
    def get_all_payments(self, page: int = 1, page_size: int = 10):
        offset = (page - 1) * page_size

        payments = (self.session.query(Payment)
                   .order_by(Payment.id)
                   .limit(page_size)
                   .offset(offset)
                   .all())
        
        return payments
    
    def update_payment_by_id(self, payment_id: int, update_data: dict):
        payment = self.session.query(Payment).filter(Payment.id == payment_id).first()
        if not payment:
            return None

        for key, value in update_data.items():
            setattr(payment, key, value)
        
        self.session.commit()
        self.session.refresh(payment)
        return payment
    
    def delete_payment(self, payment_id: int):
        payment = self.session.query(Payment).filter(Payment.id == payment_id).first()
        if not payment:
            return None
        
        self.session.delete(payment)
        self.session.commit()
        return payment
    
    def get_payment_by_order_id(self, order_id: int):
        payment = self.session.query(Payment).filter_by(order_id=order_id).first()
        return payment
    
    def get_payments_by_status(self, status: str, page: int = 1, page_size: int = 10):
        offset = (page - 1) * page_size

        payments = (self.session.query(Payment)
                   .filter(Payment.status == status)
                   .order_by(Payment.paid_at.desc())
                   .limit(page_size)
                   .offset(offset)
                   .all())
        
        return payments
    
    def get_payments_by_method(self, method: str, page: int = 1, page_size: int = 10):
        offset = (page - 1) * page_size

        payments = (self.session.query(Payment)
                   .filter(Payment.method == method)
                   .order_by(Payment.paid_at.desc())
                   .limit(page_size)
                   .offset(offset)
                   .all())
        
        return payments
