from app.models.customer import Customer
from app.utils.database import db

class CustomerRepo():
    def get_list_customer(self):
        customer = Customer.query.all()
        return customer
    
    def update_customer(self, customer_id, customer):
        customer_obj = Customer.query.get(customer_id)
        customer_obj.name = customer.name
        customer_obj.phone = customer.phone
        customer_obj.address = customer.address
        
        db.session.commit()
        
    def search_customer(self, name):
        customers = Customer.query.filter(Customer.name.like(f"%{name}%")).all()
        return customers