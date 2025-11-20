```
import React, { useState, useRef, useEffect } from 'react';
import { MessageSquare, X, Send, Loader2 } from 'lucide-react';
import { cn } from '../lib/utils';

const ChatWidget = () => {
  const [isOpen, setIsOpen] = useState(false);
  const [messages, setMessages] = useState([
    { role: 'assistant', content: 'Hello! I am your Personal OS Co-pilot. How can I help you today?' }
  ]);
  const [input, setInput] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const messagesEndRef = useRef(null);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages, isOpen]);

  const sendMessage = async () => {
    if (!input.trim()) return;

    const userMessage = { role: 'user', content: input };
    setMessages(prev => [...prev, userMessage]);
    setInput('');
    setIsLoading(true);

    try {
      const response = await fetch('http://localhost:8000/api/chat', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ message: input })
      });
      
      const data = await response.json();
      const aiMessage = { role: 'assistant', content: data.response };
      setMessages(prev => [...prev, aiMessage]);
    } catch (error) {
      console.error('Error sending message:', error);
      setMessages(prev => [...prev, { role: 'assistant', content: 'Sorry, I encountered an error processing your request.' }]);
    } finally {
      setIsLoading(false);
    }
  };

  const handleKeyPress = (e) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      sendMessage();
    }
  };

  return (
    <div className="fixed bottom-6 right-6 z-50 flex flex-col items-end">
      {isOpen && (
        <div className="mb-4 w-96 h-[500px] flex flex-col rounded-2xl border border-white/10 bg-black/60 backdrop-blur-xl shadow-2xl overflow-hidden transition-all duration-300 origin-bottom-right animate-in fade-in zoom-in-95">
          {/* Header */}
          <div className="p-4 border-b border-white/10 flex justify-between items-center bg-white/5">
            <div className="flex items-center gap-2">
              <div className="w-2 h-2 rounded-full bg-green-500 animate-pulse"></div>
              <h3 className="font-semibold text-white">Co-pilot</h3>
            </div>
            <button 
              onClick={() => setIsOpen(false)}
              className="text-white/50 hover:text-white transition-colors"
            >
              <X size={18} />
            </button>
          </div>

          {/* Messages */}
          <div className="flex-1 overflow-y-auto p-4 space-y-4 scrollbar-thin scrollbar-thumb-white/10 scrollbar-track-transparent">
            {messages.map((msg, index) => (
              <div 
                key={index} 
                className={cn(
                  "max-w-[85%] rounded-2xl px-4 py-3 text-sm leading-relaxed",
                  msg.role === 'user' 
                    ? "bg-white text-black ml-auto rounded-tr-sm" 
                    : "bg-white/10 text-white mr-auto rounded-tl-sm border border-white/5"
                )}
              >
                {msg.content}
              </div>
            ))}
            {isLoading && (
              <div className="flex items-center gap-2 text-white/50 text-xs ml-2">
                <Loader2 size={12} className="animate-spin" />
                <span>Thinking...</span>
              </div>
            )}
            <div ref={messagesEndRef} />
          </div>

          {/* Input */}
          <div className="p-4 border-t border-white/10 bg-white/5">
            <div className="relative flex items-center">
              <input
                type="text"
                value={input}
                onChange={(e) => setInput(e.target.value)}
                onKeyDown={handleKeyPress}
                placeholder="Type a message..."
                className="w-full bg-black/20 border border-white/10 rounded-xl pl-4 pr-12 py-3 text-sm text-white placeholder-white/30 focus:outline-none focus:border-white/20 focus:bg-black/40 transition-all"
              />
              <button 
                onClick={sendMessage}
                disabled={!input.trim() || isLoading}
                className="absolute right-2 p-1.5 bg-white/10 rounded-lg text-white/70 hover:text-white hover:bg-white/20 disabled:opacity-50 disabled:cursor-not-allowed transition-all"
              >
                <Send size={16} />
              </button>
            </div>
          </div>
        </div>
      )}

      <button
        onClick={() => setIsOpen(!isOpen)}
        className={cn(
          "p-4 rounded-full shadow-lg transition-all duration-300 hover:scale-105 active:scale-95",
          isOpen 
            ? "bg-white/10 text-white border border-white/10 rotate-90" 
            : "bg-white text-black hover:bg-gray-200"
        )}
      >
        {isOpen ? <X size={24} /> : <MessageSquare size={24} />}
      </button>
    </div>
  );
};

export default ChatWidget;
```
