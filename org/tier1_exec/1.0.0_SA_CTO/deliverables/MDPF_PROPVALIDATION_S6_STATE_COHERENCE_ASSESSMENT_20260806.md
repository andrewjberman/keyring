# MDPF_PROPVALIDATION — §6 state-coherence ASSESSMENT (Rule 24(iv))

**Author:** `1.0.0_SA_CTO~Z` (site Z) · 2026-08-06
**Owns:** the assessment. Supersedes the classification in
`org/tier0_exec/0.0.0_AB_MSTR/deliverables/MDPF_PROPVALIDATION_STATE_COHERENCE_FRAMING_20260806.md` @73ca92eb3
(MSTR~Z framed the shape and explicitly delegated the verdict).
**Consumers:** `2.0.0_SA_COO~Z` (decomposes Phases 0–6 off THIS classification), `0.7.0_AE_CloudOps~Z`,
`0.4.0_DS_ClientPlatform~Z`, `0.0.0_AB_MSTR~Z` (carries the Andrew-facing items).
**Source pack:** `projects/MDPF_PROPVALIDATION/` §6 of `04_VALIDATION_ROLLBACK_AND_OPEN_HOLES.md`.
**⚡ AMENDED IN-FLIGHT 2026-08-06 ~2030Z:** Andrew resolved H4 while this was being written
(`ANDREW_DIRECT_20260806_MDPF_EC2_TEARDOWN_AUTHORIZED_PORT_COMPLETENESS_CONDITION.md` @c801ec9d5).
H4's authority half is closed; its **condition** re-lands on Class A as an ordering-critical item. See §2B and §2A′′.

> **⛔ NO GATE IS CREATED BY THIS DOCUMENT.** Not one row here is an approval step, co-sign, hold, or
> review choke point. The classification is a **ledger honesty instrument**: it says what closes each
> item and what a closure claim is allowed to assert. Every phase proceeds on its own evidence.
> Two rows (B1/B2) attach to specific **irreversible physical acts** and are **pre-existing** — one is
> already in the pack, one is already CLAUDE.md standing law. Surfacing existing law is not
> manufacturing a gate (CLAUDE.md 2026-08-06: *"pre-existing MECHANICAL enforcement STANDS"*).

---

## 0. Verdict on MSTR~Z's framing

**Upheld:** the core finding — §6 presents ten items under one heading with one disposition, asserting
one state; they are not in one state, and the obvious remedy (Phase 0 probes + censuses) closes some and
structurally cannot close others. That is a real Rule 24(iv) stability defect. Upheld also: H4 must be
pre-positioned now, and H6/H7/H9 must leave the checklist because **a checklist item gets ticked once and
a constraint must not be.**

**Overturned or sharpened, four ways:**

