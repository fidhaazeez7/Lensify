import {
  TrendingUp,
  Shield,
  Zap,
  Code2,
} from "lucide-react";

export default function FeatureSection() {
  const features = [
    {
      icon: TrendingUp,
      title: "AI-Powered Insights",
      description: "Deep analysis with AI",
    },
    {
      icon: Shield,
      title: "Secure & Private",
      description: "Your code is safe",
    },
    {
      icon: Zap,
      title: "Instant Analysis",
      description: "Results in seconds",
    },
    {
      icon: Code2,
      title: "Developer Focused",
      description: "Built for developers",
    },
  ];

  return (
    <section className="mt-16 mb-12">
      <div className="max-w-6xl mx-auto flex flex-wrap justify-center gap-10">

        {features.map((feature, index) => {
          const Icon = feature.icon;

          return (
            <div
              key={index}
              className="flex items-start gap-3"
            >
              <Icon className="h-6 w-6 text-blue-600 mt-1" />

              <div>
                <h3 className="font-semibold text-slate-900">
                  {feature.title}
                </h3>

                <p className="text-sm text-slate-500">
                  {feature.description}
                </p>
              </div>
            </div>
          );
        })}

      </div>
    </section>
  );
}