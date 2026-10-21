# Drive log 2026-10-21 04Z -- 2.0.0_SA_COO~G2 (host desktop-n8rjv0a)

Scope: IRPT_ANLREQ workstream G (FWD-10 Core) and IRPT_YCDGEN. Leases read FULL for both.

| time (Z) | limb | act | result |
|---|---|---|---|
| 03:47 | rule | IB2 R34Q census (msg 11845) | 0 rows under `irpt-dashbd-x10-v1` (both hashes) and `irpt-anlreq-audit-x10-v1`; 2524 items scanned; control revision 11 rows |
| 03:5x | L7 verify and merge | worker 354 (AR-g-181) reported; the issuer re-ran the three checks on the official stage | record OK, tree OK, scripts OK; tar sha256 f757171891f3 equals the rehearsal; merged 535aead683f; worktree and branch removed |
| 03:5x | release | r34q never-widen packet f65fe411e3 (blob a453712369), COO half signed | CTO half signed f6949e0502 (msg 11854); the CTO measured that the runner role's GetItem on opal-tickets reads implicitDeny, so the audit is wired but refused |
| 04:0x | apply | TO-APPLY-R34Q cut (22a1f0434c), GO to IB2 (msg 11857) | IB2: r34q live 04:04:17Z, V2S OK, census 7/0/0, receipt 16 of 16, ledger CLOSED (msg 11861) |
| 04:08 | L6 run order | TO-RUN-FWD10-MULTICOMP-7I (d07a3e87dc), holdings fwd10_holdings_7i.csv (3125b93613e2); GO to IB2 (msg 11865) | filed 04:16:14Z: ticket TCK-20261021-26db6ce5, comparables ticked 2, variant multicomp, comparison_keys 2; IB2 polling the resident |

Open: IB2's run 7I receipt and the saved PDF (then the page-by-page read against independent recomputation with `checks/fwd10_read.py` and by eye; the report to the CTO and Y2 names the admission pass, the packager outcome, the audit outcome and the PDF path, size, sha and pages); CVO L9 on FWD-10 after the read; FWD-11 scoping after FWD-10 is met; Y2's ticket-read policy apply waits for 7I's report. Gateway restart window 06:00Z to 06:55Z: no gateway-calling runs in it.
