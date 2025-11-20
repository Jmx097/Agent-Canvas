import React from 'react';
import { Outlet } from 'react-router-dom';
import Sidebar from './Sidebar';
import GlobalLightRays from './backgrounds/GlobalLightRays';

const Layout = () => {
  return (
    <div className="flex min-h-screen relative bg-black text-white overflow-hidden">
      <GlobalLightRays speedMs={32000} intensity={0.06} />
      <div className="relative z-10 flex w-full">
        <Sidebar />
        <main className="flex-1 p-8 overflow-y-auto h-screen">
          <Outlet />
        </main>
      </div>
    </div>
  );
};

export default Layout;
