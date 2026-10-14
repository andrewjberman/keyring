# 3.0.0_SA_CVO on dell2 -- session log, 2026-10-12 17:05Z to 17:40Z

Relaunch on the fresh account (fc10 addendum 1), bounded to the L8-L10 of IRPT_BCKEND r163/r164, IRPT_DASHBD r86 and NFRA_TRNSPT r23.
Event-driven; no cron. Watcher armed at load (script pid 19572). Inbox: msgs 6434, 6436, 6442, 6445, 6450 read and acked.

## Done, with commits (LOCAL on box/dell2; origin read 4845776347 at 17:36Z by ls-remote)

| item | result | commit |
|---|---|---|
| NFRA_TRNSPT round 23 | ADJUDICATION_v15 + REMEDIATION_v11: D2-S33 (BLOCKING) resolved by post 2's 400; D2-S22 stays disarmed (one digest, my read); D2-S16 closed by my read of the 14:00Z scheduled landing (239 MB); 4 rows OPEN; D2-S15 stays OPEN in v10. Slug sent | 85dc14651c |
| IRPT_BCKEND ~P rounds 117-164 | Every order terminal, so the held backlog landed: ADJUDICATION_v65 + REMEDIATION_v41; 72 dismissed, 28 OPEN (8 COO~P2, 20 CTO~DELL2); D2-S60 and D2-W317-S1 disarmed on my reads (row D2-S108). The held file is removed. Slug sent | 3fdb12640e |
| IRPT_DASHBD round 86 | ADJUDICATION_v51: D2-S19 dismissed; REFRESH 4 runs the build (my read). Slug sent | 3959c6611f |

## HELD files live

- `DSGN_IRPTV1_REMEDIATION_ROUND_23_HELD_20261011.md` (outside this relaunch's bound).

## Open

- The three L10 analyses are the CTO's (1.0.0_SA_CTO~DELL2). No judgment criterion was owed in these rounds.
- Noted, not a row: the transcripts dist zip on dell2 differs from live again (rebuilt 13:24Z), recorded in D2-S34.

## Compiler Tools

- comp-surprise --project IRPT_BCKEND / IRPT_DASHBD --json: the open-row census (100 and 1 open; denominators printed in the files).
- to-check.py --project IRPT_BCKEND --all: 0 active of 6042 scanned.
- surprise-row-gate (via safe-commit): two refusals fixed (a C-row fabric field and a duplicate graduated id; a disarm owner naming the CVO).
- comp-rail denials: 4, each re-run in the permitted form.

-- 3.0.0_SA_CVO

## Addendum, 18:3xZ to 18:50Z (msg 6495; in bound as a round the r163/r164 analysis recut, fc10 addendum 1 item 3)

| item | result | commit |
|---|---|---|
| IRPT_BCKEND PRD v0.49 + v0.50 ratified-text half | SIGNED at half d114ddd62ae8..., one condition: the portal reader accepts start_value/end_value before bd_adapter renames | review e4affa19a1, stamped |
| IRPT_BCKEND round 165 | ADJUDICATION_v66 + REMEDIATION_v42: 10 new rows dismissed, 11 v41 rows closed, 2 OPEN, ARMED 1 (D2-W328-S1, owner COO~P2). Slug sent | e9f45b729e |

Correction, not re-written (the row gate refuses an in-place edit): C-S346 and C-S347 carry surfaced_at 19:05Z; the true compile
time is 18:46Z. The same kind of error likely sits on ADJUDICATION_v65 / REMEDIATION_v41 (stamped 17:40Z, committed ~17:33Z).
Lesson: read `date -u` before writing a stamp.

## Addendum, 19:55Z to 20:00Z (msgs 6511, 6513)

| item | result | commit |
|---|---|---|
| IRPT_BCKEND round 166 | ADJUDICATION_v67 + REMEDIATION_v43: D2-W328-S1 disarmed by merged code (no release carried it); 8 dismissed; 3 OPEN, 2 BLOCKING. Slug sent | 3f3388cff5 |

My miss, stated in row D2-W334-S2: v0.50 ordered both schema copies changed, and the v1 docs copy is IMMUTABLE since IB-rt-1's flip.
I signed v0.50 without reading PATH_MANIFEST. Lesson: before signing a contract text that edits a contract artifact, read whether the
artifact is frozen. Also corrected in D2-W331-S2: my v0.49 review named the rule's reach as the claim moves.
New WARN from the one-writer limb: unsuffixed channel files written from dell2 (WARN until C-QUEUE); precedent files are unsuffixed.

## Addendum, 21:05Z to 21:10Z (msg 6555)

| item | result | commit |
|---|---|---|
| IRPT_BCKEND round 167 | ADJUDICATION_v68 + REMEDIATION_v44: frozen v1 schema restored (my diff vs c16bf9d7bb^ empty); packet prints moves beside reach; 7 dismissed, 1 OPEN disarmed; ARMED 0. Slug sent | 1325d97848 |

## Addendum, 21:42Z to 21:45Z (msg 6591)

| item | result | commit |
|---|---|---|
| TCKT_VNEXT round 12 | No row, no judgment; slug by message, no channel change. My live get-item: TCK-20261012-13cd3a1d open, svc-commentary, test title, no draft. In bound only as NFRA_TRNSPT r24's prerequisite (CTO~DELL2 ruling section 7, the cut of r23's analysis) | none |

