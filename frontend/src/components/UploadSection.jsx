import React, { useRef } from 'react';
import { UploadCloud, FileText, Loader2, Search } from 'lucide-react';

const UploadSection = ({ file, setFile, loading, onAnalyze, error }) => {
  const fileInputRef = useRef(null);

  const handleFileChange = (e) => {
    if (e.target.files && e.target.files[0]) {
      setFile(e.target.files[0]);
    }
  };

  const handleDrop = (e) => {
    e.preventDefault();
    if (e.dataTransfer.files && e.dataTransfer.files[0]) {
      setFile(e.dataTransfer.files[0]);
    }
  };

  const handleDragOver = (e) => {
    e.preventDefault();
  };

  return (
    <div className="glass-card upload-container">
      <div className="form-group">
        <label>Upload Resume (PDF/DOCX)</label>
        <div 
          className="dropzone" 
          onClick={() => fileInputRef.current.click()}
          onDrop={handleDrop}
          onDragOver={handleDragOver}
        >
          {file ? (
            <div>
              <FileText className="dropzone-icon" />
              <h3>{file.name}</h3>
              <p style={{ marginTop: '0.5rem', color: 'var(--text-secondary)' }}>Click or drag to replace</p>
            </div>
          ) : (
            <div>
              <UploadCloud className="dropzone-icon" />
              <h3>Drag & drop your resume here</h3>
              <p style={{ marginTop: '0.5rem', color: 'var(--text-secondary)' }}>or click to browse files</p>
            </div>
          )}
          <input 
            type="file" 
            ref={fileInputRef} 
            onChange={handleFileChange} 
            accept=".pdf,.docx,.doc" 
            style={{ display: 'none' }}
          />
        </div>
      </div>

      {error && <div style={{ color: '#fb7185', textAlign: 'center', fontWeight: '500' }}>{error}</div>}

      <button 
        className="btn btn-primary" 
        onClick={onAnalyze} 
        disabled={!file || loading}
        style={{ marginTop: '1rem' }}
      >
        {loading ? (
          <>
            <Loader2 className="loading-spinner" /> Analyzing 26+ Roles...
          </>
        ) : (
          <>
            <Search size={20} /> Analyze Match
          </>
        )}
      </button>
    </div>
  );
};

export default UploadSection;
