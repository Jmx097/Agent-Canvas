import React from 'react';
import { NavLink } from 'react-router-dom';
import { LayoutDashboard, Briefcase, MessageSquare, BrainCircuit } from 'lucide-react';

const Sidebar = () => {
  return (
    <aside className="sidebar">
      <div className="logo-area">
        <div className="logo-text">Personal OS</div>
      </div>
      
      <nav className="nav-links">
        <NavLink to="/" className={({ isActive }) => `nav-item ${isActive ? 'active' : ''}`}>
          <LayoutDashboard className="nav-icon" />
          <span>Dashboard</span>
        </NavLink>
        
        <NavLink to="/job-scout" className={({ isActive }) => `nav-item ${isActive ? 'active' : ''}`}>
          <Briefcase className="nav-icon" />
          <span>Job Scout</span>
        </NavLink>
        
        <NavLink to="/thread-spotter" className={({ isActive }) => `nav-item ${isActive ? 'active' : ''}`}>
          <MessageSquare className="nav-icon" />
          <span>Thread Spotter</span>
        </NavLink>
        
        <NavLink to="/orchestrator" className={({ isActive }) => `nav-item ${isActive ? 'active' : ''}`}>
          <BrainCircuit className="nav-icon" />
          <span>Orchestrator</span>
        </NavLink>
      </nav>
    </aside>
  );
};

export default Sidebar;
