import { Link, useNavigate } from 'react-router-dom';
import { useEffect } from 'react';

export default function Citizen_dashboard() {
  const navigate = useNavigate();
  let timeoutId;

  const logout = () => {
    alert("Session expired. You will be redirected to the Landing page.");
    localStorage.removeItem('aadhar');
    navigate('/'); 
  };

  const resetTimer = () => {
    clearTimeout(timeoutId);
    timeoutId = setTimeout(logout, 30000); 
  };

  useEffect(() => {
    const centerId = localStorage.getItem('aadhar');
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

  const handleLogout = () => {
    localStorage.removeItem('aadhar');
    navigate('/');
  };

  return (
    <div className="bg-gradient-to-b from-[#0D0D0D] to-[#1D1D1D] flex flex-col justify-center min-h-screen" style={{ fontFamily: '"Mona Sans", "Helvetica Neue", Helvetica, Arial, sans-serif' }}>
      <div className="z-0 absolute inset-0 bg-[linear-gradient(to_right,#4f4f4f2e_1px,transparent_1px),linear-gradient(to_bottom,#4f4f4f2e_1px,transparent_1px)] bg-[size:200px_200px]" />
      <div className="sm:mx-auto sm:w-full sm:max-w-md">
        <h2 className="mt-6 text-center text-3xl font-extrabold text-[#D1D5DB]">
          Welcome to the Ration Shop!
        </h2>
      </div>

      <div className="mt-8 bg-[#1D1D1D] sm:mx-auto sm:w-full sm:max-w-md z-10">
        <div className="bg-[#1D1D1D] py-8 px-6 shadow-lg rounded-lg">
          <h3 className="text-xl font-semibold text-[#D1D5DB] mb-4">What would you like to do?</h3>

          <div className="space-y-4">
            <Link
              to="/view-rations"
              className="block py-3 px-4 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-orange-600 hover:bg-orange-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-orange-500"
            >
              View Rations
            </Link>

            <Link
              to="/update-rations"
              className="block py-3 px-4 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-orange-600 hover:bg-orange-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-orange-500"
            >
              Update Rations
            </Link>

            <Link
              to="/report"
              className="block py-3 px-4 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-orange-600 hover:bg-orange-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-orange-500"
            >
              Generate Report
            </Link>
          </div>

          <div className="mt-6">
            <button
              onClick={handleLogout}
              className="w-full flex justify-center py-3 px-4 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-red-600 hover:bg-red-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-red-500"
            >
              Logout
            </button>
          </div>
        </div>
      </div>
    </div>
  );
}
