# django_employee_management_system
Basic employee management website using Django

The system properly compares any two employees against each other to determine if they are the same Person. 
This means that if you compared two People with the same Name, Birthday, Organization and its details, the system should think that they are equals to one another. 
If any of these properties are different, then the two People are not the same Person.

Project Includes:

  Register Page : any employee can register to a specific Organization(Google or Microsoft) by giving its details.

  Login Page: Its only for the Admins of Organization which is able to see following:
  - List of employees with their Details 
  - Total number of employees present/registered
  - List of employees are presented according to last registered

  ADMIN LOGIN----

  admin@google.com--->adming

  admin@microsoft.com--->adminm

  Authenticated and authorizied using auth_middleware---cant access details page unless you login
  
  
  
  
