# FRM-Login Documentation (English & Français)

## 🌐 Project Overview / Présentation du projet

**EN:**
FRM-Login is a modern authentication system built with FastAPI (Python backend), React (frontend), and MySQL database. It supports traditional email/password login, as well as OAuth login with Google and Microsoft. It also features 3D visuals using Three.js for an enhanced user experience.

**FR :**
FRM-Login est un système d'authentification moderne développé avec FastAPI (backend Python), React (frontend), et une base de données MySQL. Il prend en charge l’authentification traditionnelle email/mot de passe ainsi que OAuth avec Google et Microsoft. Il inclut aussi des animations 3D via Three.js pour améliorer l'expérience utilisateur.

---

## 🚀 Setup / Installation

### Backend (FastAPI + MySQL)

**EN:**

1. Clone the repository: `git clone https://github.com/Nicolas-C-G/FRM-Login`
2. Navigate to backend: `cd FRM-Login/backend`
3. Create a virtual environment: `python -m venv env`
4. Activate it and install dependencies: `pip install -r requirements.txt`
5. Set up environment variables in a `.env` file (example below).
6. Run the server: `uvicorn main:app --reload`

**FR :**

1. Cloner le dépôt : `git clone https://github.com/Nicolas-C-G/FRM-Login`
2. Aller dans le dossier backend : `cd FRM-Login/backend`
3. Créer un environnement virtuel : `python -m venv env`
4. L’activer et installer les dépendances : `pip install -r requirements.txt`
5. Configurer les variables d’environnement dans un fichier `.env`
6. Lancer le serveur : `uvicorn main:app --reload`

### Frontend (React)

**EN:**

1. Navigate to the frontend: `cd ../frontend/frm-login`
2. Install dependencies: `npm install`
3. Run the development server: `npm start`

**FR :**

1. Aller dans le frontend : `cd ../frontend/frm-login`
2. Installer les dépendances : `npm install`
3. Lancer le serveur de développement : `npm start`

---

## 📁 Project Structure / Structure du projet

```
FRM-Login/
├── backend/
│   ├── auth/            # OAuth and login logic
│   ├── functions/       # Utility functions and schemas
│   ├── models/          # SQLAlchemy models
│   ├── database.py      # DB connection
│   └── main.py          # FastAPI app
│
├── frontend/
│   └── frm-login/
│       ├── src/
│       │   ├── components/   # React components
│       │   │   ├── LoginForm.js
│       │   │   ├── RegisterForm.js
│       │   │   └── ThreeBackground.js
│       │   └── App.js
```

---

## 🔐 Authentication / Authentification

**EN:**

* Traditional login with JWT token
* OAuth login via Google and Microsoft
* Access control using route protection in React

**FR :**

* Connexion traditionnelle avec JWT
* Authentification OAuth via Google et Microsoft
* Contrôle d’accès avec protection des routes dans React

---

## ✨ 3D Animation / Animation 3D

**EN:**

* `ThreeBackground.js` renders a 3D starscape using Three.js
* Appears only on the login screen

**FR :**

* `ThreeBackground.js` affiche une animation 3D avec des étoiles grâce à Three.js
* S’affiche uniquement sur l’écran de connexion

---

## 🔒 Security Features / Fonctionnalités de sécurité

* Email uniqueness enforced
* Passwords are hashed using bcrypt
* JWT token validation with expiration check
* Plans for token injection protection

---

## 💡 Potential Improvements / Améliorations potentielles

* Add LinkedIn OAuth
* Role-based access (e.g., admin/user)
* Password recovery
* Email verification
* Multi-language support in UI

---

## 📄 License / Licence

MIT License

---

## 🤝 Contributions

Pull requests are welcome. For major changes, please open an issue first.

**FR :**
Les contributions sont les bienvenues. Pour des modifications majeures, merci d’ouvrir d’abord une issue.

---

## 📬 Contact

**Nicolas Cartes**
GitHub: [Nicolas-C-G](https://github.com/Nicolas-C-G)
