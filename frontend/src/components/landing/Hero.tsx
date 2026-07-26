import { Search } from "lucide-react";

export default function Hero() {
  return (
    <section className="w-full flex flex-col items-center text-center pt-20">

      <div className="flex h-20 w-20 items-center justify-center rounded-full bg-blue-50 border border-blue-100 shadow-md">
        <Search className="h-10 w-10 text-blue-600" strokeWidth={2.5} />
      </div>

      <h1 className="mt-8 text-7xl font-extrabold tracking-tight text-slate-900">
        Lensify
      </h1>

      <h2 className="mt-4 text-3xl font-bold text-blue-600">
        See Beyond the Code
      </h2>

      <p className="mt-8 max-w-3xl text-lg leading-8 text-slate-500">
        Understand any software project with AI. Upload a ZIP file to receive
        architecture, bug detection, code quality analysis, and intelligent
        project insights.
      </p>

    </section>
  );
}