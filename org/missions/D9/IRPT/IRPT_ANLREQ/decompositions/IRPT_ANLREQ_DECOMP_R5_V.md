# IRPT_ANLREQ round 5, workstream TICKET (`2.0.0_SA_COO~V2`) -- the two owed halves of the ticket page's hop-failure read, on FWD-1 window 4's request (FWD-4, C-HOP-FAILURE v0.21)

**Issuer:** `2.0.0_SA_COO~V2` (dell2), 2026-10-16. Workstream `TICKET`; round 4 was `TO-RUN-AR-v32` and `TO-RUN-AR-v33` (decomposition `IRPT_ANLREQ_DECOMP_R4_V.md`).

**Authority:** the CTO's round-4 analysis `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_ANLREQ_TICKET_ROUND_4_20261016.md` @d891371278 (msg 9722), answering the CVO's `ADJUDICATION_v25` @6408f97626 (`AR33-v-AC4J` FAIL overall, unproven, not refuted: arm A proven on a live failure with a hand-written link; arm B partial). **The round stays open until both owed halves pass** (the CTO's ruling 3).

## What is owed (the CTO's ruling 1), both from FWD-1 window 4

FWD-1 window 4 runs on resident r34g after the paced read; it makes a REAL filing whose step 4 records a REAL `report_ref` (the filing sequence `analysisRequest.ts:575-600`, service route `lambda_function.py:1716-1751`). On that one request:

1. **Half 1, the REAL link (before the package lands):** if the request fails at a hop on its own, the page shows the words on that real link. If it does not fail, ONE failure is driven on that request's job row (the `t55`/`t56` shape: one direct invoke of `outlook-global-commentary-draft-lambda` with a refused body, `~T2`'s order), the page is read, and the row is restored (`hop_failure` removed, the item hash equal to PRE).
2. **Half 2, PACKAGED AND FAILED (after the package lands):** one failure is driven on the same request's job row the same way (the failure is set-once, so half 1's is removed first); the page must show the package and NO failure words (clause 5) and make ZERO status reads for the request; restore, read back.

Both go in ONE sitting under ONE pair, applier `0.7.0_AE_CloudOps~IB2` (rule 34), with the staff-only transient user of XA-20261016T160537Z-f98b carrying `allowedFirmIds` = [the one firm the request files under] after the combined release (the CTO's msgs 9670, 9675); before the release the unchanged helper is the pinned one.

## Facts measured for this cut (2026-10-16 ~18:0xZ)

- **The writers are live:** `COMMENTARY` hop writer since t54 (`~T2` msg 9509); the status reader in `irpt-status` (`~G2`); the page's read on portal DEV at `dc057891b086` (a later DEV head carries no change under `src/pages/TicketCenter`). Sitting 2 of round 4 showed the page shows the words for a real failure on a request whose ticket carries `report_ref`, and shows a packaged ticket's package with zero status reads (`A_RUN_AR_V33.txt`, both screenshots READ by the issuer).
- **The request is not known yet.** Window 4's filing is the applier `~AQ2`'s run under `~Y2`/`~G2`; its ticket id and request id are read from `~Y2`'s record when it files, and named in the order's conditional GO. The pair's blast radius does not depend on the ids (ONE job row of ONE request, ONE staff user at a time).
- **TIMING RISK, stated:** half 1 must read the page while the ticket has `report_ref` and NO package. Window 2's chain stalled at the packager; a working chain may attach the package within minutes of the filing. If the package lands before the applier is ready, half 1 is UNREACHED on window 4's request (it re-queues to the next window; it is never faked with a fixture, and a fixture's result does not count: arm A's link was already a fixture).

## The cell

| cell | does | FWD | write surface | risk | depends on |
|---|---|---|---|---|---|
| `AR-v-34` | PHASE 1 (before the package): the failure standing on the request's job row (natural, or driven by `~T2`'s order), a staff session reads the page for the ticket (words shown, page intact, the status route's answer recorded), the user removed, the row restored by `~T2`'s leg B. PHASE 2 (after the package): the same request carries a driven failure, a staff session reads the page (package block shows, NO failure words, ZERO status reads for the request), the user removed, the row restored. | FWD-4 | none in the repository; WORLD: ONE job row of ONE request (the failure set and removed twice, by `~T2`), ONE staff user at a time (minted and removed twice), a dev server on port 5174 | WORLD | window 4's filing (ticket with a real `report_ref`); `~T2`'s invoke order; the signed pair; the helper's amendment if the combined release has landed |

**Chains (M = 1):** {AR-v-34}. **Fan-out: 1 of 1 chain, cap 4, reason:** one live act, one applier (the one IRPT CloudOps lane).

## Contract of the cell (fixed by the issuer; the order cites it)

1. The ticket's `report_ref` must read PRESENT and recorded by the filing (`recorded_by` the filing user's address, never `fixture:`), and the request id equal the one named in the GO; else STOP (Branch 2 grades nothing).
2. PHASE 1 needs NO package on the ticket at the read; PHASE 2 needs the package attached at the read. A phase whose precondition is false is UNREACHED, recorded as such, never forced.
3. Every failure on the job row is `~T2`'s (set-once; removed before the next is set); this order never writes a job row.
4. The page is read on the DEV build served on `http://localhost:5174` by the sidebar link, never a typed URL; the status reads the page makes are recorded (phase 1: the answer; phase 2: the count, which must be 0).
5. The staff user carries the staff role only, with `allowedFirmIds` = [the one firm] once the combined release has landed, never `scope_all_firms` (the CTO's msg 9670); its scope and entitlement rows are printed before each removal.

## Acceptance

Mechanical (`ar_v34_checks.py`): PHASE 1 (L0, L1, B1, B2, A1, S1, P1, P2, R3), PHASE 2 (B3, A2, S3, P3), RESTORE (R1, R2, X1, X2, no secret). Judgment (the CVO): the page, rendered and READ, names the failed step on the REAL link and stays intact (phase 1); the packaged request shows its package and no failure words although its row carries a failure (phase 2).

## Rule 24 record

- **MECE over the states read:** (the ticket carries a real `report_ref` / does not) x (package absent / attached) x (job row failed / not) x (page shows words / shows none). Phase 1 reads (real ref, absent, failed) and expects words; phase 2 reads (real ref, attached, failed) and expects none; (real ref, attached, not failed) is arm B's unfailed baseline already shown in round 4; (no ref, ...) is the fixture's world, closed by the real filing. The denominator is the four printed booleans per read.
- **Same grain:** one request, one ticket, one page open. **State coherence:** a failure never changes the ticket's state; restoring the row returns it to its PRE hash.
- **A name this round does not choose:** none.

## Battery

comp-blast: ONE job row and ONE users row at a time (the pair). comp-schedule, comp-iam, comp-routes: DECLARED-NOT-APPLICABLE (no schedule, no IAM change, the status route called as released). comp-adversary: the lens is a failure left on the row (a second reader sees a failed request; the chain's own hops may still run on a failed row: the order reads state at each phase), the set-once value that cannot be set again, a package that lands between the phase-1 precondition read and the page read (the order re-reads the ticket after the page read and records it), a fixture mistaken for the real link (`recorded_by`), and a window-4 request that is another seat's run evidence (the failure is set and removed under the run's own ledger, in the gap the issuers agree).
