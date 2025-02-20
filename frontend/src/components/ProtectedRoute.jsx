import { Navigate } from 'react-router-dom';

const ProtectedRoute = ({ children }) => {
  const centerId = localStorage.getItem('center_id');
  const role = localStorage.getItem('role');

  if (!centerId || !role ) {
    return <Navigate to="/" replace />;
  }

  return children; 
};

const ProtectedRouteAdmin = ({ children }) => {
    const admin = localStorage.getItem('admin');
    
    if (!admin) {
      return <Navigate to="/" replace />;
    }
  
    return children; 
  };

  const ProtectedRouteCitizen = ({ children }) => {
    const admin = localStorage.getItem('aadhar');
  
    if (!admin) {
      return <Navigate to="/" replace />;
    }
  
    return children; 
  };

  const ProtectedRouteDiag = ({ children }) => {
    const admin = localStorage.getItem('username');
  
    if (!admin) {
      return <Navigate to="/" replace />;
    }
  
    return children; 
  };


export default ProtectedRoute
export { ProtectedRouteAdmin };
export { ProtectedRouteCitizen };
export {ProtectedRouteDiag};

