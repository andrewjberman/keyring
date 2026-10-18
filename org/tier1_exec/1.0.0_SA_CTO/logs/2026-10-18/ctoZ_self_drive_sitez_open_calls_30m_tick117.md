# 1.0.0_SA_CTO~Z -- /self-drive 30m sitez open calls, ticks 116-117 (2026-10-18 11:25Z to 12:12Z)

**archetype:** COORDINATE

Arming record: `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261016_024xZ_SELF_DRIVE_30M_SITEZ_BOX_OPEN_CALLS.md` @b155c4c03a.
Session cron e6b088c9. **state: ARMED**

## Ticks

- **Tick 116 (11:27Z):** quiet.
- **Between ticks:**
  - **The newest-instance gate is BUILT** (MSTR~Z msg 35691; CVO verdict 35689). 9 tests pass, and it is NOT armed.
    - Census: 33 multi-instance orders of 4,883 pairs.
    - The flip-gate verdict changes for 10 orders, all rc1 -> rc0. The round-close verdict changes for 1 (HVST-s-1, OK -> NOT-OK).
    - 3 orders already flipped complete read FAIL or INVALID on their newest instance: RIV-f-3 and RIV-q-1 (COO~RV) and FB-f-9
      (COO~B1). Each gets one surprise row, filed by MSTR~Z.
  - **Act:** `.tools/to-pipeline-gate.py` is lane LOOP_MECHANISM (CTO+CVO).
    - I reviewed MSTR~Z's patch: `_newest_instance_only()` is inert unless the flag `org/mcp/proof-newest-instance.enforce` or
      `PROOF_NEWEST_INSTANCE=1` is set.
    - I ran the 9 tests (pass) and py_compile (ok).
    - I widened the worktree's sparse cone to `org/modules/graph`, because the commit-gate needs `comp_constants_cli`.
    - COMMITTED @a982a238c0 on branch box/sitez-proofsel (C:/tmp/slot-proofsel).
    - The battery (lane TOOL_BATTERIES, author != gate) was asked of CVO~Z. MSTR~Z commits its three paths, drains, and only then
      arms (35693/35694).
  - **NFRA_OPLGTW round 43 issued** (COO~O msg 35692, 581ee61977, R3-T.120). Workers ~151-155 run OG-pr-4, OG-sec-2, OG-sec-3,
    OG-ev-8 and OG-ev-9. **Readings ruled** (35695):
    - the SSRF denominator is 21 over six modules: accepted;
    - the audit-write sites are 81: accepted;
    - the firm pin means the call's firm equals the lease firm AND the call's account equals the lease account, both checked before
      the tool runs; a lease with a missing or unparseable firm is malformed.
- **Tick 117 (12:12Z):** 0 unread; 4 open (55 rows), all `act`, which only Andrew can do: f0d2, 8ed7, def4 (postponed by Andrew) and
  5b35.

## Compiler Tools

| tool | used for | result |
|---|---|---|
| pytest (test_proof_instance_select) | patch review | 9 passed |
| commit-gate.sh | gate patch | clean (after the sparse widening) |
| check_inbox | 0.8 measurement | 0 unread |
