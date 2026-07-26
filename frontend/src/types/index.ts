export interface PerformanceIssue {
  type: string;
  severity: string;
  file: string;
  line: number;
  description: string;
  recommendation: string;
}

export interface PerformanceSummary {
  total: number;
  high: number;
  medium: number;
  low: number;
}

export interface Performance {
  score: number;
  rating: string;
  issues: PerformanceIssue[];
  summary: PerformanceSummary;
}