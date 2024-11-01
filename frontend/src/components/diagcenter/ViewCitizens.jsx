import React, { useEffect, useState } from 'react';
import placeholderImage from '../../assets/images.jpeg'; 
import india from '../../assets/india.webp'; 
import './ViewCitizens.css';
import CitizenVisuals from './CitizenVisuals';

const ViewCitizens = () => {
  const [citizens, setCitizens] = useState([]);
  const [filteredCitizens, setFilteredCitizens] = useState([]);
  const [loading, setLoading] = useState(true);
  const [searchTerm, setSearchTerm] = useState('');
  const [selectedCitizen, setSelectedCitizen] = useState(null);
  const [nutritionData, setNutritionData] = useState([]);
  const diagnosticCenterId = localStorage.getItem('centerid');

  useEffect(() => {
    const fetchCitizens = async () => {
      try {
        const response = await fetch(`http://localhost:5000/get_citizens?diagnostic_center_id=${diagnosticCenterId}`);
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        const data = await response.json();
        setCitizens(data);
        setFilteredCitizens(data);
      } catch (error) {
        console.error('Error fetching citizens:', error);
      } finally {
        setLoading(false);
      }
    };

    fetchCitizens();
  }, [diagnosticCenterId]);

  const handleSearchChange = (event) => {
    setSearchTerm(event.target.value);
    const lowerCaseSearchTerm = event.target.value.toLowerCase();
  
    const filtered = citizens.filter((citizen) => 
      Object.values(citizen).some(
        (value) =>
          value &&
          value.toString().toLowerCase().includes(lowerCaseSearchTerm)
      )
    );
  
    setFilteredCitizens(filtered);
  };

  const handleCitizenSelect = async (citizen) => {
    setSelectedCitizen(citizen);

    try {
      const response = await fetch(`http://localhost:5000/nutrition_data?citizen_id=${citizen.citizen_id}`);
      if (!response.ok) {
        throw new Error('Network response was not ok');
      }
      const data = await response.json();
      setNutritionData(data);
    } catch (error) {
      console.error('Error fetching nutrition data:', error);
    }
  };
  const handleViewPDF = async (reportId) => {
    try {
        const response = await fetch(`http://localhost:5000/ViewPDF?report_id=${reportId}`, {
            method: 'GET',
        });
        if (response.ok) {
            const data = await response.json();
            const blobData = data.blob_data;

            const byteCharacters = atob(blobData);
            const byteNumbers = new Uint8Array(byteCharacters.length);
            for (let i = 0; i < byteCharacters.length; i++) {
                byteNumbers[i] = byteCharacters.charCodeAt(i);
            }
            const blob = new Blob([byteNumbers], { type: 'application/pdf' });

            const url = URL.createObjectURL(blob);

            const newTab = window.open(url, '_blank');
            if (newTab) {
              newTab.document.title="Report" 
            } else {
                console.error('Failed to open new tab. Please allow pop-ups.');
            }
        } else {
            console.error('Failed to fetch PDF');
        }
    } catch (error) {
        console.error('Error generating PDF:', error);
    }
};

  const handleBack = () => {
    setSelectedCitizen(null);
    setNutritionData([]);
  };

  if (loading) {
    return <div>Loading...</div>;
  }

  return (
    <div className="mt-4 z-40">
      <h3 className="text-xl font-semibold mb-4 text-white text-center">Citizen Records</h3>

      {selectedCitizen ? (
        <div>
          <div className="mt-4 flex justify-center">
            <div className="bg-gradient-to-r from-[#1d1d1d] to-[#5d5d5d] p-6 rounded-md shadow-lg w-full max-w-2xl flex">
              <div className="w-2/3 pl-6">
                <div className='flex items-center mb-3 justify-end'>
                  <img src={india} alt="Citizen" className="w-[50px] h-[50px] mb-5 rounded-3xl my-auto" /> 
                  <p className='ml-5 font-serif italic text-xl'>Government of INDIA</p>
                </div>
                <p className='mb-2 text-lg'><strong>Citizen ID:</strong> {selectedCitizen.citizen_id}</p>
                <p className='mb-2 text-lg'><strong>Ration Card ID:</strong> {selectedCitizen.ration_card_id}</p>
                <p className='mb-2 text-lg'><strong>Name:</strong> {selectedCitizen.name}</p>
                <p className='mb-2 text-lg'><strong>Sex:</strong> {selectedCitizen.sex}</p>
                <p className='mb-2 text-lg'><strong>DOB:</strong> {new Date(selectedCitizen.dob).toLocaleDateString()}</p>
                <p className='mb-2 text-lg'><strong>Address:</strong> {selectedCitizen.address}, {selectedCitizen.location_pin}</p>
                <p className='mb-2 text-lg'><strong>Contact Number:</strong> {selectedCitizen.contact_number}</p>
              </div>
              <div className="w-1/3 text-center">
              <br></br><br></br><br></br>
                <img src={placeholderImage} alt="Citizen" className="w-[150px] h-[150px] mb-5 rounded-3xl mx-auto" />
                <p className='mb-2 text-lg'><strong>Ration: </strong> {selectedCitizen.ration_shop_id}</p>
                <p className='mb-2 text-lg'><strong>Diagnostic: </strong> {diagnosticCenterId}</p>
              </div>
            </div>
          </div>

          <h4 className="mt-4 text-xl font-semibold text-center text-white mb-2">Nutrition Reports</h4>
          <div className="overflow-auto max-h-[300px]">
            <table className="w-2/3 bg-transparent border-collapse border border-gray-200 rounded-xl shadow-lg mx-auto">
              <thead>
                <tr className="bg-[#2D2D2D] text-white">
                  <th className="py-2 px-4 border border-gray-300">Report ID</th>
                  <th className="py-2 px-4 border border-gray-300">Report Date</th>
                  <th className="py-2 px-4 border border-gray-300">Action</th>
                </tr>
              </thead>
              <tbody>
  {nutritionData.length > 0 ? (
    nutritionData.map((report, index) => (
      <tr key={index} className={index % 2 === 0 ? 'bg-[#4d4d4d]' : 'bg-[#3d3d3d]'}>
        <td className="py-2 px-4 border border-gray-300 text-white text-center">{report.report_id}</td>
        <td className="py-2 px-4 border border-gray-300 text-white text-center">
          {new Date(report.report_date).toLocaleDateString()}
        </td>
        <td className="py-2 px-4 border border-gray-300 text-center">
          <button
            className="px-2 py-1 bg-green-600 text-white rounded-md hover:bg-green-700"
            onClick={() => handleViewPDF(report.report_id)}
          >
            View PDF
          </button>
        </td>
      </tr>
    ))
  ) : (
    <tr>
      <td colSpan="3" className="py-2 px-4 border border-gray-300 text-center text-white">NO REPORT FOUND</td>
    </tr>
  )}
</tbody>

            </table>

            <CitizenVisuals citizen_id={selectedCitizen.citizen_id}/>

          </div>

          <div className="flex justify-center">
            <button
              onClick={handleBack}
              className="mt-6 w-1/4 px-4 py-2 bg-orange-600 text-white font-semibold rounded-lg hover:bg-orange-700 transition"
            >
              Back to Citizens
            </button>
          </div>
        </div>
      ) : (
        <div>
          <div className="flex justify-center mb-12">
            <input
              type="text"
              placeholder="Search..."
              value={searchTerm}
              onChange={handleSearchChange}
              className="p-2 pl-4 border border-gray-400 rounded-lg w-1/2 outline-none transition duration-200 ease-in-out transform focus:border-blue-400 focus:shadow-lg focus:scale-105"
              style={{
                backgroundColor: '#2D2D2D',
                color: 'white',
                boxShadow: '0px 4px 10px rgba(0, 0, 0, 0.2)',
              }}
            />
          </div>
          <div className="overflow-auto max-h-[600px] max-w-6xl mx-auto">
            <table className="w-full bg-transparent border-collapse border border-gray-200 rounded-xl rounded-r-none overflow-hidden shadow-lg">
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
                {filteredCitizens.length > 0 ? (
                  filteredCitizens.map((citizen, index) => (
                    <tr
                      key={index}
                      className={`${index % 2 === 0 ? 'bg-[#4d4d4d]' : 'bg-[#3d3d3d]'}`}
                    >
                      <td className="py-2 px-4 border border-gray-300 text-white text-center">{index + 1}</td>
                      <td className="py-2 px-4 border border-gray-300 text-white text-center">{citizen.citizen_id}</td>
                      <td className="py-2 px-4 border border-gray-300 text-white text-center">{citizen.ration_card_id}</td>
                      <td className="py-2 px-4 border border-gray-300 text-white text-center">{citizen.name}</td>
                      <td className="py-2 px-4 border border-gray-300 text-white text-center">{citizen.sex}</td>
                      <td className="py-2 px-4 border border-gray-300 text-white text-center">
                        {new Date(citizen.dob).toLocaleDateString()}
                      </td>
                      <td className="py-2 px-4 border border-gray-300 text-white text-center">{citizen.address}</td>
                      <td className="py-2 px-4 border border-gray-300 text-white text-center">
                        <button
                          className="px-2 py-1 bg-blue-600 text-white rounded-md hover:bg-blue-700"
                          onClick={() => handleCitizenSelect(citizen)}
                        >
                          View Details
                        </button>
                      </td>
                    </tr>
                  ))
                ) : (
                  <tr>
                    <td colSpan="8" className="py-2 px-4 border border-gray-300 text-center">
                      No citizens found.
                    </td>
                  </tr>
                )}
              </tbody>
            </table>
          </div>
        </div>
      )}

    </div>
  );
};

export default ViewCitizens;
