# 0.4.0_DS_ClientPlatform~A — ADVI_IDSPINE.WP-4 (dim_relationship v3, explicit carry) — 2026-08-19 22:15–22:50Z

**Archetype:** BUILD (schema change + first test coverage for a01)
**TO:** `ADVI_IDSPINE.WP-4` — ungated, deliberately independent of WP-1..3
**Commits:** `96fc16ac05` (a01 + tests) · deployed + byte-verified to `_code/`

---

## The problem WP-4 actually solves

SS6 landed a declared-stale mode earlier the same day: when `fact_fam` has no partition at the
chain date, a01 falls back to the latest vintage and sets `fam_declared_stale` **in the manifest**.

The manifest does not travel with the rows. A consumer reading the parquet saw a household
attribution and had no way to tell whether today's fam answered it or a vintage frozen weeks ago.
**That is the whole gap**: a carry that does not say it is a carry renders exactly like fresh data.

## What I built

Two columns on every row — `identity_source` and `source_as_of` — with a three-value axis:

| value | meaning | `source_as_of` |
|---|---|---|
| `fam-live` | fam answered at the chain date | the chain date |
| `fam-carried` | fam answered at an **earlier** vintage | **that vintage** |
| `self-family` | **no fam row at any vintage**; anchored on the account itself | the chain date |

The third value is what keeps the axis MECE. Collapsing "no answer from fam" into "an old answer
from fam" would have overstated how much of the book the carry actually covers.

**Rule 24 declared in the manifest rather than left implicit.** Intent: which layer answered and at
what vintage. Grain: row. The **stability frame** (postulate iv) is the one it does not pass
trivially, so it is named: `fam-live`/`fam-carried` move together the instant Schwab resumes — one
remedy, no code change — while `self-family` **does not move with them**; it clears only when the
vendor adds the account. "Resume the feed and the labels resolve" covers two of three values.

**Tail declaration (WP4-4)** with count + basis + vintage, degrading to `UNDETERMINED` with a reason
when the BD universe is unreadable — because a missing basis and an empty tail are different facts,
and a bare `0` reads as "no custodial tail" when it means "not computed".

**The BD read is best-effort and can never take the build down.** WP4-1 exists precisely so this
table builds when upstream identity feeds are unavailable; failing closed on a *tail declaration*
would reintroduce the dependency the carry exists to survive.

## Live build (WP4-1 + WP4-4), on the real carried partition

```
WARN: fact_fam DECLARED-STALE -- chain date=2026-08-18 has no fact_fam partition (latest=2026-08-10)
fact_fam date=2026-08-10 (chain date=2026-08-18): 7,202 rows; fact_acc universe 7,316
BD xref date=2026-08-18: 5,376 distinct schwab accounts (tail basis)
IDENTITY PROVENANCE: {'fam-carried': 7202, 'self-family': 119} | CUSTODIAL tail=2006 (basis 2026-08-18)
BUILD OK: 7,321 rows x 14 cols | mapped=7202 + unmapped=119 == 7321 | relationships=4365
```

The tail reconciles exactly: **1,887 fam-only + 119 self-family = 2,006**.

## Findings I carried up rather than absorbed

1. **The TO and the spec both state the carry is "as-of 2026-08-07". It is not.** The latest
   `fact_fam` partition is **2026-08-10** — 7,202 rows, a real feed day on the same 09:46Z cadence
   as 08-07 (7,186 rows) — and **7,202 is the very number the spec's own basis measurement uses**
   while its prose says 08-07. The code derives the vintage (`fam_dates[-1]`) and always did, so
   nothing was broken. But hardcoding the TO's stated date would have baked a **false vintage into
   every row of a label whose entire purpose is telling the truth about vintage.**
2. **The measured tail is 2,006, not the spec's 1,925 — different instrument.** The spec measured
   against the BD *allocation export* (bronze `allocation_390224`); I measured against silver
   `dim_account_xref`. I declared the basis and vintage rather than hand-reconciling two
   instruments into a false equivalence.
3. **WP4-1 was already satisfied before this TO started**, by the SS6 work landed earlier today. I
   only learned this from the mutant run — 7 of 8 tests fail on the old file and that one passes.
   Without the mutant control I would have reported all four criteria as delivered by this change.
4. **a01 had no tests at all**, despite being the identity spine's household-grain producer and
   having been rewritten on 2026-08-11.

## Controls

- **Mutant:** whole battery vs the pre-WP-4 file → **7 of 8 FAIL** (`KeyError: identity_source`,
  `KeyError: custodial_tail`, `KeyError: identity_source_axis`, `TypeError: unexpected kwarg
  bd_ids`). Restore verified **byte-identical** by sha256.
- **Deployed bytes:** sha256 identical, 15,921 B, positive control (6 `identity_source` hits in the
  deployed artifact) proving the search sees the file.
- **Proof instance:** `rc=0 VALID`, rc read **without a pipe**; negative controls on copies return
  `rc=1` for a removed required field and for an omitted criterion.
- A near-miss worth recording: I wrote the BD read with `bucket=rc.SILVER_BUCKET` kwargs that
  **do not exist** on `rc.read_partition`. The `try/except` around it would have swallowed the
  `TypeError` and produced a permanent, entirely legitimate-looking `UNDETERMINED` tail. Caught by
  reading the helper signatures instead of assuming them; `_bucket_for` resolves the bucket from the
  prefix family on its own.

## Compiler Tools

| tool | invocation | result |
|---|---|---|
| `comp-find` | `--name "SPEC_IDENTITY_SPINE_FAM_RESOLUTION*"` | located the governing spec + the 1,925 tail basis at `:30-31`, `:64` |
| `commit-gate.sh` | a01 + the new test file, every iteration | PASS |
| `safe-deploy.sh` | `a01_dim_relationship.py` | DEPLOYED + VERIFY OK → `_code/`, then re-grounded on deployed bytes rather than accepted on the gate's verdict |
| `comp-pipescript` | `deployed` (via safe-deploy VERIFY leg) | MATCH |
| `proof-of-spec-check.py` | `<instance> WP4-1,...,WP4-5` | VALID rc=0, violations=0 |

**Checker gap found and reported, not worked around silently:** the artifact-coverage rule keys on
the artifact stem appearing in a **criterion_id** (`{firm}-{group}-{artifact}-{check}` DS grammar).
This TO's ids are `WP4-1..WP4-5` by its own `proof_of_spec` block, so the heuristic **structurally
cannot match however well the artifact is covered** — and all five criteria are about that one file.
Its sanctioned escape is naming the artifact in `declared_exclusions`, which risks reading as "the
artifact was excluded". I made the existing (genuine) exclusion more precise and stated inline that
it excludes the historical *re-emission* only, then reported the gap.
