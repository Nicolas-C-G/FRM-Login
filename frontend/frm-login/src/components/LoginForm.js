import { useState } from "react";
import axios from "axios";

function LoginForm() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");

  const handleLogin = (e) => {
    e.preventDefault();
    axios.post("http://localhost:8000/login", { username, password })
      .then(res => {
        localStorage.setItem("token", res.data.token);
        window.location.href = "/dashboard";
      })
      .catch(() => alert("Login failed"));
  };

  return (
    <div>
      <form onSubmit={handleLogin}>
        <input type="text" value={username} onChange={e => setUsername(e.target.value)} placeholder="Username" />
        <input type="password" value={password} onChange={e => setPassword(e.target.value)} placeholder="Password" />
        <button type="submit">Login</button>
      </form>

      <button onClick={() => window.location.href = "http://localhost:8000/auth/google"}>
        Login with Google
      </button>

      <button onClick={() => window.location.href = "http://localhost:8000/auth/microsoft"}>
        Login with Microsoft
      </button>
    </div>
  );
}

export default LoginForm;
