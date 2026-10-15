# self-drive cluster open calls -- tick 66 (2026-10-15 ~02:5xZ), 1.0.0_SA_CTO laptop

state: ARMED   cadence: 60m   cron: 6ca5a587   ticks covered: 66

## Measurements this tick

- Cluster list, read ~02:55Z: boxes=4, read=4, absent=none; open=17 (fork 0, act 17, approval 0), closed=202.
- Changes since tick 65:
  - CLOSED dell2 `2402` (the commentary PDF reader approval).
  - CLOSED dell2 `076d` (the filled-report serve path), on XA-20261015T024033Z-ef7f RULED (b) @d4cce447c1: dell2 `~P2` issues
    hops 2-4.
- **The MDPF edge firm gate is DONE.** Ledger `mdpf-canon-edge-firm-gate` is CLOSED by `0.7.0_AE_CloudOps~U7` (fac3025ca7, in
  CLOUD 02d22c80d1); the sentinel is gone from `.open_deploys/`.
  - Proofs: v24 on 27 of 27; no-token 401; internal read 200; the synthetic-claim arms 14 of 14 at v24 against 6 of 14 at v23;
    v23 still answers for rollback.
  - Not proven: the L1 WAF hash (method not kept; 0 UpdateWebACL events), and a live partner 403 (no partner login exists).
  - U7 was respawned at 02:22:58Z under the switched account and finished inside the extended window.
- **The keep-driving switch** was re-set ON at 02:10:00Z on Andrew's word. Loops armed: site Z 6/6, dell1 7/7, dell2 11/11,
  laptop 3/4 (COO~C chased at 03:00Z).

## Calls this tick

- None for this seat.

## Acts only Andrew can do

- Laptop: `3717` (spend limit; seats now run under the switched account); `7841`; `8f2b`, `44eb`, `e435`; G4; the
  DSGN_RBNDV2 endpoint.
- dell2: `53cb` (the scratch delete); `f61b` (P2's last blocker), `a252` (P1's disclosure page), `2106`, `e260`.
- Site Z: `21d9`, `def4`/`3b41`, `a519`, `21c5`/`8ed7`/`f0d2`.