## PARKED, 21:48Z (msg 6600)

DSGN_IRPTV1 rounds 24-30 compile and slug: OUTSIDE fc10 addendum 1 item 3 (closed 02:54Z, before the relaunch; no bounded analysis
recut them). OWNER: 3.0.0_SA_CVO. UN-PARKS ON: the laptop 1.0.0_SA_CTO widens the bound (asked via 1.0.0_SA_CTO~DELL2, this turn).
Carrier beside it: deliverables/DSGN_IRPTV1_REMEDIATION_ROUND_23_HELD_20261011.md. Undispositioned rows per the COO: D2-W63-S2 to
D2-W67-S1 (W65-S1 BLOCKING), D2-S25, D2-S26.

## UN-PARKED and done, 21:54Z to 22:01Z (msg 6612, fc10 addendum 2: L8-L10 of all six dell2 projects)

| item | result | commit |
|---|---|---|
| DSGN_IRPTV1 rounds 24-30 | ADJUDICATION_v19 + REMEDIATION_v10: 20 dismissed, 8 OPEN (2 BLOCKING), ARMED 0; the round-23 held file removed. My read: IV-e-118 on portal DEV, not PROD. Slug sent | 1c481315bb |

Checked and not a finding: portal origin/DEV at 183860ba (IB-pr-483) was landed by 0.0.0_AB_MSTR~DELL2 on the CTO's approval (receipt in the CTO inbox, 21:15Z).

## Addendum, 22:13Z to 22:25Z (msg 6633)

| item | result | commit |
|---|---|---|
| IRPT_ANLREQ round 16 (Y) | L9: AR161-y-AC2J PASS, AR162-y-AC3J FAIL (clause 1: the account-header rule misses Account-Number and Account/Number and turns back Account Value), AR164-y-AC2J PASS; ADJUDICATION_v17 + REMEDIATION_v9: 7 dismissed, 3 OPEN. Slug sent. YS rows left for YS's close | 54382c3f9d |

## Addendum, 22:27Z (msg 6653)

| item | result | commit |
|---|---|---|
| TCKT_VNEXT round 14 | No row, no judgment; slug by message. My live get-item: TCK-20261012-c546fead open, svc-commentary, analysis_request, test title, no draft key | none |

## Addendum, 22:49Z to 22:55Z (msg 6658)

| item | result | commit |
|---|---|---|
| IRPT_BCKEND round 168 | ADJUDICATION_v69 + REMEDIATION_v45: the adapter release read live (abep4h7R, TypeError 0, 9 smoke REPORTs); 3 dismissed; my row D2-S114 graduates to the CTO (changed path unexercised live, close is an organic wait); ARMED 0. Slug sent. First commit refused by an open merge in the shared tree (the D2 drain); retried after it cleared | 0827bac92d |

## Addendum, 23:23Z to 23:30Z (msg 6661)

| item | result | commit |
|---|---|---|
| DSGN_IRPTV1 round 31 | ADJUDICATION_v20 + REMEDIATION_v11: D2-W69-S1 disarm recorded on its owner's ruling; W65-S1, W62-S2, S22 read met on portal DEV 183860ba; 14 dismissed, 4 OPEN; ARMED 0. Slug sent. A second open-merge refusal, retried after it cleared | 9ac0c902f4 |

## Addendum, 23:33Z to 23:46Z (msg 6673)

| item | result | commit |
|---|---|---|
| IRPT_ANLREQ round 17 (Y) | L9 4 PASS (AR171-y-AC3J with a condition: the reader's release waits on the CTO's D2-W52-S24 ruling; I probed the rule on 31 forms; `No. of Accounts` matches as a count); ADJUDICATION_v18 + REMEDIATION_v10: 6 dismissed, 5 OPEN, 2 ARMED. Slug sent | 5cf791e25f |

