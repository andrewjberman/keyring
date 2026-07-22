# 0.4.0_DS_ClientPlatform — session 1521-1755Z — HELD-lane carrier repair + Cottonwood proposal

**archetype:** MIXED
**secondary_archetypes:** DIAGNOSE, SCRIBE, VALIDATE

**Window:** 2026-07-22 ~1521Z (session reset / reinstantiation) -> ~1755Z.
**Prior log:** `2026-07-22/p0_global_headline_basisB_and_three_sibling_defects.md` (pre-reset).
**Standing mode:** HELD on MDPF (Andrew ~1408Z; CTO 151655Z fabric-wide; re-affirmed 163007Z —
a priority statement does not authorize execution ahead of the sovereign's own 1552Z gate).
**No MDPF work started. Nothing deployed, staged, published. Co-sign remains 0 of 3 by design.**

## Summary

Resumed a reset lane and spent the window on **carrier repair** — the class the R1-R12 sweep
named — then took an Andrew-direct Cottonwood task read-only. Eight commits, all record or prose;
**zero behaviour changes shipped.** Two sovereign orders arrived mid-window and both were executed
(dirty-tree resolution; Cottonwood proposal). Four material corrections issued to other lanes, and
**four errors of my own found and recorded**, two of them by instruments rather than by care.

## Work completed

| # | Item | Evidence |
|---|---|---|
| 1 | Startup: serial file (LD-0290), register, watcher confirmed LIVE | Monitor task `b28ipqbgh` delivered into context — consumer-side proof, not `ps` |
| 2 | Lane had **no handoff on disk**; wrote one | `a372f05ee` |
| 3 | **§7f defect in MY OWN prepared audit wiring** — marker is a hardcoded 2-key dict | `c138e7f58` |
| 4 | STOP block on the diff itself + stale approval marked SUPERSEDED IN PART | `930d85108` |
| 5 | inf puller: docstring + `--help` described a 17a violation as the design | `9176d5773` |
| 6 | eclipse puller: `--date` fabrication prohibition carried IN THE SCRIPT | `2e3910270` |
| 7 | Dispatch tree preserved as applyable patch (round-trip proven) | `bfcc9e7c7` |
| 8 | **Dirty dispatch file REVERTED** on Andrew ~1712Z | tree==HEAD==DEPLOYED `b4ace664c4427e09` |
| 9 | Cottonwood total-AUA proposal (Andrew ~1735Z) | `0ecf2139b` |
| 10 | Proposal SUPERSEDED IN PART after Andrew ~1747Z correction | `00511f9ce` |

## Findings issued to other lanes

- **0.6.2** — 07-13/14/15 is a **real eclipse feed gap, not a producer artifact** (missing partitions
  match declared honest-Nones exactly; `07-03` is the observed July-4 holiday, NOT a gap). Warned of
  an **opposite-axis date collision**: the same strings mean ABSENT in my eclipse deliverable and
  PRESENT in the 49F legacy-vs-serve-real list. They confirmed the trap worked and independently
  matched my 7 dates on their table — my non-mergeable caveat **resolved**.
- **0.7.0** — do not land my wiring as prepared; Control 5 (synthetic third firm must be NAMED in the
  marker) accepted as an **apply precondition**. Later caught that their carrier held the doctrine but
  **not the apply gate**; they landed it in two carriers `@f9f24312a` (verified by me: 3/3, neg 0).
- **COO** — R1 carrier verified on disk rather than accepted; later flagged the **uncarried** apply
  gate to them as trigger-keeper (recorded as cell (3) UNCARRIED, re-derive at fire time).
- **CTO** — **R15's premise clause is false**: `134926Z` reached a commit at **13:54:05Z**
  (`e552b6af5:29`), 3.5h before R15 landed 17:21:03Z. Proof is the event R15 says it could not
  survive — I ran that `git checkout` and the approval survived because it was committed.
- **DE** — their `Cash Equivalent` blocker **inverts** (below). Confirmed by them `@93dd76ef8`.

## Errors of my own — recorded, not buried

1. **`git stash` in a shared worktree** — BLOCKED by the gate. I reached for a global mutation to
   answer a local question **while working on a shared-worktree hazard**, one message after COO
   broadcast narrow-pathspec discipline, having spent the hour writing that care is not a control.
   **The gate caught what my care did not.**
2. **~93% -> ~72.6%** — I used 0.6.2's single-model $30.99M as the whole modeled slice; the real Opal
   subtotal is $125,618,015.02 across 6 models. I labelled it attributed-not-adopted and hedged the
   sentence and it was **still wrong**: *attribution is not a substitute for asking whether a quantity
   is the same KIND of thing as the one you need.*
3. **Near-miss: 0 of 911 accounts** — nearly reported catastrophic conservation failure; it was an
   **ID-space mismatch** (`account_id` bare int vs `AccountID` `z09`-prefixed). Correct key gives
   **906 shared, 99.4%**. DE made this error two hours earlier in the same file, opposite sign.
4. **Fabricated `Z` markers** — `git log --date=format:"...Z"` renders each commit's OWN offset, not
   UTC. It showed R15 four hours early, inverting the causal order. Correct form:
   `TZ=UTC git log --date=format-local:`. Sibling of the `aws s3 ls` trap — there the tool omits the
   marker; here **I stamped a false one myself**, twice in five minutes, mid-correction about vintages.
5. **My §5 model leg would have REBUILT `dim_model_portfolio`** — I reasoned up from silver because
   that is where I began measuring and never asked whether the roll-up already existed.

## Compiler Tools

| Tool | Invocation | Result | Note |
|---|---|---|---|
| `comp-grep` | `"second post-flip cycle"` | **PASS (misleading)** | 0 matches / 23,081 files — a **true 0 on the wrong pattern**; record says "SECOND". Needed a positive control to distinguish from an absent carrier |
| `comp-grep` | `"post-flip"`, `"audit wiring"` | PASS | located R1 at `MDPF_CONSOLIDATED_PLAN:185` + `LD-0330:884` |
| `comp-grep` | `"134926Z"` | **PARTIAL** | returned 8 files at 17:19Z vs COO's 9 at 17:23Z — **not an instrument gap: R15's own commit created the 9th between us.** A count is a measurement, not a property |
| `comp-grep` | `"keys_staged"` | PASS | proved `keys_staged: 7` is 0.7.0's file, not mine |
| commit-gate | 2 `.py` files | PASS | prose-only edits, py_compile + ruff clean |
| safe-commit | 8 commits | PASS | surface-check clean; risk-reflex `!! STALE` danger map (202h) on every run |
| never-rules-gate | `git stash` | **DENY (correct)** | see error 1 |
| comp-rail | `grep` under `infra/` | **DENY -> rail-checked** | post-revert token check; no comp-tool takes a git ref or answers "does this file still contain X" |

**What worked:** the gates. Two independent blocks (`stash`, comp-rail) both fired on real hazards.
**What failed:** `comp-grep`'s clean `0` is indistinguishable from an absent carrier — **needs a
positive control every time**. `git log --date=format:` fabricates UTC markers.
**Gap found:** **`comp-grep` cannot search a git ref** (working tree only), so HEAD-vintage searches
fall off the rail entirely and require a `# rail-checked:` bypass. Candidate: `comp-grep --ref <ish>`.

## Blockers

- **AT CTO (open, asked 174821Z):** the MDPF runner **cannot read `blackdiamond/cottonwood/silver/*`
  at all**; my total-AUA base reads `silver/fact_holdings`. **Does any gold artifact carry the firm
  TOTAL, or is silver the only source?** Evidence-cited, not assumption-BLOCKED — `0.7.0` is building
  the additive grants on Andrew's GO.
- **AT CTO (open, surfaced 173721Z):** carve-out ruling on the Cottonwood BUILD. Proposal proceeded
  read-only on Andrew's later sovereign instruction; **build not started.**
- **MEASURED, NOT EXPLAINED:** `fact_holdings` (33 partitions, 06-09..07-20) and
  `fact_model_assignment` / `dim_model_portfolio` (2 each, 07-21 + 07-22) share **ZERO dates**.
  `non_model = total - model` is computable for **no date**. Cadence vs backfill vs schedule —
  undetermined, not guessed.

## Current State

**Lane HELD, at a clean seam, nothing half-landed.** Working tree clean for every file I touched;
`mdpf-daily-dispatch.sh` is byte-identical across tree/HEAD/deployed (`b4ace664c4427e09`), the audit
wiring recoverable from `bfcc9e7c7` (`git apply --check` clean, byte-identical to DE's independent
capture `6145935bd383c4fb`).

- **§7f defect UNRESOLVED and gated.** The wiring does not land until: marker keys derived from the
  world; `unaudited_firms` a first-class field (non-empty = NOT clean); **Control 5** — stage a
  synthetic third firm under `gold/mdpf_revamp/`, assert the marker NAMES it. Controls 1-4 all pass
  green on a cycle missing an entire firm. Three carriers: `930d85108` (diff), `f9f24312a` (0.7.0,
  two), COO's fire-time checklist. **All retire at apply; the durable fix is the firm REGISTRY, which
  also closes R13's publisher (`PUBLISH_MAP` 9/9 with Cottonwood never served).**
- **Cottonwood proposal `00511f9ce`:** model leg WITHDRAWN (read `dim_model_portfolio`, do not
  re-derive). Standing: the 0824 identity (`dim_mdpf_aggregate_aua_timeseries.py:323-327/597-600/
  611-614/621`); `.fillna(0.0)` at `:327` hits **0.00% of 7,086 rows — never fired**, so mirror the
  IDENTITY and re-decide nulls; **cash IS in the $458,114,003.10 total** (1,428 rows, $15,232,656.26,
  3.33%); the 4,328 MV-null rows are wholly empty (`Unaccrued Market Value` + `Accrual` both null) so
  **assert an invariant, not a null policy**; `fact_holdings_s2` is a 5-row BD **section-2 footer**.
- **Eclipse 06-01/07-01/07-13/07-14/07-15 = PERMANENTLY UNFILLABLE.** All 4 consumed endpoints are
  current-state; date params exist only on `/auditlog/*` across 493 paths. Disposition is
  **record-and-move-on, never a fill path.** `pull_eclipse_portfolios.py --date` **fabricates** —
  prohibition carried in the script `2e3910270`; **I have not run it and will not.**
- R9 + R11 acknowledged as binding this lane on resumption.

## Next Steps

1. **[1.0.0_SA_CTO]** rule the Cottonwood build carve-out; answer the gold-vs-silver total-AUA read
   path; consider the R15 premise amendment (substance stands, one clause false).
2. **[1.0.0_SA_CTO / 0.4.0_DE_ClientPlatform]** the **zero-date-overlap** blocker — no daily series is
   derivable until the two legs share dates. Mechanism undetermined.
3. **[0.7.0_AE_CloudOps]** consider the in-SCRIPT comment beside the marker block — the only carrier
   that outlives the flip; all current ones retire at apply.
4. **[0.4.0_DS_ClientPlatform, me]** on hold-lift + Cottonwood fold: producer-validate leg, then
   hand-run `mdpf_revamp_count_source_audit.py` against the POST-Cottonwood set, reporting verdict +
   coverage fraction incl. firm axis **in the limb itself** (R10).

## MCP traffic

~14 messages handled. Significant: Andrew-direct x2 (~1712Z dirty-file order; ~1735Z Cottonwood
task, both relayed under his command) · CTO scope ruling + R15 + the `dim_model_portfolio`
correction · COO cascade / fence / URGENT eclipse prohibition / un-strike · DE Andrew relays +
confirmation `@93dd76ef8` · 0.7.0 ACK + two-carrier fix · 0.6.2 grounding confirmation.
