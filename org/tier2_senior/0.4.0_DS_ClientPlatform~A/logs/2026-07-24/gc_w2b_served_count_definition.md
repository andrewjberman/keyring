# GC-W2b — establishing what the served count actually counts

**archetype:** DIAGNOSE
**Agent:** `0.4.0_DS_ClientPlatform~A` · 2026-07-24 · **TO:** `MDPF_3FIRMS.GC-W2b` @`e4a2724577` · committed @`4d0831382`
**NOT PUSHED** — Andrew-direct ~1600Z: pushes are Tier-1 only, COO is primary push operator. Commits unchanged.

## Origin

My own GC-W2a 0.04% finding created this TO. CTO accepted the tractability verdict for the reason I gave rather
than the easier one — naming **the 0.04%, not the 0-of-22**, as binding — and gated the decouple on a definition
that reproduces the served figure **exactly**.

## Outcome — split across the seam, and the split is the answer

- **Side A (frontier stamp): `reproduces-exactly`.** Definition source-confirmed at
  `dim_mdpf_account_distribution.py:211-240 @34e38a8e5` and measured exact on **four independent quantities**
  (count 7,026; all 5 per-model cells; `total_aum` 1,399,317,335.17 **to the cent**; max 33,630,390.73).
  The `$1,000` floor (`:89`) was **independently bracketed from the data** to (999.17, 1036.06] — source and
  measurement agree without either being assumed from the other.
- **Side B (served-real legacy import): `NOT-DERIVABLE-FROM-RETAINED-SOURCES`.** Ten variants tested; closest
  off by 1 on one date and by 10 on the next — a different quantity, not a residual.

**Why the split matters:** the two sides map exactly onto GC-W2a's two hole generators. The **open-ended** one
(build-gap/frontier) is Side A — now solved. The **closed** historical set is Side B. So the half that keeps
regenerating the complaint is the half where an exact definition now exists.

**I did not take the named shortcut.** Reporting `open` at −3 would have passed every tolerance we own — it was
my own 0.04% defect wearing this TO's hat. The real definition was three predicates away and is exact.

## Sum vs distinct — resolved on the discriminator COO named

CTO and `0.6.2~B` measured the same equality on INF and drew opposite conclusions. Resolved: **the field IS the
sum** (`dim_mdpf_aggregate_aua_timeseries.py:1732-1734 @3efc9dc6d`, plus 407/407 measured). INF's
`distinct == sum` is a property of INF's *data*, not of the field — which is why INF alone could never
discriminate. Divergence by firm: 49F **0** (by construction, `:232`), INF **0**, **cottonwood +147**, global
**+147**. So the +147 is the field working as designed, and Global "Count" exceeds distinct funded accounts by
~1.8%. Whether SUM is the *right* convention is a product question at CTO's gate — quantified, not ruled.

**Premise correction:** `294` was attributed to my W-1 and **does not occur in it** (zero occurrences). It is
cottonwood's `total.active_accounts_count`; the distinct funded figure there is **291**. Flagged rather than
reasoned from — a number attributed to a measurement that never made it returns as corroboration otherwise.

## New finding — as-of semantics

`:214-215` resolves roster and valuation partitions via `_latest_date()` **independently**, so the stamped
value's as-of is *"whenever `account_distribution` last ran"*, not the axis date it lands on. I **tested and
rejected** the T-1-by-design reading: `DEFN(07-22)` = 7,038, but the served 07-22 cell is 7,026 = `DEFN(07-21)`.
Two independent clocks, unbounded skew. This compounds GC-W2a's build-gap finding: dates that get nothing, and
dates that get something whose vintage is not the date's.

## Compiler Tools

| Tool | Command | Result | Notes |
|---|---|---|---|
| `comp-grep` | `comp-grep account_distribution data/mdpf` | PASS — 12 matches / 5 files, 51 scanned | Located `dim_mdpf_account_distribution.py` — the producer whose source carries the whole definition. This was the pivot of the TO. |
| `comp-which` | *"which gold script writes gold/mdpf_revamp account_distribution.json"* | ROUTED | Correctly flagged its own **tied top scores** ("the order is NOT a ranking") rather than presenting a false #1; I fell through to `comp-grep` as it suggested. |
| `comp-blast` / `comp-pipescript io` | (GC-W2a, same producer family) | — | Not re-run; no new script surface touched this pass. |
| `comp-validate` | *not run* | **N/A, stated** | Read-only definition work; no gold script run, no artifact produced by me. |
| `comp-surface-check` | *not run* | **N/A** | Deliverable + log + TO status only; zero portal files, zero producer edits. |
| `s3api` / `list-object-versions` | 4 `account_distribution` keys, 2 silver feeds × 11 partitions, object versions | PASS | Explicit-Z throughout; `aws s3 ls` avoided. |
| `pandas` | roster ⋈ valuation reconciliation across 11 dates | PASS | The exact-reproduction test and the 10-variant negative. |

## Grounding posture

Every element of the definition carries `file:line @ commit-ish`. Denominators printed. Two items left
deliberately ungraded-up: **whether SUM is the right convention** (product, not mine) and **what the legacy
producer counted** (UNDETERMINED — Side B's source is the legacy chain and GC-W2a established the legacy
artifact is its only surviving record).

## Next

Committed, **not pushed** — handing to COO per the 1600Z push directive. CTO gates the decouple on this; CVO
takes validation.
