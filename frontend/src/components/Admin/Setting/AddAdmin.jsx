import React, { useState } from 'react';
import axios from 'axios';

const AddAdmin = () => {
  const [formData, setFormData] = useState({
    username: '',
    contact_number: '',
    password: '',
    confirm_password: '',
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData((prevData) => ({
      ...prevData,
      [name]: value,
    }));
  };

  const handleSubmit = (e) => {
    e.preventDefault();

    // Basic validation
    if (formData.password !== formData.confirm_password) {
      alert("Passwords do not match!");
      return;
    }

    axios.post('http://localhost:5000/add_admin', formData)
      .then((response) => {
        alert(response.data.message);
        // Reset form fields
        setFormData({
          username: '',
          contact_number: '',
          password: '',
          confirm_password: '',
        });
      })
      .catch((error) => {
        console.error('Error adding admin:', error);
        alert('Failed to add admin: ' + error.response.data.error);
      });
  };

  return (
    <div className="flex justify-center items-start h-screen">
      <div className="bg-[#4d4d4d] bg-opacity-30 backdrop-filter backdrop-blur-lg rounded-xl shadow-2xl p-8 w-full max-w-4xl">
        <h2 className="text-3xl font-semibold mb-4 text-center">Add Admin</h2>
        <form onSubmit={handleSubmit} className="grid grid-cols-1 sm:grid-cols-2 gap-4">
          <div className="mb-4">
            <label htmlFor="username" className="block mb-2">
              Username: <span className="text-red-500">*</span>
            </label>
            <input
              type="text"
              id="username"
              name="username"
              value={formData.username}
              onChange={handleChange}
              required
              className="appearance-none block w-full px-4 py-3 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring focus:ring-orange-500 focus:border-orange-500 sm:text-sm bg-[#2D2D2D] text-[#D1D5DB]"
            />
          </div>

          <div className="mb-4">
            <label htmlFor="contact_number" className="block mb-2">
              Contact Number: <span className="text-red-500">*</span>
            </label>
            <input
              type="text"
              id="contact_number"
              name="contact_number"
              value={formData.contact_number}
              onChange={handleChange}
              required
              className="appearance-none block w-full px-4 py-3 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring focus:ring-orange-500 focus:border-orange-500 sm:text-sm bg-[#2D2D2D] text-[#D1D5DB]"
            />
          </div>

          <div className="mb-4">
            <label htmlFor="password" className="block mb-2">
              Password: <span className="text-red-500">*</span>
            </label>
            <input
              type="password"
              id="password"
              name="password"
              value={formData.password}
              onChange={handleChange}
              required
              className="appearance-none block w-full px-4 py-3 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring focus:ring-orange-500 focus:border-orange-500 sm:text-sm bg-[#2D2D2D] text-[#D1D5DB]"
            />
          </div>

          <div className="mb-4">
            <label htmlFor="confirm_password" className="block mb-2">
              Confirm Password: <span className="text-red-500">*</span>
            </label>
            <input
              type="password"
              id="confirm_password"
              name="confirm_password"
              value={formData.confirm_password}
              onChange={handleChange}
              required
              className="appearance-none block w-full px-4 py-3 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring focus:ring-orange-500 focus:border-orange-500 sm:text-sm bg-[#2D2D2D] text-[#D1D5DB]"
            />
          </div>

          <button
            type="submit"
            className="mt-4 col-span-2 px-4 py-2 bg-orange-600 text-white font-semibold rounded-md hover:bg-orange-700 transition"
          >
            Add Admin
          </button>
        </form>
      </div>
    </div>
  );
};

export default AddAdmin;