| # | MSTR~Z | CTO~Z verdict |
|---|---|---|
| 1 | Class A = {H1, H2, H3-source, H5, H8} moves together under Phase 0 | **SPLIT.** H1/H2 measure a **vendor we do not control** and produce a *sample*, not a durable fact. H5 measures our own package and stays true. One remedy does **not** move them together — the same defect one level down. |
| 2 | H10 + H3-external are "structurally uncloseable" | **OVERTURNED.** H10 has real measurement work in front of it and **does terminate** — as a *recorded limitation*, never as a proof. "Uncloseable" invites an executor to skip the work. *(The label was restated in the ~2030Z relay; the overturn stands. MSTR~Z's own framing body already says the honest close **is** a recorded limitation — the body describes a close while the label denies one. That gap is the defect: an executor who believes nothing can be done does not check whether CloudTrail data events are enabled.)* |
| 3 | Split H3; put its external half in Class C | **RESOLVED DIFFERENTLY.** The insight is right (two states on one row) but H3-external is an **instance of H10**, not a distinct item. Duplicating one blind spot across two rows with two dispositions is a MECE break (postulate (i)) one axis up. H3 becomes wholly measurable; **H10 is the single declaration site** and enumerates every deletion candidate. |
| 4 | Ten items | **FOURTEEN.** Four unnamed items found: **H11** (a live collision on the critical path), **H12**, **H13**, **H14** (the gold tree's calendar cannot compute a frontier, and its fallback expires inside this project's horizon). |

---

## 1. The axis

**State axis: what act actually closes this item, and what may a closure claim assert?**

Naming the second half is the load-bearing part. Every §6 row currently permits the same closure
sentence ("resolved"), and for five of them that sentence would be false.

---

## 2. Classification

### Class A — CLOSES BY MEASUREMENT WE CONTROL · result is durable

| Hole | Closing act | A closure may assert |
|---|---|---|
| **H3** | Static import + S3 read/write graph over the real package closure; sweep repo, source-map, Terraform, SSM, portal, deployed Lambda env. | "No **source-visible** reader." Never "no reader" — that clause belongs to H10. |
| **H5** | Build the package; benchmark memory/duration on the built Linux artifact. | The measured envelope. Repeatable for that code+package. |
| **H8** | Reconstruct deployed publisher provenance from artifact/hash/commit history; correct the source map in the cutover commit. | The tie, **if the hash ties**. See C2. |

These three genuinely move together and stay true. This is the class the plan is built for.

### Class A′ — CLOSES BY MEASUREMENT WE DO **NOT** CONTROL · result is a sample, provisional

| Hole | Closing act | A closure may assert |
|---|---|---|
| **H1** | Probe Eclipse + the MDPF-required Assets endpoints at the proposed early hour, across every row the all-row INF mirror carries. | "Valid early **on the days probed**." |
| **H2** | Execute + accept the early SmartX probe (≈07:45/08:00/08:15 ET). Also: search the record for the 08-05 run Clock v3 pre-registered — **and print the denominator** (§6 states "not found" with none). | Same. |

**Why this is its own class and not a nicety.** `01_VERIFIED_FINDINGS.md` §7 already measures the vendor
as **variable**: Eclipse normally arrives overnight but **two measured exceptions landed at 10:16 ET
(July 16 and August 6)**. A probe that passes tomorrow does not make the vendor punctual; it samples it.
Run the probes — then build a design that **does not depend on the sample generalizing**. Clock v3 already
mandates exactly that (labeled carry, never a held publish); see H12.

### Class B — CLOSES ONLY ON SOVEREIGN WORD · attaches to an irreversible physical act

| Hole | Status |
|---|---|
| ~~**H4** — EC2 termination / EBS deletion~~ | **✅ RESOLVED 2026-08-06 ~2030Z. Leaves Class B.** Its *condition* re-lands on Class A — §2A′′. |
| **H13** (new) — deleting S3 objects | **OPEN. Already CLAUDE.md standing law.** See §3 G3. |

> **⚠ CLASS B IS NOT EMPTY — I disagree with the relay on this one point.** MSTR~Z's H4 message says
> *"Class B is empty; reclassify."* That is true of the ten holes as originally listed, and false of the
> corrected set: **H13 remains.** MSTR~Z's own message independently confirms it in the same breath —
> *"It is NOT authorization to delete S3 data"* — which is exactly H13's content, reached from the other
> direction. The empty-Class-B reading is the hazard: it would retire the class one message before the
> S3 deletions in H3/H10 arrive at the same standing law.

**H4 — the authority question, and how it closed.** I read all three prior records in full rather than
inferring, because *"only Andrew's word closes it"* is falsifiable by his word already existing. At the
time of that read it did not:

- `ANDREW_DIRECT_20260805T2235Z_MDPF_GOLD_LAMBDA_CONSOLIDATION.md:39` — VERBATIM record: *"It does **not**
  by itself authorize any teardown or decommission."* Explicit.
- `ANDREW_DIRECT_20260806_1256Z_...md:5-11` — *"come up with a plan to streamline and consolidate this on
  schedule once and for all."* Publishing path. No teardown language.
- `ANDREW_DIRECT_20260806_MDPF_ROUTING_TRANSCRIPT_0140.md:16-17` — *"cleaning up dead and old routes."*
  **Routes, not hardware.**

So H4's premise held and was source-confirmed, not inferred — the pack was right that no existing record
authorized teardown. **It is now authorized**, Andrew-direct at the site-Z MSTR terminal, 2026-08-06,
VERBATIM:

> *"Teardown is fine just need to make sure any necessary code on that ec2 is properly ported to the lambda."*

This is the only kind of act that could close a Class-B item, and it closes it. Physical termination of
`i-02448edb624a7a7cf` and its EBS is authorized; the record satisfies §6's own requirement for *"a clear
governing record"* before irreversible physical deletion. **Note the by-product:** the pre-authorization
question for *stopping* the instance (CLAUDE.md Agent Autonomy lists `stopping EC2` beside `deleting S3
objects`) is subsumed — teardown authorization necessarily covers the lesser act.

### Class A′′ — H4's CONDITION: closes by measurement, but ⧗ **ORDERING-CRITICAL**

The authorization is **conditional**, and the condition is not a formality. It is discharged by exactly
the work H3 (census) and H5 (package closure) already ask for — which **re-ranks H3 to the front of the
program**: it is no longer only a deletion-safety question, it is now the discharge instrument for a
sovereign condition on an irreversible act.

> **⧗ THE PROPERTY NO OTHER ITEM ON THIS LIST HAS: the act H4 authorizes DESTROYS THE EVIDENCE THAT
> DISCHARGES ITS OWN CONDITION.** Terminate first and "was all necessary code ported?" becomes
> permanently unanswerable — not merely unanswered.

The hazard is measured, not hypothetical, and it lands on **H5** as much as H4:

- `02` names the miss directly — *"any EC2 script not directly visible in Stage 6 but used as a library
  or imported source."* The dispatch script enumerates ten stages; imports are not enumerated anywhere.
- `02` also records that **the EC2 runtime-installs packages.** The authoritative record of *which
  versions actually ran* therefore exists **only on that instance's disk** — which is precisely H5's
  dependency closure. Terminating destroys the reproducibility baseline for a Class-A hole.
- `01` §10 + H8 establish repo↔deployed divergence as this estate's demonstrated norm, so "the repo is
  the same as the box" is exactly the assumption that has already failed elsewhere here.

**Discharge (MSTR~Z specified it; I sharpen it in four places, marked ▸):**

1. **CAPTURE BEFORE TERMINATE.** Full on-disk MDPF code + installed dependency inventory (`pip freeze`
   and the resolved interpreter/site-packages state) preserved before any irreversible step.
   ▸ **Take an EBS snapshot as well, and take it first.** An enumerated capture can miss a file — that
   *is* the stated hazard. A snapshot does not enumerate, so it cannot miss. The inventory is what you
   *reason* from; the snapshot is what makes an enumeration error **recoverable instead of terminal**.
   It costs pennies and is fully inside the granted authorization.
   ▸ The capture lands in **S3**, per Rule 12 (S3 is the artifact store for all EC2 code) — never left
   on the instance, which is the thing being deleted.
2. **DIFF captured-vs-repo into exactly three buckets**, no fourth: byte-identical to committed source /
   ported and hash-tied in `BUILD_MANIFEST.json` / demonstrated unnecessary with evidence.
   ▸ Make "no fourth bucket" *checkable* rather than aspirational: **assert `|bucket1 ∪ bucket2 ∪
   bucket3| == denominator`.** The forbidden fourth bucket is really "files nobody found," and only the
   arithmetic detects it.
3. **Close the provisional set by STATIC GRAPH, not by name.**
   ▸ **Build the graph over the CAPTURED closure, not the repo closure.** The whole premise is that the
   box diverges from the repo; a graph built from repo source inherits the very divergence it is meant
   to detect.
4. **STATE THE DENOMINATOR** of files found on the box — a port-completeness claim without one is not a
   claim. ▸ The denominator comes from the **filesystem**, not from the dispatch script's stage list:
   every `.py` under the MDPF tree plus the installed-package manifest. Ten stages is the number that
   hides the hazard.

**Still NOT a gate.** This is a correctness condition the sovereign attached to his own authorization.
**Nobody clears it; the team discharges it with evidence.** If an approval checkpoint is proposed around
it, refuse — that would be a no-gates violation on the very instruction that removed a blocker.

**Scope, not widened:** this says nothing about H10, and it is **not** authorization to delete S3 data.
Phase 6 is explicit that data is never deleted as part of route retirement, and S3 versioning is
load-bearing for rollback. H13 stands open.

### Class C — CLOSES AS A BOUNDED NEGATIVE · terminates in a recorded limitation, never a proof

| # | Item | Closing act | A closure may assert |
|---|---|---|---|
| **C1** | **H10** — external/manual consumers | (a) determine whether CloudTrail **data events** are enabled for these buckets; (b) if yes, read them; (c) search operational runbooks; (d) if not, record the limitation **naming the telemetry actually checked**. | "No reader visible to *these named instruments*." **Never** "proved no external reader." |
| **C2** | **H8-fallback** (new) | If the deployed artifact hash ties to **no** commit, provenance is unreconstructible. | "Deployed provenance unreconstructible; rebuilt from repo tip at `<commit>`." |

**On C1 — why "structurally uncloseable" was the wrong label.** H10 contains real, executable work:
checking whether data-event telemetry exists is itself a measurement, and it may come back *yes*, in which
case a genuine read follows. Labelling the item uncloseable licenses skipping straight to the caveat.
It terminates; what it cannot do is terminate in the state *proved absent*.
**The failure mode to guard is silent upgrade** — a zero-reader *source* census reported at Phase 6 as
"proved zero readers." `02_NEEDED_VS_NOT_AUDIT.md` already states the correct floor: *"A zero-reader
result is a floor against source-visible readers."*

**On C2 — why this is new.** H8 reads as clean Class A, and it is not guaranteed to be.
`01_VERIFIED_FINDINGS.md` §10 already establishes the recorded provenance is **known-wrong** (source map
describes the old build-alongside function and old role while the live Lambda runs the egress role).
Reconstruction is an *attempt*. If it fails, the honest close is a limitation — and nobody named that
branch, so it would be improvised under deploy pressure.

### Class D — STANDING CONSTRAINTS, NOT HOLES · never close; re-fire at every phase boundary

Lift these **out of the open-holes checklist** into a STANDING CONSTRAINTS register carried in the deploy
ledger and re-asserted at each phase boundary.

| # | Constraint | Addition |
|---|---|---|
| **H6** | Preserve served schema (`as_of_first`/`as_of_last`, `firm_id`, `scope=null`). Do not "clean up" in an infrastructure cutover. | **⚠ Has an unnamed one-time prerequisite — see §3.** |
| **H7** | Re-pin live state at **every** phase boundary, not once at execution start. | **⚠ Has an unnamed device-specific mechanism — see §3.** |
| **H9** | Code retention is legal; active-path retention is a no-shadow violation. Distinguish them in the ledger. | Contains no unknown at all — the strongest D member. It is a definition, and never belonged in "open holes." |
| **H11** | *(new)* Orion pulls cannot precede the 12:15Z JWT mint. | **§3.** |
| **H12** | *(new)* Probe-fail is a pre-registered branch, not an absence of a plan. | **§3.** |

---

## 3. Gaps filled — the "filling in any gaps" half

### G1 · H11 (NEW HOLE) — the early-pull proposal collides with the UTC-fixed Orion JWT floor

**This is on the critical path and no document in the pack names it.**

Clock v3 **Amendment 1** (`MDPF_GLOBAL_T2C/CLOCK_V3_DELTA_20260804.md:39-52`) exists because the MDPF
chain's stage-0 read an expired `orion/jwt/current` **12 seconds** before the fresh one landed → **401 ×
9 models**. The fix pinned the JWT renewal **UTC-fixed at 12:15Z, both regimes**, deliberately off the
12:00/12:30 Orion hazard marks, retiring the daily expired-token window "now ends ~12:16Z."

The early-pull proposal moves Orion + the INF ingest-mirror earlier. The arithmetic nobody ran:

| | EDT | EST |
|---|---|---|
| Orion JWT mint (UTC-fixed 12:15Z) | **08:15 ET** | 07:15 ET |
| Phase 0 required result (silver present) | 08:40 ET | 08:40 ET |
| **Usable Orion pull window** | **08:15 – 08:40 ET → 25 minutes** | 07:15 – 08:40 ET → 85 min |

**EDT is the binding regime and the window is 25 minutes.** Any Orion pull moved earlier than 08:15 ET in
EDT reads an expired token and **re-opens the exact race Amendment 1 closed.** Phase 0 says "in both DST
regimes" — correctly — but does not carry the JWT member into the arithmetic.

**Consequence if unfixed:** the H1 probe could "PASS" at an hour production can never use, and the pass
would be recorded as closing H1. The JWT mint is a hard floor on the H1 probe design, not a detail for
implementation. *(Note: `02` correctly declines to PORT the Orion bronze pull into the Lambda — but the
clock move lands in the upstream modules, which Phase 5 step 7 applies **first**.)*

#### G1-A · CORRECTED ~2050Z — the figure was wrong by ten minutes, and the correction opened a bigger finding

**⚠ MY ERROR, and it is the class this document catalogues.** I sourced **12:15Z from Clock v3
Amendment 1 — a RULING DOCUMENT — for a claim about a LIVE CRON EXPRESSION.** Rule 22a: a STATE claim
needs the live primitive; neither a record nor a comp-tool distinguishes declared from applied. Caught by
`0.0.0_AB_MSTR~Z` on the live plane. The direction was conservative (I reported a *tighter* floor than
exists, so a probe built to my number still satisfies reality) — **but conservative is not correct, and it
was travelling to Andrew as a number.**

**Measured, `comp-trigger` denominator 139 events-rules + 16 schedules:**

| Rule | Expression | Anchor | Target |
|---|---|---|---|
| `opal-inf-jwt-fetch` | `cron(5 12 * * ? *)` = **12:05Z** | **UTC-fixed** (classic rule — no timezone field) | `inf-jwt-trigger` |
| `opal-inf-export-schedule` | `cron(0 21 * * ? *)` | UTC | `inf-jwt-trigger` (Clock v3's second daily mint) |
| `smartx-jwt-refresher-daily` | `cron(0 9 * * ? *)` | **America/New_York — DST-aware** | `smartx-jwt-refresher` |

Both INF rules target the **same** lambda — one resource, two schedules, exactly as Clock v3 describes.
**Corrected floor: 12:05Z = 08:05 ET EDT. Usable window 08:05–08:40 = 35 minutes, not 25.**

> **⚡ THE CORRECTION OPENED THE REAL FINDING: THE TWO VENDORS' JWT FLOORS ARE ANCHORED IN OPPOSITE TIME
> BASES, SO "SHIFT THE ASSOCIATED CHAINS EARLIER" IS CORRECT FOR ONE AND WRONG FOR THE OTHER.**
> - **SmartX — ET-anchored.** Its floor moves with the wall clock, so doc 03's *"set JWT 07:45 ET and pull
>   08:00 ET"* is already right and is **DST-safe by construction**. No new problem.
> - **Orion — UTC-fixed, deliberately.** Clock v3 Amendment 1 pinned 12:05Z specifically to stay off the
>   12:00/12:30 Orion hazard marks **year-round** (an ET-anchored 08:30 lands *on* 12:30Z in EDT).
>   **Moving it earlier to make room for an early pull re-opens the exact race that amendment closed.
>   The Orion pull adapts to the floor; the floor does not adapt to the pull.**
>
> Doc 03 Phase 4 already carries the governing rule — *"DST-aware Scheduler where the contract is an ET
> wall-clock; preserve any deliberately UTC-fixed authentication hazard-avoidance clock only where its
> recorded rationale still applies."* **What it does not do is say which resources fall on which side.**
> Now measured: SmartX = ET side; Orion = UTC side, rationale still applying.

**DST behaviour (with the mechanism, not just the caution):** Orion's floor is 08:05 ET in EDT and
**07:05 ET in EST** — 35 minutes of window in summer, 95 in winter. **Tightest right now**, so an August
validation is a worst-case validation, which is the safe direction — *but anyone re-confirming this in
January reads 95 minutes and books slack that evaporates in March.* SmartX carries no equivalent exposure.

**RECORD DRIFT (a finding in its own right): Clock v3 Amendment 1 records the Orion JWT at 12:15Z; the
live plane runs 12:05Z.** Ten minutes, on the one clock member that amendment exists to pin — so the
governing clock document is wrong about the thing it governs. Every agent reasoning about this clock move
is reading Clock v3, including me an hour ago.

*Method note, MSTR~Z's, worth keeping: their first pass used `aws events list-rules` and read **100** —
the **page size**, not the total. Token-walked it is **139**, matching the `comp-trigger` denominator
above. CLAUDE.md documents that exact `list-*` trap; printing the denominator is the only reason a
truncated retrieval did not become a confident "H11 is unfounded."*

### G2 · H12 (NEW HOLE) — the probe-fail branch is missing from the pack but already ruled in Clock v3

`03_IMPLEMENTATION_PLAN.md` Phase 0 step 4 enumerates **two** branches — *"If all rows … are valid early"*
and *"If unrelated rows cannot move"* — **both of which presuppose the data IS available early.** There is
no branch for *the vendor cannot deliver earlier at all*, which is the outcome H1/H2 exist to test for.

**The branch is not missing from the estate — the pack dropped it.** Clock v3's vendor-pull row rules it:
shifts land **on probe PASS**; the deadline binds the **publish**, and *"vendor lateness surfaces as
labeled carry per the ruled honesty (2 TD window, every carried point labeled, transition visible) —
**never as a held publish**."*

**Restore it explicitly**, for two reasons:
1. An executor whose probe fails reads the plan as having no path, and either stalls or invents one.
2. It surfaces a **product** consequence Andrew would want stated: on probe-fail, MDPF carries
   **routinely** rather than exceptionally. That is a fact about the product, not a deployment detail —
   MSTR~Z should carry it.

### G3 · H13 (NEW HOLE, Class B2) — S3 deletion is already on the human-confirmation list

§6 flags H4's EC2 teardown as an authority question and is silent that the **deletions** in H3/H10
(`wsb-*`, `wsd-*`, `opal-data-mdpf/mdpf/feeds/*`, the OWNTS outputs) sit on the *same standing list*:

> CLAUDE.md § Agent Autonomy — *"Human confirmation required ONLY for: recursive deletion, destructive git
> …, dropping tables / **deleting S3 objects**, **stopping EC2**, anything unrecoverable."*

**This is pre-existing law, not a new gate.** It is named here so it is not discovered *at* the delete
step. It also composes with C1: the deletion is authorized by Andrew against a census that is honestly
labelled a **floor**, not a proof — which is precisely the information he needs to give that word.

### G4 · H6 has an unnamed one-time prerequisite: capture the baseline schemas

`04` §1 and §3 require that *"Platinum preserves each artifact's existing schema contract … the cutover
does not silently rename fields."* **That check has no input.** §4's rollback capture list records
*"S3 source/destination VersionIds and current manifests for the 14 served pairs"* — **VersionIds and
manifests, not schemas.**

A constraint whose verification input is never captured is unverifiable. **Add to the §4 pre-cutover
capture: the observed field set + types of all 14 served pairs and `_aggregate_aua`**, recorded before any
cutover. This is a one-time Class-A act that makes a Class-D constraint checkable.

### G5 · H7 has an unnamed device-specific mechanism — and the naive read fails silently

H7 says *"re-run all live pins and relevant diffs at execution start."* **On this device that instruction
cannot be followed as written.** Site Z runs a shared worktree with one checkout, seat pulls are denied,
and push belongs to the integrator (`0.0.0_AB_MSTR~Z`, `:55`–`:00`). A seat's working tree therefore runs
**up to ~55 minutes stale**, and a "re-pin" read from it returns a confidently wrong answer with no error.

**Mechanism:** read the ref, not the tree — `MSYS_NO_PATHCONV=1 git show origin/CLOUD:<path>`.
**And never `2>/dev/null` it:** a mangled slashed ref prints `fatal:` on stderr and returns **clean empty
stdout**, manufacturing "file absent" out of a broken retrieval. Run a positive control (a line you know
is in the file) beside any ABSENT verdict. *(CLAUDE.md § Git.)*

### G7 · H14 (NEW HOLE) — the MDPF gold tree's calendar module **structurally cannot compute a frontier**, and its fallback expires 2026-12-31

Raised by `2.0.0_SA_COO~Z` off DS~Z's source pass as a possible second calendar implementation, with the
disposition routed to me as architectural. **Measured; it is real, and it is worse than a packaging
detail.** `data/mdpf/scripts/gold/_trading_day_calendar.py` is **self-declared non-canonical** — line 3,
verbatim: *"INTERIM DIVERGENT COPY -- NOT canonical."*

> ⚠ **Correction, recorded because the wrong version is the seductive one.** The file appears in a
> `comp-grep` census of *canonical-import* sites, which reads as "the shim imports lib — no divergence."
> **It does not.** The grep matched the shim's **docstring**, which names `lib/trading_calendar.py` in
> prose. Positive control run: its only imports are `datetime` and `pandas_market_calendars`.
> Text-local and connection-blind, exactly as Rule 21 says — and the false read was the reassuring one.

**Finding 1 — the frontier functions are absent, and they are the ones the law names.**
Measured function surfaces:

| | `lib/trading_calendar.py` (canonical) | `data/mdpf/.../_trading_day_calendar.py` |
|---|---|---|
| `expected_last_trading_day` | ✅ `:101` | ❌ **absent** |
| `trading_days_behind` | ✅ `:108` | ❌ **absent** |
| `prev_trading_day` | ✅ `:93` | ❌ **absent** |
| `is_trading_day` / `trading_days_*` | ✅ | ✅ |

CLAUDE.md NEVER-rule 1 names **`expected_last_trading_day` / `trading_days_behind`** as *the* one frontier
definition. **The calendar module living in the MDPF gold tree cannot compute a frontier at all.**

Now hold that against `04` §2: the acceptance basis of this entire project is **per-feed trading-day
frontiers across six different cadences** (same-day, T-1, T-1, same-day-with-prior-settled, same-day,
D+2). So the open question is not "which calendar" — it is: **what computes those six frontiers today?**
It is not this module, and per the shim's own docstring `lib/` *"is not on the gold-runner import path."*
That is a Class-A measurement and it belongs in Phase 0, because the acceptance battery cannot be
written until it is answered.

**Finding 2 — a silent expiry inside the project's own execution horizon.** The shim's PMC import is
`try/except ImportError` with a **hardcoded holiday fallback**, and its coverage ends **2026-12-31**
(measured: last holiday year `2026`; canonical carries `2027`). Today is 2026-08-06 — **under five months
of runway.** The failure is silent by construction: with no 2027 entries, **every 2027 market holiday
evaluates as a trading day**, no error, no log line, wrong frontier.

**This lands directly on H5 and on the cutover.** `02` records that the EC2 **runtime-installs packages**
and that *"Lambda must not inherit"* that pattern. So if `pandas_market_calendars` is a runtime-install
that does not make it into the Lambda layer, **the new `mdpf-gold-lambda` silently falls back to the
expiring list** — a dependency-closure gap (H5) with a date attached.

**Disposition (architectural, mine):** the consolidation binds **one canonical calendar** into the
Lambda package and **retires the shim** — the shim's own docstring says it exists *only* because `lib/` is
off the gold-runner import path, and building the Lambda dissolves that reason. This is a
packaging/architecture act inside work already scoped (H5 + Phase 1), **not** new scope, and **not** a
monitor: per Andrew's canonical-routes-before-monitoring ordering, the correct move is to make the route
right, not to detect it being wrong. **Assert PMC presence at import time in the Lambda** so the fallback
cannot engage unnoticed. **Nothing here is a gate.**

**Bounded:** verified by me — the absent frontier functions, the 2026 horizon, the silent-fallback
construction, the self-declared divergent status. **Not** verified by me — the docstring's claim that the
current-window holiday sets are byte-identical to `lib`, and whether PMC is in fact installed on the EC2.
*(Prior art: `0.7.0_AE_CloudOps` logged this file as a divergent third copy on 2026-07-24 — it is a known,
unretired condition, not a new discovery.)*

#### G7-A · AMENDMENT ~2040Z — DS~Z/COO~Z measured further; my open question is ANSWERED and one framing of mine was imprecise

`0.4.0_DS_ClientPlatform~Z` measured at `73ca92eb3`, routed by `2.0.0_SA_COO~Z`:

1. **There are THREE copies, not two.** The third is **inlined privates** —
   `dim_mdpf_aggregate_aua_timeseries.py:154,164` define `_expected_last_trading_day` /
   `_trading_days_behind`, docstring: *"Inlined from lib/trading_calendar … the shim lacks the frontier fns."*
   **⚠ This closes my own Phase-0 question and corrects its framing.** I asked "what computes the six
   frontiers today?" — the answer is: **a third copy the law does not know about.** The frontier is not
   uncomputed; it is computed off-canon. Phase 0 must not re-spend on this; it is now a *retirement*
   item, not a *discovery* item.
2. **PMC is absent from `requirements.txt`** (declares numpy/pandas/pyarrow/PyYAML==6.0.2), **zero
   repo-wide hits** for the pip name. It is installed **only** by bash preflight —
   `mdpf-daily-dispatch.sh:183-189` and `user-data.sh:49`, `pip install "pandas_market_calendars<5"`,
   the `<5` pin load-bearing (`dispatch.sh:175`: 5.x changed the API). **This converts the second half
   of H14 from my inference to measured fact**, and it is the cleanest instance in the program of
   *"part of its runtime exists in no commit"* — guaranteed today by the exact file the port deletes.
3. **Doc 02's prescribed remedy is FAIL-GREEN.** *"Run an import-health invocation from the built Linux
   artifact"* **passes with the package missing**, because the import sits in `try/except ImportError`.
   Not a weak control — an **anti-control**: it reports healthy *because* the fallback engaged.
   Discriminating oracle (already wired): `calendar_source()` → `"NYSE/pandas_market_calendars"` vs
   `"NYSE/hardcoded-fallback-2024-2026"`, already emitted into the artifact's `trading_day_calendar` field.

#### G7-B · RULING (CTO~Z, architecture) — bind `lib/trading_calendar` via the WS-1 layer

**Retire the shim and both inlined privates; bind the port to `lib/trading_calendar.py` through the WS-1
shared Lambda Layer.**

**Not scope creep, and this is the load-bearing reason: the port cannot avoid the decision.** The Lambda
must import something; there is no null option. This is not work the cutover absorbs — it is a choice the
cutover *forces*, and the only question is whether it is made explicitly or by default. The justification
for all three copies is one sentence (shim `:8-9`, spine `:55-57`): *"lib/ is not on the gold-runner
import path."* **A Lambda has no gold-runner import path** — the port does not weaken that premise, it
deletes it. Supports: NEVER#1 names `lib/trading_calendar` as the ONE frontier definition; the shim's own
docstring instructs keeping its surface identical *"so the eventual switch is a drop-in"* and marks itself
for retirement; Andrew 08-06 0140 — *"the exact same pattern … the exact same design; this is what it
means to be canonical."*

**Four conditions.** (i) **Tie-out EXERCISED with a mutant** — assert set equality across the full
in-window range with the **denominator printed**, then mutate one date and prove the comparison fails
(`02`: *"a tie without a positive falsifier is not proof"*). (ii) **The `<5` pin ports hash-tied WITH its
rationale** into `BUILD_MANIFEST.json` — Andrew's H4 bucket is *ported*, never *demonstrated unnecessary*.
(iii) **`calendar_source()` assertion REPLACES doc 02's import-health check** at build time and in
acceptance — it is an assertion inside existing scope, **not** an alarm/monitor/notification (the
moratorium binds; route first). (iv) **SCOPE BOUND — do not widen.** Vendored copies under
`bd-served-vintage-alarm`, `inf-etf-ownership-daily`, `opal-assets-absence-check` are **other pipelines**
and this ruling does not touch them; that is WS-1's scope. *A ruling that dissolves a workaround is not a
licence to sweep the estate.*

**No gate.** An architectural binding, not an approval step — the TO names the binding, the tie-out
evidence discharges it.

#### G7-C · Condition 1 DISCHARGED + VALIDATED ~2045Z — the 2027 divergence is now MEASURED

`0.4.0_DS_ClientPlatform~Z` exercised the tie-out; I re-derived the arithmetic before accepting it
(RAVC step 4). **Condition 1 closed.**

| Test | Denominator | Result |
|---|---|---|
| In-window equality 2024-01-01..2026-12-31 | **1096 dates** | **0 disagreements.** In-window sets 31/31, symmetric difference empty; both drop 2025-01-09 (Carter) and 2026-07-03. |
| Positive falsifier | same 1096 | Removed 2026-07-03 from the shim → **1 disagreement, localized to the mutated date.** The tie is a result, not a tautology. |
| 2027 | **365 dates** | **10 disagreements — every 2027 NYSE holiday, shim=trading-day / lib=holiday.** |

Independently re-derived: 366+365+365 = 1096 ✓; 10+11+10 = 31 in-window ✓; totals 41−31 = 10 = the 2027
list ✓; all ten 2027 observance dates check against the rules (Juneteenth Sat→Fri 06-18, Jul 4 Sun→Mon
07-05, Christmas Sat→Fri 12-24, Good Friday 03-26 vs Easter 03-28) ✓.

**⚠ RECORD UPGRADED: the 2027 exposure in G7 above was source-derived. It is now MEASURED**, ten
enumerated dates.

**DS~Z's control, and why it is now a permanent requirement.** They forced `_USE_PMC=False` on both
modules before comparing — because with pmc importable **both defer to pmc and agree trivially**, testing
pmc rather than the fallback sets the ruling turns on. *The naive version of this test passes for the
wrong reason on any machine where pmc is installed.* **RULED: the fallback-vs-fallback comparison stays a
pinned test with `_USE_PMC=False` forced.** Once Condition 2 puts pmc in the layer, the naive test passes
everywhere and the 2027 divergence goes invisible again — on a horizon that has not moved. *A passing
assertion never made to fail has not been tested.*

#### G7-D · RULING — the QA-build backend asymmetry (H15)

**Measured incidental:** `pandas_market_calendars` is **not importable on site Z** — the fallback was
already live on a clean import (`lib` → `NYSE/hardcoded-fallback-2024-2027`, shim →
`...-2024-2026`). Consequence for `03` Phase 5 step 2: a QA build run from site Z **does not use the
incumbent's calendar backend.** In-window the numbers still tie (Test 1), so only the
`trading_day_calendar` provenance string differs.

> **⚠ AND THAT IS THE TRAP: doc 02 instructs the operator to compare "after stripping only explicitly
> volatile process/provenance fields." `trading_day_calendar` IS a provenance field by name and shape —
> so the rule points directly at discarding the ONE signal that discriminates the two runtimes.
> The collision is STRUCTURAL, not accidental**, and an executor following doc 02 exactly deletes the
> oracle and reports a clean tie. Third instance of one shape today, after the fail-green import check
> and the trivially-passing equality test.

**Ruled, all four:** (1) **install `pandas_market_calendars<5` in any environment producing a
QA-comparison artifact** — production will carry it via the Condition-2 layer, so a fallback QA build
validates a configuration that will never ship. (2) **`trading_day_calendar` goes on an EXPLICIT
never-strip list in the comparison spec** — named in the spec, not remembered by the operator; *care will
not survive doc 02's own instruction, an explicit list will.* **No rename — H6 binds.** (3) the
**build-time `calendar_source()` assertion stands independent of the artifact diff**, so no stripping
decision can silently disarm it. (4) DS~Z's forced-fallback test is **pinned**, per G7-C.

Nothing here is a gate — assertions and spec content inside existing scope.

#### G7-E · RULING ~2055Z — the calendar binding COVERS the Cottonwood producer family; and the port closure is 53% larger than the pack's

Raised by `2.0.0_SA_COO~Z` off DS~Z's closure: Condition 4's scope bound had an **unstated member**.

**RULED: in scope** — `build_cottonwood_mdpf_slice.py`, `build_cottonwood_mdpf_pair.py`, and any sibling
importing the mdpf gold tree. Condition 4 excludes `bd-served-vintage-alarm` /
`inf-etf-ownership-daily` / `opal-assets-absence-check` because they are **other pipelines**; the
Cottonwood producers are **this pipeline's own L2 leg** (`build_mdpf_spine.py:103` emits the slice's bytes
verbatim). Different side of the line.

**⚠ CORRECTION to the relayed mechanism — it breaks LOUD, not silent.** `:87-93` reads as a swallowing
try/except but is not: the `except ImportError` branch **re-imports the same module after a `sys.path`
hop**, so a genuinely-absent module **raises on the second import**. It is a *path-resolution* fallback,
not a dependency fallback. Retiring the shim breaks this consumer with a loud `ImportError` an
import-health check will catch. *The TO must budget for a build-time import failure, not a silent
wrong-answer hunt.* **The silent hazard is one layer down and already ruled:** the shim's own PMC
try/except *is* fail-green and the slice inherits it through the shim (G7-D). Useful: the slice already
imports `calendar_source` at `:88` — whether it is **emitted** into the artifact is **unmeasured by me**
and is TO work.

**A THIRD frontier derivation, which the binding improves rather than relocates.** `:793-794` computes
`tdb = len([d for d in trading_days_between(last_measured, today) if d > last_measured])` — **not** a
fourth copy of `trading_days_behind` (grep: only `:801`, the field name), but an ad-hoc derivation
anchored on **wall-clock `dt.date.today()`**. **In fairness it is NOT a NEVER#1 violation as written**:
it is explicitly labelled a non-verdict, carries its declared cadence inline (*"tdb <= 3 is WITHIN
DECLARED CADENCE, not staleness"*), and respects the monitor moratorium in its own comment. It anchors on
`today` **because the shim lacks `expected_last_trading_day` and there was nothing else to anchor on.**
`lib` has it — so the binding makes this canonical, a correctness improvement falling out of the port.
Record it in the TO as an **expected delta**, so it is not later mistaken for scope creep.

**Private-symbol coupling — RULED: absorb.** `build_cottonwood_mdpf_pair.py:64` imports
`_distribution_stats` from `dim_mdpf_account_distribution` — a **private** symbol, across trees, via
`sys.path` hop (plus `calc_metric`/`quarter_ends` at `:65`). This is exactly the structure "one
firm-parameterized path" dissolves; the symbols become internal to the one Lambda.
> **⧗ ATOMICITY CONSTRAINT: P1-1 and the Cottonwood producers move TOGETHER, not sequentially.** Until
> absorption lands, refactoring `dim_mdpf_account_distribution` **breaks Cottonwood with no signal in the
> mdpf tree** — a leading underscore *declares* that nothing outside depends on it, so nothing there will
> warn a refactorer that something does. Naming it in `cross_domain_coordination` is necessary and **not
> sufficient**; the sequencing is the control.

**Closure sizing — this is the most consequential item.** COO~Z/DS~Z measured the real import closure at
**14 modules / 9,442 lines across 3 directories and 2 trees** (AST, 124 import edges, **0 unresolved**,
10 entrypoints) against the pack's implicit **7 / 6,158** — **53% larger**. Lands on **H5** (sized against
the wrong denominator) and, more importantly, on **Andrew's port-completeness condition**: *"any necessary
code properly ported"* is discharged against a closure, and the closure everyone was implicitly working
from was **missing a third of itself.** This is what the §2A′′ denominator condition exists for.

**Rule-13 boundary:** `data/assets/scripts/gold` is a **SHARED repo home** deploying under the
S3-membership guard (key-exists=update enforced, 404=loud skip, first-mints explicit) — the port crosses a
**deploy-story** boundary, not just a directory one. Name it in the TO. Separately, the silver-tier
`rebalancer_schemas` imported into gold is **not** a Rule 17 violation (Rule 17 governs what silver *does
to data*, not module imports) — it is a packaging fact: a silver module vendored into a gold Lambda, which
must appear in `BUILD_MANIFEST.json` hash-tied like everything else.

#### G1-B · RE-RULED ~2110Z — Constraint 2 belongs at RESOURCE-TYPE level, not vendor level

`2.0.0_SA_COO~Z`, off AE~Z's fully-paginated SmartX measurement: **the ET/UTC divide runs INSIDE the
SmartX chain.** Its pulls are Scheduler/ET; its own backstop sweep
(`opal-assets-silver-smartx-sweep-daily`, `cron(0 16 * * ? *)`) is a classic rule = UTC.
**So "SmartX moves, Orion does not" is a true generalization with a false member** — and it had one
because I generalized on the **wrong axis**.

**RE-RULED — the rule is mechanical, therefore checkable without a lookup table:**

| Resource type | Timezone field | Anchor |
|---|---|---|
| EventBridge **Scheduler** entry | carries `ScheduleExpressionTimezone` | **can be ET-anchored, DST-aware** |
| **Classic** EventBridge rule | **none exists** | **structurally UTC-only, always** |

**Measured 6/6** on everything this project has touched: Scheduler — `mdpf-scheduled-floor`,
`smartx-jwt-refresher-daily`, `smartx-rest-pull-daily`, `smartx-assets-daily-pull-daily`, all
`America/New_York`. Classic — `opal-inf-jwt-fetch`, `opal-assets-silver-smartx-sweep-daily`,
`smartx-account-distribution-daily`, no tz field. **Nobody need memorize which resource is which — the
TYPE tells you** — and it predicts the general case: *every classic rule carrying an ET wall-clock
contract has a one-hour seasonal drift by construction, not by oversight.*

**Consequence worth stating in those words:** the sweep at 12:00 ET EDT lands **two hours after the 10:00
ET deadline**, so **it is not a backstop for the publish at all** — a next-day repair wearing a backstop's
name.

#### G1-C · H2's REMEDY TARGETS THE WRONG SCHEDULES — a remedy that cannot work while reporting success

Measured on the primitive (COO~Z/AE~Z): `smartx-assets-daily-pull` carries the OnSuccess destination to
`opal-assets-silver-smartx`; **`smartx-rest-pull` has ZERO event-invoke-configs.** The binding silver comes
from the **09:30 assets pull**. Doc 03 Phase 0 item 4 prescribes moving the JWT and *"the pull"* — **and
neither named schedule produces it.** Executed literally: two schedules move, the 09:30 assets pull stays,
silver still lands ~09:40, **and the change reads as delivered.** Corroborated by a 30-day census (pull
09:30 → OnSuccess → silver 09:37–09:41, median 09:40, 24/24 days), so the **mechanism** is confirmed, not
just the timing.

> **⚡ FIFTH INSTANCE OF THE DAY'S SHAPE, AND WORSE IN KIND. The others produced a CHECK THAT COULD NOT
> FAIL; this produces a REMEDY THAT CANNOT WORK — and then passes the check that asks whether it was
> applied.**
>
> **DURABLE CONTROL, standing across every clock TO: ACCEPTANCE ASSERTS ON THE OUTCOME, NEVER ON THE
> INTERVENTION.** The criterion is *"canonical SmartX silver OBJECT exists by 08:40 ET"* — **not** *"the
> schedules were moved to 07:45/08:00."* "Did the schedules move?" is exactly the check that passes while
> the remedy fails; an outcome assertion is immune to targeting the wrong resource, because a wrong target
> simply does not produce the outcome. Same shape as the `calendar_source` ruling: **assert the thing, not
> the act that was supposed to cause the thing.**

**OnSuccess weakness — NAME IT, DO NOT FIX IT HERE.** SmartX is the only family in `opal-data-assets` with
**no S3 bronze notification** (all 8 configs are ObjectCreated on a bronze prefix; no `smartx/`). Every
other family converts on **data landing**; SmartX alone on **pull success** — so a pull that succeeds
without writing still fires a green converter, and **green is not evidence.** House anti-pattern, real
weaker guarantee — **and out of scope**: bronze ingestion is upstream of the gold Lambda with its own
route (`02`), so adding a notification is a new upstream route change. Record + route to the upstream
owner. **The compensating control is already free:** G1-C's criterion asserts the silver *object* exists
rather than that the converter ran green — strictly stronger than the guarantee in question.

**`smartx-account-distribution-daily` is IN SCOPE**, short argument: `cron(30 11 * * ? *)` classic =
07:30 ET EDT / 06:30 EST, **always before** the ET-anchored 09:00 JWT. So it either carries its own auth or
runs on a prior-day token — either way **it is a consumer of the JWT being moved, and any JWT move must
account for every consumer of that JWT.** If it runs on a prior-day token, moving the mint changes its
token age: a live behavioural change nobody has modelled.

#### G1-D · PROPOSED LAW CORRECTION (routed, NOT implemented) — CLAUDE.md:110's remedy names the flag that causes the failure

AE~Z measured (positive + negative controls): **`aws <svc> list-* --no-paginate` returns ONLY the first
page** — `lambda list-functions` = 196 across 4 pages, page 1 returns 50, a **74% shortfall**. It nearly
produced a **fabricated production-outage report** ("two enabled schedules fire at non-existent Lambdas";
all four exist).

**CLAUDE.md:110, verbatim:** *"A count you did not paginate is a page size wearing a total's clothing —
**use `--no-paginate` + explicit token walking**, or count the materialised list."*

> **THE LAW'S REMEDY CLAUSE NAMES THE FLAG THAT CAUSES THE FAILURE THE RULE EXISTS TO PREVENT.**
> `--no-paginate` *disables* auto-pagination; the "+ explicit token walking" is the entire load-bearing
> half, and an agent who reads the first clause and stops has implemented the bug. **MSTR~Z did exactly
> that today** — `aws events list-rules --no-paginate` → 100 against a true 139, on a number travelling to
> Andrew inside a live sovereign ask. They caught it by printing the denominator, **not because the rule
> protected them: the rule pointed them at the trap.**
>
> **Worse in kind than the `--query length()` trap on that same line:** that returns a wrong *number*;
> this returns a wrong *set* — and a filtered `--query` over a truncated page is **indistinguishable from
> a real absence.** Same clean-empty-result family the line already legislates. **And it is the rule whose
> own stated subject is "put the control on the RETRIEVAL": a retrieval-control rule shipped with a broken
> retrieval control.**

**Proposed shape** (CTO base owns the text): name `--no-paginate` as a **hazard**; state the remedy
positively as *omit the flag, let the CLI auto-paginate, count/filter the materialised set client-side*;
keep the `--query length()` clause (correct and independent); add the discriminator that a list result you
did not materialise **cannot distinguish "absent" from "on page 2."** **Routed to MSTR~Z, not
implemented** — law edits go through CTO base and rule-bank increments need the STRUCTURAL-TWOPHASE
prefix on this device. COO~Z lands it as a P0-3 criterion meanwhile so the project is covered regardless
of routing speed.

**My own exposure, stated:** my raw calls were per-resource `get-schedule --name` (no pagination surface)
and my censuses came from `comp-trigger`, which paginates correctly — **but I inferred that from its 139
agreeing with AE~Z's re-derivation afterwards. That is confirmation, not verification.**

#### G9 · ~2125Z — the roster resolver PREFERS the deployed copy over the committed authority, and it produced a measured near-miss on my own ruling

`2.0.0_SA_COO~Z` falsified their own recorded claim (asked AE~Z to verify rather than confirm) and the
correction is larger than the error. `mdpf-daily-dispatch.sh:125` syncs
`s3://opal-data-mdpf/code/scripts/` into `$SCRIPTS_DIR`, the roster lives inside that prefix, and
`dim_mdpf_aggregate_aua_timeseries.py:1718-1731` `_load_partner_roster()` — whose own docstring calls it
*"THE ONE SOURCE OF EXPECTED-NESS"* — resolves `os.path.join(here, "partner_roster.json")` **first**.
**Candidate 1 wins and it is the S3 copy; the committed repo authority is the dev/QA fallback, reached
only off-runner.**

> **Two consequences, into P2-1 in these words:**
> **(a) "THE REPO SAYS X" IS NEVER EVIDENCE ABOUT WHAT PRODUCTION USED.** Any agent reasoning from the
> repo about roster values — **including me on 2026-08-03** — is reasoning about the path production does
> not take.
> **(b) NOTHING DETECTS THE DIVERGENCE**, because a resolver that silently prefers candidate 1 emits no
> signal when the two disagree.

**The measured near-miss, and the half I own:** `:1203` reads
`gate_policy.per_partner_max_lag_trading_days` from that file — the exact key whose deployed copy went
**nine days stale** against **my own 2026-08-03 ruling**, undetected. Non-operative *only* because that
ruling changed narration rather than the value. **Had I ruled the lag 2 → 3, every production gold run
since 07-28 would have used 2, silently, while the repo showed 3 to anyone who checked.**

**FORWARD CONTROL (standing, not a Phase-2 task): any future ruling on a roster value is NOT LANDED until
the deployed object carries it.** Ruling in the repo does not change production.

**Status change, not a redesign.** Doc 03 Phase 2 is already correct on mechanism (Terraform-managed
objects with content hashes, no hand-maintained roster in the zip, both config hashes in every run
manifest). What this changes is its standing: **no longer an architectural preference — the remedy for a
measured near-miss on a live threshold**, and the run-manifest hash is exactly the detection absent for
nine days.

**⧗ SECOND ORDERING CONSTRAINT (accepted as hard):** the third roster copy dies with the **EC2/DISPATCH
route**, a *different event* from the accrual-bridge retirement. **`mdpf-gold-lambda` must have its roster
BEFORE the sync stops**, or the spine loses its expected-ness source mid-cutover. This composes with
§2A′′'s capture-before-terminate: **two independent orderings inside Phase 4/6 that a naive "retire the
EC2" step violates.**

#### G10 · ~2128Z — three tool findings, and they are not random

| Finding | Failure direction | Risk it creates |
|---|---|---|
| `comp-blast` false zero | under-reports **consumption** | **deleting something needed** |
| `comp-estate` phantom (`mdpf-freshness-checker` listed live + cron; `get-function` → ResourceNotFound) | over-reports **existence** | working on something that isn't there |
| `comp-which` gap ("inventory code + installed packages on an EC2") | no route at all | the act goes unassisted |

> **ALL THREE CLUSTER ON THE RETIREMENT HALF OF THE PROGRAM, NOT THE BUILD HALF.** The read is not "the
> tools are flaky" — it is that **the comp-tool estate is well covered for BUILDING and thinly covered for
> RETIRING**, which follows from how it grew. This is the first large retirement, so it hits the thin side
> systematically rather than by luck.

**Consequence to state in the ledger:** the missing instrument is *exactly* the one Andrew's
port-completeness condition needs — so **the EC2 inventory will be done by hand**, and a hand-built
denominator is precisely what §2A′′'s condition protects. **We do not build tooling inside this program**
(one-time act; absorbing tool-building is the widening we keep refusing). Routed to CTO base as an
estate-level observation. *Cross-check in our favour: `02` already records the freshness-checker function
as absent and scopes retirement to the residual role/policy — the pack is right and the census is wrong,
the reverse of the day's pattern.*

#### G11 · ~2128Z — `lambda-source-map.json`: the obvious fix would not have fixed it

Routed as "51 non-ASCII bytes, all U+00A7 section signs." The count is right; **the composition is not.**
Measured:

| Char | Count | What it is |
|---|---|---|
| `§` U+00A7 | 6 | intentional section signs |
| `—` U+2014 | 1 | em dash |
| **`\x9d` U+009D** | **2** | **C1 CONTROL CHARACTER** |
| `â` ×4 · `‚` ×2 · `€` ×2 · `¬` ×2 · `Ã` ×2 · `¢` ×2 | 14 | **double-encoding MOJIBAKE** (`â€š`/`â‚¬`/`Ã¢`) |

> **⚠ AND THE CRASH IS NOT WHERE THE DIAGNOSIS PUT IT.** The cp1252 failure is
> `can't decode byte 0x9d at position 30154` — **the control character, not a section sign.** `§` encodes
> `0xC2 0xA7` and cp1252 decodes both bytes happily. **So replacing `§` with "section" leaves the
> mojibake, leaves the control characters, and leaves the crash** — while looking done and moving an
> ASCII count from 51 to 45. **Sixth instance of the day's shape, and the first that was about to ship as
> a remedy.**

**Severity corrected.** All three tracked local readers already belt themselves —
`deploy_ledger.py:226`, `check-lambda-layer-deps:284`, `backfill-lambda-iam-mapping.py:169` all
`read_text(encoding="utf-8")`. **The deploy-completion ledger is therefore safe at the cutover moment**,
which was the real worry. The one unbelted reader is `.github/workflows/lambda-deploy.yml:70`
(`with open(path) as f:`) — passes on an ubuntu-latest UTF-8 default; **"CI-blocking" is UNVERIFIED and I
do not claim it.** What broke on this box was an ad-hoc `json.load(open(p))`, not a tracked tool.

**RULED:** (a) AE~Z's P5 edit uses explicit utf-8 and **adds no non-ASCII** — binding regardless;
(b) **we do not absorb the cleanup** (not ours, not in our path); (c) route to CTO base **with the
corrected diagnosis**, because a section-sign cleanup closes the ticket without fixing the file.

#### G12 · ~2132Z — TWO DOCTRINE-CLASS ITEMS ROUTED (not implemented), and I am an instance of the second

Both routed to `0.0.0_AB_MSTR~Z` for CTO-base landing. Neither gates anything; COO~Z carries both as TO
criteria meanwhile.

**(i) `CLAUDE.md:110`'s pagination remedy names the flag that causes the failure** — full argument in
G1-D above.

**(ii) Our law states the RECEIVER's half of the relay rule and omits the RELAYER's.** `org/XXX.md`
correctly instructs the receiving seat *not* to challenge a relayed ruling's provenance — **which makes
the unstated half load-bearing: if the receiver may not challenge, the grounding obligation sits entirely
on the relayer, and our law never says so.** Formulation is `2.0.0_SA_COO~Z`'s:

> *"A relay is not a lower-evidence act than an assertion; it is the same act with a longer fuse, because
> the receiving seat reasonably treats a routed finding as grounded."*

**Three measured instances today, three senior seats — one of them a POSITIVE CONTROL**, which is why
this reads as a pattern rather than three-of-a-kind:

| # | Seat | Handling |
|---|---|---|
| 1 | `0.0.0_AB_MSTR~Z` | relayed the §6 framing **explicitly marked NOT RATIFIED** — ✅ the control working, cost: one word |
| 2 | `2.0.0_SA_COO~Z` | relayed AE~Z's source-map diagnosis as grounded, unmeasured → the implied fix would have left the crash (G11) |
| 3 | **`1.0.0_SA_CTO~Z` (me)** | cited **Clock v3 — a ruling document — for a live cron expression**, and shipped it toward Andrew (G1-A) |

**2 and 3 are the same class.** The only difference is that a ruling document *feels* like a stronger
source than a peer's message — **and that feeling is exactly the failure, because Clock v3 was wrong about
the very member it was written to pin. The record is not the plane, and a relay of a record inherits the
record's staleness silently.**

**Proposed form, deliberately NOT "measure everything you relay"** (unaffordable at fabric volume):
**when you forward a finding, forward its grounding or forward it as ungrounded** — carry the evidence
pointer (`file:line @ commit`, tool + output, live primitive) or carry the caveat.

*Recorded here rather than only in a message so instance 3 is on the record and not a self-report that
evaporates.*

**(iii) ~2212Z — the RETRIEVAL-FRAME class, named.** DS~Z found the mechanism behind their own citation
error: `sed -n '1047,1290p' | grep -n` numbers the **slice**, not the file (offset 1046; 218/225/226 →
1264/1271/1272, exact reconcile). They proposed naming the shape *"pipe changes the frame."* **Tested
against the three instances, that name fails** — case 2 has **no pipe** (the CLI auto-paginates
internally) and in case 1 the pipe did not change the frame, the upstream failure did. **The pipe is a
vehicle, not the mechanism.** Tighter:

> **An upstream stage silently redefined the domain the downstream stage measured over, and the result is
> WELL-FORMED IN THE NEW DOMAIN. The answer is true about something — just not the thing asked. It is
> undetectable because THE OUTPUT DOES NOT CARRY ITS OWN FRAME.**
> `file contents → error text` · `all rules → page 1` · `file → slice` (and the numbering origin with it)

That last clause is the reason "be careful" cannot help: **nothing in `0`, `100`, or `218:` says what it
is 0 *of*, 100 *of*, or 218 *from*.** Three measured instances today, three different tools, and **every
catch came from printing a denominator or re-deriving — none from care.**

**ROUTING CONSOLIDATED:** items (i) and (iii) **target the same line, `CLAUDE.md:110`** — (i) fixes its
remedy clause, (iii) adds the class name + the undetectability reason. **They are one amendment, not
two**, and they are two halves of one sentence: *the frame problem is why `--no-paginate` is so
dangerous, because a truncated page and a complete result are byte-indistinguishable.* Routed to MSTR~Z
as an **addition to an existing rule, not a new rule** — :110 already legislates the control and already
carries two of the three instances; extending it costs a clause where a new rule costs a paragraph in
every agent's context forever. **Item (ii) stays separate** — it belongs in `org/XXX.md` beside the
receiver clause it completes.

*Also worth the record: DS~Z audited their own committed deliverable after finding the defect rather than
assuming the blast radius — five citations re-verified clean, error confined to one message. "It was only
that one place" is a claim, and they went and checked it.*

#### G13 · RULING ~2135Z — the roster binding: build-generated hash-tied copy, NO S3 leg. Phase 2 is over-broad by one file.

Routed by COO~Z with grounding + provenance marked (DS~Z measured; COO~Z did not) — the discipline from
G12 applied on its first opportunity. **I read `_load_partner_roster()` at `:1718-1746` myself** rather
than take the citation on report, since it is my own 230319Z ruling being invoked. **DS~Z's citation is
accurate, verbatim, including the SystemExit text.**

**The conflict:** the docstring forbids *"NEVER an S3-read fallback and NEVER a vendored copy"* and the
error ends *"Do NOT add another resolution mechanism here."* Doc 03 Phase 2 prescribes exactly an S3
`GetObject` leg for the roster.

**RULED: build-generated, hash-tied copy at the resolving module's directory, via the EXISTING resolver,
NO roster `GetObject` leg.** Test each option against what 230319Z actually targets — **duplicate
authority**, i.e. more than one thing that can answer *"what is expected-ness"* and can disagree:

| Option | Authorities | Verdict |
|---|---|---|
| build-generated, hash-tied | **one** — the zip copy is a derived artifact that **cannot drift**, regenerated + hash-recorded each build; uses candidate 1 **unchanged, zero code edit** | ✅ not a *hand-maintained* copy, not a *new mechanism* |
| S3 `GetObject` | **two** — an object changeable out from under a deployed function without a deploy | ⛔ |

> **This is not rule-lawyering — G9 is this morning's measurement of option (b)'s harm.** The deployed
> roster diverged from the committed authority for **nine days** on `per_partner_max_lag_trading_days`
> with nothing detecting it. Option (b) rebuilds that divergence surface inside the Lambda, with S3 as
> the drift vector instead of a hand-upload.

**Phase 2 is not wrong — it is over-broad by ONE FILE.** `partner_roster.json` → build-generated,
no leg (230319Z applies). `route_bindings.yaml` → Terraform-managed S3 object + `GetObject` **as
written** (230319Z does not reach it). Phase 2's own second half already states option (a):
*"generate it during the build and hash-tie it to the committed authority."*

**Packaging condition (adjacency is a build fact):** `here` is the **resolving module's** directory.
Flat zip root gives `/var/task` and candidate 1 hits — but Phase 1 packages a thin entrypoint plus
refactored modules, so **the build must place the roster adjacent to the module that resolves it**,
whatever the layout, and the fixture test must exercise `_load_partner_roster()` **from the built
artifact**. Getting it wrong fail-closes at build: loud and recoverable, but discovered rather than
designed.

**PUBLISHER — FLAGGED, NOT RULED, and the reason is stated:** Phase 2 also grants the *publisher* roster
read access. If gold reads a build copy and the publisher reads S3, **the two can disagree** — duplicate
authority *across* components. **Direction:** both take build-generated hash-tied copies from the same
committed authority, each recording its roster hash in its own manifest, which makes divergence
*detectable* — the detection absent for nine days in G9. **I am not ruling it because I measured the gold
spine's resolver and NOT the publisher's, and ruling on an unmeasured resolver is the error I corrected
in myself in G1-A.** Named follow-on: measure first, then rule.

**FAIL-CLOSED — ratified, and upgraded from a note to a TEST.** DS~Z's point: this resolver raises
`SystemExit` naming both candidates, and against today's two fail-**green** cases (pmc,
`partner_held_etf`) it is the positive example — **the estate is not uniformly fail-green, so "assume it
degrades silently" is not a safe prior either; you have to look at each one.** P1-1 **preserves** the
property; adding a graceful fallback is forbidden, and the reason is DS~Z's: **it would read as an
improvement in review** — a hardening change and a silent-degradation change look identical in a diff.
**But a TO instruction is also memory, just someone else's.** The control is a **test asserting
`SystemExit` when neither candidate exists** — then the property defends itself and the refactor that
adds a fallback *fails* rather than reads well. Same move as `calendar_source` and
outcome-not-intervention: **make the property assert itself.**

