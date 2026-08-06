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
would be recorded as closing H1. **12:15Z is a hard floor on the H1 probe design**, not a detail for
implementation. *(Note: `02` correctly declines to PORT the Orion bronze pull into the Lambda — but the
clock move lands in the upstream modules, which Phase 5 step 7 applies **first**.)*

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
