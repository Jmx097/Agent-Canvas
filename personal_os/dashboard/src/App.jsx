import React from 'react';
import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom';
import Layout from './components/Layout';
import DashboardHome from './pages/DashboardHome';
import JobScoutView from './pages/JobScoutView';
import './App.css';

// Placeholder components for other agents
const ThreadSpotterView = () => (
  <div className="glass-card">
    <h2 className="card-title">Thread Spotter</h2>
    <p style={{ color: 'var(--text-muted)' }}>Coming soon...</p>
  </div>
);

const OrchestratorView = () => (
  <div className="glass-card">
    <h2 className="card-title">Orchestrator</h2>
    <p style={{ color: 'var(--text-muted)' }}>Coming soon...</p>
  </div>
);

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
