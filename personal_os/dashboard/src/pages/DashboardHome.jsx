import React, { useEffect, useState } from 'react';
import ChatWidget from '../components/ChatWidget';
import { BentoCard } from '../components/bento/BentoCard';

const DashboardHome = () => {
  const [tasks, setTasks] = useState([]);
  const [events, setEvents] = useState([]);

  useEffect(() => {
    fetch('http://localhost:8000/api/tasks')
      .then(res => res.json())
      .then(data => setTasks(data.tasks || []))
      .catch(err => console.error("Failed to fetch tasks", err));

    fetch('http://localhost:8000/api/calendar')
      .then(res => res.json())
      .then(data => setEvents(data.events || []))
      .catch(err => console.error("Failed to fetch calendar", err));
  }, []);

  return (
    <div className="space-y-8 relative z-10 max-w-7xl mx-auto">
      <header className="mb-12 text-center">
        <h1 className="text-5xl font-bold bg-clip-text text-transparent bg-gradient-to-b from-white to-white/60 tracking-tight">
          Command Center
        </h1>
        <p className="text-white/60 mt-4 text-lg">Your Personal OS is online and monitoring.</p>
      </header>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
        {/* Tasks Widget */}
        <BentoCard 
            title="Active Tasks" 
            icon="✅" 
            className="min-h-[300px]"
        >
          <div className="space-y-3 mt-2">
            {tasks.length === 0 ? (
              <p className="text-white/40 italic">No active tasks.</p>
            ) : (
              tasks.map(task => (
                <div key={task.id} className="flex items-center justify-between p-3 bg-white/5 rounded-lg hover:bg-white/10 transition-colors border border-white/5">
                  <span className="text-white/90">{task.title}</span>
                  <span className="text-xs px-2 py-1 bg-blue-500/20 text-blue-300 rounded border border-blue-500/30">{task.status}</span>
                </div>
              ))
            )}
          </div>
        </BentoCard>

        {/* Calendar Widget */}
        <BentoCard 
            title="Schedule" 
            icon="📅" 
            className="min-h-[300px]"
        >
          <div className="space-y-3 mt-2">
            {events.length === 0 ? (
              <p className="text-white/40 italic">No upcoming events.</p>
            ) : (
              events.map(event => (
                <div key={event.id} className="p-3 bg-white/5 rounded-lg border-l-2 border-purple-500 hover:bg-white/10 transition-colors">
                  <div className="font-medium text-white/90">{event.title}</div>
                  <div className="text-sm text-white/50 mt-1">
                    {new Date(event.start).toLocaleTimeString([], {hour: '2-digit', minute:'2-digit'})} - 
                    {new Date(event.end).toLocaleTimeString([], {hour: '2-digit', minute:'2-digit'})}
                  </div>
                </div>
              ))
            )}
          </div>
        </BentoCard>
      </div>

      <ChatWidget />
    </div>
  );
};

export default DashboardHome;
