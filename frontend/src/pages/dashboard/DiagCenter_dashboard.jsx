import React, { useEffect } from 'react';
import { useNavigate, Link, Outlet } from 'react-router-dom';

const DiagCenter_dashboard = () => {
  const navigate = useNavigate();
  let timeoutId;

  const resetTimer = () => {
    clearTimeout(timeoutId);
    timeoutId = setTimeout(sessionExpired, 300000);
  };
  const sessionExpired=()=>{
    alert("Session expired. You will be redirected to the Landing page.");
    localStorage.removeItem('username');
    navigate('/');
  }
  const logoutButton = () => {
    localStorage.removeItem('username');
    navigate('/');
  };

  useEffect(() => {
    const centerId = localStorage.getItem('username');
    if (!centerId) {
      navigate('/');
    } else {
      resetTimer();
    }

    const events = ['mousemove', 'keydown', 'click', 'scroll'];
    events.forEach(event => window.addEventListener(event, resetTimer));

    return () => {
      clearTimeout(timeoutId);
      events.forEach(event => window.removeEventListener(event, resetTimer));
    };
  }, [navigate]);

  return (
    <div className="bg-gradient-to-b z-40 from-[#0D0D0D] to-[#1D1D1D] flex flex-col min-h-screen" style={{ fontFamily: '"Mona Sans", "Helvetica Neue", Helvetica, Arial, sans-serif' }}>
<div className="z-0 fixed inset-0 bg-[linear-gradient(to_right,#4f4f4f2e_1px,transparent_1px),linear-gradient(to_bottom,#4f4f4f2e_1px,transparent_1px)] bg-[size:200px_200px]"/>

      {/* Menu Bar */}
      <nav className="bg-[#1D1D1D] p-4 shadow-md z-10 transition duration-300 ease-in-out mb-4">
        <div className="container mx-auto flex justify-between items-center">
          <Link to="/diagcenter" className="text-white text-lg font-semibold glow">Home</Link>
          <div className="flex space-x-4">
            <Link to="/diagcenter/submit-report" className="text-white hover:text-orange-500 glow">Submit Report</Link>
            <Link to="/diagcenter/view-citizens" className="text-white hover:text-orange-500 glow">View Citizens</Link>
            <Link to="/diagcenter/change-password" className="text-white hover:text-orange-500 glow">Change Password</Link>
          </div>
          <button 
            onClick={logoutButton} 
            className="bg-red-600 hover:bg-red-700 text-white font-bold py-2 px-4 rounded transition-colors glow"
          >
            Logout
          </button>
        </div>
      </nav>

      

      <style jsx>{`
        .glow {
          position: relative;
          color: white;
          text-shadow: 0 0 5px rgba(255, 165, 0, 0.7), 0 0 10px rgba(255, 165, 0, 0.5);
        }

        nav {
          box-shadow: 0 0 15px rgba(255, 165, 0, 0.5);
        }
      `}</style>
      <Outlet/>
    </div>
  );
};

export default DiagCenter_dashboard;
