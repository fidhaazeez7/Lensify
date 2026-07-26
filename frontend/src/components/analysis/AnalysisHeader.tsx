import {
  Sparkles,
  FolderGit2,
  Calendar,
  Cpu,
} from "lucide-react";

export default function AnalysisHeader() {
  return (
    <header className="border-b border-slate-200 bg-white shadow-sm">
      <div className="mx-auto flex max-w-7xl items-center justify-between px-8 py-8">

        {/* Left */}

        <div>

          <div className="flex items-center gap-3">

            <div className="flex h-14 w-14 items-center justify-center rounded-2xl bg-blue-600">

              <Sparkles className="h-7 w-7 text-white" />

            </div>

            <div>

              <h1 className="text-4xl font-bold text-slate-900">
                Lensify AI Analysis
              </h1>

              <p className="mt-1 text-slate-500">
                Intelligent Software Project Analyzer
              </p>

            </div>

          </div>

        </div>

        {/* Right */}

        <div className="hidden gap-6 lg:flex">

          <InfoCard
            icon={<FolderGit2 className="h-5 w-5 text-blue-600" />}
            title="Project"
            value="Analyzed"
          />

          <InfoCard
            icon={<Calendar className="h-5 w-5 text-green-600" />}
            title="Status"
            value="Completed"
          />

          <InfoCard
            icon={<Cpu className="h-5 w-5 text-purple-600" />}
            title="AI Engine"
            value="Gemini 2.5"
          />

        </div>

      </div>
    </header>
  );
}

type InfoCardProps = {
  icon: React.ReactNode;
  title: string;
  value: string;
};

function InfoCard({
  icon,
  title,
  value,
}: InfoCardProps) {
  return (
    <div className="flex items-center gap-3 rounded-2xl border border-slate-200 bg-slate-50 px-5 py-3">

      {icon}

      <div>

        <p className="text-xs text-slate-500">
          {title}
        </p>

        <p className="font-semibold text-slate-900">
          {value}
        </p>

      </div>

    </div>
  );
}