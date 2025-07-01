import { useState } from "react";
import axios from "axios";

function RegisterForm() {
    const [username, setUsername] = useState("");
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");

    const handleRegister = (e) => {
        e.preventDefault();
        axios.post("http://localhost:8000/register", {
            username,
            email,
            password,
        })
        .then(() => {
            alert("Registation successful!");
            window.location.href = "/";
        })
        .catch(() => alert("Registration failed"));
    };

    return (
    <div>
      <h2>Register</h2>
      <form onSubmit={handleRegister}>
        <input type="text" placeholder="Username" value={username} onChange={(e) => setUsername(e.target.value)} />
        <input type="email" placeholder="Email" value={email} onChange={(e) => setEmail(e.target.value)} />
        <input type="password" placeholder="Password" value={password} onChange={(e) => setPassword(e.target.value)} />
        <button type="submit">Register</button>
      </form>
    </div>
  );

}

export default RegisterForm;