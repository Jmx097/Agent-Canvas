import React from 'react';
import { Link } from 'react-router-dom';

export const JobsWidget = ({ jobs, onRun, loading }) => {
  return (
    <div className="glass-card widget-card">
      <div className="widget-header">
        <h3>Job Scout</h3>
        <span className="badge">{jobs.length} New</span>
      </div>
      <div className="widget-content">
        {jobs.length === 0 ? (
          <p className="empty-state">No new matches.</p>
        ) : (
          <ul className="widget-list">
            {jobs.slice(0, 5).map((job) => (
              <li key={job.id} className="widget-item">
                <div className="item-main">
                  <span className="item-title">{job.title}</span>
                  <span className="item-score">{job.score.toFixed(0)}</span>
                </div>
              </li>
            ))}
          </ul>
        )}
      </div>
      <div className="widget-actions">
        <button className="btn btn-sm btn-primary" onClick={onRun} disabled={loading}>
          {loading ? 'Running...' : 'Run Scout'}
        </button>
        <Link to="/job-scout" className="btn btn-sm btn-ghost">View All</Link>
      </div>
    </div>
  );
};

export const TrendsWidget = ({ threads, onRun, loading }) => {
  return (
    <div className="glass-card widget-card">
      <div className="widget-header">
        <h3>Thread Spotter</h3>
        <span className="badge">{threads.length} New</span>
      </div>
      <div className="widget-content">
        {threads.length === 0 ? (
          <p className="empty-state">No new signals.</p>
        ) : (
          <ul className="widget-list">
            {threads.slice(0, 5).map((thread) => (
              <li key={thread.id} className="widget-item">
                <div className="item-main">
                  <span className="item-title">{thread.title}</span>
                  <span className="item-score">{thread.score.toFixed(0)}</span>
                </div>
              </li>
            ))}
          </ul>
        )}
      </div>
      <div className="widget-actions">
        <button className="btn btn-sm btn-primary" onClick={onRun} disabled={loading}>
          {loading ? 'Scanning...' : 'Run Spotter'}
        </button>
        <Link to="/thread-spotter" className="btn btn-sm btn-ghost">View All</Link>
      </div>
    </div>
  );
};

export const SummaryWidget = ({ plan, onGenerate, loading }) => {
  // Simple markdown preview (first few lines)
  const preview = plan ? plan.split('\n').slice(0, 6).join('\n') : "No plan generated yet.";

  return (
    <div className="glass-card widget-card summary-widget">
      <div className="widget-header">
        <h3>Daily Briefing</h3>
        <span className="badge">Today</span>
      </div>
      <div className="widget-content">
        <div className="markdown-preview">
          <pre>{preview}...</pre>
        </div>
      </div>
      <div className="widget-actions">
        <button className="btn btn-sm btn-primary" onClick={onGenerate} disabled={loading}>
          {loading ? 'Generating...' : 'Regenerate Plan'}
        </button>
        <Link to="/orchestrator" className="btn btn-sm btn-ghost">Full Plan</Link>
      </div>
    </div>
  );
};
