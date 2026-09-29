# Site Z crash investigation — 29 September 2026

**RCN-0019 · `4.0.0_SA_CRO~Z` · Opal Bloomberg device · all incident times Eastern.**
Commission and limits: [Andrew-direct record](../ANDREW_DIRECT_20260929_SITE_Z_CRASH_INVESTIGATION.md).
Research and recommendations only. No remediation dispatched or destructive operation executed by CRO.

## Finding

**The device suffered both disk exhaustion and a kernel driver stall.** Writes were
failing by **10:30:59 AM**, while four development worktrees were being created.
Around **10:47:23 AM**, threads stopped progressing at a lock inside
`SentinelMonitor.sys` (SentinelOne 26.1.2.177). A Bloomberg thread retained a Windows
GUI lock while waiting there, spreading the stall to Terminal and other desktop
applications. **1,070 of 6,850 examined thread stacks** were blocked in this driver.
The stack and disassembly strongly support a **reentrant lock deadlock**; vendor
confirmation of its internal logic remains necessary.

Andrew forced the crash at **11:34:55 AM**, about **47½ minutes after the earliest
observed driver waits**. The E2 bugcheck records that manual capture, not the cause
of the preceding hang. Disk exhaustion is proven and preceded the deadlock, but
the evidence does **not** establish that disk exhaustion triggered it. Cleaning
the disk alone therefore does not close this incident.

A third failure resurfaced after reboot: bare `python` selected a Python 3.14
installation whose standard library had already been removed on September 26.
That configuration problem predates today's crash. It had even been repaired on
September 28 before recurring.

## 1. Timeline and evidence

| Time, ET | Observed event | Evidence and interpretation |
|---|---|---|
| Sep 26, 13:02 | Python 3.14 component removal, including standard library, followed by installation of Add to Path | MsiInstaller component events. SYSTEM identifies the execution account, not the human or program that initiated it. The MSI event stream alone does not prove a particular installer UI mode. |
| Sep 28, 14:42–14:43 | Clean Start-menu restart and boot | System 1074, followed by boot records. |
| Sep 28, 15:20 | Broad MSI product reconfiguration sweep, including Python Add to Path | 104 reconfiguration events across about 52 products. A possible PATH writer; an event alone does not show the actual environment write. |
| Sep 28, 15:42 | Elevated removal of four Python314 Machine PATH entries; fresh Python 3.11.9 and `mcp` verified | Retained MSTR transcript and commit `be2d74b00739ab0b94b5a97f5f7b4ab68adf7044`. Subsequent launches explicitly used a sanitized environment. This explains why the fabric could run after yesterday's restart. The 15:20 sweep preceded this successful repair. |
| Sep 29, 03:25:53 | VSS snapshot creation hit its configured storage limit | Volsnap 36. This is not proof that C: was already full. |
| 08:06:00–08:06:06 | Process performance collection failed; VSS could not allocate paged heap | PerfOS 2012, PerfProc 8192, Volsnap 6/15. Memory/resource pressure predates the first recovered disk-full write failure. |
| 08:28:53–08:32:01 | SentinelAgent.exe crashed and wrote a separate dump; service termination logged | Local dump exception `0x01042021`, SentinelAgentCore.dll 26.1.2.177; System record 565387, event 7031. Dump occupies 6.40 GiB logical / 4.68 GiB allocated. Preserve it with the kernel dump. |
| **10:30:59** | Four CRPS14 worktree checkouts encountered `No space left on device` | Actual COO tool result, retained transcript line 5148. Wrapper still reported exit 0. `wk-crps14-5` has 145 missing and 35 zero-length tracked files. |
| 10:43–10:45 | COO diagnosed near-zero free space; subsequent shell writes failed; warning message landed empty | Transcript records `sed`, `cat` and `head` write failures. The 10:45:01 MSTR inbox file is exactly zero bytes. Its missing body is not recoverable from the broker snapshot. |
| 10:46:51 | Dell instrumentation could not write logs because there was insufficient disk space | Application .NET Runtime events; first retained record 431020. |
| 10:46:56 | Last pre-hang Desktop tripwire sample / CyberCNS log activity | Existing freeze evidence folder. Tripwire watched scan duration and log silence, not disk capacity. |
| 10:47:22.325 | Last recovered pre-crash Claude transcript record | Latest timestamp in the 158 recent transcript files examined. This is a logging bound, not proof of the last running process. |
| **~10:47:23.285** | Earliest observed SentinelMonitor lock waits begin | Crash clock minus 47m32.078s of kernel wait time. SentinelAgent file callback and a bash process-exit callback wait on the same push lock. |
| ~10:47:23.770 onward | Bloomberg `wintrv.exe` waits in a SentinelMonitor registry callback while retaining shared GUI resource | Terminal rendering threads have waits from about 10:50:25; Bloomberg `bplus64.exe` and the raw-input thread also wait for the GUI resource. See [debugger findings](DEBUGGER_FINDINGS.md). |
| 11:34:38 / **11:34:55.363** | Event 6008's prior-shutdown label / dump's actual debug-session clock | Distinct timestamps. Andrew confirms he intentionally triggered the crash because the device was hung. Bugcheck E2 agrees. |
| **11:39:54.500** | Reboot | Kernel-General event 12, record 565461. |
| 11:39:56–11:40:36 | Dump captured, but next-capture initialization also reported errors | MEMORY.DMP and minidump exist and load. Volmgr 162 reports successful generation; events 46/164 report initialization/dedicated-dump configuration failures. Do not treat the present dump as proof that the next capture is ready. |
| 11:40:10–11:40:29 | FontCache/CAMSvc terminated; tripwire resumed | Both services subsequently measured running. The reboot did not itself repair Python. |
| ~11:52–11:55 | MSTR removed two Python314 Machine PATH entries | Today's backup and fresh-shell Python verification. CRO did not repeat this change. |
| 12:16:21 and 12:16:36 | Python Add to Path reconfigured again during another broad MSI sweep | Application records 431248 and 431300. MSTR reports a concurrent PATH relapse; this supports MSI repair as the recurring writer, with the initiating process still to be established. |
| 12:24:50 | Python Add to Path product removal completed | MsiInstaller 11724/1034, records 431337/431338. MSTR reports performing this additional intervention and re-stripping PATH. This was not performed by CRO under its investigation authorization. |

