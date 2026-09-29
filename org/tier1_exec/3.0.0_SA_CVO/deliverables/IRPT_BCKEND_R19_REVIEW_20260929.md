# IRPT_BCKEND round 19 -- L8 compile and L9 review (`3.0.0_SA_CVO`)

**Seating:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260928_180xZ_SEATING_CVO.md` @4cfdc2bd49 (L8/L9 for
the three workstreams ~P, ~M, ~Y; PRD v0.18 addendum). **Carriers written:** `surprise-channel/adjudications/ADJUDICATION_v14.md`
(rows C-S223..C-S237) and `surprise-channel/remediations/REMEDIATION_v10.md` (30 rows), co-committed.

## Round state (measured from the order files at CLOUD, 2026-09-29 01:xxZ)

| workstream | order | status | what it proves |
|---|---|---|---|
| ~P | TO-IB-pr-191 (+ IB-pr-194 reopened in place) | complete | the compute guard is served (irpt-performance-adapter `hcZpXDDo`, STATUS~P.md:21); the retained-reopen guard IB-pr-194 is built (@90c4b596f3) and NOT served, so CRO D1 is NOT MET (STATUS~P.md:34) |
| ~P | TO-IB-pr-192 | superseded | Since-inception moves to the holdings-basis gold (PRD v0.19) |
| ~P | TO-IB-pr-193 | complete | an async export replay logs REFUSED, never FAILED |
| ~M | TO-IB-m19-1 | complete | the R1 read-backs ran and FAILED on served output for S173's cause; ruled by the CTO in S188 |
| ~M | TO-IB-m19-2 | complete | R4 holdings re-mint: the QA fire succeeded at all three firms after amendments 1-3; ENABLE half sent (STATUS~M.md:65) |
| ~Y | TO-IB-yr-1 | complete | a saved non-fixed portfolio type refuses before generation (entry-point harness); its served run rides ~P's next resident build |
| ~Y | TO-IB-yr-2 | complete | the lookup-capture test runs from pinned fixtures (suite hygiene) |
| ~E | TO-IB-er-191 | cancelled | Andrew-direct 0b6f598df4 redirects the engine fix into the holdings gold |

Every round-19 order is terminal. No round-19 order carries a JUDGMENT criterion (0 hits across the 7 files), so L9 is
row dispositions only.

## The one served fact this round did not change (P0)

NEW-01 still shows on the page. `2.0.0_SA_COO~D`'s walks of 2026-09-28 22:04Z and 2026-09-29 00:0xZ
(`tmp/ui-walk/20260928T220437Z` shot 011, `tmp/ui-walk/20260929T000244Z` shot 010, md5 `9820db3b70bd588b1af3fe592998afe7`)
read 49F ****9079 / IRA ($99,253.73 held) at "-100.00%" YTD, falling on 2026-04-16. That is S176/S177's account. The
compute guard is served, but the page reopens the RETAINED pre-guard report, and IB-pr-194 is not served. This
seat's row S186 called it "a third account"; that was wrong, and C-S233 disposes it as a duplicate.
TO-IB-pr-191 is `complete` on its criteria; its outcome, D1, is not met on the served page.

## Channel compile

- **Denominator:** 66 undispositioned items on the committed index at 01:3xZ (resolver: `.tools/surprise-row-gate.py`
  `_latest_dispositions`). **Watermark:** 64 compiled here. S189 and S190 (00:40Z, 0.4.0_DS_ClientPlatform~E, cell
  TO-IB-er-201) belong to workstream ~E's round 1 and are left for its L8. S191 (01:05Z, the same cell, BLOCKING ~E's
  first commit) is dispositioned here because the row gate holds every new remediation row until a BLOCKING item is
  dispositioned. Its owner is 1.0.0_SA_CTO.
- **36 dismissed** through 17 adjudication rows, each with its reason:
  - disarmed and read on the carrier: the directory family via CLOUD `schedule.tf`; S148's fence via
    `comp-find --corpus aws`; W42-S1/S2 via the 3/3 QA fire;
  - remedied: S122/S123; S131/S134 by S137; S157 by S170;
  - benign: S130/S133;
  - superseded by PRD v0.19: S143, S158 (also disarmed by S169), S185, S181;
  - ruled by the CTO: W41-S1/S2 by S188;
  - duplicates: S186, S177, S184, and the proof-name class rows.
- **28 graduated OPEN** to owned remediation rows. Priority: P0 1 (S176); P1 6 (S173, S155, S182, S165, S132, S191);
  P2 the other 21. **ARMED rows carried OPEN with a named owner:** S176, S173, S155, S182, S147, S149, S151, S152,
  S165, S166, W62-S1.
- **16 closed remediation rows** for items their authors had already GRADUATED with no remediation row (S129, S136,
  S137, S150, S159-S164, S167-S172). The row gate refused the slug without them. Each is written REMEDIATED on its own
  record.

| owner | open remediation rows |
|---|---|
| 2.0.0_SA_COO~P | S176 (P0), S147, W62-S1, S175, S178, S180 |
| 2.0.0_SA_COO~M | S155, S182, S152, S145, S174 |
| 2.0.0_SA_COO~Y | S151, S144, S119, S121, S120 |
| 1.0.0_SA_CTO | S173, S165, S166, S132, S191, W42-S4, S187, W42-S3 |
| 0.0.0_AB_MSTR | S118, S124, S141 |
| 0.7.0_AE_CloudOps (via the CTO) | S149 |

## What you should have asked but did not

Whether a `complete` order means its outcome holds on the page. TO-IB-pr-191 flipped complete on a valid proof-of-spec,
while the page served the exact figure the order exists to stop. The criteria graded the compute path, and the page
reads the retained path. The mechanical bar cannot see a second reader of the same figure. STATUS~P.md:70 already names
the fix for this case ("both readers of the served figure counted: compute AND reopen"). The unasked question is whether
L6 should require every order that changes a served figure to name ALL of that figure's readers in its criteria, so a
round cannot close green while the page is red. Recommend the CTO's round-19 analysis answer it once, as an L6 rule,
rather than per order.

-- 3.0.0_SA_CVO
