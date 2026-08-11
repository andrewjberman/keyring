# The MDPF scheduling jam — its general form, and an implementation strategy

**Author:** `4.0.0_SA_CRO~A` · **2026-08-11 ~0330Z** · **archetype:** TRACE + COORDINATE
**Scope authority:** Andrew-direct @85e51be03a: *"there has been some problems we've been jammed up
on with scheduling and I need you to figure it out. I suspect that our atom_decomp workflow may come
in handy to get to ground truth fast on this subject… [suggest] implementation strategy."*
**Companion record (the proving run):**
`org/tier1_exec/4.0.0_SA_CRO/deliverables/MDPF_COTTONWOOD_CUSTODY_INVERSION_MECHANISM_20260811.md`
@562cbd444d. **Evidence base for rows I did not measure tonight:**
`MDPF_REMEDIATION_PLAN_20260810.md` @dbbbfa9cd3 + `org/projects/MDPF_PIPELINE_TRUTH.json` — each
matrix cell below carries its source class.

---

## 1 · THE JAM'S GENERAL FORM, IN ONE PARAGRAPH

Every measured defect in this program — the floor reading before its inputs land, orion/eclipse
serving one trading day mislabelled, the cottonwood custody freeze on unsettled versions, the smartx
DirtyRunError conversion miss, the schwab weekend duplicates — is the SAME SHAPE at different
coordinates: **two adjacent stages of one leg disagreeing about an undeclared property of the
schedule.** Not one broken clock; a set of pairwise composition mismatches. The fabric has been
finding these cells one at a time, each by accident, each looking like a novel incident. The
remediation waves (W1–W5b) fix the cells found so far, and they are correct — but nothing prevents
the next retime, new vendor, or new leg from minting a fresh mismatch, because **the properties that
must agree are nowhere declared; they live implicitly in code, cron expressions, and vendor
behavior.** The strategy below makes them explicit, closes the one policy question they all lean on,
and routes the two mechanical fixes — with almost zero new construction (Build Ladder rungs 2 and 6).

## 2 · THE FIVE-ATOM SCHEDULING CONTRACT (the atom_decomp application)

Decompose each pipeline leg into five independent properties. Tonight's custody dig was the proving
run: the defect was invisible at every single stage (each behaved as designed) and became visible
only at an atom boundary — which is precisely the decomposition's claim about where to look.

| atom | question | values seen in this estate |
|---|---|---|
| **A1 · write cardinality** | how many times is one date-key written? | single-write · multi-write-restating (cot custody) · multi-write-fill (weekend lag-collapse; schwab D-20) |
| **A2 · date-label semantics** | what does `date=D` / `…_DAILY_D` MEAN, and who derives it? | content as-of (schwab, blackdiamond) · run date (eclipse, cot gold) · run−1 forward-label (orion) · filename-only, no in-file carrier (cot custody xlsx) |
| **A3 · trigger predicate** | what makes the next stage run? | S3 object-created (5 of 6 silver legs) · process-OnSuccess (smartx — the W5 deviation) · clock (floor, mirrors) · sentinel object (`_BRONZE_COMPLETE.json`) |
| **A4 · consumer re-delivery policy** | what happens when a key it already consumed is written again? | first-write-wins (`mirror_conversion.py:474` skipped-idempotent) · merge/dedup (cot silver etag-skip) · re-serve-last-good (publisher) |
| **A5 · settle window** | when does the vendor stop restating a date? | 0d assumed everywhere · **measured ≥2d for Black Diamond custody** (version deltas) · unmeasured for schwab (G-3c: "no measured vintage") |

**Rule-24 self-check (Taxonomy Law binds this schema too):** one intent per axis (each describes one
scheduling property), same grain (all per leg×table), values MECE within each axis. State-coherence:
A1–A4 are code/config-owned and move under one remedy each; **A5 is vendor-owned and CANNOT be moved
by us — named per Rule 24(iv) as the axis that does not move with the others.** That asymmetry is
load-bearing: A5 is measured and accommodated, never fixed.

**The composition law the jam keeps violating:** `A4 must match A1` (a multi-write key with a
first-write-wins consumer silently freezes on the earliest version) · `A3 must fire on every write
A1 produces` (OnSuccess misses landed-but-dirty; a clock floor misses everything after it) ·
`A2 must be derivable from content or a declared offset, never from the consumer's clock` ·
`serving must not read a key inside its A5 window as final`. Every W-wave and every finding tonight
is one of these four sentences at specific coordinates.

## 3 · THE MEASURED MATRIX — where every known defect sits

Source classes: **[T]** measured tonight by me · **[P]** measured in the remediation plan / truth
JSON · **[U]** unverified, flagged for the owning census.

| leg | A1 | A2 | A3 | A4 | A5 | defect at the boundary |
|---|---|---|---|---|---|---|
| cot custody (BD→silver) | **multi-write** [T] | filename-only [P] | S3-event [P] | **first-write-wins** [T] | **≥2d** [T] | **A1×A4: frozen on unsettled v1; +$1.10M raw-grain on 08-07** [T] |
| cot custody retry-net | — | **re-pull of day d lands d−1bd** [T] | sweep-before-primary [T] | — | — | **A2 double-lag: self-report wrong 1bd nightly; phantom heal structural** [T] |
| smartx (axis source) | single [P] | content as-of [P] | **OnSuccess** [P] | first-write-wins | ?0d | **A3: landed-dirty bronze converts nothing (08-10 live)** [P] |
| orion | single [P] | **run−1 forward-label; normalizer sealed but never called** [P] | S3-event [P] | — | 0d? | **A2: served one trading day late, exact-to-the-cent** [P] — W1 |
| eclipse | single [P] | **run-date key, date=D+1 contains D** [P] | S3-event [P] | — | ? | **A2: same class** [P] — W1 |
| schwab CRS | **multi-fill (weekend carries Thursday)** [P] | content as-of [P] | S3-event [P] | idempotent | **unmeasured (G-3c)** [P] | A1 benign only while A5=0 holds — unproven |
| floor/gold | — | run-date partitions (cot gold collision class) [P] | **clock 13:00Z before 4 inputs** [P] | — | — | **A3: ordering — W3's ruled fix (floor 13:30, pulls 13:02)** |
| 49F BD runner | **[U]** same code pattern (`bd-49f-runner/lambda_function.py:61`, lag=1 env) | | | | | **routed to CTO's predicate census — not solved twice** |

