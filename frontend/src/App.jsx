import React, { useState } from "react";
import "./App.css";

function App() {
  const [cvFile, setCvFile] = useState(null);
  const [message, setMessage] = useState("");
  const [recommendations, setRecommendations] = useState([]);

  const handleFileChange = (event) => {
    const file = event.target.files[0];

    if (file) {
      setCvFile(file);
      setMessage("");
      setRecommendations([]);
    }
  };

  const handleAnalyze = async () => {
    if (!cvFile) {
      setMessage("Please upload your CV first.");
      return;
    }

    setMessage("Analyzing your CV...");
    setRecommendations([]);

    try {
      const formData = new FormData();
      formData.append("cv", cvFile);

      const response = await fetch(
        "http://127.0.0.1:5000/api/analyze",
        {
          method: "POST",
          body: formData,
        }
      );

      const data = await response.json();

      console.log("Backend response:", data);

      if (!response.ok) {
        throw new Error(data.error || "CV analysis failed.");
      }

      setRecommendations(data.recommendations || []);
      setMessage("CV analyzed successfully!");

    } catch (error) {
      console.error("Backend error:", error);
      setMessage(`Backend connection error: ${error.message}`);
    }
  };

  return (
    <div className="app">

      {/* Navbar */}
      <nav className="navbar">
        <div className="logo">CVMatch AI</div>

        <div className="nav-links">
          <a href="#home">Home</a>
          <a href="#how-it-works">How It Works</a>
          <a href="#features">Features</a>
          <a href="#about">About</a>
        </div>
      </nav>

      {/* Hero Section */}
      <section className="hero" id="home">
        <div className="hero-content">

          <div className="badge">
            AI-Powered Job Recommendation
          </div>

          <h1>
            Find Your Perfect Job with <span>CVMatch AI</span>
          </h1>

          <p>
            Upload your CV and let AI analyze your skills,
            experience, and profile to find the most relevant
            job opportunities for you.
          </p>

          {/* Upload Box */}
          <div className="upload-box">

            <div className="upload-icon">
              📄
            </div>

            <h2>Upload Your CV</h2>

            <p>
              Upload your resume in PDF or DOCX format
            </p>

            <label className="choose-button">
              Choose CV

              <input
                type="file"
                accept=".pdf,.doc,.docx"
                onChange={handleFileChange}
                hidden
              />
            </label>

            {cvFile && (
              <div className="selected-file">
                Selected: {cvFile.name}
              </div>
            )}

            <button
              className="analyze-button"
              onClick={handleAnalyze}
            >
              Analyze CV
            </button>

            {message && (
              <div className="message">
                {message}
              </div>
            )}

          </div>
        </div>
      </section>

      {/* Recommendations */}
      {recommendations.length > 0 && (
        <section className="recommendations">
          <h2>Recommended Jobs</h2>

          <div className="job-list">
            {recommendations.map((job, index) => (
              <div className="job-card" key={index}>

                <h3>
                  {job.title || job.job_title || "Job Opportunity"}
                </h3>

                {job.company && (
                  <p>
                    <strong>Company:</strong> {job.company}
                  </p>
                )}

                {job.location && (
                  <p>
                    <strong>Location:</strong> {job.location}
                  </p>
                )}

                {job.match_percentage !== undefined && (
                  <p>
                    <strong>Match:</strong>{" "}
                    {job.match_percentage}%
                  </p>
                )}

                {job.description && (
                  <p>{job.description}</p>
                )}

              </div>
            ))}
          </div>
        </section>
      )}

      {/* How It Works */}
      <section className="how-it-works" id="how-it-works">
        <h2>How It Works</h2>

        <div className="steps">

          <div className="step-card">
            <div className="step-number">1</div>

            <h3>Upload CV</h3>

            <p>
              Upload your CV and provide your professional profile.
            </p>
          </div>

          <div className="step-card">
            <div className="step-number">2</div>

            <h3>AI Analysis</h3>

            <p>
              Our AI analyzes your skills, experience and CV content.
            </p>
          </div>

          <div className="step-card">
            <div className="step-number">3</div>

            <h3>Get Recommendations</h3>

            <p>
              Receive job recommendations matching your profile.
            </p>
          </div>

        </div>
      </section>

      {/* Features */}
      <section className="features" id="features">
        <h2>Features</h2>

        <div className="feature-card">
          <div className="feature-icon">🤖</div>

          <h3>AI Powered Matching</h3>

          <p>
            Uses AI to understand your CV and match it
            with relevant jobs.
          </p>
        </div>

        <div className="feature-card">
          <div className="feature-icon">🎯</div>

          <h3>Smart Recommendations</h3>

          <p>
            Get personalized job recommendations based
            on your profile.
          </p>
        </div>

        <div className="feature-card">
          <div className="feature-icon">⚡</div>

          <h3>Fast Analysis</h3>

          <p>
            Analyze your CV and discover opportunities quickly.
          </p>
        </div>

      </section>

      {/* About */}
      <section className="about" id="about">
        <h2>About CVMatch AI</h2>

        <p>
          CVMatch AI is an intelligent job recommendation
          system designed to help job seekers discover
          opportunities that match their skills and experience.
        </p>
      </section>

      {/* Footer */}
      <footer>
        <p>
          © 2026 CVMatch AI. All rights reserved.
        </p>
      </footer>

    </div>
  );
}

export default App;