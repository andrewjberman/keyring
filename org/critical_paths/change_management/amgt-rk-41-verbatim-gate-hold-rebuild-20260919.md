# DEPLOY LEDGER -- AMGT_RESAPP AMGT-rk-41: C-VERBATIM-GATE = HOLD, drafting/v1 rebuild

**Opened:** 2026-09-19T05:17Z by 0.9.0_WK_AMGT_RESAPP~43 (deploy-start, before AC6; NEVER#6)
**Status:** OPEN (closes on completion of this entry, same session)
**PRD:** org/missions/D5/AMGT/AMGT_RESAPP/prd/AMGT_RESAPP_PRD.md v0.13 @1699960261
  `C-VERBATIM-GATE` :907-920, `C-VALIDATION-NAMES` :1652-1658, `C-PRODUCTION-HOME` :1617-1650
**Never-widen pair (both on file, section `AMGT-rk-41` present, SIGNED at re-signature
2026-09-18 ~23:3xZ against COO halves `541d395e0d`):**
  - COO half: `org/missions/D5/AMGT/AMGT_RESAPP/ledger/NEVER_WIDEN_ROUND14_CHAIN_F_COO_HALVES.md`
    sha256 `3cebb1945f39560b074c3a85f90e8250def4f576acf9a78d0f1226d32ec61a5d` (measured fresh, this
    worktree, at open)
  - CTO half: `org/missions/D5/AMGT/AMGT_RESAPP/ledger/NEVER_WIDEN_ROUND14_CHAIN_F_CTO_HALVES.md`
    sha256 `e28490dad2446b4cee7ffc0f1ffa32a4d4a1db0b08ced9b8324b873d302ad64c` (measured fresh, this
    worktree, at open)

## The act

`python -m lib.research.filings.drafting_build --rebuild-pool --population
crosswalk/v1/2026-09-15.json --dry-run` (AC5, read-only, run first) then, live, `python -m
lib.research.filings.drafting_build --rebuild-pool --population crosswalk/v1/2026-09-15.json
--only-keys CAT_US_Equity,CSL_AU_Equity,6861_JP_Equity --pre-act-dir
.scratch/drafting_v1_preact` (AC6). ONE rebuild, through the ONE writer
(`analyze.write_outputs(..., drafting_only=True)`), of `drafting/v1/<key>.json` -- NO model call
(build_drafting_document is a pure re-apply of the gate over the STORED analysis), NO Lambda
redeploy.

## Blast radius (issuer bind D4, CTO msg 23833; narrowed at re-signature)

**LIVE this round:** ONLY the three validation names `CAT_US_Equity`, `CSL_AU_Equity`,
`6861_JP_Equity`, each REWRITTEN IN PLACE at `drafting/v1/<key>.json` if and only if the pool
carries an analysis object for that key (`filings/v1/<key>/*.analysis.json`); a name with none is
reported NOT ATTEMPTED, never a FAIL. Measured at AC5's cut (this session, read-only): none of the
three carries a pool analysis object yet (`rk-38`/`rk-39`/`rk-40` not drained at this HEAD,
`b501ea3c82`), so the LIVE leg is expected to REBUILD 0 of 3 -- recorded here as the DESIRED
outcome per the producer's own rule (`_newest_analysis_key` returns None for all three), not
assumed before AC6 runs.

**DRY-RUN ONLY this round (never written):** the twelve covered `drafting/v1` keys the measured
population (`crosswalk/v1/2026-09-15.json`, MEASURED=33) already carries an analysis object for.
AC5's fresh read (this session) -- key: pre-act sha256 (document-sha256 Metadata, `head_object`):

| key | served_on_span | held_no_span | refused | sentences_drafted | pre_act_sha256 |
|---|---|---|---|---|---|
| ASML_NA_Equity | 2 | 8 | 3 | 13 | `68995eb736aa83ff239e97ff55781b2c28817882112df47a017fbdc438249087` |
| BABA_US_Equity | 34 | 2 | 4 | 40 | `1da4627a9a6d86a61ec6f63e4dc85163f418a16849e4a5d7839e1160cb047ee0` |
| BA_US_Equity | 17 | 21 | 2 | 40 | `50e76d82833b6c76b35c86ce79ad7002524ad4d5e39e249f83f27c3ea7452122` |
| COST_US_Equity | 15 | 24 | 1 | 40 | `d0c719ac097acd21fd447dcd1397571c32b5dc8fd576abc96273ae30302830e7` |
| HAL_US_Equity | 11 | 7 | 22 | 40 | `7b9cdb09e94900dbc14e3487d87b96d5a7afb41509a8f8e86d0dd82bae776de3` |
| HD_US_Equity | 20 | 16 | 4 | 40 | `9a55e1ae052e0f7ef2544d7a8b57170c2b61da5d7995e18fd95d54f1fbfe394d` |
| INTU_US_Equity | 26 | 14 | 0 | 40 | `bedcbe982610368f56df3de4bc40512e60345e1deba3bd874c1e0e36c46385f7` |
| KMB_US_Equity | 18 | 21 | 1 | 40 | `35285a89b7fc67e7560775f80bcbcdeded0329c0b6293679dc2beecc2268cc6b` |
| NU_US_Equity | 8 | 19 | 13 | 40 | `754119f46084df63c97ed588258e694c0f086ad54a820ee4c31b54cea16d5d6e` |
| PBR_US_Equity | 16 | 13 | 11 | 40 | `d94534b006ca05c0abe29acad7f96d17d983178e728567358123a9a736b51113` |
| SAP_GY_Equity | 30 | 8 | 0 | 38 | `3800c516b78eb8750cc83c7c83e294923eb254687cc3af1fc09c98ed5e2f6ae4` |
| VLO_US_Equity | 13 | 26 | 1 | 40 | `79d8878ee8f02131cf27b172b130ee1225baa5671956923ffb4fac052348937a` |

TOTALS (12 keys): served_on_span=210 held_no_span=179 refused=62 -- served_on_span + held_no_span
= 389, matching the CRO's previously measured total served count exactly (msg 23744); held_no_span
179 matches the CRO's measured 179 exactly. 21 of the 33 measured names carry no analysis object
(NOT ATTEMPTED, no analysis object) and are untouched either way.

None of these twelve is written by this deploy -- AC6 runs `--only-keys` naming ONLY the three
validation names, so the covered twelve stay exactly as measured above (DRY-RUN only, per D4: a
rebuild of the covered population is a producer re-run over covered names, barred by Andrew's
standing word until the process is validated end to end).

## Readers of the moved property

`lib/research/api/scoped_amgt.py:1594` (thesis bundle / `read_drafted_sections`), `:2574-2592`
(description line, sentence[0] of `company_description`), `lib/research/posture/packs.py:107`
(Thesis D-1 input). Writers of `drafting/v1/<key>`: N = 1 at this act (`analyze.write_outputs`,
AMGT-rk-42 landed @eea3d7917c collapsing the prior N=2 into one writer; the composing rule is
`build_drafting_document` / `pipeline.py` / `verbatim.py`, unchanged by count).

## Expected outcome, both branches (D3 bind, bound in the order and closed at re-signature)

The rebuilt document ships ONLY `PASS` sentences in `sections[].sentences`; every held sentence is
carried in a top-level `held_no_span` block and in the printed split; no sentence in
`sections[].sentences` carries a `verbatim_check` outside `{PASS, REFUSE}` -- AC6 prints
`sections_values` per key and it must read a subset of `{PASS, REFUSE}`. Branch A (an analysis
object exists for a validation name): REWRITTEN in place, served_no_span 0, held_no_span_count
printed. Branch B (no analysis object, all three as measured at open): NOT ATTEMPTED, nothing
written, REBUILT 0 of 3 -- both branches are covered; neither is a FAIL.

## Rollback

Per-key: `--pre-act-dir .scratch/drafting_v1_preact` saves the pre-act bytes of every LIVE-touched
key BEFORE its first write. Rollback = re-put the saved bytes to the same key
(`crosswalk.write_pool`), then `head_object` read-back of the sha256. Not exercised if AC6
rebuilds 0 keys (branch B above) -- no key is touched, nothing to roll back.

## Close (checked only when TRUE, with evidence)

- [ ] AC6 run; per-key line(s) recorded (pre_act_sha256, post_act_sha256, sections_values) or
      NOT ATTEMPTED reasons for all 3 validation names
- [ ] AC7 before/after Lambda-invoke pair recorded for BA_US_Equity (a covered, non-validation
      key -- DRY-RUN only this round, so the before/after reading is expected UNCHANGED; this is
      the ISSUER BIND D4's own consequence, not a rollback condition)
- [ ] CLOSED with post-act sha256 per key actually written (or "0 keys written" if branch B)