**Read-down of the in-flight waves against the matrix:** W1 = A2 fixes (orion/eclipse) · W2 = the
frontier-coupling half of A2 · W3 = the A3 clock ordering (ruled) · W4 = the firm selector that
makes per-firm A3 possible · W5/W5b = A3 predicate unification (smartx to estate pattern) + guard
integrity. **The waves are right and none of them is displaced by this document.** What the matrix
shows is what remains uncovered after they land: the cot custody column [T], the schwab A5 cell
(G-3c), and the 49F adjacency [U].

## 4 · THE STRATEGY — three moves and one proposal, in order

**MOVE 1 — DECLARE THE CONTRACT (make A1–A5 explicit per leg).** The estate already has the homes:
`comp-estate --definitions` carries ratified terms; `comp-freshness` already carries a declared
`freshness_basis` per artifact — the same declaration pattern, extended by five fields per leg,
**inside the existing registry, not a new tool** (Build Ladder rung 2; the alarm moratorium is
untouched — a declaration is not a monitor). Population is one sitting: the matrix above IS the
initial content for the MDPF legs; each [P] cell inherits its citation, each [U] stays marked.
Owner suggestion: CVO lane owns the registry surface (graph-lane single-writer discipline), values
supplied by the leg owners. **What this buys:** the next retime/vendor/leg change has a place where
its composition assumptions are visible BEFORE the apply — the cutover-gap discipline W3's TO
already demands, generalized from "state it in your apply plan" to "it is already on record."

**MOVE 2 — CLOSE THE ONE POLICY QUESTION EVERYTHING LEANS ON (Andrew, one ruling).** The A4 cell
for restating vendors is not an engineering choice: *when a vendor restates date D inside its settle
window, does our silver track the restatement (latest-write-wins until settled) or freeze the first
observation (point-in-time)?* This is the same axis as his 08-10 point-in-time ruling (gold roster)
and `1.0.0_SA_CTO`'s open custody-history call — **jointly presented with CTO per our agreed split,
one question, ruled once, then applied per contract row instead of re-litigated per incident.**
Note the asymmetry his 08-10 ruling already teaches: point-in-time was ruled for ASSIGNMENT history
(a business event). A custody VALUE inside the vendor's settle window is not a business event — it
is the same number still settling. Whether that distinction moves his answer is exactly why it is
his call and not ours.

**MOVE 3 — ROUTE THE TWO MECHANICAL FIXES (no policy content, COO routes).** C-2 (retry-net
double-lag: pass as-of dates to a window builder that does not re-apply the lag —
`cot_bronze_ingest.py:1135`/`:306-320`) and C-3 (sweep/primary order or probe-day universe —
`ssm.tf:143` vs `:165`). Both are single-function corrections inside the existing nightly; no new
paths, no schedule change, DS/AE lanes per Rule 13. They are correct under EITHER Move-2 answer, so
they need not wait on it.

**PROPOSAL ONLY (Andrew's word required — no-inferred-gates):** a commit-time lint candidate —
any diff touching a `ScheduleExpression`, EventBridge/Scheduler cron, S3 notification config, or
converter idempotency path must cite the contract row it changes. Not implemented, not designed
beyond this sentence; it is the gate-shaped shadow of Move 1 and only he can want it.

## 5 · METHOD NOTE — what atom_decomp did and did not do (for the ATOM_DECOMP program record)

**Did:** the custody dig succeeded exactly as the workflow predicts — every stage read as designed
in isolation; decomposing the leg into independently-verifiable atoms (producer arithmetic, sweep
arithmetic, step order, mirror fidelity, converter policy, artifact clocks) localized the defect to
boundaries, and three of the five boundary checks produced findings (C-1, C-2, C-3). The
"two instruments each seeing one write of a multi-write key" dissolution is a textbook
map-vs-territory catch the coherence base's proxy warnings name.
**Did not:** atom_decomp did not supply the axis vocabulary — A1–A5 had to be coined here (and
Rule-24-checked). If the contract registry is ratified, the vocabulary becomes reusable and the next
leg's decomposition starts from filled axes instead of raw code. That is the workflow maturing from
method to instrument, and it is the honest version of "came in handy": it shaped the dig; it did not
run it.

## 6 · OPEN AT ANDREW (the complete list from this document)

1. **Move-2 ruling** — restating-vendor conversion policy (joint CRO+CTO presentation; CTO holds
   the custody-history half).
2. **Move-1 ratification** — the five-axis contract as a registry surface (Rule-24 checked above;
   his Taxonomy Law makes new classification schemas his to accept).
3. The **gate candidate** in §4 — proposal only.
4. Nothing else: C-2/C-3 routing is COO-lane once he nods at the direction; the W-waves continue
   untouched by all of this.
