import React, { useEffect, useState } from 'react';
import axios from 'axios';

const AddUser = () => {
  const [formData, setFormData] = useState({
    citizen_id: '',
    ration_card_id: '',
    ration_shop_id: '',
    location_pin: '',
    diagnostic_center: '',
    name: '',
    sex: '',
    dob: '',
    address: '',
    contact_number: '',
    income_level: 'Low',
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData((prevData) => ({
      ...prevData,
      [name]: value,
    }));

    if (name === 'location_pin' && value.length === 6) {
      axios.get(`http://localhost:5000/get_ration_shop_by_pin/${value}`)
        .then((response) => {
          const shopId = response.data.ration_shop_id;

          setFormData((prevData) => ({
            ...prevData,
            ration_shop_id: shopId,
            diagnostic_center: '',
          }));

          return axios.get(`http://localhost:5000/get_center_by_ration_shop/${shopId}`);
        })
        .then((response) => {
          const centerId = response.data.center_id;

          setFormData((prevData) => ({
            ...prevData,
            diagnostic_center: centerId,
          }));
        })
        .catch((error) => {
          console.error('Error fetching ration shop or center:', error);
          setFormData((prevData) => ({
            ...prevData,
            ration_shop_id: '',
            diagnostic_center: '',
          }));
        });
    }
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    if (formData.ration_card_id) {
      axios.post('http://localhost:5000/add_citizen', formData)
        .then((response) => {
          alert(response.data.message);
          setFormData({
            citizen_id: '',
            ration_card_id: '',
            ration_shop_id: '',
            location_pin: '',
            diagnostic_center: '',
            name: '',
            sex: '',
            dob: '',
            address: '',
            contact_number: '',
            income_level: 'Low',
          });
        })
        .catch((error) => {
          console.error('Error adding citizen:', error);
          alert('Failed to add citizen');
        });
    }
  };

  return (
    <div className="flex justify-center items-start h-screen">
      <div className="bg-[#4d4d4d] bg-opacity-30 backdrop-filter backdrop-blur-lg rounded-xl shadow-2xl p-8 w-full max-w-4xl">
        <h2 className="text-3xl font-semibold mb-4 text-center">Add Citizen</h2>
        <form onSubmit={handleSubmit} className="grid grid-cols-1 md:grid-cols-2 gap-4">
          
          <div className="mb-4">
            <label htmlFor="citizenId" className="block mb-2">
              Citizen ID:<span className="text-red-500">*</span>
            </label>
            <input
              type="text"
              id="citizenId"
              name="citizen_id"
              value={formData.citizen_id}
              onChange={handleChange}
              required
              className="appearance-none block w-full px-4 py-3 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring focus:ring-orange-500 focus:border-orange-500 sm:text-sm bg-[#2D2D2D] text-[#D1D5DB]"
            />
          </div>

          <div className="mb-4">
            <label htmlFor="rationCardId" className="block mb-2">
              Ration Card ID:<span className="text-red-500">*</span>
            </label>
            <input
              type="text"
              id="rationCardId"
              name="ration_card_id"
              value={formData.ration_card_id}
              onChange={handleChange}
              required
              className="appearance-none block w-full px-4 py-3 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring focus:ring-orange-500 focus:border-orange-500 sm:text-sm bg-[#2D2D2D] text-[#D1D5DB]"
            />
          </div>

          {/* Location Pin (spanning both columns) */}
          <div className="col-span-2 mb-4">
            <label htmlFor="locationPin" className="block mb-2">
              Location Pin:<span className="text-red-500">*</span>
            </label>
            <input
              type="text"
              id="locationPin"
              name="location_pin"
              value={formData.location_pin}
              onChange={handleChange}
              required
              pattern="^\d{6}$"
              className="appearance-none block w-full px-4 py-3 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring focus:ring-orange-500 focus:border-orange-500 sm:text-sm bg-[#2D2D2D] text-[#D1D5DB]"
              placeholder="Enter 6-digit Location Pin"
            />
          </div>

          <div className="mb-4">
            <label htmlFor="rationShopId" className="block mb-2">Ration Shop ID:</label>
            <input
              type="text"
              id="rationShopId"
              name="ration_shop_id"
              value={formData.ration_shop_id || 'Not allocated yet'} // Fallback text
              readOnly
              className="appearance-none block w-full px-4 py-3 rounded-md bg-gray-200 text-gray-600"
            />
          </div>

          <div className="mb-4">
            <label htmlFor="diagnosticCenter" className="block mb-2">Diagnostic Center:</label>
            <input
              type="text"
              id="diagnosticCenter"
              name="diagnostic_center"
              value={formData.diagnostic_center || 'Not allocated yet'} // Fallback text
              readOnly
              className="appearance-none block w-full px-4 py-3 rounded-md bg-gray-200 text-gray-600"
            />
          </div>

          <div className="mb-4">
            <label htmlFor="name" className="block mb-2">
              Name:<span className="text-red-500">*</span>
            </label>
            <input
              type="text"
              id="name"
              name="name"
              value={formData.name}
              onChange={handleChange}
              required
              className="appearance-none block w-full px-4 py-3 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring focus:ring-orange-500 focus:border-orange-500 sm:text-sm bg-[#2D2D2D] text-[#D1D5DB]"
            />
          </div>

          <div className="mb-4">
            <label htmlFor="sex" className="block mb-2">
              Sex:<span className="text-red-500">*</span>
            </label>
            <select
              id="sex"
              name="sex"
              value={formData.sex}
              onChange={handleChange}
              required
              className="appearance-none block w-full px-4 py-3 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring focus:ring-orange-500 focus:border-orange-500 sm:text-sm bg-[#2D2D2D] text-[#D1D5DB]"
            >
              <option value="">Select Sex</option>
              <option value="Male">Male</option>
              <option value="Female">Female</option>
              <option value="Other">Other</option>
            </select>
          </div>

          <div className="mb-4">
            <label htmlFor="dob" className="block mb-2">
              Date of Birth:<span className="text-red-500">*</span>
            </label>
            <input
              type="date"
              id="dob"
              name="dob"
              value={formData.dob}
              onChange={handleChange}
              required
              className="appearance-none block w-full px-4 py-3 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring focus:ring-orange-500 focus:border-orange-500 sm:text-sm bg-[#2D2D2D] text-[#D1D5DB]"
            />
          </div>

          <div className="mb-4">
            <label htmlFor="contactNumber" className="block mb-2">
              Contact Number:<span className="text-red-500">*</span>
            </label>
            <input
              type="text"
              id="contactNumber"
              name="contact_number"
              value={formData.contact_number}
              onChange={handleChange}
              required
              className="appearance-none block w-full px-4 py-3 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring focus:ring-orange-500 focus:border-orange-500 sm:text-sm bg-[#2D2D2D] text-[#D1D5DB]"
            />
          </div>

          <div className="col-span-2 mb-4">
            <label htmlFor="address" className="block mb-2">
              Address:<span className="text-red-500">*</span>
            </label>
            <input
              type="text"
              id="address"
              name="address"
              value={formData.address}
              onChange={handleChange}
              required
              className="appearance-none block w-full px-4 py-3 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring focus:ring-orange-500 focus:border-orange-500 sm:text-sm bg-[#2D2D2D] text-[#D1D5DB]"
            />
          </div>

          <div className="col-span-2 mb-4">
            <label htmlFor="incomeLevel" className="block mb-2">
              Income Level:<span className="text-red-500">*</span>
            </label>
            <select
              id="incomeLevel"
              name="income_level"
              value={formData.income_level}
              onChange={handleChange}
              className="appearance-none block w-full px-4 py-3 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring focus:ring-orange-500 focus:border-orange-500 sm:text-sm bg-[#2D2D2D] text-[#D1D5DB]"
            >
              <option value="Low">Low</option>
              <option value="Medium">Medium</option>
              <option value="High">High</option>
            </select>
          </div>

          <div className="col-span-2">
            <button
              type="submit"
              className="mt-4 w-full px-4 py-2 bg-orange-600 text-white font-semibold rounded-md hover:bg-orange-700 transition"
            >
              Add Citizen
            </button>
          </div>
        </form>
      </div>
    </div>
  );
};

export default AddUser;
