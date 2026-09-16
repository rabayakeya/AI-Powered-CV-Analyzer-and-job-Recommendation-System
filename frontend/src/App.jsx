import { useState } from "react";
import "./App.css";

function App() {
  const [cvFile, setCvFile] = useState(null);
  const [message, setMessage] = useState("");

  const handleFileChange = (event) => {
    const file = event.target.files[0];

    if (!file) {
      return;
    }

    if (file.type !== "application/pdf") {
      setMessage("Please upload a PDF file.");
      setCvFile(null);
      return;
    }

    setCvFile(file);
    setMessage("");
  };

  const handleAnalyze = () => {
    if (!cvFile) {
      setMessage("Please select your CV first.");
      return;
    }

    setMessage(
      "CV selected successfully. Backend connection will be added next."
    );
  };

  return (
    <div className="app">
      <nav className="navbar">
        <div className="logo">CVMatch AI</div>

        <div className="nav-links">
          <a href="#home">Home</a>
          <a href="#how-it-works">How It Works</a>
          <a href="#about">About</a>
        </div>
      </nav>

      <section className="hero" id="home">
        <div className="hero-content">
          <div className="badge">AI-Powered Career Assistant</div>

          <h1>
            Find the Right Job
            <br />
            <span>With Your CV</span>
          </h1>

          <p>
            Upload your CV and let our AI analyse your skills,
            experience, and qualifications to find suitable job
            opportunities.
          </p>

          <div className="upload-box">
            <div className="upload-icon">📄</div>

            <h2>Upload Your CV</h2>

            <p>Upload your CV in PDF format</p>

            <label className="choose-button">
              Choose CV
              <input
                type="file"
                accept=".pdf,application/pdf"
                onChange={handleFileChange}
                hidden
              />
            </label>

            {cvFile && (
              <div className="selected-file">
                <strong>Selected CV:</strong>
                <br />
                {cvFile.name}
              </div>
            )}

            <button
              className="analyze-button"
              onClick={handleAnalyze}
            >
              Analyze My CV
            </button>

            {message && <div className="message">{message}</div>}
          </div>
        </div>
      </section>

      <section className="how-it-works" id="how-it-works">
        <h2>How CVMatch AI Works</h2>

        <p className="section-description">
          Our system analyses your CV and compares your skills
          with available job opportunities.
        </p>

        <div className="steps">
          <div className="step-card">
            <div className="step-number">1</div>
            <h3>Upload CV</h3>
            <p>Upload your CV as a PDF file to the system.</p>
          </div>

          <div className="step-card">
            <div className="step-number">2</div>
            <h3>AI Analysis</h3>
            <p>
              The system extracts information and identifies
              relevant skills from your CV.
            </p>
          </div>

          <div className="step-card">
            <div className="step-number">3</div>
            <h3>Job Recommendations</h3>
            <p>
              AI compares your CV with jobs and recommends
              suitable positions.
            </p>
          </div>
        </div>
      </section>

      <section className="features">
        <h2>What Our System Provides</h2>

        <div className="feature-grid">
          <div className="feature-card">
            <div className="feature-icon">📄</div>
            <h3>CV Analysis</h3>
            <p>
              Extract important information and skills from your
              uploaded CV.
            </p>
          </div>

          <div className="feature-card">
            <div className="feature-icon">🤖</div>
            <h3>AI Job Matching</h3>
            <p>
              Compare your CV with job descriptions using machine
              learning techniques.
            </p>
          </div>

          <div className="feature-card">
            <div className="feature-icon">🎯</div>
            <h3>Skill Matching</h3>
            <p>
              Identify matching skills between your CV and available
              jobs.
            </p>
          </div>

          <div className="feature-card">
            <div className="feature-icon">📊</div>
            <h3>Match Percentage</h3>
            <p>
              See how closely each job matches your CV and skills.
            </p>
          </div>
        </div>
      </section>

      <section className="about" id="about">
        <h2>About CVMatch AI</h2>

        <p>
          CVMatch AI is an AI-powered CV analyser and job
          recommendation system. The application helps job seekers
          understand their skills and discover relevant job
          opportunities based on their CV.
        </p>
      </section>

      <footer>
        <p>© 2026 CVMatch AI</p>
        <p>AI-Powered CV Analyser and Job Recommendation System</p>
      </footer>
    </div>
  );
}

export default App;