# Deploy Completion Record
**Date opened:** 2026-10-11T09:55:46.979659+00:00
**Status:** SUPERSEDED -- nothing stranded, nothing written under this entry (L1 reads only) -- closed 20261012T062505Z by 0.7.0_AE_CloudOps~FB1; replaced by advi-firmbkts-fb-f-9-act2-mode-move-dell1-20261012
**Deploy:** ADVI_FIRMBKTS TO-FB-f-9 phase B (window act 2): ship the 19 dormant gold .py objects and the dispatcher switch to s3://opal-data-bd/code/gold/, moving BD_PLATINUM_MODE to canonical for the scheduled production chain; pair COO half @12b22ef020 + ADDENDUM 1 @1d7f94ebb1, CTO half @03c1c6f001 + ADDENDA 1 @6ac66a8950 and 2 @3d24ccdbd2
**Authored by:** 0.7.0_AE_CloudOps~FB1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 12.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

> ### SUPERSEDED. READ THE LEG TABLE: "closed" THERE MEANS *DISPOSED OF*, NOT *DONE*.
>
> This entry was opened 2026-10-11T09:55Z for the first, held attempt of TO-FB-f-9 phase B (no object written under it; row D1-S18
> found the producers' role grant missing, since applied by FB-g-8 and FB-f-16). The act ran on the issuer's GO (AMENDMENT 13
> @f5da2fc917) under `advi-firmbkts-fb-f-9-act2-mode-move-dell1-20261012`, which carries the shipment, the switch, `MOVE_TS` and the
> rollback record.

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | step 2 reads: opal-data-bd versioning, the 20 keys' prior VersionIds, the actor's grants at object grain, the producers' role grant at the new home, the schedule, deployed-equal before-read | the entry carries the 20 rows and the read lines | performed 2026-10-11 ~09:5xZ and recorded in this entry's STEP 2 READS section: opal-data-bd versioning Enabled; the 20 keys' prior VersionIds (18 present, 2 new keys); actor identity PutObject allowed on code/gold; the producers' role had NO Allow at the new home (row ADVI_FIRMBKTS-D1-S18, since applied by FB-g-8 and FB-f-16); schedule read. The reads are superseded by the 2026-10-12 entry's fresh reads | CLOSED 20261012T062505Z |
| L2 | s3-prefix | s3://opal-data-bd/code/gold/ 19 .py objects: 14 writers (C_05 C_06 C_07 C_08 D_00 D_00b D_00c D_00f D_01 D_02 D_03 D_04 E_01 E_24) + lib/{platinum_dest,platinum_dest_view,gold_utils,helpers,etf_classifier}.py (step 3, HELD for the build-final amendment) | 19 of 19 read back equal to git show HEAD:<path> (sha256 per key) | NOT PERFORMED under this entry -- superseded by the entry advi-firmbkts-fb-f-9-act2-mode-move-dell1-20261012 (opened 2026-10-12T06:15Z on the issuer's GO, AMENDMENT 13 @f5da2fc917); this entry's reads of 2026-10-11 pre-dated the grant (row D1-S18, applied by FB-g-8) and the window; nothing was written under it | CLOSED 20261012T062428Z |
| L3 | s3-prefix | s3://opal-data-bd/code/gold/gold_dispatch.sh -- the switch (step 4, HELD for the GO amendment), aws s3 cp --sse AES256 then cmp | cmp read-back equal, 0 bytes above 127, MOVE_TS recorded | NOT PERFORMED under this entry -- superseded by the entry advi-firmbkts-fb-f-9-act2-mode-move-dell1-20261012 (opened 2026-10-12T06:15Z on the issuer's GO, AMENDMENT 13 @f5da2fc917); this entry's reads of 2026-10-11 pre-dated the grant (row D1-S18, applied by FB-g-8) and the window; nothing was written under it | CLOSED 20261012T062428Z |
| L4 | activation | the first SCHEDULED production chain after MOVE_TS (--chain, not --single, not QA) | the chain's exit and a run log with no ValueError and no NoSuchKey on a served read | NOT PERFORMED under this entry -- superseded by the entry advi-firmbkts-fb-f-9-act2-mode-move-dell1-20261012 (opened 2026-10-12T06:15Z on the issuer's GO, AMENDMENT 13 @f5da2fc917); this entry's reads of 2026-10-11 pre-dated the grant (row D1-S18, applied by FB-g-8) and the window; nothing was written under it | CLOSED 20261012T062428Z |
| L5 | verify | AC1 deployed-equal 20 of 20, AC2 new-home 11 of 11 since MOVE_TS, AC3 old-home 0 keys of 11 classes since MOVE_TS | the three outputs of r3_act2_reads.py quoted | NOT PERFORMED under this entry -- superseded by the entry advi-firmbkts-fb-f-9-act2-mode-move-dell1-20261012 (opened 2026-10-12T06:15Z on the issuer's GO, AMENDMENT 13 @f5da2fc917); this entry's reads of 2026-10-11 pre-dated the grant (row D1-S18, applied by FB-g-8) and the window; nothing was written under it | CLOSED 20261012T062428Z |
| L6 | git | proof instance written and TO-FB-f-9 status flipped complete in one commit | commit hash | NOT PERFORMED under this entry -- superseded by the entry advi-firmbkts-fb-f-9-act2-mode-move-dell1-20261012 (opened 2026-10-12T06:15Z on the issuer's GO, AMENDMENT 13 @f5da2fc917); this entry's reads of 2026-10-11 pre-dated the grant (row D1-S18, applied by FB-g-8) and the window; nothing was written under it | CLOSED 20261012T062429Z |

## Log

- 20261011T095546Z OPENED by 0.7.0_AE_CloudOps~FB1 with 6 leg(s)
- 20261011T095603Z HELD-PRE-APPLY gate=external/TO-FB-f-9 amendment commit by 2.0.0_SA_COO~B1 declaring the build final (step 3)
- 20261011T095840Z HELD-PRE-APPLY gate=external/TO-FB-f-9 build-final amendment commit by 2.0.0_SA_COO~B1 (step 3), the GO amend
- 20261012T062428Z LEG L2 closed: NOT PERFORMED under this entry -- superseded by the entry advi-firmbkts-fb-f-9-act2-mode-move-dell1-20261012 (opened 202
- 20261012T062428Z LEG L3 closed: NOT PERFORMED under this entry -- superseded by the entry advi-firmbkts-fb-f-9-act2-mode-move-dell1-20261012 (opened 202
- 20261012T062428Z LEG L4 closed: NOT PERFORMED under this entry -- superseded by the entry advi-firmbkts-fb-f-9-act2-mode-move-dell1-20261012 (opened 202
- 20261012T062428Z LEG L5 closed: NOT PERFORMED under this entry -- superseded by the entry advi-firmbkts-fb-f-9-act2-mode-move-dell1-20261012 (opened 202
- 20261012T062429Z LEG L6 closed: NOT PERFORMED under this entry -- superseded by the entry advi-firmbkts-fb-f-9-act2-mode-move-dell1-20261012 (opened 202
- 20261012T062505Z LEG L1 closed: performed 2026-10-11 ~09:5xZ and recorded in this entry's STEP 2 READS section: opal-data-bd versioning Enabled; the 20 
- 20261012T062505Z CLOSED AS SUPERSEDED -- L1 reads performed; L2 to L6 carry NOT PERFORMED proofs; the work ran under advi-firmbkts-fb-f-9-act2-mode-move-dell1-20261012

## STEP 2 READS (0.7.0_AE_CloudOps~FB1, 2026-10-11T09:58:07Z)

**Required text (the CTO's condition): a hand run of E_24 exports BD_PLATINUM_MODE=canonical or it writes the legacy home.**

- Bucket `opal-data-bd` versioning: Enabled. `deployed-equal` before-read 09:52:24Z: 0 of 20 equal the repository at HEAD.
- 20 keys, prior versions (18 present, 2 new keys with no prior version, which need none: nothing is deleted by this act):

| key | prior VersionId | prior LastModified |
|---|---|---|
| `code/gold/C_05.client_tax_liability.py` | YqgnppEg80iK97hxtMHshNtVFwuDUnLQ | 2026-07-09T19:58:04+00:00 |
| `code/gold/C_06.client_mix_timeseries.py` | AREnJgLoyQnZ1zKwPan793py8CCkNHHA | 2026-10-11T06:20:04+00:00 |
| `code/gold/C_07.advisor_attribution.py` | tZ7Wwj5x61yIIdNDSUGqwF7TjcXS07Ni | 2026-07-06T18:00:10+00:00 |
| `code/gold/C_08.advisor_fee_efficiency.py` | qEevkpFT4KffZikRF8sBpYeCfa.JKC3C | 2026-09-27T05:47:50+00:00 |
| `code/gold/D_00.portal_aggregates.py` | anWrmMfHewKok9jJ1hN3AABWEX7R4Pqf | 2026-07-24T17:07:21+00:00 |
| `code/gold/D_00b.portal_timeseries.py` | ZNmwLpljcBHv63pQJaFHH3nOGDoC.rbZ | 2026-06-08T17:28:07+00:00 |
| `code/gold/D_00c.portal_leaderboard.py` | MoFlEhFGZMURzc0wk_B6Ru45kOl9atmU | 2026-07-09T18:57:50+00:00 |
| `code/gold/D_00f.advisor_nna_canonical.py` | h8_.GRABDePrlcnmkR7w.p.eRsNu4KKK | 2026-06-18T13:02:09+00:00 |
| `code/gold/D_01.partner_analytics.py` | Wa9oOvBT6N.J188iZYgiHNJnb085liR1 | 2026-06-08T18:20:58+00:00 |
| `code/gold/D_02.advisor_client_detail.py` | rPfpepK2VL2b9m1.VZeZJkjm._InlXN9 | 2026-08-18T20:27:41+00:00 |
| `code/gold/D_03.composition_artifacts.py` | YNpZz346bYe1tWxkn3vfulYyNQXTHOpH | 2026-10-11T06:20:07+00:00 |
| `code/gold/D_04.client_portal_summary.py` | N_isqMcDp.qdYQIJuzHV3bNQv9W6kor. | 2026-10-11T06:20:01+00:00 |
| `code/gold/E_01.account_quality_tiers.py` | oYi4tzz.5Z1JQcLeT4yceEodNKXSSLW8 | 2026-09-27T05:48:01+00:00 |
| `code/gold/E_24.rebuild_fee_scorecard.py` | eTubWXzpw4AUjRGYxFQRWApnW11kcVVz | 2026-09-27T05:49:34+00:00 |
| `code/gold/lib/etf_classifier.py` | hnOzzH4QClDqa_qbd6Y5tqKu3Kag4vtM | 2026-10-09T09:54:21+00:00 |
| `code/gold/lib/gold_utils.py` | 8ER4z09VIIXHvOxDlCDiJ12U7T._EIUE | 2026-05-12T20:58:26+00:00 |
| `code/gold/lib/helpers.py` | Ccc.2tQQ3h5EEIgtp0Q.uYuM.fehKZc0 | 2026-05-11T20:43:01+00:00 |
| `code/gold/lib/platinum_dest.py` | ABSENT (new key) | - |
| `code/gold/lib/platinum_dest_view.py` | ABSENT (new key) | - |
| `code/gold/gold_dispatch.sh` | VikjYXAEPXBxYRenSPh6YfD_PuuHLvTM | 2026-10-01T08:41:28+00:00 |

- Actor identity `user/cloudops-dell1-agent-user` simulated on its own ARN, one resource per call: PutObject allowed on the dispatcher
  and on the lib and writer keys sampled; DeleteObject explicitDeny (control).
- Producers' role: runner -> `bd-exporter-profile` -> `bd-exporter-ec2-role`. The order's `simulate-principal-policy` on that role
  is AccessDenied for this identity (instrument gap, stated). A policy-document read of all 18 policies finds NO Allow for
  PutObject or GetObject on `opal-data-49financial/advi/49financial/platinum/*` and a ListBucket Allow whose prefix condition is
  `gold/advi/*` or `_code/*`; the bucket policy carries no Allow. Row `ADVI_FIRMBKTS-D1-S18` BLOCKING. Evidence:
  `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FB1/act2/step2_reads.txt`.
- Schedule: `bd-gold-nightly-fallback` ENABLED `cron(0 23 ? * MON-SAT *)` to `bd-gold-trigger`; the monthly rule DISABLED. The last
  legacy chain's end is read at the GO.
- Steps 3 and 4 are HELD by the issuer (msgs 3721 and 3716). No object has been written by this lane.
