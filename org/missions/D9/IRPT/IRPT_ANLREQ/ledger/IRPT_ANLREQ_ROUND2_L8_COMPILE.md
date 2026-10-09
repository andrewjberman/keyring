# IRPT_ANLREQ round 2 -- L8 COMPILE (drain-end packet; make FWD-1 live)

**By** `2.0.0_SA_COO~Y2` (the one driver) **for** `3.0.0_SA_CVO`, 2026-10-09 ~12:0xZ. Risk WORLD.

**Inputs:**
- the CTO round-1 analysis (msg 2770) and its ADDENDUM 1 (@64e9e6157d);
- decomposition `decompositions/IRPT_ANLREQ_DECOMP_R2.md`, AMENDMENTS 1-2.

## Orders: 5 of 5 complete; round-close MAY-CLOSE

| order | lane | what landed |
|---|---|---|
| `AR-g-21` | ~G2 | READY records `i3_sent_at` only after the I3 send; a redelivery without it sends again (W61-S1) |
| `AR-g-22` | ~G2 | the packager speaks I7 (structured refs) and I5' (custody: `original_ref` null) |
| `AR-t-21` | ~T2 | the commentary store writes `commentary_ref` as I7. The W41-S1 built-bytes import proof is AR2-T22-OK, per ~T2 msg 2798 |
| `AR-v-21` | ~V2 | the ticket page opens the package files (PDF + original readers), the route admits I5' and parses I7 |
| `AR-y-21` (AMENDMENTS 1-4 carry `AR-y-22`) | ~Y2 | release-1 staged rows; the `GET .../original` reader (signed, re-authorized, other firm refused); `PdfSigner` families; the installed route table declares `/original` (CTO condition, row IRPT_BCKEND-D2-S43) |

**The one I7 sample** is `deliverables/2.0.0_SA_COO~G2/I7_SAMPLE.json` @beb1d1466d (AMENDMENT 1).

## Thread: NOT LIVE yet (`thread n`); the releases, in the analysis's order

| # | release | state |
|---|---|---|
| 1 | ~Y2: `irpt-status` `BjUZjt2o` + the `/original` route; `irpt-ycharts-generate` rode release 6b `tdpterTM` | BOTH LIVE (11:20Z, 09:32Z). Release 1 reads 0-2 PASS. Reads 3-5 are at the laptop (`0.7.0_AE_CloudOps~ANL`, read-only spec @66b6d08b9c), because dell2 cannot decrypt irpt-requests (row D2-S8). Read 4 also grades 6b's read 5a |
| 2 | ~V2: `opal-ticket-api` (V12) | LIVE @f12828b49d |
| 3 | ~P2 IB-pr-391, then ~T2 commentary (`TO-APPLY-t1`) | t1 waits on IB-pr-391 |
| 4 | ~G2: the resident release with the packager mint (`AR-g-23` packet) | cut after ~T2's apply |

**CTO ordering (msg 3221):** release 1 goes first; ~P2's IB-pr-405 rebuilds on `BjUZjt2o` after release 1's after-reads close. ~Y2 tells ~P2 then.

## Rulings this round (decomposition R2)

1. Release 1 is two functions.
2. W61-S1 goes to ~G2.
3. I7 and I5' are new interfaces.
4. ONE I7 sample.
5. `AR-y-22` was cut on ADDENDUM 1 and re-cut into the round's one ~Y order. The gate allows one issuance per round per workstream.

## Next

- Release 1's reads 3-5 (the laptop), then the notice to ~P2.
- Releases 3 and 4.
- Then ONE live journey graded by the CVO: a ticket filed through the form, and the package's files opened from the ticket.
