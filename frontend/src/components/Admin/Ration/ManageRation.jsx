import React, { useState, useEffect } from 'react';
import axios from 'axios';

const ManageRation = () => {
  const [rationShops, setRationShops] = useState([]);
  const [newUser, setNewUser] = useState({ centerId: '', username: '', password: '', role: "ration" });
  const [viewUsersId, setViewUsersId] = useState(null);
  const [addUserShopId, setAddUserShopId] = useState(null);
  const [users, setUsers] = useState([]);
  const [activeAction, setActiveAction] = useState(null);
  const [searchTerm, setSearchTerm] = useState('');
  const [currentPage, setCurrentPage] = useState(1); // State for current page
  const itemsPerPage = 10; // Number of items per page

  // Fetch ration shops when the component mounts
  useEffect(() => {
    const fetchRationShops = async () => {
      try {
        const response = await axios.get("http://localhost:5000/get_ration_shops");
        setRationShops(response.data);
      } catch (error) {
        console.error("Failed to fetch ration shops:", error);
      }
    };

    fetchRationShops();
  }, []);

  // Handle user addition
  const handleAddUser = async (e) => {
    e.preventDefault();
    try {
      const userData = {
        ...newUser,
        centerId: addUserShopId,
      };
      const response = await axios.post('http://localhost:5000/add_username', userData);
      alert(response.data.message);
      setNewUser({ centerId: '', username: '', password: '', role: "ration" });
      setAddUserShopId(null);
      setActiveAction(null);
      if (viewUsersId) fetchUsers(viewUsersId);
    } catch (error) {
      console.error("Failed to add user:", error);
    }
  };

  // Handle shop deletion
  const handleDeleteShop = async (shopId) => {
    if (window.confirm('Are you sure you want to delete this center?')) {
        try {
          const response = await axios.delete(`http://localhost:5000/delete_ration_shop/${shopId}`);
          alert(response.data.message);
          window.location.reload();
        } catch (error) {
          console.error('Failed to delete center:', error);
        }
      }
  };

  // Fetch users based on selected ration shop
  const fetchUsers = async (centerId) => {
    try {
      const response = await axios.get(`http://localhost:5000/get_users/${centerId}`);
      setUsers(response.data);
    } catch (error) {
      console.error("Failed to fetch users:", error);
    }
  };

  // Handle view users action
  const handleViewUsers = (centerId) => {
    setViewUsersId(centerId);
    fetchUsers(centerId);
    setActiveAction('view');
    setAddUserShopId(null);
  };

  // Handle adding user action
  const handleAddUserAction = (shopId) => {
    setAddUserShopId(shopId);
    setActiveAction('add');
    setViewUsersId(null);
  };

  // Handle user deletion
  const handleDeleteUser = async (userId) => {
    if (window.confirm("Are you sure you want to delete this user?")) {
      try {
        const response = await axios.delete(`http://localhost:5000/delete_user/${userId}`);
        alert(response.data.message);
        if (viewUsersId) fetchUsers(viewUsersId);
      } catch (error) {
        console.error("Failed to delete user:", error);
        alert("An error occurred while trying to delete the user.");
      }
    }
  };

  // Handle search
  const filteredShops = rationShops.filter(shop => 
    shop.address.toLowerCase().includes(searchTerm.toLowerCase()) ||
    shop.location_pin.toString().includes(searchTerm) ||
    shop.contact_number.includes(searchTerm) ||
    shop.shop_id.toString().includes(searchTerm)
  );

  // Pagination logic
  const totalPages = Math.ceil(filteredShops.length / itemsPerPage); // Total pages based on filtered data
  const currentData = filteredShops.slice((currentPage - 1) * itemsPerPage, currentPage * itemsPerPage);

  // Handle page change
  const handlePageChange = (pageNumber) => {
    setCurrentPage(pageNumber);
  };

  return (
    <div className="flex justify-center items-start h-screen">
      <div className="bg-[#4d4d4d] bg-opacity-30 backdrop-filter backdrop-blur-lg rounded-xl shadow-2xl p-8 w-full max-w-4xl">
        <h2 className="text-3xl font-semibold mb-4 text-center">Manage Ration Shops</h2>
        
        {/* Search input */}
        <div className="mb-4">
          <input 
            type="text" 
            placeholder="Search by address, pin, contact, or rationId" 
            value={searchTerm}
            onChange={(e) => setSearchTerm(e.target.value)}
            className="border border-gray-300 px-4 py-2 w-full bg-[#1d1d1d] text-white"
          />
        </div>

        <table className="min-w-full bg-[#1d1d1d] border border-gray-300 mb-4">
          <thead>
            <tr>
              <th className="py-2 px-4 text-center">ID</th>
              <th className="py-2 px-4 text-center">Address</th>
              <th className="py-2 px-4 text-center">Location Pin</th>
              <th className="py-2 px-4 text-center">Contact Number</th>
              <th className="py-2 px-40 text-center">Actions</th>
            </tr>
          </thead>
          <tbody>
            {currentData.map(shop => (
              <tr key={shop.shop_id}>
                <td className="border border-gray-300 py-2 px-4 text-center">{shop.shop_id}</td>
                <td className="border border-gray-300 py-2 px-4 text-center">{shop.address}</td>
                <td className="border border-gray-300 py-2 px-4 text-center">{shop.location_pin}</td>
                <td className="border border-gray-300 py-2 px-4 text-center">{shop.contact_number}</td>
                <td className="border border-gray-300 py-2 px-4 text-center">
                  <button 
                    onClick={() => handleDeleteShop(shop.shop_id)} 
                    className="bg-red-500 text-white px-4 py-2 rounded mr-2"
                  >
                    Delete
                  </button>
                  <button 
                    onClick={() => handleViewUsers(shop.shop_id)} 
                    className="bg-blue-500 text-white px-4 py-2 rounded mr-2"
                  >
                    View Users
                  </button>
                  <button 
                    onClick={() => handleAddUserAction(shop.shop_id)} 
                    className="bg-green-500 text-white px-4 py-2 rounded"
                  >
                    Add User
                  </button>
                </td>
              </tr>
            ))}
          </tbody>
        </table>

        {/* Pagination Controls */}
        <div className="flex justify-center space-x-2 mb-4">
          {[...Array(totalPages)].map((_, index) => (
            <button
              key={index}
              onClick={() => handlePageChange(index + 1)}
              className={`px-4 py-2 rounded ${currentPage === index + 1 ? 'bg-blue-500 text-white' : 'bg-gray-300 text-black'}`}
            >
              {index + 1}
            </button>
          ))}
        </div>

        {activeAction === 'view' && viewUsersId && (
          <div>
            <h3 className="text-xl mt-6 mb-2">Users for Shop ID: {viewUsersId}</h3>
            <table className="min-w-full bg-[#1d1d1d] border border-gray-300 mb-4">
              <thead>
                <tr>
                  <th className="py-2 px-4 text-center">Username</th>
                  <th className="py-2 px-4 text-center">Password</th>
                  <th className="py-2 px-4 text-center">Action</th>
                </tr>
              </thead>
              <tbody>
                {users.map(user => (
                  <tr key={user.id}>
                    <td className="border border-gray-300 py-2 px-4 text-center">{user.username}</td>
                    <td className="border border-gray-300 py-2 px-4 text-center">{user.password}</td>
                    <td className="border border-gray-300 py-2 px-4 text-center">
                      <button 
                        onClick={() => handleDeleteUser(user.id)} 
                        className="bg-red-500 text-white px-4 py-2 rounded"
                      >
                        Delete User
                      </button>
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        )}

        {activeAction === 'add' && addUserShopId && (
          <div>
            <h3 className="text-xl mt-6 mb-2">Add User for Shop ID: {addUserShopId}</h3>
            <form onSubmit={handleAddUser}>
              <input 
                type="text" 
                placeholder="Username" 
                value={newUser.username}
                onChange={(e) => setNewUser({ ...newUser, username: e.target.value })}
                className="border border-gray-300 px-4 py-2 mb-4 w-full bg-[#1d1d1d] text-white"
              />
              <input 
                type="password" 
                placeholder="Password" 
                value={newUser.password}
                onChange={(e) => setNewUser({ ...newUser, password: e.target.value })}
                className="border border-gray-300 px-4 py-2 mb-4 w-full bg-[#1d1d1d] text-white"
              />
              <button type="submit" className="bg-green-500 text-white px-4 py-2 rounded">
                Add User
              </button>
            </form>
          </div>
        )}
      </div>
    </div>
  );
};

export default ManageRation;
