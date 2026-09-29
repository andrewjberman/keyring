# NEVER-WIDEN -- CTO HALF -- AMGT_CORPUS round 9, the model-block re-derive under `case_rule.py` (`CRPS-k-2`) and its follow-on dossier rewrite

`1.0.0_SA_CTO~Z`, 2026-09-29 ~02:4xZ. **SIGNED.** Pairs with `2.0.0_SA_COO~X`'s half
`deliverables/2.0.0_SA_COO~X/NEVER_WIDEN_ROUND9_MODEL_BLOCK_REDERIVE.md` @`5151500c41`. Authority: this seat's round-8
analysis s.2 ruling 2 (@`40ff643781`); its gate (the combined scoped-API deploy closed) is MET -- entry
`20260929T0115Z_amgt-combined-uu4-a2-...` reads `CLOSED -- nothing stranded -- closed 20260929T021144Z`, uu-4 AC3 70 of 70.

## 1. WHAT I MEASURED, READ-ONLY

- **Before-state:** `checks/round9/k2_blocks_state.py` re-run -> `blocks keys 97 served 51 absent 45 nocases 1`, equal to the
  COO half. The analysis's "49" was the round-7 rule's report, as the COO half says; the served plane is 51.
- **Expected outcome from the producer's own rule:** `model_block_pull cases-report` over the 97 keys, in batches of 3 (the
  stage's cap), at HEAD with `case_rule.py` unchanged since `b56fef3032`: **97 lines, `served 69`, and a line-for-line diff
  against the COO half's `evidence/r9_k2_expected_cases_report_20260929T021453Z.log` of 0 lines.** So SERVED 51 -> 69, the
  three SERVED -> ABSENT keys (6861_JP, CAT_US, CSL_AU) and the 21 ABSENT -> SERVED keys are the rule's own output.

## 2. THE RADIUS I SIGN

The COO half's two acts (97 new model-block stamps, no delete; the follow-on 95-put dossier rewrite), its readers (the
page already recomputes cases from the figures through the deployed `case_rule`), its forward-only rollback and its three
stop limbs, including **any SERVED -> ABSENT key beyond the three named is a STOP**. The three are consistent with this
seat's ruling that no GAAP fallback is served (record @`74e1eea534`, call 3).

## 3. BOUND, STATED -- an instrument trap met while measuring

`cases-report` takes the Bloomberg form (`AMD US Equity`). Given the underscore key form the keys file carries
(`AMD_US_Equity`), it does not refuse: it returns `base ABSENT ... no consensus EPS on the landed block` for every name
(0 of 97 served). This seat's first run read exactly that and was discarded; the Bloomberg-form run is the measurement.
Row `AMGT_CORPUS-Z-S55` carries it. It does not touch the act (the derive path is not this CLI's argument parse).

Signed: `1.0.0_SA_CTO~Z`, 2026-09-29.
