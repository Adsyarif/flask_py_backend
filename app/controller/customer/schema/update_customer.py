from pydantic import BaseModel, Field
from typing import Optional

class UpdateCustomerRequest(BaseModel):
    name: str = Field(..., description = "Customer name", min_length=3, max_length=50)
    phone: Optional[str] = Field(None, descrtiption = "Customer phone number")
    address: Optional[str] = Field(..., descrtiption = "Customer address")