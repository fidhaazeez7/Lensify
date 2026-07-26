import {
  PieChart,
  Pie,
  Cell,
  ResponsiveContainer,
  Tooltip,
  BarChart,
  Bar,
  XAxis,
  YAxis,
  CartesianGrid,
} from "recharts";

import type { AnalysisResponse } from "../../types/analysis";

type Props = {
  result: AnalysisResponse;
};

const COLORS = [
  "#2563eb",
  "#16a34a",
  "#f59e0b",
  "#dc2626",
];

export default function DashboardCharts({
  result,
}: Props) {
  const bugData = [
    {
      name: "Bugs",
      value: result.bugs.length,
    },
    {
      name: "No Bugs",
      value: Math.max(0, 10 - result.bugs.length),
    },
  ];

  const securityData = [
    {
      name: "Issues",
      value: result.security.length,
    },
    {
      name: "Safe",
      value: Math.max(0, 10 - result.security.length),
    },
  ];

  const projectData = [
    {
      name: "Files",
      value: result.analysis.total_files,
    },
    {
      name: "Lines",
      value: result.analysis.total_lines ?? 0,
    },
    {
      name: "Technologies",
      value: result.analysis.total_technologies ?? 0,
    },
    {
      name: "Dependencies",
      value: result.analysis.total_dependencies ?? 0,
    },
  ];

  return (
    <div className="grid gap-6 lg:grid-cols-2">

      {/* Bug Chart */}
      <div className="rounded-2xl bg-white p-6 shadow">
        <h2 className="mb-4 text-xl font-bold">
          Bug Overview
        </h2>

        <ResponsiveContainer width="100%" height={250}>
          <PieChart>
            <Pie
              data={bugData}
              dataKey="value"
              outerRadius={80}
              label
            >
              {bugData.map((_, index) => (
                <Cell
                  key={index}
                  fill={COLORS[index]}
                />
              ))}
            </Pie>

            <Tooltip />
          </PieChart>
        </ResponsiveContainer>
      </div>

      {/* Security Chart */}
      <div className="rounded-2xl bg-white p-6 shadow">
        <h2 className="mb-4 text-xl font-bold">
          Security Overview
        </h2>

        <ResponsiveContainer width="100%" height={250}>
          <PieChart>
            <Pie
              data={securityData}
              dataKey="value"
              outerRadius={80}
              label
            >
              {securityData.map((_, index) => (
                <Cell
                  key={index}
                  fill={COLORS[index]}
                />
              ))}
            </Pie>

            <Tooltip />
          </PieChart>
        </ResponsiveContainer>
      </div>

      {/* Project Statistics */}
      <div className="rounded-2xl bg-white p-6 shadow lg:col-span-2">
        <h2 className="mb-4 text-xl font-bold">
          Project Statistics
        </h2>

        <ResponsiveContainer width="100%" height={320}>
          <BarChart data={projectData}>
            <CartesianGrid strokeDasharray="3 3" />

            <XAxis dataKey="name" />

            <YAxis />

            <Tooltip />

            <Bar
              dataKey="value"
              radius={[8, 8, 0, 0]}
            />
          </BarChart>
        </ResponsiveContainer>
      </div>

    </div>
  );
}