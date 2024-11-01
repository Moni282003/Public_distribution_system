import React from 'react';
import axios from 'axios';

const PDFViewer = ({ citizenId }) => {
  const fetchPDF = async () => {
    try {
      const response = await axios.get(`/api/get-pdf?citizen_id=${citizenId}`, {
        responseType: 'blob',
      });

      const pdfUrl = window.URL.createObjectURL(new Blob([response.data]));
      window.open(pdfUrl, '_blank');
    } catch (error) {
      console.error("Error fetching the PDF:", error);
    }
  };

  return (
    <div className="pdf-viewer-container">
      <button 
        onClick={fetchPDF} 
        className="px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700"
      >
        View PDF
      </button>
    </div>
  );
};

export default PDFViewer;
