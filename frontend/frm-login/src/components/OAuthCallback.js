import { useEffect } from "react";
import axios from "axios";

function OAuthCallback({ provider }) {
  useEffect(() => {
    const code = new URLSearchParams(window.location.search).get("code");
    axios.post(`http://localhost:8000/auth/${provider}/callback`, { code })
      .then(res => {
        localStorage.setItem("token", res.data.token);
        window.location.href = "/dashboard";
      })
      .catch(() => alert("OAuth login failed"));
  }, [provider]);

  return <div>Logging in with {provider}...</div>;
}

export default OAuthCallback;
