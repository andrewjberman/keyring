# NEVER-WIDEN SIGN-OFF, CRO HALF -- mdpf-gold-lambda Cottonwood FIX-FORWARD (pin 5991626d4f)

**Author:** 4.0.0_SA_CRO. **Packet:** `org/tier2_senior/0.7.0_AE_CloudOps/deliverables/NEVER_WIDEN_SIGNOFF_PACKET_MDPF_COTTONWOOD_FIXFORWARD_20260922.md`
blob `0194edad411b85ce45be6be9814b0c8877cc5191` (`git hash-object` of the working file == the blob named in msg 99524).
**CRO half covers:** s.1, s.3, s.6, s.7 (packet s.8).

## VERDICT: REFUSE -- on s.6 only. s.1, s.3 and s.7 are sign-ready; re-sign follows one packet amendment.

## s.6 -- REFUSED: the blast radius omits three write surfaces the real invoke reaches

s.6 states: *"No key outside these two prefixes is reachable by either function's role"* (the two prefixes being
`opal-data-assets/portal/gold/mdpf/` and `opal-data-portal-v2/platinum/mdpf/`). At the pin this is false. LEG C's
invoke is the production branch (`{}`, not qa_local), and that branch of `run_cottonwood_family`
(`mdpf_gold_consolidator.py:1113` @5991626d4f) runs three writers IN-PROCESS before any portal key:

| writer (call site @5991626d4f) | key written, bucket `opal-data-assets` | source |
|---|---|---|
| `bdmp.main(["--date", adate, "--upload"])` :1206 | `blackdiamond/cottonwood/gold/dim_model_portfolio/date=<adate>/data.parquet` | `build_dim_model_portfolio.py:72` GOLD_PREFIX, `:531-535` put_object |
| `slice_mod.main(["--upload"])` :1212 | `gold/mdpf_revamp/cottonwood/aggregate_aua_timeseries.json` | `build_cottonwood_mdpf_slice.py:122-123` SLICE_KEY, `:1153` |
| `pair_mod.main(["--date", adate, "--upload"])` :1216 | `gold/mdpf_revamp/cottonwood/<filename>` (distribution, metrics, and the `account_units.json` sidecar s.3 itself names) | `build_cottonwood_mdpf_pair.py:134` STAGING_PREFIX, `:741-745` `_stage_upload` |

Two of the three (slice, pair) are Phase A+B code, changed in this zip (+128/-8, +46/-6, s.2), so their outputs are
exactly the bytes this act changes. s.3 already depends on one of them (the sidecar decides 16 vs 15) without s.6
covering it.

**Not new exposure, so this is a completeness refusal, not a hazard:** the RUNNING pin `48b8671569` makes the same three
calls (`:1172/:1178/:1182`, wired at `:1265`), so the scheduled fire writes these keys daily. What is new is the code
producing them, and a rollback that restores the portal keys but leaves the staged Cottonwood gold and sidecar at
fix-forward content is a half rollback.

**Amendment that clears the refusal (text only, no re-measure beyond one versioning read):** add a C-stage row to s.6
naming the three keys above, and state `opal-data-assets` versioning (already read Enabled for the portal keys; the same
bucket) with per-key rollback by prior VersionId. Also correct the sentence to "no key outside these FOUR prefixes". The dim
partition is keyed by assignment date, and per the code comment at `:1123-1125` a re-run rewrites a landed date. So
state which `adate` the invoke will write (newest `fact_model_assignment` partition), and that its prior version, if
one exists, is the rollback.

## s.1 -- sign-ready

- `1465fd3f7d` is NOT an ancestor of the running `48b8671569`: `git merge-base --is-ancestor` rc=1, measured by this
  seat. So the deployed plane has lacked the 09-11 null-tail guard, as stated.
- `74d7efe144` IS an ancestor of `5991626d4f` (rc=0), and `git log 74d7efe144..5991626d4f` = exactly the 3 commits
  s.2's table names (`47e00fa9ad`, `3756c846a4`, `5991626d4f`). The pin is what was signed yesterday plus those three.
- The misread is owned (row MDPF_COTREMEDIATION-S20). The custom-model cause is excluded with a reason. Accepted.

## s.3 -- sign-ready, with one NOTE

The two named outcomes (16/16; 15/16 with `global/account-distribution` ABSENT) are consistent with the code read. NOTE,
not a condition: the null-tail guard (reader 1) WITHHOLDS a scope's category-views when its LATEST cell is null. On
the production vintage cottonwood's values lag its axis (09-18 vs 09-21 was the measured shape). So a third reachable
branch exists unless reader 2's roll-forward fills that cell for the category-views path too: cottonwood
`category-views` ABSENT (withheld, never zero-filled). This does not widen anything, since an ABSENT writes nothing and
stays inside the blast radius, so it needs no signature. But Andrew's visual smoke should be told it is possible
rather than meet it as a surprise. The s.7 step-4 ping should report per-scope ABSENTs by name.

## s.7 -- sign-ready

The sequence runs ledger first, then build-pinned upload of the exact signed file, a code-gated targeted plan, a
read-back, ONE invoke each, and a served read. The will-nots (no HEAD build, no rebuild, no EC2 act, no LEG B restore,
no window widening, no qa_local acceptance, no second invoke) match Andrew's rulings: "Leave them, cover in the fix"
(MSTR 99504) and the fix-forward direction quoted in the packet. LEG B stays open until MSTR's push reads ETag
`a2b5f5980e9f66c9b1cfc2f67c8586dd`. Accepted.

## Instruments (different from the packet's)

`git merge-base --is-ancestor` (x3), `git log` range, and `git show <pin>:<file>` reads of the consolidator and all
three builders at 5991626d4f and 48b8671569. No AWS read by this seat. The versioning claim is the packet's (s.6) and
is not re-measured here.
