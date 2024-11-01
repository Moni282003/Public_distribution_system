import React, { useState, useEffect } from 'react';
import axios from 'axios';
import placeholderImage from '../../../assets/images.jpeg';
import india from '../../../assets/india.webp';

const ViewUsers = () => {
  const statesData = {
    "states": [
      {
        "name": "Andhra Pradesh",
        "pin_code_range": {
            "min": "500001",
            "max": "534450"
        }
    },
    {
        "name": "Arunachal Pradesh",
        "pin_code_range": {
            "min": "791001",
            "max": "791119"
        }
    },
    {
        "name": "Assam",
        "pin_code_range": {
            "min": "780001",
            "max": "788931"
        }
    },
    {
        "name": "Bihar",
        "pin_code_range": {
            "min": "800001",
            "max": "855117"
        }
    },
    {
        "name": "Chhattisgarh",
        "pin_code_range": {
            "min": "490001",
            "max": "494999"
        }
    },
    {
        "name": "Goa",
        "pin_code_range": {
            "min": "403001",
            "max": "403516"
        }
    },
    {
        "name": "Gujarat",
        "pin_code_range": {
            "min": "360001",
            "max": "396993"
        }
    },
    {
        "name": "Haryana",
        "pin_code_range": {
            "min": "121001",
            "max": "134204"
        }
    },
    {
        "name": "Himachal Pradesh",
        "pin_code_range": {
            "min": "171001",
            "max": "175175"
        }
    },
    {
        "name": "Jharkhand",
        "pin_code_range": {
            "min": "816001",
            "max": "828119"
        }
    },
    {
        "name": "Karnataka",
        "pin_code_range": {
            "min": "560001",
            "max": "577999"
        }
    },
    {
        "name": "Kerala",
        "pin_code_range": {
            "min": "670001",
            "max": "689999"
        }
    },
    {
        "name": "Madhya Pradesh",
        "pin_code_range": {
            "min": "450001",
            "max": "499999"
        }
    },
    {
        "name": "Maharashtra",
        "pin_code_range": {
            "min": "400001",
            "max": "444999"
        }
    },
    {
        "name": "Manipur",
        "pin_code_range": {
            "min": "795001",
            "max": "795999"
        }
    },
    {
        "name": "Meghalaya",
        "pin_code_range": {
            "min": "793001",
            "max": "793999"
        }
    },
    {
        "name": "Mizoram",
        "pin_code_range": {
            "min": "796001",
            "max": "796999"
        }
    },
    {
        "name": "Nagaland",
        "pin_code_range": {
            "min": "797001",
            "max": "797999"
        }
    },
    {
        "name": "Odisha",
        "pin_code_range": {
            "min": "751001",
            "max": "769999"
        }
    },
    {
        "name": "Punjab",
        "pin_code_range": {
            "min": "140001",
            "max": "152001"
        }
    },
    {
        "name": "Rajasthan",
        "pin_code_range": {
            "min": "302001",
            "max": "344999"
        }
    },
    {
        "name": "Sikkim",
        "pin_code_range": {
            "min": "737001",
            "max": "737511"
        }
    },
    {
        "name": "Tamil Nadu",
        "pin_code_range": {
            "min": "600001",
            "max": "641999"
        }
    },
    {
        "name": "Telangana",
        "pin_code_range": {
            "min": "500001",
            "max": "509999"
        }
    },
    {
        "name": "Tripura",
        "pin_code_range": {
            "min": "799001",
            "max": "799999"
        }
    },
    {
        "name": "Uttar Pradesh",
        "pin_code_range": {
            "min": "201001",
            "max": "284999"
        }
    },
    {
        "name": "Uttarakhand",
        "pin_code_range": {
            "min": "246001",
            "max": "249999"
        }
    },
    {
        "name": "West Bengal",
        "pin_code_range": {
            "min": "700001",
            "max": "743999"
        }
    }
    ]
};

const [filters, setFilters] = useState({
  ration_shop_id: '',
  diagnostic_center_id: '',
  location_pin: '',
  state: ''
});
const [searchId, setSearchId] = useState('');
const [citizens, setCitizens] = useState([]);
const [selectedCitizen, setSelectedCitizen] = useState(null);
const [error, setError] = useState('');
const [rationShopOptions, setRationShopOptions] = useState([]);
const [diagnosticCenterOptions, setDiagnosticCenterOptions] = useState([]);
const [locationPinOptions, setLocationPinOptions] = useState([]);

const stateOptions = statesData.states.map(state => state.name);

const getStateByLocationPin = (pin) => {
  return statesData.states.find(state => {
    const pinCode = parseInt(pin, 10);
    return pinCode >= parseInt(state.pin_code_range.min) && pinCode <= parseInt(state.pin_code_range.max);
  })?.name || '';
};

const filteredCitizens = citizens.filter(citizen => {
  const citizenPinState = getStateByLocationPin(citizen.location_pin);
  return (
    citizen.citizen_id.toString().includes(searchId) &&
    (!filters.state || citizenPinState === filters.state)
  );
});

useEffect(() => {
  const fetchOptions = async () => {
    try {
      const rationShopResponse = await axios.get('http://localhost:5000/unique_ration_shops');
      setRationShopOptions(rationShopResponse.data);

      const diagnosticCenterResponse = await axios.get('http://localhost:5000/unique_diagnostic_centers');
      setDiagnosticCenterOptions(diagnosticCenterResponse.data);

      const locationPinResponse = await axios.get('http://localhost:5000/unique_location_pins');
      setLocationPinOptions(locationPinResponse.data);
    } catch (error) {
      console.error('Error fetching dropdown options:', error);
    }
  };

  fetchOptions();
}, []);

const handleChange = (e) => {
  const { name, value } = e.target;
  setFilters((prev) => ({ ...prev, [name]: value }));
};

const handleSubmit = async (e) => {
  e.preventDefault();
  setError('');
  try {
    const response = await axios.get('http://localhost:5000/view_citizens', { params: filters });
    setCitizens(response.data);
  } catch (err) {
    setError('Error fetching citizens: ' + (err.response?.data?.error || err.message));
  }
};

const handleCitizenSelect = (citizen) => {
  setSelectedCitizen(citizen);
};

const handleBack = () => {
  setSelectedCitizen(null);
};

return (
  <div className="flex justify-center items-start h-screen">
    <div className="bg-[#4d4d4d] bg-opacity-30 backdrop-filter backdrop-blur-lg rounded-xl shadow-2xl p-8 w-full max-w-4xl">
      <h2 className="text-3xl font-semibold mb-4 text-center">View Citizens</h2>

      {!selectedCitizen ? (
        <>
          <form onSubmit={handleSubmit} className="grid grid-cols-2 gap-4">
            <div className="mb-4">
              <label htmlFor="state" className="block mb-2">State:</label>
              <select
                id="state"
                name="state"
                value={filters.state}
                onChange={handleChange}
                className="block w-full px-4 py-3 rounded-md shadow-sm bg-[#2D2D2D] text-[#D1D5DB]"
              >
                <option value="">Select State</option>
                {stateOptions.map((option, index) => (
                  <option key={index} value={option}>{option}</option>
                ))}
              </select>
            </div>

            <div className="mb-4">
              <label htmlFor="ration_shop_id" className="block mb-2">Ration Shop ID:</label>
              <select
                id="ration_shop_id"
                name="ration_shop_id"
                value={filters.ration_shop_id}
                onChange={handleChange}
                className="block w-full px-4 py-3 rounded-md shadow-sm bg-[#2D2D2D] text-[#D1D5DB]"
              >
                <option value="">Select Ration Shop ID</option>
                {rationShopOptions.map((option, index) => (
                  <option key={index} value={option}>{option}</option>
                ))}
              </select>
            </div>

            <div className="mb-4">
              <label htmlFor="diagnostic_center_id" className="block mb-2">Diagnostic Center ID:</label>
              <select
                id="diagnostic_center_id"
                name="diagnostic_center_id"
                value={filters.diagnostic_center_id}
                onChange={handleChange}
                className="block w-full px-4 py-3 rounded-md shadow-sm bg-[#2D2D2D] text-[#D1D5DB]"
              >
                <option value="">Select Diagnostic Center ID</option>
                {diagnosticCenterOptions.map((option, index) => (
                  <option key={index} value={option}>{option}</option>
                ))}
              </select>
            </div>

            <div className="mb-4">
              <label htmlFor="location_pin" className="block mb-2">Location Pin:</label>
              <select
                id="location_pin"
                name="location_pin"
                value={filters.location_pin}
                onChange={handleChange}
                className="block w-full px-4 py-3 rounded-md shadow-sm bg-[#2D2D2D] text-[#D1D5DB]"
              >
                <option value="">Select Location Pin</option>
                {locationPinOptions.map((option, index) => (
                  <option key={index} value={option}>{option}</option>
                ))}
              </select>
            </div>

            <button
              type="submit"
              className="mt-4 col-span-2 px-4 py-2 bg-orange-600 text-white font-semibold rounded-md hover:bg-orange-700 transition"
            >
              View Citizens
            </button>
          </form>

          <div className="mt-4">
            <input
              type="text"
              placeholder="Search by Citizen ID"
              value={searchId}
              onChange={(e) => setSearchId(e.target.value)}
              className="w-full px-4 py-2 mt-4 rounded-md shadow-sm bg-[#2D2D2D] text-[#D1D5DB]"
            />
          </div>

          {error && <p className="text-red-500 mt-4">{error}</p>}

          {filteredCitizens.length > 0 && (
            <div className="mt-8">
              <h3 className="text-2xl font-semibold mb-2">Citizen Records:</h3>
              <div className="overflow-auto max-h-96">
                <table className="min-w-full bg-transparent border-collapse border border-gray-200 rounded-xl">
                  <thead>
                    <tr className="bg-[#2D2D2D] text-white">
                      <th className="py-2 px-4 border border-gray-300">S.No</th>
                      <th className="py-2 px-4 border border-gray-300">Citizen ID</th>
                      <th className="py-2 px-4 border border-gray-300">Ration Card ID</th>
                      <th className="py-2 px-4 border border-gray-300">Name</th>
                      <th className="py-2 px-4 border border-gray-300">Sex</th>
                      <th className="py-2 px-4 border border-gray-300">DOB</th>
                      <th className="py-2 px-4 border border-gray-300">Address</th>
                      <th className="py-2 px-4 border border-gray-300">Actions</th>
                    </tr>
                  </thead>
                  <tbody>
                    {filteredCitizens.map((citizen, index) => (
                      <tr key={index} className="bg-[#4d4d4d]">
                        <td className="py-2 px-4 border border-gray-300">{index + 1}</td>
                        <td className="py-2 px-4 border border-gray-300">{citizen.citizen_id}</td>
                        <td className="py-2 px-4 border border-gray-300">{citizen.ration_card_id}</td>
                        <td className="py-2 px-4 border border-gray-300">{citizen.name}</td>
                        <td className="py-2 px-4 border border-gray-300">{citizen.sex}</td>
                        <td className="py-2 px-4 border border-gray-300">{citizen.dob}</td>
                        <td className="py-2 px-4 border border-gray-300">{citizen.address}</td>
                        <td className="py-2 px-4 border border-gray-300">
                          <button onClick={() => handleCitizenSelect(citizen)} className="text-white hover:underline bg-blue-500">View Details</button>
                        </td>
                      </tr>
                    ))}
                  </tbody>
                </table>
              </div>
            </div>
          )}
        </>
      ) : (
          <div>
          <div className="mt-8 flex justify-center">
          <div className="bg-gradient-to-r from-[#1d1d1d] to-[#5d5d5d] p-6 rounded-lg shadow-lg w-full max-w-4xl flex">
                    <div className="w-2/3 pl-6">
        <div className='flex items-center mb-3 justify-end'>
        <img 
            src={india} 
            alt="Citizen" 
            className="w-[50px] h-[50px] mb-5 rounded-3xl my-auto" 
          /> 
          <p className='ml-5 font-serif italic text-xl'>Government of INDIA</p>
          </div>
          <p className='mb-2 text-lg'><strong>Citizen ID:</strong> {selectedCitizen.citizen_id}</p>
          <p className='mb-2 text-lg'><strong>Ration Card ID:</strong> {selectedCitizen.ration_card_id}</p>
          <p className='mb-2 text-lg'><strong>Name:</strong> {selectedCitizen.name}</p>
          <p className='mb-2 text-lg'><strong>Sex:</strong> {selectedCitizen.sex}</p>
          <p className='mb-2 text-lg'><strong>DOB:</strong> {new Date(selectedCitizen.dob).toLocaleDateString()}</p>
          <p className='mb-2 text-lg'><strong>Address:</strong> {selectedCitizen.address+", "+selectedCitizen.location_pin}</p>
          <p className='mb-2 text-lg'><strong>Contact Number:</strong> {selectedCitizen.contact_number}</p>
        </div>
        <div className="w-1/3"><br></br><br></br><br></br>
        <img 
            src={placeholderImage} 
            alt="Citizen" 
            className="w-[150px] h-[150px] mb-5 rounded-3xl justify-center mx-auto" 
          />          <p className='mb-2 text-lg'><strong>Ration Shop: </strong> {selectedCitizen.ration_shop_id}</p>
          <p className='mb-2 text-lg'><strong>Diagnostic Center: </strong> {selectedCitizen.diagnostic_center_id}</p>
        </div>
      </div>
      
    </div>
    
    <button 
        onClick={handleBack} 
        className="mt-6 w-full px-4 py-2 bg-orange-600 text-white font-semibold rounded-md hover:bg-orange-700 transition"
      >
        Back to Citizens
      </button></div>
        )}
      </div>
    </div>
  );
};

export default ViewUsers;
