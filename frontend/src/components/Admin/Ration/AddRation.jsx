import React, { useState } from 'react';

const AddRation = () => {
  const [shopId, setShopId] = useState('');
  const [address, setAddress] = useState('');
  const [locationPin, setLocationPin] = useState('');
  const [contactNumber, setContactNumber] = useState('');
  
  const handleSubmit = async (e) => {
    e.preventDefault();
    const response = await fetch('http://localhost:5000/add_ration_shop', { // Adjust URL as needed
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ 
            shop_id: shopId, 
            address, 
            location_pin: locationPin, 
            contact_number: contactNumber 
        }),
    });

    if (response.ok) {
        const result = await response.json();
        alert(result.message);
        
        // Clear the input fields after successful submission
        setShopId('');
        setAddress('');
        setLocationPin('');
        setContactNumber('');
    } else {
        const error = await response.json();
        alert('Error:', error);
    }
};

  return (
    <div className="flex justify-center items-start h-screen"> {/* Centering the container */}
      <div className="bg-[#4d4d4d] bg-opacity-30 backdrop-filter backdrop-blur-lg rounded-xl shadow-2xl p-8 w-full max-w-4xl">
        <h2 className="text-3xl font-semibold mb-4 text-center">Add Ration Shop</h2>
        <form onSubmit={handleSubmit}>
          <div className="mb-4">
            <label htmlFor="shopId" className="block mb-2">Shop ID (e.g., RA1234A)</label>
            <div className="relative">
              <span className="absolute left-3 top-3 text-gray-400">🛒</span> {/* Symbol for Shop ID */}
              <input
                type="text"
                id="shopId"
                value={shopId}
                onChange={(e) => setShopId(e.target.value)}
                required
                pattern="^RA\d{4}[A-Z]$" // Pattern for validating Shop ID
                className="appearance-none block w-full px-4 py-3 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring focus:ring-orange-500 focus:border-orange-500 sm:text-sm bg-[#2D2D2D] text-[#D1D5DB] pl-10"
                placeholder="Enter Shop ID"
              />
            </div>
          </div>

          <div className="mb-4">
            <label htmlFor="address" className="block mb-2">Address</label>
            <div className="relative">
              <span className="absolute left-3 top-3 text-gray-400">🏠</span> {/* Symbol for Address */}
              <textarea
                id="address"
                value={address}
                onChange={(e) => setAddress(e.target.value)}
                required
                className="appearance-none block w-full px-4 py-3 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring focus:ring-orange-500 focus:border-orange-500 sm:text-sm bg-[#2D2D2D] text-[#D1D5DB] pl-10"
                placeholder="Enter Address"
              />
            </div>
          </div>

          <div className="mb-4">
            <label htmlFor="locationPin" className="block mb-2">Location Pin (6 digits)</label>
            <div className="relative">
              <span className="absolute left-3 top-3 text-gray-400">📍</span> {/* Symbol for Location Pin */}
              <input
                type="text"
                id="locationPin"
                value={locationPin}
                onChange={(e) => setLocationPin(e.target.value)}
                required
                pattern="^\d{6}$" // Pattern for validating Location Pin
                className="appearance-none block w-full px-4 py-3 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring focus:ring-orange-500 focus:border-orange-500 sm:text-sm bg-[#2D2D2D] text-[#D1D5DB] pl-10"
                placeholder="Enter Location Pin"
              />
            </div>
          </div>

          <div className="mb-4">
            <label htmlFor="contactNumber" className="block mb-2">Contact Number (10 digits)</label>
            <div className="relative">
              <span className="absolute left-3 top-3 text-gray-400">📞</span> {/* Symbol for Contact Number */}
              <input
                type="text"
                id="contactNumber"
                value={contactNumber}
                onChange={(e) => setContactNumber(e.target.value)}
                required
                pattern="^\d{10}$" // Pattern for validating Contact Number
                className="appearance-none block w-full px-4 py-3 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring focus:ring-orange-500 focus:border-orange-500 sm:text-sm bg-[#2D2D2D] text-[#D1D5DB] pl-10"
                placeholder="Enter Contact Number"
              />
            </div>
          </div>

          <div className="flex justify-center"> {/* Centering the button */}
            <button type="submit" className="bg-orange-600 hover:bg-orange-400 text-white py-2 px-4 rounded">Add Shop</button>
          </div>
        </form>
      </div>
    </div>
  );
};

export default AddRation;