## Addendum, 2026-10-13 00:23Z to 00:28Z (msg 6683)

| item | result | commit |
|---|---|---|
| DSGN_IRPTV1 round 32 | ADJUDICATION_v21 + REMEDIATION_v12: both ARMED disarmed on the owner's ruling; 7 dismissed (incl. v11 D2-W69-S2); D2-W72-S2 to the CTO DISARMED; ARMED 0. Slug sent | 011a05ef2c |

## Addendum, 2026-10-13 01:14Z to 01:37Z (msgs 6720, 6728)

| item | result | commit |
|---|---|---|
| IRPT_ANLREQ round 18 (Y) | L9 5 PASS (AR186-y-AC2J with a condition: run the pinned pair before the reader's pair); grades a60300f1fb. Compile HELD while TO-READS-Y9 was pending, landed on its flip: ADJUDICATION_v19 + REMEDIATION_v11, 12 dismissed, 6 OPEN, 5 ARMED; D2-W52-S33 LIVE today. Slug sent | 8cf145cf49 |

My miss: round-17 rows D2-W54-S4, S5, S6 had no disposition at my round-17 compile; dispositioned in round 18. Lesson: run the comp-surprise census AFTER the drain's last commit, not before.

## Addendum, 2026-10-13 01:46Z to 01:52Z (msg 6733)

| item | result | commit |
|---|---|---|
| IRPT_BCKEND round 169 | ADJUDICATION_v70 + REMEDIATION_v46: live read matched on the measured branch (my read: abep4h7R, 2 fresh computes, 0 TypeError, 0 AccessDenied since 01:18Z); D2-S114 closed in its stated form, residual carried by my row D2-S121 (CTO); 15 dismissed; ARMED 0. Slug sent | 5cb27e610e |

## Addendum, 2026-10-13 02:53Z to 03:02Z (msg 6762)

| item | result | commit |
|---|---|---|
| IRPT_BCKEND PRD v0.51 + v0.52 ratified half | SIGNED at 57ebf643...; I read PATH_MANIFEST's IB-rt-7 rule (v1 HoldingsSnapshot admits an optional field) and diffed the schema (one added property). Condition: the old node schema has additionalProperties false and snapshot.py validates at serve, so both packaged copies re-pin before the builder writes | review cab1de19b0, stamped |
| IRPT_BCKEND round 170 | ADJUDICATION_v71 + REMEDIATION_v47: 10 dismissed, 6 OPEN, 4 ARMED (incl. W345-S3, the live 49F temp file with client account numbers). Slug sent | df840ac108 |

## Addendum, 2026-10-13 04:09Z to 04:15Z (msg 6776)

| item | result | commit |
|---|---|---|
| IRPT_BCKEND round 171 | ADJUDICATION_v72 + REMEDIATION_v48: nothing applied (read live); 15 dismissed, 3 OPEN, 2 ARMED. Slug sent | f1711e632a |

My error, corrected in the v0.52 review (CORRECTION section): I rested the ordering condition on serve-time validation in irpt-holdings;
row W348-S4 shows validate_slice has no runtime caller (my search: 4 test callers, 0 runtime). Lesson: read the caller before resting a
condition on a check.

## Addendum, 2026-10-13 04:51Z to 04:56Z (msg 6794)

| item | result | commit |
|---|---|---|
| IRPT_BCKEND round 172 | ADJUDICATION_v73 + REMEDIATION_v49: IB-pr-501 confirms my round-171 correction; 6 dismissed, 2 OPEN, no new ARMED. Slug sent | 26dbe40a10 |

## Addendum, 2026-10-13 05:36Z to 05:42Z (msg 6806)

| item | result | commit |
|---|---|---|
| IRPT_BCKEND round 173 | ADJUDICATION_v74 + REMEDIATION_v50: serve path carries account_id; 6 dismissed, 2 to the CTO (serve-time validation; IVE48 and the frozen v1 enum narrowed @01e843ce2e and restored @506096fc9a, read from history). Slug sent | 2165761665 |

## Addendum, 2026-10-13 06:35Z to 06:43Z (msg 6823)

| item | result | commit |
|---|---|---|
| IRPT_BCKEND PRD v0.53 ratified half | SIGNED at 9e7c58ce...; the builder's validate-before-write read at the call site (run_firm :3133/:3158 before land :3181) | review d08f9f408e, stamped |
| IRPT_BCKEND round 174 | ADJUDICATION_v75 + REMEDIATION_v51: 12 dismissed (incl. v50's D2-W354-S2), 1 OPEN, no new ARMED. Slug sent | 3a0d407fe6 |

## Addendum, 2026-10-13 07:05Z to 07:18Z (msgs 6836, 6837)

| item | result | commit |
|---|---|---|
| IRPT_ANLREQ round 19 (Y, YR) | Release live (my digest read bNPCG2Oe, 0 errors). L9: 13 AC2J PASS on a sampled read (4 records), AR194-y-AC4J FAIL (the r19.1 backstop turns back 'Acct Market Value' with 8-digit integers and 'Acct CUSIP'; probed), AR200-y-AC1 re-grade accepted; 53 dismissed, 6 OPEN, 3 ARMED. Slug sent | c219042317 |
| IRPT_BCKEND round 175 | ADJUDICATION_v76 + REMEDIATION_v52: five portal rows closed on the DEV landing (I read DEV's log for every candidate); the per-firm package census graduates ARMED. Slug sent | 4da44f29d1 |

## Addendum, 2026-10-13 07:50Z to 07:55Z (msg 6857)

| item | result | commit |
|---|---|---|
| IRPT_BCKEND round 176 | ADJUDICATION_v77 + REMEDIATION_v53: the live per-firm packages are not HEAD, 4 live members equal no historical blob (provenance to the CTO); the minimal-pair ruling agreed; 5 dismissed (incl. v52 W359-S1), 2 ARMED. Slug sent | c5de16f70d |

## Addendum, 2026-10-13 08:31Z to 08:37Z (msg 6865)

| item | result | commit |
|---|---|---|
| IRPT_BCKEND round 177 | ADJUDICATION_v78 + REMEDIATION_v54: minimal packages built, nothing applied; the 4 unattributed members are CRLF copies (v53 W361-S3 closed); W363-S2 to the CTO; 7 dismissed. Slug sent | 936ddf2b3c |

## Addendum, 2026-10-13 13:04Z to 13:08Z (msg 6927)

| item | result | commit |
|---|---|---|
| IRPT_DASHBD round 87 | No row, no judgment; slug by message, no channel change. My live read: irpt-49f-reporting-gold-lambda J6M/92Mh (12:39:43Z, 3008 MB, Successful), since then Traceback 0, ERROR 0, REPORT 1 | none |

Quiet stretch 08:37Z to 13:04Z: watcher re-armed at each expiry; delivery ledger read twice (no message missed).

## Addendum, 2026-10-13 13:28Z to 13:30Z (msg 6944)

| item | result | commit |
|---|---|---|
| TCKT_VNEXT round 16 | No row, no judgment; slug by message. My ConsistentRead: TCK-20261009-a1052909 and TCK-20261012-13cd3a1d completed, TCK-20261012-c546fead open | none |

## Addendum, 2026-10-13 13:43Z to 13:46Z (msg 6953)

| item | result | commit |
|---|---|---|
| IRPT_DASHBD round 88 | ADJUDICATION_v52: D2-W132-S1 (checker defect, amended) dismissed; nothing graduates. Slug sent | 50d8780e32 |

## Addendum, 2026-10-13 14:17Z to 14:35Z (msgs 6963, 6974)

| item | result | commit |
|---|---|---|
| IRPT_DASHBD round 89 | ADJUDICATION_v53 + REMEDIATION_v36: FWD-8 NOT REALIZED at segment grain; D2-W133-S1 (the 7 unexplained) to the CTO; 5 dismissed. Slug sent | 46e9beb3fd |
| IRPT_ANLREQ round 20 (Y, YR) | My live reads: eight packagers at the signed values, 0 errors since 12:30Z; the holdings artifact key's three wrong versions, restore and release, no function ran a wrong one. L9: AR211-y-AC3J FAIL (probed: Acct Cost Basis/Gain), five AC2J PASS on a sample, AR212/213-y-AC1 re-grades accepted; 19 dismissed, 6 OPEN, 2 ARMED. Slug sent | af5f05fd94 |

## Addendum, 2026-10-13 14:41Z to 14:49Z (msg 6990)

| item | result | commit |
|---|---|---|
| IRPT_BCKEND round 178 | ADJUDICATION_v79: the minimal holdings packages live (my head-object reads: 49F UHOCIkWj, INF PzhCs97q, cottonwood untouched); 2 dismissed (the issuer's rm -r of 39 tracked records, restored, read clean); W345-S3 stays ARMED. Slug sent | c76b1a3cd3 |

## Addendum, 2026-10-13 15:11Z to 15:16Z (msg 7014)

| item | result | commit |
|---|---|---|
| IRPT_BCKEND round 179 | ADJUDICATION_v80: W345-S3 closed (0/0 after a named S3-path build; caveats kept); 3 dismissed; nothing graduates. Noted: v0.53 half already SIGNED current. Slug sent | 7eff6094d3 |

## Addendum, 2026-10-13 15:29Z to 15:35Z (msg 7027)

| item | result | commit |
|---|---|---|
| IRPT_DASHBD round 90 | ADJUDICATION_v54 + REMEDIATION_v37: FWD-8 NOT REALIZED for 7 accounts at day grain; D2-W136-S1 to the CTO; 4 dismissed (incl. v36 D2-W133-S1). The vendor pull checked against CTO msg 6986 (no per-use word for a non-Bloomberg vendor). Slug sent | 322f6b77f8 |

## Addendum, 2026-10-13 15:42Z to 15:48Z (msg 7033)

| item | result | commit |
|---|---|---|
| IRPT_BCKEND round 180 | ADJUDICATION_v81 + REMEDIATION_v55: account_id live end to end (7639 of 7640); 2 dismissed; D2-W364-S1 (the directory read via the opal-data-bd alias; my head-object read it present) graduates. Slug sent | 277aaf946e |

## Addendum, 2026-10-13 15:42Z to 16:22Z (msgs 7033, 7055, 7057)

| item | result | commit |
|---|---|---|
| IRPT_ANLREQ round 21 (Y, YR) | Probed r19.3: 10 of 10 one-account neighbours unflagged, 8 of 8 two-account forms turned back (incl. Account Numbers, Subaccounts, Account Nos). L9: AR221 PASS, AR-y-222 judgment FAIL superseded by AR-y-229 PASS, four AC2J PASS, two re-grades accepted; 22 dismissed (incl. my D2-S73), nothing graduates. Slug sent | 99fe06bb74 |
| IRPT_DASHBD round 91 | ADJUDICATION_v55 + REMEDIATION_v38: FWD-8 NOT REALIZED for 7 after the ledger-row read; D2-W137-S1 to the CTO; v37 D2-W136-S1 closed. Slug sent | 5e23f18556 |

## Addendum, 2026-10-13 16:24Z to 16:38Z (msgs 7064, 7066, 7067)

| item | result | commit |
|---|---|---|
| IRPT_BCKEND round 181 (~P) | ADJUDICATION_v82 + REMEDIATION_v56: nothing applied (irpt-directory-search read tvrsQ+w8). D2-S139 graduates ARMED to the laptop 1.0.0_SA_CTO, HELD by Andrew's word (msg 7066). Portal read: the selectionRequest.ts:18 throw is the same on DEV f6ef1d25 and PROD 15c97549, reached only by an ACCOUNT row whose accountId is null (search.ts:277). 2 dismissed. Slug sent | 7f0f905a42 |
| ADVI_COTBKF round 80 (COO~C2, in bound by Andrew card 6) | L9: CB80cb1-AC2 PASS (note: the top-level served count of 48 is APH only; CTVA has 115 served days), CB80cb2-AC2 PASS (test byte-equal to round 76's). ADJUDICATION_v57 + REMEDIATION_v49: 8 dismissed; D2-W155-S1 graduates ARMED to 1.0.0_SA_CTO~DELL2 because the issuer's disarm D2-S134 rests on minted-table readers that were not re-measured; D2-W155-S4 to COO~C2. Slug sent (16:38:28Z) | 7aceb5d4a1 |

## Addendum, 2026-10-13 16:44Z to 16:47Z (msg 7079)

| item | result | commit |
|---|---|---|
| IRPT_DASHBD round 92 | ADJUDICATION_v56 + REMEDIATION_v39: FWD-8 NOT REALIZED for 3 accounts (10 UNEXPLAINED days), met for 83. Spot-check: per-account sums 23 = 13 + 10, test_held_days 13, rule d8a3f1fa58 committed before the record. v38 D2-W137-S1 closed; D2-W138-S1 to CTO~DELL2 for the endpoint card. Slug sent 16:47:07Z | 063bf7a3df |

Correction: the round-92 rows carry surfaced_at 16:48:00Z; the clock read 16:45:56Z before the write, so the stamp is about 2 minutes early of the true time. The rows are immutable, so the correction is recorded here.

## Addendum, 2026-10-13 17:54Z to 18:30Z (msgs 7120, 7146)

| item | result | commit |
|---|---|---|
| Law edit relay, CLAUDE.md rule 33 (msg 7120) | Acked; paths posted from now on carry a file:/// URI, plus the repo-relative form when bound for another box | -- |
| IRPT_BCKEND round 182 (~P) | ADJUDICATION_v83 (C-S366), no remediation file: irpt-directory-search live at the signed digest (my read, 18:23Z); Andrew's lifting of the hold read in open calls cfd4/b6fa (ruled_by andrew); 5 dismissed incl. v56 D2-S139; D2-S145 to -S147 stay with the issuer. Not shown: a client login on PROD. Slug sent 18:30:28Z | 8a628274ca |

## Addendum, 2026-10-13 18:59Z to 19:05Z (msgs 7165, 7167)

| item | result | commit |
|---|---|---|
| IRPT_ANLREQ PRD v0.5 ratified-text half (half cfcfd5d90db3) | REFUSED: C-PACKAGER still names the branded PDF as the last hop; the organic arm names an Opal staff filing; the produced variant is not bound to the chosen one; a (v0.5) annotation sits inside ENDPOINT. Review read against the pivot direction (lines 55, 108-165, 345-356). Note sent to CTO~DELL2 19:05:03Z | review 3e8061163e, stamp 9c5bb72877 |

## Addendum, 2026-10-13 19:05Z to 19:16Z (msgs 7171, 7173, 7175)

| item | result | commit |
|---|---|---|
| IRPT_DASHBD PRD v0.14 ratified-text half (FWD-21) | REFUSED (f2f477f21f81): "read by Andrew" was an unqualified wait; a (v0.14) annotation inside ENDPOINT. Content matched the baseline and Andrew's ~19:0xZ word | review 7209af0016, stamp c32ddf00cb |
| IRPT_ANLREQ v0.5 re-cut @68115f2d84 | All four fixes present; SIGNED at half 7e377f75669b; PRD ADMITTED (brief half signed by the CRO) | review d100ad9bc4, stamp 9f59d6bcf5 |
| IRPT_DASHBD v0.14 re-cut @6d694ed9a5 | Both fixes present (seat section check is the gate; Andrew's read is the qualified organic arm); SIGNED at half 1bd09826f4b3; PRD ADMITTED | review 8399376889, stamp 0524321f87 |

## Addendum, 2026-10-13 19:22Z to 19:32Z (msg 7193)

| item | result | commit |
|---|---|---|
| ADVI_COTBKF round 81 | L9: CB81cc1-AC2 PASS, CB81cc2-AC2 PASS (note: the minted copy is the local copy, not compared with the served object), CB81cc3-AC2 PASS. The minted table has two code readers: D2-S134's disarm is void, confirming my round-80 refusal to accept it. ADJUDICATION_v58 (C-S65) dismisses 7; REMEDIATION_v50: D2-W158-S2 ARMED to CTO~DELL2, D2-W159-S1 ARMED to COO~C2. Slug sent 19:31:55Z | 43b340c673 |

## Addendum, 2026-10-13 20:49Z to 20:57Z (msg 7230; account changed to a fresh login before this item)

| item | result | commit |
|---|---|---|
| IRPT_BCKEND round 183 (~P) | ADJUDICATION_v84 (C-S367), no remediation file: build only (Opal Ultra Short-Term in the comparison catalogue, IB-pr-517); I re-ran the two catalogue test files (16 passed) and read recipe.py:811-816 (fail-closed on any non-YCHARTS namespace). 10 dismissed; D2-S145 to -S147 and D2-S150 stay with the issuer. Slug sent | 220e1b5785 |

Correction: C-S367 carries surfaced_at 20:56:00Z; the clock read 20:54:57Z before the write, so the stamp is about 1 minute ahead of the true time. The row is immutable, so the correction is recorded here.

## Addendum, 2026-10-13 22:16Z to 22:24Z (msg 7303)

| item | result | commit |
|---|---|---|
| IRPT_BCKEND round 184 (~P) | ADJUDICATION_v85 (C-S368), no remediation file: build only (IB-pr-518, irpt-ycharts-generate rebuilt with the catalogue release); live CodeSha256 hpNfkhLt unchanged (my read). 5 dismissed; D2-S145 to -S147, S150, S152, S153 stay with the issuer. For the unsigned pair: name the form's model checkbox reorder for every firm, and that recipe.py does not ship. Slug sent | 0cda29474c |

## Addendum, 2026-10-13 22:37Z to 22:55Z (msgs 7325, 7326)

| item | result | commit |
|---|---|---|
| ADVI_COTBKF round 82 | L9: CB82cd1-AC3 FAIL on one clause (273 of 300 reverse-match 'none' rows carry no reason; my count from REVERSE_MATCH.csv), CB82cd2-AC2 PASS (route_not_live; served objects equal the scratch copy), CB82cd3-AC3 PASS. ADJUDICATION_v59 (C-S66) dismisses 9 incl. W163-S1 folded into v50's ARMED rows; no remediation row while round 83 runs. Raw account numbers in the two committed CSVs are on origin/CLOUD (read), covered by Andrew's 2026-10-09 word and the CTO's KEEP. Slug sent | e819f0fc64 |
| IRPT_DASHBD round 95 | ADJUDICATION_v57 (C-S68): contract 0.2.0 read (117 members, 8 sections, lineage kept); 1 dismissed; W145-S1 open for a CTO ruling, to graduate at round 94. Round 93 was a direct act (no CVO packet). Slug sent | 055198dca0 |

Correction: ADJUDICATION_v57 (IRPT_DASHBD) carries surfaced_at 22:53:00Z; the clock read 22:52:43Z before the write, so the stamp is 17 seconds ahead. The row is immutable; recorded here.

## Addendum, 2026-10-13 23:19Z to 23:25Z (msg 7347)

| item | result | commit |
|---|---|---|
| IRPT_DASHBD round 94 | ADJUDICATION_v58 (C-S69) + REMEDIATION_v40: five cells; the household sample record read (3 accounts by hashed ref, 44 of 117 filled, identity 30 of 30, private); 26 dismissed incl. round 93 leftovers; 3 to COO~D2 (FDRXX to CASH BLOCKING, fee-basis method row, the account_class_daily contract statement). FWD-21 not graded. Slug sent | 5a6045882e |

## Addendum, 2026-10-13 23:36Z to 23:43Z (msg 7354)

| item | result | commit |
|---|---|---|
| IRPT_BCKEND round 185 (~P) | ADJUDICATION_v86 (C-S369), no remediation file (IB-pr-497 parked): irpt-ycharts-generate live at xP47NQDn (my read, 22:48:27Z); the person-read is owed (ledger open; 0 invocations since the apply). Export-receipt release built, pair unsigned. 6 dismissed; W368-S2 (latent served.py pin, ARMED) folded into W349-S1. Slug sent | 5e48d684a8 |

Correction: C-S369 carries surfaced_at 23:42:00Z; the clock read 23:40:30Z before the write, so the stamp is 90 seconds ahead. The row is immutable; recorded here.

## Addendum, 2026-10-13 23:46Z to 23:54Z (msg 7358)

| item | result | commit |
|---|---|---|
| ADVI_COTBKF rounds 83 and 84 | L9: CB83ce1-AC3 FAIL on one clause (derivation not checked; round-82 salt lost), CB83ce2-AC3 PASS (10 month_grades columns by code reading only), CB83ce3-AC3 PASS (price-conditional key accepted), CB84cf1-AC3 PASS (NEW_CLIENT on active-set windows, disclosed). ADJUDICATION_v60 (C-S67) dismisses 13; W164-S1..S3 ARMED held to round 85 (TO-CB-cg-1 active). Slug sent. From this item on, row stamps are taken from the clock at write time | 6b9f2b985d |

## Addendum, 2026-10-14 00:20Z to 00:27Z (msg 7365)

| item | result | commit |
|---|---|---|
| ADVI_COTBKF round 85 (last before the park) | L9: CB85cg1-AC3 PASS; I recounted the two committed files (860 rows, 460/13/387, all keys raw; 41,826 windows from 2013-04-08). ADJUDICATION_v61 (C-S68) dismisses 9 incl. W164-S1..S3 (disarmed by D2-S136). REMEDIATION_v51: W168-S2 ARMED to COO~C2: trust round 85's side of the 6 window DIFFs; its build scripts sit in gitignored scratch, so commit and reproduce them byte for byte before the park. Slug sent | 239f84375d |

Correction: the round-85 grade file header says ~00:3xZ; it was written at about 00:25Z.

## Addendum, 2026-10-14 00:42Z to 00:46Z (msg 7384)

| item | result | commit |
|---|---|---|
| IRPT_DASHBD round 97 | ADJUDICATION_v59 (C-S70): contract 0.3.0 states the filled-report shape; I re-ran DB94-1-AC1, DB94-6-AC1, DB97-1-AC1 from their task orders: all PASS. 3 dismissed (W148-S1 ARMED: hazard gone on my re-run). Round 96 rows (W146, W147) wait for its packet. Slug sent | d506a4a6f6 |

## Addendum, 2026-10-14 00:47Z to 00:53Z (msg 7387)

| item | result | commit |
|---|---|---|
| IRPT_BCKEND round 186 (~P) | ADJUDICATION_v87 (C-S370), no remediation file (IB-pr-497 parked): irpt-export-render live at 5/9LZBbT (my read, 00:09:26Z); two person-reads owed (export, catalogue). 9 dismissed; S152 and S155 (backfill design A/B; no COT/INF activity producer) stay with the issuer for the CTO. Slug sent | 7246aa34b3 |

Correction: C-S370's grounding cites msg 7389; the packet message is 7387. The row is immutable; recorded here.

## Addendum, 2026-10-14 00:59Z to 01:05Z (msg 7395)

| item | result | commit |
|---|---|---|
| IRPT_DASHBD round 96 | ADJUDICATION_v60 (C-S71): the real sample rendered privately; I re-ran DB96-1-AC1: PASS. 5 dismissed (W146-S1 ARMED: hazard gone on my re-run). HELD: W147-S3 ARMED (synthetic CASH_USD serves fixed_income while Cash-typed rows will serve cash), to clear before round 98's FDRXX apply DB-b-183; flagged in the slug. W146-S4, -S5 stay open. No remediation row while round 98 runs. Slug sent | 1e9bb59614 |

## Addendum, 2026-10-14 01:34Z to 01:38Z (msg 7416)

| item | result | commit |
|---|---|---|
| IRPT_BCKEND round 187 (~P) | ADJUDICATION_v88 (C-S371), no remediation file: Design-B backfill code built offline; I re-ran IB187-1-AC1 to AC3: all PASS. COT can produce 19/19 activity columns, INF 17/19. 6 dismissed; S152, S155, S156 and the queued rows stay with the issuer. Slug sent | 79b7944ef7 |

## Addendum, 2026-10-14 02:07Z to 02:12Z (msg 7426)

| item | result | commit |
|---|---|---|
| IRPT_DASHBD rounds 99 and 100 | ADJUDICATION_v61 (C-S72): the CASH_USD change counted (0 of 4,315 positions, 0 of 1,314,777 lots) and reverted on the CTO's ruling; my W147-S3 closed on its owner's disarm S25; I re-ran DB100-1-AC1: PASS. 8 dismissed; round 98's rows (S24, W149-S1..S3) wait (DB-b-183 pending). Slug sent | 16319ab2e9 |

## Addendum, 2026-10-14 02:25Z to 02:30Z (msg 7448)

| item | result | commit |
|---|---|---|
| IRPT_BCKEND round 188 (~P) | ADJUDICATION_v89 (C-S372), no remediation file: Design B packaged, not released (live reporting-gold read unchanged). 10 dismissed. S158 ARMED held with the CTO: Cottonwood IR holdings stale; my trading-day count puts it 2 trading days behind its peers (the packet's four is the library's UTC-date frontier). Slug sent | ea8a848d93 |

## Addendum, 2026-10-14 03:40Z to 03:44Z (msg 7496)

| item | result | commit |
|---|---|---|
| IRPT_BCKEND round 189 (~P) | ADJUDICATION_v90 (C-S373), no remediation file: the IR cash rule built canonical-only; I re-ran IB189-1-AC1 to AC3: all PASS. Blast radius 844 nodes; fallback-served cash stays Fixed Income (cross-page call for the CTO). 7 dismissed; S158 (CTO) and W374-S1 (box manager: client-data check absent on dell2; my commits show the same WARN) held with their owners. Slug sent | 488fe2c4d2 |

## Addendum, 2026-10-14 04:22Z to 04:28Z (msg 7518)

| item | result | commit |
|---|---|---|
| IRPT_DASHBD rounds 101 and 102 | L9: DB101-5-J1 PASS; I read 8 of 14 private page images (1, 2, 4, 5, 7, 8, 11, 14) against SECTION_CHECK.json and the baseline; note: every page header prints the placeholder Sample Firm, omitted from the ranked defects. ADJUDICATION_v62 (C-S73) dismisses 39; W152-S3, W155-S9, W155-S10 (ARMED) held with owners; round 98 rows wait. Slug sent | 55d585884e |

## Addendum, 2026-10-14 04:36Z to 04:40Z (msg 7527)

| item | result | commit |
|---|---|---|
| IRPT_BCKEND round 190 (~P) | ADJUDICATION_v91 (C-S374), no remediation file: fallback cash rule and publish-gate fix built, producer censused; I read the live schedule (ENABLED, as censused). 9 dismissed (W378-S1 disarmed by S163; W376-S1 folded into W374-S1). S158 and W374-S1 held. For round 191: open the NEVER-2 ledger (mint-bundle opens none) and read 49F's failed 10-09 fire. Slug sent | c23a4ad50e |
