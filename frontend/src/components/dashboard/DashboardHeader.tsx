import { Search } from "lucide-react";

export default function DashboardHeader() {
  return (
    <header className="bg-white border-b border-slate-200 px-8 py-5">

      <div className="max-w-7xl mx-auto flex items-center justify-between">

        {/* Left */}
        <div className="flex items-center gap-4">

          <div className="flex h-12 w-12 items-center justify-center rounded-full bg-blue-50">
            <Search className="h-6 w-6 text-blue-600" />
          </div>

          <div>
            <h1 className="text-2xl font-bold text-slate-900">
              Lensify Dashboard
            </h1>

            <p className="text-slate-500">
              ecommerce-platform.zip
            </p>
          </div>

        </div>

        {/* Right */}

        <div className="text-right">

          <p className="text-sm text-slate-500">
            Last Analysis
          </p>

          <p className="font-semibold text-slate-900">
            Just Now
          </p>

        </div>

      </div>

    </header>
  );
}