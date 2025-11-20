import React from 'react';
import { Link, useLocation } from 'react-router-dom';
import { LayoutDashboard, Search, MessageSquare, BrainCircuit } from 'lucide-react';

const Sidebar = () => {
  const location = useLocation();
  
  const navItems = [
    { path: '/', label: 'Dashboard', icon: <LayoutDashboard size={20} /> },
    { path: '/job-scout', label: 'Job Scout', icon: <Search size={20} /> },
    { path: '/thread-spotter', label: 'Thread Spotter', icon: <MessageSquare size={20} /> },
    { path: '/orchestrator', label: 'Orchestrator', icon: <BrainCircuit size={20} /> },
  ];

  return (
    <aside className="w-64 h-screen bg-black/40 backdrop-blur-md border-r border-white/5 flex flex-col p-6 z-20">
      <div className="mb-10 px-2">
        <h2 className="text-xl font-bold text-white tracking-wider">PERSONAL OS</h2>
        <div className="h-1 w-8 bg-white/20 mt-2 rounded-full"></div>
      </div>
      
      <nav className="flex-1 space-y-2">
        {navItems.map((item) => {
          const isActive = location.pathname === item.path;
          return (
            <Link
              key={item.path}
              to={item.path}
              className={`flex items-center gap-3 px-4 py-3 rounded-xl transition-all duration-200 ${
                isActive 
                  ? 'bg-white/10 text-white shadow-[0_0_15px_rgba(255,255,255,0.1)] border border-white/5' 
                  : 'text-white/50 hover:text-white hover:bg-white/5'
              }`}
            >
              {item.icon}
              <span className="font-medium text-sm">{item.label}</span>
            </Link>
          );
        })}
      </nav>

      <div className="mt-auto px-2">
        <div className="text-xs text-white/30 font-mono">v1.0.0</div>
      </div>
    </aside>
  );
};

export default Sidebar;
