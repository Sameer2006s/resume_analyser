import React from 'react';
import { CheckCircle, XCircle, ArrowLeft, Lightbulb, Trophy } from 'lucide-react';

const MatchCard = ({ match, isPrimary }) => {
  const { role, match_percentage, matched_skills, missing_skills, suggestions } = match;

  return (
    <div className={`glass-card match-card ${isPrimary ? 'primary-match' : 'secondary-match'}`} style={{ marginBottom: '2rem' }}>
      <div className="match-header" style={{ display: 'flex', alignItems: 'center', gap: '2rem', marginBottom: '2rem', flexWrap: 'wrap' }}>
        <div className="score-circle" style={{ '--percentage': match_percentage, width: isPrimary ? '150px' : '100px', height: isPrimary ? '150px' : '100px', fontSize: isPrimary ? '3rem' : '2rem' }}>
          <span className="score-value">{match_percentage}%</span>
        </div>
        <div>
          <h2 style={{ fontSize: isPrimary ? '2.5rem' : '1.8rem', display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
            {isPrimary && <Trophy color="var(--accent-warning)" />} {role}
          </h2>
          <p style={{ color: 'var(--text-secondary)', marginTop: '0.5rem' }}>
            {isPrimary ? 'Your strongest career match!' : 'Great alternative career path.'}
          </p>
        </div>
      </div>

      <div className="results-grid" style={{ gridTemplateColumns: isPrimary ? '1fr 1fr' : '1fr', gap: '2rem', marginTop: '0' }}>
        <div>
          <div className="section-title">
            <CheckCircle color="var(--accent-success)" /> 
            <h3 style={{ fontSize: '1.2rem' }}>Matched Skills</h3>
          </div>
          {matched_skills.length > 0 ? (
            <div className="skills-container">
              {matched_skills.map(skill => (
                <span key={skill} className="skill-pill matched">{skill}</span>
              ))}
            </div>
          ) : (
            <p style={{ color: 'var(--text-secondary)', marginBottom: '1.5rem' }}>No matching skills found.</p>
          )}

          <div className="section-title">
            <XCircle color="#fb7185" /> 
            <h3 style={{ fontSize: '1.2rem' }}>Missing Skills</h3>
          </div>
          {missing_skills.length > 0 ? (
            <div className="skills-container">
              {missing_skills.map(skill => (
                <span key={skill} className="skill-pill missing">{skill}</span>
              ))}
            </div>
          ) : (
            <p style={{ color: 'var(--text-secondary)', marginBottom: '1.5rem' }}>You have all the core required skills!</p>
          )}
        </div>

        <div>
          <div className="section-title">
            <Lightbulb color="var(--accent-warning)" />
            <h3 style={{ fontSize: '1.2rem' }}>Suggestions</h3>
          </div>
          <ul className="suggestions-list">
            {suggestions.map((sug, i) => (
              <li key={i}>{sug}</li>
            ))}
          </ul>
        </div>
      </div>
    </div>
  );
};

const ResultsSection = ({ matches, onReset }) => {
  return (
    <div>
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '2rem' }}>
        <h2 style={{ fontSize: '2rem' }}>Top Career Matches</h2>
        <button className="btn" onClick={onReset} style={{ padding: '0.5rem 1rem', background: 'rgba(255,255,255,0.1)', color: 'white' }}>
          <ArrowLeft size={18} /> Back
        </button>
      </div>

      {matches.map((match, index) => (
        <MatchCard key={match.role} match={match} isPrimary={index === 0} />
      ))}
    </div>
  );
};

export default ResultsSection;
