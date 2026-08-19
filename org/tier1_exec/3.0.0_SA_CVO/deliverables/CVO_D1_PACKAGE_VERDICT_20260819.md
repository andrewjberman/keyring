# CVO VERDICT — D1 package (MDPF Asset-Category Views) — the Rule-24 taxonomy pass

**Reviewer:** `3.0.0_SA_CVO` · **Date:** 2026-08-19 · **archetype:** VALIDATE
**Package scored, vintage-pinned:**
- `docs/architecture/D1_ASSET_CATEGORY_VIEWS_PRD.md` @8d662d5f1f (191 lines)
- `org/tier1_exec/1.0.0_SA_CTO/deliverables/D1_ATOMDECOMP/run_20260819.md` @8d662d5f1f (45 lines)

**Verdict: ACCEPT WITH 2 P0 — BOTH INSIDE THE RULE-24 DECLARATION ITSELF.** This is the most careful
of the three packages read so far and the declaration is a serious one: it states axis intent, grain,
MECE and state-coherence separately, and it **volunteers a Rule-24(iv) non-mover** (Alternatives/
Insurance empty-but-declared). The display-vs-stored composition table (§3) is the right resolution of
Andrew's label against the spec's stored-enum ban, and Q1 was raised rather than assumed. **Both P0s
say the declaration is incomplete, not wrong.**

**Andrew's taxonomy is sovereign and I am not reviewing it.** What is reviewable is the agent-authored
COMPOSITION of his labels onto CRO's ratified axes — that composition is a Rule-24 authoring act, and
that is what follows.

---

## P0-1 — For CTO. The Rule-24(iv) state-coherence claim is false for one of the five values, and it is the value the postulate was written to catch.

§3's declaration states: *"State coherence: all five nodes are DISPLAY-layer over one registry + one
projection change — **one remedy moves all values together.**"*

That is not true of **Client > Residual**, and the PRD's own text proves it. Four of the five view
nodes are populated by **REGISTRY MEMBERSHIP** — §4.1 keys entries by `member_id` and §4.2 raises on a
member absent from the registry. Residual is populated by **ARITHMETIC**: R10 defines today's
non_model as the per-firm residual `total_aua - model_aum` (the A4 two-term rule), and §3 maps
Residual to *"the residual class (~= served non_model compatibility number)"*.

**A registry cannot deliver Residual, by construction — Residual is the COMPLEMENT of the registry.**
Adding a member populates the other four nodes; it *shrinks* Residual without the registry ever
naming it. So the "one remedy" structurally delivers 4 of 5 values, which is precisely Rule-24(iv)'s
own test: *"If building the obvious instrument delivers some values and structurally cannot deliver
others, the axis is a stability defect and YOU MUST NAME WHICH VALUES DO NOT MOVE."*

**The declaration names a non-mover — but the wrong one.** Alternatives/Insurance being empty is a
*population* fact that the registry WILL fix the moment a member is registered; it is the benign case
and it was correctly disclosed. Residual is the *structural* case and is undisclosed. §4.2's own guard
makes this explicit and is otherwise excellent: *"member in data but not registry -> RAISE (F5), never
silent fold to residual."* That guard exists precisely because Residual is fed by a different producer.

**Recommend (CTO):** amend the Rule-24(iv) line to name Residual as the structural non-mover and state
its producer (the A4 subtraction) beside the registry. This changes no build — TO-D1c already keeps the
compatibility number emitted unchanged — but it stops a future reader concluding that registering a
member is sufficient to move every view node.

---

## P0-2 — For CTO + DE. The five view numbers do not sum to total AUA, and the PRD asserts they partition. This is the exact class D2 measured today.

§3 declares: *"MECE: the five peers **partition** the registered population; Client is the explicit
catch-all."* Formally that is scoped to *the registered population*, and within that scope it holds.
**But the VIEW displays registered and unregistered populations side by side as five peer numbers**,
and two PRD requirements together guarantee they overlap:

1. §3 component 2: *"unfolding the 2 SMAs from non_model into the SMA view is the first visible
   change; **per-firm non_model compatibility numbers stay emitted unchanged**"* (R10).
2. TO-D1c acceptance: *"SMA view carries the 2 unfolded SMAs; **non_model compatibility number
   unchanged**."*

So after this ships, the 2 SMAs (`opal_growth_sma`, `opal_div_sma` — R5, today folded into non_model)
appear in the **SMA** node **and remain inside the unchanged non_model figure that Residual displays.**
**Summing the five top-level numbers double-counts them.** The `~=` in §3's Residual row
(*"~= served non_model compatibility number"*) is carrying the entire ambiguity: it is not stated
whether Residual displays non_model, or non_model minus the unfolded members.

**Why this is P0 rather than a labelling nit:** DE builds the top-level view from these numbers, a
five-peer breakdown is the one UI shape a user will instinctively add up, and the compatibility
requirement is deliberate and correct — so the overlap is not a bug to fix but a property to DECLARE.

**The estate measured this exact class today, in the package I reviewed two hours ago.** D2's run R17
records that BD portfolio groups are *"OVERLAPPING VIEWS, never a partition: 90.6% of accounts sit in
2+ groups; **NEVER sum across groups** (all-group MV sum ~$10.2B vs ~$1B book — overlap, not error)"*,
and D2 §4b makes never-sum *"a hard rule in the oracle's own frame."* **D1 asserts partition where D2
proved overlap, on the same day, over an adjacent population.**

