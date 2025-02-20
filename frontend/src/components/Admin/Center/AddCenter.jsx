import React, { useState, useEffect } from 'react';
import axios from 'axios'; // Import Axios

const AddCenter = () => {
  const [rationIds, setRationIds] = useState([]); 
  const [selectedRationId, setSelectedRationId] = useState('');
  const [centerId, setCenterId] = useState('');
  const [locationPin, setLocationPin] = useState('');
  const [centerName, setCenterName] = useState('');
  const [address, setAddress] = useState('');
  const [contactNumber, setContactNumber] = useState('');

  useEffect(() => {
    const fetchRationIds = async () => {
      try {
        const response = await axios.get("http://localhost:5000/get_ration_ids"); 
        if (response.data && Array.isArray(response.data.ration_ids)) {
          setRationIds(response.data.ration_ids);
        } else {
          console.error("Unexpected response format:", response.data);
          setRationIds([]); 
        }
      } catch (error) {
        console.error("Failed to fetch ration IDs:", error);
        setRationIds([]); 
      }
    };

    fetchRationIds();
  }, []);

  const handleSubmit = async (e) => {
    e.preventDefault();
    const response = await fetch('http://localhost:5000/add_center', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        ration_id: selectedRationId,
        center_id: centerId,
        location_pin: locationPin,
        center_name: centerName,
        address,
        contact_number: contactNumber,
      }),
    });

    if (response.ok) {
      const result = await response.json();
      alert(result.message);
      setCenterId('')
      setCenterName('')
      setContactNumber('')
      setLocationPin('')
      setAddress('')
      // Optionally, reset the form or provide feedback
    } else {
      const error = await response.json();
      console.error('Error:', error);
    }
  };

  return (
    <div className="flex justify-center items-start h-screen">
      <div className="bg-[#4d4d4d] bg-opacity-30 backdrop-filter backdrop-blur-lg rounded-xl shadow-2xl p-8 w-full max-w-4xl">
        <h2 className="text-3xl font-semibold mb-4 text-center">Add Diagnostic Center</h2>
        <form onSubmit={handleSubmit}>
          <div className="mb-4">
            <label htmlFor="rationId" className="block mb-2">Ration ID</label>
            <select
              id="rationId"
              value={selectedRationId}
              onChange={(e) => setSelectedRationId(e.target.value)}
              required
              className="appearance-none block w-full px-4 py-3 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring focus:ring-orange-500 focus:border-orange-500 sm:text-sm bg-[#2D2D2D] text-[#D1D5DB]"
            >
              <option value="">Select Ration ID</option>
              {rationIds.map((id) => (
                <option key={id} value={id}>{id}</option>
              ))}
            </select>
          </div>

          <div className="mb-4">
            <label htmlFor="centerId" className="block mb-2">Center ID</label>
            <input
              type="text"
              id="centerId"
              value={centerId}
              onChange={(e) => setCenterId(e.target.value)}
              required
              className="appearance-none block w-full px-4 py-3 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring focus:ring-orange-500 focus:border-orange-500 sm:text-sm bg-[#2D2D2D] text-[#D1D5DB]"
              placeholder="Enter Center ID"
            />
          </div>

          <div className="mb-4">
            <label htmlFor="locationPin" className="block mb-2">Location Pin (6 digits)</label>
            <input
              type="text"
              id="locationPin"
              value={locationPin}
              onChange={(e) => setLocationPin(e.target.value)}
              required
              pattern="^\d{6}$"
              className="appearance-none block w-full px-4 py-3 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring focus:ring-orange-500 focus:border-orange-500 sm:text-sm bg-[#2D2D2D] text-[#D1D5DB]"
              placeholder="Enter Location Pin"
            />
          </div>

          <div className="mb-4">
            <label htmlFor="centerName" className="block mb-2">Center Name</label>
            <input
              type="text"
              id="centerName"
              value={centerName}
              onChange={(e) => setCenterName(e.target.value)}
              required
              className="appearance-none block w-full px-4 py-3 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring focus:ring-orange-500 focus:border-orange-500 sm:text-sm bg-[#2D2D2D] text-[#D1D5DB]"
              placeholder="Enter Center Name"
            />
          </div>

          <div className="mb-4">
            <label htmlFor="address" className="block mb-2">Address</label>
            <textarea
              id="address"
              value={address}
              onChange={(e) => setAddress(e.target.value)}
              required
              className="appearance-none block w-full px-4 py-3 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring focus:ring-orange-500 focus:border-orange-500 sm:text-sm bg-[#2D2D2D] text-[#D1D5DB]"
              placeholder="Enter Address"
            />
          </div>

          <div className="mb-4">
            <label htmlFor="contactNumber" className="block mb-2">Contact Number (10 digits)</label>
            <input
              type="text"
              id="contactNumber"
              value={contactNumber}
              onChange={(e) => setContactNumber(e.target.value)}
              required
              pattern="^\d{10}$"
              className="appearance-none block w-full px-4 py-3 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring focus:ring-orange-500 focus:border-orange-500 sm:text-sm bg-[#2D2D2D] text-[#D1D5DB]"
              placeholder="Enter Contact Number"
            />
          </div>

          <div className="flex justify-center">
            <button type="submit" className="bg-orange-600 hover:bg-orange-400 text-white py-2 px-4 rounded">Add Center</button>
          </div>
        </form>
      </div>
    </div>
  );
};

export default AddCenter;
