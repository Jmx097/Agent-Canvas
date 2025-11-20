import React, { useState, useEffect } from 'react';
import ReactMarkdown from 'react-markdown';

const API_BASE = "http://localhost:8000/api";

const DashboardHome = () => {
  const [plan, setPlan] = useState("");
  const [loading, setLoading] = useState(false);
  const [status, setStatus] = useState("");

  const fetchPlan = async () => {
    setLoading(true);
    try {
      // In a real app, we might have a specific endpoint for just the plan
      // For now, we'll simulate or reuse the orchestrator run if needed, 
      // but ideally we just want to fetch the *current* plan.
      // Since the original app didn't have a "get plan" endpoint separate from running,
      // we might need to adjust the backend or just show a placeholder if empty.
      // Let's assume we can get it or it's stored. 
      // For this refactor, I'll keep the "Refresh Plan" button logic.
      setStatus("Ready");
    } catch (err) {
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  const runOrchestrator = async () => {
    setLoading(true);
    setStatus("Running Orchestrator...");
    try {
      const res = await fetch(`${API_BASE}/run/orchestrator`, { method: "POST" });
      const data = await res.json();
      setStatus(data.message);
      setPlan(data.result || "Plan updated. Check logs."); // Adjust based on actual API response
    } catch (err) {
      console.error(err);
      setStatus("Failed to run Orchestrator.");
    } finally {
      setLoading(false);
    }
  };
  
  // Initial fetch
  useEffect(() => {
      // If we had a persistence layer, we'd fetch here.
  }, []);

  return (
    <div className="dashboard-home">
      <header className="page-header">
        <h1 className="page-title">Command Center</h1>
        <p className="page-subtitle">Overview of your Personal OS activity</p>
      </header>

      <div className="glass-card">
        <div className="card-header">
          <h2 className="card-title">Daily Plan</h2>
          <button 
            className="btn btn-primary" 
            onClick={runOrchestrator}
            disabled={loading}
          >
            {loading ? "Updating..." : "Generate Plan"}
          </button>
        </div>
        
        <div className="markdown-body">
          {plan ? (
            <ReactMarkdown>{plan}</ReactMarkdown>
          ) : (
            <p className="text-muted">No plan generated yet. Run the Orchestrator to get started.</p>
          )}
        </div>
      </div>
      
      <div className="glass-card">
        <div className="card-header">
            <h2 className="card-title">System Status</h2>
        </div>
        <div style={{ color: 'var(--text-muted)' }}>
            Status: <span style={{ color: 'var(--primary-cyan)' }}>{status || "Idle"}</span>
        </div>
      </div>
    </div>
  );
};

export default DashboardHome;
