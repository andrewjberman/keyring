# A Value Must Carry Its Claim

**Status:** Doctrine. Binding on design, gate conditions, and acceptance criteria.
**Author:** `1.0.0_SA_CTO`, 2026-07-24. **Occasion:** six independent instances in ~30 hours, across six
subsystems, five agents, three git trees — reached from different directions, on the same day, by people not
talking to each other about it.

> Three coincident rulings bind only their three surfaces. **Doctrine binds the next one.** — `2.0.0_SA_COO`

---

## The principle

**A value must carry the claim it is making, in a field a consumer can reject on — never in a heuristic, a
convention, or a reader's memory of how it was produced.**

Two claims travel with every served value, and both get dropped:

| The claim | The question it answers | When it is dropped |
|---|---|---|
| **PROVENANCE** — *how do we know this?* | measured / inferred / held / absent | a value and a guess share one type |
| **BASIS** — *what quantity is this?* | which firms, which axis, which source | the same field name spans two quantities |

When either is dropped, **the artifact asserts more than it knows** — and nothing downstream can tell.

---

## Corollary 1 — the missing third state

**Binary models collapse "we do not know" into either "fine" or "broken." Both are lies.**

Every instance below was first framed as a two-state problem, and every fix was **adding the state, not widening
the predicate**:

| Surface | The false binary | The state that was missing |
|---|---|---|
| cot completeness sidecars | complete / incomplete | **UNKNOWN ≠ COMPLETE** — `>=1 row` measures *not-a-stub*, not completeness |
| D_00 served firm AUA | certified / substituted | **HELD ≠ CERTIFIED** — a held cert is not a fresh one, and silently re-basing is not holding |
| deploy_ledger red-scan | closed / unclosed | **UNREADABLE ≠ UNCLOSED** — three ledgers were closed *in fact*; the reader could not parse them |
| retry-net `_table_complete` | complete / incomplete | **INFERRED-PRESENT ≠ MEASURED** — enough to stop re-asking, *not* enough to advance a client-data chain |

> **The instinct to widen a predicate until the awkward cases pass is always wrong.** It retires the control.
> The awkward cases are awkward because the model is missing a state.

**Test:** if a consumer asks "did we measure this or infer it?" and the artifact cannot answer, the state is
missing. Add it.

## Corollary 2 — carry the basis

**The same field name across two bases is a defect even when both values are correct.**

| Surface | Two bases, one name |
|---|---|
| MDPF Global count | `measured` (3-firm) · `band_2firm` (49F+INF only) · `frontier_stamp` (roster, own as-of) — plotted as one line. The +408 step on 07-17→07-22 is a **basis seam, not growth** |
| MDPF value vs count | the **value** line includes Cottonwood; the **count** line does not — *same chart, same artifact, same `by_model`* |
| bd/49F served AUA | `header_metrics` held-cert **$1,879,986,733.13** vs `timeseries_chart`/`partner_analytics` gold **$1,692,561,337.83** — **−9.97%, same nightly run, no instrument reports it** |
| P1 total-name asymmetry | Global `opal_aggregate_aua` vs per-firm `partner_custody_total` — genuinely different quantities |

**On that last one the intuitive fix was wrong and was refused:** forcing *one name* would have hidden a real
semantic difference behind a shared label. The ruling is **one ACCESS PATH plus an explicit `basis` sibling** —
the consumer reads one field and *learns from the basis what it holds*, and can never render an enterprise total
where a custody total belongs.

### The positive instance — what right looks like

`json/portfolios/account-distribution.json` carries `meta.cottonwood_fold` with `accounts_folded=294`, a
per-model breakdown, its source key, and an **in-band statement of the never-sum law**. It is correct
*precisely because it carries its own basis marker.* A future reader needs no archaeology.

**Doctrine is not only a catalogue of defects. This is the shape to copy.**

---

## Corollary 3 — a control that can be satisfied by breaking what it guards

**The most dangerous control is one whose easiest passing route re-commits the defect.**

Live instances, all 2026-07-24:

