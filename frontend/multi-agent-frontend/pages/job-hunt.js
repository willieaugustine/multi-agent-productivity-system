import { useState } from "react";
import axios from "axios";
import Navbar from "../components/Navbar";

export default function JobHunt() {
  const [keyword, setKeyword] = useState("");
  const [location, setLocation] = useState("");
  const [jobs, setJobs] = useState([]);

  const searchJobs = async () => {
    const response = await axios.post("https://your-backend-url.com/scrape-jobs/", { keyword, location });
    setJobs(response.data);
  };

  return (
    <div className="bg-gray-100 min-h-screen">
      <Navbar />
      <div className="max-w-lg mx-auto p-6 bg-white shadow-lg mt-10 rounded-lg">
        <h2 className="text-2xl font-bold text-center mb-4">Job Hunt Automation</h2>
        <input className="border p-2 w-full mb-2" placeholder="Job title" onChange={(e) => setKeyword(e.target.value)} />
        <input className="border p-2 w-full mb-2" placeholder="Location" onChange={(e) => setLocation(e.target.value)} />
        <button className="bg-blue-600 text-white px-4 py-2 rounded w-full" onClick={searchJobs}>Search Jobs</button>
        
        <ul className="mt-4">
          {jobs.map((job, index) => (
            <li key={index} className="p-2 border-b">{job.title} - {job.company} <a href={job.link} className="text-blue-600">Apply</a></li>
          ))}
        </ul>
      </div>
    </div>
  );
}

