# CVO (base) — RV-0049 ACCEPTED-CVO · F-003b: the orphan-hook fix is INERT ON THE RUNNER · and the OPAL_ASSETS read hazard is 4.70x, not 3.3x

**agent:** 3.0.0_SA_CVO · **date:** 2026-07-13 · **window:** 13:38Z (cold start, Andrew-respawn) -> 14:35Z
**archetype:** VALIDATE · **secondary_archetypes:** DIAGNOSE, COORDINATE

## Context on the start

Andrew closed my prior session and respawned me directly. **Its watcher child did not die with it.** A fresh
session that finds a matching `inbox-watch.sh` has found an ORPHAN, not a watcher — pid 648983 (ppid 647377,
**dead**), running since 06:19 local, `mv`ing my arriving mail into `read/` before echoing into a dead pipe.

Reaped it **scoped** (`kill-orphans --serial 3.0.0_SA_CVO --force`), after reading the tool's matching code
rather than trusting the flag name: `--serial` is tilde-EXACT (`[ "$serial" = "$SERIAL_FILTER" ] || continue`),
so it cannot reach `3.0.0_SA_CVO~B` — **who was live and working.** Positive-controlled both ways: the dry-run
matched exactly 1 pid, and I asserted the **spare list** before and after (**10/10 healthy watchers survived**).
*A reap reports what it KILLED; it must also prove what it SPARED* — that arm is the only one that catches a
cascade, and the CTO's `Stop-Process` cascade earlier today is why it exists.

## What happened

### 1. RV-0049 — **ACCEPTED-CVO** (`a83c6fadb`). Watermark may advance.

MSTR was proxy-ineligible (19 overrides + 33 law-doc edits in-window) and the watermark was frozen on my verdict.
**I re-took both of my blocking readings rather than accept his report that they were clear** — his own message
carries the rule that binds me: *"a review that does not re-take its own readings is auditing a photograph."*

- **B1 (F-003 fix uncommitted) -> DISCHARGED.** `920a7bb77` is a real ancestor of HEAD on CLOUD; HEAD's hook =
  **180 lines** (control on the RETRIEVAL — a `grep -c 0` can count an error message, a line count cannot).
  **And `git diff HEAD -- <hook>` is EMPTY, so the copy that EXECUTES is the copy that was reviewed** (a hook runs
  from the working tree; "fixed in HEAD, stale on the runner" is the F7 shape).
- **B2 (F-001 disclosure) -> DISCHARGED.** `git-author-override-audit.log:13187`, confirmed by independent
  `grep -n` (not his line number), in a **13,340-line** file — denominator printed, because `sed -n '13187p'` on a
  shorter file prints NOTHING and I must never read that silence as absence.

### 2. **F-003b (NEW, HIGH) — THE FIX LANDED. THE CONTROL DID NOT.**

The hook has 3 observables: the success marker (written ONLY on rc==0), an `ORPHAN-CLEANUP-FAILED` audit line, and
the reap itself. **A real `register_agent` produces NONE of them.** Across 3 post-fix registrations (AE~A 13:25:20Z;
me 13:42:18Z + 14:06:35Z): marker **absent**, failure lines **0**, `KILL-ORPHAN` **7 -> 7**, my live watcher **alive**.
**Zero markers exist fabric-wide since the fix landed** (last 10:38Z; fix 11:02Z).

**Controls (a zero is the one result an instrument can produce for reasons unrelated to the estate):** the `find` is
not blind (**7** markers pre-fix, **0** after); **PostToolUse hooks DO fire in my session** (telemetry written the same
minute); the matcher is exactly right and **fired this morning** (21 markers, 10:15-10:38Z); **the hook WORKS when
executed** (fed the documented payload directly it resolves a real bash, runs kill-orphans, rc==0, writes its marker —
every time); and **the wiring did not change** (`920a7bb77` touches ONLY the .py; settings.json unchanged since 02:02,
i.e. BEFORE the 21 good markers). **The regression window is EXACTLY the fix commit, wiring held constant.**

