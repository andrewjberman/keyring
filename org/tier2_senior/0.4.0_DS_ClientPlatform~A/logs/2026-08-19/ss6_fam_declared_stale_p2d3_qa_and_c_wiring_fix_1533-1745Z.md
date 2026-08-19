# SS6 Perishable Dispatch — fam DECLARED-STALE + P2D-3 QA (found+fixed 2 severe defects) + P3 dims — 0.4.0_DS_ClientPlatform~A

**Date:** 2026-08-19
**Task Order:** OPAL_ADVIPOINTERS.P2-DISPATCH-49F (+ SS6 dispatch, no separate TO file — COO spawn 15:33Z direct)
**Status:** COMPLETE

**archetype:** MIXED

---

## Objective

Andrew's Friday-word SS6 compression (push plan @762b06ca84 §6/§7) required today: (1) implement
fam DECLARED-STALE mode so one stalled vendor feed never freezes the whole chain, (2) run P2D-3's
QA exercise on the real S3-code path and deliver AE the measured duration that pins today's floor
cron, (3) land P3 dims (a07 home + a06 xwalk) behind that run. All three close today; the floor
cron applied live at 12:45Z UTC for tomorrow's first unattended fire.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| py_compile | `python -m py_compile <each edited file>` | PASS | run before every commit, 4 separate edit passes |
| safe-commit.sh | 6 commits today | PASS | commit-gate (py_compile+AST+ruff) clean every time |
| safe-deploy.sh | 4 deploy passes (explicit-files mode, S3-code path) | PASS | VERIFY OK / comp-pipescript deployed MATCH every time — the 08-18 log's "registry gap, degraded" note did NOT reproduce today; not re-flagged |
| comp-pipescript io | `io a01_dim_relationship.py --pipeline bd` | FAIL (known gap) | "Unknown script" — runners_49f still absent from the BD-gold registry; disclosed in the 08-18/08-19 TOs, retires at 0.8.0's NFRA_COMPTOOLS.REG |
| aws iam get-role-policy (rail-checked) | live-applied-plane reads on bd-exporter-ec2-role, 3 separate times | PASS | grounded 2 real IAM gaps precisely (Rule 22a: comp-iam is DESIRED-only, live get-role-policy is APPLIED) with zero false-positive reports; also checked cross-firm-bucket-deny's actual scope before flagging a leg, avoiding a false Deny-conflict claim |
| aws ssm send-command / get-command-invocation (rail-checked) | 6 live fires on bd-gold-layer-runner | mixed, by design | each failure was a REAL defect the exercise exists to catch (see Work Completed); the 6th fire is CHAIN OK |
| proof-of-spec-check.py | `<instance> P2D-1,P2D-2,P2D-3,P2D-4,P2D-5` | PASS after 2 fix rounds | first pass: 12 schema-enum violations (my own enum literals didn't match the schema's allowed set); second pass: 4 artifact-coverage violations (this TO's P2D-N criterion-id grammar doesn't stem-match the {artifact}-{check} heuristic — declared as an exclusion, the tool's own documented escape); final: rc=0 VALID |
| comp-system | regenerate 06_current_state | PASS | commit-gate blocked on stale system-state snapshot ahead of the proof-of-spec commit; regenerated cleanly, non-rule-bank so no STRUCTURAL-TWOPHASE override needed |

**What worked:** the rail-checked live IAM/S3 reads caught every real gap with zero false positives; the corpus-wide grep for `parents\[` found all 5 bundle-path bugs in one pass instead of 5 separate live-fire discoveries.
**What failed:** comp-pipescript io still can't see this corpus (known, disclosed, not re-raised).
**Gap found:** none new beyond the already-filed registry gap.

---

## Work Completed

### 1. fam DECLARED-STALE mode (SS6 item 1)
`a01_dim_relationship.py`: replaced the hard `REFUSED: fact_fam has no partition date={asof}`
SystemExit with a dynamic fallback — when the chain's requested date has no fact_fam partition,
build off the latest available fam vintage instead, print a loud WARN, and carry `fam_as_of` +
`fam_declared_stale` in the manifest (never silent; auto-lifts the instant the vendor feed
catches up, no code change needed). `runner_common.py` gained `read_upstream_declared_stale()`
so a downstream consumer (DS~B's D-fleet publisher) can propagate the flag verbatim instead of
re-deriving it — deliberately left un-wired into any d-tier file (D-fleet is DS~B's P4 lane).
Live-exercised in every QA fire today: `fam_as_of=2026-08-10`, `fam_declared_stale=True` against
a chain date of `2026-08-18`. Commit `f891776875`.

Flagged (not adjudicated) a live number discrepancy: SS6's text cites `fam_as_of=2026-08-07`; the
live silver frontier is `date=2026-08-10`. COO resolved this as the content-AsOf-vs-delivery-date
grain split (both true, different grains) — my dynamic derivation is correct regardless of which
figure is "right" since it always reads whatever the artifact declares.

### 2. P2D-3 QA exercise — found and fixed two severe, previously undiscovered defects
First-ever real fire of `chain_49f_entrypoint.py` on the S3-code path (not the repo tree) — this
is exactly what P2D-3 exists to prove, and it worked as designed: it broke on real defects a
repo-tree dry-run structurally could not have found.

**Defect A — shallow-bundle-path IndexError (5 files):** `chain_49f_entrypoint.py`,
`a00_dim_account.py`, `a04_dim_calendar.py`, `a05_ref_txn_classification.py`,
`a07_dim_asset_classification.py` all hardcoded a `Path(__file__).resolve().parents[N]`
repo-root assumption for their `lib/trading_calendar.py` import (or, for a05/a07, an `org/`
deliverable and a `data/black_diamond/` lib file). On the deployed bundle path
(`/tmp/advi_49f_code`, 2 parents deep) this IndexErrors before ever trying the correct
bundle-local candidate. Would have CHAIN ABORTed the very first scheduled production fire.
Fixed all 5 with a lazy repo-then-bundle candidate list; vendored 2 missing non-.py bundle
members (`ref/SCHWAB_TRANSACTION_CODE_CLASSIFICATION_20260811.json`,
`ref/etf_classifier.py`, explicit `aws s3 cp`, same treatment as the original
`POLICY_BLOCK.json` first-mint — neither is duplicated in-repo, only mirrored to S3). Commits
`11fb1edcd3`, `a9a494087e`.

**Defect B — SEVERE: c00/c01/c02 wired to a colliding project's scripts.** `_stage_list()`
invoked `c00_runner.py` / `c01_runner.py` / `c02_runner.py` under the labels "c00_flow_ledger" /
"c01_nna_canonical" / "c02_twr_daily" — but those three files are OPAL_GLDRNS.A4's wrapper
files for a completely different project (account_gains/account_performance/client_performance),
which independently chose the same C_00/C_01/C_02 casebook numbering and landed in this shared
directory. Every prior run — the 08-18 dry-run smoke included — would have reported
`CHAIN OK rc=0` while silently NEVER writing this product's own `canonical/flow_ledger`,
`canonical/nna_canonical`, `canonical/twr_daily`. Checks-pass-work-fails at maximum severity.

Escalated same-turn to CTO/COO/AE/MSTR (separate sends per the broker single-recipient rule —
an in-body "cc" delivers nothing). CTO endorsed the fix scope (161345Z): rewire c00/c01/c02 to
invoke the REAL modules (`c00_flow_ledger.py`, `c01_nna_canonical.py`, `c02_twr_engine.py`)
directly — same "module IS the live producer" pattern as a01 — explicitly scoped OUT the
colliding OPAL_GLDRNS wrapper files themselves (routed to COO as a follow-on, not today's act).
Those three real modules stage their upstream inputs from a LOCAL directory rather than reading
S3 directly, so added a shared `workdir/canon_mirror` local-mirror target wired to every upstream
stage they depend on (a02 dim_boundary, a04 dim_calendar, a05 ref_txn_classification, b00
canonical_valuation, b01 canonical_positions) via their existing `--local-out` support. Also
found and fixed, same pass: `c02_twr_engine.py:157` hardcoded `date=2026-08-07` in its
dim_calendar read (a NEVER#1-class defect independent of the wiring bug) — now derives from
`--date`. Commit `acf0132aef`.

CTO set the acceptance oracle explicitly: **tables-not-labels** — presence of the 3 real
canonical prefixes + absence of new writes to the 3 colliding ones, both live-verified against
S3, never the run's self-report.

### 3. Two IAM gaps found and escalated (grounded on the live-applied plane, Rule 22a)
- `smartx/platform/silver/fact_allocation_account_map/*` on `opal-data-assets` (jd1 vintage
  stamp + a06 identity crosswalk, same prefix serves both) — flagged to AE 160817Z, applied as
  grant "B8" 16:12Z, sim-proven both directions.
- `opal-data-inf/silver/api_dims/positions_mv/*` + `opal-data-assets/blackdiamond/cottonwood/silver/fact_holdings/*`
  (a07's firm-neutral asset-classification population union, by design per its own docstring +
  the CTO 160826Z substrate amendment) — AE correctly routed this to CTO as a NEVER#2
  firm-separation question rather than pasting it as routine IAM; CTO in turn ruled it above
  their own gate and escalated to Andrew as CALL 1 of an open-calls aggregate. Andrew ruled
  "Yes, approved" (~17:2xZ); AE applied + battery-proved both legs (positive + negative
  controls both discriminating correctly) within minutes of the ruling landing.

### 4. Full corrected chain — clean end-to-end
Fired the moment the last grant landed: `CHAIN OK date=2026-08-18 wall=107.1s rc=0`, all 16
stages + the c04 validation battery green, including a07's three-firm population union working
exactly as designed (49F 2,329 + INF 1,658 + COT 1,066 = 3,869 distinct securities, 90.90%
classified). Live-verified (not the run's self-report): `canonical/flow_ledger` (in=25,004
out=25,004), `canonical/nna_canonical` (5,351 accounts, headline NNA $1,746,760.76),
`canonical/twr_daily` (7,315 rows) all present at `date=2026-08-18`; `canonical/account_gains`,
`canonical/account_performance`, `canonical/client_performance` all still zero objects — the
Defect-B mutant's own negative control, run for real, passing.

### 5. P3 dims (a07 home + a06 xwalk) — landed in the same run, live-verified
`gold/advi/dimensions/dim_asset_classification/date=2026-08-18/` + `alias_key_expansion/` +
their manifests under `dimensions/_manifests/2026-08-18/` — all present. `dim_identity_crosswalk`
(a06) — data.parquet + manifest.json present, 7,305 rows. This was the item blocking DS~B's two
P3-gated D-tier twins (`d06_firm_mix_summary`, `d14_advisor_nna_canonical`) per the roster's
Friday-feasibility flag; both inputs now exist at the scheduled root.

### 6. P2D-4 contract re-issued (CTO 161352Z ask)
Appended an addendum to the existing `OPAL_ADVIPOINTERS_P2D4_INVOCATION_CONTRACT_49F_CHAIN_20260818.md`
(original preserved unchanged) covering the 2 vendored ref/ bundle members, the full measured
IAM surface across all Sids (incl. B8 and the a07 legs), and a plain-language note on the
c00/c01/c02 local-mirror correction. Commit `2276ad55d5`.

### 7. Proof-of-spec instance (P2D-1..P2D-5)
`OPAL_ADVIPOINTERS.P2-DISPATCH-49F_PROOF_OF_SPEC~A.json` — VALID rc=0 after two schema-fix
rounds (enum literals, then the artifact-coverage heuristic's criterion-id grammar mismatch,
resolved via the tool's own documented `declared_exclusions` escape). Commit `32ce6d5301`.

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Derive `fam_as_of` dynamically from the latest available partition rather than hardcode either cited literal (2026-08-07 or 2026-08-10) | Required for the SS6-mandated auto-lift property; a hardcoded value cannot lift itself when the vendor feed heals |
| Left `read_upstream_declared_stale()` un-wired into any d-tier file | D-fleet is DS~B's P4 lane per the roster split; building the plumbing but not the wiring respects lane discipline (matches AE's own instinct on the publisher-invocation-form question) |
| Did NOT touch the colliding OPAL_GLDRNS.A4 wrapper files | CTO explicit scope line (161345Z): disambiguation is a routed COO follow-on, not today's act — composition-only fix on my own component |
| Escalated the a07 IAM question rather than asking AE to grant it | Genuinely triggers NEVER#2's letter (bd-tree role reading another firm's bucket); AE's own caution was correct and I did not push back on it |
| Verified every acceptance claim against live S3 state, never the run log alone | Rule 22a; also the exact axis Defect B proved untrustworthy — CTO named this explicitly as the acceptance oracle |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `data/assets/scripts/gold/runners_49f/a01_dim_relationship.py` | fam DECLARED-STALE fallback + manifest fields | Yes — `f891776875` |
| `data/assets/scripts/gold/runners_49f/runner_common.py` | `read_upstream_declared_stale()` helper | Yes — `f891776875` |
| `data/assets/scripts/gold/runners_49f/chain_49f_entrypoint.py` | bundle-path import fix, then full c00/c01/c02 rewiring + local-mirror | Yes — `11fb1edcd3`, `acf0132aef` |
| `data/assets/scripts/gold/runners_49f/{a00_dim_account,a04_dim_calendar,a05_ref_txn_classification,a07_dim_asset_classification}.py` | bundle-path import fix | Yes — `a9a494087e` |
| `data/assets/scripts/gold/runners_49f/c02_twr_engine.py` | hardcoded-date fix | Yes — `acf0132aef` |
| `org/tier2_senior/0.4.0_DS_ClientPlatform~A/deliverables/OPAL_ADVIPOINTERS_P2D4_INVOCATION_CONTRACT_49F_CHAIN_20260818.md` | re-issue addendum | Yes — `2276ad55d5` |
| `org/tier2_senior/0.4.0_DS_ClientPlatform/deliverables/OPAL_ADVIPOINTERS.P2-DISPATCH-49F_PROOF_OF_SPEC~A.json` | new, P2D-1..5 VALID | Yes — `32ce6d5301` |
| `infra/system/06_current_state.{md,json}` | regenerated (commit-gate dependency) | Yes — `32ce6d5301` |
| `s3://opal-data-49financial/_code/ref/{SCHWAB_TRANSACTION_CODE_CLASSIFICATION_20260811.json,etf_classifier.py}` | vendored (not a repo file — S3-only artifact) | N/A — explicit `aws s3 cp` |

---

## Blockers

None remaining. All three SS6 items closed; AE applied the floor cron (Root A, `advi-49f-gold-floor`
ENABLED at `cron(45 12)`) citing today's 107.1s + live acceptance as the pin basis, closed ledger
`@647c432a7d`. First unattended green fires tomorrow 12:45Z UTC.

---

## Current State

Today's SS6 dispatch (fam DECLARED-STALE, P2D-3 duration, P3 dims) is fully closed with live
evidence, not self-report. The chain now runs correctly end-to-end on the real S3-code path
(107.1s), writing the correct canonical tables under their correct names for the first time ever
in this deploy form. Two IAM grants landed today (B8 smartx/jd1, and the Andrew-ruled a07
cross-firm pair) — both battery-proven. The floor cron is live; tomorrow's 12:45Z fire is the
first unattended green of the Thu+Fri SS6 bar-compression pair. The colliding OPAL_GLDRNS.A4
wrapper files (`c00_runner.py`/`c01_runner.py`/`c02_runner.py` + their
account_gains/account_performance/client_performance modules) remain in the corpus, untouched,
disambiguation routed to COO as a follow-on. BDMERGE-CONVERGE (08-21) and my other pre-SS6 TOs
(INF_RUNNER_REFACTOR.P1, NFRA_COMPILERKIT.P1 joint, OPAL_GLDRNS.A4 respec-held) are unchanged by
today's work — COO sequences.

---

## Next Steps

1. **Watch for tomorrow's 12:45Z first green** — event-driven, no action needed unless it aborts
   (the mutex/failure-signature table in the P2D-4 contract covers the discriminators).
2. **[2.0.0_SA_COO] route the OPAL_GLDRNS wrapper-file disambiguation** — CTO named this a
   routed follow-on, not assigned to a seat yet as of this log.
3. **[0.4.0_DS_ClientPlatform~B] wire `read_upstream_declared_stale()` into the D-fleet publisher**
   at Thursday's respawn, per the plumbing-not-wiring lane split landed today.
4. BDMERGE-CONVERGE (08-21, unchanged) and prior TOs resume per COO's sequencing.
