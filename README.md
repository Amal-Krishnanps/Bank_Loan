# Bank Loan System
System for a bank to lend money to borrowers and receive payment for the loans.

## Setup Instructions
**1. Clone the Repository**

    git clone https://github.com/Amal-Krishnanps/Bank_Loan.git
    
    cd bank_system

**2. Create a Virtual Environment**
   
     python -m venv venv
   
 **3. Activate the Virtual Environment**
 
      On Windows:
      venv\Scripts\activate
     
      On macOS/Linux:
      source venv/bin/activate
   
**4. Install Dependencies**

      pip install -r requirements.txt

**5. Apply Migrations**

     python manage.py migrate

**6. Create Superuser**

     python manage.py createsuperuser

**7. Run the Development Server**

     python manage.py runserver

Visit http://127.0.0.1:8000/ to view the API.

### API Endpoints

**1. Customer Management**
   
   **Create Customer**
    
    Method: POST
    URL: /api/customers/
    Payload: Provide customer details in the request body.

  **List All Customer**

    Method: GET
    URL: /api/customers/

  **Retrieve Customer Details**

    Method: GET
    URL: /api/customers/{customers_id}/

  **Update Vendor Details**

    Method: PUT
    URL: /api/customers/{customers_id}/
    Payload: Provide updated customer details in the request body.

  **Delete Vendor**

    Method: DELETE
    URL: /api/customers/{customers_id}/

    
**2. Loan Section**

  **Issue New Loan :**
  
      Method: POST
      URL: /api/issue/
      Payload: Provide loan details in the request body.

  **List All Loans**
  
      Method: GET
      URL: /api/issue/

**3. Accept Payments from Customer**

  **Payemnt Receipts**
  
    Method: POST
    URL: /api/payment/
    Payload: Provide details in the request body.

**4. Reports**

  **Individual Loans Ledger**

      Method: GET
      URL: /api/ledger//{loan_id}/


