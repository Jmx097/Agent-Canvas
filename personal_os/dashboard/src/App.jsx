import { useState, useEffect } from 'react'
import ReactMarkdown from 'react-markdown'
import './App.css'

const API_BASE = "http://localhost:8000/api";

function App() {
  const [plan, setPlan] = useState("");
  const [loading, setLoading] = useState(false);
  const [status, setStatus] = useState("");
  const [jobs, setJobs] = useState([]);

  const fetchPlan = async () => {
    try {
      const res = await fetch(`${API_BASE}/plan`);
      const data = await res.json();
      setPlan(data.content);
    } catch (err) {
      console.error(err);
      setStatus("Failed to fetch plan.");
    }
  };

  useEffect(() => {
    fetchPlan();
  }, []);

  const runAgent = async (name) => {
    setLoading(true);
    setStatus(`Running ${name}...`);
    setJobs([]); // Clear previous jobs
    try {
      const res = await fetch(`${API_BASE}/run/${name}`, { method: "POST" });
      const data = await res.json();
      setStatus(data.message);
      
      if (name === "job-scout" && data.jobs) {
        setJobs(data.jobs);
      }
      
      if (name === "orchestrator") fetchPlan();
    } catch (err) {
      console.error(err);
      setStatus(`Failed to run ${name}.`);
    } finally {
      setLoading(false);
    }
  };

  const prune = async () => {
    if (!confirm("Are you sure you want to prune old data?")) return;
    setLoading(true);
    setStatus("Pruning...");
    try {
      const res = await fetch(`${API_BASE}/prune`, { method: "POST" });
      const data = await res.json();
      setStatus(data.message);
    } catch (err) {
      console.error(err);
      setStatus("Failed to prune.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="dashboard">
      <header className="header">
        <h1>Personal OS Command Center</h1>
        <div className="status-bar">{status || "Ready"}</div>
      </header>

      <main className="main-content">
        <div className="controls">
          <div className="card control-card">
            <h2>Agents</h2>
            <div className="button-group">
              <button disabled={loading} onClick={() => runAgent("job-scout")}>
                Job Scout
              </button>
              <button disabled={loading} onClick={() => runAgent("thread-spotter")}>
                Thread Spotter
              </button>
              <button disabled={loading} onClick={() => runAgent("orchestrator")}>
                Orchestrator
              </button>
            </div>
          </div>

          <div className="card control-card">
            <h2>Maintenance</h2>
            <div className="button-group">
              <button disabled={loading} onClick={prune} className="danger">
                Prune Data
              </button>
              <button onClick={fetchPlan} className="secondary">
                Refresh Plan
              </button>
            </div>
          </div>
        </div>

        <div className="results-container">
          {jobs.length > 0 && (
            <div className="card jobs-card">
              <h2>Top {jobs.length} Job Matches</h2>
              <div className="jobs-list">
                {jobs.map((job, idx) => (
                  <div key={job.id} className="job-item">
                    <div className="job-header">
                      <span className="job-number">#{idx + 1}</span>
                      <h3>{job.title}</h3>
                      <span className="job-score">{job.score.toFixed(0)}</span>
                    </div>
                    <div className="job-details">
                      {job.score_details && (
                        <div className="score-breakdown">
                          {Object.entries(job.score_details).map(([key, val]) => (
                            <span key={key} className="score-tag">
                              {key}: {typeof val === 'number' ? val.toFixed(0) : val}
                            </span>
                          ))}
                        </div>
                      )}
                      <p className="job-summary">{job.content_summary}</p>
                    </div>
                  </div>
                ))}
              </div>
            </div>
          )}

          <div className="plan-container card">
            <h2>Daily Plan</h2>
            <div className="markdown-content">
              <ReactMarkdown>{plan}</ReactMarkdown>
            </div>
          </div>
        </div>
      </main>
    </div>
  )
}

export default App
