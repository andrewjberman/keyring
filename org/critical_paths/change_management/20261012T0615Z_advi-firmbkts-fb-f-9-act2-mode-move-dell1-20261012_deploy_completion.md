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
| L2 | s3-prefix | s3://opal-data-bd/code/gold/ 19 .py objects (14 writers + 5 lib) shipped through .tools/safe-deploy.sh and read back (step 3) | 19 of 19 equal git show HEAD:<path>, sha256 per key | step 3: 19 of 19 .py objects equal git show HEAD:<path> (sha256) read 2026-10-12T06:21:27Z; shipped through .tools/safe-deploy.sh in two runs (run 1 shipped 1 of 19 because this lane's path list carried CRs; run 2 shipped the 18 remaining, 18 DEPLOYED 18 VERIFY OK); 18 prior VersionIds and 2 new keys recorded in the entry | CLOSED 20261012T062338Z |
| L3 | s3-prefix | s3://opal-data-bd/code/gold/gold_dispatch.sh -- the switch (step 4), aws s3 cp --sse AES256 then cmp, MOVE_TS read after the copy returned | cmp equal, 0 bytes above 127, MOVE_TS printed, ownership-map baseline re-printed | step 4: gold_dispatch.sh HEAD blob 370c95552e 75897 bytes copied 06:22:06Z with --sse AES256, new VersionId JTxOlFbqGVj9SOajf2YKlMVo.E3Sv35K, cmp read-back EQUAL, 0 bytes above 127; MOVE_TS=2026-10-12T06:22:08Z (S3 LastModified 06:22:09Z); prior object VersionId VikjYXAEPXBxYRenSPh6YfD_PuuHLvTM git blob 631d6e6f4a; ownership-map legacy baseline re-printed unchanged (FcsnGhU7Rt280E9rmDacateI5WiK8S28) | CLOSED 20261012T062339Z |
| L4 | verify | AC1 deployed-equal 20 of 20 and the legacy-quiet read old-home --since MOVE_TS (it must name exec_summary.json among the classes it covers) | the two outputs quoted | AC1 deployed-equal: DEPLOY EQUAL: 20 of 20 objects equal the repository at HEAD (06:22:38Z); old-home --since 2026-10-12T06:22:08Z: OLD HOME QUIET: 0 keys of 11 classes modified (the 11 include platinum/advisors/ which holds exec_summary.json); AC2 0 of 11 because no chain has run, not graded | CLOSED 20261012T062339Z |
| L5 | activation | the first SCHEDULED production chain AFTER act 4 (step 5): exit, run log with no ValueError and no NoSuchKey on a served read (a read after the issuer's act 4, not before) | the chain evidence |  | OPEN |
| L6 | verify | AC2 new-home 11 of 11 since MOVE_TS and AC3 old-home 0 keys of 11 classes since MOVE_TS, read after that chain | the outputs of r3_act2_reads.py quoted |  | OPEN |
| L7 | git | proof instance written and TO-FB-f-9 status flipped complete in one commit | commit hash |  | OPEN |

## Log

- 20261012T061517Z OPENED by 0.7.0_AE_CloudOps~FB1 with 7 leg(s)
- 20261012T061603Z LEG L1 closed: pair COO 12b22ef020 + ADDENDA 1-3 and CTO 03c1c6f001 + ADDENDA 1-4 SIGNED, 0 uncommitted; versioning Enabled; deployed-e
- 20261012T062338Z LEG L2 closed: step 3: 19 of 19 .py objects equal git show HEAD:<path> (sha256) read 2026-10-12T06:21:27Z; shipped through .tools/safe-
- 20261012T062339Z LEG L3 closed: step 4: gold_dispatch.sh HEAD blob 370c95552e 75897 bytes copied 06:22:06Z with --sse AES256, new VersionId JTxOlFbqGVj9
- 20261012T062339Z LEG L4 closed: AC1 deployed-equal: DEPLOY EQUAL: 20 of 20 objects equal the repository at HEAD (06:22:38Z); old-home --since 2026-10-12

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

## STEP 3 AND STEP 4 -- THE SHIPMENT AND THE SWITCH (0.7.0_AE_CloudOps~FB1, 2026-10-12T06:23:38Z)

- **Step 3, the 19 `.py` objects:** `.tools/safe-deploy.sh --author 0.7.0_AE_CloudOps~FB1 --tree black_diamond <paths>` (upload of the
  index blob, ETag equal to the blob's md5, comp-pipescript confirm), two runs: run 1 named 19 paths and shipped 1
  (`lib/platinum_dest_view.py`): this lane's path list carried a trailing carriage return on 18 lines and the tool ignored them
  silently (its receipt said "1 path(s) to deploy"); run 2 named the 18 remaining, clean, 18 DEPLOYED and 18 VERIFY OK. No object was
  shipped twice. Read back 19 of 19 equal to `git show HEAD:<path>` (sha256), 06:21:27Z. `evidence/act2_move/py19_after.json`.

| key | prior VersionId | new VersionId |
|---|---|---|
| `code/gold/C_05.client_tax_liability.py` | YqgnppEg80iK97hxtMHshNtVFwuDUnLQ | Hgs5ns1ZAFnKzwS3GX8tLqvHp7kwehqm |
| `code/gold/C_06.client_mix_timeseries.py` | AREnJgLoyQnZ1zKwPan793py8CCkNHHA | 5xAeM.OWYUSxd7gHYSF6SKmR.ZTmo.PP |
| `code/gold/C_07.advisor_attribution.py` | tZ7Wwj5x61yIIdNDSUGqwF7TjcXS07Ni | GSQxSQjT94vGZOmQ4s5uLh5zM4CiHkzj |
| `code/gold/C_08.advisor_fee_efficiency.py` | qEevkpFT4KffZikRF8sBpYeCfa.JKC3C | AwSisOdioHrIleZRK20p2jfw9G3TeI_h |
| `code/gold/D_00.portal_aggregates.py` | anWrmMfHewKok9jJ1hN3AABWEX7R4Pqf | hAA2jEJvGBoGRWHzZUuDLmci3cW5enME |
| `code/gold/D_00b.portal_timeseries.py` | ZNmwLpljcBHv63pQJaFHH3nOGDoC.rbZ | JbRIXX0BSjYEucoGkHEEHdTXleFVM.Qi |
| `code/gold/D_00c.portal_leaderboard.py` | MoFlEhFGZMURzc0wk_B6Ru45kOl9atmU | NvfUwJI2KxPgfooU0l1UJvWWT2Qk6B3g |
| `code/gold/D_00f.advisor_nna_canonical.py` | h8_.GRABDePrlcnmkR7w.p.eRsNu4KKK | p8fzjL9ePXL5_xs3bXMRX.4u.mcnInQc |
| `code/gold/D_01.partner_analytics.py` | Wa9oOvBT6N.J188iZYgiHNJnb085liR1 | FbyKa20OM50RrvEVAKjPo4G3d_GiAY0R |
| `code/gold/D_02.advisor_client_detail.py` | rPfpepK2VL2b9m1.VZeZJkjm._InlXN9 | YakZC5Xn99vjZmRiP79DjIZJAE3qS6XD |
| `code/gold/D_03.composition_artifacts.py` | YNpZz346bYe1tWxkn3vfulYyNQXTHOpH | A8UtTTbdB0LL7iiyhfEl1XdyHwW_.Fjo |
| `code/gold/D_04.client_portal_summary.py` | N_isqMcDp.qdYQIJuzHV3bNQv9W6kor. | ap.CyBT8aJijz5kWFsSNjEFU99itbXED |
| `code/gold/E_01.account_quality_tiers.py` | oYi4tzz.5Z1JQcLeT4yceEodNKXSSLW8 | floBGIOpKN9LG2wUHt9yOhjex.xB56gX |
| `code/gold/E_24.rebuild_fee_scorecard.py` | eTubWXzpw4AUjRGYxFQRWApnW11kcVVz | 6Tpbi7maASJDI1YRpK0RjD_G6i7SBHDs |
| `code/gold/lib/etf_classifier.py` | hnOzzH4QClDqa_qbd6Y5tqKu3Kag4vtM | 0jhXHH7axm_H934t5s5gVDVNJ6Y_WqI. |
| `code/gold/lib/gold_utils.py` | 8ER4z09VIIXHvOxDlCDiJ12U7T._EIUE | pJMnvi5FZyuocTAQfXCzcLne.RsEAKWC |
| `code/gold/lib/helpers.py` | Ccc.2tQQ3h5EEIgtp0Q.uYuM.fehKZc0 | IUnYWr1Yx4sAnaIxMQ3qqRQpUEUygZS6 |
| `code/gold/lib/platinum_dest.py` | ABSENT (new key) | BMu_D3jV0AWkNof4byZxpu08cVRl0.MN |
| `code/gold/lib/platinum_dest_view.py` | ABSENT (new key) | k28U1C7uz1XNni9WO8zpcjCw1fgseeB7 |

- **Step 4, the switch:** `gold_dispatch.sh` (HEAD blob `370c95552e`, 75,897 bytes, 0 CR, 0 bytes above 127) copied to
  `s3://opal-data-bd/code/gold/gold_dispatch.sh` with `aws s3 cp --sse AES256` at 06:22:06Z; new VersionId
  `JTxOlFbqGVj9SOajf2YKlMVo.E3Sv35K`, SSE AES256; read back and `cmp` EQUAL. **Prior object (the rollback): VersionId `VikjYXAEPXBxYRenSPh6YfD_PuuHLvTM`, LastModified 2026-10-01T08:41:28Z,
  74731 bytes, git blob `631d6e6f4ae39909b88926a500499646fd6ccb01` (= `96f3212d22`'s).**
- **`MOVE_TS` = 2026-10-12T06:22:08Z** (this lane's clock, read after the copy returned; S3 stamps the object `2026-10-12T06:22:09Z`, so the local
  clock reads about one second behind S3's; both are recorded).
- **Ownership-map baseline re-printed at step 4 (the CTO's condition 3):** legacy `platinum/49financial/ownership_map.json`
  VersionId `FcsnGhU7Rt280E9rmDacateI5WiK8S28`, LastModified 2026-10-12T05:22:13Z, 474,841 bytes: UNCHANGED from the GO's baseline
  and from step 1. Canonical copy VersionId `XS0wkMtSm5c3ZZOOjsIri5FCmtD8rQvm`, LastModified 2026-10-11T04:01:18Z, 474,726 bytes: unchanged.
- **Before the switch (06:21:27Z):** gold runner, QA runner and detail generator `stopped`; SSM invocations in flight 0.
- **AC1** `deployed-equal`: `DEPLOY EQUAL: 20 of 20 objects equal the repository at HEAD` (06:22:38Z).
- **Legacy-quiet read (AC3's form) at 06:22:38Z:** `OLD HOME QUIET: 0 keys of 11 classes modified since 2026-10-12T06:22:08Z`; the class
  `platinum/advisors/` is among the 11 and holds `<id>/exec_summary.json` (the script prints class prefixes and counts, never a key
  under an entity). `evidence/act2_move/ac3_old_home_quiet.out`.
- **AC2** (`new-home --since`) reads 0 of 11 because no chain has run since the move; it is NOT graded here. It and AC3 are read
  again after the first SCHEDULED chain that follows act 4 (legs L5 and L6).
- **State of the world, stated:** the mode is moved for the next scheduled production chain (`--chain`, not dry-run, not QA) and
  nothing has run. The router, the validator and the IRPT consumers still read the legacy home until act 4. Acts 3, 4b and 4c follow.
  **If act 4 cannot land before the next scheduled chain (Monday 23:00Z fallback), this act rolls back the same hour:** re-upload
  `gold_dispatch.sh` VersionId `VikjYXAEPXBxYRenSPh6YfD_PuuHLvTM` through `aws s3api copy-object` or `aws s3 cp` of that version's bytes, read back with `cmp`.
- **Not done by this lane, as ordered:** no gold script, no dispatcher run, no SSM command, no delete, no copy of data.
