# CVO~B — GATE-2 PRE-READ RE-ANCHOR (determination #5) + the census-boundary finding

**archetype:** VALIDATE
**agent:** `3.0.0_SA_CVO~B` (Andrew-direct dedicated AoR validation lane, LD-0277)
**window:** 2026-07-15 22:37Z (spawn) -> ~23:25Z
**commits (1):** `5652424d4` (pushed to CLOUD)

## Summary

Re-spawned for the LD-0277 gate-2 cold pre-read (CTO 223623Z via MSTR 223756Z). Rendered
**determination #5 — PRE-READ RE-ANCHOR at `327db12ea`**: det-#4's structural clearance CARRIES; the
re-scope's fold-ON condition is met-by-evidence-read, not-yet-met-by-my-own-run; battery re-fire
pre-registered (section 5) and offered to CTO for sequencing; **V4 = WITHHELD — NOT RUN — explicit gap**,
fires on the first post-flip nightly against the pre-registered section-6 bar. **NO hold motion was made.**

State of the world recorded at determination time (23:03Z, read live): **`INF_AOR_FOLD_ACTIVE=1` armed on
the trigger** (post-Andrew-GO 22:42Z, recorded verbatim by DS~B), **chokepoint still HELD**. The release
window is executing; the pre-read landed inside it.

## The one new finding (routed URGENT to CTO 232031Z; NOT a hold motion)

`INF_D_02c` / `INF_D_04` / `INF_09` are deployed at **pre-round-8-consumer-migration vintages** — md5
vintage-tie: two == `5581c0de1^` EXACTLY — still sentineled in repo, absent from the G3 bundle manifest,
and dispatch-invoked `--upload`. A chain-wide run under fold-ON executes pre-canonical attribution on three
served surfaces (the `dbd10d7aa` "partial, silent, inconsistent fold" class, one layer out). Run scope =
gate owner's call; COO folded it into never-widen scope precision (232154Z). Class named:
**a release-parity census must cover the DISPATCH-INVOKED closure, not the sentinel list** (the ring
outside DS~B's own CATCH-2 from the same night).

## What was verified vs attested (the pre-read's epistemic ledger)

- VERIFIED at my own instruments: instrument integrity (git), runner parity (fresh sweep + one download
  md5-tie after a tool timeout), pin guard both directions at source, suite census (155 = 154 assertions +
  1 DS-disclosed scribe-record that cannot fail), reproduce-gate mechanism teeth, live trigger/chokepoint state.
- ATTESTED (DS-run, my re-run rides the battery fire): the 155-pass execution, the reproduce-gate PASS
  numbers (164 exact), the timelock 0/9,510 fold-OFF baseline.
- PRE-REGISTERED before my battery re-fires: per-arm expectations incl. `phantom_switch_arm` EXPECTED to
  change state on the real basis (det-#4 §3's reachable switch-dependence is now real — the arm working,
  not a regression) and `phantom_advisor_arm` RED-until-served-then-MUST-flip.

## Housekeeping

`aor_timelock_bar_v2_account_grain.py` (mine, 07-13) had sat untracked — pinned in `5652424d4`.

## Compiler Tools

| Tool | Result | Note |
|---|---|---|
| `comp-glob` x3 | hit | suite/reproduce/preview locates |
| `comp-grep` x1 | hit | pin-guard source census (INF_AOR_SRC_ETAG, denominator = full data/inf/scripts) |
| `comp-pipescript deployed` (no-arg sweep) | **the finding** | inf-gold: resolver+D_11+8 bundle scripts MATCH; D_02c/D_04/INF_09 STALE; D_00d TIMEOUT (transient — md5-tied by download) |
| `comp-pipescript deployed INF_D_00d.cumulative_chart.py` | misroute | single-script form routed to bd tree and hit a **stale bd-hold SKIP** (the 07-14 sovereign lift not reflected in the tool's hold config) — gap noted for the tool owner |
| `.tools/safe-commit.sh -F` + commit-gate + comp-pulse | PASS | risk reflex CLEAN, denominator 2/1239; danger map STALE-flagged 41h (noted, not mine) |

**What worked:** the no-arg sweep's denominator (the dispatch table) is exactly why it saw what the
sentinel-set census could not. **Gap found:** (1) single-script `comp-pipescript deployed <name>` defaults
to the bd tree and its hold config predates the 07-14 lift; (2) the sweep TIMEOUT class can silently thin a
parity census — mine hit 1 of 45 and I closed it by hand; a census with a TIMEOUT row is not a census.

## MCP traffic

IN: MSTR spawn direction (223756Z), COO ACK+scope-precision (232154Z). OUT: URGENT evidence to CTO
(232031Z), interim CCs to MSTR+COO (2320xZ), RAVC close to CTO + CCs (2323-2324Z).

## Blockers

None mine. Event-gated: battery re-fire awaits CTO sequencing; V4 awaits the first post-flip nightly BY
DEFINITION; the census-boundary scope ruling is CTO's.

## Next steps

- **[me]** fire `aor_gate2_runner.py` at `327db12ea` when CTO sequences it; grade against det-#5 §5. Then
  V4 on the first post-flip nightly's SERVED artifact against det-#5 §6. Re-verify the three census-boundary
  scripts' disposition after CTO's ruling.
- **[1.0.0_SA_CTO]** the 232031Z finding's scope ruling; battery re-fire sequencing.
- **[2.0.0_SA_COO]** never-widen co-sign scope precision (sent, theirs).
- **[Andrew]** nothing from this lane. Nothing in this window authorizes anything.

---

## DELTA 23:28Z-23:38Z — ruling consumed, battery FIRED, one prediction worn

- **CTO 232824Z** (`194d3d674`): my finding ruled the **named stage-B precondition** — the three `--upload`
  legs HELD this window; exclusion oracle (listings UNCHANGED) ledger-recorded; stage A dispatched with the
  release sentinel live. Det-#5 §6.5 annotated to parity (`02ec19aea`). **28 minutes of margin** between my
  232031Z and the flip — the pre-read landed where it had to.
- **CTO 232947Z commissioned the battery re-fire NOW.** Fired at `327db12ea`: **exit 0 — 9 GREEN + 1
  expected RED**, denominator 10 live / 10 declared exclusions (the four 07-13-PM time-lock-chapter arms
  declared EXCLUDED before firing — the runner's no-silent-caps guard refused until they were). Evidence
  transcript + runner declarations + det-#5 annotation @ `84e7e2dcc`. **Gate-2 now stands on a FIRED
  battery at HEAD.** Reported to CTO 233820Z with denominator per his rider (b).
- **The one outside-§5 reading, worn not buried:** `phantom_switch_arm` stayed GREEN — **my pre-registered
  prediction was wrong** (I mis-attributed the release's "phantom GONE" to the fold; it rides the
  silver-rescue leg G4). Triage found the arm's "grounded live 873 rows" line is a **hardcoded 07-13
  label** (hermetic arm — its own §15 class); re-grounded LIVE on `api_dims/accounts_v2` 07-15 (874 rows):
  560/703/1225 ALL still roster-ABSENT, control 42 PRESENT, the +1 is account 4364. **V4 precision
  banked:** the "phantom GONE" cell binds to the rescue leg having executed — grade mechanism-discriminated.
- Compiler-tools delta: boto3 direct-read for the roster re-ground (the aws-shim-from-Python lesson
  honored); one NoSuchKey on an assumed prefix corrected by listing (`silver/api_dims/accounts_v2/`, not
  `silver/accounts_v2/`) — assumed paths are hypotheses too.
