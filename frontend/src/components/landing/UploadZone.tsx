import { useRef, useState } from "react";
import { Upload, FolderOpen, FileArchive } from "lucide-react";

import api from "../../services/api";
import type { AnalysisResponse } from "../../types/analysis";

type UploadZoneProps = {
  onAnalysisComplete: (data: AnalysisResponse) => void;
};

export default function UploadZone({
  onAnalysisComplete,
}: UploadZoneProps) {
  const zipInputRef = useRef<HTMLInputElement>(null);
  const folderInputRef = useRef<HTMLInputElement>(null);

  const [uploadMode, setUploadMode] = useState<"zip" | "folder">("zip");

  const [selectedZip, setSelectedZip] = useState<File | null>(null);
  const [selectedFolder, setSelectedFolder] = useState<File[]>([]);

  const [uploading, setUploading] = useState(false);

  const chooseZip = () => {
    zipInputRef.current?.click();
  };

  const chooseFolder = () => {
    folderInputRef.current?.click();
  };

  const handleZipChange = (
    event: React.ChangeEvent<HTMLInputElement>
  ) => {
    const file = event.target.files?.[0];

    if (!file) return;

    if (!file.name.toLowerCase().endsWith(".zip")) {
      alert("Please choose a ZIP file.");
      return;
    }

    setUploadMode("zip");
    setSelectedZip(file);
    setSelectedFolder([]);
  };

  const handleFolderChange = (
    event: React.ChangeEvent<HTMLInputElement>
  ) => {
    const files = Array.from(event.target.files ?? []);

    if (files.length === 0) return;

    setUploadMode("folder");
    setSelectedFolder(files);
    setSelectedZip(null);
  };

  const handleUpload = async () => {
    try {
      setUploading(true);

      const formData = new FormData();

      let response;

      if (uploadMode === "zip") {
        if (!selectedZip) {
          alert("Please choose a ZIP file.");
          setUploading(false);
          return;
        }

        formData.append("file", selectedZip);

        response = await api.post<AnalysisResponse>(
          "/analyze",
          formData,
          {
            headers: {
              "Content-Type": "multipart/form-data",
            },
          }
        );
      } else {
        if (selectedFolder.length === 0) {
          alert("Please choose a project folder.");
          setUploading(false);
          return;
        }

        selectedFolder.forEach((file) => {
          formData.append("files", file, file.webkitRelativePath || file.name);
        });

        response = await api.post<AnalysisResponse>(
          "/analyze-folder",
          formData,
          {
            headers: {
              "Content-Type": "multipart/form-data",
            },
          }
        );
      }

      console.log("API Response:", response.data);

onAnalysisComplete(response.data);

    } catch (error: any) {
      console.error("Upload Error:", error);

      if (error.response) {
        console.log("Status:", error.response.status);
        console.log("Data:", error.response.data);
        alert(JSON.stringify(error.response.data));
      } else {
        alert(error.message);
      }

    } finally {
      setUploading(false);
    }
  };
  return (
  <div className="mt-12 flex justify-center">
    <div className="w-full max-w-3xl rounded-3xl border-2 border-dashed border-blue-300 bg-white p-12 text-center shadow-sm hover:border-blue-500 transition">

      <Upload className="mx-auto h-12 w-12 text-blue-600" />

      <h2 className="mt-6 text-3xl font-bold text-slate-900">
        Upload your project
      </h2>

      <p className="mt-4 text-slate-500">
        Upload a ZIP file or an entire project folder for AI analysis.
      </p>

      {/* Hidden ZIP Input */}
      <input
        ref={zipInputRef}
        type="file"
        accept=".zip"
        className="hidden"
        onChange={handleZipChange}
      />

      {/* Hidden Folder Input */}
      <input
  ref={folderInputRef}
  type="file"
  multiple
  className="hidden"
  onChange={handleFolderChange}
  {...({ webkitdirectory: "", directory: "" } as any)}
/>

      {/* Upload Buttons */}
      <div className="mt-8 flex justify-center gap-4">

        <button
          onClick={chooseZip}
          disabled={uploading}
          className="flex items-center gap-2 rounded-xl bg-blue-600 px-6 py-3 text-white hover:bg-blue-700 disabled:bg-gray-400"
        >
          <FileArchive size={20} />
          Upload ZIP
        </button>

        <button
          onClick={chooseFolder}
          disabled={uploading}
          className="flex items-center gap-2 rounded-xl bg-indigo-600 px-6 py-3 text-white hover:bg-indigo-700 disabled:bg-gray-400"
        >
          <FolderOpen size={20} />
          Upload Folder
        </button>

      </div>

      {/* Selected ZIP */}
      {uploadMode === "zip" && selectedZip && (
        <div className="mt-6 rounded-xl border border-green-200 bg-green-50 p-4">
          <p className="font-semibold text-green-700">
            📦 {selectedZip.name}
          </p>
          <p className="mt-1 text-sm text-green-600">
            {(selectedZip.size / 1024 / 1024).toFixed(2)} MB
          </p>
        </div>
      )}

      {/* Selected Folder */}
      {uploadMode === "folder" && selectedFolder.length > 0 && (
        <div className="mt-6 rounded-xl border border-green-200 bg-green-50 p-4">
          <p className="font-semibold text-green-700">
            📁 Project Folder Selected
          </p>

          <p className="mt-1 text-sm text-green-600">
            {selectedFolder.length} files selected
          </p>

          <p className="mt-2 text-xs text-gray-600 break-all">
            {selectedFolder[0].webkitRelativePath.split("/")[0]}
          </p>
        </div>
      )}

      {/* Analyze Button */}
      <button
        onClick={handleUpload}
        disabled={
          uploading ||
          (uploadMode === "zip" && !selectedZip) ||
          (uploadMode === "folder" && selectedFolder.length === 0)
        }
        className="mt-8 rounded-xl bg-green-600 px-8 py-3 text-white hover:bg-green-700 disabled:bg-gray-400"
      >
        {uploading ? "Analyzing..." : "Analyze Project"}
      </button>

    </div>
  </div>
);
}