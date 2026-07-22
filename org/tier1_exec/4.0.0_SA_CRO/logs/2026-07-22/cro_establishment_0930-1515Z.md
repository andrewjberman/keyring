# CRO establishment — serial chain, exec home, grants, and RCN-0001 re-tag (0930-1515Z)

**archetype:** MIXED
**secondary_archetypes:** COORDINATE, SCRIBE, DIAGNOSE, EXPLORE

**Agent:** `4.0.0_SA_CRO` (Chief Research Officer, Tier-1 exec)
**Session:** 2026-07-22, ~0930Z start -> 1515Z. **First log of this serial.**
**Window:** whole session (no prior log — serial did not exist at session start).

---

## Summary

Started this session as `0.4.0_DS_ClientPlatform~Z` to reload the 07-21 Black Diamond research thread on
Andrew's instruction. Andrew then established a standing competitive-recon mandate, converted it to a
standalone serial, then to a **Tier-1 exec**. Session ran under **three serials on one PID (23096)**, all
Andrew-direct. Ended established: exec home committed and exercised, two owned-paths grants landed by others
as grantor, ORG_CHART row in, both open authority cells ruled by Andrew, RCN-0001 re-tagged.

**No research tasking executed this session.** The work was establishment + governance + the RCN-0001 context
reload. Holding for research tasking.

---

## Serial chain (DO NOT "RECONCILE" — see charter §7 / LD-0331)

| Serial | Window | Outcome |
|---|---|---|
| `0.4.0_DS_ClientPlatform~Z` | 07-21 -> 07-22 | Produced RCN-0001. **Commits authored `~Z` permanently** (`efdb4dbd8`, `b3783b866`, `a6dfa0a7e`) |
| `0.9.0_FR_ExtResearch` | 07-22, ~1 hour | Superseded before committing anything. Left no commits |
| **`4.0.0_SA_CRO`** | 07-22 -> | **Current.** Owns everything above |

Same PID, same session throughout — re-identification, never a second agent. Three `register_agent` calls
carry `identity_override`; reasons are in the audit. Docs are **re-tagged** to the CRO with the producing
serial preserved beside the tag: **commit author = historical fact, tag = current ownership.**

---

## Work completed

**Establishment (mine):**
- Exec home `org/tier1_exec/4.0.0_SA_CRO/` — charter (README), launch persona (prompt.md), append-only
  `RECON_REGISTER.md`, `scripts/`, standard exec dirs. 13 tracked files at HEAD.
- **Recon tooling rescued** from a session scratchpad `/kill storage` reaps -> `scripts/`.
- ORG_CHART Tier-1 row, carrying the authority boundary and the then-open cells.
- Charter bound to `docs/doctrine/INSTRUMENTS_AND_AXES.md` (method rule 9) + three worked failure examples.
- Both Andrew rulings recorded as **answered**, not deleted.

**Grants (landed by OTHERS as grantor — SoD, I am the grantee and wrote none of them):**
- `74639eb59` (`0.0.0_AB_MSTR`) — `CRO_WORKSPACE` lane + home path rule + `ANY_EXEC`.
- `c3b2f0dab` (`0.0.0_AB_MSTR`) — `ANY_EXEC_OR_AE`, **scoped in the lane comment to project registration
  only**, on Andrew's ruling.

**RCN-0001 re-tag:** 3 docs in `docs/research/bd_dashboard_teardown/` re-tagged to CRO ownership; one stale
*ownership* reference corrected inside the build spec; the three *provenance* references to `~Z` deliberately
kept.

---

## Verification performed (what was EXERCISED vs merely applied)

| Claim | Grade | Evidence |
|---|---|---|
| Home-folder grant works | **EXERCISED** | The gate returned 6x `UNDEFINED` pre-grant and refused; post-grant 3 commits landed (`2ac742e2b`, `e031b1365`, `0da685f2b`). Behaviour, not config. |
| Preserved tooling is behavior-neutral | **EXERCISED** | Re-ran original AND ruff-normalized scripts over the original 8-HAR corpus: **229 endpoints / 52 schemas** reproduced (the exact published denominators) and **218 output files byte-identical**. |
| ORG_CHART row landed | **EXERCISED** | `git show HEAD:org/ORG_CHART.md` -> 2 occurrences. |
| SoD held on both grants | **MEASURED** | grantor `0.0.0_AB_MSTR` != grantee `4.0.0_SA_CRO` on both. |
| `ANY_EXEC_OR_AE` membership | **APPLIED, NOT EXERCISED** | Verified at HEAD w/ generated negative control (target YES; positive `1.0.0_SA_CTO` YES; negatives `0.4.0_DE_ClientPlatform` NO and fabricated `9.9.9_ZZ_NotAnAgent` NO). **No project registered — refused to manufacture a throwaway JSON to prove a gate (hand-staging the artifact).** First real registration is the test. |
| Identity clean after cleanup | **EXERCISED** | Plain `heartbeat("4.0.0_SA_CRO")` with **no** `identity_override` returns OK. |

