import { Upload, Lock } from "lucide-react";

export default function UploadCard() {
  return (
    <div className="w-full max-w-4xl rounded-3xl border border-slate-200 bg-white shadow-xl p-12">

      {/* Upload Icon */}
      <div className="flex justify-center">
        <div className="flex h-24 w-24 items-center justify-center rounded-full bg-blue-50">
          <Upload className="h-12 w-12 text-blue-600" />
        </div>
      </div>

      {/* Title */}
      <h1 className="mt-8 text-center text-5xl font-bold text-slate-900">
        Analyzing your project...
      </h1>

      {/* Subtitle */}
      <p className="mt-4 text-center text-lg text-slate-500">
        Please wait while we extract and analyze your code.
      </p>

      {/* File Card */}
      <div className="mt-10 flex items-center justify-between rounded-2xl border border-slate-200 bg-slate-50 px-6 py-4">

        <div className="flex items-center gap-3">

          <div className="flex h-10 w-10 items-center justify-center rounded-lg bg-blue-100 text-xl">
            📄
          </div>

          <div>
            <p className="font-semibold text-slate-900">
              ecommerce-platform.zip
            </p>

            <p className="text-sm text-slate-500">
              Ready for analysis
            </p>
          </div>

        </div>

        <p className="font-medium text-slate-500">
          245 MB
        </p>

      </div>

      {/* Progress Bar */}
      <div className="mt-8">

        <div className="mb-2 flex justify-between text-sm text-slate-500">
          <span>Analysis Progress</span>
          <span>45%</span>
        </div>

        <div className="h-3 w-full overflow-hidden rounded-full bg-slate-200">

          <div
            className="h-full rounded-full bg-blue-600 transition-all duration-700"
            style={{ width: "45%" }}
          />

        </div>

      </div>

      {/* Progress Steps */}
      <div className="mt-10 flex justify-between">

        {[
          "Uploading",
          "Extracting",
          "Analyzing",
          "Generating Insights",
        ].map((step, index) => (

          <div
            key={index}
            className="flex flex-1 flex-col items-center"
          >

            <div
              className={`flex h-10 w-10 items-center justify-center rounded-full font-semibold ${
                index === 0
                  ? "bg-blue-600 text-white"
                  : "bg-slate-200 text-slate-600"
              }`}
            >
              {index + 1}
            </div>

            <p className="mt-3 text-center text-sm text-slate-500">
              {step}
            </p>

          </div>

        ))}

      </div>

      {/* Security Note */}
      <div className="mt-12 flex items-center justify-center gap-2 text-slate-500">

        <Lock className="h-5 w-5 text-blue-600" />

        <p className="text-sm">
          Your files are encrypted and automatically deleted after analysis.
        </p>

      </div>

    </div>
  );
}