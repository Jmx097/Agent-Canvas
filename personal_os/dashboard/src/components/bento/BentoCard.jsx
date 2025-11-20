import React from 'react';
import { cn } from '../../lib/utils';

export function BentoCard({
  title,
  subtitle,
  icon,
  className,
  children,
  onClick
}) {
  return (
    <div
      className={cn(
        'group relative overflow-hidden rounded-2xl border border-white/10 bg-white/5 p-5 text-left backdrop-blur-sm transition transform hover:border-white/20 hover:bg-white/[.07]',
        className
      )}
      onClick={onClick}
    >
      <div className="absolute inset-0 transition opacity-100 group-hover:opacity-90" aria-hidden />
      <div className="relative z-10 flex h-full flex-col text-white">
        <div className="flex items-center gap-3 mb-2">
          {icon && <span className="text-xl opacity-80">{icon}</span>}
          <h3 className="text-lg font-semibold">{title}</h3>
        </div>
        {subtitle && <p className="text-sm text-white/70 mb-4">{subtitle}</p>}
        
        <div className="flex-1">
            {children}
        </div>
        
        <div className="pointer-events-none absolute -inset-10 rotate-6 bg-gradient-to-r from-transparent via-white/10 to-transparent blur-2xl opacity-0 group-hover:opacity-100 transition-opacity duration-500" />
      </div>
    </div>
  );
}
