# NFRA_OPLGTW -- ROUND 27 ANALYSIS (L10)

**Author:** `1.0.0_SA_CTO~Z`, 2026-10-07 ~18:0xZ, in the place of `1.0.0_SA_CTO~O` (not live).
**Slug:** `3.0.0_SA_CVO~Z` msg 31246, `surprise-channel/adjudications/ADJUDICATION_v19.Z.md` @e41e02011b (LOCAL). The slug message
was read; the adjudication file was not read line by line by this seat.
**Round:** one order, OG-rl-13, the r27 gateway release. Terminal: live `510c8cfed2` since 16:57:30Z (`2.0.0_SA_COO~O` msg 31226).

## 1. What the round did

- r27 is live. `rl13.AC1` PASS (3 of 3 host files) and `rl13.AC2` PASS by the issuer's re-grade at 17:29Z.
- The status tool's `displayed_date` now returns the manifest's `generated_at`.
- The rivalfunds audit records keep `day`, `route` and `fund`, with `bytes` (round-24 ruling R36).
- The sign-in cache was not opened in Phase B (the CTO half's ruling on section 4 (a)).
- Rows: Z-S64 and Z-W28-S13 REMEDIATED; Z-W28-S19 DISARMED and REMEDIATED; 4 graduated, 3 dismissed; 0 open, 1 ARMED.

## 2. What is NOT yet shown

**R36 has no acceptance on the audit lake.** No rivalfunds record had reached the S3 audit lake at 17:05Z (53 objects, one read).
Phase A used scratch sinks. So the record's shape is proven on the gateway's own sink and not on the lake. The first lake record
after a real page view is the acceptance, and Andrew's own look at /rivalfunds (asked of him for ETFS_RIVALS today) produces one.

## 3. Rulings

| # | row | ruling | why |
|---|---|---|---|
| R39 | Z-W28-S24: `deploy-to-ec2.sh` runs `bun install` on every gateway deploy | No gateway deploy from site Z until the install step FAILS on a cache miss and never fetches (cell OG-bi-1, issued @7cc16c57ac). The 16:55Z and 14:02Z installs are accepted as CACHE-ONLY for package content: 0 of 6,441 cache entries touched today. A metadata request that wrote nothing is not excluded. | Andrew's no-fetch word. The script would fetch on a miss; today's result rested on a warm cache. |
| R40 | the same script's host step, `pip install --upgrade pip` and `pip install -r requirements.txt` on the EC2 host | A second cell removes `--upgrade pip`. The requirements line stays. A release whose diff touches `requirements.txt` comes to this seat before its pair. | Whether an AWS host is a "box" under Andrew's word is his to say; asked at ~17:4xZ, unanswered. These terms hold under either reading. r27's host log read 48 already satisfied, 0 downloads. |
| R41 | Z-W28-S20: the principal source | The release form names the source of any principal identifier a check needs. The sign-in cache is never one. | Round 27's Phase A opened it once on a worker's choice because the order named no source. |
| R42 | Z-W28-S21 (ARMED): a republish can look like a change | The release form carries the page-time read: BEFORE and AFTER taken in the deploy window, and a difference counts only if the object's `LastModified` did not move. ARMED until the form carries it. | As amendment A2 did by hand in this round. |
| R43 | Z-W28-S26: an audit-lake key with an empty timestamp | One cell reads which writer produced it and fixes the key's stamp at the writer. | A key with an empty time segment sorts wrongly and may collide. Not read by this seat. |
| R44 | the half's note on `displayed_date` | The next form edit states that the value is the time the manifest was generated, not the data's as-of date. | A re-publish of an older date would read as today's. |

**Own-act correction:** this seat's r27 half read the release's diff and not the deploy script that ships it. R39 is the result.
From here a CTO half on a deploy names the script that runs and the install or download lines in it, from the census
`org/tier0_exec/0.0.0_AB_MSTR~Z/deliverables/SITEZ_INSTALL_DOWNLOAD_LINE_CENSUS_20261007.md` @543bee5743.

## 4. ENRICHMENT LIST (round 28, one issuance by `2.0.0_SA_COO~O`)

1. OG-bi-1: the bun install step fails on a cache miss, with the negative control (issued).
2. Remove `pip install --upgrade pip` from the host step (R40).
3. The release form: the principal source (R41), the page-time read (R42), the `displayed_date` sentence (R44).
4. The audit-lake key with an empty timestamp (R43).
5. Read the first rivalfunds record on the audit lake: `day`, `route`, `bytes`, and no other arg (R36's acceptance).

## 5. ACTS ONLY ANDREW CAN DO (cited)

- His word on whether "no fetch on any box" covers an AWS host installing its own packages at deploy. It is his word; this seat
  does not widen or narrow it (CLAUDE.md section 2, DO NOT MANUFACTURE FRICTION (b)).

-- 1.0.0_SA_CTO~Z

## ADDENDUM 1 -- ROUND 28 (2026-10-07 ~18:4xZ), on `3.0.0_SA_CVO~Z` slug msg 31258 (`ADJUDICATION_v20.Z.md` @491389285e)

Round 28 ran items 1 to 3 of section 4: OG-bi-1 and OG-bi-2 complete and drained @8ab8d612a0 (`2.0.0_SA_COO~O` msg 31253); the
release form @ce3a1e8a08. Rows Z-W28-S24 and Z-W28-S20 REMEDIATED, Z-W28-S21 DISARMED and REMEDIATED, on the CVO's own run of
the three test files (13 of 13). 0 open rows but Z-W28-S26; 0 ARMED.

**R39's hold was lifted by this seat at ~18:3xZ (msg 31254), before this slug.** The slug states a limit that ruling did not
have: the pre-check tests that each lockfile entry's cache DIRECTORY EXISTS, not that it is complete. A directory left partial
would pass, and the install would then fetch. The lift stands, with one term added:

- **R45.** The first gateway deploy under the pre-check carries its own control: after the install, the count of bun cache entries
  created or modified since the deploy began is read, and it is 0. Above 0 is a fetch: the release stops there and it comes to this
  seat as a BLOCKING row. That read is in the release form from now on.
- **R46.** One cell in round 29 makes the pre-check test completeness (the entry against the lockfile's own integrity value, or
  bun's own record of a finished entry), with a negative control of a directory that exists and is empty.

**ENRICHMENT LIST, round 29** (one issuance by `2.0.0_SA_COO~O`): R46; the audit-lake key with an empty timestamp, deployed
(Z-W28-S26, which waits on a release); the read of the first rivalfunds record on the audit lake (R36's acceptance); the
metadata-request measurement, if a read exists that decides it without a fetch.

-- 1.0.0_SA_CTO~Z
