# WhatBytes Django Assignment  

This Django project is a fully functional user management system featuring authentication, user profiles, and restricted access pages. It is designed with a clean and intuitive UI to meet the requirements specified in the assignment.

---

## 🚀 Live Demo  

**[Visit the Live Website](https://what-bytes-assignment-six.vercel.app/)**  

Or copy the link provided below and paste it in your browser:  
https://what-bytes-assignment-six.vercel.app/  

---

## 🛠️ Features  

### 🔐 **User Authentication**  
- Login with email or username and password.  
- Secure password reset functionality via email.  

### 🌐 **Pages & Functionalities**  
- **Login Page:**  
  - Username/Email and password fields.  
  - Links to Sign Up and Forgot Password pages.  
- **Sign Up Page:**  
  - Fields for username, email, password, and confirm password.  
  - Navigation back to the Login page.  
- **Forgot Password Page:**  
  - Input email to receive password reset instructions.  
  - Sends an email containing a reset password link.  
- **Change Password Page:**  
  - Authenticated users only.  
  - Fields for old password, new password, and confirm password.  
  - Navigation back to the Dashboard.  
- **Dashboard:**  
  - Accessible only to authenticated users.  
  - Displays a greeting message, links to Profile and Change Password pages, and logout functionality.  
- **Profile Page:**  
  - Displays user information: username, email, date joined, and last updated.  
  - Navigation back to the Dashboard and logout functionality.  

---

## 🎨 UX/UI Highlights  

- User-friendly interface with easy navigation between pages.  
- Proper validation and error handling for all forms.  
- Smooth transitions between pages and intuitive design choices.  

---

## 🧰 Tech Stack  

- **Backend:** Django (built-in authentication system)  
- **Frontend:** Django Templates  
- **Email Service:** Configured for secure password reset  
- **Hosting:** Vercel  

---

## 📦 Installation  

To run this project locally:  

1. Clone the repository:  
   ```bash  
   git clone https://github.com/Yuvaprakash24/WhatBytes-assignment.git  
   cd WhatBytes-assignment  

2. Create a virtual environment and activate it:  
   ```
   python -m venv venv  
   venv/bin/activate  

4. Install dependencies:  
   ```
   pip install -r requirements.txt  
   Migration is not required because I'm using online PostgreSQL database.    
5. Run the development server:  
   ```
   python manage.py runserver  

  Access the application at http://localhost:8000/.  

---

## 📚 Usage Instructions
Visit the live website.
Navigate through the Login, Signup, Dashboard, and Profile pages.
Test authentication features like password reset and change password.

---

## 🤝 Acknowledgments
Thank you for providing this opportunity to showcase my Django development skills.

---
