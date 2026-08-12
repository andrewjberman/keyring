# W4b semantic authoring tranche 1 + guard repair — CVO~Z session
**archetype:** MIXED (VALIDATE + IMPLEMENT)

**Agent:** `3.0.0_SA_CVO~Z` · **Window:** 2026-08-12 17:01–17:45Z · **Commit:** `32e1ea7781`
**Scope:** OPAL_ANALYST only (Andrew-direct ~1545Z @504f4d7ae0 — site Z is mechanical-work only).

## Startup

`/watcher` armed (Monitor `bkjmypmwb`, confirmed `running` by `TaskOutput` — the only probe that
observes a consumer). Registered PID 17220; identity clean, no peer, no orphan. XXX.md 1b A.1/A.3/D/E
complete; PATH 91 of 97 comp-tools resolve bare and the EXERCISE line confirms a forwarder RAN.
**Zero crons armed.**

**Self-caught defect:** my cwd lingered in the inbox `read/` dir across calls, so the first startup
batch created `org/mcp/sessions/` and `.comp-graph/` *inside the inbox*. Removed; redone at root with
absolute paths. Exactly the Step-1a hazard — a lingering cwd silently retargets relative writes.

## Findings surfaced (none adjudicated by me)

1. **Launcher carries the BASE-CVO 1b-F row.** It reads "MAIN-fabric verify ONLY" and "SYSPARITY IS
   NOT YOURS — moved to `3.0.0_SA_CVO~Z`" — the serial it names as recipient is *me*. XXX.md's actual
   `~Z` row says the opposite. **Did not adjudicate**; armed zero crons (correct under every reading),
   ran the parity check once as a read. CTO~Z ruled: XXX.md's `~Z` row binds, launcher is a copy
   error, handling correct.
2. **`comp-system --check` → `06 STALE`**, `file_count` unchanged at 210, only `max_mtime` moved —
   the signature of a checkout, not content drift. CTO~Z named the pull (CLOUD→SITEZ parity merge
   carrying `a737956b19`) and dropped it for this session.

## W5 prep (delivered to CTO~Z, all adopted)

- **F-3's ruling is not executable as written.** `certification.json`'s `verdict` is **str in 12 of 14,
  dict in 2**, three tokens across two container shapes. → CTO ruled a W5 verdict normalizer that
  RAISES rather than defaults.
- **The void is filename-encoded, not field-encoded, in 1 of 2 cases.** Reported as 1-of-2 not 2-of-2
  because my own matcher matched the substring `state` inside `seal_state_at_signature` — a spurious
  hit I ran a control on. → F-3 now prohibits a `certification*.json` glob.
- **P1's first half has no substrate at artifact grain: 0 of 13 certified consumables carry any
  machine-readable key/artifact field** (3 schema variants, no key slot in any). Key totals appear in
  prose in 2 of 13; **1 of 18 subjects has a persisted key enumeration**. Expansion is not estimable
  from entity count (722→4 vs 19→4, a 38-fold spread). Measured floor of the key universe: **≥741**.
