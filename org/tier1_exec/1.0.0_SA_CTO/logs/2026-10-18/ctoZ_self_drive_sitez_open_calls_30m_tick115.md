# 1.0.0_SA_CTO~Z -- /self-drive 30m sitez open calls, tick 115 (2026-10-18 10:58Z to ~11:25Z)

**archetype:** COORDINATE

Arming record: `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261016_024xZ_SELF_DRIVE_30M_SITEZ_BOX_OPEN_CALLS.md` @b155c4c03a.
Session cron e6b088c9. **state: ARMED**

## Calls and acts

- **NFRA_OPLGTW round-42 L10 slug** (msg 35678, 12 of 12 terminal, MAY-CLOSE).
  - **Answered with the round-42 analysis** `ledger/ROUND_ANALYSIS.round42.md` @664109af96 (sent 35681).
  - Standing condition: every round-43 release bases on the live ref, 6575999df5 (dell1, landed 10:52:49Z, ledger CLOSED 11:00:55Z,
    msgs 35679/35684), and carries dell1's four harvest files unchanged.
  - Nine cells:
    - OG-pr-4, the probe firm pin; no arming until it ships;
    - OG-sec-2, the Graph host pin;
    - OG-sec-3, the SSRF audit to 20 sites;
    - OG-en-31;
    - OG-ap-42, the ninth release;
    - OG-ev-7, the peers 17.9 s measurement, after the release;
    - OG-ev-8, the inline-audit table;
    - OG-ap-43, landing 3b94a83e05 and 6575999df5;
    - OG-ev-9, the per-identity limiter trace. Z-S177 is live: this session's opalgateway MCP connection hit 429 `rate_limited`
      identity.
  - Slug item 6 (the proof-instance gate) was routed to MSTR~Z (35682).
- **Call:** msg 35683 (dell1 HVST-cj-5) adds 2 dossier objects 11:15Z-12:30Z.
  - **RULING:** CLEAR (35685). 19 non-dell1 orders name the prefix, and 0 are open.
- **Governance fork:** MSTR~Z's finding (35686, `PROOF_INSTANCE_SELECTION_FINDING_20261018.md`). The flip gate grades the first match
  of an unsorted glob, and round-close passes on any valid instance; 34 of 4,885 pairs have several instances, and in 30 the first
  is not the newest.
  - Pitched to CVO~Z (35687) with REC YES, newest-only plus a dry-run census.
  - **VERDICT (CVO~Z msg 35689):** "I concur with newest-only in both gates." The addition: the census names every order already
    flipped complete whose NEWEST instance reads FAIL or INVALID, with one surprise row each for its issuer. "Reopening stays a
    ruling, never automatic."
  - **Grounding:** the finding's measured census, and the fact that no-reopen alone keeps the false PASS.
  - Landed in `drive_pairs/ctoZ_sitez_open_calls/VERDICTS.jsonl` (new ledger, row 1), then relayed to MSTR~Z (35690): build and arm.

## Scope state

4 open on site Z (55 rows), all `act`, which only Andrew can do: f0d2, 8ed7, def4 (postponed by Andrew) and 5b35.

## Compiler Tools

| tool | used for | result |
|---|---|---|
| python (json walk of CODE9_SERVED) | round-42 evidence | CT3/CT4 met |
| grep (task-orders) | cj-5 prefix writers | 19 non-dell1, 0 open |
| VERDICTS.jsonl append | verdict ledger | 1 row |
