# NFRA_OPLGTW -- ROUND 17 ANALYSIS (L10), `1.0.0_SA_CTO~O`, 2026-10-06 ~01:xxZ

**L10 on `3.0.0_SA_CVO~O`'s round-17 slug** (msg 29839, `surprise-channel/remediations/REMEDIATION_v5.md` @62493191ea):
- 15 rows: 10 dismissed and 5 graduated OPEN, 4 of them to this seat.
- No L9 grade.
- The channel reads 0 open of 339.

**The issuer's terminal message** is msg 29836: round 17 is terminal at 6 of 6. Release r17 `e91819e281` and r17c
`37be3485db` are LIVE.

**Issuer: `2.0.0_SA_COO~O`.** ONE issuance, section 4.

## 1. What round 17 did

- **OG-q-7, then OG-rl-6 (r17 `e91819e281`, LIVE).** The `dim_asset` download and export paths apply C3's holdings
  restriction: held-only (49 of a 2,160-CUSIP universe, 0 unheld), and an empty holding set is REFUSED. Three halves.
- **OG-rl-6 C2 (r17c `37be3485db`, LIVE).** `/yearinreview` is owner-only, through its own fail-closed roster (R15).
  - The verify passed 19 of 19, including the CVO's T2 arms.
  - `.env` has 51 names, and the prior 50 value hashes are equal.
  - The owner's 200 stays UNEXERCISED until Andrew opens the page.
- **OG-gr-4.** `dim_balance`'s grain `(account,)` is UNIQUE on 28 of 28 served snapshots (0 duplicate keys), and a rows
  page is served (synthetic principal, 0 writes).
- **OG-ti-1.** The schwab set runs in one process: 134 collected, 133 passed, 0 errors, plus the baseline failure.
  Isolation is still incomplete (Z-W15-S37, Z-W15-S40).
- **OG-pm-1.** The p95 re-measure ran on the first full trading day, 2026-10-05, and confirms the regression
  (Z-W27-S3, below).

## 2. Outcome grades

| FWD | grade | why |
|---|---|---|
| FWD-1 (Menachem, Schwab, work Claude) | HELD | Unchanged: OG-v-7 waits on Andrew's own tests, then Alyssa. G-E stands. |
| FWD-2 (accurate answers, masters separate) | **HELD** (was NOT_REALIZED) | The round-16 bar is met: `dim_balance` is UNIQUE and SERVED on 28 of 28 (OG-gr-4), and holdings page on R9. The EXERCISED proof (chosen examples against independent answers) runs at the walkthrough. |
| FWD-3 (each sees only their grant) | HELD | Unchanged. |
| FWD-4 (download equals query) | **HELD** (was NOT_REALIZED) | The capability is served: `dim_asset` downloads are held-only under C3 on `e91819e281`, matching the query. No REAL principal can exercise it, because the one live `dim_asset` grant lacks `download_filtered` (Z-W15-S41). That grant write is Andrew's word (section 3, R18), and then the walkthrough follows. |
| FWD-5 (scope, date, limits) | HELD | Unchanged. |
| FWD-6 (change or revoke) | HELD | Unchanged. |
| FWD-7 (existing users keep working) | **NOT_REALIZED** (was HELD) | The gateway target's full-day p95 is 0.9473 s against the 0.6642 s cap (Z-W27-S3). Every release served that day is over the cap. Until OG-pm-2 (section 4) shows the breach is a mix artifact, it reads against existing users. |
| FWD-8 (support and withdraw the pilot) | HELD | Unchanged. |

**Tally: 0 REALIZED, 1 NOT_REALIZED, 7 HELD, 0 DEFERRED** (round 16: 0 / 2 / 6 / 0).

## 3. Rulings

**R16 -- the gateway's source lineage (Z-W15-S47): (a). CLOUD is the source of record, and every release drains back.**
- **The current state.** Releases are cut on live, so CLOUD and live have diverged both ways:
  - live carries template lines and the `environ_with_external_ids` call that CLOUD lacks;
  - CLOUD carries cells that were drained but never released.
  Every release now re-proves its diff against two bases, and a CLOUD-based cut would regress live.
- **The rule.** The release-order form gains a final DRAIN-BACK step. After the post-act read, the release branch's
  gateway files merge to CLOUD, so CLOUD equals live plus a LISTED set of CLOUD-only pending items.
- **One-time reconcile: OG-ln-1** (section 4).
  - Every difference between CLOUD and live `37be3485db` under `infra/aws/ec2/opal-gateway/` is classified.
  - LIVE-ONLY lines port to CLOUD.
  - Each CLOUD-ONLY item is listed with its owning cell and a disposition: ships in a named release, or reverts on its
    owner's word.
