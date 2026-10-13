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