**The benign reading is FALSIFIED BY EXERCISE, and my own watcher is the discriminator.** *"CLAUDE_CODE_SESSION_ID
unset -> marker=None -> silent"* reproduces the signature exactly — **but on that branch the hook STILL RUNS THE
SUBPROCESS**, and `kill-orphans --serial 3.0.0_SA_CVO --force` **matches my live watcher exactly**, with the V4
self-kill guard **disengaged** (no marker existed). **It would have been reaped. IT WAS NOT.**
>> **THEREFORE THE HOOK NEVER REACHES ITS SUBPROCESS CALL.** <<

**MECHANISM: UNGROUNDED, and I did not guess it.** Routed to CTO (hook owner). *Six mechanisms, seven agents, eleven
hours, zero correct — the answer was in a log nobody opened.*

**Consequence:** the defect F-003 names is **unchanged and live** — my own orphan survived ~7h20m THROUGH a fresh
registration and had to be killed by hand. **And the repair ARMS a worse bug if done naively:** the marker IS the V4
guard; every agent registering post-fix has none; so the moment the hook starts executing, a mid-session re-register
reaps the agent's OWN LIVE WATCHER. **Fix execution + marker in one commit, and exercise a re-register with a live
watcher present before signing.**

**By-catch, resolving a rulebook `UNDETERMINED`:** my manual reap wrote the **first-ever `KILL-ORPHAN` audit line**.
The audit path is real — so a zero hook-driven reap count is now a **REAL ZERO, an observation rather than an
instrument gap.**

### 3. Andrew-direct: verify 0.7.0_AE_CloudOps~B's two queue items. **BOTH REPORTS WERE STALE.**

- **OPAL_ASSETS R-A/R-B:** reported *"held pending 0.8.0's guard rewrite."* **CLOSED 06:28:35Z**, all 5 legs proven;
  0.8.0's v0.2 guard (`f10d957a1`) is IN L1, suite 30/30.
- **Schwab 08335338 L3:** reported *"held on the EC2 job."* **CLOSED 10:37:03Z**; 6,932 files landed, census green.
- **The tell:** he said **494 rows**; live table is **532** (DDB ItemCount + my full scan agree). 532-494 = 38 =
  19 partitions x 2 total rows — **the rows R-A ADDED.** He is reporting a pre-06:28Z snapshot.
- **CVO~A IS DEAD** (no watcher, absent from liveness.json, last mail 04:31Z). **That — not negligence — is why the
  residue decision "nobody has touched" was untouched: it was parked on a lane that no longer exists.** Its inbox is
  empty (0 unread, no orphan), so nothing was silently eaten.

### 4. **The OPAL_ASSETS read hazard is REAL, and LARGER than reported — and R-A made the naive read WORSE.**

Grounded on the LIVE table (`opal-assets-daily-aua`, keys `run_date`/`cohort_id`, 532 rows, full pagination):
- **`SUM(value) WHERE additive` = $1,758,111,296.54** on 2026-07-10 — the certified headline **to the cent**, on
  **all 19 partitions**. **R-A works.** 0 rows missing `additive`, 0 missing `basis`.
- **Naive `SUM(value)` = $8,261,089,407.78** on the same partition — a **4.70x** overstatement.
  **NOT the ~$5.82B / 3.3x reported. His figure does not reproduce against the live table and I did not guess why.**
- **R-A INCREASED the naive number** by adding 2 total rows/partition. *The fix that made the correct query correct
  made the incorrect query further wrong.* A flag protects a reader who knows to filter; a reader who does not is now
  **further from the truth than before the fix.**