- **Why not (b).** Naming CLOUD "not the source" leaves the trunk wrong forever and pushes the two-base proof onto every
  future cell.
- **OA-e-10** (NFRA_OPALAI, `/login` narrowed to the configured server identities, fail closed, drained @09dc173612,
  never released) is the first CLOUD-only item.
  - It ships in a named gateway release after OG-ln-1.
  - Its halves name WHO `/login` admits before and after, measured from 30 days of live audit.
  - Any identity that used `/login` in that window and falls outside the configured set blocks the release. It is never
    discovered as an outage.

**R17 -- the p95 regression (Z-W27-S3): a cause read before any fix or any cap ruling.**
- **The data.**
  - Day-level reads (Z-W27-S2) were 0.545 s on 09-30 and 0.606 s on 10-01, both under the cap, then 0.897 s on 10-02.
  - So the jump PREDATES round 16's Schwab serving.
  - It begins on the day OG-rl-3 (`/hx/teams`) released.
  - On 10-05, 23 of 24 hours are near 1 s at 60-151 requests an hour. The one high-volume hour (02Z, 1,356 requests)
    is under the cap.
- **Two causes fit and must be separated.**
  - (i) A MIX artifact: a new steady caller of a slow, Graph-backed route since 10-02 (for example a poller of
    `/hx/teams`) dominates p95 in the quiet hours.
  - (ii) A slowdown of routes that existed at OG-p-1.
- **The read: OG-pm-2.** The ruling follows the read:
  - **If (i):** the cap is re-stated per route against OG-p-1's own routes, and new routes get their own reference. That
    is a measurement-method ruling, not a relaxation.
  - **If (ii):** a fix cell follows.

**R18 -- rows routed to this seat.**
- **Z-W15-S41 (FWD-4 has no real principal):** AT ANDREW.
  - The call: write `download_filtered` onto the one live `dim_asset` grant. The state store holds 1 distinct principal.
  - PRD v1.7 reserves every grant change to his word.
  - REC: yes. It adds no data the holder cannot already query, the file is held-only under C3, and the post-act read is
    a real download.
  - Until he answers, FWD-4 stays HELD on it.
- **Z-S55 (the stale onboarding kit):** a LOCAL doc cell, OG-dc-1 (section 4).
- **Z-W15-S51 (checks graded against anchors they cannot read), the issuer's row:** the remedy is ACCEPTED as a standing
  release-order step. Each new or reused check runs once against the release tree BEFORE GO, with its expected PASS and
  one negative control, and runs again on any amendment, `.env`-shape change or step-order change.

## 4. THE ENRICHMENT LIST ROUND 18 CUTS (one issuance, `2.0.0_SA_COO~O`)

1. **OG-pm-2 (read-only): the latency cause read.**
   - Read the per-route (and, where recorded, per-caller) request count and p95 for 2026-10-05 and for 2026-09-30, from
     the gateway's own audit records or the ALB access logs. Name the instrument used and what it cannot see.
   - Report the routes that existed at OG-p-1 separately from the routes added since.
   - Test hypothesis (i) first: is there a steady caller since 10-02, and what are its route, its rate and its p95?
   - 0 writes.
2. **OG-ln-1: the lineage reconcile (R16).**
   - Classify every CLOUD-vs-live difference under `infra/aws/ec2/opal-gateway/`.
   - Port the LIVE-ONLY lines to CLOUD.
   - Write the CLOUD-ONLY list, each item with its owner and disposition.
   - The release-order form gains the DRAIN-BACK step and Z-W15-S51's pre-GO check exercise.
   - LOCAL: no release.
3. **OG-dc-1 (LOCAL doc): Z-S55.** Rewrite `.tools/m365-mcp-kit/`, or retire it with a pointer, to the hosted-gateway
   reconnect:
   - remove the old entry;
   - `claude mcp add --transport http -s user opalgateway https://mcp.opalinvest.dev/mcp`;
   - authenticate with the work account.
4. **Z-W15-S37 / S40:** finish the one-process isolation, so that the full set runs with 0 setup errors and no
   per-module reset seam.

**Stated dependencies, not cells:**
- Z-W15-S41 is at Andrew (R18).
- OG-v-7 waits on Andrew's own tests, then Alyssa. It is where FWD-1 through FWD-6 and FWD-8 are exercised.
- The pilot waits on G-E and on R7's host-side flag.
- Z-S43 waits on the meeting invitation.
- OA-e-10 ships after OG-ln-1 under R16's terms.

## 5. What this analysis does not do

It deploys, applies and grants nothing. It re-measured only from git and the repository:
- the five graduated rows and Z-W27-S2;
- OG-gr-4's completion commit (@fb9317b042);
- OA-e-10's drain (@09dc173612);
- the r17 and r17c releases this seat signed (@de3381d39f, @86e34b783d).
