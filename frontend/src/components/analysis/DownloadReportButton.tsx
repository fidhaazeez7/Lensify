import api from "../../services/api";

import type { AnalysisResponse } from "../../types/analysis";

type DownloadReportButtonProps = {
  result: AnalysisResponse;
};

export default function DownloadReportButton({
  result,
}: DownloadReportButtonProps) {
  const downloadReport = async () => {
    try {
      const response = await api.post(
        "/download-report",
        result,
        {
          responseType: "blob",
        }
      );

      const blob = new Blob([response.data], {
        type: "application/pdf",
      });

      const url = window.URL.createObjectURL(blob);

      const link = document.createElement("a");

      link.href = url;

      link.download =
        `${result.analysis.project_name}_report.pdf`;

      document.body.appendChild(link);

      link.click();

      link.remove();

      window.URL.revokeObjectURL(url);

    } catch (error) {
      console.error(error);

      alert("Unable to generate report.");
    }
  };

  return (
    <button
      onClick={downloadReport}
      className="rounded-xl bg-green-600 px-6 py-3 font-semibold text-white transition hover:bg-green-700"
    >
      📄 Download Report
    </button>
  );
}