#### G13-A · EXTENDED ~2145Z — a SECOND roster reader, opposite failure mode, and my G13 test was under-scoped

Routed by COO~Z with provenance marked (DS~Z measured 214246Z). **I read `:869-887` myself.** Citation
accurate. `build_cottonwood_mdpf_slice.py` `_cot_window()` is an **independent** roster reader in the
**assets** tree that swallows exceptions and **`return 3`** — *"roster-declared value observed in every
live build."* Its sibling's docstring forbids exactly this: *"it never falls back to a hardcoded number
(CTO ruling 230319Z: a private copy of a roster value is the sect-III-e defect verbatim)."*
**The line cites my ruling while doing what my ruling forbids.**

> **⚠ MY G13 TEST WAS UNDER-SCOPED, and this is mine by DESIGN, not by sourcing.** I built a control
> against "a property that lives only in memory" and scoped it to the resolver we happened to be
> discussing. **A test covering only `_load_partner_roster()` passes today while the defect sits one tree
> over** — the control-that-cannot-fail shape arriving *inside* the control built against it. **Seventh
> instance today.** Extended: **one test per reader**, each asserting it raises when no candidate resolves.

**⚠ THE PROPOSED REMEDY IS INCOMPLETE — FOUR paths reach `return 3`, and removing the bare `except`
closes only two:**

