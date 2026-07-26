import {
  Shield,
  Layers,
  Sparkles,
  Clock,
} from "lucide-react";

export default function SummaryCards() {
  const cards = [
    {
      icon: Layers,
      title: "Architecture",
      value: "85 / 100",
      color: "text-blue-600",
      bg: "bg-blue-50",
    },
    {
      icon: Shield,
      title: "Security",
      value: "7 Issues",
      color: "text-red-500",
      bg: "bg-red-50",
    },
    {
      icon: Sparkles,
      title: "Code Quality",
      value: "78 / 100",
      color: "text-green-600",
      bg: "bg-green-50",
    },
    {
      icon: Clock,
      title: "Analysis Time",
      value: "42 sec",
      color: "text-amber-600",
      bg: "bg-amber-50",
    },
  ];

  return (
    <section className="max-w-7xl mx-auto px-8 mt-8">

      <div className="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-4 gap-6">

        {cards.map((card, index) => {
          const Icon = card.icon;

          return (
            <div
              key={index}
              className="rounded-2xl bg-white shadow-sm border border-slate-200 p-6 hover:shadow-md transition"
            >
              <div
                className={`h-12 w-12 rounded-xl flex items-center justify-center ${card.bg}`}
              >
                <Icon className={`h-6 w-6 ${card.color}`} />
              </div>

              <p className="mt-5 text-slate-500">
                {card.title}
              </p>

              <h2 className="mt-2 text-3xl font-bold text-slate-900">
                {card.value}
              </h2>
            </div>
          );
        })}

      </div>

    </section>
  );
}