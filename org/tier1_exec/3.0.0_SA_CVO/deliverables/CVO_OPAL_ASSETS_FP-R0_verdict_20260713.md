# CVO FP-R0 VERDICT — OPAL_ASSETS PRD v0.1

**agent:** 3.0.0_SA_CVO (base — completing the `~A` lane's open review) · **date:** 2026-07-13
**archetype:** VALIDATE
**Review object:** `docs/architecture/OPAL_ASSETS_PRD.md` @ `79231da3e` (CTO~B)
**Scope requested (CTO~B, 024240Z):** claim-classing + evidence discipline on the row shape
`{cohort, source_master(s), value, as_of, state}`, the ONE-`as_of` semantics, the both-masters dedup
grain, and the AC1–AC6 spine.

---

## Verdict: **ACCEPT WITH FOLDS** — not a block.

The spine is sound. The frozen G1–G6 form survives synthesis intact, §3d (own-field `as_of`, never a
cross-partner min) is the right call and is stated unambiguously, and the honesty thesis — *"a stale or
missing cohort is visible as itself"* (`:107`) — is the correct north star.

**But the row schema does not yet deliver that thesis, and one AC names a falsifier nothing can
detect.** Five folds below. FP-R0-1 should land before COO decomposes; the rest can fold into v0.2.

---

## FP-R0-1 — **[P0]** The `state` enum cannot represent `incomplete`. The bucket would be *less honest than the checker it converges.*

**Grounded.** The live cohort-freshness checker emits a **fourth** state:
`infra/aws/lambda/mdpf-pipeline/mdpf-freshness-checker/lambda_function.py:305` — `state = "incomplete"`,
fired for a `partner_multi_master` cohort when an expected sub-source master is absent from the served
artifact. Its own comment (`:298-300`) is explicit: *"partial-present, not wholly-missing"* — the primary
master is present (possibly merely stale) but the gap **must be LOUD**, and `:310` escalates it to
`MISSING_STALENESS` so it alarms.

The PRD's row carries `state ∈ {fresh, rolled_forward, missing}` (`:11`, `:49`, AC5 `:85`). **Cohort-8's
CURRENT live condition is `incomplete`.** Forced into this enum it becomes one of three wrong things:
- `fresh` → **false green, the undercount is invisible** — a direct violation of the PRD's own guardrail 5,
  *"NEVER silently undercount"* (`:103`);
- `missing` → false: the value IS there (the `08242234` avgcap side);
- `rolled_forward` → false: it was not rolled forward.

AC5's falsifier (*"a rolled_forward row labeled fresh"*) **does not catch this** — an `incomplete` cohort
labeled `fresh` passes AC5 as written.

Note the PRD already expresses partialness — but in a *second, disjoint* place and at a different grain:
the G4 `partial: 08242234-only` flag (`:74`, AC4 `:84`). So v0.1 has two unrelated representations of the
same concept and no state for it on the cohort row, while the live checker already has one unified
representation.

**→ For CTO~B (fold):** carry `source_masters` (**expected**) + `masters_present` (**actual**) on the row.
Then incompleteness is **derivable** rather than hand-maintained, the G4 `partial` flag collapses into the
row schema instead of living beside it, and the bucket's vocabulary is a superset of the checker's — never
a lossy projection of it. Whether `incomplete` is then a stored enum value or a derived predicate is your
call; what must not ship is a bucket that cannot say what the alarm layer can already say.

---

## FP-R0-2 — **[P1]** AC3's double-count falsifier has **no detector**.

AC3 (`:83`) falsifies on *"cohort-8 `missing`/`99`, **or a double-count across masters**."* The first
limb is detectable — the G6 alarm spine reads it. The second is not: **the alarm spine measures
FRESHNESS/staleness**, and a double-counted cohort is perfectly fresh. It just reads *bigger*. Nothing in
G6, and nothing in the PRD's AC spine, can observe it.

An AC whose falsifier has no instrument is an AC that always passes.

**→ For CTO~B (fold):** G2 acceptance needs a **dedup reconciliation instrument** — the both-masters
account-overlap census (see FP-R0-4), asserted against the deduped row count. **→ For COO:** this is a
G2-acceptance deliverable, not an afterthought; it should appear in the G2 TO.

---

## FP-R0-3 — **[P1]** AC5's `as_of` is unfalsifiable by any *live read* of the bucket. It needs an **emit-time mutant**.

AC5 (`:85`) requires each row's `as_of` to be the cohort's OWN-field value. Its falsifiers are
*"two `as_of` semantics observable in one bucket"* or *"a rolled_forward row labeled fresh."* Both are
**read-side** checks on the emitted artifact.

Consider the emitter stamping `as_of` at **emit time** (today's date) instead of propagating the source's
own vintage. Every row is then internally self-consistent: fresh `as_of`, `state: fresh`, plausible value.
**The bucket looks perfect. No read of it — however sharp — can detect the bug**, because the evidence
that would betray it was destroyed at write time.

Only a mutant at the emitter catches it: feed a **known-stale** source, assert the row carries the
**source's** `as_of`, not today's. This is the same date-axis class as the round-8 AoR finding (a
frozen/repeated as-of collapsing the partition so a green reading hides a swap) — and I will note it is
the same class as the defect I am simultaneously reporting against the AoR chokepoint. **A vintage field
that is carried but never asserted on is the recurring shape of our misses.**

**→ For CTO~B (fold):** AC5 needs an emit-time mutant as an explicit acceptance artifact, not a read-side
assertion. **→ For DS (when G5 is GO'd):** the emitter must propagate, never stamp.

---

## FP-R0-4 — **[P1]** The dedup grain is under-specified — and the under-specification has an undercount edge.

§3c (`:56`) commits to *"avgcap (`08242234` RPS) + `08335338` CBUGL positions, **DEDUPED BY ACCOUNT**"* —
and calls it *"the confirmed composite design, not a hedge."* The design is right; the **grain** is not
specified. Three things are missing, and each changes the number:
1. **The duplicate key.** Account number alone? Account × CUSIP? Account × CUSIP × date?
2. **Master precedence.** When both masters carry the same account with *different* positions, which wins?
3. **Account- vs position-level.** §3c says "by account," but the evidence it cites is *positional*
   (~22K position rows in `08335338`; ~$153M DIVZ in `08242234` RPS). **Account-level dedup across masters
   that hold different positions for the same account silently DROPS one master's positions** — the exact
   undercount G4's `partial` flag exists to prevent, reintroduced at a different seam.

**→ For CTO~B (fold):** specify the key, the precedence, and the level. **→ For COO:** the
both-masters **account-overlap census** belongs in the G2 TO as an explicit *investigate-and-report*
deliverable — which is consistent with the PRD's own guardrail 3 (`:103`, *"`08335338` work is
investigate-and-report first, never a silent cutover"*). Do not let the census be inferred from the fix.

---

## FP-R0-5 — **[P2]** G1's mechanism claim is grounded — but the PRD carries no citation.

G1 (`:70`) asserts *"silver alternates 46K/1.2M rows = stub/partial landings."* That claim **is**
grounded, just not here: `org/critical_paths/change_management/20260702T2042Z_bd-silver-alloc-stub-reject_deploy_completion.md:19-21`
— *"GROUNDED LIVE: silver/allocations/2026-07-02.parquet landed at 45KB vs 07-01 = 1.2MB — BD returns an
intraday T-0 allocations SNAPSHOT as an undersized partial stub."* The PRD cites it **zero** times
(`grep -c` on the PRD = 0).

No re-investigation is needed — only a pointer. **→ For CTO~B:** attach it, so COO's G1 TO inherits
Rule-22 grounding instead of re-deriving a causal claim that is already source-confirmed elsewhere.

---

## Deferrals (explicit)

- **G3(b) — 2021 depth.** Not reviewed, not a fold. It is Andrew's vendor-channel call and the PRD
  correctly marks it non-gating (`:92` P2 / gate table). I am not re-litigating it.
- **The DynamoDB key design** (PK=`run_date` / SK=`cohort_id` + GSI `cohort_history`) is **out of my FP-R0
  scope** — CTO~B already arch-gated it ACCEPT-AS-BUILT (`70687ba8a`) and the strongly-consistent
  cross-cohort daily read is the better criterion. No objection; flagging only that I did not verify it.
- **AC6 (never-widen co-sign)** needs no fold. It is correctly stated and correctly binding.

---

## What you should have asked but did not

**Which of the six converging sources can *lie about its own `as_of`* — and does the bucket inherit the
lie?** The PRD's entire honesty guarantee rests on each cohort's OWN-field `as_of` being truthful at the
source. §2 (`:42`) already records that **two conflicting `as_of` semantics exist today** (timeseries
`as_of_last=07-08` vs partition `as_of=07-06`) — i.e. we have live, documented proof that at least one
source's self-reported vintage disagrees with its partition vintage. The PRD resolves which semantics the
*bucket* commits to (§3d — correct), but it never asks **which semantics each SOURCE is reporting when
G5 reads it.** If a source hands the emitter a timeseries `as_of` while its data is partitioned a day
behind, the bucket faithfully records a truthful-looking `as_of` that is wrong — and every downstream
falsifier in AC1–AC6 reads green, because they all check the bucket's *internal* consistency, never the
bucket-against-source. FP-R0-3's emitter mutant closes the *stamping* half of this. The other half — a
per-source `as_of`-semantics audit before G5 wires them together — is not in the PRD, not in the AC spine,
and is the one thing that would make the convergence untrustworthy while looking perfect. I have not
verified how many of the six sources are exposed; that census is the ask.

---

**Routing:** `1.0.0_SA_CTO~B` (folds → PRD v0.2) · `2.0.0_SA_COO` (FP-R0-2/-4 are TO-shaped: the dedup
census + the double-count detector are G2 acceptance deliverables, not implementation details).
FP-R0-1 before decomposition; the rest fold into v0.2.

— 3.0.0_SA_CVO
