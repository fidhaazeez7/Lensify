import { Boxes } from "lucide-react";

import type {
  AnalysisData,
  ArchitectureData,
  TechnologyData,
} from "../../types/analysis";

type ArchitectureTabProps = {
  analysis: AnalysisData;
  technology: TechnologyData;
  architecture: ArchitectureData;
};

export default function ArchitectureTab({
  analysis,
  technology,
  architecture,
}: ArchitectureTabProps) {
  const frameworks = architecture?.frameworks;

  const frontend =
    technology.dependencies.frontend.join(", ") ||
    frameworks?.frontend ||
    analysis.frontend ||
    "Unknown";

  const backend =
    technology.dependencies.backend.join(", ") ||
    frameworks?.backend ||
    analysis.backend ||
    "Unknown";

  const database =
    technology.dependencies.database.join(", ") ||
    frameworks?.database ||
    analysis.database ||
    "Unknown";

  const authentication =
    technology.dependencies.authentication.join(", ") ||
    analysis.authentication ||
    "Unknown";

  const deployment =
    technology.dependencies.deployment.join(", ") ||
    frameworks?.deployment ||
    analysis.deployment ||
    "Unknown";

  return (
    <div className="mx-auto mt-10 max-w-7xl px-8">
      <div className="rounded-3xl border border-slate-200 bg-white p-8 shadow-sm">

        {/* Header */}
        <div className="flex items-center gap-3">
          <div className="flex h-12 w-12 items-center justify-center rounded-xl bg-purple-50">
            <Boxes className="h-6 w-6 text-purple-600" />
          </div>

          <div>
            <h2 className="text-3xl font-bold text-slate-900">
              Project Architecture
            </h2>

            <p className="text-slate-500">
              Automatically detected architecture
            </p>
          </div>
        </div>

        {/* Project Name */}
        <div className="mt-12 flex flex-col items-center">

          <div className="rounded-xl bg-blue-600 px-8 py-4 text-white shadow-lg">
            <h3 className="text-lg font-semibold">
              {analysis.project_name}
            </h3>
          </div>

          <div className="my-6 h-10 w-1 bg-slate-300"></div>

          {/* Architecture Summary */}
          <div className="grid w-full max-w-5xl grid-cols-2 gap-6">

            <div className="rounded-2xl border border-indigo-200 bg-indigo-50 p-6">
              <h3 className="text-lg font-bold text-indigo-700">
                Architecture
              </h3>

              <p className="mt-3 text-slate-700">
                {architecture.architecture || "Unknown"}
              </p>
            </div>

            <div className="rounded-2xl border border-cyan-200 bg-cyan-50 p-6">
              <h3 className="text-lg font-bold text-cyan-700">
                Pattern
              </h3>

              <p className="mt-3 text-slate-700">
                {architecture.pattern || "Unknown"}
              </p>
            </div>

          </div>

          <div className="my-8 h-10 w-1 bg-slate-300"></div>

          {/* Technology Stack */}
          <div className="grid w-full max-w-6xl grid-cols-2 gap-6 md:grid-cols-3">

            <TechCard
              title="Frontend"
              color="blue"
              value={frontend}
            />

            <TechCard
              title="Backend"
              color="green"
              value={backend}
            />

            <TechCard
              title="Database"
              color="purple"
              value={database}
            />

            <TechCard
              title="Communication"
              color="sky"
              value={frameworks?.communication || "REST API"}
            />

            <TechCard
              title="Authentication"
              color="yellow"
              value={authentication}
            />

            <TechCard
              title="Deployment"
              color="orange"
              value={deployment}
            />

          </div>

        </div>

        {/* AI Explanation */}
        <div className="mt-12 rounded-2xl bg-slate-50 p-6">

          <h3 className="text-xl font-bold">
            🤖 AI Explanation
          </h3>

          <p className="mt-4 leading-8 text-slate-600">

            Lensify detected a{" "}
            <strong>{architecture.architecture || "software"}</strong>{" "}
            project following the{" "}
            <strong>{architecture.pattern || "standard"}</strong>{" "}
            architecture pattern.

            <br /><br />

            Frontend:
            <strong> {frontend}</strong>

            <br />

            Backend:
            <strong> {backend}</strong>

            <br />

            Database:
            <strong> {database}</strong>

            <br />

            Authentication:
            <strong> {authentication}</strong>

            <br />

            Deployment:
            <strong> {deployment}</strong>

          </p>

        </div>

      </div>
    </div>
  );
}

type TechCardProps = {
  title: string;
  value: string;
  color: string;
};

function TechCard({
  title,
  value,
  color,
}: TechCardProps) {
  return (
    <div
      className={`rounded-2xl border border-${color}-200 bg-${color}-50 p-6 text-center`}
    >
      <h3 className={`text-xl font-bold text-${color}-700`}>
        {title}
      </h3>

      <p className="mt-2 break-words text-slate-600">
        {value}
      </p>
    </div>
  );
}