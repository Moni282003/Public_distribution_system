import { Link, useNavigate } from 'react-router-dom'; 
import { useState, useEffect } from 'react';
import { ArrowLeft, RefreshCw, Eye, EyeOff } from 'lucide-react'; 
import Header from '../components/Header';

export default function Diagnostic_login() {
  const [id, setId] = useState(''); 
  const [username, setUsername] = useState(''); 
  const [password, setPassword] = useState('');
  const [captcha, setCaptcha] = useState('');
  const [userCaptcha, setUserCaptcha] = useState('');
  const [error, setError] = useState('');
  const [showPassword, setShowPassword] = useState(false); 
  const navigate = useNavigate(); 
  useEffect(() => {
    const disableBackButton = () => {
      window.history.pushState(null, '', window.location.href);
      window.onpopstate = function (event) {
        window.history.go(1);
      };
    };
  
    disableBackButton();
  
    return () => {
      window.onpopstate = null; 
    };
  }, []);
  useEffect(() => {
    generateCaptcha();
  }, []);

  const generateCaptcha = () => {
    const characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789';
    let result = '';
    for (let i = 0; i < 6; i++) {
      result += characters.charAt(Math.floor(Math.random() * characters.length));
    }
    setCaptcha(result);
  };

  const handleSubmit = async(e) => {
    e.preventDefault();
  
    try {
      const response = await fetch('http://localhost:5000/login', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          center_id: id, 
          username: username, 
          password: password, 
          role:"diag"
        }),
      });
  
      if (!response.ok) {
        const error = await response.json();
        console.error('Login failed:', error);
        setError('Invalid credentials. Please try again.'); 
        return;
      }
  
      const data = await response.json();
      console.log('Login successful:', data);
      alert("Success");
      localStorage.setItem('username', username);
      localStorage.setItem('role', "diag");
      localStorage.setItem('centerid', id);

      navigate('/diagcenter'); 
    } catch (error) {
      console.error('Error during login:', error);
      setError('An error occurred. Please try again later.'); 
    }
  };

  return (
    <>
      <div className="bg-gradient-to-b from-[#0D0D0D] to-[#1D1D1D] flex flex-col justify-center sm:px-6 lg:px-8 min-h-screen" style={{ fontFamily: '"Mona Sans", "Helvetica Neue", Helvetica, Arial, sans-serif' }}>
        <div className="z-0 absolute inset-0 bg-[linear-gradient(to_right,#4f4f4f2e_1px,transparent_1px),linear-gradient(to_bottom,#4f4f4f2e_1px,transparent_1px)] bg-[size:200px_200px]" />
        <Header />
        <div className="sm:mx-auto sm:w-full sm:max-w-md">
          <h2 className="mt-6 text-center text-3xl font-extrabold text-[#D1D5DB]">
            Diagonstic center Login
          </h2>
        </div>

        <div className="mt-8 bg-[#1D1D1D] sm:mx-auto sm:w-full sm:max-w-md z-10">
          <div className="bg-[#1D1D1D] py-8 px-6 shadow-lg rounded-lg">
            <form className="space-y-6" onSubmit={handleSubmit}>
              {/* ID Field */}
              <div>
                <label htmlFor="id" className="block text-sm font-medium text-[#D1D5DB]">
                  Center ID
                </label>
                <div className="mt-1">
                  <input
                    id="id"
                    name="id"
                    type="text"
                    required
                    className="appearance-none block w-full px-4 py-3 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring focus:ring-orange-500 focus:border-orange-500 sm:text-sm bg-[#2D2D2D] text-[#D1D5DB]"
                    value={id} // Bind value to id state
                    onChange={(e) => setId(e.target.value)} // Update onChange to set id
                    placeholder="Enter your ID" // Placeholder for ID input
                  />
                </div>
              </div>

              {/* Username Field */}
              <div>
                <label htmlFor="username" className="block text-sm font-medium text-[#D1D5DB]">
                  Username
                </label>
                <div className="mt-1">
                  <input
                    id="username" // Changed from aadhar to username
                    name="username"
                    type="text"
                    required
                    className="appearance-none block w-full px-4 py-3 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring focus:ring-orange-500 focus:border-orange-500 sm:text-sm bg-[#2D2D2D] text-[#D1D5DB]"
                    value={username} // Updated value
                    onChange={(e) => setUsername(e.target.value)} // Updated onChange
                    placeholder="Enter your username" // Updated placeholder
                  />
                </div>
              </div>

              {/* Password Field */}
              <div>
                <label htmlFor="password" className="block text-sm font-medium text-[#D1D5DB]">
                  Password
                </label>
                <div className="mt-1 relative">
                  <input
                    id="password"
                    name="password"
                    type={showPassword ? 'text' : 'password'} 
                    required
                    className="appearance-none block w-full px-4 py-3 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring focus:ring-orange-500 focus:border-orange-500 sm:text-sm bg-[#2D2D2D] text-[#D1D5DB]"
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                    placeholder="Enter your password"
                  />
                  <button
                    type="button"
                    onClick={() => setShowPassword(!showPassword)} // Toggle password visibility
                    className="absolute inset-y-0 right-0 flex items-center pr-3"
                    aria-label="Toggle Password Visibility"
                  >
                    {showPassword ? <EyeOff className="h-5 w-5 text-gray-600" /> : <Eye className="h-5 w-5 text-gray-600" />}
                  </button>
                </div>
              </div>

              {/* Captcha Field */}
              <div>
                <label htmlFor="captcha" className="block text-sm font-medium text-[#D1D5DB]">
                  Captcha
                </label>
                <div className="mt-1 flex items-center">
                  <div className="flex-1 mr-2 bg-gray-200 p-2 rounded text-center font-mono text-3xl">
                    {captcha}
                  </div>
                  <button
                    type="button"
                    onClick={generateCaptcha}
                    className="p-2 bg-gray-100 rounded hover:bg-gray-200 transition duration-150 ease-in-out cursor-pointer"
                    aria-label="Refresh Captcha"
                  >
                    <RefreshCw className="h-5 w-5 text-gray-600" />
                  </button>
                </div>
                <div className="mt-4">
                  <input
                    id="captcha"
                    name="captcha"
                    type="text"
                    required
                    className="appearance-none block w-full px-4 py-3 border border-gray-600 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring focus:ring-orange-500 focus:border-orange-500 sm:text-sm bg-[#2D2D2D] text-[#D1D5DB]"
                    value={userCaptcha}
                    onChange={(e) => setUserCaptcha(e.target.value)}
                    placeholder="Enter the captcha above"
                  />
                </div>
              </div>

              {error && (
                <div className="bg-red-600 text-white p-3 rounded-md text-sm font-semibold text-center mt-4">
                  {error}
                </div>
              )}

              {/* Submit Button */}
              <div>
                <button
                  type="submit"
                  className="w-full cursor-pointer flex justify-center py-3 px-4 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-orange-600 hover:bg-orange-700 transition duration-150 ease-in-out focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-orange-500"
                >
                  Login
                </button>
              </div>
            </form>

            {/* Link to Sign Up */}
            <p className="mt-6 text-center text-sm text-[#D1D5DB]">
              <Link to="/" className="font-medium text-orange-500 hover:text-orange-400">
              Go back to Home page
              </Link>
            </p>
          </div>
        </div>
      </div>
    </>
  );
}