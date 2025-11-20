import React, { useState, useEffect } from 'react';

const API_BASE = "http://localhost:8000/api";

const ThreadSpotterView = () => {
  const [threads, setThreads] = useState([]);
  const [loading, setLoading] = useState(false);
  const [status, setStatus] = useState("");

  const fetchThreads = async () => {
    try {
      const res = await fetch(`${API_BASE}/trends`);
      const data = await res.json();
      setThreads(data.threads || []);
    } catch (err) {
      console.error(err);
    }
  };

  const runThreadSpotter = async () => {
    setLoading(true);
    setStatus("Running Thread Spotter...");
    try {
      const res = await fetch(`${API_BASE}/run/thread-spotter`, { method: "POST" });
      const data = await res.json();
      setStatus(data.message);
      fetchThreads();
    } catch (err) {
      console.error(err);
      setStatus("Failed to run Thread Spotter.");
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchThreads();
  }, []);

  return (
    <div className="space-y-6">
      <header className="flex justify-between items-center mb-8">
        <div>
            <h1 className="text-3xl font-bold text-white">Thread Spotter</h1>
            <p className="text-gray-400">Monitoring high-signal discussions.</p>
        </div>
        <div className="flex flex-col items-end gap-2">
            <button 
                onClick={runThreadSpotter} 
                disabled={loading}
                className="px-4 py-2 bg-purple-600 hover:bg-purple-500 text-white rounded-lg transition-colors disabled:opacity-50"
            >
                {loading ? 'Scanning...' : 'Run Thread Spotter'}
            </button>
            {status && <span className="text-sm text-purple-300">{status}</span>}
        </div>
      </header>

      <div className="grid gap-4">
        {threads.map(thread => (
          <div key={thread.id} className="bg-white/5 border border-white/10 rounded-xl p-5 hover:bg-white/10 transition-all group">
            <div className="flex justify-between items-start">
                <div>
                    <h3 className="text-lg font-semibold text-gray-200 group-hover:text-purple-300 transition-colors">
                        <a href={thread.url} target="_blank" rel="noopener noreferrer">{thread.title}</a>
                    </h3>
                    <p className="text-sm text-gray-500 mt-1">
                        {thread.content_summary}
                    </p>
                </div>
                <div className="flex flex-col items-end">
                    <span className="text-2xl font-bold text-purple-400">{thread.score}</span>
                    <span className="text-xs text-gray-500 uppercase tracking-wider">Score</span>
                </div>
            </div>
          </div>
        ))}
        
        {threads.length === 0 && !loading && (
            <div className="text-center py-12 text-gray-500">
                No threads found. Run the spotter to find discussions.
            </div>
        )}
      </div>
    </div>
  );
};

export default ThreadSpotterView;
