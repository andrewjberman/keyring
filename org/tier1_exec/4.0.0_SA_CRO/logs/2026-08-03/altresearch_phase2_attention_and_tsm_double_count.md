# OPAL_ALTRESEARCH Phase 2: attention-over-time shipped -- and its parity control caught a Phase-1 double-count

**archetype:** IMPLEMENT
**secondary_archetypes:** VALIDATE, DIAGNOSE

**Agent:** 4.0.0_SA_CRO (Chief Research Officer, Tier-1)
**Window:** 2026-08-03 ~15:24Z (session start) -> ~15:45Z
**Commits:** `7e302a890c` (authored 4.0.0_SA_CRO)

---

## Summary

Startup protocol completed clean (details below). Inbox empty, no pending TOs, the fabric is on
the MDLP_MONPUB fire and the CRO has no role in it. The addressable next step was the one my own
07-31 log named and deferred: **Phase 2 attention-over-time**, gated on "the dating standing
unchallenged" -- it stood 3 days, so I opened it.

Delivered in one commit: the Phase-2 analyzer + its two artifacts, **plus a Phase-1 correction
its parity control forced** -- the shipped build queue double-counted TSM (said 10 mentions; the
corpus contains 5).

---

## What landed (`7e302a890c`)

**1. `bin/build_attention.py`** -- per-meeting mention timeseries + per-security trend classes.
Method choices stated in the docstring so a reader audits rather than inherits:
- Matcher IMPORTED from `build_mentions.py` -- one dictionary, one set of adjudicated false
  positives, one parse. Nothing re-derived.
- Halves split BY MEETING COUNT (14/14), both denominators printed with char totals
  (573,339 vs 701,160 chars -- H2 is ~22% longer, context for judging rate moves).
- Trend classes DERIVED with stated thresholds (EMERGED / RISING x2 / STEADY / ONE-OFF /
  FADING x0.5 / DROPPED). Raw counts, never length-normalized.
- REJECTED adjudications excluded (CI); date-confidence carried onto every timeseries row
  (1 doc below HIGH: RT-20260512-1026, the known ORDER-only placement).

**2. Artifacts.** `analysis/attention_timeseries.csv` (278 date x ticker rows),
`analysis/attention_trends.csv` (62 securities).

**Headline (DERIVED, H1 -> H2 mentions):**
- **RISING:** ServiceNow 22->58, Workday 6->51, Netflix 11->28, Apple 6->26
- **EMERGED (0 in H1):** Tesla 0->19, Copa 0->4
- **STEADY at volume:** ASML 54->40, Microsoft 25->47
- **FADING:** Nike 50->22, Visa 14->7, Mastercard 12->6, Intuitive 13->5
- **DROPPED (0 in H2):** Home Depot 12->0, UPS 10->0

**3. The Phase-1 fix.** The parity control (Phase-2 totals must equal the independently-produced
build queue's `n_mentions`) failed on exactly one ticker: TSM, queue 10 vs mine 5, factor of
exactly 2. Mechanism source-confirmed: `analysis/etf_firm_materiality.csv` carries TSM on TWO
rows (ADR line, IDVZ, rank 48; ordinary line, PFOE, rank 59); `load_dictionary` emitted a target
per ROW while `main()` keys hits per TICKER -- every duplicate-row ticker counted the same text
once per row. Raw recount both channels: 5 true occurrences. Blast radius measured before
fixing: 165 unique tickers in 166 rows, **TSM the only duplicate**. Fix: duplicates MERGE at
load (min firm_rank, summed weight, unioned funds -- in speech the share class is
indistinguishable, so one security). Queue regenerated: TSM 5 mentions / rank 48 / weight
1.3679 / IDVZ,PFOE; coverage denominator now honest at 165 matchable. Parity re-check after
fix: 62/62, 0 mismatches.

**The control note worth banking:** the parity check is discriminating BECAUSE it failed once on
a real defect before passing -- it is not an instrument that cannot fail. And the defect
direction matters: my accidental-overwrite in `count_mentions` produced the CORRECT number while
the shipped Phase-1 path was wrong. Two independent implementations disagreeing is what surfaced
it; neither alone would have.

---

## Startup protocol (compressed)

/watcher: registered (PID 5856), Monitor `b1x5kvwla` armed and `TaskOutput`-confirmed running,
no orphans (`watcher-status` + ps both empty first), LD-0290 serial file written. A.3: 94/94
comp-tools resolve AND the exercise line ran a real forwarder. Launcher's loop-arming block
reported UNRECOGNIZED for this serial -- **role-mapping gap for 4.0.0_SA_CRO in ajb.ps1 warned
to MSTR by MCP same turn** (152600Z), zero crons armed regardless. A.2 audit-archive-invoker:
rc=1, 1 finding -- `org/tombstone-gate-audit.log` uncovered by MANIFEST (persists from 07-31;
prints at every exec startup, owner 0.7.0_AE_CloudOps will see it; not pinged mid-fire).
07-31 commits confirmed integrated on origin/CLOUD.

---

## Compiler Tools

| Tool | Purpose | Result |
|---|---|---|
| `comp-which` | A.3 startup exercise (resolution is not execution) | **PASS** -- 94/94 resolve AND a forwarder RAN |
| `python .tools/audit-archive-invoker.py` | startup A.2 | **rc=1, 1 finding** -- tombstone-gate-audit.log uncovered (known, owner will see) |
| `.tools/commit-gate.sh` (via safe-commit) | pre-commit on 2 `.py` | **PASS** first try this session |
| `.tools/safe-commit.sh -F` | 1 commit, LD-0276 -F path | **PASS** -- surface-check OK (5 files vs 6 surfaces), risk-reflex CLEAN (5 files vs 1672 danger nodes, denominator printed) |
| `comp-surface-check` (via safe-commit) | critical-surface screen | **PASS** -- no critical surface touched |

**What worked:** the parity check against the independently-built Phase-1 queue -- a genuine
control, exercised in the failing direction on TSM before it passed.
**Gap (repeat from 07-31, still true):** no estate instrument detects a parser or counter
silently mis-counting; both the 07-31 parser defects and today's double-count were caught by
hand-chosen cross-checks. That is still care, not a control.

---

## MCP traffic

1 outbound: WARN to `0.0.0_AB_MSTR` (launcher role-mapping gap, 152600Z). 0 inbound.

---

## Blockers

**None.** Residuals unchanged: 2026-07-13 transcript unretrievable; 2026-05-12 second recording
missing (its doc stays LOW date-confidence and is flagged per-row in the timeseries);
Teams-retention decision at Andrew; m365 gateway paging/`$select` architecture item at CTO.

---

## Next Steps

- **[4.0.0_SA_CRO]** Phase 2b candidates, not started: attention-vs-position-change overlay
  (needs position history), and a per-security first-mention -> firm-weight lead/lag read.
  Both want Andrew's steer on which is decision-useful before spending the corpus's credibility.
- **[Andrew]** Standing: Teams transcript retention decision (April meetings inside the
  deletion window as of 07-31).
- **[integrators]** `7e302a890c` + this log are committed on CLOUD, not pushed (lanes commit,
  integrators push).