- **`additive` is a CONVENTION, not a STRUCTURE.** Five `basis` grains (`partner_aua` 57, `partner_model_detail` 133,
  `partner_platform_view` 19, `etf_fund` 95, `etf_ownership` 228) + totals all carry an attribute named `value` and are
  structurally identical. **The obvious query returns 4.7x and nothing stops it.** *A row that looks like the thing and
  is not* — the phantom-advisor class. **Fix PROPERTY (mechanism is CTO~B's PRD call): a non-summable row must not carry
  a summable attribute named `value`,** so the naive query is right BY CONSTRUCTION rather than merely avoidable.
- **Surfaced, not adjudicated:** the "daily" table has **gaps** (06-25 -> 07-02; 07-09 missing). Andrew's mandate is
  worded *bullet-proof DAILY tracking*. Needs an explicit yes/no; I have not grounded the cause.

### 5. **The 08335338 residue: KEEP — but "keep" is not "verified", and the decision is Andrew's.**

Nothing leaked: `backfill/` holds only `08335338/`; `01_raw/`/`bronze/`/`silver/` are **zero**. **There is nothing to
purge.** My independent object count (**6935**) matches L3's census exactly.

**I identified the 233 residue files independently** — objects with `LastModified` before the resumed run's plan
(03:56:51Z). The split comes out **233 / 6,699, matching `final_manifest` EXACTLY** (a positive control neither of us
planned). They are `rld` 110, `tcf` 119, + 4 singletons; written 03:00-03:53Z; **0 zero-byte**; 7.8KB-8.5MB.

**They are almost certainly fine and I refuse to inflate it:** S3 `PutObject` is **atomic**, so a killed upload leaves
NO object — every landed object is a complete upload of a local file that passed the non-zero gate.

**But two things are true and NEITHER is recorded anywhere:**
1. **The 233 are the only files with no fresh integrity evidence.** The other 6,699 each passed HTTP-200 + non-zero +
   `s3 cp rc=0`. These were skipped on **filename existence alone** (`sdd-backfill-08335338.ps1:161 @ working-tree`:
   `if ($landed.ContainsKey($pn)) { $skip++; continue }`) — and they came from **the run that was HALTED.**
   **Every census control (0 zero-byte, 0 duplicates, plan==landed per type) is BLIND TO CONTENT.** A truncated object
   is non-zero, unique, and counted in its type: **it passes every one of them.**
2. **If any of them IS bad, it can NEVER self-heal.** The resume index keys on **filename only**, so a corrupt object is
   skipped forever, on every future run. **Append-only + skip-on-exist is a silent poison pill** (same family as F8's
   append-only + fail-on-read).

Also: `plan_manifest.json` carries only per-TYPE aggregates (**no per-file sizes**), and `final_manifest.json` records
`skipped: 233` as a **bare counter with no skipped LIST**. *The 233 were not even identified until I reconstructed them.*

**DISPOSITION: KEEP, UNVERIFIED, DISCLOSED — pending Andrew.** The only real verification is a **re-download of the 233**
(~12 min at the measured 19/min, 0.3% of the job) — **and that is a SCHWAB VENDOR CALL, which remains HELD** (the
2026-07-13 Orion lift is **ORION-ONLY**; every other vendor stays held). **So this is properly a sovereign decision and
I will not touch it without his explicit per-use word.** *Recording "keep" as GREEN would be the lie; recording it as
KEEP-UNVERIFIED is the truth.*

**Durable fix (next backfill, a design item — NOT this decision): the resume index must key on `(filename, size)` and
the run must persist the skipped list.** Today, *"a file that EXISTS"* and *"a file that is CORRECT"* share a signature.

## Compiler Tools

| Tool | Run | Result |
|---|---|---|
| `.tools/kill-orphans` | dry-run then `--serial 3.0.0_SA_CVO --force` | **PASS** — 1 match, reaped; **10/10 healthy watchers SPARED** (spare-list asserted pre+post). Read its matching code before trusting `--serial`: tilde-EXACT, cannot reach `~B`. |
| `org/mcp/hook_register_orphan_cleanup.py` | driven directly with the documented stdin payload (probe serial owning ZERO watchers) | **PASS as code / FAIL in the wild** — writes its marker every time when executed; produces NOTHING on a real registration. This IS F-003b. |
| `.tools/safe-commit.sh` | determination + this log | PASS (`a83c6fadb`); surface-check OK, 0 critical surfaces |
| boto3 / `aws` (live reads) | DDB full-scan `opal-assets-daily-aua` (532 rows); S3 full-pagination `backfill/08335338/` (6,935 objects) | **grounded every number on the LIVE artifact, never the ledger** (NEVER#5). Every census printed its DENOMINATOR. |

- **What worked:** exercising, not reading. F-003b exists because I ran a `register_agent` and *looked at what came
  back*, and the benign explanation died to a live watcher rather than to an argument. The 233-file reconstruction
  matching `final_manifest` to the row is the positive control that makes the residue finding trustworthy.
- **What failed — MY OWN INSTRUMENT, twice.** (a) My first DDB read **summed across all 19 partitions** and reported
  $157B/$33.9B; the verdict unit is **one partition**. *Count at the unit at which the verdict is rendered.* I caught it
  because $33.9B/19 landed suspiciously near the certified headline. (b) My S3 prefix listing used
  `--query 'CommonPrefixes[]'`, which applies **PER PAGE** and printed `None` x28 — **the exact artifact the 08335338
  ledger itself warns about.** I re-ran with an instrument that works instead of reading the `None`s as an absence.
- **Gap found / rail miss, self-disclosed:** I ran a raw `dynamodb describe-table`, which per CLAUDE.md Rule 21 is a
  `comp-aws`/`comp-freshness` case. The row-level scan is legitimately off-rail (DATA-ACCESS, no graph), but the
  describe was not. **Disclosing my own miss rather than omitting the row.**

## Blockers

**None mine.** Two items are gated on OTHERS, and neither is a block on me:
- **F-003b mechanism** is CTO's (hook owner). I supplied the exercised symptom + the falsified benign reading; I will
  not supply a guess.
- **The 233-file re-verify is SOVEREIGN-GATED** (a Schwab vendor call). Awaiting Andrew's explicit per-use word.
  **Not a block — a correctly-placed decision.**

## Current State (zero-context handoff)

- **RV-0049: ACCEPTED-CVO** @ `a83c6fadb` (`org/tier1_exec/3.0.0_SA_CVO/deliverables/CVO_RV0049_DETERMINATION_20260713.md`).
  Watermark may advance. **F-003 STAYS OPEN — nobody closes it on `920a7bb77`.** MSTR + CTO both messaged.
- **F-003b OPEN:** `org/mcp/hook_register_orphan_cleanup.py` is committed, code-sound, and **does not execute on a real
  `register_agent`**. Orphans are still never auto-reaped fabric-wide. The naive repair arms a deafness bug (see above).
- **OPAL_ASSETS:** R-A/R-B **landed and CORRECT** (`SUM WHERE additive` == certified headline to the cent, all 19
  partitions). **Read hazard OPEN:** naive `SUM(value)` = **$8.26B vs $1.76B (4.70x)**. Not routed yet — see Next Steps.
- **08335338:** backfill COMPLETE, census green, nothing leaked, **nothing to purge**. Residue = **233 named files**,
  **KEEP-UNVERIFIED**, pending Andrew.
- **Watcher:** Monitor task `bw5w9yvdc`, child pid 1570173. **Zero crons** (LD-0175).
- **My standing queue (from CTO, unchanged):** verify DS's RESIDUAL guard on the patrick_scanlan **$52,604.80** served
  defect (`d52ab4cbe` / `10273505d` landed), and DS~A's silver chokepoint guard (`d28f2d5b9`) — **against what the
  LAMBDA runs, not the repo** (the vendored libs are a diverged fork), and **with the over-condemnation arm**.

## Next Steps

- **[me]** route the OPAL_ASSETS read-hazard finding (4.70x, and R-A made naive worse) to **[1.0.0_SA_CTO~B]** (PRD
  owner), **[2.0.0_SA_COO]**, **[0.8.0_AE_CloudComp]** (guard) — the fix PROPERTY, not the mechanism.
- **[me]** verify DS's RESIDUAL guard + the silver chokepoint guard on the DEPLOYED artifact.
- **[Andrew]** the 233-file re-verify: a Schwab vendor call, held. **KEEP-UNVERIFIED until he says otherwise.**
- **[1.0.0_SA_CTO]** ground F-003b's mechanism; fix execution + marker in ONE commit; exercise a re-register with a
  live watcher present.
- **[0.0.0_AB_MSTR]** RV-0049 tag/watermark; fold F-003b in.
- **[2.0.0_SA_COO]** **CVO~A is DEAD** with an OPAL_ASSETS validation lane parked on it — respawn or re-home.

— 3.0.0_SA_CVO
