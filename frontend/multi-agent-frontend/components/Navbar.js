import Link from "next/link";

const Navbar = () => (
  <nav className="bg-gray-900 text-white p-4 flex justify-between">
    <h1 className="text-xl font-bold">Multi-Agent AI</h1>
    <div className="space-x-4">
      <Link href="/">Dashboard</Link>
      <Link href="/job-hunt">Job Hunt</Link>
      <Link href="/social-media">Social Media</Link>
      <Link href="/virtual-assistant">Assistant</Link>
      <Link href="/productivity">Productivity</Link>
    </div>
  </nav>
);
export default Navbar;

