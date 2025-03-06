"""
Models for the Employees API.
"""
from datetime import datetime, date as date_type
from typing import Any, Dict, List, Optional

from pydantic import Field

from .base import BaseModel, BaseResponse, PaginationParams, DateRangeParams


class EmployeeAddress(BaseModel):
    """Employee address model."""
    
    street: Optional[str] = Field(default=None, description="Street address")
    city: Optional[str] = Field(default=None, description="City")
    postal_code: Optional[str] = Field(default=None, description="Postal code")
    province: Optional[str] = Field(default=None, description="Province or state")
    country: Optional[str] = Field(default=None, description="Country")


class EmployeeBankAccount(BaseModel):
    """Employee bank account model."""
    
    bank_name: Optional[str] = Field(default=None, description="Bank name")
    account_number: Optional[str] = Field(default=None, description="Account number")
    iban: Optional[str] = Field(default=None, description="IBAN")
    swift: Optional[str] = Field(default=None, description="SWIFT/BIC code")


class EmployeeCreate(BaseModel):
    """Model for creating an employee."""
    
    name: str = Field(..., description="Employee name")
    email: Optional[str] = Field(default=None, description="Employee email")
    phone: Optional[str] = Field(default=None, description="Employee phone")
    position: Optional[str] = Field(default=None, description="Employee position/job title")
    department: Optional[str] = Field(default=None, description="Employee department")
    hire_date: Optional[date_type] = Field(default=None, description="Hire date")
    birth_date: Optional[date_type] = Field(default=None, description="Birth date")
    tax_id: Optional[str] = Field(default=None, description="Tax ID/SSN")
    address: Optional[EmployeeAddress] = Field(default=None, description="Employee address")
    bank_account: Optional[EmployeeBankAccount] = Field(default=None, description="Bank account information")
    salary: Optional[float] = Field(default=None, description="Employee salary")
    salary_period: Optional[str] = Field(default=None, description="Salary period (monthly, yearly)")
    notes: Optional[str] = Field(default=None, description="Employee notes")
    custom_fields: Optional[Dict[str, Any]] = Field(default=None, description="Custom fields")


class EmployeeUpdate(BaseModel):
    """Model for updating an employee."""
    
    name: Optional[str] = Field(default=None, description="Employee name")
    email: Optional[str] = Field(default=None, description="Employee email")
    phone: Optional[str] = Field(default=None, description="Employee phone")
    position: Optional[str] = Field(default=None, description="Employee position/job title")
    department: Optional[str] = Field(default=None, description="Employee department")
    hire_date: Optional[date_type] = Field(default=None, description="Hire date")
    birth_date: Optional[date_type] = Field(default=None, description="Birth date")
    tax_id: Optional[str] = Field(default=None, description="Tax ID/SSN")
    address: Optional[EmployeeAddress] = Field(default=None, description="Employee address")
    bank_account: Optional[EmployeeBankAccount] = Field(default=None, description="Bank account information")
    salary: Optional[float] = Field(default=None, description="Employee salary")
    salary_period: Optional[str] = Field(default=None, description="Salary period (monthly, yearly)")
    notes: Optional[str] = Field(default=None, description="Employee notes")
    custom_fields: Optional[Dict[str, Any]] = Field(default=None, description="Custom fields")


class Employee(EmployeeCreate):
    """Employee model."""
    
    id: str = Field(..., description="Employee ID")
    status: Optional[str] = Field(default=None, description="Employee status")
    created_at: Optional[datetime] = Field(default=None, description="Creation date")
    updated_at: Optional[datetime] = Field(default=None, description="Last update date")


class EmployeeListParams(PaginationParams):
    """Parameters for listing employees."""
    
    department: Optional[str] = Field(default=None, description="Filter by department")
    status: Optional[str] = Field(default=None, description="Filter by status")
    query: Optional[str] = Field(default=None, description="Search query")