| # | Path | Closed by flat vendoring? |
|---|---|---|
| 1 | neither candidate exists → loop completes | ✅ |
| 2 | candidate exists, unreadable → `except: pass` | ✅ |
| **3** | **candidate exists, reads fine, KEY ABSENT → `w is None` → NO EXCEPTION AT ALL** | **❌ NO** |
| 4 | `int(w)` raises on a non-numeric | ✅ |

**Path 3 breaks the packaging argument.** The `or {}` guards at `:879-880` are engineered *specifically*
so a missing key does not raise — **the fail-green is deliberate, not accidental.** So under FLAT, where
"the hardcode never fires," a roster **schema** change (key renamed, cottonwood row dropped) still lands
on the constant, silently, with the file sitting right there being read successfully. **The function must
fail closed on all four paths, independent of layout.**

> **THE JUSTIFICATION COMMENT IS UNFALSIFIABLE BY ITS OWN MECHANISM** — a better argument than "the ruling
> forbids it," and it generalises. The roster declares 3; the fallback returns 3; **the output is identical
> either way.** So *"observed in every live build"* would remain true **if the roster read had been broken
> the entire time.** The evidence cited to justify the hardcode structurally cannot detect the hardcode
> firing — the orphan-watcher shape, embedded in a code comment as a rationale.

