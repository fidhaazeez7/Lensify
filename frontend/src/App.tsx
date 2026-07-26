import { useState } from "react";

import LandingPage from "./pages/LandingPage";
import AnalysisPage from "./pages/AnalysisPage";

import type { AnalysisResponse } from "./types/analysis";

export default function App() {
  const [result, setResult] = useState<AnalysisResponse | null>(null);

  return (
    <>
      {result ? (
        <AnalysisPage result={result} />
      ) : (
        <LandingPage
          onAnalysisComplete={setResult}
        />
      )}
    </>
  );
}