## 2. Why it happened — separate causal findings

**2.1 Capacity failure: established.** Development checkouts continued until NTFS
could no longer satisfy writes. The post-reboot census found **235.76 GiB of
registered worktree contents**, about **49.8% of the entire C: volume's capacity**.
The four-worktree operation is the earliest recovered operation that visibly ran
out of space; it is not proof that those four checkouts alone filled the disk.
Accumulated worktrees dominate the measured developer footprint. The morning
Sentinel dump also consumed space before the failure. Exact pre-failure free-space
history and allocation by every writer were not recorded.

**2.2 Hang mechanism: strongly supported driver deadlock.** The same SentinelMonitor
push lock blocked registry, file, process and thread callbacks. The SentinelAgent
thread's stack re-enters its own file filter from a driver-initiated file query;
disassembly shows an outer shared acquisition before that nested call. A process
exit callback waits for exclusive access. This supports a recursive shared-lock
deadlock with a writer pending. Bloomberg's blocked thread held the GUI resource,
making a security-driver stall appear as a frozen desktop. The driver's private
symbols/source and a controlled reproduction are not available; the triggering
condition and relationship to disk/memory pressure remain open.

**2.3 Resource pressure: established earlier, not terminal RAM exhaustion.** At
08:06 Windows reported memory allocation failures. The kernel dump records 171
failed commit requests during the boot, but at capture it still had about
31.45 GiB physical memory available and 53.36 GiB committed against a 69.93 GiB
limit. A prior peak can disappear by capture time. Large pool consumers included
security token objects and ETW buffers. A single snapshot cannot assign a leak
to a vendor. The earlier Sentinel service crash is relevant evidence, not proof
that its private exception means out-of-memory.

