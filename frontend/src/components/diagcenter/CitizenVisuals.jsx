import React, { useEffect, useState } from 'react';
import { Line } from 'react-chartjs-2';
import { Chart as ChartJS, LineElement, CategoryScale, LinearScale, PointElement } from 'chart.js';

// Register necessary components
ChartJS.register(LineElement, CategoryScale, LinearScale, PointElement);

const CitizenVisuals = ({ citizen_id }) => {
  const [nutritionData, setNutritionData] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchNutritionData = async () => {
      try {
        const response = await fetch(`http://localhost:5000/nutrition_data?citizen_id=${citizen_id}`);
        if (response.ok) {
          const data = await response.json();
          setNutritionData(data);
        } else {
          console.error('Failed to fetch nutrition data');
        }
      } catch (error) {
        console.error('Error fetching nutrition data:', error);
      } finally {
        setLoading(false);
      }
    };

    fetchNutritionData();
  }, [citizen_id]);

  if (loading) return <p className="text-center text-white">Loading...</p>;

  // Check if there is nutrition data
  if (nutritionData.length === 0) {
    return <p className="text-center"></p>;
  }

  // Prepare data for charts
  const labels = nutritionData.slice(0, 3).map(report => new Date(report.report_date).toLocaleDateString());

  const createChartData = (metric, color) => ({
    labels,
    datasets: [{
      label: metric.charAt(0).toUpperCase() + metric.slice(1),
      data: nutritionData.slice(0, 3).map(report => report[metric]),
      borderColor: color,
      backgroundColor: color.replace('rgba', 'rgba').replace('1)', '0.2)'),
      fill: true,
    }],
  });

  const chartsData = {
    bmi: createChartData('bmi', 'rgba(75, 192, 192, 1)'),
    stunting: createChartData('stunting', 'rgba(255, 99, 132, 1)'),
    wasting: createChartData('wasting', 'rgba(153, 102, 255, 1)'),
    height: createChartData('height', 'rgba(255, 159, 64, 1)'),
    weight: createChartData('weight', 'rgba(54, 162, 235, 1)'),
    iron_level: createChartData('iron_level', 'rgba(255, 206, 86, 1)'),
    vitamin_a: createChartData('vitamin_a', 'rgba(75, 192, 192, 1)'),
    vitamin_d: createChartData('vitamin_d', 'rgba(153, 102, 255, 1)'),
    zinc: createChartData('zinc', 'rgba(255, 99, 132, 1)'),
    folic_acid: createChartData('folic_acid', 'rgba(255, 159, 64, 1)'),
    iodine: createChartData('iodine', 'rgba(54, 162, 235, 1)'),
    blood_glucose: createChartData('blood_glucose', 'rgba(255, 206, 86, 1)'),
    lipid_profile: createChartData('lipid_profile', 'rgba(75, 192, 192, 1)'),
    serum_protein: createChartData('serum_protein', 'rgba(153, 102, 255, 1)'),
    sodium: createChartData('sodium', 'rgba(255, 99, 132, 1)'),
    potassium: createChartData('potassium', 'rgba(255, 159, 64, 1)'),
    calcium: createChartData('calcium', 'rgba(54, 162, 235, 1)'),
  };

  return (
    <div className="p-4 flex flex-wrap gap-4">
      {Object.entries(chartsData).map(([key, data]) => (
        <div key={key} className="mb-8 w-full md:w-1/3 bg-[#2d2d2d] px-3 mx-auto rounded-lg">
          <h3 className="text-lg font-semibold text-white">{key.charAt(0).toUpperCase() + key.slice(1)} Over Time</h3>
          <Line data={data} />
        </div>
      ))}
    </div>
  );
};

export default CitizenVisuals;
