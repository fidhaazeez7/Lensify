import {
  LayoutDashboard,
  Bug,
  Shield,
  Boxes,
  BookOpen,
  Bot,
  Gauge,
} from "lucide-react";

type AnalysisTabsProps = {
  activeTab: string;
  setActiveTab: (tab: string) => void;
};

const tabs = [
  {
    name: "Summary",
    icon: LayoutDashboard,
  },
  {
    name: "Architecture",
    icon: Boxes,
  },
  {
    name: "Performance",
    icon: Gauge,
  },
  {
    name: "Bugs",
    icon: Bug,
  },
  {
    name: "Security",
    icon: Shield,
  },
  {
    name: "Documentation",
    icon: BookOpen,
  },
  {
    name: "AI Assistant",
    icon: Bot,
  },
];

export default function AnalysisTabs({
  activeTab,
  setActiveTab,
}: AnalysisTabsProps) {
  return (
    <div className="border-b border-slate-200 bg-white shadow-sm">
      <div className="mx-auto flex max-w-7xl overflow-x-auto px-8">
        {tabs.map((tab) => {
          const Icon = tab.icon;

          return (
            <button
              key={tab.name}
              onClick={() => setActiveTab(tab.name)}
              className={`flex items-center gap-2 whitespace-nowrap border-b-2 px-5 py-5 text-sm font-semibold transition-all duration-200 ${
                activeTab === tab.name
                  ? "border-blue-600 text-blue-600"
                  : "border-transparent text-slate-500 hover:border-blue-300 hover:text-blue-600"
              }`}
            >
              <Icon className="h-5 w-5" />
              {tab.name}
            </button>
          );
        })}
      </div>
    </div>
  );
}