**2.4 Python startup failure: pre-existing configuration damage plus recurrence.**
The missing standard library is explained by the September 26 installer events,
not by today's disk-full interval. September 28's successful repair means the
broken PATH must subsequently have returned. Today's 12:16 reconfiguration and
reported relapse make MSI self-repair a strong lead. Exact initiating process
and the intervening pre-reboot PATH rewrite are not yet reconstructed. Existing
processes can also retain their earlier environment; only fresh terminal windows
exercise the corrected Machine PATH.

## 3. Storage denominator and reclamation

**Volume capacity: 508,636,950,528 bytes = 473.705 GiB.** Free at 12:02:47:
11,163,373,568 bytes = 10.397 GiB. Free at approximately 12:25:
6,800,195,584 bytes = 6.333 GiB. The investigation directory, including downloaded
symbols, measured about 207 MB at 12:27; it does not explain that decline.
At **12:38:09**, free space measured **18,106,683,392 bytes (16.86 GiB)**. Other
activity is changing allocation during this investigation; CRO did not reclaim
space and does not attribute that recovery without an execution receipt.

Census: 12:04:04–12:17:53, 7,113,597 files / 961,186 directories. Logical sizes,
703 access failures, 1,368 skipped reparse points, no hardlink deduplication.
These are **footprint measurements, not guaranteed reclaimable allocation**.

| Pool | GiB logical | Scope / overlap | Recommended treatment |
|---|---:|---|---|
| Registered worktree contents | **235.76** | 180 measured roots from 185 registrations across workspace/portal; includes main checkouts and nested ownership assigned to deepest registered root | MSTR/COO owner review; checkout-only reclamation candidates, branches and unique work preserved |
| All `C:\tmp` | **179.42** | Includes 177.40 GiB assigned to 151 registered worktree roots; overlaps preceding row | Largest immediate developer-residue pool |
| Desktop freeze evidence folder | **25.24** | Historical captures; inside Users | KEEP until preservation/retention decision |
| `C:\dedicateddump.sys` | **32.00** | Preallocated capture backing, separate from MEMORY.DMP | KEEP; deliberate crash-capture configuration, not scratch |
| `C:\Windows\MEMORY.DMP` | **17.40** | Today's kernel evidence, inside Windows | KEEP; preserve off C before any retention decision |
| Sentinel service dump | **6.40** | 4.68 GiB allocated, inside ProgramData | KEEP; directly relevant to 08:28 crash |
| Pagefile | **4.00 now / 6.47 at crash** | Root file; runtime virtual-memory backing | KEEP; do not reclaim by reducing virtual-memory headroom |
| Terraform-related paths | **13.71** | Overlapping census category, including installed providers, not all abandoned temp | Separate live provider caches from failed-download residue before approval |
| Cache-named paths | **5.58** | Overlapping path-name category; not exhaustive | Candidate review, not blanket deletion |
| `node_modules` | **9.29** | Mostly within checkouts above | Count only once in a checkout reclamation proposal |

Disjoint top-level footprint includes C:\tmp 179.42, Users 114.10, Windows 55.22,
dedicateddump 32, Anaconda 13.79, ProgramData 13.52, Program Files 10.15,
blp 6.91, Program Files (x86) 6.29, Drivers 4.40 and pagefile 4 GiB.
Windows/hardlink duplication and unreadable files prevent reconciling this logical
inventory directly to volume allocation.

The original census stores depth-2/3/5 groups in one map: shallow **file** keys
repeat (root files three times, MEMORY.DMP twice). Report figures correct that
aggregation; exact large-file records and directory totals are used. Never sum
that raw map. MSTR was notified before preparing the joint table.

**Joint recommendation:** use reviewed development checkouts for substantial
reclamation before sacrificing crash evidence. MSTR's proposed batch is roughly
165–168 GiB of checkouts plus about 2.5 GiB scratch; its exact count and timestamp
reconciliation is tracked in [reclamation review](RECLAMATION.md). This is a
proposal, not a deletion authorization. Retaining branches alone does not preserve
untracked or ignored source, dirty submodule files, or an unpinned detached HEAD.

