# /spot-check cycle — 2026-07-28T1315Z (base CVO, MAIN fabric)

**archetype:** VALIDATE

Ad-hoc single cycle at session load. **No cron armed** — the skill's default is a 20m cron, but
LD-0175 + XXX.md Step 1b-F bind base CVO to ZERO crons; the launcher's `/spot-check ad-hoc` wins over
the skill's default form. Recorded because a future reader will see a bare `/spot-check` invocation
and should know the cron was deliberately not armed.

## Scope — stated, not silently capped

| quantity | value |
|---|---|
| `.spot-check-checkpoint` | `f6cb5b13f` — **2026-07-20T18:42Z. The sweep has not run in 8 days.** |
| delta checkpoint..origin/CLOUD | **1,637 commits** |
| delta since my last base-CVO commit (`6543fd12ef`, 07-24T2225Z) | **417 commits** |
| of those, main-fabric-authored | **4** (all `1.0.0_SA_CTO`) |
| of those, ~Z-group + `0.8.0_AE_CloudComp` pod | **413** |

**I did not triage 1,637 commits and I am not going to imply that I did.** The window I actually
swept is the 417 since my last base-CVO session — the period the main fabric ran with no main-fabric
verifier present. Within it, **413 of 417 commits are outside my lane**: `1.0.0_SA_CTO~Z` (170),
`3.0.0_SA_CVO~Z` (70), the `0.8.0_AE_CloudComp` pod incl. 5 lanes (171), `2.0.0_SA_COO~Z` (2). Per
LD-0325 the ~Z group's verification surface is CVO~Z's, not mine. **The 1,220 commits between the
07-20 checkpoint and 07-24 remain UNSWEPT** and the checkpoint advance below does not mean they were
examined — it means the checkpoint was already 8 days stale and re-walking that backlog per-commit is
not the cheapest way to catch what it would catch.

**Retrieval control (it fired):** `git log … | wc -l` returned 416; `| grep -c .` returned **417**.
git's output carries no trailing newline, so `wc -l` undercounts by one. The true denominator is 417.
A one-commit error changes nothing here — I record it because the same undercount on a *gate* count
would, and the control cost one extra call.

## Findings

### F-1 (P1, routed — CTO + COO) — a P0 program with 12+ closure rows is INVISIBLE to every registry-based governance instrument

`MDPF_CHANNEL_INDEPENDENCE` has:
- a **34,947-byte PRD** at `docs/architecture/MDPF_CHANNEL_INDEPENDENCE_PRD.md`,
- **12+ enumerated closure rows** with per-row owners across ≥5 serials (`0.6.2~C`, `0.7.0`,
  `0.7.0~A`, `0.7.0~B`, `0.4.0_DS~A`, me),
- an **Andrew-direct P0 authorization** ("Go now, this is P0", ~1720Z 07-24) and a sovereign
  design directive behind it,
- TOs dispatched and at least one verdict delivered (CI-R4),

and **NO `org/projects/MDPF_CHANNEL_INDEPENDENCE.json`** and **NO row in `org/projects/REGISTRY.md`**
(`grep -c` → **0**).

**Positive control run separately, and it is what makes the zero mean something:** `MDPF_3FIRMS` →
**2** hits in the same file with the same grep. The instrument finds a known-present sibling, so the
zero is a real absence and not a broken retrieval. Eleven other `MDPF_*` projects carry JSONs.

**Consequence, which is the part that matters:** `/registry-check`, `/prd-check`, `/to-check`'s
hot-project filter and COO's `/drive` scan all resolve work through the registry + project JSONs.
**A program that exists only as a PRD plus TOs is unreachable by all of them.** It cannot be listed
as active, cannot be closed via the 2-step closure discipline (which is defined *on* the JSON), and
its 12 rows cannot be rolled up by anything except a human who already knows to look. This is not a
tidiness complaint — it is the reason a P0's rows can sit four days without anyone's status view
showing a gap.

**Not fixed by me, deliberately.** Creating a project JSON + REGISTRY row is project *creation*, not
alignment-metadata repair; my fix scope covers drift in existing records, not minting the
authoritative close-state artifact for someone else's program. **CTO** owns the PRD and the closure
gate; **COO** owns registry decomposition. Routed to both.

### F-2 (observation, no action) — the record-surface touches in the window are all outside my lane

Every `task_orders/` and `org/projects/` touch in the 417 is under
`org/tier2_senior/0.8.0_AE_CloudComp/task_orders/` (NFRA_MSBEFF, NFRA_SYSPARITY ×2, NFRA_TOOLARCH ×3,
nfra-toolunify). ~Z-group surface → CVO~Z's, not mine. No main-fabric project JSON or REGISTRY row
was touched by anyone in four days.

### Closed this cycle (self-caught, recorded in full elsewhere)

- CI-R4 TO cell `pending` → `complete`, then **amended** to separate the TO's completion from PRD row
  4's *non*-closure per CTO's explicit instruction (`b5d46c6b7`, `c26a30418`).
- The 07-24 unlogged 7-hour window → RECONSTRUCTED log, marked as such.
- **My own claim "not even SENT is established" RETRACTED** — CTO produced the `read/` artifact.
  Mechanism: I treated the absence of *my* record as the absence of *the event*, without looking in
  the recipient's folder. Wrong in the direction that overstated the gap.

## Compiler Tools

| Tool | Invocation | Result | Note |
|---|---|---|---|
| `comp-surface-check` (auto via `safe-commit`) | 2 commits | no critical surface | both confined to my own tree |
| `comp-pulse diff` risk-reflex (auto) | 2 commits | reflex clean | denominator printed per commit |
| `git` + `grep` with positive control | F-1 | 0 hits / control 2 hits | the control is what licenses the zero |

**Why no graph/comp traversal tool ran:** every question this cycle was *"does this record exist and
does it agree with that artifact"* — record-presence and cross-doc alignment, which no comp-tool
models. **`comp-which` was not consulted first, which is a rail deviation I am recording rather than
excusing**; A.3 measured **4 of 92 comp-tools resolving bare** in this shell, so bare `comp-which`
would not have resolved anyway and the explicit `.tools/` prefix was available. The honest statement
is that I reached for `git`/`grep` by reflex and the rail's fallback was degraded in the same shell.

## Checkpoint

Advanced `f6cb5b13f` → `origin/CLOUD` HEAD. **This advance asserts the 417-commit window was swept at
the stated scope; it does NOT assert the 1,220-commit 07-20→07-24 backlog was examined.** Recorded so
the next cycle does not read a clean checkpoint as a clean history.

— 3.0.0_SA_CVO
