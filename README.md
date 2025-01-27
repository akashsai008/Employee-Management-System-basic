```markdown
# Employee Management System (emp_mgt)

This is a simple Employee Management System built using Django. It allows you to manage employees, including viewing, adding, and removing employees, as well as filtering and displaying employee details based on different criteria. 

## Features

- **View All Employees**: Displays a list of all employees with their details.
- **Add Employee**: Allows you to add a new employee with details such as name, salary, bonus, phone number, department, and role.
- **Remove Employee**: Allows you to remove an existing employee by selecting from a dropdown.
- **Filter Employees**: Filter employees based on name, department, and role.
- **Dropdown for Employee Details**: Displays detailed information about an employee selected from a dropdown.

## Requirements

- Python 3.x
- Django 5.1.1

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/emp_mgt.git
   cd emp_mgt
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Apply database migrations:

   ```bash
   python manage.py migrate
   ```

4. Create a superuser (optional, for admin access):

   ```bash
   python manage.py createsuperuser
   ```

5. Start the development server:

   ```bash
   python manage.py runserver
   ```

6. Access the application at:

   ```
   http://127.0.0.1:8000/
   ```

## Directory Structure

```
emp_mgt/
│
├── emp_app/              # The app containing the employee management logic
│   ├── migrations/       # Database migration files
│   ├── models.py         # Models for Employee, Department, and Role
│   ├── views.py          # Views for handling requests
│   ├── urls.py           # URL configurations
│   ├── templates/        # HTML templates for rendering views
│   └── admin.py          # Admin configurations (if needed)
│
├── emp_mgt/              # Main project folder
│   ├── settings.py       # Django settings file
│   ├── urls.py           # Main URL configuration
│   └── wsgi.py           # WSGI entry point for the application
│
└── manage.py             # Django management command line tool
```

## Models

1. **Department**: Stores information about different departments within the company.
   - `name`: Name of the department.
   - `location`: Location of the department.

2. **Role**: Stores information about different roles.
   - `name`: Name of the role.

3. **Employee**: Stores employee information.
   - `firstname`: First name of the employee.
   - `lastname`: Last name of the employee.
   - `salary`: Salary of the employee.
   - `bonus`: Bonus of the employee.
   - `phonenum`: Phone number of the employee.
   - `hiredate`: The date the employee was hired.
   - `dept`: ForeignKey to the Department model.
   - `role`: ForeignKey to the Role model.

## Templates

1. **home.html**: The homepage.
2. **view_all_emp.html**: Displays all employees.
3. **add_emp.html**: Form to add a new employee.
4. **remove_emp.html**: Page for removing an employee.
5. **dropdown_emp.html**: Displays a dropdown of employees to select and view their details.
6. **filter_emp.html**: Filter employees based on name, department, and role.

## Contributing

Feel free to fork the repository and submit pull requests for any improvements or bug fixes!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```

### Notes:

- Replace `https://github.com/your-username/emp_mgt.git` with your actual repository URL if you're hosting it on GitHub.
- Make sure to adjust the installation steps if you have specific package dependencies in a `requirements.txt`.
- This `README.md` file assumes you have created the `requirements.txt` file to list your project dependencies.
