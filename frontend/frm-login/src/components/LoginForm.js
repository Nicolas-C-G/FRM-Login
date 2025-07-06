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
    <div className="d-flex align-items-center justify-content-center vh-100 position-relative">
      <ThreeBackground />
      
      <div
        className="p-5 rounded shadow-lg position-relative"
        style={{
          backgroundColor: "rgba(255, 255, 255, 0.9)",
          zIndex: 1,
          minWidth: "350px",
        }}
      >
        <h2 className="text-center mb-4">Login</h2>
        <form onSubmit={handleLogin}>
          <div className="mb-3">
            <input
              type="text"
              className="form-control"
              value={email}
              onChange={(e) => setUsername(e.target.value)}
              placeholder="Email"
              required
            />
          </div>
          <div className="mb-3">
            <input
              type="password"
              className="form-control"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              placeholder="Password"
              required
            />
          </div>
          <button type="submit" className="btn btn-primary w-100 mb-3">
            Login
          </button>
        </form>

        <button
          className="btn btn-outline-dark w-100 mb-2"
          onClick={() => (window.location.href = "http://localhost:8000/auth/google")}
        >
          Login with Google
        </button>
        <button
          className="btn btn-outline-dark w-100 mb-3"
          onClick={() => (window.location.href = "http://localhost:8000/auth/microsoft")}
        >
          Login with Microsoft
        </button>

        <p className="text-center">
          <Link to="/register" className="text-decoration-none">
            Register New User
          </Link>
        </p>
      </div>
    </div>
  );
}

export default LoginForm;