The 32 GiB dedicated allocation was documented in the Desktop investigation's
July 30 elevated capture setup, with a session-temporary enable script. The
record does not identify a human operator. Its purpose was to permit kernel
capture despite a small pagefile. Current CrashDumpEnabled is 2; the old SUMMARY
incorrectly labels value 3 as kernel, so its prose is not the configuration oracle.
Today's kernel dump loaded successfully. Shrinking/removing capture backing needs
a deliberate replacement design and verification by the endpoint administrator.

## 4. Collateral damage and present condition

| Surface | Finding | Owner / remaining action |
|---|---|---|
| `C:\tmp\wk-crps14-5` | **145 tracked files absent; 35 tracked files zeroed** against non-empty HEAD versions | COO~X + worktree owner: hold this candidate; recover deliberately from known commits after preserving local edits |
| 10:45 disk warning | Zero-byte file, missing broker body | MSTR/COO~X: retain failed artifact; recover intended content from sender record if needed |
| Main workspace tracked files | 47,051 paths examined; all 356 zero-length files were also empty at HEAD | No new zeroed tracked files found in this main checkout; not a byte-for-byte validation of all files or all worktrees |
| Git objects/index | Workspace and portal `git fsck --full` exit 0; index readable | Dangling objects are not corruption; do not prune them during recovery |
| Nine open-deploy JSONs | Valid JSON; semantic timestamp-field changes, not just CRLF churn; mtimes 01:42 | Deploy-state owner: ordinary semantic review, no evidence of crash truncation |
| Graph risk edges / Bloomberg field map | Valid JSON; edge count 1,662→1,524, field map 98→99 securities; mtimes 01:42 | Respective owners: review meaning, not automatic rollback |
| Broker | SQLite read-only integrity check `ok`; port 7800 and message delivery functioning after restart | MCP owner: harden durable write/receipt behavior; missed writes can occur despite intact DB pages |
| Kuzu | Read-only open and counts work: 27,134 nodes / 58,432 edges | Graph owner: old Sept 3/4 stale refresh/WAL/lock state predates incident; query success is not an all-page integrity audit |
| FontCache / CAMSvc | Crashed briefly during reboot; both measured running | Endpoint admin: no current outage shown |
| Python 3.14 | Standard library still absent; Python 3.11.9 and `mcp` work in fresh environment; Machine PATH has zero Python314 entries at 12:38 | MSTR/CTO: retain interpreter validation and resolve PATH rewrite mechanism; no CRO repair |
| Next crash capture | Initialization errors at boot despite today's successful dump | Endpoint admin/MSP: verify capture readiness after capacity recovery |
| Existing Desktop tripwire | Survived and resumed, but records scan timing rather than capacity/driver progress | CTO/endpoint admin: reuse evidence folder and extend observations deliberately |

Ntfs event 98 messages explicitly say the listed volumes are healthy. Their count
is not evidence of NTFS corruption. The reported earlier 04:36Z delivery-state
message was not recovered in the searched retained sources; it is not used to
attribute a midnight outage to today's disk exhaustion.

## 5. Recommended owners and acceptance evidence

These are proposed actions, not task orders or authority to modify the device.

| Recommendation | Proposed owner | Evidence that it worked |
|---|---|---|
| Reclaim reviewed, inactive checkouts and proven disposable scratch under Andrew's approved exact scope; preserve branches, detached refs, dirty/untracked work and pinned candidates | MSTR coordinates; COO lanes and checkout owners execute | Exact approved path manifest, preflight/live-owner review, bytes before/after; no unique work lost |
| Add capacity admission checks to bulk checkout/install jobs and propagate per-checkout failures | CTO + developer tooling owner | Insufficient-space attempt stops before fan-out, returns failure, creates no accepted partial candidate; reserve is based on measured concurrent needs |
| Make inbox/broker persistence reject failed or empty writes and surface capacity failure outside the failing local sink | CTO + MCP owner | Simulated write failure yields no false delivery success and preserves retryable message content |
| Investigate SentinelMonitor 26.1.2.177 with endpoint/MSP vendor support, using both dumps and the lock evidence | Endpoint administrator/MSP; CRO supplies local analysis | Vendor identifies the recursive-lock path and supplies a validated mitigation/update; ordinary workload no longer reproduces stall |
| Preserve today's kernel, minidump and Sentinel service dump on approved storage before overwrite/retention changes | CRO evidence owner + endpoint administrator | Hashes and retained locations recorded; no upload without separate authorization |
| Review memory pressure, pool growth, process churn and pagefile/capture capacity together | Endpoint administrator + CTO | Time series captures the peak that a post-stall snapshot misses; crash capture passes its operational check |
| Keep fresh-terminal interpreter preflight and track the MSI initiator; use a validated device-local interpreter selection where appropriate | MSTR + CTO runtime owner | Fresh `python` imports encodings and mcp after repair sweeps and reboot; the PATH writer is identified |
| Recover damaged checkout and reconcile missed deliveries before resuming its output | COO~X / checkout owner, MCP owner | Candidate files match intended commit plus preserved edits; consumer verifies actual delivery |

