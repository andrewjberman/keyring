# IRPT_ANLREQ workstream TICKET (~V2), round 3 -- L8 PACKET

**Compiled by** `2.0.0_SA_COO~V2`, 2026-10-16 ~08:1xZ, on dell2. **For** the macro reviewer on this box, `3.0.0_SA_CVO~IRPT` (or `3.0.0_SA_CVO`), at L9, as a FILE. This is not the L10 slug. Every commit named here is LOCAL on `box/dell2` unless a line says it is on origin or DEV; push state of the workspace commits is not read.

**Authority:** `decompositions/IRPT_ANLREQ_DECOMP_R3_V.md` (blob `92afe1ef6f`, AMENDMENTS 1 to 4); the CTO's FWD-4 ruling msg 8908 (`CTO_RULING_DELL2_IRPT_ANLREQ_FWD4_HOP_FAILURE_READ_NOT_WRITE_20261016.md`) and PRD v0.21 C-HOP-FAILURE (both halves SIGNED); the status shape from `~G2` msg 9053/9134.

`round-close-check.py --project IRPT_ANLREQ --round 3 --workstream TICKET`: `orders=1 judgment=1 graded=0 ungraded=1 self_graded=0 verdict=REFUSED`. **The only reason is the one ungraded judgment criterion below.** The order is complete, its proof instance is VALID, and every row of the round is dispositioned in the issuer's record (section 3).

## 1. Terminal order

| order | cell | risk | instance (`deliverables/`) | issuer re-run | landed |
|---|---|---|---|---|---|
| TO-AR-v31 (blob `6cdb51e0e4`; AMENDMENTS 1 to 4) | AR-v-31: the ticket page reads a hop failure through the existing status route and shows its words only while no package is attached | LOCAL (portal, Opal-internal, DEV only) | `0.9.0_WK_IRPT_ANLREQ~270/IRPT_ANLREQ.TO-AR-v31.ticket-page-reads-the-hop-failure.proof_of_spec.json` (blob `4e9178db70`, VALID rc=0 on main) | AC1 `V31-FAILURE-OK pass=13` on the PROD-based candidate and on the DEV-based head (issuer runs; the worker reports 13 of 13 on its own tree); AC2 `tsc -b` rc 0; the TicketCenter suite 196 pass 0 fail across 31 files on the DEV-based head (141 pass across 25 on the PROD base); AC3 `MUTANT-FIRES` on `makes no status call for a ticket whose package is attached`, restore verified, tree clean | **portal DEV** `dc057891b086` (ls-remote read 2026-10-16), by `portal-merge-forward.sh` on the CTO's approval row `dell2-20261016T075042Z-a06e` (msg 9185); parents DEV `34a6baf8` and the approved head `bdeeaa88f359`; the merge tree is identical to the tested head's tree |

The PROD-based head `cand/dell2/ticket-hop-failure-read` at `ac828834e433` (approved first as row `d870`) stays on origin for the PROD promote, which the CTO orders after the four overlapping DEV features (XA-20261016T073942Z-102b).
What the cell does (one read of `getJobStatus(request_id, firm)` when the ticket is shown and one on Refresh; the failure's words shown only while no package is attached, for a ticket with or without a draft; the codes: the five silent hops plus `ANALYSIS_FAILED`, `ANALYSIS_REQUIRES_ATTENTION` and `DELIVERIES_EXHAUSTED`; no call for a finished request or a non-analysis ticket; a failed read shows nothing extra) and the thirteen named tests are in the order and in `portal/src/pages/TicketCenter/__tests__/hop-failure-read.test.tsx` on DEV.

## 2. For L9 -- the one judgment (graded on the artifacts, never self-graded)

- **`AR31-v-AC4J`:** the ticket page names the failed step and what happens next only while no package is attached, for a ticket with or without a draft, makes no call it should not, leaves no blank row when there is nothing to say, never breaks the page, and adds no route, write, principal or colour.
- **Read:** the landed diff `git -C portal diff 34a6baf8 dc057891 -- src/pages/TicketCenter` (3 files, +410 -9); the worker's render evidence `0.9.0_WK_IRPT_ANLREQ~270/render_markup.txt` (blob `68b1b8b279`), `render_hop_markup.test.tsx.txt` and `render_row_markup.test.tsx.txt` (the three board-row states: a failure before any draft shows one row; no draft, no package and no failure shows zero rows; a draft with a failure shows one row); the worker's record `R3_V_RECORD.json` (blob `cefb7df663`) and its mutant checker `mutant_check.py` (blob `fe008b2e73`; the issuer re-ran it: it fires and the restore is verified); `deliverables/2.0.0_SA_COO~V2/R3_V_ROW_DISPOSITIONS.md` (blob `2db1598ec1`).
- **Limits of the evidence, stated:** (a) **no screenshot was looked at**: the worker rendered the block in a DOM test (`ui-smoke.mjs` was not run: it needs fixtures nobody validated for this state), so the portal law's "render and READ the page" is met by the DOM markup, not by a pixel render; (b) **no live failure exists yet**: `irpt-status` carries the reader live (`~G2` msg 9134, CodeSha `+TcZDWmw...`), but no job row carries `hop_failure` until the resident writers ship (r34) and the commentary writer lands (`~T2`), so the live arm is not exercised; (c) `DELIVERIES_EXHAUSTED` is held against a producer that exposes it: as written the producer only uses it to select words (`ops/owned_status.py` `PHASES` and `read`, `ops/status.py` `FAILURE_WORDS`), so only the two `ANALYSIS_*` generator codes are reachable today.

## 3. Rows (full dispositions in `R3_V_ROW_DISPOSITIONS.md`)

- `IRPT_ANLREQ-D2-W270-S1` (BLOCKING, ARMED): the draft-axis gap; disarmed by AMENDMENT 1 (the issuer found the same gap in review before the worker reported). `S2` (the firm field) not a defect; `S3` (WAIT and NONE share one adapter action) not a defect for this cell; `S4` (the stale mutant) dispositioned by AMENDMENT 3.
- **The issuer's own misses, stated:** the cut omitted the draft axis; the first version made a status call for every ticket on the board; the mutant it named went stale with its own amendment; its code set held only the hop codes, so a generator failure showed nothing (the CTO declined the first candidate head for exactly that, row `0633`); and "this seat approves the portal candidate" in the CTO's ruling means the CTO, not the issuer.

## 4. What is owed, and when

- **FWD-4's live arm** (each failure driven on purpose against the released status route; the ticket names the step): after the r34 resident writers (waiting on the host's yfinance library) and `~T2`'s commentary writer. Not this cell's.
- **The PROD promote of this page:** after the four overlapping DEV features, in the CTO's promote list.
- **Nothing client-facing:** the block renders only in the internal board (a partner login's view returns before the board).
- **The notice contacts input** (one per client firm, named by Andrew with his client-opening word) is a different item, not this cell's.
