import React, { useState, useEffect } from 'react';
import axios from 'axios';

const ManageCenters = () => {
  const [diagnosticCenters, setDiagnosticCenters] = useState([]);
  const [newUser, setNewUser] = useState({ centerId: '', username: '', password: '', role: 'diag' });
  const [viewUsersId, setViewUsersId] = useState(null);
  const [addUserCenterId, setAddUserCenterId] = useState(null);
  const [users, setUsers] = useState([]);
  const [activeAction, setActiveAction] = useState(null);
  const [searchTerm, setSearchTerm] = useState('');
  
  // Pagination state
  const [currentPage, setCurrentPage] = useState(1);
  const [centersPerPage] = useState(5); // Number of centers per page
  const totalCenters = diagnosticCenters.length;

  // Options for the Select component
  const centerOptions = diagnosticCenters.map(center => ({
    value: center.center_id,
    label: `${center.address} - ${center.center_id}`,
  }));

  // Fetch diagnostic centers when the component mounts
  useEffect(() => {
    const fetchDiagnosticCenters = async () => {
      try {
        const response = await axios.get('http://localhost:5000/get_diagnostic_centers');
        console.log(response.data); // Log the response data for debugging

        // Check if the response data contains a 'centers' property
        if (response.data.centers && Array.isArray(response.data.centers)) {
          setDiagnosticCenters(response.data.centers);
        } else {
          console.error('Unexpected response format:', response.data);
        }
      } catch (error) {
        console.error('Failed to fetch diagnostic centers:', error);
      }
    };

    fetchDiagnosticCenters();
  }, []);

  // Handle user addition
  const handleAddUser = async (e) => {
    e.preventDefault();
    try {
      const userData = {
        ...newUser,
        centerId: addUserCenterId,
      };
      const response = await axios.post('http://localhost:5000/add_username', userData);
      alert(response.data.message);
      setNewUser({ centerId: '', username: '', password: '', role: 'diag' });
      setAddUserCenterId(null);
      setActiveAction(null);
      if (viewUsersId) fetchUsers(viewUsersId);
    } catch (error) {
      console.error('Failed to add user:', error);
    }
  };

  // Handle center deletion
  const handleDeleteCenter = async (centerId) => {
    if (window.confirm('Are you sure you want to delete this center?')) {
      try {
        const response = await axios.delete(`http://localhost:5000/delete_diagnostic_center/${centerId}`);
        alert(response.data.message);
        
        // Refresh the whole page after deletion
        window.location.reload();
      } catch (error) {
        console.error('Failed to delete center:', error);
      }
    }
  };

  // Fetch users for a specific center
  const fetchUsers = async (centerId) => {
    try {
      const response = await axios.get(`http://localhost:5000/get_diag/${centerId}`);
      if (Array.isArray(response.data.users)) {
        setUsers(response.data.users); 
      } else {
        console.error('Unexpected response format for users:', response.data);
      }
    } catch (error) {
      console.error('Failed to fetch users:', error);
    }
  };

  // Handle view users action
  const handleViewUsers = (centerId) => {
    setViewUsersId(centerId);
    fetchUsers(centerId);
    setActiveAction('view');
    setAddUserCenterId(null);
  };

  // Handle adding user action
  const handleAddUserAction = (centerId) => {
    setAddUserCenterId(centerId);
    setActiveAction('add');
    setViewUsersId(null);
  };

  // Handle user deletion
  const handleDeleteUser = async (userId) => {
    if (window.confirm('Are you sure you want to delete this user?')) {
      try {
        const response = await axios.delete(`http://localhost:5000/delete_diag/${userId}`);
        alert(response.data.message);
        
        // Refresh the user list after deletion
        if (viewUsersId) fetchUsers(viewUsersId);
      } catch (error) {
        console.error('Failed to delete user:', error);
        alert('An error occurred while trying to delete the user.');
      }
    }
  };

  // Handle search
  const filteredCenters = diagnosticCenters.filter(center =>
    center.address.toLowerCase().includes(searchTerm.toLowerCase()) ||
    center.location_pin.toString().includes(searchTerm) ||
    center.contact_number.includes(searchTerm) ||
    center.center_id.toString().includes(searchTerm)
  );

  // Pagination logic
  const indexOfLastCenter = currentPage * centersPerPage;
  const indexOfFirstCenter = indexOfLastCenter - centersPerPage;
  const currentCenters = filteredCenters.slice(indexOfFirstCenter, indexOfLastCenter);

  const totalPages = Math.ceil(filteredCenters.length / centersPerPage);

  return (
    <div className="flex justify-center items-start h-screen">
      <div className="bg-[#4d4d4d] bg-opacity-30 backdrop-filter backdrop-blur-lg rounded-xl shadow-2xl p-8 w-full max-w-4xl">
        <h2 className="text-3xl font-semibold mb-4 text-center">Manage Diagnostic Centers</h2>
        
        {/* Search input */}
        <div className="mb-4">
          <input 
            type="text" 
            placeholder="Search by address, pin, contact, or center ID" 
            value={searchTerm}
            onChange={(e) => setSearchTerm(e.target.value)}
            className="border border-gray-300 px-4 py-2 w-full bg-[#1d1d1d] text-white"
          />
        </div>

        <table className="min-w-full bg-[#1d1d1d] border border-gray-300 mb-4">
          <thead>
            <tr>
              <th className="py-2 px-4 text-center">Center ID</th>
              <th className="py-2 px-4 text-center">Address</th>
              <th className="py-2 px-4 text-center">Location Pin</th>
              <th className="py-2 px-4 text-center">Contact Number</th>
              <th className="py-2 px-44 text-center">Actions</th>
            </tr>
          </thead>
          <tbody>
            {currentCenters.map(center => (
              <tr key={center.center_id}>
                <td className="border border-gray-300 py-2 px-4 text-center">{center.center_id}</td>
                <td className="border border-gray-300 py-2 px-4 text-center">{center.address}</td>
                <td className="border border-gray-300 py-2 px-4 text-center">{center.location_pin}</td>
                <td className="border border-gray-300 py-2 px-4 text-center">{center.contact_number}</td>
                <td className="border border-gray-300 py-2 px-4 text-center">
                  <button 
                    onClick={() => handleDeleteCenter(center.center_id)} 
                    className="bg-red-500 text-white px-4 py-2 rounded mr-2"
                  >
                    Delete
                  </button>
                  <button 
                    onClick={() => handleViewUsers(center.center_id)} 
                    className="bg-blue-500 text-white px-4 py-2 rounded mr-2"
                  >
                    View Users
                  </button>
                  <button 
                    onClick={() => handleAddUserAction(center.center_id)} 
                    className="bg-green-500 text-white px-4 py-2 rounded"
                  >
                    Add User
                  </button>
                </td>
              </tr>
            ))}
          </tbody>
        </table>

        {activeAction === 'view' && viewUsersId && (
          <div>
            <h3 className="text-xl mt-6 mb-2">Users for Center ID: {viewUsersId}</h3>
            <table className="min-w-full bg-[#1d1d1d] border border-gray-300 mb-4">
              <thead>
                <tr>
                  <th className="py-2 px-4 text-center">Username</th>
                  <th className="py-2 px-4 text-center">Password</th>
                  <th className="py-2 px-4 text-center">Last Login</th>
                  <th className="py-2 px-4 text-center">Action</th>
                </tr>
              </thead>
              <tbody>
                {users.map(user => (
                  <tr key={user.id}>
                    <td className="border border-gray-300 py-2 px-4 text-center">{user.username}</td>
                    <td className="border border-gray-300 py-2 px-4 text-center">{user.password}</td>
                    <td className="border border-gray-300 py-2 px-4 text-center">{user.last_login}</td>
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

        {activeAction === 'add' && addUserCenterId && (
          <div className="mt-6">
            <h3 className="text-xl mb-2">Add User for Center ID: {addUserCenterId}</h3>
            <form onSubmit={handleAddUser}>
              <div className="mb-4">
                <label className="block mb-2 text-white">Username:</label>
                <input 
                  type="text" 
                  value={newUser.username}
                  onChange={(e) => setNewUser({ ...newUser, username: e.target.value })}
                  className="border border-gray-300 px-4 py-2 w-full bg-[#1d1d1d] text-white"
                />
              </div>
              <div className="mb-4">
                <label className="block mb-2 text-white">Password:</label>
                <input 
                  type="password" 
                  value={newUser.password}
                  onChange={(e) => setNewUser({ ...newUser, password: e.target.value })}
                  className="border border-gray-300 px-4 py-2 w-full bg-[#1d1d1d] text-white"
                />
              </div>
              
              <button type="submit" className="bg-blue-500 text-white px-4 py-2 rounded">Add User</button>
            </form>
          </div>
        )}

        {/* Pagination Controls */}
        <div className="flex justify-between items-center mt-6">
          <button 
            onClick={() => setCurrentPage(currentPage - 1)} 
            disabled={currentPage === 1} 
            className="bg-gray-500 text-white px-4 py-2 rounded hover:bg-blue-500"
          >
            Previous
          </button>
          <span className="text-white">Page {currentPage} of {totalPages}</span>
          <button 
            onClick={() => setCurrentPage(currentPage + 1)} 
            disabled={currentPage === totalPages} 
            className="bg-gray-500 text-white px-4 py-2 rounded hover:bg-blue-500"
          >
            Next
          </button>
        </div>
      </div>
    </div>
  );
};

export default ManageCenters;
