import React, { useState } from "react";
import { sendEmail, scheduleTask, fetchResearch } from "./api";

function App() {
  const [email, setEmail] = useState({ recipient: "", subject: "", body: "" });
  const [task, setTask] = useState({ event_title: "", event_time: "" });
  const [research, setResearch] = useState("");
  const [researchResult, setResearchResult] = useState("");

  return (
    <div>
      <h1>Multi-Agent Dashboard</h1>
      <button onClick={() => sendEmail(email)}>Send Email</button>
      <button onClick={() => scheduleTask(task)}>Schedule Task</button>
      <button onClick={() => fetchResearch(research)}>Fetch Research</button>
      <p>{researchResult}</p>
    </div>
  );
}

export default App;

