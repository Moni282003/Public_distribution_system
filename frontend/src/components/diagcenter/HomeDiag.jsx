import React, { useEffect, useState, useRef } from 'react';
import axios from 'axios';
import { Bar, Pie } from 'react-chartjs-2';
import Clock from 'react-clock';
import 'react-clock/dist/Clock.css';
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  BarElement,
  Title,
  Tooltip,
  Legend,
  ArcElement,
} from 'chart.js';
import './HomeDiag.css';
import { FaArrowDown, FaArrowUp } from 'react-icons/fa';




// Register the necessary components
ChartJS.register(CategoryScale, LinearScale, BarElement, Title, Tooltip, Legend, ArcElement);

// CSS for arrow animation
const arrowStyle = {
  display: 'inline-block',
  animation: 'arrow-up 0.5s ease-in-out infinite',
};

const HomeDiag = () => {
  const [averageData, setAverageData] = useState({});
  const [citizenCounts, setCitizenCounts] = useState({});
  const [loading, setLoading] = useState(true);
  const [time, setTime] = useState(new Date());
  const centerid = localStorage.getItem('centerid');
  const chartRefs = useRef([]); // Initialize chartRefs

  const chartOptions = {
    responsive: true,
    maintainAspectRatio: false,
    plugins: {
      legend: {
        display: true,
      },
      tooltip: {
        enabled: true,
      },
    },
  };

  useEffect(() => {
    const fetchAverageMetrics = async () => {
      try {
        const response = await axios.get('http://localhost:5000/three_avg_metrics');
        const formattedData = {};

        response.data.forEach(record => {
          for (let key in record) {
            if (key !== 'citizen_id') {
              const baseKey = key.split('_').slice(0, -1).join('_');
              const index = key.split('_').slice(-1);

              if (!formattedData[baseKey]) {
                formattedData[baseKey] = { 1: null, 2: null, 3: null };
              }
              if (record[key] !== null && record[key] !== undefined) {
                formattedData[baseKey][index] = Number(record[key]);
              }
            }
          }
        });

        for (let key in formattedData) {
          for (let i = 1; i <= 3; i++) {
            if (!formattedData[key][i]) {
              formattedData[key][i] = 0;
            }
          }
        }

        setAverageData(formattedData);
      } catch (error) {
        console.error('Error fetching average metrics:', error);
      }
    };

    const fetchUniqueCitizenCounts = async () => {
      try {
        const response = await axios.get(`http://localhost:5000/unique_citizens/count?diagnostic_center_id=${centerid}`);
        setCitizenCounts(response.data);
      } catch (error) {
        console.error('Error fetching unique citizen counts:', error);
      } finally {
        setLoading(false);
      }
    };

    fetchAverageMetrics();
    fetchUniqueCitizenCounts();
  }, [centerid]);

  useEffect(() => {
    const intervalId = setInterval(() => setTime(new Date()), 1000);
    return () => clearInterval(intervalId);
  }, []);

  if (loading) return <p>Loading data...</p>;

  return (
    <div className='mx-3 z-50'>
      <div className='flex'>
        <div className='w-5/6 h-[1250px]' >
          <div className='mr-3 h-[120px]'>
            <div style={{ border: '1px solid ', borderRadius: '8px', textAlign: 'center' }} className='w-full h-[110px] mx-auto flex py-1 gap-3'>
              <div className='w-1/5 bg-[#1d1d1d] px-2 py-2 rounded-lg'>
                <h3 className='text-gray-300 text-md text-left'>Total Citizens</h3>
                <h2 className='text-white text-5xl text-right mt-2'>{citizenCounts.citizens_count}</h2>
              </div>
              <div className='w-1/5 bg-[#1d1d1d] px-2 py-2 rounded-lg'>
                <h3 className='text-gray-300 text-md text-left'>Due citizens</h3>
                <h2 className='text-white text-5xl text-right mt-2'>{citizenCounts.recent_nutrition_data + citizenCounts.citizens_count - citizenCounts.nutrition_data_count}</h2>
              </div>
              <div className='w-1/5 bg-[#1d1d1d] px-2 py-2 rounded-lg'>
                <h3 className='text-gray-300 text-md text-left'>Not reported</h3>
                <h2 className='text-white text-5xl text-right mt-2'>{citizenCounts.recent_nutrition_data + citizenCounts.citizens_count - citizenCounts.nutrition_data_count}</h2>
              </div>
              <div className='w-2/5 bg-[#1d1d1d] px-2 py-2 rounded-lg'>
                <h1 className='text-left text-gray-300 text-2xl'>Dash Board</h1>
                <h2 className='text-right text-white text-5xl'>{centerid}</h2>
              </div>
            </div>
          </div>
          <div className='flex gap-[0.9px] flex-wrap mr-3 h-[1250px]'>
            <div key="unique-citizens-report" className='w-[275px] h-1/5 mb-4 px-4 bg-[#2d2d2d] mx-0.5 rounded-lg shadow-md py-6 border-[1px]'>
              <Pie
                ref={ref => chartRefs.current[0] = ref}
                data={{
                  labels: ['Reported', 'No report'],
                  datasets: [
                    {
                      label: 'Count',
                      data: [
                        citizenCounts.nutrition_data_count || 0,
                        (citizenCounts.citizens_count - citizenCounts.nutrition_data_count) || 0,
                      ],
                      backgroundColor: ['rgba(153, 102, 255, 0.6)', 'rgba(75, 192, 192, 0.6)'],
                      borderColor: ['rgba(153, 102, 255, 1)', 'rgba(75, 192, 192, 1)'],
                      borderWidth: 2,
                    },
                  ],
                }}
                options={chartOptions}
                width={300}
                height={300}
              />
            </div>

            <div key="due-counts" className='w-[275px] h-[250px] mb-4 px-4 bg-[#2d2d2d] mx-0.5 rounded-lg shadow-md py-6 border-[1px]'>
              <Pie
                ref={ref => chartRefs.current[1] = ref}
                data={{
                  labels: ['Due', 'No Due'],
                  datasets: [
                    {
                      label: 'Count',
                      data: [
                        citizenCounts.citizens_count - citizenCounts.nutrition_data_count || 0,
                        citizenCounts.nutrition_data_count || 0,
                      ],
                      backgroundColor: ['rgba(153, 102, 255, 0.6)', 'rgba(75, 192, 192, 0.6)'],
                      borderColor: ['rgba(153, 102, 255, 1)', 'rgba(75, 192, 192, 1)'],
                      borderWidth: 2,
                    },
                  ],
                }}
                options={chartOptions}
                width={300}
                height={300}
              />
            </div>

            {Object.entries(averageData).map(([metric, values], index) => (
              <div key={`bar-${metric}-${index}`} className='w-[275px] h-1/5 mb-4 px-4 bg-[#2d2d2d] mx-0.5 rounded-lg shadow-md py-6 border-[1px] border-[white]'>
                <h3 style={{ fontSize: '1rem', textAlign: 'center', color: '#ffffff', marginBottom: "2px" }}>{metric.toUpperCase().replace("AVG_", "").replace("_", " ")}</h3>
                <Bar
                  data={{
                    labels: ['1', '2', '3'],
                    datasets: [{
                      label: `${metric}`,
                      data: [values[1], values[2], values[3]],
                      backgroundColor: [
                        'rgba(75, 192, 192, 0.6)',
                        'rgba(153, 102, 255, 0.6)',
                        'rgba(255, 159, 64, 0.6)',
                      ],
                      borderColor: [
                        'rgba(75, 192, 192, 1)',
                        'rgba(153, 102, 255, 1)',
                        'rgba(255, 159, 64, 1)',
                      ],
                      borderWidth: 2,
                      hoverBackgroundColor: [
                        'rgba(75, 192, 192, 0.4)',
                        'rgba(153, 102, 255, 0.4)',
                        'rgba(255, 159, 64, 0.4)',
                      ],
                      hoverBorderColor: [
                        'rgba(75, 192, 192, 1)',
                        'rgba(153, 102, 255, 1)',
                        'rgba(255, 159, 64, 1)',
                      ],
                    }],
                  }}
                  options={chartOptions}
                  height={150}
                />
              </div>
            ))}
          </div>
        </div>

        <div className='w-1/6'>
          <div style={{ display: 'flex', justifyContent: 'center', border: '1px solid #ddd', borderRadius: '8px' }} className='mb-4 bg-gray-400 w-full p-2 h-[180px] py-2.5 rounded-md shadow-md'>
          <div className="clock-wrapper">
        <Clock value={time} size={150} />
      </div>
          </div>
          <div style={{ display: 'flex', flexWrap: 'wrap', gap: '16px', justifyContent: 'center', zIndex: "40" }}>
            <div style={{ borderRadius: '8px' }} className='w-full'>
            {Object.entries(averageData).slice(0, 7).map(([metric, values], index) => (
  <div
    key={index}
    style={{
      border: '1px solid #ddd',
      borderRadius: '8px',
      backgroundColor: index % 2 === 0 ? '#2d2d2d' : '#1d1d1d',
    }}
    className='w-full h-[150px] mb-8 rounded-md shadow-md'
  >
    <p style={{ color: 'white', zIndex: "40" }} className='p-1 text-md px-2'>
      {metric.toUpperCase().replace("AVG_", "").replace("_", " ")}
    </p>
    <div>
        <div>
        <span className='text-5xl text-white ml-4 mt-4'>{values[1]}</span>
          </div>
        <div>
      <p style={{ color: values[1] - values[2] >= 0 ? 'green' : 'red', zIndex: "40", display: 'flex', justifyContent: "flex-end", alignItems: 'center' }} className='p-1 text-md text-right px-3 text-3xl mt-3'>
        <span style={{ marginRight: '5px' }}>
          {values[2] === 0 ? 100 : (((values[1] - values[2]) / (values[2] || 1)) * 100).toFixed(2)}%
        </span>
        <span style={{ animation: 'bounce 1s infinite' }} className='mb-4 inline text-right'>
          {values[1] - values[2] >= 0 ? <FaArrowUp /> : <FaArrowDown />}
        </span>
      </p>
      </div>
      </div>
  </div>
))}

            </div>
          </div>
        </div>
      </div>
      <div className='flex flex-wrap w-full gap-1 justify-around'>
  {Object.entries(averageData).slice(8, 18).map(([metric, values], index) => (
    <div
      key={index}
      style={{
        border: '1px solid #ddd',
        borderRadius: '8px',
        backgroundColor: index % 2 === 0 ? '#2d2d2d' : '#1d1d1d',
      }}
      className='w-[225px] h-[150px] mb-3 rounded-md shadow-md' 
    >
      <p style={{ color: 'white', zIndex: "40" }} className='p-1 text-md px-2'>
        {metric.toUpperCase().replace("AVG_", "").replace("_", " ")}
      </p>
      <div>
        <div>
        <span className='text-5xl text-white ml-4 mt-4'>{values[1]}</span>
          </div>
        <div>
      <p style={{ color: values[1] - values[2] >= 0 ? 'green' : 'red', zIndex: "40", display: 'flex', justifyContent: "flex-end", alignItems: 'center' }} className='p-1 text-md text-right px-3 text-3xl mt-3'>
        <span style={{ marginRight: '5px' }}>
          {values[2] === 0 ? 100 : (((values[1] - values[2]) / (values[2] || 1)) * 100).toFixed(2)}%
        </span>
        <span style={{ animation: 'bounce 1s infinite' }} className='mb-4 inline text-right'>
          {values[1] - values[2] >= 0 ? <FaArrowUp /> : <FaArrowDown />}
        </span>
      </p>
      </div>
      </div>
    </div>
  ))}
</div>


    </div>
  );
};

export default HomeDiag;
