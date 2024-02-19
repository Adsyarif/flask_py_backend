from app.repositories.customer_repo import CustomerRepo

class CustomerService:
    def __init__(self):
        self.customer_repo = CustomerRepo()
        
    def get_customers(self):
        customers = self.customer_repo.get_list_customer()
        return [customer.as_dict() for customer in customers ]
    
    def update_customer(self, customer_id, customer_data_dto):
        updated_customer = self.customer_repo.update_customer(customer_id, customer_data_dto)  
        return updated_customer.as_dict()
    
    def search_customers(self, name):
        customers = self.customer_repo.search_customer(name)
        return [customer.as_dict() for customer in customers ]