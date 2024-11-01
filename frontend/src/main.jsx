import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import App from './App.jsx'
import './index.css'
import {
  createBrowserRouter,
  RouterProvider,
} from "react-router-dom";
import Home from './pages/Home.jsx';
import ErrorPage from './pages/ErrorPage.jsx';
import { AppProvider } from './context/AppContext.jsx';
import LandingPage from './pages/LandingPage.jsx';
import Citizen_login from './pages/Citizen_login.jsx';
import Admin_login from './pages/Admin_login.jsx';
import Ration_login from './pages/Ration_login.jsx';
import Diagnostic_login from './pages/Diagnostics_login.jsx';
import Highlights from './components/Highlights.jsx';

// src/main.jsx or wherever you are importing
import ProtectedRoute, { ProtectedRouteAdmin,ProtectedRouteCitizen, ProtectedRouteDiag } from './components/ProtectedRoute';
import Admin_dashboard  from './pages/dashboard/Admin_dashboard.jsx';
import Citizen_dashboard  from './pages/dashboard/Citizen_dashboard.jsx';
import AddUser from './components/Admin/Citizen/AddUser.jsx';
import ViewUsers from './components/Admin/Citizen/ViewUsers.jsx'
import ViewRation from './components/Admin/Citizen/ViewRation.jsx';
import ManageRation from './components/Admin/Ration/ManageRation.jsx';
import AddRation from './components/Admin/Ration/AddRation.jsx';
import AddCenter from './components/Admin/Center/AddCenter.jsx';
import ManageCenters from './components/Admin/Center/ManageCenters.jsx';
import ChangePassword from './components/Admin/Setting/ChangePassword.jsx';
import AddAdmin from './components/Admin/Setting/AddAdmin.jsx';
import  DiagCenter_dashboard  from './pages/dashboard/DiagCenter_dashboard.jsx';
import ViewCitizens from './components/diagcenter/viewCitizens.jsx';
import Submitcitizens from './components/diagcenter/Submitcitizens.jsx';
import HomeDiag from './components/diagcenter/HomeDiag.jsx';
import ChangePassDiag from './components/diagcenter/ChangePassDiag.jsx';
const router = createBrowserRouter([
  {
    path: "/",
    element: <App />,
    errorElement: <ErrorPage />,
    children: [
      {
        path: "/",
        element: <LandingPage />
      },
      {
        path: "/citizen-login",
        element: <Citizen_login />
      },
      {
        path: "/central-Admin-login",
        element: <Admin_login />
      },
      {
        path: "/ration-login",
        element: <Ration_login />
      },
      {
        path: "/diagnostics-login",
        element: <Diagnostic_login />
      },
      {
        path: "/home",
        element: (
          <ProtectedRoute>
            <Home />
          </ProtectedRoute>
        )
      },
      {
        path: "/admin",
        element: (
          <ProtectedRouteAdmin>
            <Admin_dashboard />
          </ProtectedRouteAdmin>
        ),
        children:[
          {
            path: "/admin",
            element: <ProtectedRouteAdmin><Highlights/></ProtectedRouteAdmin>
          },
        {
          path: "/admin/add-user",
          element:<ProtectedRouteAdmin><AddUser/></ProtectedRouteAdmin>
        },
        {
          path: "/admin/view-users",
          element:<ProtectedRouteAdmin><ViewUsers/></ProtectedRouteAdmin>
        },
        {
          path: "/admin/view-ration",
          element:<ProtectedRouteAdmin><ViewRation/></ProtectedRouteAdmin>
        },
        {
          path: "/admin/add-ration",
          element:<ProtectedRouteAdmin><AddRation/></ProtectedRouteAdmin>
        },
        {
          path: "/admin/add-center",
          element:<ProtectedRouteAdmin><AddCenter/></ProtectedRouteAdmin>
        },
        {
          path: "/admin/manage-ration",
          element:<ProtectedRouteAdmin><ManageRation/></ProtectedRouteAdmin>
        },
        {
          path: "/admin/manage-centers",
          element:<ProtectedRouteAdmin><ManageCenters/></ProtectedRouteAdmin>
        },
        {
          path: "/admin/change-password",
          element:<ProtectedRouteAdmin><ChangePassword/></ProtectedRouteAdmin>
        },
        {
          path: "/admin/add-admin",
          element:<ProtectedRouteAdmin><AddAdmin/></ProtectedRouteAdmin>
        }
        
      ]
      },
      {
        path:"/diagcenter",
        element:(
          <ProtectedRouteDiag>
          <DiagCenter_dashboard/></ProtectedRouteDiag>
        ),
        children:[
          {
            path:"/diagcenter",
            element:(
              <ProtectedRouteDiag>
              <HomeDiag/></ProtectedRouteDiag>
            )
          },
          {
            path: "/diagcenter/view-citizens",
            element:(<ProtectedRouteDiag><ViewCitizens/></ProtectedRouteDiag>)
          },
          {
            path:"/diagcenter/submit-report",
            element:(<ProtectedRouteDiag><Submitcitizens/></ProtectedRouteDiag>)
          },
          {
            path:"/diagcenter/change-password",
            element:(<ProtectedRouteDiag><ChangePassDiag/></ProtectedRouteDiag>)
          }
        ]
      },
      {
        path: "/citizen",
        element: (
          <ProtectedRouteCitizen>
            <Citizen_dashboard />
          </ProtectedRouteCitizen>
        )
      }
    ]
  }
]);


createRoot(document.getElementById('root')).render(
  <StrictMode>
    <AppProvider>
    <RouterProvider router={router} /></AppProvider>
  </StrictMode>,
)