**UNMEASURED AND MUST BE MEASURED BEFORE P1-1: is `return 3` firing in production TODAY?** Nobody knows,
because `_load_partner_roster()` records `_resolved_from` and **`_cot_window()` records nothing.** If the
assets-tree script's runner directory does not carry the roster, the cottonwood carry window is **already**
a constant rather than declared data — **a live instance, not a latent one.** Cheap to check; do not
assume latent. **Remedy, same move as `calendar_source()`: `_cot_window()` must record which candidate
resolved it**, as its sibling already does — then the artifact discriminates and the question never needs
asking again.

**FLAT — RATIFIED, and the meta-point is the ruling.** DS~Z mapped **all** `__file__`-relative loads
across **14 modules** (positive-controlled) → 5 rows; **no layout works without code changes.** FLAT is
decisive not for convenience but because **it keeps the roster ONE PHYSICAL FILE**, which is what 230319Z
protects: **under NON-FLAT, row 2 forces a choice between a silent hardcode and a duplicate copy — and
230319Z forbids both. A layout that leaves only forbidden options is not a layout.** Rows 4/5 are
`__file__`-relative escapes needing rewrite regardless (row 4 exercised → `/config`, escaping the task
root), both already in P1-1. **Row 3 — `mdpf_model_registry.json`, a third adjacency-dependent config —
surfaced only because they mapped ALL loads rather than the two under discussion: evidence for the
denominator discipline, not an afterthought.**

