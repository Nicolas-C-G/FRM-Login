import { useEffect } from "react";
import axios from "axios";

function OAuthCallback({ provider }) {
  useEffect(() => {
    const code = new URLSearchParams(window.location.search).get("code");

    if (!code) {
      alert("No code in URL");
      return;
    }

    axios.post(`http://localhost:8000/auth/${provider}/callback`, { code })
      .then(res => {
        if (res.data && res.data.token) {
          localStorage.setItem("token", res.data.token);
          window.location.href = "/dashboard";
        } else {
          throw new Error("No token in response");
        }
      })
      .catch(err => {
        console.error("OAuth error:", err);
        alert("OAuth login failed");
      });
  }, [provider]);

  return <div>Logging in with {provider}...</div>;
}

export default OAuthCallback;
