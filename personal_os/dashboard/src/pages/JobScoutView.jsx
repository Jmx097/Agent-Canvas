import React, { useState, useEffect } from 'react';

const API_BASE = "http://localhost:8000/api";

const JobScoutView = () => {
  const [jobs, setJobs] = useState([]);
  const [loading, setLoading] = useState(false);
  const [status, setStatus] = useState("");

  const fetchJobs = async () => {
    try {
      const res = await fetch(`${API_BASE}/jobs`);
      const data = await res.json();
      setJobs(data.jobs || []);
    } catch (err) {
      console.error(err);
    }
  };

  const runJobScout = async () => {
    setLoading(true);
    setStatus("Running Job Scout...");
    try {
      const res = await fetch(`${API_BASE}/run/job-scout`, { method: "POST" });
      const data = await res.json();
      setStatus(data.message);
      fetchJobs();
    } catch (err) {
      console.error(err);
      setStatus("Failed to run Job Scout.");
    } finally {
      setLoading(false);
    }
  };

  const pruneData = async () => {
    if (!confirm("Are you sure you want to prune old data?")) return;
    setLoading(true);
    setStatus("Pruning...");
    try {
      const res = await fetch(`${API_BASE}/prune`, { method: "POST" });
      const data = await res.json();
      setStatus(data.message);
      fetchJobs();
    } catch (err) {
      console.error(err);
      setStatus("Failed to prune.");
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchJobs();
  }, []);

  return (
    <div className="job-scout-view">
      <header className="page-header">
        <h1 className="page-title">Job Scout</h1>
        <p className="page-subtitle">Automated job sourcing and scoring agent</p>
      </header>

      <div className="glass-card">
        <div className="card-header">
          <h2 className="card-title">Controls</h2>
          <div style={{ display: 'flex', gap: '1rem' }}>
            <button 
              className="btn btn-secondary" 
              onClick={pruneData}
              disabled={loading}
            >
              Prune Data
            </button>
            <button 
              className="btn btn-primary" 
              onClick={runJobScout}
              disabled={loading}
            >
              {loading ? "Running..." : "Run Job Scout"}
            </button>
          </div>
        </div>
        {status && (
            <div style={{ color: 'var(--primary-cyan)', marginTop: '0.5rem', fontSize: '0.9rem' }}>
                {status}
            </div>
        )}
      </div>

      <div className="jobs-list">
        {jobs.length === 0 ? (
            <p style={{ color: 'var(--text-muted)', textAlign: 'center', padding: '2rem' }}>No jobs found. Run the scout to find matches.</p>
        ) : (
            jobs.map((job, idx) => (
            <div key={job.id || idx} className="job-item">
                <div className="job-header-row">
                <div style={{ display: 'flex', alignItems: 'center', gap: '1rem' }}>
                    <span style={{ fontFamily: 'monospace', color: 'var(--text-muted)' }}>#{idx + 1}</span>
                    <h3 className="job-title">{job.title}</h3>
                </div>
                <span className="job-score-badge">
                    {job.score ? job.score.toFixed(0) : 'N/A'}
                </span>
                </div>
                
                <div className="job-tags">
                {job.score_details && Object.entries(job.score_details).map(([key, val]) => {
                    if (key === 'url') return null;
                    return (
                    <span key={key} className="tag">
                        {key}: {typeof val === 'number' ? val.toFixed(0) : val}
                    </span>
                    );
                })}
                </div>

                <p className="job-summary">{job.content_summary}</p>
                
                {job.url && (
                <div style={{ marginTop: '1rem' }}>
                    <a 
                    href={job.url} 
                    target="_blank" 
                    rel="noopener noreferrer" 
                    className="btn btn-secondary"
                    style={{ fontSize: '0.8rem', padding: '0.4rem 0.8rem' }}
                    >
                    Apply Now ↗
                    </a>
                </div>
                )}
            </div>
            ))
        )}
      </div>
    </div>
  );
};

export default JobScoutView;