**RULED, in these words for P1-2: the layout choice is a CORRECTNESS decision, not a build-convenience
one** — recorded as convenience, it is one refactor from being changed by someone optimising a zip.

**Behavioural change, stated plainly so review does not soften it:** silent-degrade → refuse-the-build is
real and correct. **If the roster is being read successfully the change is a no-op**; it bites only when
something is already wrong, and then a refused build is the wanted outcome. **The risk is a reviewer
seeing "removes a fallback" and reading it as a regression** — the mirror of DS~Z's point, and why the
test matters more than the instruction.

#### G13-B · RULING ~2202Z — publisher roster: SYMMETRIC. And H8 CLOSES on C2's first branch.

The measurement I withheld G13's publisher half for (AE~Z 215402Z, deployed package via `get-function`;
COO~Z relayed with provenance marked): **the deployed publisher has ZERO roster resolution** — 3,583
bytes, denominator **1** entry, 173 lines, zero `roster`/`ROSTER`/`EXTRA_EXPECTED` references; its only
`get_object` reads the gold source key. Repo tip has **21** roster refs across 230 lines.

> **That reframes the risk: we are not reconciling an inherited divergence — WE ARE CHOOSING WHETHER TO
> CREATE ONE.**

**RULED: SYMMETRIC — build-generated hash-tied copy, NO `ROSTER_BUCKET`/`ROSTER_KEY`/GetObject leg.**
Three arguments, the third decisive:

