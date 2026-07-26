import { Files, Bug, Shield, Star } from "lucide-react";
import type { AnalysisResponse } from "../types/analysis";

type DashboardStatsProps = {
  result: AnalysisResponse;
};

export default function DashboardStats({ result }: DashboardStatsProps) {
  const healthScore = result.health?.score ?? 0;

  return (
    <div className="mx-auto mt-8 grid max-w-7xl gap-6 px-8 md:grid-cols-2 xl:grid-cols-4">
      <StatCard
        icon={<Files className="h-7 w-7 text-blue-600" />}
        title="Total Files"
        value={String(result.analysis?.total_files ?? 0)}
        color="bg-blue-50"
      />

      <StatCard
        icon={<Bug className="h-7 w-7 text-red-600" />}
        title="Bugs Found"
        value={String(result.bugs?.length ?? 0)}
        color="bg-red-50"
      />

      <StatCard
        icon={<Shield className="h-7 w-7 text-green-600" />}
        title="Security Issues"
        value={String(result.security?.length ?? 0)}
        color="bg-green-50"
      />

      <StatCard
        icon={<Star className="h-7 w-7 text-yellow-600" />}
        title="Health Score"
        value={`${healthScore}%`}
        color="bg-yellow-50"
      />
    </div>
  );
}

type StatCardProps = {
  icon: React.ReactNode;
  title: string;
  value: string;
  color: string;
};

function StatCard({ icon, title, value, color }: StatCardProps) {
  return (
    <div className={`rounded-3xl border border-slate-200 ${color} p-6 shadow-sm`}>
      <div className="flex items-center justify-between">
        <div>
          <p className="text-sm text-slate-500">{title}</p>
          <h2 className="mt-2 text-3xl font-bold text-slate-900">{value}</h2>
        </div>
        {icon}
      </div>
    </div>
  );
}