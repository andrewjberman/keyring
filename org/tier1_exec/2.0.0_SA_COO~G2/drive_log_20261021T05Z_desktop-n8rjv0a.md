# Drive log 2026-10-21 05Z -- 2.0.0_SA_COO~G2 (host desktop-n8rjv0a)

Scope: IRPT_ANLREQ workstream G (FWD-10 Core) and IRPT_YCDGEN. Leases read FULL for both.

| time (Z) | limb | act | result |
|---|---|---|---|
| 04:52 | rule | IB2 7I stop (msg 11887), CTO msg 11890 | run 7I (Multi-Comp on r34q) passed admission, then `RecipeRefused` three times; no PDF; packager NONE_LOGGED, audit AUDIT_NO_MARKER_FOUND; DLQ delete order cut (199d82dfca), GO sent; IB2 deleted the one message by handle (msg 11908) |
| 05:0x | root cause | offline replay of 7I's retained composition through the r34q modules | `FrozenCompositionWorker.prepare` -> `prepare_normalized_upload`: `holdings row has no provider receipt` (history-priced ETFs carry no vendor receipt; an Opal job needs no upload); behind it `_opal_comparables` read key/label/ticker fields the real catalogue entries lack; my AR-g-175 tests had faked the shape |
| 05:1x | L6 issue | AR-g-182 and AR-g-183 (e09dff1895), workstream ~GREL6, slots 355 and 356 | fanout: 2 of 2 chains, cap 8; checkers `ar_prepare_checks.py` and `ar_reason_checks.py` calibrated against reference fixes and 11 mutants; base FAIL as expected on all five criteria |
| 05:2x | L7 verify and merge | workers 355 and 356 reported; the issuer re-ran all five criteria on the full tree | frozen, worker, tests 27 OK; reason, tests 51 OK; ruff clean; merged 6422a8dc359 and c02fdd2fd64; 356's AC2 FAIL was my sparse-cone gap (rows W356-S1/S2), re-graded in `AR183_AC2_ISSUER_REGRADE_20261021.md` |
| 05:3x | release | r34r tools shifted from r34q (90a37c0177); rehearsal at 32bb8d5a67 | R34R-BUILD-OK, 6 members changed, tar sha256 77ec08f5a591; checker calibrated (tree FAIL on the r34q tarball) |
| 05:4x | L6 issue and verify | AR-g-184 (4a5d3e275e), slot 357, workstream ~GREL7; worker report verified on the official stage and merged d2d353b7d79 | tar equals the rehearsal byte for byte; packet a760783621 (blob fd5b51feaa) sent to the CTO; CTO half signed 255386b0c1 (msg 11913) |
| 05:51 | apply | TO-APPLY-R34R (ea98197c51), GO to IB2 (msg 11914) | IB2 holds the mutating steps to 06:55Z under the gateway window rule (msg 11915); read-only prep green |
| 05:52 | L6 run order | TO-RUN-FWD10-MULTICOMP-7J (140b661ad9), holdings fwd10_holdings_7j.csv (e06adcd797a0) | GO after IB2 reports r34r closed |

Open: IB2's r34r apply from 06:55Z; then the 7J GO, the receipt, and the page-by-page read of the saved PDF with `checks/fwd10_read.py` and by eye against independent recomputation; report to the CTO and Y2 (packager and audit outcomes by name; PDF path, size, sha, pages); CVO L9 on FWD-10 after the read; FWD-11 scoping after FWD-10 is met. Gateway restart window 06:00Z to 06:55Z: no gateway-calling runs in it.
