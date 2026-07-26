import { useState } from "react";

import type { AnalysisResponse } from "../types/analysis";

import AnalysisHeader from "../components/analysis/AnalysisHeader";
import DashboardStats from "../components/analysis/DashboardStats";
import AnalysisTabs from "../components/analysis/AnalysisTabs";
import DownloadReportButton from "../components/analysis/DownloadReportButton";

import SummaryTab from "../components/analysis/SummaryTab";
import BugsTab from "../components/analysis/BugsTab";
import SecurityTab from "../components/analysis/SecurityTab";
import ArchitectureTab from "../components/analysis/ArchitectureTab";
import DocumentationTab from "../components/analysis/DocumentationTab";
import AIChatTab from "../components/analysis/AIChatTab";
import PerformanceTab from "../components/PerformanceTab";

type AnalysisPageProps = {
  result: AnalysisResponse;
};

export default function AnalysisPage({
  result,
}: AnalysisPageProps) {
  console.log("Analysis Result:", result);

  const [activeTab, setActiveTab] = useState("Summary");

  return (
    <main className="min-h-screen bg-slate-100">
      {/* Header */}
      <AnalysisHeader />

      {/* Dashboard Statistics */}
      <DashboardStats result={result} />

      {/* Download Report */}
      <div className="mx-auto mt-6 flex max-w-7xl justify-end px-8">
        <DownloadReportButton result={result} />
      </div>

      {/* Navigation Tabs */}
      <AnalysisTabs
        activeTab={activeTab}
        setActiveTab={setActiveTab}
      />

      {/* Summary */}
      {activeTab === "Summary" && (
        <SummaryTab
          analysis={result.analysis}
          technology={result.technology}
          architecture={result.architecture}
          health={result.health}
          aiReview={result.ai_review}
          bugs={result.bugs}
          security={result.security}
        />
      )}

      {/* Architecture */}
      {activeTab === "Architecture" && (
        <ArchitectureTab
          analysis={result.analysis}
          technology={result.technology}
          architecture={result.architecture}
        />
      )}

      {/* Performance */}
      {activeTab === "Performance" && (
        <PerformanceTab
          performance={result.performance}
        />
      )}

      {/* Bugs */}
      {activeTab === "Bugs" && (
        <BugsTab
          bugs={result.bugs}
        />
      )}

      {/* Security */}
      {activeTab === "Security" && (
        <SecurityTab
          security={result.security}
        />
      )}

      {/* Documentation */}
      {activeTab === "Documentation" && (
       <DocumentationTab
  documentation={result.documentation}
/> 
      )}

      {/* AI Assistant */}
     {activeTab === "AI Assistant" && (
  <AIChatTab
    analysis={result.analysis}
    bugs={result.bugs}
    security={result.security}
    health={result.health}
    performance={result.performance}
    documentation={result.documentation}
    architecture={result.architecture}
    technology={result.technology}
  />
)} 
    </main>
  );
}