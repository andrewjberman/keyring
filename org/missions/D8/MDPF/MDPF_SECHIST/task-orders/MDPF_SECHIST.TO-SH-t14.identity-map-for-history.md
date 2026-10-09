# TO MDPF_SECHIST.TO-SH-t14 -- round 4 SH-t-14: identity map for history (FWD-6)

<to_id>MDPF_SECHIST.TO-SH-t14</to_id>
<project>MDPF_SECHIST</project>
<issued_to>0.9.0_WK_MDPF_SECHIST~13</issued_to>
<issued_by>2.0.0_SA_COO~H1</issued_by>
<issued_date>2026-10-09</issued_date>
<status>issued</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>4</round>

**Directive:** D8 | **Fabric:** dell1 | **Decomp cell:** `SH-t-14` (`decompositions/MDPF_SECHIST_DECOMP_R4.md`) | **outcome_ref:** FWD-6 |
**depends_on:** none (the census, SH-t-11, is merged @183e35580f)

---

## WORKER FACE

### THE CELL

`SH-t-14` (FWD-6). Cut on the CTO's ruling, round-2 analysis ADDENDUM 2 @8a279047c9
(`org/missions/D8/MDPF/MDPF_SECHIST/ledger/ROUND_ANALYSIS.round2.md`): `NAME::` is a canonical CLASSIFICATION key and NEVER an
IDENTITY for history. Build `data/mdpf/scripts/silver/security_identity_map.py`: for each `etf-classifications` row (input passed in,
the way the census read it: `org/missions/D8/MDPF/MDPF_SECHIST/deliverables/0.9.0_WK_MDPF_SECHIST~10/name_key_census.txt`), give ONE
identity for history or list it UNRESOLVED with its reason:
- a bare ticker or a `BBG:` key is its own identity;
- a non-ticker key form (`CUSIP:`, `ISIN:`, FIGI and the like) resolves through an EXISTING resolution path already in the estate --
  the MDPF_DEMQUE locked ticker map (`price_store` `lock.json` rows, `PRICE_STORE_CONTRACT.md`), a row's own ticker field, or
  `data/black_diamond/scripts/classification/resolve_tickers.py` -- to exactly one identity; more than one candidate is UNRESOLVED
  ("ambiguous"), none is UNRESOLVED ("no resolver match"). Build no new resolver and make no vendor call;
- a holding whose ONLY key is `NAME::` is listed `UNRESOLVED-FOR-HISTORY` with reason `name key only`. It is never guessed into a ticker
  and never becomes a pull label or join key.
Each output value carries its claim (MEASURED where a lock or a row field states it, INFERRED otherwise). Offline tests with fakes in
`data/mdpf/scripts/silver/test_security_identity_map.py`; the negative arm plants a `NAME::`-only row and asserts it is listed with
that reason and absent from the pull set the module returns.

### ACCEPTANCE

<criterion id="SH4-t14-AC1" cell_refs="SH-t-14"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECHIST_H1/R3_CHECKS/r3_named_tests.py IDENTITY data/mdpf/scripts/silver/test_security_identity_map.py test_non_ticker_key_resolves_to_one_identity test_unresolvable_listed_with_reason test_name_only_listed_never_pulled</invocation><expect>IDENTITY-TESTS-OK</expect></criterion>

<expected_criteria>SH4-t14-AC1</expected_criteria>

The criterion FAILS at the base (2026-10-09 ~14:1xZ): `IDENTITY-TESTS-BAD missing-file=data/mdpf/scripts/silver/test_security_identity_map.py`.
Run it from the worktree root; do not edit the check.

## BOUNDS

- Write only the files in `<paths>`. No S3 or DynamoDB write, no Bloomberg or Yahoo call. Classification rows are MDPF_SECCLASS's
  (C-TABLE): read them, never write them.
- A new S3 address or resource name is `lib/opal_naming.py` output only; a builder refusal is a missing registry row to report.
- Anything odd outside this cell: append ONE surprise row (dell1 id form `<CODE>-D1-W<n>-S<k>`) and keep working.

<paths>
data/mdpf/scripts/silver/security_identity_map.py
data/mdpf/scripts/silver/test_security_identity_map.py
org/missions/D8/MDPF/MDPF_SECHIST/deliverables/0.9.0_WK_MDPF_SECHIST~13/MDPF_SECHIST.TO-SH-t14.identity-map-for-history.proof_of_spec.json
</paths>

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_SECHIST/decompositions/MDPF_SECHIST_DECOMP_R4.md</decomp_doc> (round 4), cell `SH-t-14`.
<owned_cells>SH-t-14</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: SH4-t14-AC1. Instance at `org/missions/D8/MDPF/MDPF_SECHIST/deliverables/0.9.0_WK_MDPF_SECHIST~13/MDPF_SECHIST.TO-SH-t14.identity-map-for-history.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> SH4-t14-AC1` BEFORE the flip.
</proof_of_spec>

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE code and tests only; no schedule change.
comp-iam: DECLARED-NOT-APPLICABLE no AWS call; fakes only.
comp-adversary: RUN -- 5 of 5 round-4 criteria dry-run at the base 2026-10-09 ~15:4xZ, 5 FAIL (decomposition Battery); BLIND: which existing resolution path covers which key form, until the worker reads them.
risk: LOCAL.
direct_act: false -- a build cell.
</preflight>

Source: CTO round-2 analysis ADDENDUM 2 @8a279047c9 (msg 2521); census @183e35580f; PRD v0.2 C-IDENTITY.
