import { Boxes, ArrowDown } from "lucide-react";

export default function ArchitectureCard() {
  return (
    <section className="rounded-3xl border border-slate-200 bg-white p-8 shadow-sm">

      {/* Header */}

      <div className="flex items-center gap-3">

        <div className="flex h-12 w-12 items-center justify-center rounded-xl bg-blue-50">
          <Boxes className="h-6 w-6 text-blue-600" />
        </div>

        <div>
          <h2 className="text-2xl font-bold text-slate-900">
            Project Architecture
          </h2>

          <p className="text-slate-500">
            AI-generated project structure
          </p>
        </div>

      </div>

      <div className="my-8 h-px bg-slate-200" />

      {/* Architecture Diagram */}

      <div className="flex flex-col items-center">

        {/* Root */}

        <div className="rounded-xl bg-blue-600 px-6 py-3 text-white font-semibold shadow">
          ecommerce-platform
        </div>

        <ArrowDown className="my-4 h-6 w-6 text-slate-400" />

        {/* Modules */}

        <div className="grid w-full grid-cols-3 gap-6">

          <div className="rounded-xl border border-blue-200 bg-blue-50 p-5 text-center">
            <h3 className="font-semibold text-slate-900">
              Frontend
            </h3>

            <p className="mt-2 text-sm text-slate-500">
              React
            </p>
          </div>

          <div className="rounded-xl border border-green-200 bg-green-50 p-5 text-center">
            <h3 className="font-semibold text-slate-900">
              Backend
            </h3>

            <p className="mt-2 text-sm text-slate-500">
              FastAPI
            </p>
          </div>

          <div className="rounded-xl border border-purple-200 bg-purple-50 p-5 text-center">
            <h3 className="font-semibold text-slate-900">
              Database
            </h3>

            <p className="mt-2 text-sm text-slate-500">
              PostgreSQL
            </p>
          </div>

        </div>

        <ArrowDown className="my-4 h-6 w-6 text-slate-400" />

        {/* Authentication */}

        <div className="rounded-xl border border-amber-200 bg-amber-50 px-8 py-4 text-center">

          <h3 className="font-semibold text-slate-900">
            Authentication
          </h3>

          <p className="mt-2 text-sm text-slate-500">
            JWT + OAuth
          </p>

        </div>

      </div>

    </section>
  );
}