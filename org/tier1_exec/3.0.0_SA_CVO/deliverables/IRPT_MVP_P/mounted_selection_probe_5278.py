"""Exact portal snapshot, isolated local Vite, supplied and independent mounted controls."""
from datetime import datetime, timezone
import hashlib
import io
import json
import os
from pathlib import Path
import socket
import subprocess
import tempfile
import time
import zipfile

PIN = "52786a7a4e16d0faec2f1f0b3e587d6e88c496cd"
BACKEND = "c5eace08c76176c6d9ebb78dd31ced3b0e57ea2d"


def main():
    here = Path(__file__).resolve()
    root = here.parents[5]
    portal = root / "portal"
    snapshot = Path(tempfile.mkdtemp(prefix="cvo-p-mounted-5278-", dir=Path(os.environ["LOCALAPPDATA"]) / "Temp"))
    hashes = {}
    for repo, pin, paths in ((portal, PIN, ["src", "package.json", "postcss.config.js"]),
                             (root, BACKEND, ["docs/contracts/investor-reporting/v1"])):
        data = subprocess.check_output(["git", "archive", "--format=zip", pin, *paths], cwd=repo)
        with zipfile.ZipFile(io.BytesIO(data)) as archive:
            for name in archive.namelist():
                target = (snapshot / name).resolve()
                assert target.is_relative_to(snapshot.resolve())
                if name.endswith("/"):
                    continue
                data = archive.read(name)
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_bytes(data)
                hashes[name] = hashlib.sha256(data).hexdigest()
    subprocess.run(["powershell", "-NoProfile", "-Command",
                    f"New-Item -ItemType Junction -Path '{snapshot / 'node_modules'}' -Target '{portal / 'node_modules'}' | Out-Null"], check=True)
    independent = here.with_name("mounted_selection_cases.mjs").read_bytes()
    (snapshot / "reviewer-mounted.mjs").write_bytes(independent)
    with socket.socket() as probe:
        probe.bind(("127.0.0.1", 0))
        port = probe.getsockname()[1]
    origin = f"http://127.0.0.1:{port}"
    # Local-only review host, without the development config's production proxy.
    server_code = f'''import {{ createServer }} from 'vite';
import react from '@vitejs/plugin-react';
import {{ resolve }} from 'node:path';
import {{ writeFileSync }} from 'node:fs';
const server = await createServer({{configFile:false, plugins:[react()],
  resolve:{{alias:{{'@':resolve('src')}}}}, cacheDir:resolve('.vite-review'),
  server:{{host:'127.0.0.1',port:{port},strictPort:true}}}});
await server.listen(); writeFileSync('review-ready','ready');
'''
    (snapshot / "review-server.mjs").write_text(server_code, encoding="utf-8")
    environment = {k: v for k, v in os.environ.items() if not k.startswith("IRPT_")}
    environment.update(IRPT_TEST_ORIGIN=origin, IRPT_CONTRACTS_DIR=str(snapshot / "docs/contracts/investor-reporting/v1"))
    evidence = {"seat": "3.0.0_SA_CVO~P", "portal_pin": PIN, "backend_contract_pin": BACKEND,
                "snapshot": str(snapshot), "origin": origin, "runs": [],
                "independent_sha256": hashlib.sha256(independent).hexdigest(),
                "host_sha256": hashlib.sha256(server_code.encode()).hexdigest(),
                "source_sha256": {name: sha for name, sha in hashes.items() if name in [
                    "src/pages/InvestorReporting/index.tsx", "src/pages/InvestorReporting/tabs/TabShell.tsx",
                    "src/pages/InvestorReporting/tabs/holdings/HoldingsTab.tsx",
                    "src/pages/InvestorReporting/tabs/analysis/AnalysisTab.tsx"] or "/__tests__/m-selection/" in name}}

    def run(label, command):
        result = subprocess.run(command, cwd=snapshot, env=environment, capture_output=True,
                                text=True, encoding="utf-8", errors="replace", timeout=60)
        evidence["runs"].append({"label": label, "command": command, "exit_code": result.returncode,
                                 "stdout": result.stdout, "stderr": result.stderr})

    run("focused-supplied", ["bun", "test", "src/pages/InvestorReporting/__tests__/m-selection/selectionRequest.test.ts",
        "src/pages/InvestorReporting/__tests__/mvp-selection/selection.test.ts",
        "src/pages/InvestorReporting/__tests__/mvp-selection/coverage.test.ts"])
    with (snapshot / "review-server.log").open("w", encoding="utf-8") as server_log:
        server = subprocess.Popen(["node", "review-server.mjs"], cwd=snapshot, env=environment,
                                  stdout=server_log, stderr=subprocess.STDOUT, creationflags=subprocess.CREATE_NO_WINDOW)
        try:
            started = time.monotonic()
            while not (snapshot / "review-ready").exists():
                if server.poll() is not None or time.monotonic() - started > 30:
                    raise RuntimeError("isolated review Vite failed to become ready")
                time.sleep(0.1)
            for script in ("header-race.mjs", "holdings-race.mjs"):
                run("supplied-mounted:" + script, ["node", "src/pages/InvestorReporting/__tests__/m-selection/" + script])
            run("independent-mounted", ["node", "reviewer-mounted.mjs"])
        finally:
            server.terminate()
            server.wait(timeout=10)
    evidence["timestamp_utc"] = datetime.now(timezone.utc).isoformat()
    evidence["server_log"] = (snapshot / "review-server.log").read_text(encoding="utf-8")
    evidence["limits"] = "Actual pinned React components in headless Edge; controlled API harness, no LiveClient/authenticated fetch/backend/provider integration. Local Vite config with no proxy, existing dependencies. No live or full P/S acceptance."
    here.with_suffix(".json").write_text(json.dumps(evidence, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(evidence, indent=2))
    return int(any(row["exit_code"] for row in evidence["runs"]))


if __name__ == "__main__":
    raise SystemExit(main())
