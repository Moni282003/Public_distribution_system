import React, { useState, useEffect } from 'react';
import { Outlet, useNavigate, useLocation } from 'react-router-dom';
import Sidebar from '../../components/Sidebar';

function AdminDashboard() {
  const [isNavExpanded, setIsNavExpanded] = useState(false);
  const [expandedSection, setExpandedSection] = useState(false);
  const navigate = useNavigate();
  let timeoutId;
  const location = useLocation();

  useEffect(() => {
    const centerId = localStorage.getItem('admin');
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

  const logout = () => {
    alert("Session expired. You will be redirected to the Landing page.");
    localStorage.removeItem('admin');
    navigate('/');
  };

  const resetTimer = () => {
    clearTimeout(timeoutId);
    timeoutId = setTimeout(logout, 300000);
  };

  const handleLogout = () => {
    localStorage.removeItem('admin');
    navigate('/');
  };

  const toggleNav = () => setIsNavExpanded(!isNavExpanded);
  const toggleDropdown = (section) => {
    setExpandedSection(expandedSection === section ? null : section);
  };

  return (
    <div className="bg-gradient-to-b from-[#0D0D0D] to-[#1D1D1D] z-40 flex flex-col justify-center sm:px-6 lg:px-3 min-h-screen" style={{ fontFamily: '"Mona Sans", "Helvetica Neue", Helvetica, Arial, sans-serif' }}>
      <div className="z-0 absolute inset-0 bg-[linear-gradient(to_right,#4f4f4f2e_1px,transparent_1px),linear-gradient(to_bottom,#4f4f4f2e_1px,transparent_1px)] bg-[size:200px_200px]" />

      <div className="z-50 flex h-screen text-white">
        {/* Sidebar Component */}
        <Sidebar
          isNavExpanded={isNavExpanded}
          toggleNav={toggleNav}
          expandedSection={expandedSection}
          toggleDropdown={toggleDropdown}
          setIsNavExpanded={setIsNavExpanded}
          setExpandedSection={setExpandedSection}
        />

        {/* Main Content */}
        <main className="flex-1 p-8 overflow-auto">
          <div className="flex justify-between items-center mb-6">
            {location.pathname === '/admin' ?(
              <h2 className="text-3xl font-semibold">Dashboard Overview</h2>
            ):<h2></h2>}
            <button 
              onClick={handleLogout} 
              className="bg-red-600 hover:bg-red-700 text-white font-bold py-2 px-4 rounded transition-colors"
            >
              Logout
            </button>
          </div>

          <Outlet />
        </main>
      </div>
    </div>
  );
}

export default AdminDashboard;
