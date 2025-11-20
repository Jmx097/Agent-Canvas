import React from 'react';
import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom';
import Layout from './components/Layout';
import DashboardHome from './pages/DashboardHome';
import JobScoutView from './pages/JobScoutView';
import ThreadSpotterView from './pages/ThreadSpotterView';
import OrchestratorView from './pages/OrchestratorView';
import './App.css';

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Layout />}>
          <Route index element={<DashboardHome />} />
          <Route path="job-scout" element={<JobScoutView />} />
          <Route path="thread-spotter" element={<ThreadSpotterView />} />
          <Route path="orchestrator" element={<OrchestratorView />} />
          <Route path="*" element={<Navigate to="/" replace />} />
        </Route>
      </Routes>
    </BrowserRouter>
  );
}

export default App;
