# 🛍️ CoBuy - Smart Social Subscription Sharing

CoBuy is a web application that connects people with similar interests across locations, allowing them to **match and co-purchase** subscriptions or services (like OTT platforms, software licenses, online memberships, etc.) in a **social, secure, and cost-effective way**.

## 🚀 Features

- 🔍 Match users with shared interests across geographies.
- 🤝 Enable group subscription purchases for services like Netflix, Spotify, etc.
- 💬 Built-in chat/match interface (optional future expansion).
- 🌐 User-friendly interface with Tailwind CSS and responsive design.

## 🛠️ Tech Stack

- **Backend:** Python + Flask  
- **Frontend:** HTML, Tailwind CSS  
- **Database:** SQLite (or plug in your preferred DB)  
- **Deployment:** Render / Heroku / Flask server  

## 📸 Screenshots (Optional)

_Add screenshots here showing matching interface, homepage, subscription matching logic._

## 📂 Folder Structure

CoBuy/
├── __pycache__/               # Python bytecode cache (can be ignored in Git)
├── templates/                 # HTML templates for Flask
│   └── (your HTML files)      
├── app.py                     # Main Flask application
├── requirements.txt           # Python dependencies (just `Flask`)
├── script.js                  # Frontend JavaScript logic
├── style.css                  # Custom CSS styles
├── user_interest.csv          # Data file for user interests
├── users.csv                  # Data file for user info
└── README.md                  # Project documentation


## 🔧 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/cobuy.git
   cd cobuy
Create virtual environment and activate


python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
Install dependencies

pip install -r requirements.txt
Run the app

flask run
Visit the app
Open http://127.0.0.1:5000 in your browser.

🛤️ Roadmap
 User authentication with OTP/email

 Payment gateway integration (Razorpay/Stripe)

 In-app messaging or WhatsApp linking

 AI-based user interest grouping

 Admin dashboard for subscription management

🙌 Contributing
Pull requests are welcome! If you have ideas to improve matching algorithms or UX/UI,or even for better implementation of the project feel free to fork and contribute.

✨ Acknowledgements

Flask Documentation
Tailwind CSS
Coolicons for icons
Everyone contributing to open source 💙
CoBuy is built to make digital sharing smarter and more affordable.
Let’s make subscriptions social again.