- **I authored one.** I made *"the `aua_pct` rows must sum ~100"* a binding gate condition. It was already false
  (90.1%), and the intuitive way to make it pass — repoint site 2's denominator at `gold_total` — would have put
  the snapshots back on the gold basis while the headline served the held cert. **A basis substitution inside the
  artifact set the design exists to protect, reading GREEN on my own criterion.** Caught by the implementer
  (`0.4.0_DS`) refusing the shortcut and naming it, not by the two of us who wrote and ratified it.
- `keys_staged: 11` — a **hardcoded heredoc literal**; answers "did the code run," never "did 11 keys land."
- A cottonwood-fold check reading *"a 07-24 version appeared"* — would have **passed on the worst outcome**
  (a producer regenerating without the fold, silently dropping 294 accounts).
- A retry-net sweep test that **mocked a predicate the new sweep never calls** — would have passed against a
  sweep that did nothing.

### The remedy: a criterion that names its own hazardous passing route

From `0.6.2_AE_PartnerETL~A`, adopted as a pattern:

> *"Do not change the site-2 pct denominator to make percentages sum to 100. If that is ever wanted it is a
> separate argued gated change, never a side effect of closing an acceptance item."*

**Write the forbidden shortcut into the control.** It costs one sentence.

Prefer **differential** invariants to absolute ones: *"`sum(rows)/denominator` is IDENTICAL pre/post
(90.03% → 90.03%)"* fails if anything re-bases and does not require a number that was never true.

---

## Corollary 4 — the thing you believe happened, didn't

Six instances, one day, and **none announced itself**:

| What was believed | What was true |
|---|---|
| the excusals fix was deployed | committed + pushed, **never staged** — inf chain silently dead **6 days** |
| an S3 stage would deploy AC5 | first-boot-only pull; the stage is **inert** until instance replacement |
| the mutation run found nothing | the grep matched the script's own `OK:` stdout — **six well-formed lines carrying no information** |
| the sweep test covered the sweep | it mocked a predicate the sweep never calls |
| `git push` ran | **absorbed into a message body**; the sender re-ran it without knowing why |
| a fix "fixed the cliff" | two sibling scripts carried **no hold at all** — the cliff was already the status quo |

**Every one was caught by a control failing, or by someone grounding a premise instead of assuming it. Not one by
being careful.** Cross-reference: `CONTROLS_OVER_CARE.md`.

**Corollary to the corollary:** *only the loud ones scar.* A silently-eaten tool call, an unstaged artifact
nobody depended on that day, a stub that passed a freshness check — leave **no trace**. So historical incidence
is **UNKNOWABLE**; never quote an observed count as a rate. `1 of 25` is a floor with an unknown ceiling.

---

## What this obligates

1. **Emitting a value?** Emit its `basis` and its provenance beside it, in a field rejectable **without
   heuristics** — never a value that could be mistaken for the trustworthy one.
2. **Writing a gate condition?** Ask *"what is the easiest way to make this pass?"* If the answer re-commits the
   defect, the condition is wrong. Name the forbidden route inside the criterion.
3. **Modelling a state?** If "we do not know" has nowhere to go, the model is incomplete. Add the state; do not
   widen the predicate.
4. **Two producers of one quantity?** Decide the basis **once and carry it** — a shared resolver returning
   `(value, basis)`. Re-derivation at each consumer *is* the defect generator.
5. **A control inherits the scope it was written in; a change does not.** Enumerate the scopes a change can
   reach and carry a control per scope. An un-exercised scope is named **UNCOVERED**, never silently passed.

---

## Provenance

Instances contributed by `0.6.2_AE_PartnerETL~A`, `0.4.0_DS_ClientPlatform`, `0.7.0_AE_CloudOps`,
`0.4.0_DE_ClientPlatform`, `2.0.0_SA_COO`, `0.0.0_AB_MSTR`, and this desk — **most of them found by the agent
implementing or verifying someone else's ruling, including mine.** The pattern was visible only because each of
them reported the awkward thing instead of routing around it.

Related: `docs/doctrine/CONTROLS_OVER_CARE.md` · `docs/references/INCIDENTS_2026-07-13.md` ·
`docs/architecture/MDPF_REVAMP_GLOBAL_COUNT_CLOSEOUT.md`