class PayrollCreate(BaseModel):
    """Model for creating a payroll."""
    
    employee_id: str = Field(..., description="Employee ID")
    period: str = Field(..., description="Payroll period (e.g., '2023-01')")
    date: date_type = Field(..., description="Payroll date")
    base_salary: float = Field(..., description="Base salary amount")
    additions: Optional[List["PayrollAddition"]] = Field(default=None, description="Salary additions")
    deductions: Optional[List["PayrollDeduction"]] = Field(default=None, description="Salary deductions")
    taxes: Optional[List["PayrollTax"]] = Field(default=None, description="Taxes")
    notes: Optional[str] = Field(default=None, description="Payroll notes")
    custom_fields: Optional[Dict[str, Any]] = Field(default=None, description="Custom fields")


class PayrollAddition(BaseModel):
    """Payroll addition model."""
    
    name: str = Field(..., description="Addition name")
    amount: float = Field(..., description="Addition amount")
    description: Optional[str] = Field(default=None, description="Addition description")


class PayrollDeduction(BaseModel):
    """Payroll deduction model."""
    
    name: str = Field(..., description="Deduction name")
    amount: float = Field(..., description="Deduction amount")
    description: Optional[str] = Field(default=None, description="Deduction description")


class PayrollTax(BaseModel):
    """Payroll tax model."""
    
    name: str = Field(..., description="Tax name")
    amount: float = Field(..., description="Tax amount")
    rate: Optional[float] = Field(default=None, description="Tax rate")
    description: Optional[str] = Field(default=None, description="Tax description")


class PayrollUpdate(BaseModel):
    """Model for updating a payroll."""
    
    employee_id: Optional[str] = Field(default=None, description="Employee ID")
    period: Optional[str] = Field(default=None, description="Payroll period (e.g., '2023-01')")
    date: Optional[date_type] = Field(default=None, description="Payroll date")
    base_salary: Optional[float] = Field(default=None, description="Base salary amount")
    additions: Optional[List[PayrollAddition]] = Field(default=None, description="Salary additions")
    deductions: Optional[List[PayrollDeduction]] = Field(default=None, description="Salary deductions")
    taxes: Optional[List[PayrollTax]] = Field(default=None, description="Taxes")
    notes: Optional[str] = Field(default=None, description="Payroll notes")
    custom_fields: Optional[Dict[str, Any]] = Field(default=None, description="Custom fields")


class Payroll(PayrollCreate):
    """Payroll model."""
    
    id: str = Field(..., description="Payroll ID")
    status: str = Field(..., description="Payroll status")
    total_gross: float = Field(..., description="Total gross amount")
    total_net: float = Field(..., description="Total net amount")
    created_at: Optional[datetime] = Field(default=None, description="Creation date")
    updated_at: Optional[datetime] = Field(default=None, description="Last update date")


class PayrollListParams(PaginationParams, DateRangeParams):
    """Parameters for listing payrolls."""
    
    employee_id: Optional[str] = Field(default=None, description="Filter by employee ID")
    period: Optional[str] = Field(default=None, description="Filter by period")
    status: Optional[str] = Field(default=None, description="Filter by status")
    query: Optional[str] = Field(default=None, description="Search query")


class TimeOffCreate(BaseModel):
    """Model for creating a time off request."""
    
    employee_id: str = Field(..., description="Employee ID")
    type: str = Field(..., description="Time off type (vacation, sick, etc.)")
    start_date: date_type = Field(..., description="Start date")
    end_date: date_type = Field(..., description="End date")
    reason: Optional[str] = Field(default=None, description="Time off reason")
    notes: Optional[str] = Field(default=None, description="Time off notes")
    status: Optional[str] = Field(default=None, description="Time off status")
    custom_fields: Optional[Dict[str, Any]] = Field(default=None, description="Custom fields")


class TimeOffUpdate(BaseModel):
    """Model for updating a time off request."""
    
    employee_id: Optional[str] = Field(default=None, description="Employee ID")
    type: Optional[str] = Field(default=None, description="Time off type (vacation, sick, etc.)")
    start_date: Optional[date_type] = Field(default=None, description="Start date")
    end_date: Optional[date_type] = Field(default=None, description="End date")
    reason: Optional[str] = Field(default=None, description="Time off reason")
    notes: Optional[str] = Field(default=None, description="Time off notes")
    status: Optional[str] = Field(default=None, description="Time off status")
    custom_fields: Optional[Dict[str, Any]] = Field(default=None, description="Custom fields")