- **Build-Ladder rung 2: `enumerate_set.py` already exists** (0.5.0's w1_prep) — read, not cited. P1's
  first half is a RUN of an existing instrument across ~12 units, not a build.

## W4b delivery — 18 cells, 3 complete entities

`SEMANTICS_CVO_PLANE_BC.json`, entities advi.12/13/15, all six reserved fields each. Guard **CLEAN
(both limbs)**. Authority: the run's own `DOMAIN_BAR_AND_AXIS.md` §4 exclusion 1, which reserves those
six fields to me by name, committed before measurement. **SoD: CTO~Z certifies W4b** (ruled 172229Z) —
I do not sign a rectangle I authored the majority of.

Semantic content of note: advi.12 self-declares `advisor_tagged_full_nonadditive` (summing AUA across
roles double-counts); advi.13's tax axis IS additive, checked arithmetically and reconciling to
advi.12's independent firm total — **two artifacts on one page with opposite aggregation rules**;
advi.15's NMNC/NMEC grounded at their definition site, a binary invariant whose **zero means NO DATA,
not NO NEW MONEY**. `data_as_of` 4 trading days behind — calendar resolved via `lib/trading_calendar.py`
BEFORE writing, and recorded as an **observation, explicitly not a staleness verdict** (NEVER#1).

## The guard repair — my own defect, ablation-measured

`semantics_payload_guard.py`'s second limb read the plane split only from `field_planes`. **W4b
declares it under `plane_ownership.planes_B_C_certifier` — 1 of 7 runs, and it is the 290-cell one.**
So the limb never ran there, and the status line printed `axis_declaration.json ABSENT` about a file
that was present and did carry the split.

```
mutant: advi.07 (Plane-A 0/4 → all 10 cells UNMEASURED) filled on all 10 fields
  axis limb ACTIVE  →  4 AXIS-LIMB DISAGREEMENT violations   rc=1  DO NOT SHIP
  axis limb BLINDED →  "CLEAN -- safe to merge"              rc=0
```

Fixed three ways: resolve from either key and **name which**; separate ABSENT / DEGRADED / ACTIVE
(never report a present-but-unparsed file as absent); and **the verdict line now carries the assurance
it bought** — a degraded limb no longer prints "safe to merge". That last is the half that let it hide.

**`comp-find` denominator: my guard is the ONLY code reader of either key** across 25,678 files — which
is why a two-schema divergence across 7 runs went unnoticed. `cma`'s axis file records its schema was
*"copied VERBATIM from portfolios W0"*: hand-copied propagation, so the independently-authored run
diverged. **Same defect shape as the `verdict` str/dict split — two instances in one tree in one day.**

## The coverage probe that produced four false findings — and why that is the finding

Materialised `s3://opal-data-bd/platinum/firm/` (15 keys, no `--query`, no `head`) and diffed against
the 15 declared locators. Raw: 5 declared-but-absent, 3 present-but-undeclared.

**4 of the 5 were my error.** advi.01/03/08 are INFLECTION-scoped (`getInflectionActivityScan` etc.) —
I probed `bd`, the wrong bucket. **A 404 in the wrong bucket is the wrong question asked cleanly**, and
I cannot fix it by probing the right one: **NEVER#2 forbids it.** advi.05 is genuinely absent and
**reproduces the author's own measured cell** (theirs first, 23,882 keys materialised with a positive
control) — recorded as confirmation, not a finding.

**Consequence, and it reverses my own earlier answer to COO~Z:** their worry DOES hold. My runway is
**48 cells** (18 delivered + 30 ready); the remaining **108 sit behind `serving_state`**, which is
exactly what FRONTIER blocker 1 gates. Both authors hit **one** wall, and it is estate law, not
throughput. I told COO twice it did not hold and corrected it in the same session.

3 undeclared keys flagged as **candidates, not findings** (`clients-tab-slim`, `leaderboard.prior_week`,
`employee_leaderboard` at 125 days) — same-leaf-name hazard live, abandoned-vs-superseded identical
from age alone, no action taken.

## Compiler Tools

| tool | invocation | result |
|---|---|---|
| `comp-find --name` | `rectangle.final.certified.json` | DENOMINATOR 13 of 25,665 — the certified-consumable set |
| `comp-find --name` | `enumerate_set.py`, `semantics_payload_guard.py`, `ssot_validate*` | located all three; read rather than cited |
| `comp-find` (content) | `field_planes`, `planes_B_C_certifier` | **my guard is the only code reader of either** — the finding |
| `comp-find` (content) | `NMNC` in `portal/src` | 41 hits, banded; definition site found at `[HEAD]`, grounding the category semantics |
| `comp-system --check` | one-shot, LD-0319 standing responsibility | `06 STALE`, mtime-only; surfaced, not adopted |
| `semantics_payload_guard.py` | payload × rectangle, + 3 mutants + ablation | CLEAN both limbs; mutants rc=1; ablation proved the pre-fix false CLEAN |
| `lib/trading_calendar.py` | `expected_last_trading_day`, `trading_days_behind` | 4 trading days — run BEFORE writing any vintage cell |
| `aws s3 ls --recursive` | `platinum/firm/`, materialised | 15 keys, counted client-side — no `--query` on a paginated list |
| `safe-commit.sh` | `-F`, lane author | `32e1ea7781`, risk-reflex CLEAN (2 files vs 1,186 danger nodes) |

**Instrument failures worth carrying:** discarding stderr on `aws s3api get-object` manufactured three
"FAIL" verdicts on reads that worked. My strict-prefix lint found 2 of 3 fragments (missed
`advi.29` — locator value `"platinum (bare)"`). My first key-expansion census returned a uniform
`1.00x` across 13 units by inventing field names the schema does not have — **discarded rather than
reported**, caught because uniform tidiness across 13 independent units is implausible.

## Blockers

**NONE self-blocking.** 108 of my 174 cells are downstream of FRONTIER blocker 1 (cross-firm served-plane
enumeration, NEVER#2) — **owned by CTO~Z, surfaced, not held on.** Continuing on the 30 ready cells.

— `3.0.0_SA_CVO~Z`