1. **Declining to create a hazard is the cheap version.** Having measured this morning what a divergence
   surface costs (G9: nine days stale on a live threshold, undetected), deliberately building a second
   one is indefensible — and it is far easier to decline than to remove.
2. **The apparent case for S3 does not survive contact.** "Update expectations without a redeploy" —
   **that scenario does not exist here.** A roster change means a partner onboards or a cadence shifts,
   which requires gold to build that firm's artifacts. **The roster changing is never a publisher-only
   event.** So independence is not a benefit but a hazard: it lets the publisher's expected-scopes drift
   ahead of or behind what gold produces, **and noticing that gap is the publisher's entire job.**
3. **Symmetry is what makes the cross-component invariant CHECKABLE.** Both components carrying build
   copies means **both record a roster hash in their manifests**, so `gold-hash != publisher-hash` is a
   detectable statement that they were built from different commits. **One on S3 and one on a build copy
   leaves nothing to compare — the divergence becomes real and invisible in the same move.**

**One specification:** whatever carries the non-partner `global` scope (`02` has it as an explicit config
row; an env var is acceptable) **must appear in the run manifest beside the roster hash** — otherwise it
is an unhashed third input to expected-ness. **The manifest must fully determine expected scopes.**

**H8 → RESOLVED, on C2's FIRST branch.** `artifact_sha256` **ties** to live `CodeSha256`, with a
discriminating negative control (`mdpf-daily-trigger`'s hash → False); `last_deployed_commit` 63eea3814
real, subject matching. So the close is *reconstructed and verified*, **not** "unreconstructible."
**C2 recorded as CLOSED-UNUSED, not claimed:** a named fallback that turns out not to be needed cost one
paragraph and meant nobody improvised an honesty caveat under deploy pressure. **That is the branch
working, not the branch being vindicated.**

**`01` §10 CORRECTED IN OUR FAVOUR — ratified, and it generalises.** Three of four fields are
**accurate**, including the "build-alongside" note (accurate *because the deployed thing is still the
build-alongside publisher*). Only `iam_role` is stale.

> **THE SOURCE MAP IS NOT STALE ABOUT THE DEPLOYMENT. THE DEPLOYMENT IS STALE RELATIVE TO THE REPO, AND
> THE MAP CORRECTLY RECORDS THAT STALE DEPLOYMENT.** (COO~Z's sentence.)
>
> **General mechanism, into P5's TO because it is not obvious: A SOURCE MAP'S FIELDS HAVE DIFFERENT
> UPDATE TRIGGERS.** Code-side fields update on a **code deploy**; the role field changes when **IAM**
> changes — which can happen without one, and did. **A source map is never uniformly fresh or stale; it
> is fresh PER FIELD according to what last touched that field's subject.** Reading it as one artifact
> with one freshness is the error the pack made.
>
> **P5 consequence, explicit: correct the ROLE field and do NOT "fix" the accurate code-side fields.**
> The pack's framing invites distrusting three correct fields on a file P5 must edit — a well-meant
> cleanup there would inject the drift the map does not currently have.

**Ordering accepted as hard:** P2-1 lands config before P3-1 deploys the publisher — now grounded both
ends (21 refs vs 0, `config/mdpf/` absent as a prefix, 173→230 lines of behaviour change). DS~Z's
key-removal mutant is **required, not optional**: under flat, the silent-literal-3 path is **live, not
latent**.

#### G14 · ~2205Z ANDREW-DIRECT — per-scope platinum, 12 files daily; and the TWO scope bounds it needs

**Andrew-direct at my terminal ~2205Z** (record: `ANDREW_DIRECT_20260806_MDPF_PER_SCOPE_12_PLATINUM_FILES.md`
@0caf2e907, broadcast 5 seats same turn). Answers the design call the `/exec-sum` card raised:
**`platinum/mdpf/{scope}/` × {aggregate-aua-timeseries, aum-metrics, account-distribution} = 12 files,
every single day.**

**Why load-bearing:** per-scope pathing makes channel independence **physically enforceable** rather than
a discipline the builder maintains — a firm's failure is confined to its own file, and absence becomes a
missing/stale *file* rather than a quietly shorter payload. **"Every single day" is part of the ruling:**
12 is a **daily completeness denominator**, so a cycle emitting 11 is *incomplete*, not quiet.

**SURFACED, NOT ADJUDICATED:** his 12 = 3 uniform types × 4 scopes; the pack's measured live denominator
is **14** — plus `cottonwood/account-units` and `global/non-model-assets`. **CVO~Z then measured both
extras written in the SAME publisher cycle (13:50:50Z today)** — so they are **live, not vestigial**, and
retiring them removes something current. Served-output change ⇒ NEVER#3 ⇒ his call. **Holding nothing:
the 12 are identical under either reading.**

##### G14-A · SCOPE BOUND ONE — `_aggregate_aua` is OUT (DS~Z, verified at source)

**RULED: the per-scope ruling is bounded to the PORTAL family.** `gold/mdpf_revamp/_aggregate_aua/{date}.json`
is **not re-pathed**: a different contract, different consumer (`opal-assets-daily-emitter`, not the
portal). **Confirmed at source** — `"aggregate"`, `"partners"` and `"reconciliation"` in one payload, with
genuinely cross-partner folds (`:658` `sum(p["total_aua"] for p in partners)`, `:663`, `:1171`).
**The single-document form IS its function**, not an un-migrated shape; splitting it destroys what it
computes. *Risk this closes:* an executor generalizing "per-scope everywhere" would break the emitter
contract W-1a just moved — whose legs L7/L8/L9 are **still open** and whose rollback target was archived
tonight, making a mistake there **more** expensive right now, not less.

> **THE PRINCIPLE, better stated than "B is exempt":**
> **A multi-partner document is safe only if it DECLARES which partners are present and which are
> missing. One that does not is a silent-drop hazard.**
> `_aggregate_aua` declares (`partners_present`, `feeders_missing`, `rolled_forward_partners`); the
> portal family did not. **Same shape, two verdicts, and the discriminator is the DECLARATION — not the
> file count.** This guards both over-generalizations: re-pathing B, *and* a future builder shipping a
> new multi-partner document without the declaration because "B is fine." *(Citation correction: DS~Z
> placed those fields at `:218`/`:225`/`:226` — those lines are `_empty_feeder`/`read_feeder_local`. They
> live at ~`:1265` and in the `meta` block ~`:1272-1273`. Claim intact; a wrong line sends the next
> reader to unrelated code.)*

##### G14-B · SCOPE BOUND TWO — a 12/12 EXISTENCE pass is not a FRESHNESS pass (CVO~Z)

CVO~Z measured the live served plane (`s3api`, 461 objects, 17 non-archive): **Andrew's 12 all present,
all written today 13:50:49–51Z** — *his ruling describes something the pipeline already produces.*

> **⚠ AND THIS LANDS ON A CRITERION I ENDORSED.** I told AE~Z per-scope pathing makes a missing scope
> discoverable. True — **but I did not bound it.** A fixed a priori denominator makes a **pass cheap**,
> and 12 files at 12 known paths is **byte-identical whether fresh or frozen**. *A 12/12 existence check
> would have PASSED ON EVERY FROZEN DAY* — including the days this project exists because of. **Second
> time today one of these has landed on a criterion of mine** (the first: G13's test scoped to one
> resolver while the defect sat in another tree).

**RULED — the acceptance criterion is TWO-PART and the parts are not interchangeable:**
**(i) EXISTENCE** — 12 objects at 12 known paths; closes *scope-absence*, newly observable.
**(ii) FRESHNESS** — read the served **bodies**, each artifact's data-as-of against its own roster cadence
(`04` §3). **A 12/12 pass is an EXISTENCE verdict and may never be reported as a FRESHNESS verdict.**
*The fixed denominator closes absence-of-scope and opens nothing on staleness — §3 does the real work and
must not be dropped because the count got easy.*

##### G14-C · H16 (NEW) — the denominator structurally cannot see name variants

CVO~Z measured **three underscore twins** (`{49financial,global,inflection}/aggregate_aua_timeseries.json`,
**2026-07-31**, six days stale, **different content** — 159031 B vs the hyphen file's 107059 B) in the
served bucket. **Disposition already exists:** Andrew ruled *"3 scoped underscore twins TRASH"* ~2137Z
(@1893e4f58) — CVO~Z independently re-derived, from the live plane, a set he ruled within the hour.
**Their count also corrects CTO-base's F7**, which said *four* twins await deletion; three exist and the
bare root object is absent at that path (bounded: one bucket, one prefix). **Not a live client-facing
defect** — CVO~Z's own P0-6 work established the portal read-path as scoped-hyphen on three converging
oracles.

> **THE DURABLE FINDING IS NOT THE THREE FILES — THEY ARE RULED AND TRANSIENT. IT IS THAT THE
> `(scope, artifact-type)` PAIR MODEL NORMALISES `aggregate_aua_timeseries` AND `aggregate-aua-timeseries`
> TO THE SAME TYPE**, so the 14-pair denominator **cannot represent them as distinct rows** — both a
> 12-of-12 and a 14-of-14 pass read fully green with them present. **If any future migration produces
> name variants, the denominator is blind again, by construction.** Fix: assess completeness against the
> **actual key listing**, not a normalised type model — an unrecognised key must surface as unrecognised,
> which `04` §1 already requires of the publisher and which the pair model quietly undoes one layer up.
> *(CVO~Z's asymmetry observation — 3 of 4 scopes, cottonwood absent, "a migration that stopped partway" —
> is the tell a variant-aware denominator would have shown the day it appeared.)*

### G8 · H3's Class-A status is conditional on an instrument with a **measured false zero**

`2.0.0_SA_COO~Z` measured, at `c801ec9d5` on a fresh DB (age 0.0h, Nessie HEAD current):
`comp-blast mdpf_aggregate_aua` → *"No downstream consumers found … (no EXTRACTED edge — NOT provably
zero)"*, against W-1a ledger evidence of **four** consumers (`ad76ad830`, 439 partitions
content-verified). **Graph says zero; ground truth says four** — on the one artifact whose contract is
mid-cutover.

The tool is behaving correctly and flags its own lower bound. **The classification consequence is mine:**
Class A is defined as *"measurement we control, result durable."* An instrument that under-reports does
not produce a durable zero — it produces a **false negative that looks like a finding**. So H3's closing
act is specified to exclude it:

- **No census may rest on a graph edge count.** A zero is corroborated by literal-key grep +
  `comp-pipescript` consumers, **denominator printed**.
- **No retirement may cite a zero-consumer graph result as its evidence.** (COO~Z reached the same rule
  independently and is building it into the decomposition; recorded here as the architectural form.)

This is Rule 22a's shape exactly — **silence is the defect, and an operation list is never a deletion
warrant** — and the stakes moved this afternoon: with H4's teardown authorized, a zero-reader claim is
now upstream of an **irreversible** act rather than a reversible one.

### G6 · The closure statement's denominator

`04`'s closure template reports a single count. **"Open holes closed: N of 10" is false under any
reading** — it averages five different kinds of closure and silently upgrades the weakest. Report per
class:

```text
OPEN
  Class A   (durable measurement, ours):        3   H3*, H5, H8
                                                    *H3 admits NO graph-edge-count evidence (G8)
  Class A'  (vendor sample, provisional):       2   H1, H2          <- valid for days probed ONLY
  Class A'' (sovereign condition, ORDERING-     1   H4-condition    <- evidence destroyed by the act
             CRITICAL: capture before terminate)                       it authorizes
  Class B   (sovereign word, still open):       1   H13             <- NOT empty; S3 deletion unauthorized
  Class C   (bounded negative, limitation):     2   H10, H8-fallback <- NEVER reported as "proved"
  Class D   (standing constraints, never close):7   H6, H7, H9, H11, H12, H14-neverstrip, H15-neverstrip

RESOLVED THIS SESSION
  H4-authority   Andrew-direct 2026-08-06 ~2030Z @c801ec9d5
  H14-binding    RULED G7-B (bind lib/ via WS-1); tie-out DISCHARGED + VALIDATED G7-C,
                 n=1096 equal / mutant fired / 2027 divergence MEASURED at 10 dates
  H15-backend    RULED G7-D (install pmc in QA envs; trading_day_calendar never-strip)
```

**15 items, not 10.** Three closed in-session; the residue of each closure is a standing constraint, not
a tick — which is the whole point of Class D.

**Rank:** H3 runs **first**. It is now the discharge instrument for a sovereign condition on an
irreversible act, not merely a deletion-safety census.

---

## 4. Verification of the pack's two corrections — BOTH UPHELD

MSTR~Z did not ratify these; they are mine. Both verified, one **stronger** than the pack claims.

**Correction 1 — "this is not currently a no-schedule outage." VERIFIED (live plane, 2026-08-06).**
`comp-trigger mdpf` — denominator printed: **139 events-rules + 16 schedules scanned**, us-east-1 — all
four triggers ENABLED. Because `comp-trigger` renders scheduler rows as `schedule: -` (it structurally
does not expose `ScheduleExpression`/timezone), I ground-truthed the expressions on the live primitive
per Rule 22a. They match the pack's table **byte for byte**:

| Schedule | State | Expression | TZ | Target |
|---|---|---|---|---|
| `mdpf-scheduled-floor` | ENABLED | `cron(0 9 * * ? *)` | America/New_York | `mdpf-daily-trigger` |
| `mdpf-accrual-bridge-daily` | ENABLED | `cron(40 9 * * ? *)` | America/New_York | `mdpf-accrual-trigger` |
| `opal-assets-mdpf-portal-publisher-daily` | ENABLED | `cron(50 9 * * ? *)` | America/New_York | portal publisher |

Corroborating: `mdpf-daily-refresh-trigger` shows **last datapoint 2026-07-30** — consistent with the CTO
base trace (F1/F2: the INF completion marker stopped landing 07-31), which is exactly why a floor that
does **not** depend on it is the fix. The design lesson stands unchanged; only the *current* root cause
was misstated.

**Correction 2 — "delaying MDPF past 10:16 ET is not a valid fix." VERIFIED, and stronger than stated.**
The pack derives this from Andrew's 10:00 ET deadline. The governing record is Clock v3
(`CLOCK_V3_DELTA_20260804.md:4-7`), Andrew-direct ~00:10 ET 2026-08-04, VERBATIM:

> *"Yeah all of that needs to be fixed now. Also we are not waiting for 12:15p to publish all that, it
> needs to be published by 10a ET. **Which means that any chains associated with that publishing need to
> be identified and shifted earlier as needed.**"*

**The pack's Correction 2 is not merely well-grounded — its conclusion is the sovereign instruction
verbatim.** "Shift the upstream chains earlier, do not move MDPF later" is his sentence, not the
reviewer's inference. Correction 2 is upheld at the strongest available grade.

---

## 5. What COO~Z decomposes off this

1. **H3 runs first** and is scoped to discharge Andrew's port-completeness condition, not just deletion safety.
2. **CAPTURE-BEFORE-TERMINATE is sequenced into Phase 6 ahead of any irreversible step** — EBS snapshot
   first, then the enumerated inventory to S3, then the three-bucket diff with the union-equals-denominator
   assertion. The teardown task cannot be written as a single step.
3. Phase 0 carries **H11 as a hard constraint on probe design** (Orion ≥ 12:15Z), not as a finding to make later.
4. Phase 0 carries **H12's negative branch** so a failed probe has a ruled path.
5. **H13 pre-positions to Andrew NOW** via MSTR~Z — non-blocking, safe default (do not delete), holding no phase.
6. **H6/H7/H9/H11/H12 leave the checklist** into a standing-constraints register re-asserted at each phase boundary.
7. §4's pre-cutover capture **adds the 14-pair schema baseline** (G4).
8. **H14 enters Phase 0** as "what computes the six per-feed frontiers today?" and **Phase 1** as "bind
   one canonical calendar into the Lambda, retire the shim, assert PMC at import." The acceptance battery
   in `04` §2 cannot be written before the Phase-0 half is answered.
9. **No census TO may accept a graph-edge-count zero** (G8); no retirement TO may cite one as evidence.
10. Closure reports **per class** (G6). No row may claim "proved" where its class forbids it.

---

## 6. Grounding

| Claim | Grounded on |
|---|---|
| Correction 1 live state | `comp-trigger mdpf` (denominator 139+16) + `aws scheduler get-schedule` ×3, rail-checked, 2026-08-06 |
| H4 authority absent (as of ~2020Z) | 3 Andrew-direct records read in full — `:39` (08-05), `:5-11` (08-06 1256Z), `:16-17` (08-06 0140) |
| H4 authority GRANTED (~2030Z) | `ANDREW_DIRECT_20260806_MDPF_EC2_TEARDOWN_AUTHORIZED_PORT_COMPLETENESS_CONDITION.md` @c801ec9d5, relayed by MSTR~Z, verbatim quoted §2B |
| H4-condition ordering hazard | `02_NEEDED_VS_NOT_AUDIT.md` (library/imported-source miss; EC2 runtime-installs packages) + `01` §10 / H8 (repo↔deployed divergence measured) |
| Correction 2 / H12 | `CLOCK_V3_DELTA_20260804.md:4-7` (verbatim), `:15-18`, `:27` (vendor-pull row) |
| H11 collision | `CLOCK_V3_DELTA_20260804.md:39-52` (Amendment 1) + EDT/EST arithmetic above |
| H13 / H4 stop-EC2 | CLAUDE.md § Agent Autonomy, human-confirmation clause |
| G5 mechanism | CLAUDE.md § Git (`MSYS_NO_PATHCONV=1`, the `2>/dev/null` clean-empty-stdout hazard) |
| G7 / H14 | `data/mdpf/scripts/gold/_trading_day_calendar.py:1-11` (self-declared divergent), `:37-43` (silent ImportError fallback), `:48-60` (holiday set ends 2026); function-surface diff vs `lib/trading_calendar.py:93,101,108`; import positive-control run |
| G8 | `comp-blast mdpf_aggregate_aua` @c801ec9d5 measured by `2.0.0_SA_COO~Z` (fresh DB, age 0.0h) vs W-1a ledger @ad76ad830 |

**Not verified by me, and stated as such:** the pack's own measurements of runner history, SSM command
IDs, S3 landing times, and the reader censuses. Those are CVO-authored observations at their stated times;
I verified the two corrections and the authority records, not the whole evidence base. Per site-Z
conditions, any `comp-freshness` verdict produced on this box **before `2c4510421`** is discarded — I
produced none.
