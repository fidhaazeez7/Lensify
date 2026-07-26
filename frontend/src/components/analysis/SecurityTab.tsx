import {
  Shield,
  CheckCircle2,
  FileText,
  MapPin,
  Wrench,
} from "lucide-react";
import type { SecurityIssue } from "../../types/analysis";

type SecurityTabProps = {
  security: SecurityIssue[];
};

const getSeverityStyle = (severity: string) => {
  switch (severity.toLowerCase()) {
    case "high":
      return "bg-red-100 text-red-700 border-red-200";

    case "medium":
      return "bg-yellow-100 text-yellow-700 border-yellow-200";

    default:
      return "bg-blue-100 text-blue-700 border-blue-200";
  }
};

export default function SecurityTab({ security }: SecurityTabProps) {
  return (
    <div className="mx-auto mt-10 max-w-7xl px-8">
      <div className="rounded-3xl border border-slate-200 bg-white p-8 shadow-sm">
        {/* Header */}
        <div className="flex items-center gap-3">
          <Shield className="h-8 w-8 text-blue-600" />

          <div>
            <h2 className="text-3xl font-bold text-slate-900">
              Security Analysis
            </h2>

            <p className="text-slate-500">
              Security vulnerabilities detected by Lensify
            </p>
          </div>
        </div>

        {/* Empty State */}
        {security.length === 0 ? (
          <div className="mt-10 flex items-center gap-3 rounded-2xl bg-green-50 p-6">
            <CheckCircle2 className="h-7 w-7 text-green-600" />

            <div>
              <h3 className="font-bold text-green-700">
                No Security Issues Found
              </h3>

              <p className="text-green-600">
                Your project passed all current security checks.
              </p>
            </div>
          </div>
        ) : (
          <div className="mt-8 space-y-6">
            {security.map((issue, index) => (
              <div
                key={index}
                className="rounded-2xl border border-slate-200 bg-white p-6 shadow-sm transition-all duration-200 hover:shadow-md"
              >
                {/* Top Section */}
                <div className="flex items-start justify-between">
                  <div>
                    <h3 className="text-xl font-semibold text-slate-900">
                      {issue.title}
                    </h3>

                    <div className="mt-3 flex flex-wrap gap-6 text-sm text-slate-600">
                      <div className="flex items-center gap-2">
                        <FileText className="h-4 w-4" />
                        {issue.file}
                      </div>

                      <div className="flex items-center gap-2">
                        <MapPin className="h-4 w-4" />
                        Line {issue.line}
                      </div>
                    </div>
                  </div>

                  <span
                    className={`rounded-full border px-3 py-1 text-sm font-semibold ${getSeverityStyle(
                      issue.severity
                    )}`}
                  >
                    {issue.severity}
                  </span>
                </div>

                {/* Description */}
                <div className="mt-6 rounded-xl bg-slate-50 p-4">
                  <h4 className="font-semibold text-slate-800">
                    Description
                  </h4>

                  <p className="mt-2 text-slate-600">
                    {issue.description}
                  </p>
                </div>

                {/* Recommended Fix */}
                <div className="mt-4 rounded-xl bg-green-50 p-4">
                  <div className="flex items-center gap-2">
                    <Wrench className="h-5 w-5 text-green-700" />

                    <h4 className="font-semibold text-green-700">
                      Recommended Fix
                    </h4>
                  </div>

                  <p className="mt-2 text-green-700">
                    {issue.fix}
                  </p>
                </div>
              </div>
            ))}
          </div>
        )}
      </div>
    </div>
  );
}