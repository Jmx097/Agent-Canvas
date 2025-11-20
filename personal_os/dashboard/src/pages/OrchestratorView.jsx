import React, { useState, useEffect } from 'react';

const OrchestratorView = () => {
  const [plan, setPlan] = useState("");
  const [loading, setLoading] = useState(false);

  const fetchPlan = async () => {
    setLoading(true);
    try {
        const res = await fetch('http://localhost:8000/api/plan');
        const data = await res.json();
        setPlan(data.content || "No plan generated yet.");
    } catch (err) {
        setPlan("Error fetching plan.");
    } finally {
        setLoading(false);
    }
  };

  const generatePlan = async () => {
    setLoading(true);
    try {
        await fetch('http://localhost:8000/api/run/orchestrator', { method: 'POST' });
        await fetchPlan();
    } catch (err) {
        console.error("Failed to generate plan", err);
    } finally {
        setLoading(false);
    }
  };

  useEffect(() => {
    fetchPlan();
  }, []);

  return (
    <div className="space-y-6 h-full flex flex-col">
      <header className="flex justify-between items-center mb-4">
        <div>
            <h1 className="text-3xl font-bold text-white">Orchestrator</h1>
            <p className="text-gray-400">Daily planning and executive function.</p>
        </div>
        <button 
            onClick={generatePlan} 
            disabled={loading}
            className="px-4 py-2 bg-green-600 hover:bg-green-500 text-white rounded-lg transition-colors disabled:opacity-50 flex items-center gap-2"
        >
            {loading ? (
                <>
                    <span className="animate-spin">⚙️</span> Generating...
                </>
            ) : (
                <>
                    <span>⚡</span> Generate Daily Plan
                </>
            )}
        </button>
      </header>

      <div className="flex-1 bg-white/5 border border-white/10 rounded-xl p-6 backdrop-blur-sm overflow-auto">
        {loading && !plan ? (
            <div className="flex items-center justify-center h-full text-gray-500">
                Generating your plan...
            </div>
        ) : (
            <div className="prose prose-invert max-w-none">
                <pre className="whitespace-pre-wrap font-mono text-sm text-gray-300 bg-transparent border-none p-0">
                    {plan}
                </pre>
            </div>
        )}
      </div>
    </div>
  );
};

export default OrchestratorView;