---

## Compiler Tools

| Tool | Invocation | Result | Note |
|---|---|---|---|
| `.tools/commit-gate.sh` | on both preserved `.py` (twice) | **FAIL -> PASS** | Blocked on 5 then 29 ruff errors. Fixed rather than overriding; gate is universal and a style nit is not an override case. |
| `.tools/safe-commit.sh` | 4 commits | **PASS** | Also the source-read below. |
| `comp-surface-check` (auto in safe-commit) | 4x | **PASS** | "9 changed file(s) touch no critical surface" on the establishment commit. Advisory only — read, not assumed. |
| `comp-pulse diff` (risk-reflex, auto) | 4x | **CLEAN** | Denominator printed each time (e.g. 9 files vs 1239 danger nodes). **Danger map self-reported 199.8h STALE** — recorded because a clean verdict off a stale map is worth less than it looks. |
| `Get-CimInstance Win32_Process` | PID truth, 7 PIDs | **PASS** | Replaced a broken `ps -ef`; see gap. |

**What worked:** the gates did the work. `commit-gate` caught real style debt in rescued code; `safe-commit`'s
`--only` protected a shared dirty index; the owned-paths gate produced all three "a title is not a grant"
findings.
**What failed:** `ps -ef` (see gap). Also my own first two hypotheses about broker liveness.
**Gap found:** **`comp-pulse`'s danger map is ~200h stale** and says so in its own output — it is honest, but a
CLEAN reflex against a 8-day-old map is weaker evidence than the word CLEAN implies. Surfacing, not fixing;
not my lane.
**Comp-rail note:** this session was governance/doc work, not code or infra investigation, so
`comp-which`/`comp-grep` were not the right instruments for most of it — searches were native `Read`/`Grep` on
known paths plus direct `git show HEAD:<path>` reads of the record. No raw `aws` inspection and no
`infra/*.tf` grep occurred.

---

## MCP traffic

**11 messages** (5 sent, 6 received) across `0.0.0_AB_MSTR`, `1.0.0_SA_CTO`, `2.0.0_SA_COO`. Significant:
- **MSTR** — landed both owned-paths grants as grantor; authored LD-0331 (+ amendments); confirmed
  spawns/roster are NOT mine; supplied the project-registration procedure.
- **CTO** — **confirmed the authority boundary verbatim, no amendment**; took CVO's missing ORG_CHART row;
  routed the broker item to `0.8.0_AE_CloudComp`.
- **COO** — deregistered `0.4.0_DS_ClientPlatform~Z` then `0.9.0_FR_ExtResearch`; **self-reported that
  `kill_pollers=False` was wrong** (orphan `agent-poller.py` processes were silently re-registering the rows
  seconds after removal, behind a tool success message).

---

## Findings issued

1. **A TITLE IS NOT A GRANT** — three instances in one onboarding, each caught by a gate and invisible from
   the record that supposedly conferred the authority: (i) being made an exec did not grant the home folder;
   (ii) MSTR being roster authority did not let MSTR write the roster; (iii) Andrew ruling "you can register
   projects" did not permit writing a project JSON. **(iii) is sharpest — `org/projects/**` genuinely IS
   `ANY_EXEC` and I genuinely AM in it; longest-match silently reached the narrower `ANY_EXEC_OR_AE` on
   `REGISTRY.md` + `*.json`.** A correct read of the wrong rule. CTO folding in as a standing note; MSTR
   backs a gate candidate if Andrew greenlights.
2. **`safe-commit.sh:607` is `git commit --only -- PATHSPEC`** — commits only named paths, ignores the rest of
   the index. Corrects a belief MSTR was operating on and correctly narrows the documented sweep precedent
   (that incident was a *bare* `git commit`). Verified after the fact: owned-paths files in my commit = 0.
3. **Two self-corrections, both mine** — see below.

---

