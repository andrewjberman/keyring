# MDPF_SECCLASS decomposition -- ROUND 15 (2.0.0_SA_COO~M1, dell1, 2026-10-08 ~19:2xZ)

**Status: DECOMPOSED.** The issuer is this seat. One issuance covers three cells.

**Cut on:**
- 1.0.0_SA_CTO~DELL1 msg 1061: row D1-S11, "cut the fix as the next round's cell".
- msg 1071: the amended acceptance is unclassified at or below 5.0 pct, and every hedge, private or real estate fund in
  alternatives. The fix is the NAME:: lookup in classify_with_identity plus the ~106 new rows.
- msg 1066: the rows cell also remaps every AI-landed row that breaks Andrew's rule. The prompt cell lands as written, and e49
  resumes on its commit.
- Andrew-direct 2026-10-08 ~19:0xZ, VERBATIM: "Hedge funds, private funds, real estate funds, all of this falls to Alternatives."
  Record: `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261008_190xZ_HEDGE_PRIVATE_REAL_ESTATE_FUNDS_ARE_ALTERNATIVES.md`.

**State the round starts from (measured this session):**
1. Trace `MDPF_SECCLASS_M/BD_UNCLASSIFIED_TRACE_D1S11_20261008.{md,json}` @3d9077bdc5. BD unclassified is $139.40M rebuilt against
   $140.16M served, of $2,019,548,568.
   - Group A: 796 securities, $133.58M. A canonical `NAME::` row exists, but
     `data/black_diamond/scripts/gold/lib/etf_classifier.py` `classify_with_identity` (:207-230) never reads it.
   - Group B: 25 securities, $2.21M. The ticker has no row.
   - Group D: 81 securities, $3.61M. No row under any key.
2. `R15_CHECKS/sc_r15_name_lookup.py` at the base: resolved 5 of 796.
3. `R15_CHECKS/sc_r15_rows_set.py` at the base: the denominator is 106 B/D securities, and the set is absent.
4. `_shared/etf_classification_model.py` `build_prompt` (:86-99) names the six classes but not the rule.
   `R15_CHECKS/sc_r15_prompt_rule.py` at the base: hedge, private and real_estate all read False.
5. e49 is paused at chunk 175-200: 120 landed, 836 remaining (~SD msg 1067). ~SD's read of the 120 landed rows found 0 genuine rule
   violations.
6. Row D1-S12: `safe-deploy.sh` re-ships every `lib/_shared` member on any BD gold deploy. A deploy half in this round names
   that, or diffs the shipped members first.

## Rule 24 record

- **Domain:** the three directives above, 4 clauses: the NAME:: lookup, the new rows for B/D, the rule remap of AI rows, and the
  prompt sentence. Each is placed once.
  - SC-e-76 takes the lookup.
  - SC-e-77 takes the new rows and the remap; one writer covers both, under one pair.
  - SC-e-78 takes the prompt.
  - The issuer's acts are the lib deploy and the table write under their pairs, and the e49 resume amendment.
- **(ii) Same grain:** one write set per cell. **(iii) Intent coherence:** one intent per cell.
- **(iv) State coherence:**
  - SC-e-76 adds a fallback after the identity chain fails, so a position the chain already places is not moved.
  - SC-e-77 builds a set and a writer and writes nothing.
  - SC-e-78 changes one instruction string. The model's six-value vocabulary and the data-object injection rule do not move.

## The cells

| cell | what | serves | risk | depends on |
|---|---|---|---|---|
| `SC-e-76` | In BD's `classify_with_identity`, when the identity chain returns no key (or a key with no row), read `NAME::` + `normalize_name(asset_name)` and serve that row. Pin by test; write the half request for the lib deploy | FWD-16 | WORLD (shipped BD gold lib; deploy by the issuer under the pair) | -- |
| `SC-e-77` | The D1-S11 row set: one NEW row per B/D security (106), each in one of the six, with every hedge, private or real estate fund in alternatives. Plus REMAP lines for AI-landed rows (e32/e49) that are such funds outside alternatives. Also a conditional writer (dry run, `--write`, `--rollback`) and its half request | FWD-16, FWD-17 | WORLD (table write by the issuer under the pair) | -- |
| `SC-e-78` | `build_prompt`'s instruction states Andrew's rule (hedge, private and real estate funds are alternatives), pinned by test; the data-object rule is unchanged | FWD-17 | WORLD (shipped `_shared`; the e49 runner reads the repo module on dell1) | -- |

## Write sets

- **SC-e-76:**
  - `data/black_diamond/scripts/gold/lib/etf_classifier.py`
  - `data/black_diamond/scripts/gold/tests/test_etf_classifier_name_key.py`
  - `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/NEVER_WIDEN_HALF_REQUEST_SECCLASS_BD_NAME_KEY_LOOKUP_20261008.md`
- **SC-e-77:**
  - `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/S11_ROW_SET_20261008.tsv`
  - `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R15_CHECKS/s11_rows_write.py`
  - `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/NEVER_WIDEN_HALF_REQUEST_SECCLASS_S11_ROWS_20261008.md`
- **SC-e-78:**
  - `infra/aws/lambda/v2_portal/_shared/etf_classification_model.py`
  - `infra/aws/lambda/v2_portal/_shared/tests/test_prompt_alternatives_rule.py`
- Every cell may append rows to `org/missions/D8/MDPF/MDPF_SECCLASS/surprise-channel/investigations/INVESTIGATION_v1.md`.
- The write sets are disjoint. COT's `lib/etf_classifier.py` copy is not in this round. If it carries the same gap, SC-e-76 files a row.

## Dependency edges

None between the cells. **Chains:** 3 single-cell chains, so M = 3. Fan-out 3 of 3, cap 8.
Issuer acts after the cells:
1. SC-e-78's commit, then the e49 resume amendment (`--workers 2`, per ~SD msg 1067's transport rate).
2. SC-e-77's write under its pair.
3. SC-e-76's deploy under its pair, before a BD gold fire.
4. Acceptance on the next served BD firm mix: unclassified at or below 5.0 pct, and every hedge, private or real estate fund in
   alternatives.
