import { BrowserRouter as Router, Routes, Route, Navigate } from "react-router-dom";
import LoginForm from "./components/LoginForm";
import OAuthCallback from "./components/OAuthCallback";
import Dashboard from "./components/Dashboard";
import  { jwtDecode } from "jwt-decode";

const PrivateRoute = ({ children }) => {
  const token = localStorage.getItem("token");
  
  if (!token) return <Navigate to="/" />;

  try {
    const decoded = jwtDecode(token);
    const now = Date.now() / 1000;
    if (decoded.exp < now) {
      localStorage.removeItem("token");
      return <Navigate to="/" />
    }
    return children
  } catch (err) {
    localStorage.removeItem("token");
    return <Navigate to="/" />;
  }
};

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<LoginForm />} />
        <Route path="/oauth/google/callback" element={<OAuthCallback provider="google" />} />
        <Route path="/oauth/microsoft/callback" element={<OAuthCallback provider="microsoft" />} />
        <Route path="/dashboard" element={
          <PrivateRoute>
            <Dashboard/>
          </PrivateRoute>
        }/>
      </Routes>
    </Router>
  );
}

export default App;
