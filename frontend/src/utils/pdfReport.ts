import jsPDF from "jspdf";
import autoTable from "jspdf-autotable";
import type { AnalysisResponse } from "../types/analysis";

export function generatePDF(result: AnalysisResponse) {
  const doc = new jsPDF();

  // Title
  doc.setFontSize(20);
  doc.text("Lensify Software Analysis Report", 14, 20);

  doc.setFontSize(11);
  doc.text(`Generated: ${new Date().toLocaleString()}`, 14, 28);

  // Project Overview
  autoTable(doc, {
    startY: 38,
    head: [["Project Overview", "Value"]],
    body: [
      ["Project Name", result.analysis.project_name],
      ["Project Type", result.analysis.project_type],
      ["Language", result.analysis.language],
      ["Total Files", String(result.analysis.total_files)],
      ["Total Lines", String(result.analysis.total_lines)],
    ],
  });

  // Technology Stack
  autoTable(doc, {
    head: [["Technology", "Value"]],
    body: [
      ["Frontend", result.analysis.frontend ?? "-"],
      ["Backend", result.analysis.backend ?? "-"],
      ["Database", result.analysis.database ?? "-"],
      ["Authentication", result.analysis.authentication ?? "-"],
      ["Cloud", result.analysis.cloud ?? "-"],
      ["Deployment", result.analysis.deployment ?? "-"],
    ],
  });

  // Architecture
  autoTable(doc, {
    head: [["Architecture", "Value"]],
    body: [
      ["Architecture", result.architecture.architecture],
      ["Pattern", result.architecture.pattern],
      
    ],
  });

  // Performance
  autoTable(doc, {
    head: [["Performance", "Value"]],
    body: [
      ["Score", `${result.performance.score}/100`],
      ["Rating", result.performance.rating],
      ["Issues", String(result.performance.summary.total)],
    ],
  });

  // Documentation
  autoTable(doc, {
    head: [["Documentation", "Value"]],
    body: [
      ["Score", `${result.documentation.score}/100`],
      ["Coverage", `${result.documentation.coverage}%`],
      ["README", result.documentation.readme ? "Yes" : "No"],
      ["API Docs", result.documentation.api_docs ? "Yes" : "No"],
    ],
  });

  // Health
  autoTable(doc, {
    head: [["Health", "Value"]],
    body: [
      ["Score", `${result.health.score}/100`],
      ["Status", result.health.status],
    ],
  });

  // AI Review
  autoTable(doc, {
    head: [["AI Review", "Details"]],
    body: [
      ["Rating", result.ai_review.rating],
      ["Strengths", result.ai_review.strengths.join(", ")],
      ["Weaknesses", result.ai_review.weaknesses.join(", ")],
      [
        "Recommendations",
        result.ai_review.recommendations.join(", "),
      ],
    ],
  });

  doc.save(
    `${result.analysis.project_name || "Lensify"}-Report.pdf`
  );
}