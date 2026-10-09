# NFRA_TOOLARCH -- surprise channel, round 1 (INVESTIGATION_v1)

**Channel owner:** `3.0.0_SA_CVO`. **Protocol:** `org/ref/SURPRISE_CHANNEL_PROTOCOL.md` (CLAUDE.md section 2). Items are schema-validated against `../schemas/investigation_item.schema.json`.

**Round opened** 2026-10-09 on the first surfaced item for this project. Executing seats surface; the CVO files.

```json
[
 {
  "id": "NFRA_TOOLARCH-S1",
  "project": "NFRA_TOOLARCH",
  "fabric": "laptop",
  "surfaced_by": "0.8.0_AE_CloudComp",
  "surfaced_at": "2026-10-09T21:10Z",
  "one_line": "provision-path-shims.sh rests on the premise that ~/bin is 'a persistent Windows USER-level PATH entry, inherited unconditionally by every child process on this machine' -- MEASURED FALSE on the PowerShell plane: C:\\Users\\AndrewBerman\\bin is absent from the persistent user PATH (28 entries, denominator printed), so ALL 105 .cmd twins are unreachable by bare name from PowerShell, which the script's own comments call 'the primary shell on this box'.",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "spec_asserts": "The script's WHY ~/bin header asserts ~/bin is 'ALREADY on PATH in every shell sampled (bash non-interactive, and PowerShell)' and is 'a persistent Windows USER-level PATH environment variable entry, inherited unconditionally by every child process on this machine regardless of shell flavor or interactivity' -- i.e. both forms it writes are reachable by bare name, which is why it writes the .cmd twin at all.",
  "world_is": "The bash plane resolves (command -v check-inbox -> /c/Users/AndrewBerman/bin/check-inbox) but for an unrelated reason: Git Bash prepends $HOME/bin itself. The PowerShell plane does NOT: [Environment]::GetEnvironmentVariable('PATH','User') holds 28 entries and NONE is C:\\Users\\AndrewBerman\\bin, and a freshly spawned `powershell.exe -NoProfile` child reads check-inbox as NOT FOUND. So the twin plane has been dead for the bare-name case since the 2026-07-28 widening, while every run of the script prints 'wrote 105 tool(s) x2 forms' and reports success for both.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "POSITIVE CONTROL, and it is what makes this a premise defect and not a defect in the new pair: comp-which -- provisioned since July and in daily use -- is ALSO 'NOT FOUND' in PowerShell. The failure is class-level, not specific to check-inbox",
    "DURABLE AUTHORITY READ, not a session's view: [Environment]::GetEnvironmentVariable('PATH','User') = 28 entries; the ten entries matching 'bin' are Codex, anaconda (x5), VS Code, .local, .bun and ffmpeg -- ~/bin is not among them",
    "FRESH-CHILD CONTROL: powershell.exe -NoProfile -Command 'Get-Command check-inbox' -> NOT FOUND, so this is not a stale-session artifact",
    "the .cmd FILE ITSELF IS CORRECT and was exercised by absolute path from PowerShell: --which -> C:/Users/AndrewBerman/Desktop/ajb_workspace\\org\\mcp\\check-inbox.sh rc=0, and a real run with an argument -> '[check-inbox] No pending messages' rc=0. The defect is PATH membership, never the batch file",
    "CRLF verified on the new twin (file(1): 'DOS batch file, ASCII text, with CRLF line terminators')",
    "WHY NO PROBE CATCHES IT: org/XXX.md step 1b-A.3's PATH check runs in BASH, where ~/bin resolves, so it reads '102 of 102 comp-tools resolve bare' and is structurally blind to the twin plane. That is the SAME anti-correlated-probe shape the script's own header warns about for comp-which"
   ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "disarm_owner": "0.0.0_AB_MSTR -- the device's persistent user PATH is fabric infrastructure and the integrator holds it; 1.0.0_SA_CTO rules whether the remedy is the PATH entry, a different reachable directory, or a correction to the script's premise comment. NOT this seat's act: it is a machine-level environment change outside the <paths> of ADHOC.provision-shims-check-inbox-forwarder, and CLAUDE.md's DO-NOT-MANUFACTURE-FRICTION clause means a seat does not widen its own order to take it.",
  "notes": "SURFACED FROM THE AC1 PROOF of ADHOC.provision-shims-check-inbox-forwarder; that order's own work is APPLIED AND PROVEN first, so the surfacing holds nothing. || BOUNDS WHAT THE ORDER'S AC1 PROVES, AND THAT IS WHY IT IS SURFACED RATHER THAN NOTED: AC1 (`command -v check-inbox` + `test -f ~/bin/check-inbox.cmd` + a live run) passes rc=0 and is sound on its own terms, but `test -f` proves the twin EXISTS and never that it RESOLVES. The CTO's ruling (msg 108114) asked that the name resolve; it resolves on the bash plane, which is the plane org/XXX.md step 1b-B's `check-inbox {serial}` is written for. || THE NEW PAIR IS EXACTLY AS REACHABLE AS EVERY OTHER SHIM -- this finding neither blocks nor weakens it, and no part of the order is left undone on account of it. || PROPORTION: 0.7.0_AE_CloudOps~TRL's original complaint (msg 108112) was from a SHELL, i.e. the bash plane, which this order fixes. The twin-plane gap is a second, older defect that the order's verification happened to expose."
 }
]
```
