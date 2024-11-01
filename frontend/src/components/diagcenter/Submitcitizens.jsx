import React, { useState } from 'react';
import { v4 as uuidv4 } from 'uuid';

const SubmitCitizens = () => {
  const [formData, setFormData] = useState({
    report_id: '',
    citizen_id: '',
    center_id: '',
    report_date: '',
    height: '',
    weight: '',
    muac: '',
    iron_level: '',
    vitamin_a: '',
    vitamin_d: '',
    zinc: '',
    folic_acid: '',
    iodine: '',
    blood_glucose: '',
    lipid_profile: '',
    serum_protein: '',
    sodium: '',
    potassium: '',
    calcium: ''
  });

  const [error, setError] = useState('');
  const [isValid, setIsValid] = useState(false);

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({
      ...formData,
      [name]: value
    });
  };

  const centerId = localStorage.getItem('centerid');

  const handleCitizenIdValidation = async (e) => {
    e.preventDefault();
    const { citizen_id } = formData;

    try {
      const response = await fetch(`http://localhost:5000/validate_citizen?id=${citizen_id}`);
      const data = await response.json();

      if (data.exists) {
        // Generate a short report ID with "REP" prefix
        const newReportId = `REP-${uuidv4().split('-')[0]}`; // Get the first segment of the UUID
        const todayDate = new Date().toISOString().split('T')[0]; // Format: YYYY-MM-DD

        setFormData((prevData) => ({
          ...prevData,
          report_id: newReportId,
          report_date: todayDate,
          center_id: centerId 
        }));
        setIsValid(true);
        setError(''); // Clear any previous error
      } else {
        setError('Invalid Citizen ID');
        setIsValid(false);
      }
    } catch (error) {
      console.error('Error validating citizen ID:', error);
      setError('Failed to validate Citizen ID. Please try again.');
    }
  };

  const handleSubmit = async (e) => {
    console.log(formData)
    e.preventDefault();
    try {
      const response = await fetch('http://localhost:5000/submit_nutrition_data', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(formData)
      });

      if (!response.ok) {
        throw new Error('Network response was not ok');
      }
   
      const data = await response.json();
      alert(data.message);
      setFormData({
        report_id: '',
        citizen_id: '',
        center_id: '',
        report_date: '',
        height: '',
        weight: '',
        muac: '',
        iron_level: '',
        vitamin_a: '',
        vitamin_d: '',
        zinc: '',
        folic_acid: '',
        iodine: '',
        blood_glucose: '',
        lipid_profile: '',
        serum_protein: '',
        sodium: '',
        potassium: '',
        calcium: ''
      }); 
      setIsValid(false); // Reset validation state
    } catch (error) {
      console.error('Error submitting nutrition data:', error);
      alert('Failed to submit nutrition data. Please try again.');
    }
  };

  return (
    <div className='z-40 p-4 w-[1100px] mx-auto bg-[#1d1d1d] rounded-xl'>
      <h3 className='text-2xl font-semibold mb-4 text-center text-white bg-orange-600 p-2 rounded-full rounded-tr-none rounded-bl-none'>Submit Nutrition Data</h3>
      <form onSubmit={handleCitizenIdValidation}>
        <div className='mb-4'>
          <label htmlFor='citizen_id' className='block text-gray-200'>
            Citizen ID: <span className='text-red-500'>*</span>
          </label>
          <input
            type='text'
            id='citizen_id'
            name='citizen_id'
            value={formData.citizen_id}
            onChange={handleChange}
            className='p-2 border border-gray-300 bg-[#1d1d1d] text-white rounded w-1/2 outline-none'
            required
            autoComplete="off"
          />
        </div>
        <button type='submit' className='bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-200'>
          Validate Citizen ID
        </button>
      </form>
      {error && <p className='text-red-500'>{error}</p>}
      {isValid && (
        <form onSubmit={handleSubmit} className='mt-4'>
          <div className='grid grid-cols-1 md:grid-cols-2 gap-6'>
            <div className='mb-4'>
              <label htmlFor='report_id' className='block text-gray-200'>
                Report ID: <span className='text-red-500'>*</span>
              </label>
              <input
                type='text'
                id='report_id'
                name='report_id'
                value={formData.report_id}
                onChange={handleChange}
                className='p-2 border border-gray-300 rounded w-full cursor-not-allowed'
                required
                disabled
              />
            </div>
            {/* Center ID */}
            <div className='mb-4'>
              <label htmlFor='center_id' className='block text-gray-200'>
                Center ID: <span className='text-red-500'>*</span>
              </label>
              <input
                type='text'
                id='center_id'
                name='center_id'
                value={formData.center_id}
                onChange={handleChange}
                className='p-2 border border-gray-300 rounded w-full cursor-not-allowed'
                required
                disabled
              />
            </div>
            {/* Report Date */}
            <div className='mb-4'>
              <label htmlFor='report_date' className='block text-gray-200'>
                Report Date: <span className='text-red-500'>*</span>
              </label>
              <input
                type='text'
                id='report_date'
                name='report_date'
                value={formData.report_date}
                onChange={handleChange}
                className='p-2 border border-gray-300 rounded w-full cursor-not-allowed'
                required
                disabled
              />
            </div>
          </div>
  
          {/* Two-column grid for the rest of the fields */}
          <div className='grid grid-cols-1 md:grid-cols-2 gap-6'>
            {Object.keys(formData)
              .filter(key => !['report_id', 'citizen_id', 'center_id', 'report_date', 'bmi', 'stunting', 'wasting'].includes(key))
              .map((key) => {
                let unit = '';
  
                // Determine the unit for each field
                switch (key) {
                  case 'height':
                    unit = 'cm'; // Height in centimeters
                    break;
                  case 'weight':
                    unit = 'kg'; // Weight in kilograms
                    break;
                  case 'muac':
                    unit = 'cm'; // MUAC in centimeters
                    break;
                  case 'iron_level':
                  case 'zinc':
                  case 'iodine':
                    unit = 'µg/dL'; // Micrograms per deciliter
                    break;
                  case 'vitamin_a':
                    unit = 'µg'; // Micrograms
                    break;
                  case 'vitamin_d':
                    unit = 'ng/mL'; // Nanograms per milliliter
                    break;
                  case 'blood_glucose':
                    unit = 'mg/dL'; // Milligrams per deciliter
                    break;
                  case 'lipid_profile':
                    unit = 'mg/dL'; // Milligrams per deciliter
                    break;
                  case 'serum_protein':
                    unit = 'g/dL'; // Grams per deciliter
                    break;
                  case 'sodium':
                  case 'potassium':
                    unit = 'mmol/L'; // Millimoles per liter
                    break;
                  case 'calcium':
                    unit = 'mg/dL'; // Milligrams per deciliter
                    break;
                  case 'folic_acid':
                    unit = 'ng/mL'; // Nanograms per milliliter
                    break;
                  default:
                    unit = ''; // Default case for any unmatched key
                }
  
                return (
                  <div key={key} className='mb-4'>
                    <label htmlFor={key} className='block text-gray-200'>
                      {key.replace(/_/g, ' ').toUpperCase()} ({unit}): <span className='text-red-500'>*</span>
                    </label>
                    <input
                      type='text'
                      id={key}
                      name={key}
                      value={formData[key]}
                      onChange={handleChange}
                      className='p-2 border border-gray-300 bg-[#1d1d1d] text-white rounded w-full'
                      required
                      autoComplete="off"
                    />
                  </div>
                );
              })}
          </div>
          <button type='submit' className='bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-200'>
            Submit Nutrition Data
          </button>
        </form>
      )}
    </div>
  );
};

export default SubmitCitizens;
