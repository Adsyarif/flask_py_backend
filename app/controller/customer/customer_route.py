from flask import Blueprint, request
from app.utils.database import db
from app.models.customer import Customer
from app.utils.api_response import api_response
from app.service.customer_services import CustomerService
from app.controller.customer.schema.update_customer import UpdateCustomerRequest
blp = Blueprint("customer_endpoint", __name__)

@blp.route("/", methods=["POST"])
def create_customer():
    try:
        data = request.get_json()
        
        new_customer = Customer()
        new_customer.name = data["name"]
        new_customer.address = data["address"]
        new_customer.phone = data["phone"]
    
        db.session.add(new_customer)
        db.session.commit()
        return api_response(201, new_customer, "Created data successfull")
    
    except Exception:
        return api_response(404, message="Error")
    
    
@blp.route("/", methods=["GET"])
def get_all_customer():
    try:
        customer_service = CustomerService()
        customers = customer_service.get_customers()
        return api_response(201,customers, "OK")
    except TypeError:
        return {"message": "Error"}, 404
    
@blp.route("/search", methods=["GET"])
def search_customer():
    try:
        request_data = request.args
        customer_service = CustomerService()
        customers = customer_service.search_customers(request_data["name"])
        return api_response(201,customers, "OK")
    except TypeError:
        return {"message": "Error"}, 404
    
    
@blp.route("/<int:customer_id>", methods=["PUT"])
def update_customer(customer_id):
    try:
        data = request.json
        
        update_customer_request = UpdateCustomerRequest(**data)
        print(update_customer_request)

        customer = Customer()
        customer.phone = update_customer_request.phone
        customer.name = update_customer_request.name
        customer.address = update_customer_request.address
        
        
        customer_service = CustomerService()
        customers = customer_service.update_customer(customer_id, customer)
        
        return api_response(201,customers, message="updated")
    
    except Exception as e:
        return str(e), 500
    
    
@blp.route("/<int:customer_id>", methods=["DELETE"])
def delete_customer(customer_id):
    try:
        customer = Customer.query.get(customer_id)
        
        if not customer:
            return {"message": "Customer id not found"}, 404
        
        db.session.delete(customer)
        db.session.commit()
        
        return {"message": "Delete successful"}, 200
    
    except Exception as e:
        return str(e), 500