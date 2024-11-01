import React, { useEffect, useState } from 'react';

const ChangePassDiag = () => {
  const [admin, setAdmin] = useState(null);
  const [currentPassword, setCurrentPassword] = useState('');
  const [newPassword, setNewPassword] = useState('');
  const [confirmPassword, setConfirmPassword] = useState('');
  const [error, setError] = useState('');
  const [success, setSuccess] = useState('');

  useEffect(() => {
    // Retrieve admin data from local storage
    const username = localStorage.getItem('username');
    setAdmin(username);
  }, []);

  const handleChangePassword = async (e) => {
    e.preventDefault();
    setError('');
    setSuccess('');

    if (!admin) {
      setError('Admin not logged in. Please log in first.');
      return;
    }

    // Check if newPassword matches confirmPassword
    if (newPassword !== confirmPassword) {
      setError('New password and confirm password do not match.');
      return;
    }

    // Call your backend API to change the password
    try {
      const response = await fetch('http://localhost:5000/diag/change_password', {
        method: 'PUT',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          username:admin ,
          currentPassword,
          newPassword,
        }),
      });

      if (!response.ok) {
        const errorResponse = await response.json();
        setError(errorResponse.message || 'Failed to change password.');
        return;
      }

      setSuccess('Password changed successfully.');
      // Clear the fields after successful change
      setCurrentPassword('');
      setNewPassword('');
      setConfirmPassword('');
    } catch (error) {
      setError('An error occurred. Please try again later.');
    }
  };

  return (
    <div className="flex  flex-col justify-start sm:px-6 lg:px-8 " style={{ fontFamily: '"Mona Sans", "Helvetica Neue", Helvetica, Arial, sans-serif' }}>
      <div className="sm:mx-auto sm:w-full sm:max-w-md">
        <h2 className="mt-6 text-center text-3xl font-extrabold text-[#D1D5DB]">
          Change Password
        </h2>
      </div>

      <div className="mt-8 rounded-2xl bg-[#1D1D1D] sm:mx-auto sm:w-full sm:max-w-md z-10">
        <div className="bg-[#1D1D1D] py-8 px-6 shadow-lg rounded-lg">
          <form className="space-y-6" onSubmit={handleChangePassword}>
            <div>
              <label htmlFor="current-password" className="block text-sm font-medium text-[#D1D5DB]">
                Current Password
              </label>
              <div className="mt-1">
                <input
                  id="current-password"
                  name="current-password"
                  type="password"
                  required
                  className="appearance-none block w-full px-4 py-3 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring focus:ring-orange-500 focus:border-orange-500 sm:text-sm bg-[#2D2D2D] text-[#D1D5DB]"
                  value={currentPassword}
                  onChange={(e) => setCurrentPassword(e.target.value)}
                  placeholder="Enter your current password"
                />
              </div>
            </div>

            <div>
              <label htmlFor="new-password" className="block text-sm font-medium text-[#D1D5DB]">
                New Password
              </label>
              <div className="mt-1">
                <input
                  id="new-password"
                  name="new-password"
                  type="password"
                  required
                  className="appearance-none block w-full px-4 py-3 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring focus:ring-orange-500 focus:border-orange-500 sm:text-sm bg-[#2D2D2D] text-[#D1D5DB]"
                  value={newPassword}
                  onChange={(e) => setNewPassword(e.target.value)}
                  placeholder="Enter your new password"
                />
              </div>
            </div>

            <div>
              <label htmlFor="confirm-password" className="block text-sm font-medium text-[#D1D5DB]">
                Confirm New Password
              </label>
              <div className="mt-1">
                <input
                  id="confirm-password"
                  name="confirm-password"
                  type="password"
                  required
                  className="appearance-none block w-full px-4 py-3 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring focus:ring-orange-500 focus:border-orange-500 sm:text-sm bg-[#2D2D2D] text-[#D1D5DB]"
                  value={confirmPassword}
                  onChange={(e) => setConfirmPassword(e.target.value)}
                  placeholder="Confirm your new password"
                />
              </div>
            </div>

            {error && (
              <div className="bg-red-600 text-white p-3 rounded-md text-sm font-semibold text-center mt-4">
                {error}
              </div>
            )}

            {success && (
              <div className="bg-green-600 text-white p-3 rounded-md text-sm font-semibold text-center mt-4">
                {success}
              </div>
            )}

            <div>
              <button
                type="submit"
                className="w-full cursor-pointer flex justify-center py-3 px-4 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-orange-600 hover:bg-orange-700 transition duration-150 ease-in-out focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-orange-500"
              >
                Change Password
              </button>
            </div>
          </form>
        </div>
      </div>
    </div>
  );
};

export default ChangePassDiag;
