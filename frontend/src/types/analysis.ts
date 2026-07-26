export interface SecurityIssue {
  title: string;
  severity: string;
  file: string;
  line: number;
  description: string;
  fix: string;
}

export interface Bug {
  title: string;
  severity: string;
  file: string;
  line: number;
  description: string;
  fix: string;
}

export interface Health {
  score: number;
  status: string;
}

export interface AIReview {
  rating: string;
  strengths: string[];
  weaknesses: string[];
  recommendations: string[];
}

// ----------------------------
// Performance Analysis
// ----------------------------

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

// ----------------------------
// Documentation Analysis
// ----------------------------

export interface Documentation {
  score: number;
  status: string;
  readme: boolean;
  docstrings: number;
  comments: number;
  api_docs: boolean;
  coverage: string;
  suggestions: string[];
}

// ----------------------------
// Framework Detection
// ----------------------------

export interface Frameworks {
  frontend: string | null;
  backend: string | null;
  database: string | null;
  communication: string | null;
  deployment: string | null;
}

// ----------------------------
// Architecture Detection
// ----------------------------

export interface ArchitectureData {
  architecture: string;
  pattern: string;
  frameworks: Frameworks;
}

// ----------------------------
// Technology Detection
// ----------------------------

export interface TechnologyDependencies {
  frontend: string[];
  backend: string[];
  database: string[];
  authentication: string[];
  deployment: string[];
  testing: string[];
  package_manager: string[];
}

export interface TechnologyData {
  project_type: string;
  dependencies: TechnologyDependencies;
  technologies: string[];
}

// ----------------------------
// Project Analysis
// ----------------------------

export interface AnalysisData {
  project_name: string;
  project_type: string;

  language: string;

  frontend: string;
  backend: string;
  database: string;
  authentication: string;

  orm: string;
  testing: string;
  cloud: string;

  deployment: string;

  package_manager: string;
  dependency_file: string | null;

  readme: boolean;

  total_files: number;
  total_lines?: number;

  files: string[];

  architecture?: string;
  total_dependencies?: number;
  total_technologies?: number;
}

// ----------------------------
// Complete API Response
// ----------------------------

export interface AnalysisResponse {
  message: string;

  analysis: AnalysisData;

  technology: TechnologyData;

  architecture: ArchitectureData;

  security: SecurityIssue[];

  bugs: Bug[];

  health: Health;

  ai_review: AIReview;

  performance: Performance;

  documentation: Documentation;
}