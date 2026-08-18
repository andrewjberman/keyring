# 0.4.0_DS_ClientPlatform~A -- session log 2026-08-18 1720-1740Z: P2-DISPATCH-49F build window

**archetype:** BUILD-DEPLOY

## Frame
P1 CLOSED for 49F (CTO-ATTESTED @ab7c94c470 on the inventory + CVO sweep + card + instance);
P2 formally OPEN. P2D build proceeded same-session per the TO ("build may start now").

## Work executed
- **Code-home grammar question ROUTED to CTO** (per the COO amendment's route-don't-decide
  instruction) -> **RULED (a) 172006Z**: `s3://opal-data-assets/portal/gold/advi/_code/` (the
  mdpf `_code/` twin, atom-2 conformant; not sovereign-scoped).
- **P2D-1 @4dadd1354c**: `chain_49f_entrypoint.py` -- one scheduled stage, a00..a07 -> b00..b03
  -> c00..c02 + c04 battery; fail-loud per stage; mkdir-atomic mutex (refuse rc=3, never steal);
  mode single-homed (`--production` derives T-1 from `lib/trading_calendar`); input set
  enumerated in header; c03 nna_atomic EXCLUDED-disclosed (@3a924da626 D2).
- **safe_deploy_core advi tree row** (same commit, CTO gates): + LONGEST-PREFIX resolution in
  `file_to_s3_target`/`resolve_tree_layer` -- the advi home nests inside mdpf's shared
  assets_gold home and first-match-in-dict-order would be insertion-order-dependent. Verified:
  10/10 mapping cases (incl. both overlap directions + None cases), resolver agreement,
  shared-home guard semantics, `.tools/test_safe_deploy.py` 14/14, pipescript-suite commit gate
  140/140.
- **Smoke (dry-run, rc bare)**: a-stages 8/8 GREEN (~175s; a02 127.6s dominates); b00 abort
  CORRECT-BY-DESIGN on unwritten dry outputs -- fail-loud exercised on a real missing input.
  Evidence: `OPAL_ADVIPOINTERS_P2D1_CHAIN_SMOKE_20260818.md`.
- **REAL DEFECT FOUND + FILED not fixed**: `a01_runner.py` import-broken at HEAD since the 08-11
  P1 rewrite (imports `build_relationships`; module exports `build_dim_relationship`) -- cannot
  have run from this state; entrypoint invokes the live S3-native module directly; runner = P5
  candidate.
- **P2D-2 substance**: `_code/` FIRST-MINTED explicit (pre-mint 0 keys) -- 51/51 objects
  (all runners_49f `*.py` + `POLICY_BLOCK.json` + `lib/trading_calendar.py`), each
  ETag==local-md5 verified, metadata `script-sha256` + `vintage-commit 4dadd1354c`.
  comp-pipescript `deployed` MATCH degraded until 0.8.0's REG lands (flagged 173558Z).
- **P2D-4 DELIVERED** (@4dadd1354c, MCP to AE 173547Z): all 4 interface fields + the GROUNDED
  marker answer (converter manifests at `meta/conversions/` are ruled non-triggering,
  `conversion_manifest.py:50-53` -- floor-only first fire satisfies NEVER#4). Host-lifecycle
  fact folded: the box is STOPPED at the fire window; dispatcher carries the start-instance duty.
- **Own-harness slip caught + corrected in-flight**: first smoke's bash pipe (`| tail`) ate the
  entrypoint's rc (reported 0 on a CHAIN ABORT) -- the TO's own "rc WITHOUT a pipe" lesson;
  re-run bare. Also mis-cited the card commit as a peer's hash that landed between my commit and
  my `git log -1` read (shared-branch trap); corrected everywhere + disclosed to COO 171733Z.

## Banked (no action)
- a01_runner.py stale-predecessor finding (above) -- P5 census input.
- comp-system STRUCTURAL-TWOPHASE override on @8817012062 discharged in-session @eb29290.

## Compiler Tools
| Tool | Invocation | Result |
|---|---|---|
| comp-find | "dim_advisor_fee_role" / silver marker sweeps | jd2 producer + marker ruling located, denominators printed |
| comp-pipescript | (io on runners still registry-gapped) | degraded path documented in TOs; retires at 0.8.0 REG |
| test_safe_deploy.py + pipescript-suite gate | commit-time | 14/14 + 140/140 green on the resolver change |

## State at close
P2D-1/2/4 done; P2D-3 (QA exercise on the S3-code path, host, with AE -- yields the binding
duration) + P2D-5 instance = 08-19. P3-CLOSE 08-20 (b01 + A_07 persist verified on the scheduled
run). BDMERGE-CONVERGE 08-21. Event-driven hold; watcher b71q41k9y live; zero crons.
