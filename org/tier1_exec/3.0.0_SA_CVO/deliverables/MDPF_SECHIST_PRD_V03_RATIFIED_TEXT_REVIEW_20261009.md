# MDPF_SECHIST PRD v0.3 -- ratified-text half review (L4-R re-sign)

**Reviewer:** `3.0.0_SA_CVO` (dell1). **Object:** `org/missions/D8/MDPF/MDPF_SECHIST/prd/MDPF_SECHIST_PRD.md` @847e1e265e (msg 2774).
**Diff read:** `git diff cc2a7a5430 847e1e265e` on the PRD: the header, the C-MMF row (line 96) and the v0.3 addendum. No ENDPOINT line
and no FWD line changed. **Verdict: SIGN.**

## Checks

| Check | Result | Evidence |
|---|---|---|
| ENDPOINT and FWD text untouched | PASS | the PRD diff touches only `prd_version`, the C-MMF row and the addendum; `prd-signoff status` reads current by ENDPOINT hash. |
| Andrew's protected term kept | PASS | line 96: "until then that day's window is blank, never estimated". |
| Amendment grounded on a measurement | PASS | ledger commit da5f4eddee: request MDPF_SECHIST-SHT8-TR-FIELD-HISTORY-20261009, 16 cells quoted, 16 drawn, 16 of 16 non-null, every value exactly 1 (SALXX and FXFXX, 8 trading days each). A flat level cannot carry a daily return. |
| The new source is named exactly | PASS | `DAY_TO_DAY_TOT_RETURN_GROSS_DVDS`; the level field is excluded by name. |

## Note for FWD-9's grade (not a refusal)

- The C-MMF row says an empty first day "is RE-REQUESTED on the next run until it fills". Nothing yet shows that the field fills on a
  later request. At L9, FWD-9 is graded on a served re-requested day that turned from blank to a value, read from the store. A day that
  stays blank also passes the contract, but it does not show that the re-request works.

-- 3.0.0_SA_CVO
