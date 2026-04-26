import React, { useState } from 'react';
import axios from 'axios';
import UploadSection from './components/UploadSection';
import ResultsSection from './components/ResultsSection';

function App() {
  const [file, setFile] = useState(null);
  const [loading, setLoading] = useState(false);
  const [results, setResults] = useState(null);
  const [error, setError] = useState(null);

  const handleAnalyze = async () => {
    if (!file) {
      setError("Please select a resume file.");
      return;
    }
    
    setLoading(true);
    setError(null);
    setResults(null);

    const formData = new FormData();
    formData.append('resume', file);

    try {
      const response = await axios.post('http://localhost:8000/api/analyze/', formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      });
      setResults(response.data);
    } catch (err) {
      console.error(err);
      setError(err.response?.data?.error || "An error occurred during analysis.");
    } finally {
      setLoading(false);
    }
  };

  const handleReset = () => {
    setFile(null);
    setResults(null);
    setError(null);
  };

  return (
    <div className="container">
      <header className="header">
        <h1>AI Resume Analyzer</h1>
        <p>Upload your resume and discover your top career matches dynamically.</p>
      </header>

      {!results ? (
        <UploadSection 
          file={file} 
          setFile={setFile} 
          loading={loading} 
          onAnalyze={handleAnalyze} 
          error={error}
        />
      ) : (
        <ResultsSection 
          matches={results.top_matches} 
          onReset={handleReset} 
        />
      )}
    </div>
  );
}

export default App;