## Self-corrections (recorded as failures, not smoothed over)

1. **Asserted a mechanism in a durable audit record.** My `identity_override` reason stated broker liveness
   was PID-keyed as though grounded. A control **refuted** it. I flagged my own audit line as an over-claim in
   the next message rather than letting it stand.
2. **Used a broken instrument and nearly reported the output.** `ps -ef` returned "does not exist" for **every
   PID including my own and MSTR's**, whom I had messaged four times. **The positive control failed, so the
   instrument was broken, not the finding** (documented MSYS artifact). `Get-CimInstance Win32_Process` showed
   all alive and all `python.exe org/mcp/server.py` — **MCP server processes, not agent sessions** — which
   dissolved the "defect" entirely. I was also one step from reporting "`last_seen` is bulk-refreshed";
   declined for want of reading the writer, and COO's poller kill later built the control that **falsified**
   it (dead rows froze; the live row advanced).
   **Net: no defect reported. A reproducible symptom with mechanism marked UNKNOWN was routed to CTO instead.**

---

## Current State

`4.0.0_SA_CRO` is LIVE (PID 23096), registered, watcher armed under its own serial (task `be53805cs`), zero
crons, LD-0290 marker set. Registry clean — both predecessor serials deregistered by COO, plain heartbeat
succeeds with no override.

**Owned + granted:** `org/tier1_exec/4.0.0_SA_CRO/**` (lane `CRO_WORKSPACE`) · `ANY_EXEC` (cross-exec
task-order authoring) · `ANY_EXEC_OR_AE` **scoped to project registration only**.
**NOT owned (CTO-confirmed verbatim):** applies/deploys = CTO · TO-decomp/dispatch = CTO+COO · moving served
output = never-widen co-sign · **vendor egress = Andrew per-use, every time** · spawns/kill/allocation = MSTR ·
roster/ORG_CHART maintenance = MSTR+CTO.

**Andrew's rulings (2026-07-22):** project registration — *"You can register projects yes."* -> granted, and
now grant-backed. Cross-exec co-sign standing — *"Not needed."* -> **CLOSED-NOT-GRANTED, do not re-open.**

**RCN-0001 (Black Diamond)** — delivered, indexed in `RECON_REGISTER.md`, artifacts at
`docs/research/bd_dashboard_teardown/`. Downstream `fact_account_return` **HELD at CTO's D6 registration**,
post-MDPF-flip; that hold is live — the MDPF re-land co-sign went 2-of-3 -> **0-of-3** today after a defect
was found inside the frozen data. D1 (Account365 method pin) and D2 (classification build-vs-license) are
research-surfaced **build** decisions; Andrew questioned whether they pertain to CRO responsibilities and he
was right — **they are parked behind the D6 gate in the register, not carried as asks at Andrew.**

**Convention learned this session (was the one gap in the home folder):** session logs are mandatory every
tier, `## Compiler Tools` non-optional, archetype tag required, `org/compiler-tools-log.md` appended in the
same pass. MSTR ruled **`RECON_REGISTER.md` IS the CRO core document** (not `architecture_brief.xml`, which is
a Tier-2+ build-role convention and a poor fit for a research exec).

---

## Blockers

**None.** Nothing is blocked. Project registration is grant-backed but unexercised for want of a real project,
which is a state, not a blocker.

---

## Next Steps

- **[4.0.0_SA_CRO]** Hold for research tasking from Andrew. First real project registration will exercise the
  `ANY_EXEC_OR_AE` path — ping MSTR when it lands so they can confirm exercised grade. If a research macro is
  needed, propose `RCON` to CTO rather than mis-parenting under a build macro (a macro is a surface-area
  claim).
- **[4.0.0_SA_CRO]** Authority-resolution gate spec ("can X actually write the paths that constitute doing
  Y?") — **HELD, not started.** MSTR's backing is on the record; awaiting Andrew's greenlight. Self-selecting
  infrastructure work is the scope-widening the charter table exists to prevent.
- **[1.0.0_SA_CTO]** CVO's missing ORG_CHART row (he took it); the broker stale-row symptom routed to
  `0.8.0_AE_CloudComp`.
- **[0.0.0_AB_MSTR]** LD-0331 §6 carries the TO disposition: all 7 pending TOs surfacing on the `~Z` query
  resolve to `org/tier2_senior/0.4.0_DS_ClientPlatform/task_orders/` — **base-DS's, none ever `~Z`'s.**
