import { useState } from "react";
import { Bot, Send } from "lucide-react";

import api from "../../services/api";



import type {
  AnalysisData,
  Bug,
  SecurityIssue,
  Health,
  Performance,
  Documentation,
  ArchitectureData,
  TechnologyData,
} from "../../types/analysis";

type AIChatTabProps = {
  analysis: AnalysisData;
  bugs: Bug[];
  security: SecurityIssue[];
  health: Health;
  performance: Performance;
  documentation: Documentation;
  architecture: ArchitectureData;
  technology: TechnologyData;
};

type Message = {
  role: "user" | "assistant";
  content: string;
};

export default function AIChatTab({
  analysis,
  bugs,
  security,
  health,
  performance,
  documentation,
  architecture,
  technology,
}: AIChatTabProps) {

  const [question, setQuestion] = useState("");

  const [loading, setLoading] = useState(false);

  const [messages, setMessages] = useState<Message[]>([
    {
      role: "assistant",
      content:
        "Hello! 👋 I'm Lensify AI. Ask me anything about your uploaded project.",
    },
  ]);

  const askAI = async (text: string) => {
    if (!text.trim()) return;

    setMessages((prev) => [
      ...prev,
      {
        role: "user",
        content: text,
      },
    ]);

    setQuestion("");
    setLoading(true);

    try {
      const response = await api.post("/chat", {
  question: text,

  analysis,

  bugs,

  security,

  health,

  performance,

  documentation,

  architecture,

  technology,
});

      setMessages((prev) => [
        ...prev,
        {
          role: "assistant",
          content: response.data.answer,
        },
      ]);
    } catch (error) {
      console.error(error);

      setMessages((prev) => [
        ...prev,
        {
          role: "assistant",
          content: "❌ Unable to contact Lensify AI.",
        },
      ]);
    } finally {
      setLoading(false);
    }
  };

  const suggestions = [
  "Summarise my project",
  "Why is my health score low?",
  "Which bug should I fix first?",
  "Explain the security issues",
  "Explain the architecture",
  "How can I improve this project?",
];

  return (
    <div className="mx-auto mt-10 max-w-7xl px-8">
      <div className="rounded-3xl border border-slate-200 bg-white shadow-sm">

        {/* Header */}

        <div className="border-b border-slate-200 p-8">

          <div className="flex items-center gap-4">

            <div className="flex h-14 w-14 items-center justify-center rounded-full bg-blue-50">

              <Bot className="h-7 w-7 text-blue-600" />

            </div>

            <div>

              <h2 className="text-3xl font-bold">
                Lensify AI Assistant
              </h2>

              <p className="text-slate-500">
                Powered by Google Gemini
              </p>

            </div>

          </div>

        </div>

        <div className="p-8">

          {/* Suggested Questions */}

          <div className="mb-8 flex flex-wrap gap-3">

            {suggestions.map((item) => (

              <button
                key={item}
                onClick={() => askAI(item)}
                className="rounded-xl border border-slate-300 px-4 py-2 transition hover:bg-blue-50"
              >
                {item}
              </button>

            ))}

          </div>

          {/* Chat Messages */}

          <div className="space-y-5">

            {messages.map((msg, index) => (

              <div
                key={index}
                className={`flex ${
                  msg.role === "user"
                    ? "justify-end"
                    : "justify-start"
                }`}
              >

                <div
                  className={`max-w-3xl whitespace-pre-wrap rounded-2xl px-5 py-4 ${
                    msg.role === "user"
                      ? "bg-blue-600 text-white"
                      : "bg-slate-100 text-slate-800"
                  }`}
                >
                  {msg.content}
                </div>

              </div>

            ))}

            {loading && (

              <div className="flex justify-start">

                <div className="rounded-2xl bg-slate-100 px-5 py-4 text-slate-600">

                  🤖 Thinking...

                </div>

              </div>

            )}

          </div>

          {/* Input */}

          <div className="mt-10 flex gap-4">

            <input
              value={question}
              onChange={(e) => setQuestion(e.target.value)}
              onKeyDown={(e) => {
                if (e.key === "Enter") {
                  askAI(question);
                }
              }}
              placeholder="Ask Lensify anything..."
              className="flex-1 rounded-xl border border-slate-300 px-5 py-4 outline-none focus:border-blue-600"
            />

            <button
              onClick={() => askAI(question)}
              disabled={loading}
              className="rounded-xl bg-blue-600 px-6 text-white transition hover:bg-blue-700 disabled:bg-gray-400"
            >

              <Send className="h-5 w-5" />

            </button>

          </div>

        </div>

      </div>

    </div>
  );
}