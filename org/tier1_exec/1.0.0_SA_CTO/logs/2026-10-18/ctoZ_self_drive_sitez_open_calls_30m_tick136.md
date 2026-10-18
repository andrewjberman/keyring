# 1.0.0_SA_CTO~Z -- /self-drive 30m sitez open calls, ticks 135-136 (2026-10-18 20:27Z to 20:57Z)

**archetype:** COORDINATE

Arming record: `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261016_024xZ_SELF_DRIVE_30M_SITEZ_BOX_OPEN_CALLS.md` @b155c4c03a.
Session cron e6b088c9. **state: ARMED**

## Ticks

- **Tick 135 (20:27Z):** quiet; 0 unread. eff517546e is not yet on box/sitez; its landing was asked of 2.0.0_SA_COO~O at 20:06Z.
- **Between ticks: OG-ev-7, the peers measurement (row Z-S389).**
  - **20:40Z:** COO~O msg 35797 (acked) sent the re-based ask.
    - It is `NEVER_WIDEN_ASK_OG-ev-7.md`, sha256 34333184f1998cfd3221e1a7bd13a2312af154ec9c9a2520fefa0945969eee91. I re-hashed it
      (@8fa5396f6f). It is on live eff517546e, and the earlier ask e8e2d7a1a533 is void.
    - The COO's half is signed. I routed the ask to 3.0.0_SA_CVO~Z to sign FIRST, the CVO's own condition.
  - **20:43Z:** the CVO's half was SIGNED first (msg 35799, acked; @3736444fab).
    - It binds the ask's 16-hex prefix `34333184f1998cfd`.
    - Its recommendation: a NON-client placeholder account_ref in the lease.
  - **The CTO half was SIGNED @d426b5fbe5.** I read the listener at the release myself:
    - `_ACCOUNT_REF` at `probe_listener.py:58`;
    - the firm-and-account refusal at `:324-327`.
  - **My conditions:**
    - CT1: the base is eff517546e at the GO and at Step 2.1.
    - CT2: the CVO's placeholder `account_ref` is adopted, which makes the arming peers-only.
    - CT3: the counts must be exact: journal POST /probe/ = 5, lake `probe:OG-ev-7` = 3, `probe:unarmed` = 2. A /probe/ count above
      5 is an ARMED row.
    - CT4: I take the verdict `ev7.AC1` recomputes.
  - **Relayed** (this also relays the CVO's half, at the CVO's request): to 2.0.0_SA_COO~O as msg 35800 and to
    0.7.0_AE_CloudOps~NFRA1 as msg 35801. **Three halves are in hand.**
- **Tick 136 (20:57Z):** 0 unread. eff517546e is still not on box/sitez.

## Open calls

- 0 forks.
- 4 open (55 rows), all `act`, which only Andrew can do:
  - f0d2: sign in once as Opal Bloomberg;
  - 8ed7: one /control-plane and /open-calls run;
  - def4: the Alyssa sitting, postponed by Andrew (record @92df615fc6);
  - 5b35: the asset manager's harvest call.

## Waiting on

- The OG-ev-7 Step 2 report from ~NFRA1, to grade CT1-CT4.
- The release landing on box/sitez, from COO~O.

## Compiler Tools

| tool | used for | result |
|---|---|---|
| sha256sum | OG-ev-7 ask binding | equal to 34333184f199 |
| git show eff517546e:probe_listener.py | lease validation and refusal paths | a placeholder ref passes `:58`; transactions refused at `:326` |
| git merge-base --is-ancestor | release on box/sitez | not yet |
