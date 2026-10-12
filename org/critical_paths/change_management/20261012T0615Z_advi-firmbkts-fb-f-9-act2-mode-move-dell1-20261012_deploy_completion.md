# Deploy Completion Record
**Date opened:** 2026-10-12T06:15:17.547213+00:00
**Status:** OPEN
**Deploy:** ADVI_FIRMBKTS TO-FB-f-9 phase B (window act 2, the GO @f5da2fc917 AMENDMENT 13): ship the 19 dormant gold .py objects, then gold_dispatch.sh (the switch), to s3://opal-data-bd/code/gold/; MOVE_TS recorded; pair COO half @12b22ef020 + ADDENDA 1 to 3 (ADDENDUM 2 @3c47103dc7, ADDENDUM 3), CTO half @03c1c6f001 + ADDENDA 1 to 4; rollback = the export and the guard removed by re-uploading the recorded prior gold_dispatch.sh version; ROLLS BACK THE SAME HOUR if act 4 cannot land before the next scheduled chain (Mon 23:00Z fallback); a hand run of E_24 exports BD_PLATINUM_MODE=canonical or it writes the legacy home (E_24 now refuses an unset mode, FB-g-7)
**Authored by:** 0.7.0_AE_CloudOps~FB1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 48.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | step 0 and 2 reads, fresh: pair bytes and SIGNED, opal-data-bd versioning, the 20 keys' prior VersionIds, ownership-map baseline (legacy VersionId FcsnGhU7Rt280E9rmDacateI5WiK8S28), the schedule and no run in flight, the role grant, the dispatcher diff | the entry carries the 20 rows and the read lines | pair COO 12b22ef020 + ADDENDA 1-3 and CTO 03c1c6f001 + ADDENDA 1-4 SIGNED, 0 uncommitted; versioning Enabled; deployed-equal 0 of 20 (the push hook has not shipped the 19 objects); 18 prior VersionIds recorded, 2 new keys; ownership-map legacy VersionId FcsnGhU7Rt280E9rmDacateI5WiK8S28 05:22:13Z 474841 bytes equals the GO baseline, canonical 2026-10-11T04:01:18Z; gold runner stopped, 0 SSM invocations in flight; nightly fallback Mon-Sat 23:00Z; role grant matches Put/Get/Delete/List, 0 Deny; dispatcher live blob 631d6e6f4a to HEAD 370c95552e is 40 insertions 20 deletions, 0 bytes above 127; read 2026-10-12T06:14:23Z | CLOSED 20261012T061603Z |
| L2 | s3-prefix | s3://opal-data-bd/code/gold/ 19 .py objects (14 writers + 5 lib) shipped through .tools/safe-deploy.sh and read back (step 3) | 19 of 19 equal git show HEAD:<path>, sha256 per key |  | OPEN |
| L3 | s3-prefix | s3://opal-data-bd/code/gold/gold_dispatch.sh -- the switch (step 4), aws s3 cp --sse AES256 then cmp, MOVE_TS read after the copy returned | cmp equal, 0 bytes above 127, MOVE_TS printed, ownership-map baseline re-printed |  | OPEN |
| L4 | verify | AC1 deployed-equal 20 of 20 and the legacy-quiet read old-home --since MOVE_TS (it must name exec_summary.json among the classes it covers) | the two outputs quoted |  | OPEN |
| L5 | activation | the first SCHEDULED production chain AFTER act 4 (step 5): exit, run log with no ValueError and no NoSuchKey on a served read (a read after the issuer's act 4, not before) | the chain evidence |  | OPEN |
| L6 | verify | AC2 new-home 11 of 11 since MOVE_TS and AC3 old-home 0 keys of 11 classes since MOVE_TS, read after that chain | the outputs of r3_act2_reads.py quoted |  | OPEN |
| L7 | git | proof instance written and TO-FB-f-9 status flipped complete in one commit | commit hash |  | OPEN |

## Log

- 20261012T061517Z OPENED by 0.7.0_AE_CloudOps~FB1 with 7 leg(s)
- 20261012T061603Z LEG L1 closed: pair COO 12b22ef020 + ADDENDA 1-3 and CTO 03c1c6f001 + ADDENDA 1-4 SIGNED, 0 uncommitted; versioning Enabled; deployed-e

## STEP 0 AND STEP 2 READS (0.7.0_AE_CloudOps~FB1, 2026-10-12T06:16:03Z; the GO is AMENDMENT 13 @f5da2fc917)

**Required text (the CTO's condition): a hand run of E_24 exports BD_PLATINUM_MODE=canonical or it writes the legacy home** (E_24 now
also refuses an unset mode, `FB-g-7`).

- **Pair:** act-2 COO half `12b22ef020` + ADDENDUM 1 `1d7f94ebb1` + ADDENDA 2 and 3 (round 4); CTO half `03c1c6f001` + ADDENDA 1 to 4
  (`44e7a3f712` last), SIGNED at the current bytes, 0 uncommitted. The dispatcher at HEAD (blob `370c95552e`) is `2018982711`'s plus the
  `FB-g-15` guard (`c6aef00dac`) that COO ADDENDUM 2 names; against the live object (blob `631d6e6f4a`, equal to `96f3212d22`'s) it is
  40 insertions and 20 deletions, the numbers ADDENDUM 2 states; 0 bytes above 127.
- **Versioning** `opal-data-bd`: Enabled. **Deployed-equal before the act: 0 of 20.** The push hook has NOT shipped the 19 `.py`
  objects (two keys are new). Prior versions (18 present, 2 new keys that need none):

| key | prior VersionId | prior LastModified | vs HEAD |
|---|---|---|---|
| `code/gold/C_05.client_tax_liability.py` | YqgnppEg80iK97hxtMHshNtVFwuDUnLQ | 2026-07-09T19:58:04 | differs |
| `code/gold/C_06.client_mix_timeseries.py` | AREnJgLoyQnZ1zKwPan793py8CCkNHHA | 2026-10-11T06:20:04 | differs |
| `code/gold/C_07.advisor_attribution.py` | tZ7Wwj5x61yIIdNDSUGqwF7TjcXS07Ni | 2026-07-06T18:00:10 | differs |
| `code/gold/C_08.advisor_fee_efficiency.py` | qEevkpFT4KffZikRF8sBpYeCfa.JKC3C | 2026-09-27T05:47:50 | differs |
| `code/gold/D_00.portal_aggregates.py` | anWrmMfHewKok9jJ1hN3AABWEX7R4Pqf | 2026-07-24T17:07:21 | differs |
| `code/gold/D_00b.portal_timeseries.py` | ZNmwLpljcBHv63pQJaFHH3nOGDoC.rbZ | 2026-06-08T17:28:07 | differs |
| `code/gold/D_00c.portal_leaderboard.py` | MoFlEhFGZMURzc0wk_B6Ru45kOl9atmU | 2026-07-09T18:57:50 | differs |
| `code/gold/D_00f.advisor_nna_canonical.py` | h8_.GRABDePrlcnmkR7w.p.eRsNu4KKK | 2026-06-18T13:02:09 | differs |
| `code/gold/D_01.partner_analytics.py` | Wa9oOvBT6N.J188iZYgiHNJnb085liR1 | 2026-06-08T18:20:58 | differs |
| `code/gold/D_02.advisor_client_detail.py` | rPfpepK2VL2b9m1.VZeZJkjm._InlXN9 | 2026-08-18T20:27:41 | differs |
| `code/gold/D_03.composition_artifacts.py` | YNpZz346bYe1tWxkn3vfulYyNQXTHOpH | 2026-10-11T06:20:07 | differs |
| `code/gold/D_04.client_portal_summary.py` | N_isqMcDp.qdYQIJuzHV3bNQv9W6kor. | 2026-10-11T06:20:01 | differs |
| `code/gold/E_01.account_quality_tiers.py` | oYi4tzz.5Z1JQcLeT4yceEodNKXSSLW8 | 2026-09-27T05:48:01 | differs |
| `code/gold/E_24.rebuild_fee_scorecard.py` | eTubWXzpw4AUjRGYxFQRWApnW11kcVVz | 2026-09-27T05:49:34 | differs |
| `code/gold/lib/etf_classifier.py` | hnOzzH4QClDqa_qbd6Y5tqKu3Kag4vtM | 2026-10-09T09:54:21 | differs |
| `code/gold/lib/gold_utils.py` | 8ER4z09VIIXHvOxDlCDiJ12U7T._EIUE | 2026-05-12T20:58:26 | differs |
| `code/gold/lib/helpers.py` | Ccc.2tQQ3h5EEIgtp0Q.uYuM.fehKZc0 | 2026-05-11T20:43:01 | differs |
| `code/gold/lib/platinum_dest.py` | ABSENT (new key) | - | differs |
| `code/gold/lib/platinum_dest_view.py` | ABSENT (new key) | - | differs |
| `code/gold/gold_dispatch.sh` | VikjYXAEPXBxYRenSPh6YfD_PuuHLvTM | 2026-10-01T08:41:28 | differs |

- **Ownership-map baseline (the CTO's condition 3), printed at step 1:** legacy `platinum/49financial/ownership_map.json` in `opal-data-bd`
  VersionId `FcsnGhU7Rt280E9rmDacateI5WiK8S28`, LastModified 2026-10-12T05:22:13Z, 474,841 bytes: EXACTLY the GO's baseline. Canonical copy
  `advi/49financial/platinum/49financial/ownership_map.json` in `opal-data-49financial`: VersionId `XS0wkMtSm5c3ZZOOjsIri5FCmtD8rQvm`,
  LastModified 2026-10-11T04:01:18Z, 474,726 bytes (the GO's value).
- **Chain state (step 2c):** `bd-gold-layer-runner` i-01003b035d2988dfb `stopped` (launched 2026-10-12T04:00:46Z, stopped `User initiated`);
  the QA runner and the detail generator `stopped`; SSM invocations InProgress, Pending or Delayed account-wide: 0; invocations on the
  three gold instances in the last 14 h: 0. EventBridge `bd-gold-nightly-fallback` ENABLED `cron(0 23 ? * MON-SAT *)` (the next
  scheduled chain after this act: Monday 2026-10-12 23:00Z, plus the ~04:00Z chain Tuesday); `bd-gold-layer-monthly-trigger` DISABLED.
  The chain's own exit record is not readable from dell1 (as the GO states): the runner being stopped with nothing in flight is
  the read; it is not claimed as an exit code.
- **The role grant (policy-document read; simulate is denied to this identity):** `advi-49f-platinum-canonical-rw-policy` on
  `bd-exporter-ec2-role` matches PutObject and GetObject on the canonical prefix (`AdviPlatinumCanonicalObjects`), DeleteObject on the
  advisor directories (`AdviPlatinumCanonicalDelete`) and ListBucket under the prefix (`AdviPlatinumCanonicalList`); 0 Deny in the
  role's 16 inline policies. The first canonical chain run remains the live read of an SCP or the bucket-side exemption.
- **Actor's own authority:** `s3:PutObject` on `code/gold/*` allowed on this identity (simulated in the entry of 2026-10-11; unchanged).
- **Evidence:** `evidence/act2_move/step0_step2_reads.txt`, `objects_before_20_keys.json`.
