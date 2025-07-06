import { useEffect, useState } from "react";
import axios from "axios";
import { Link } from "react-router-dom";
import ThreeBackground from "./ThreeBackground";

function LoginForm() {
  const [email, setUsername] = useState("");
  const [password, setPassword] = useState("");

  useEffect(() => {
    document.body.style.backgroundColor = "black";

    return () => {
      document.body.style.backgroundColor = "";
    }
  }, []);

  const handleLogin = (e) => {
    e.preventDefault();
    axios.post("http://localhost:8000/login", { email, password })
      .then(res => {
        localStorage.setItem("token", res.data.token);
        window.location.href = "/dashboard";
      })
      .catch(() => alert("Login failed"));
  };

  return (
    <div style={{ position: "relative", height: "100vh", overflow: "hidden" }}>
      <ThreeBackground />
      
      <div style={{
        position: "relative",
        zIndex: 1,
        maxWidth: 400,
        margin: "0 auto",
        top: "20%",
        padding: 30,
        background: "rgba(255,255,255,0.9)",
        borderRadius: 10,
        boxShadow: "0 0 10px rgba(0,0,0,0.3)"
      }}>

        <form onSubmit={handleLogin}>
          <input type="text" value={email} onChange={e => setUsername(e.target.value)} placeholder="Email" />
          <input type="password" value={password} onChange={e => setPassword(e.target.value)} placeholder="Password" />
          <button type="submit">Login</button>
        </form>

        <button onClick={() => window.location.href = "http://localhost:8000/auth/google"}>
          Login with Google
        </button>

        <button onClick={() => window.location.href = "http://localhost:8000/auth/microsoft"}>
          Login with Microsoft
        </button>

        <Link to="/register">
          <button>Register New User</button>
        </Link>
      </div>
    </div>
  );
}

export default LoginForm;
