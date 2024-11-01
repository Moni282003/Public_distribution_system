import React from 'react';

const Header = () => {
  return (
    <header className="text-[#D1D5DB] p-2 px-4 flex items-center justify-between z-10"  style={{ fontFamily: '"Mona Sans", "Helvetica Neue", Helvetica, Arial, sans-serif' }}> {/* Flex for alignment */}
      <div className="flex flex-col items-start"> {/* Use a div to stack items vertically */}
        <h1 className="text-3xl font-bold flex items-center">
          <span className="mr-2 text-4xl"  style={{ fontFamily: '"Mona Sans", "Helvetica Neue", Helvetica, Arial, sans-serif' }}>🥗</span> {/* Emoji as logo */}
          Nutri<span className="text-orange-600">AI</span>d
        </h1>
        <h3 className="text-sm mt-1">Govt Initiative</h3> {/* Aligning h3 below the title */}
      </div>

      {/* Button Container */}
      <div className="flex space-x-2"> 
        <button className="border border-dotted border-white text-white px-4 py-2 rounded-full hover:bg-gray-600 transition duration-300 cursor-pointer">
          Contact
        </button>
        <button className="border border-dotted border-white text-white px-4 py-2 rounded-full hover:bg-gray-600 transition duration-300 cursor-pointer">
          Feedback
        </button>
      </div>
    </header>
  );
};

export default Header;
