import React from 'react';

const Highlights = () => {
  return (
    <div className="bg-[#1D1D1D] p-6 rounded-lg shadow-lg"> {/* Added shadow for depth */}
      <h2 className="text-2xl font-bold mb-6 text-center text-white"> {/* Increased margin bottom for spacing */}
        About Our Personalized PDS System
      </h2>

      {/* Highlights Container */}
      <div className="flex flex-col md:flex-row justify-center flex-wrap overflow-hidden">
        {[
          "Our personalized PDS (Personalized Dietary System) is designed to provide tailored nutrition plans based on individual dietary needs and preferences.",
          "With a focus on health and wellness, we utilize advanced algorithms to analyze nutritional levels and suggest optimized meal plans that fit your lifestyle.",
          "Whether you are aiming to lose weight, gain muscle, or simply maintain a balanced diet, our system offers customized recommendations to help you achieve your health goals.",
          "Join us today and take the first step towards a healthier you with our easy-to-use platform!",
          "Our system continuously learns from user feedback to improve dietary recommendations."
        ].map((highlight, index) => (
          <div
            key={index}
            className="bg-[#2A2A2A] p-6 rounded-lg flex-shrink-0 w-full md:w-64 lg:w-72 xl:w-80 flex flex-col justify-center m-4 transition-transform transform hover:scale-105" // Added hover effect and centered content
          >
            <p className="text-gray-200 text-center">{highlight}</p> {/* Changed text color for better contrast */}
          </div>
        ))}
      </div>
    </div>
  );
};

export default Highlights;
