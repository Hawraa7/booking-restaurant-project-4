# booking-restaurant-project-4
# Restaurant Booking System
## Introduction

This is a Django-based web application that serves as a restaurant booking and menu management system. The platform allows customers to browse the restaurant menu, book tables, and view their bookings. Admins can manage the menu, view and manage bookings, and update the restaurant's operations. The booking system logic was inspired by the precedent project on code's institute course and blogs. This website was created as a learning exercise for my [Code Institute](https://codeinstitute.net/global/) fourth portfolio project.
The live app can be found [here](https://booking-restaurant-project-b216b1fa54b9.herokuapp.com/bookings/).

(screenshot for responsive different pages................................)

## Project Goals
- To create a website that is easy to navigate and use.
- To create a visually appealing website.
- To create a website that is responsive on all devices.
- To create an interactive website.
- To create a website that is fun to use.
- To create a website that is easy to use.

## User Stories
### Site Users
- As a user, I want to view the restaurant's menu.

- As a user, I want to make a reservation.

- As a user, I want to receive a confirmation of my booking.

### Site Admin
- As an admin, I want to manage reservations.

- As an admin, I want to add, update, or remove menu items.

- As an admin, I want to manage user bookings efficiently.

## Design
### Look and feel

With the design for this website, the aim was to create a fun and easy-to-use website. The main colours were chosen from black and white. Had to add some CSS text-shadow trickery to improve the contrast on the light background. 

### Typography
- [Google Fonts](https://fonts.google.com/) was used for the font.
Font-family 'Arial' was chosen for the site. This font was chosen because it is easy to read and looks good on all devices. By using this font the site is more accessible for people with visual impairments whilst. 
Fall back font is Sans-serif.

## Database Schemas
The database consists of three main models: Table, MenuItem, and Booking. 

The project uses a relational database with the following models:

- A User can have multiple bookings (One-to-Many).
- A Booking is assigned to one Table (Foreign Key).
- A Booking can include multiple MenuItems, creating a many-to-many relationship.
- Each Table has a fixed capacity, and a Booking must respect that capacity ensuring that the number of guests does not exceed capacity.

Below is the detailed schema representation:

1. Table Model:

    Represents physical tables in the restaurant.

   - number: A unique identifier for the table.
   - capacity: The maximum number of guests the table can accommodate.
   (scrennshot for databse of table model.....................................................)

2. Booking Model:

   - user: Foreign Key linking to the User model.
   - table: Foreign Key linking to the Table model.
   - date: Date and time for the reservation (must be in the future).
   - guests: Number of guests for the booking.
   - status: The reservation status (confirmed/cancelled).
   (screenshot of database of booking model.........................................................)

3. MenuItem Model:

   - name: The name of the dish.
   - description: A description of the dish.
   - price: The price of the dish.
   - image: An optional image of the dish.
   (screenshot of database of menuitem model..................................................)

## Features
### Existing Features 
### User Features:
- **Navigation Bar**
  - Featured on all five pages, the full responsive navigation bar includes links to the Home page, Menu, Book a Table, Bookings of the User and Log Out page and is identical in each page to allow for easy navigation.
  - This section will allow the user to easily navigate from page to page across all devices without having to revert back to the previous page via the ´back´ button.
  (screenshot lal navbar........................)

- **Home Page**
  - The Home page displays a welcoming introduction to the restaurant with an image to the restaurant and contain two buttons to the viewing menu or booking a table. 
  (screenshot lal home page................................)

- **The Footer**
  - The footer section includes links to the relevant social media sites for Laclouc Restaurant. The links will open to a new tab to allow easy navigation for the user.
  - The footer is valuable to the user as it encourages them to keep connected via social media.
  (scrennshot lal footer........................................)

- **Menu Page**
  - The Menu page allows users to browse menu items categorized by type.
  - Displays images, descriptions, and prices for each dish.
  - Users can filter menu items by category (e.g., appetizers, main dish, desserts, beverage).
  - Admins can add, update, and remove menu items.
   
   In conclusion, The customers can browse the restaurant's menu, including details such as dish names, descriptions, prices, and images of the dishes.
   (screnshot lal menu page................................)

- **Reservation System in a Book a Table Page**
  - Users can select a date, time, and number of guests for their booking.
  - The system ensures that the selected date is in the future.
  - A waiting of confirmation email is sent upon successful booking.
  - Users can modify or cancel their reservations.
  - The system checks table capacity to ensure it matches the number of guests.
  - Admins have access to a dashboard to manage all reservations.
  (scrennshot lal book a table page...................................)

- **Bookings Page**
  - Users can view their current and past bookings.
  - Users can update or cancel their reservations.
  - Displays reservation details including table, date, time, number of guests, and status.
  (scrennshot lal bookings page..............................)

- **Admin Dashboard**
  - Admin Dashboard: Enables restaurant staff to manage bookings and update menu items.
  (screenshot lal url /admin...........................)

### Admin Features:
- **Manage Menu Items**
  - Admins can add, update, or remove dishes from the menu.
  - Admins can upload images and set descriptions and prices.

- **Manage Bookings**
   - Admins have the ability to view all bookings made by users, update booking status (e.g., confirmed, pending, canceled), and even cancel or reschedule bookings.

- **User Management** 
  - Admins can manage user accounts, which includes viewing their information and associated bookings. This ensures that the admin can keep track of users' activity on the platform.

- **LogOut Page**
  - This page allows users to securely log out of their account after they've finished interacting with the website.
  - Once logged out, users are redirected to the Home Page including Sign In or Register page, depending on the authentication flow.
  - Clears the user session, ensuring their data is no longer accessible after log out.
  - The Sign In Page allows returning users to log into their accounts.The users must enter their username/email and password to access their account. Upon successful login, the users are redirected to the homepage or the last visited page.
  - The Register Page allows new users to create an account by providing their details, so they can make reservations, view their booking history, and more. The users must provide a unique username/email and a password. After registration, users are automatically logged in and redirected to the homepage or their dashboard.

  This feature enhances the security and privacy of the users by ensuring that they can exit their session whenever they choose, and gives them the option to log back in or create a new account.
  (screenshot lal sign out page and sign in and register............................)

### Future Features
  - Online Payment Integration: Allow users to pay for reservations online.
  - Reviews & Ratings: Allow customers to leave feedback on menu items.
  - Special Offers & Discounts: Promote seasonal deals and discounts.

### Technologies Used

 #### Languages
   - Python as the backend programming language.
   - HTML as the markup language and templating language.
   - CSS as the style sheet language.
   - JavaScript to create carousel on index.html.

 #### Frameworks & Libraries
   - Django as the Python web framework.
   - Bootstrap as the CSS framework.
   - PostgreSQL
   - jQuery to simplify DOM manipulation.

 #### Django Packages
  
    Django installs a few packages by default and some packages get installed with other packages. Will list out the ones that I installed.

    1. crispy bootstrap : django-crispy-bootstrap5 provides you with a crispy-forms template pack to use with django-crispy-forms in your Django projects.
    2. Django: Django is a high-level Python Web framework that encourages rapid development and clean, pragmatic design.
    3. Django-allauth: integrated set of Django applications addressing authentication, registration, account management as well as 3rd party (social) account authentication.
    4. Django-storages : Django Storages is a collection of custom storage backends for Django.
    5. Pillow: PIL is the Python Imaging Library.
    6. Psycopg2: Psycopg is the most popular PostgreSQL database adapter for the Python programming language. Its main features are the complete implementation of the Python DB API 2.0 specification and thread safety (several threads can share the same connection). It was designed for heavily multi-threaded applications that create and destroy lots of cursors and make a large number of concurrent “INSERT”s or “UPDATE”s.
    7. whitenoise:  With a couple of lines of config WhiteNoise allows your web app to serve its own static files, making it a self-contained unit that can be deployed anywhere. 

#### Other tools and programs

- Food images used in the menu page were sourced from [Pexels](https://www.pexels.com/), which provide free high-quality images.
- Icons used in the project were taken from [Font Awesome](https://fontawesome.com/).
- [ami.responsivedesign.is](https://ui.dev/amiresponsive) was used to create the mockup image.
- [Visual Studio Code](https://code.visualstudio.com/) did all of my coding and synchronizing with GitHub on VS Code.
- [GitHub](https://github.com/) : for hosting repositories.
- [Heroku](https://www.heroku.com/) where the website is deployed.

  

## Testing

Each feature of the application was manually tested to ensure that it works as intended. The following actions were performed:

- Navigation Links: Checked that all navigation links work correctly and direct the user to the appropriate page.

- Menu Display: Verified that all menu items are displayed properly with images, descriptions, and prices.

- Booking System: Ensured that users can select a date, time, and number of guests, and that the system correctly validates and confirms reservations.

- Booking Modification: Tested the ability to edit and cancel reservations.

- Admin Features: Confirmed that the admin can manage bookings, add/update/delete menu items, and oversee reservation schedules.

- User Authentication: Verified that users can register, log in, and log out securely.

### Automated Testing

Django unit tests were written for key functionalities, including:

- Models: Tested relationships and constraints such as ensuring a booking cannot be made for a past date.

- Views: Checked that all views return the correct HTTP responses and templates.

- Forms: Validated form submission, including error handling and required fields.

- Authentication: Ensured that unauthorized users cannot access restricted pages.

To run automated tests:
- python manage.py test
(screenshot lal tests............................................................)
### Cross-Browser Testing

The website was tested on the following browsers:

- Google Chrome
- Mozilla Firefox
- Microsoft Edge
- Safari

All features functioned as expected across different browsers.

### Responsive Design Testing

The site was tested on multiple screen sizes to ensure it is fully responsive:

- Desktop (1920x1080)
- Laptop (1366x768)
- Tablet (768x1024)
- Mobile (375x667)
(screenshot lal sheshet ino responsive..........................................................)
Results:

- Navigation and layout adjusted dynamically.
- The reservation system remained accessible and easy to use.
- Images and text resized correctly without breaking layouts.

### Performance Testing
- Page Load Speed: The homepage and menu pages were tested using Chrome DevTools and Lighthouse to optimize performance.
- Database Queries: Ensured that database queries are efficient and do not cause slowdowns.

### Validator Testing
- HTML
  - No errors were returned when passing through the official [W3C validator](https://validator.w3.org/).
- CSS
  - No errors found via the official [W3C (Jigsaw) validator](https://jigsaw.w3.org/css-validator/).
- Python
  -  Code quality checked with flake8 for [PEP8 compliance](https://pep8ci.herokuapp.com/).

### Unfixed Bugs
  - No known unfixed bugs were found during testing. All identified issues were addressed to ensure smooth functionality across different devices, browsers, and user scenarios. The system has been thoroughly tested for usability, performance, and responsiveness.

## Deployment 
The site was deployed to GitHub pages. The steps to deploy are as follows:
- Ensure dependencies are up to date by running: 
  - pip freeze > requirements.txt
- Create a Procfile in the root directory with the following content:
  - web: gunicorn bookingrestaurant.wsgi
- Create a new Heroku app
- Set environment variables in Heroku:
  - set DEBUG=False
  - heroku config-var:
    - set SECRET_KEY= my_secret_key
  - heroku config-var:
    - set DATABASE_URL= my_database_url
- Run database migrations on Heroku
- Push the project to Heroku
- Manual deploy in heroku
(screenshot..........................................................)
- Open App or click View when you see: Your app was successfully deployed.
Once the deployment process is completed, the application will be live on Heroku and accessible through the provided URL: (https://booking-restaurant-project-b216b1fa54b9.herokuapp.com/bookings/)

## Credits
### Content
- Some code snippets and logic were adapted from the Django documentation ([Django Docs](https://docs.djangoproject.com/en/5.1/)).
- The booking system logic was inspired by the precedent project on code's institute course and blogs.
- Instructions on how to implement form validation on the Sign Up page was taken from [Specific YouTube Tutorial](https://www.youtube.com/)
- The deployment steps were adapted from the official Heroku documentation (Heroku Docs).





  












