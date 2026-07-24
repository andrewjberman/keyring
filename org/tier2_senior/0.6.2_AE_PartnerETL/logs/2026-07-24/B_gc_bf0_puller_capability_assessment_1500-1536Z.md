# 0.6.2_AE_PartnerETL~B — GC-BF0 puller capability assessment (1500–1536Z)

**archetype:** VALIDATE
**Serial:** `0.6.2_AE_PartnerETL~B` (PID 38992) · Monitor `bmj0upuva` · session `2bc0671a`
**TO:** MDPF_3FIRMS.GC-BF0 @3b9ea142e (+ CVO addendum @0a99ec058, CTO scope ruling 152449Z)
**Commits:** `a8203a9b2` (assessment), `6cd7e2ded` (egress question named) — pushed

---

## Current State

Lane `~B` spawned, registered, watcher armed, TO delivered and executed to completion inside ~35 minutes.
**GC-BF0 is COMPLETE and sitting at CTO's gate** (reported 153432Z, COO CC 153458Z).

**VERDICT: both in-scope pullers `NOT-CAPABLE` — both fail (B) fidelity.**

- **Eclipse** `pull_eclipse_portfolios.py` — `--date` (:299) reaches nine label sites, zero request sites;
  `eclipse_get` (:254) has no date param; all four endpoints are literal current-state paths. The sentinel
  writes `"date": date_iso` (:376) — the artifact self-certifies a false vintage.
- **SmartX** `wsb_49f_smartx_model_aua.py` — `--date` (:281) terminates in exactly two places: the S3 key
  (:247) and the **`as_of_date` DATA COLUMN** (:168/:190/:202). This is the more dangerous shape: the false
  date is stamped into the very field a content-side check would read.

**The collection order (~1509Z) cannot be executed as written** — it would land run-date data under 22 target
keys at exit 0 and pass Andrew's visual smoke test. COO's 151103Z read was right and the source bears it out.

**The one good result:** `2026-05-21 INF = 399 accounts` is recoverable from our own retained S3 object
version (`u1V7X3xHgkPAPChJhpyh1Hk50aOWLAgO`, 2026-07-08), corroborated across six concordant versions. No
pull, no egress, no fabrication risk. It is the only date the assessment clears — and it is the date Andrew
originally named.

## Blockers

**NONE.** Nothing pending at Andrew from my lane. One decision belongs to CTO (whether to pursue Eclipse
`/auditlog/*`, the only date-bearing paths in the vendor catalog) — **named, not probed, not recommended**;
it would need Andrew's per-use word since Eclipse is not on the standing egress lift list.

## What I did NOT do

- **Zero vendor calls** — neither Eclipse (not authorized) nor SmartX (authorized but unnecessary).
- **Zero bytes written** to any bucket. Every probe read-only.
- **NEVER#4 affirmed** — no ad-hoc gold run.
- **Cottonwood untouched** — not assessed, not re-derived, not probed. (Used *only* as a control corpus to
  test my own search pattern, which is instrument-validation, not assessment. Stated in the report.)
- **Did not re-derive** the 22 dates or the firm-leg classes — consumed DS~A's W-1 measurement.

## Two defects I found in my OWN instruments (the reason this log matters)

1. **The `params=` blindness.** My first date-param search found 0 hits across 25 bronze pullers — and it
   would have "confirmed" Eclipse was clean. It found nothing because **no puller in the estate uses
   `params=` at all**; the estate passes dates in request *bodies*. The corrected pattern found cot's real
   `startDate`/`endDate`/`asOfDate`, proving it discriminates. *A pattern that finds nothing anywhere is not
   evidence of absence — it is an untested instrument.*
2. **The dict-lookup hole.** My first recovery predicate tested `new[date] is None`, which **silently skips
   dates absent from the axis entirely**. It returned a confident `0 recoverable` and would have buried the
   399. Caught only because the arithmetic did not close (429 non-null vs 407 shared). *A retrieval that
   cannot tell "null" from "not present" is the same failure as a puller that cannot tell D from the run date.*

Both are recorded in the deliverable, not just here — they are the TO's own subject matter turned inward.

## Incidental correction banked

The 22 dates on the legacy 49F axis but absent from the current one are **market holidays** (Thanksgiving,
Christmas, MLK, Good Friday, Juneteenth, Labor Day …) — each carrying a **non-null count**. The legacy axis
was holiday-polluted; the revamp correctly replaced it with a trading-day axis. Supports the addendum's
**429-not-447** instruction, and means legacy counts on non-trading days were never real observations.

## Compiler Tools

| Tool | Invocation | Result | Value |
|---|---|---|---|
| `comp-which` | "which pullers feed the SmartX 49F / Eclipse INF count axis" | **NO CURATED RULE** — top score 0.44 of 68 tools | Correctly refused to guess and said so loudly. Routed me to `comp-grep`/`pipescript` instead of inventing a match. **Coverage gap worth noting: no rule maps a "which puller feeds axis X" question.** |
| `pipescript` | `--list`, `smartx`, `mdpf` | 27 threads; named the 4 MDPF feeders + 5 SmartX resources | **The highest-value call of the session.** Gave me the whole producer→served→frontend chain in one read, incl. that `smartx-rest-pull`'s source is deploy-only. Vintage header (39d old) correctly flagged its own staleness. |
| `comp-glob` | `**/*eclipse*` | 27 files | Located `pull_eclipse_portfolios.py` immediately. |
| `comp-grep` | `-l 'smartx'`, `'MDPF_ASSETS.012\|MDPF.012'` | 16 files / 5 files | **Caught my escaped-pipe error explicitly** (`Python re treats \| as literal`) and warned the 0-result might be the pattern, not a real absence. That warning is exactly the control this session was about — it prevented a false negative. |
| `comp-to` | set session TO_ID | OK, race-free per-session | — |
| `safe-commit.sh` | ×2 | surface-check OK; risk-reflex CLEAN, **denominator stated (1 file vs 1511 danger nodes)** | Printed a measured denominator rather than a bare pass. |
| raw `aws` (s3 ls / s3api) | bucket + object-version enumeration | operational/data-plane reads | Off-rail by the graph-presence principle (object-version history is not modeled by any comp tool). This is a **genuine coverage gap**: no comp tool answers "what do the retained versions of this served key contain?" — which is precisely where the session's one positive finding came from. |

**Gap worth routing:** the version-history recovery check (RC-1) has no tool. It found a real, verified,
zero-egress repair path that every existing instrument missed. If counts can go missing from a served
artifact and survive in its own version history, that question will recur.

## Next Steps

1. **[CTO]** Gate the assessment. Two live decisions: whether to land 05-21 = 399 via RC-1, and whether to
   seek Andrew's word on Eclipse `/auditlog/*`.
2. **[me, if routed]** Execute the RC-1 landing of 2026-05-21. Available now.
3. **[CVO]** RC-1 is written to be runnable without me, with its negative cases exercised (5/5 Eclipse
   dates flagged absent, 2/2 weekends, 21/21 49F, positive control 05-20/05-22 present, 0 disagreements
   across 407 shared dates).
4. **[COO/CTO]** The `as_of_date` warning must reach whoever writes the next acceptance criterion — that
   field is puller-stamped and is not a control.
