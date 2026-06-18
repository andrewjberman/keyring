# NFRA_GCONTR.TO-5 -- contract-engine hardening (fail-loud-on-unresolved + grain-annotation)

**archetype:** IMPLEMENT
**secondary_archetypes:** DIAGNOSE, COORDINATE

## Window
2026-06-18 ~1635-1803Z. Off my own GCONTR.TO-4 finding -> CTO ruling -> COO GO. Pre-nightly window
(NNA/cot still event-gated). Heavy multi-agent design collaboration (CTO/COO/CVO) through a churny
but convergent thread.

## Current State (zero-context handoff)
TO-5 COMPLETE + LANDED + live-verified. Hardened the contract-engine value layer in THREE ways per
CTO's evolving ruling (165140Z + 170120Z):

ENGINE (contract_engine.py + surface_check_cli.py) -- **CTO owner-committed 92733a2e5** (cross-tool:
these are CTO's tools, lane ANY_EXEC_OR_AE; I authored, CTO owner-reviewed+committed -- the convention
default, NOT --force):
- **(1) exact name-match** kept (no fuzzy-stem -- FP risk on a never-widen guard).
- **(2) fail-loud-on-unresolved**: new `live_iam_roles(graph)` (classes_data.iam.nodes, exact id/name/
  arn); in q2_join, a forbidden_writers entry resolving to 0 live IAM roles (+ not observed) on a
  grain=key surface -> status `UNRESOLVED_FORBIDDEN_WRITER` (LOUD), never 0-hits-clean. run_contract_check
  + the comp-surface-check shared path (surface_check_cli `_contract_advisory`) both pass live_roles ->
  comp-surface-check INHERITS (the SEV1 gate is now fail-loud-on-unresolved). IAM-rename regression test
  in contract-selfcheck (phantom->UNRESOLVED; resolved-live-role -> no false-positive).
- **(3) grain-annotation** (part-3 replacement; true key-grain not graph-derivable): contract field
  `enforcement.forbidden_writer_grain`, **DEFAULT "bucket"** (CTO 170120Z fail-safe -- bucket-grain
  write data today makes "key"-default a FALSE-POSITIVE generator on shared buckets + stalls the §9
  ramp; forfeits 0 real coverage since canonical_writer + value-limb enforce regardless). "bucket" =
  DECLARATIVE (forbidden axis advisory, never hard-flips); opt-in "key" to hard-enforce (single-tenant
  today / any surface once key-grain derive lands -> promote via the documented hook).

CLI (pipescript_cli.py) -- **DS-committed bfd89480a** (my lane, owned-paths 0096b5cbb):
- cmd_flipped exit 2 on UNRESOLVED_FORBIDDEN_WRITER; cmd_contract surfaces UNRESOLVED + exit 2;
  contract_id fallback (CVO note); usage docstring.

LIVE-VERIFIED (deployed, pipescript --flipped --since 20260617): benchmark(SEV1)/aum/peers all
WATCH-declarative, **ZERO UNRESOLVED** (default=bucket -> clean standalone, not dependent on any
contract reload); headline/advisor_intelligence UNCONTRACTED-LOUD (pre-existing TO-4). exit 2.
contract-selfcheck ALL PASS; gate-b 25/25 non-regressed.

## Files Modified
contract_engine.py + surface_check_cli.py (commit **92733a2e5**, CTO owner-commit of DS-authored);
pipescript_cli.py (commit **bfd89480a**, DS); TO status->complete (83a05dbc3).

## Key decisions / findings (this thread)
- The graph's WRITES edges are BUCKET-grain IAM-capability (no key/prefix; IAM nodes carry no statement
  resources). So true key/prefix-grain write-match (CTO's part-3 brittleness) is NOT graph-derivable ->
  Option-A (derive emits IAM-policy-statement S3 prefixes on WRITES edges) routed to AE; my q2_join
  key-grain consumer hook documented (forward-compatible). I refused to fake key-grain over bucket-grain.
- The benchmark verdict is (b) HEALTHY (CVO): yang-only writes the benchmark VALUE keys; smartx writes
  only _smartx_ co-tenant keys in the shared bucket -> NOT a BMKAUD breach -> demote, not name-correct.
- CROSS-TOOL discipline: the TO lane_note wrongly claimed "DS commit-direct" for contract_engine +
  surface_check_cli (they're CTO's tools). The owned-paths gate caught it; I surfaced (didn't --force)
  -> CTO owner-committed those 2 (option B); I committed pipescript_cli (my lane). COO owned the lane_note
  error. surface_check_cli (the SEV1 gate) stays owner-committed (no standing DS lane = no over-grant).

## Compiler Tools
| `<run>` (TO mandate) | Result | Observed vs `<expect>` |
|---|---|---|
| Phase-2: IAM-rename regression test (contract-selfcheck) | PASS | phantom forbidden_writer -> UNRESOLVED_FORBIDDEN_WRITER; resolved-live-role -> NOT UNRESOLVED (no FP); declarative grain=bucket -> WATCH advisory |
| Phase-2: `.tools/ds-commit-gate.sh` (3 files) | PASS | exit 0 each |
| Phase-3: `comp-surface-check contract-selfcheck` (deployed) | PASS | CONTRACT-SELFCHECK: ALL PASS (T1 UNSANCTIONED preserved on grain=key) |
| Phase-3: `pipescript --flipped --since 20260617` (live) | PASS | benchmark surfaces declarative WATCH (NOT silent; NOT a false UNSANCTIONED) -- the inert-tripwire is now grain-annotated; 0 UNRESOLVED on default=bucket |
| Phase-3: `pipescript --contract model_portfolios.benchmark` (live) | PASS | declared contract + observed writers + grain-aware |
| `pipescript --gate-b` (pre + post) | PASS | 25/25 non-regressed (additive) |
| `comp-iam` (graph IAM-role inspection) | PASS | classes_data.iam.nodes = 116 IAM_ROLE nodes -> the live-role resolution set; all 4 benchmark forbidden_writers resolve to 0 (phantom) |

- **What worked:** delegating to contract_engine + reusing the live-role node set; the default=bucket
  flip makes the deploy clean standalone (no contract-reload dependency); ground-truthing the edge grain
  before claiming part-3 buildable.
- **What failed:** nothing in the build. The lane gate correctly blocked my cross-tool commit (the TO's
  lane claim was unwired) -> resolved via owner-commit (B).
- **Gap found:** (1) true key-grain write attribution absent from the derive -> AE Option-A TO. (2) The
  TO-5 lane_note mis-stated DS ownership of CTO tools -> COO owns; surfaced not bypassed.

## Blockers
None now (was BLOCKED on the lane gate; resolved by CTO owner-commit B). TO-5 complete + landed.

## Next Steps
1. **[2.0.0_SA_COO]** RAVC2 close TO-5 (engine 92733a2e5 + CLI bfd89480a, live-verified).
2. **[0.7.0_AE_CloudOps / globgrph]** Option-A: derive emits IAM-policy-statement S3 prefixes on WRITES
   edges (key-grain write attribution) -> then a contract promotes grain="key" + my q2_join hook matches
   writer-prefix INTERSECT artifact_key-prefix. (CTO routes.)
3. **[3.0.0_SA_CVO / 1.0.0_SA_CTO]** benchmark phantom DenyNonYangWriteBenchmarks backstop (never applied)
   + §9 ratify -- Andrew-facing, independent of this engine.
4. **[self, event-driven]** NNA D_00f + cot-transactions nightly verifies (tomorrow-AM, separate threads).
