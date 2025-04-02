import Navbar from "../components/Navbar";

export default function Home() {
  return (
    <div className="bg-gray-100 min-h-screen">
      <Navbar />
      <div className="text-center mt-10">
        <h2 className="text-3xl font-bold">Multi-Agent AI Dashboard</h2>
        <p className="text-gray-600">Automate job hunting, social media, and productivity tasks.</p>
      </div>
    </div>
  );
}

