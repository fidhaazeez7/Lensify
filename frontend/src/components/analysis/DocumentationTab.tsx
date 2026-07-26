import {
  BookOpen,
  FileText,
  MessageSquare,
  FileCode,
  CheckCircle,
  XCircle,
} from "lucide-react";

import type { Documentation } from "../../types/analysis";

type DocumentationTabProps = {
  documentation: Documentation;
};

export default function DocumentationTab({
  documentation,
}: DocumentationTabProps) {
  return (
    <div className="mx-auto mt-10 max-w-7xl px-8 space-y-6">

      {/* Score Card */}
      <div className="rounded-3xl border border-slate-200 bg-white p-8 shadow-sm">

        <div className="flex items-center gap-3">
          <BookOpen className="h-8 w-8 text-blue-600" />

          <div>
            <h2 className="text-3xl font-bold">
              Documentation Analysis
            </h2>

            <p className="text-slate-500">
              AI-generated documentation quality report
            </p>
          </div>
        </div>

        <div className="mt-8 flex items-center justify-between">

          <div>
            <p className="text-slate-500">
              Documentation Score
            </p>

            <h1 className="text-5xl font-bold text-blue-600">
              {documentation.score}%
            </h1>
          </div>

          <div className="rounded-xl bg-blue-100 px-6 py-3 text-xl font-semibold text-blue-700">
            {documentation.status}
          </div>

        </div>
      </div>

      {/* Statistics */}
      <div className="grid gap-6 md:grid-cols-2 lg:grid-cols-4">

        <StatCard
          icon={<FileText className="text-blue-600" />}
          title="README"
          value={documentation.readme ? "Available" : "Missing"}
        />

        <StatCard
          icon={<FileCode className="text-green-600" />}
          title="Docstrings"
          value={documentation.docstrings.toString()}
        />

        <StatCard
          icon={<MessageSquare className="text-purple-600" />}
          title="Comments"
          value={documentation.comments.toString()}
        />

        <StatCard
          icon={
            documentation.api_docs ? (
              <CheckCircle className="text-green-600" />
            ) : (
              <XCircle className="text-red-600" />
            )
          }
          title="API Docs"
          value={documentation.api_docs ? "Enabled" : "Not Found"}
        />

      </div>

      {/* Coverage */}
      <div className="rounded-3xl border border-slate-200 bg-white p-8 shadow-sm">

        <h3 className="text-xl font-bold">
          Documentation Coverage
        </h3>

        <div className="mt-6 h-4 w-full rounded-full bg-slate-200">

          <div
            className="h-4 rounded-full bg-blue-600"
            style={{
              width: documentation.coverage,
            }}
          />

        </div>

        <p className="mt-3 font-semibold text-blue-600">
          {documentation.coverage}
        </p>

      </div>

      {/* Suggestions */}
      <div className="rounded-3xl border border-slate-200 bg-white p-8 shadow-sm">

        <h3 className="text-xl font-bold mb-6">
          Improvement Suggestions
        </h3>

        {documentation.suggestions.length === 0 ? (
          <p className="text-green-600 font-semibold">
            Excellent! No documentation improvements are required.
          </p>
        ) : (
          <ul className="space-y-3">
            {documentation.suggestions.map(
              (suggestion, index) => (
                <li
                  key={index}
                  className="rounded-xl border border-slate-200 p-4"
                >
                  💡 {suggestion}
                </li>
              )
            )}
          </ul>
        )}

      </div>

    </div>
  );
}

type StatCardProps = {
  icon: React.ReactNode;
  title: string;
  value: string;
};

function StatCard({
  icon,
  title,
  value,
}: StatCardProps) {
  return (
    <div className="rounded-2xl border border-slate-200 bg-white p-6 shadow-sm">

      <div className="flex items-center gap-3">
        {icon}

        <span className="font-semibold">
          {title}
        </span>
      </div>

      <p className="mt-5 text-2xl font-bold">
        {value}
      </p>

    </div>
  );
}