## 6. Capability brief for any follow-on — NOT current implementation claims

### Part I: outcome territory

**O1 — Andrew can keep using the desktop under normal development load** without
silent disk exhaustion or a security-driver lock freezing interactive applications.

**O2 — A development owner can recover capacity without losing unique work** and
can tell which outputs failed when storage was exhausted.

**O3 — The endpoint operator can diagnose the next stall from preserved evidence**
and can launch a fresh agent seat against a validated interpreter after reboot.

### Parts II–V: boundary, quality, substrate and dependencies

This owns the site Z incident findings and suggested prevention territory. It does
not own security-agent deployment, worktree removal, Python repair, or runtime code
changes. Existing `/cleanup`, `/kill` storage tooling, the Desktop freeze tripwire,
canonical seat startup, and MSTR's reclamation work are the measured substrate;
do not replace them merely because an incident occurred. The quality bar is usable
desktop continuity, truthful failure reporting, preserved unique work, and evidence
that survives the failure it records. Dependencies are Andrew's exact destructive
scope, endpoint-administrator access, vendor confirmation, and owner review of
candidate worktrees. No new project or task-order decomposition is issued here.

### Part VI: measured status — NOT OUTCOME-BEARING

Measurements span 12:00–12:38 ET, September 29; detailed clocks and units are in
the evidence summary. Capture-time observations describe 11:34:55, not current
resource use. Present remediation status from other seats is attributed explicitly.

### Part VII: nonclaims and remaining uncertainty

No exact free-space trace exists for the moment the volume first filled. No
complete pre/post allocation ledger identifies every growing or reclaimed file.
The amount of space restored by reboot is not fully explained: pagefile contraction
accounts for about 2.47 GiB; old dump replacement and other concurrent housekeeping
were not reconstructed. File mtimes do not measure newly allocated bytes.
No proof ties disk exhaustion to the driver's deadlock or the 08:28 service crash.
No private Sentinel symbols, vendor confirmation, driver reproduction, or whole-disk
forensic image was obtained. No universal all-worktree/content integrity claim is
made. An available broker is not proof that every seat is ready.

## References and retained evidence

- [Debugger findings and reproducible commands](DEBUGGER_FINDINGS.md).
- [Joint reclamation review](RECLAMATION.md).
- [Sanitized measurements and evidence fingerprints](evidence-summary.json).
- Raw outputs remain local under `.runtime/crash-investigation-20260929/`; raw
  transcripts, dump files and full machine event exports are not committed.
- Existing Desktop folder:
  `C:\Users\Opal Bloomberg\Desktop\OPAL_BLOOMBERG_freeze_investigation_2026-07-30`.
- Prior Python repair:
  `org/tier1_exec/1.0.0_SA_CTO/deliverables/HANDOFF_ELEVATED_PYTHON_PATH_FIX_20260928.md`
  at `be2d74b00739ab0b94b5a97f5f7b4ab68adf7044`.
- Source transcript for ENOSPC:
  `.claude/projects/C--Users-Opal-Bloomberg-Desktop-ajb-workspace/ebcfd7bb-bf38-4724-a6b1-60d4edace135.jsonl`,
  line 5148, beneath this device's user profile.
- BRIEF PATH: this file. PROJECT: NONE-YET. EXISTING PRD: NONE for this incident.
  SIBLING WORK: MSTR site Z reclamation. No follow-on implementation approved here.
