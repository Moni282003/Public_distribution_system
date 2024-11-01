import React from 'react';
import { Link } from 'react-router-dom'; 
import { Users, Store, Stethoscope, BarChart, ChevronLeft, ChevronRight, Settings, PlusCircle, ChevronDown, ChevronUp } from 'lucide-react';

function Sidebar({ isNavExpanded, toggleNav, expandedSection, toggleDropdown, setIsNavExpanded, setExpandedSection }) {
  return (
    <nav
      className={`bg-[#1D1D1D] mt-4 rounded-3xl transition-all duration-300 ease-in-out ${isNavExpanded ? "w-64" : "w-20"}`}
      style={{ marginLeft: '1px' }}
    >
      <div className="p-4 flex justify-between items-center">
        {/* Wrap Admin Panel title with Link */}
        <Link to="/admin" onClick={() => setIsNavExpanded(false)} className={`text-2xl font-bold ${isNavExpanded ? "block" : "hidden"}`}>
          Admin Panel
        </Link>
        <button onClick={toggleNav} className="p-2 rounded-full hover:bg-orange-600 transition-colors">
          {isNavExpanded ? <ChevronLeft size={20} /> : <ChevronRight size={20} />}
        </button>
      </div>

      <ul className="mt-6">
        {[ 
          { name: "Manage Users", icon: <Users size={20} />, subItems: [{ title: 'Add User', link: '/admin/add-user' }, { title: 'View Users', link: '/admin/view-users' }, { title: 'View Ration', link: '/admin/view-ration' }] },
          { name: "Manage Ration", icon: <Store size={20} />, subItems: [{ title: 'Add Ration', link: '/admin/add-ration' }, { title: 'Manage Ration', link: '/admin/manage-ration' }, { title: 'View Allocation', link: '/view-allocation' }] },
          { name: "Manage Diag Center", icon: <Stethoscope size={20} />, subItems: [{ title: 'Add Center', link: '/admin/add-center' }, { title: 'Manage Centers', link: '/admin/manage-centers' }, { title: 'View Reports', link: '/view-reports' }] },
          { name: "Settings", icon: <Settings size={20} />, subItems: [{ title: 'Change Password', link: '/admin/change-password' }, { title: 'Add Admin', link: '/admin/add-admin' }] },
          { name: "Analytics", icon: <BarChart size={20} />, subItems: [] },
        ].map((item) => (
          <li key={item.name} className="mb-2">
            <div
              className={`flex items-center justify-between px-4 py-2 ${isNavExpanded ? "w-64" : "w-20"} hover:bg-gray-700 rounded-lg transition-transform cursor-pointer`}
              onClick={() => toggleDropdown(item.name)}
            >
              <div className={`ml-2 flex items-center ${isNavExpanded ? "justify-start" : "justify-center"}`}>
                {item.icon}
                <span className={`ml-2 ${isNavExpanded ? "block" : "hidden"}`}>
                  {item.name}
                </span>
              </div>
              {item.subItems.length > 0 && isNavExpanded && (
                <span>
                  {expandedSection === item.name ? <ChevronUp size={20} /> : <ChevronDown size={20} />}
                </span>
              )}
            </div>
            {/* Dropdown items */}
            {expandedSection === item.name && isNavExpanded && (
              <ul className="ml-6 mt-2">
                {item.subItems.map((subItem, index) => (
                  <li key={index} className="flex items-center py-2 text-gray-400 hover:text-orange-600 transition-colors rounded-lg">
                    <Link onClick={() => {setIsNavExpanded(false)
                        setExpandedSection(false)
                    }} to={subItem.link} className="flex items-center w-full">
                      <PlusCircle size={16} className="mr-2" />
                      {subItem.title}
                    </Link>
                  </li>
                ))}
              </ul>
            )}
          </li>
        ))}
      </ul>
    </nav>
  );
}

export default Sidebar;
