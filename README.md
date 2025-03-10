# PKcarwash-APP

## Description

The PKcarwash-APP helps both service providers and people who wish to easily reach a car wash shop, saving a lot of time! The app allows the admin to manage customer appointment requests efficiently.

## Actors

- **Admin**
- **Customers**

## Admin Operations

The admin can perform the following operations:

- **Login/Logout**: Admin can log in and out of the system.
- **View All Appointments**: Check the list of customer appointment requests.
- **Accept and Assign Appointment**: Accept the request (appointment) and assign it to a specific employee.
- **Reject an Appointment**: Choose to reject the appointment.
- **View Previous 10 Appointments Delivered**: View the last 10 appointments that have been delivered.
- **View All Appointments Delivered**: View all the appointments that have been delivered.

## Customer Operations

Customers can perform the following operations:

- **Register**: Create a new account.
- **Login/Logout**: Log in and out of the system.
- **Request for Appointment**: Request an appointment for a car wash.

## Service Types

The app supports the following service types:

1. Internal Wash
2. External Wash
3. Comprehensive Wash

## Tables/Collections

The app uses the following tables/collections to store data:

### Customers

- `id`: Unique identifier for the customer
- `name`: Name of the customer
- `phone_num`: Phone number of the customer
- `place`: Place of residence of the customer
- `adhaar_number`: Aadhaar number of the customer

### Appointments

- `id`: Unique identifier for the appointment
- `date`: Date of the appointment
- `time`: Time of the appointment
- `customer_id`: Identifier of the customer who made the appointment
- `status`: Status of the appointment (e.g., pending, accepted, rejected)
- `service_type`: Type of service requested

### Shop Collection

- `id`: Unique identifier for the shop collection
- `date`: Date of the collection
- `amount`: Amount collected

### Admin

- `id`: Unique identifier for the admin
- `name`: Name of the admin
- `password`: Password for the admin account

## Future Enhancements

- Add support for more service types.
- Implement notifications for appointment status updates.
- Enhance security features for admin and customer accounts.

## Author

Developed by Pavan Kalyan Manda

Website Developer | IoT & Embedded Systems Enthusiast | AI/ML Developer
