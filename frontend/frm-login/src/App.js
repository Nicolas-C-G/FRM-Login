import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import LoginForm from "./components/LoginForm";
import OAuthCallback from "./components/OAuthCallback";
import Dashboard from "./components/Dashboard";

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<LoginForm />} />
        <Route path="/oauth/google/callback" element={<OAuthCallback provider="google" />} />
        <Route path="/oauth/microsoft/callback" element={<OAuthCallback provider="microsoft" />} />
        <Route path="/dashboard" element={<Dashboard />} />
      </Routes>
    </Router>
  );
}

export default App;