**Recommend (CTO):** state explicitly in §3 whether the five displayed numbers sum to total AUA. If
Residual displays the unchanged compatibility number, they do not — and the never-sum caveat belongs in
the view's own frame (D2 §4b is the precedent), plus a TO-D1d acceptance line that no cross-node total
is expressible in the UI. If instead Residual is to display non_model-minus-unfolded, that is a served
semantics change and TO-D1c's "compatibility number unchanged" acceptance contradicts it — those two
readings cannot both hold.

---

## P1-1 — For CTO. Family vocabulary, third data point; plus a split-verdict row that cannot be cited unambiguously.

**(a) Third spelling.** D1's run declares only **MEASURED / INFERRED** and then uses **`MEASURED
(record)`** on rows 1, 10, 11. Across three packages by one author on one day: D2 =
`MEASURED-AT-RECORD`, D7 = `MEASURED-RECORD`, D1 = `MEASURED (record)`. **Three spellings of one class,
and only D7 declared it.** This is now measured across three of ten packages rather than suspected —
it confirms the D7 P1-2 recommendation (promote D7's header to the family standard) and makes it a
family act, not a per-package fix.

**(b) Split verdict, row 9.** R9 carries **two verdicts on one row**: *"INFERRED (dollars) / MEASURED
(grain hazard)."* Epistemically this is *good* — the author correctly refused to launder Andrew's
figures into MEASURED. But it means **"cites R9" does not identify which half is being relied on**, and
both halves are cited: §2 uses R9 for the Cottonwood dollars AND for the relationship-grain hazard,
and §4.2's grain guard cites R9. Under your own illegal-derivation rule, a citation that cannot resolve
to a single verdict cannot be checked. **Recommend: split R9 into two rows (R9a dollars INFERRED, R9b
grain MEASURED) so every citation resolves.**

---

## P2-1 — For CTO. The "SMA" display label implies its four siblings are not SMAs.

§3 resolves the stored-enum half correctly and I am not reopening it: the ban binds the stored value,
Andrew's later sovereign word governs display, `strategy` stays stored. **That is right.**

The residual tension is at the display layer only: the prior-art spec's invariant is *"every account is
inherently an SMA"* (R2). Labelling **one of five peer nodes** "SMA" therefore asserts something false
about the other four — Models, Alternatives, Insurance and Client accounts are SMAs too, under the
spec's own definition. R3 concludes *"No conflict: display label vs stored enum"*, which is true of the
enum and not quite true of the label.

**Andrew's word stands and this is not a request to change it.** Recommend one sentence in §3 recording
that the display label is scoped to the strategy-products view and does not assert account structure —
so that a future reader meeting the spec's invariant does not "fix" the label back and reopen a
sovereign call.

## P2-2 — For CTO. DONE could be read as an acceptance target derived from an INFERRED row.

DONE reads: *"Cottonwood shows ~$7M Custom + ~$30M Client **(measured values)** under the correct
nodes."* The `(measured values)` qualifier and TO-D1e's *"MEASURE the … figures from cot BD data"* are
the correct handling of an INFERRED row and I am **not** reporting this as the illegal-derivation class
— the PRD does the right thing.

The narrow risk is a reader taking `~$7M` as the bar. **Recommend:** state that the measured figure
REPLACES the estimate and that DONE is *"the measured Custom and Client figures display under the
correct nodes"*, with the estimates recorded as the pre-measurement expectation. If the measurement
returns $12M, DONE should be met and the estimate corrected — not the reverse.

---

## Explicit deferrals

- **Andrew's taxonomy itself** — sovereign. Reviewed the composition, not the choice.
- **R9 Cottonwood dollars as INFERRED** — correctly marked, and the PRD converts measuring them into
  acceptance work (TO-D1e). **This is the pattern your rule wants and I am flagging it as exemplary,
  not defective.**
- **Build-ladder rung 2 (extend the crosswalk, not a new framework)** — §5.3 shows the evidence
  changed the design from standalone artifact to mechanism extension. Conforming; no finding.
- **RQ key namespacing** — new keys under `['mdpf','category-views',...]` against a clean 105-site,
  0-mismatch baseline (R8). Conforming.

---

## What you should have asked but did not

**If the category-views rollout half-fails, what tells anyone — given the fallback is designed to be
invisible?**

§4.3's error case reads: *"absent `category_views` block -> the page renders today's view
(feature-gated fallback, **no hard dependency during rollout**)."* That is good engineering and I would
not remove it. But pair it with §4.2's *"Existing fields UNCHANGED"* and the result is that
**a successful deployment and a failed one render identically.** If TO-D1c ships and the projection
emits an empty `category_views` block — registry empty for a firm, view_path mismatch, a rollup that
silently produces no nodes — the page falls back to today's view, which is exactly what a correct
pre-rollout state looks like. Nothing in the PRD distinguishes *not deployed yet* from *deployed and
producing nothing*.

**This is the third instance of one shape in three packages from the same authoring pass**, which is
why it is worth naming as a pattern rather than a per-PRD nit: D2's C4 could clear us using our own
input as our own witness; D7's SLA receipt lives only in the Analyst's memory so an un-ticketed mail
leaves no trace; D1's fallback makes rollout success unobservable. **Each is a case where the failure
mode produces a clean, healthy-looking surface** — Rule 22b's anti-correlated class, three times.

**Moratorium-safe closure, and it is not a monitor:** make TO-D1d's acceptance *exercise the
empty-block case explicitly* (assert the fallback fires when it should), and make the DONE bar a
POSITIVE assertion that `category_views` is being consumed — five nodes rendering with non-null
member lists for at least one firm — rather than "the page renders". A rendered page is not evidence
of a shipped feature when the fallback renders the same page. That is an acceptance criterion, not an
alarm.

— 3.0.0_SA_CVO
