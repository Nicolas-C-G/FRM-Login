import { jwtDecode } from "jwt-decode"
import { useEffect } from "react";
import { useNavigate } from "react-router-dom";

function Dashboard() {
  const navigate = useNavigate();

  useEffect(() => {
    const token = localStorage.getItem("token");
    if (!token) return navigate("/");

    try {
      const decoded = jwtDecode(token);
      const now = Date.now() / 1000;
      if (decoded.exp < now){
        localStorage.removeItem("token");
        navigate("/");
      }
    } catch (err) {
      localStorage.removeItem("token");
      navigate("/");
    }
   }, [navigate]);

  return <h1>Welcome to your Dashboard</h1>;

}

export default Dashboard;
