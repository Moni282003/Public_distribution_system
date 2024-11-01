import { Link } from 'react-router-dom';
import Header from '../components/Header';
import Footer from '../components/Footer';
import Highlights from '../components/Highlights';
import { useEffect } from 'react';
import { motion } from 'framer-motion';

export default function LandingPage() {
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

  // Animation variants for the Highlights section
  const fadeIn = {
    hidden: { opacity: 0 },
    visible: { opacity: 1, transition: { duration: 0.6 } }
  };

  return (
    <div className="min-h-screen bg-[#0D0D0D] text-[#D1D5DB] flex flex-col justify-between" style={{ fontFamily: '"Mona Sans", "Helvetica Neue", Helvetica, Arial, sans-serif' }}>
      <Header />

      {/* Larger grid background */}
      <div className="absolute h-full w-full bg-[linear-gradient(to_right,#4f4f4f2e_1px,transparent_1px),linear-gradient(to_bottom,#4f4f4f2e_1px,transparent_1px)] bg-[size:200px_200px]" />

      {/* Card Section Centered */}
      <div className="flex-grow flex items-center justify-center relative z-10">
        <div className="container mx-auto flex justify-center h-full px-4 py-8">
          <div className="w-full md:w-1/2 flex flex-col justify-center p-4">
            <h1 className="text-4xl font-bold mb-8 text-center">Welcome to Nutri<span className="text-orange-600">AI</span>d</h1>
            <div className="grid grid-cols-1 md:grid-cols-2 gap-4 w-full">
              {[
                { name: 'Citizen', href: '/citizen-login', icon: '👤' },
                { name: 'Ration Shop', href: '/ration-login', icon: '🏪' },
                { name: 'Diagnostic Center', href: '/diagnostics-login', icon: '🧪' },
                { name: 'Central Admin', href: '/Central-Admin-login', icon: '🛠️' },
              ].map((user) => (
                <Link
                  key={user.name}
                  to={user.href}
                  className="bg-[#1D1D1D] p-6 rounded-lg text-center hover:bg-gray-600 transition duration-300 flex-grow flex flex-col justify-center border-t-4 border-orange-600"
                >
                  <span className="text-4xl mb-2 block">{user.icon}</span>
                  <span className="text-lg font-semibold">{user.name}</span>
                </Link>
              ))}
            </div>
          </div>
        </div>
      </div>

      {/* Highlights Section with Transition */}
      <motion.div
        className="relative z-10 mx-12"
        initial="hidden"
        animate="visible"
        variants={fadeIn}
      >
        <Highlights />
      </motion.div>

      {/* <Footer /> */}
    </div>
  );
}
