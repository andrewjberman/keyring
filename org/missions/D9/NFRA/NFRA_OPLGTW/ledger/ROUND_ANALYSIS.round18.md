# NFRA_OPLGTW -- ROUND 18 ANALYSIS (L10), `1.0.0_SA_CTO~O`, 2026-10-06 ~02:2xZ

**L10 on `3.0.0_SA_CVO~O`'s round-18 slug** (msg 29857, `surprise-channel/remediations/REMEDIATION_v6.md` @a4992dba0c):
- 5 rows: 3 dismissed and 2 graduated OPEN, both the issuer's.
- 5 rows advanced to REMEDIATED in place: Z-W15-S37, S51, S36, S47 and Z-W16-S5.
- No L9 grade.

**The issuer's terminal message** is msg 29851: round 18 is terminal at 4 of 4, last drain `0fe94c71e2`.

**Issuer: `2.0.0_SA_COO~O`.** ONE issuance, section 4.

## 1. What round 18 did

- **OG-pm-2, finding MIX (R17 branch (i)).**
  - The routes that existed at OG-p-1 read p95 0.515 s on 2026-10-05 and 0.538 s on 09-30. Both are under the 0.6642 s
    cap and under OG-p-1's own 0.5535 s.
  - The breach is the teamsassist poller of `GET /hx/teams/chats`: 60 per hour since 10-02, p95 1.02 s, and 70% of the
    quiet-hour requests (rows Z-W27-S4, S5).
  - No existing route slowed.
- **OG-ln-1 (R16).**
  - 0 live-only lines remain.
  - 18 CLOUD-only items are listed in `LINEAGE_R18.json`, each with its owning cell, all `SHIPS_IN_RELEASE`.
  - `RELEASE_ORDER_FORM.md` carries the DRAIN-BACK step and the pre-GO check exercise.
- **OG-ti-2.** The schwab set runs in one process: 147 collected, 0 errors, no reset seam (Z-W15-S37 REMEDIATED).
- **OG-dc-1.** `.tools/m365-mcp-kit/README.md` is the hosted-gateway reconnect, read at HEAD this turn: remove the old
  entry, `claude mcp add --transport http -s user opalgateway https://mcp.opalinvest.dev/mcp`, then work-account sign-in.

## 2. Outcome grades

| FWD | grade | why |
|---|---|---|
| FWD-1 | HELD | OG-v-7: Andrew's own tests, then Alyssa. G-E stands. |
| FWD-2 | HELD | Unchanged since round 17. |
| FWD-3 | HELD | Unchanged. |
| FWD-4 | HELD | Z-W15-S41 is at Andrew: the grant write of `download_filtered`. |
| FWD-5 | HELD | Unchanged. |
| FWD-6 | HELD | Unchanged. |
| FWD-7 | **HELD** (was NOT_REALIZED) | OG-pm-2: OG-p-1's routes are at 0.515 s, under the cap, and the breach was a new caller's own route (R19). The walkthrough remains. |
| FWD-8 | HELD | Unchanged. |

**Tally: 0 REALIZED, 0 NOT_REALIZED, 8 HELD, 0 DEFERRED** (round 17: 0 / 1 / 7 / 0).
- Every outcome now waits on a human act: OG-v-7 (Andrew's own tests, then Alyssa), G-E (Menachem's tid/oid), the
  S41 grant word, and R7's host-side flag.
- No engineering cell is owed to any FWD.

## 3. Rulings

**R19 -- the latency cap is per route (Z-W27-S3, R17 branch (i)).**
- **OG-p-1's routes** keep the 0.6642 s p95 cap, measured per route with OG-pm-2's instrument.
- **A route added since OG-p-1** takes its own reference: its p95 over its first full trading day, with a cap of +20 %.
  For `GET /hx/teams/chats` that is 1.02 s, so its cap is 1.224 s.
- **The aggregate ALB p95** depends on the request mix. It is RETIRED as a grade and kept as a diagnostic only.
- **Not a relaxation.** The cap came from the OG-r-3 order form, not ratified text, and no existing route's bar moves.
- Z-W27-S3 closes ACCEPTED_BY_RULING R19; the CVO writes the clock on this word (@cc05804f8f).

**R20 -- the rows routed to this seat.**
- **Z-S55 (the onboarding kit): REMEDIATED**, on the HEAD read in section 1. The CVO writes the clock.
- **Z-W15-S41:** still at Andrew. REC unchanged: yes.

**R21 -- the release-order form gains one pre-GO arm.**
- A release that adds or removes a route runs `tests/test_principal_cutover.py`'s ROUTE_CLASS inventory and
  `tests/test_data_entitlement_guard.py`'s route census in its pre-GO exercise.
- r17c shipped `/yearinreview` without a ROUTE_CLASS entry (Z-W22-S10).
- Live was not exposed: the deployed verify read 401 with no identity and 403 for a non-owner. The inventory, though,
  is the one place every route's auth class is declared, and a release must not leave it stale.

## 4. THE ENRICHMENT LIST ROUND 19 CUTS (one issuance, `2.0.0_SA_COO~O`)

1. **OG-ts-2 (LOCAL test cell): Z-W22-S10.**
   - Classify `/yearinreview` and `/yearinreview/` in ROUTE_CLASS, with the same class as `/sprint`.
   - Bump the host-inputs key count to 51.
   - Align the `build_package` call to CLOUD's signature.
   - Remove the S9 pair from the baseline, so that each file runs green in its own process.
   - Also Z-W25-S3: give each test process its own export directory, so that two concurrent schwab runs both pass.
2. **OG-rl-7 (release): the CLOUD-only items onto live `37be3485db`, under three halves.** After it, CLOUD equals live
   for the gateway tree.
   - **Behaviour changes, each named in the ask with both branches:**
     - `admin_refusals.py` (NFRA_MCPMSP MS-sg-1, sender fields from entry args only);
     - `envelope.py` (OG-o-4, the narrow page);
     - `server.py` (NFRA_OPALAI OA-e-10, `/login` narrowed to the configured server identities).
   - **OA-e-10's admit lists (R16):** the ask names who `/login` admits before and after, from 30 days of live audit.
     An identity that used `/login` in that window and falls outside the configured set BLOCKS the release.
   - The runbook, the walkthrough protocol and the tests ride along; they are not service behaviour.
   - Follow `RELEASE_ORDER_FORM.md` in full, including the DRAIN-BACK step and R21's pre-GO arm.

**Stated dependencies, not cells:**
- Z-W15-S41 is at Andrew.
- OG-v-7: Andrew's own tests, then Alyssa.
- G-E: Menachem's tid/oid.
- R7's host-side flag.
- Z-S43: the meeting invitation.

## 5. What this analysis does not do

It deploys, applies and grants nothing. It re-measured only:
- `.tools/m365-mcp-kit/README.md` at HEAD;
- `LINEAGE_R18.json` (18 items, all SHIPS_IN_RELEASE);
- ROUTE_CLASS's call sites (`test_principal_cutover.py:489-598`, `test_data_entitlement_guard.py:719-729`).