class TimeOff(TimeOffCreate):
    """Time off model."""
    
    id: str = Field(..., description="Time off ID")
    days: int = Field(..., description="Number of days")
    created_at: Optional[datetime] = Field(default=None, description="Creation date")
    updated_at: Optional[datetime] = Field(default=None, description="Last update date")


class TimeOffListParams(PaginationParams, DateRangeParams):
    """Parameters for listing time off requests."""
    
    employee_id: Optional[str] = Field(default=None, description="Filter by employee ID")
    type: Optional[str] = Field(default=None, description="Filter by type")
    status: Optional[str] = Field(default=None, description="Filter by status")
    query: Optional[str] = Field(default=None, description="Search query")


class ExpenseCreate(BaseModel):
    """Model for creating an expense."""
    
    employee_id: str = Field(..., description="Employee ID")
    date: date_type = Field(..., description="Expense date")
    amount: float = Field(..., description="Expense amount")
    category: str = Field(..., description="Expense category")
    description: Optional[str] = Field(default=None, description="Expense description")
    receipt_url: Optional[str] = Field(default=None, description="Receipt URL")
    status: Optional[str] = Field(default=None, description="Expense status")
    custom_fields: Optional[Dict[str, Any]] = Field(default=None, description="Custom fields")


class ExpenseUpdate(BaseModel):
    """Model for updating an expense."""
    
    employee_id: Optional[str] = Field(default=None, description="Employee ID")
    date: Optional[date_type] = Field(default=None, description="Expense date")
    amount: Optional[float] = Field(default=None, description="Expense amount")
    category: Optional[str] = Field(default=None, description="Expense category")
    description: Optional[str] = Field(default=None, description="Expense description")
    receipt_url: Optional[str] = Field(default=None, description="Receipt URL")
    status: Optional[str] = Field(default=None, description="Expense status")
    custom_fields: Optional[Dict[str, Any]] = Field(default=None, description="Custom fields")


class Expense(ExpenseCreate):
    """Expense model."""
    
    id: str = Field(..., description="Expense ID")
    created_at: Optional[datetime] = Field(default=None, description="Creation date")
    updated_at: Optional[datetime] = Field(default=None, description="Last update date")


class ExpenseListParams(PaginationParams, DateRangeParams):
    """Parameters for listing expenses."""
    
    employee_id: Optional[str] = Field(default=None, description="Filter by employee ID")
    category: Optional[str] = Field(default=None, description="Filter by category")
    status: Optional[str] = Field(default=None, description="Filter by status")
    query: Optional[str] = Field(default=None, description="Search query")


# Response models
class EmployeeResponse(BaseResponse, Employee):
    """Response model for a single employee."""
    pass


class EmployeeListResponse(BaseResponse):
    """Response model for a list of employees."""
    
    items: List[Employee] = Field(..., description="List of employees")
    total: Optional[int] = Field(default=None, description="Total number of employees")
    page: Optional[int] = Field(default=None, description="Current page")
    limit: Optional[int] = Field(default=None, description="Items per page")


class PayrollResponse(BaseResponse, Payroll):
    """Response model for a single payroll."""
    pass


class PayrollListResponse(BaseResponse):
    """Response model for a list of payrolls."""
    
    items: List[Payroll] = Field(..., description="List of payrolls")
    total: Optional[int] = Field(default=None, description="Total number of payrolls")
    page: Optional[int] = Field(default=None, description="Current page")
    limit: Optional[int] = Field(default=None, description="Items per page")


class TimeOffResponse(BaseResponse, TimeOff):
    """Response model for a single time off request."""
    pass


class TimeOffListResponse(BaseResponse):
    """Response model for a list of time off requests."""
    
    items: List[TimeOff] = Field(..., description="List of time off requests")
    total: Optional[int] = Field(default=None, description="Total number of time off requests")
    page: Optional[int] = Field(default=None, description="Current page")
    limit: Optional[int] = Field(default=None, description="Items per page")


class ExpenseResponse(BaseResponse, Expense):
    """Response model for a single expense."""
    pass


class ExpenseListResponse(BaseResponse):
    """Response model for a list of expenses."""
    
    items: List[Expense] = Field(..., description="List of expenses")
    total: Optional[int] = Field(default=None, description="Total number of expenses")
    page: Optional[int] = Field(default=None, description="Current page")
    limit: Optional[int] = Field(default=None, description="Items per page")
