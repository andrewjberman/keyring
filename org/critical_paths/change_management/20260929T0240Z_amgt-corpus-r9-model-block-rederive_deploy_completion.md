# Deploy Completion Record
**Date opened:** 2026-09-29T02:40:37.126812+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260929T031451Z
**Deploy:** AMGT_CORPUS round 9 k-2: model_block_pull derive over 97 keys under case_rule.py (batches of 3), then the follow-on dossier rewrite; pair COO 5151500c41 / CTO 0fbb50e84e; gate amgt-combined-uu4-a2 CLOSED 02:11:44Z
**Authored by:** 2.0.0_SA_COO~X
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 3.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| D | activation | derive over the 97 keys in batches of 3 (served derived/model_block) | every batch rc 0; 97 new stamps | evidence/r9_k2_derive.log: 33 of 33 batches rc 0 (02:4x-02:47:36Z), 97 DERIVE lines, 0 non-zero; 97 of 97 newest stamps dated 20260929 (evidence/r9_k2_blocks_after.txt) | CLOSED 20260929T024849Z |
| DV | verify | served blocks vs the rule's expected log | k2_blocks_state: served 69; verify keys 97 match 97 mismatch 0; SERVED->ABSENT exactly 6861_JP CAT_US CSL_AU | evidence/r9_k2_blocks_after.txt (k2_blocks_state.py vs the expected log r9_k2_expected_cases_report_20260929T021453Z.log): blocks keys 97 served 69 absent 28 nocases 0; verify keys 97 match 97 mismatch 0; SERVED->ABSENT exactly 6861_JP_Equity, CAT_US_Equity, CSL_AU_Equity (before 51 served) | CLOSED 20260929T024849Z |
| F | activation | follow-on dossier --write --workers 10 (served research-dossier) | 95 put_performed, 0 ERROR; objects 563 -> 658 | evidence/r9_k2_followon_dossier_rewrite.log: dossier --write --workers 10, rc 0, 0 ERROR, 'names 95 written 93 existed 2'. PREDICTION MISS IN THE COO HALF, NOT IN THE ACT: the half expected 95 puts assuming every dossier name has a model block; 93 do. BP/_LN_Equity and NG/_LN_Equity carry no block key (the 97 block keys and the 95 dossier names differ by these two and by 6861_JP, CAT_US, CSL_AU, NVDA_US), so the re-derive moves no input of theirs and write_one took its unchanged branch ('unchanged inputs_sha16 ... wrote 0') as its rule states. Objects 563 -> 656 (+93) | CLOSED 20260929T031450Z |
| FV | verify | dossier after the follow-on | serves the last write 95 of 95; dossier_pick stale_pick 0; case_census unchanged | evidence/r9_k2_followon_after.txt: partitions 95 objects 656; read_dossier serves the last write 95 of 95; rewrites_on_unchanged_inputs 37 (unchanged); dossier_pick names 95 current_method_available 95 stale_pick 0 (BP/ and NG/ serve their /2 object from the first rewrite); case_census body 84 heading_only 0 absent 201 ordering_violated 0 unit_carried 10 (unchanged) | CLOSED 20260929T031451Z |

## Log

- 20260929T024037Z OPENED by 2.0.0_SA_COO~X with 4 leg(s)
- 20260929T024849Z LEG D closed: evidence/r9_k2_derive.log: 33 of 33 batches rc 0 (02:4x-02:47:36Z), 97 DERIVE lines, 0 non-zero; 97 of 97 newest stamps 
- 20260929T024849Z LEG DV closed: evidence/r9_k2_blocks_after.txt (k2_blocks_state.py vs the expected log r9_k2_expected_cases_report_20260929T021453Z.log
- 20260929T031450Z LEG F closed: evidence/r9_k2_followon_dossier_rewrite.log: dossier --write --workers 10, rc 0, 0 ERROR, 'names 95 written 93 existed 2
- 20260929T031451Z LEG FV closed: evidence/r9_k2_followon_after.txt: partitions 95 objects 656; read_dossier serves the last write 95 of 95; rewrites_on_u
- 20260929T031451Z CLOSED -- all 4 legs proven
