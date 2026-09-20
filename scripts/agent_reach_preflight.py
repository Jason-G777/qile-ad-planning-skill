#!/usr/bin/env python3
"""Read-only Agent Reach runtime preflight for Codex."""

from __future__ import annotations

import json
import os
import platform
import shutil
import subprocess
import sys
from pathlib import Path


def executable_candidates() -> list[Path]:
    home = Path.home()
    names = ["agent-reach.exe", "agent-reach"] if os.name == "nt" else ["agent-reach"]
    folders = [
        home / ".local" / "bin",
        home / ".agent-reach-venv" / ("Scripts" if os.name == "nt" else "bin"),
        home / "pipx" / "venvs" / "agent-reach" / ("Scripts" if os.name == "nt" else "bin"),
        home / ".local" / "pipx" / "venvs" / "agent-reach" / ("Scripts" if os.name == "nt" else "bin"),
    ]
    if os.name != "nt":
        folders.extend([Path("/opt/homebrew/bin"), Path("/usr/local/bin")])
    return [folder / name for folder in folders for name in names]


def run_doctor(executable: str) -> dict[str, object]:
    try:
        completed = subprocess.run(
            [executable, "doctor", "--json"],
            capture_output=True,
            text=True,
            timeout=45,
            check=False,
        )
    except subprocess.TimeoutExpired:
        return {"ok": False, "reason": "timeout", "message": "doctor timed out after 45 seconds"}
    except OSError as exc:
        return {"ok": False, "reason": "os_error", "message": str(exc)}

    stdout = completed.stdout.strip()
    stderr = completed.stderr.strip()
    parsed: object | None = None
    if stdout:
        try:
            parsed = json.loads(stdout)
        except json.JSONDecodeError:
            parsed = None
    return {
        "ok": completed.returncode == 0,
        "returncode": completed.returncode,
        "result": parsed if parsed is not None else stdout[:4000],
        "stderr": stderr[:2000],
    }


def main() -> int:
    python_supported = sys.version_info >= (3, 10)
    visible = shutil.which("agent-reach")
    detected = next((str(path) for path in executable_candidates() if path.is_file()), None)

    report: dict[str, object] = {
        "platform": platform.platform(),
        "python": {
            "executable": sys.executable,
            "version": platform.python_version(),
            "supported": python_supported,
            "minimum": "3.10",
        },
        "commands": {
            name: shutil.which(name)
            for name in ("agent-reach", "pipx", "git", "gh", "node", "mcporter", "opencli", "bili", "yt-dlp")
        },
        "conda_required": False,
        "setup_reference": "references/agent-reach-runtime-setup.md",
    }

    executable = visible or detected
    if visible:
        doctor = run_doctor(visible)
        report["doctor"] = doctor
        report["status"] = "ready" if doctor.get("ok") else "doctor_failed"
    elif detected:
        report["status"] = "path_not_visible"
        report["detected_executable"] = detected
        report["doctor"] = run_doctor(detected)
    else:
        report["status"] = "runtime_missing"

    if not python_supported:
        report["status"] = "python_too_old"

    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if report["status"] == "ready" else 2


if __name__ == "__main__":
    raise SystemExit(main())
