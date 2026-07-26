import type { Performance } from "../types/analysis";




interface Props {
  performance: Performance;
}

export default function PerformanceTab({ performance }: Props) {
  return (
    <div className="space-y-6">
      {/* Score Card */}
      <div className="rounded-xl border p-6">
        <h2 className="text-xl font-bold">⚡ Performance Score</h2>

        <div className="mt-4 text-5xl font-bold">
          {performance.score}%
        </div>

        <p className="mt-2 text-gray-500">
          Rating: {performance.rating}
        </p>
      </div>

      {/* Summary */}
      <div className="rounded-xl border p-6">
        <h2 className="text-lg font-semibold">
          Issue Summary
        </h2>

        <div className="grid grid-cols-4 gap-4 mt-4">
          <div>Total: {performance.summary.total}</div>
          <div>High: {performance.summary.high}</div>
          <div>Medium: {performance.summary.medium}</div>
          <div>Low: {performance.summary.low}</div>
        </div>
      </div>

      {/* Issues */}
      <div className="rounded-xl border p-6">
        <h2 className="text-lg font-semibold mb-4">
          Performance Issues
        </h2>

        {performance.issues.length === 0 ? (
          <p>No performance issues found.</p>
        ) : (
          <div className="space-y-4">
            {performance.issues.map((issue, index) => (
              <div
                key={index}
                className="border rounded-lg p-4"
              >
                <h3 className="font-semibold">
                  {issue.type}
                </h3>

                <p>
                  <strong>Severity:</strong>{" "}
                  {issue.severity}
                </p>

                <p>
                  <strong>File:</strong>{" "}
                  {issue.file}:{issue.line}
                </p>

                <p>{issue.description}</p>

                <p className="mt-2 text-green-600">
                  💡 {issue.recommendation}
                </p>
              </div>
            ))}
          </div>
        )}
      </div>
    </div>
  );
}