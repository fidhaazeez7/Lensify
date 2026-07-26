import Hero from "../components/landing/Hero";
import UploadZone from "../components/landing/UploadZone";
import FeatureBar from "../components/landing/FeatureBar";

import type { AnalysisResponse } from "../types/analysis";

type LandingPageProps = {
  onAnalysisComplete: (data: AnalysisResponse) => void;
};

export default function LandingPage({
  onAnalysisComplete,
}: LandingPageProps) {
  return (
    <main className="min-h-screen bg-white">
      <Hero />

      <UploadZone
        onAnalysisComplete={onAnalysisComplete}
      />

      <FeatureBar />
    </main>
  );
}