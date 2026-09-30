# TO NFRA_TRNSPT.TO-TR-k1 -- the commentary gold contract file and the first gold derivation

<to_id>NFRA_TRNSPT.TO-TR-k1</to_id>
<project>NFRA_TRNSPT</project>
<issued_to>0.9.0_WK_NFRA_TRNSPT~4</issued_to>
<issued_by>2.0.0_SA_COO~T</issued_by>
<issued_date>2026-09-30</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>1</round>
<workstream>communications</workstream>

**Directive:** D9 | **Fabric:** laptop | **Decomp cell:** `TR-k-1` (`decompositions/NFRA_TRNSPT_DECOMP.md`) |
**outcome_ref:** FWD-7, FWD-10 | **depends_on:** TR-w-1 (drained; `silver.py` and its columns on your branch)

---

## WORKER FACE

### THE CELL

`TR-k-1`, communications item 4 (PRD section 3): "Gold first run on the C-GOLD-FIELDS schema and its contract file." Andrew-direct:
"Gold is when we first run Alyssa's schema" and "We can make any adjustments we want to format, Alyssa's format is a suggestion only
for our inspiration." C-GOLD-FIELDS (binding): ONE contract file `org/standards/NFRA_TRNSPT_COMMENTARY_GOLD_CONTRACT.json` (CLAUDE_ANNEX
17c: one Opal shape, one contract file -- READ `docs/doctrine/CLAUDE_ANNEX.md` section 17c for the contract-file form and conform to
it). Fields: `record_id, sent_at, recipient_firm, yc_variant (1/2/3 from models referenced 0/1/2+), models_referenced (alias table
mapped to IRPT comparison_keys), account_type, themes (list of {theme, client_figure, model_figure}), body_text, paragraph_hashes[],
body_hash, pdf_sha256, has_pdf, plus nullable holdings and request_text`. "`approved` is not a field (an external send is
approved); a null is not a schema violation for a field named nullable."

**Build:**
1. `org/standards/NFRA_TRNSPT_COMMENTARY_GOLD_CONTRACT.json`: `{"contract": "NFRA_TRNSPT_COMMENTARY_GOLD", "version": "1.0.0",
   "table": "analysis_commentary", "one_opal_shape": true, "authored_by": "0.9.0_WK_NFRA_TRNSPT~4 (round 1 cell TR-k-1)",
   "source": {...}, "fields": [{"name","type" (parquet/arrow type string),"nullable","derivation","claim"}]}` -- exactly the fourteen
   fields above, `holdings` and `request_text` nullable, `claim` one of `measured|inferred|held|absent` per field (this round:
   `holdings` is `absent` -- no PDF bytes yet; `request_text` `absent`; `sent_at` is `inferred` from `received_at` while
   `sentDateTime` is not returned; `pdf_sha256` `absent` -- attachment bytes ride S12; the rest `measured`). Plus whatever 17c
   requires. Andrew's freeze is a signed file, not this order (ruling 6.7).
2. `data/transcripts/scripts/outlook/gold.py`: `derive(silver_rows, assets) -> gold_rows` per the contract: `yc_variant` from the
   count of distinct `models_referenced` (0 -> 1, 1 -> 2, 2+ -> 3); `models_referenced` by matching aliases from
   `data/transcripts/assets/model_aliases.json` in `body_text` (word-boundary, case-insensitive for multi-word aliases, case-sensitive
   for short tokens like `LT`/`ULT`/`UST`), mapped to `comparison_key`; `account_type` by keyword rules (IRA, Roth, 401(k),
   brokerage, trust, else household); `themes` from heading blocks and the first `X% versus Y%` / `X% vs Y%` / `X versus Y` figure
   pair in the following paragraph; `paragraph_hashes` sha256 per block, `body_hash` sha256 of `body_text`; `has_pdf` from the
   silver `ycharts_pdf`; `pdf_sha256` null this round; `sent_at` = `received_at`. `build(date, *, s3, kms_key_arn, apply) -> key`
   reads the silver parquet for the date, derives, validates every row against the contract (types, nullability), writes ONE
   parquet at `address("outlook","transcripts","gold","analysis_commentary","date=<date>","analysis_commentary.parquet")` with the
   KMS headers. CLI: `python data/transcripts/scripts/outlook/gold.py --date YYYY-MM-DD [--apply]` prints
   `GOLD-COMMENTARY rows=<n> variants={1:a,2:b,3:c} key=<addr>`.
3. Tests `data/transcripts/scripts/tests/test_outlook_gold.py`: synthetic silver rows (inline) -> the variant rule on 0/1/2+ models,
   alias matching (including "Long-Term Portfolio", "LT", "Dividend Income"), account type, themes from a heading and a figure
   pair, hashes, contract conformance (a row with a non-nullable null is REFUSED), parquet schema equal to the contract's
   field list and order, the KMS headers on the fake-S3 put.

### ACCEPTANCE

<criterion id="TR1-k1-AC1" cell_refs="TR-k-1"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_TRNSPT_T/R1_CHECKS/r1_gold_contract_check.py</invocation><expect>GOLD-CONTRACT-OK</expect></criterion>
`TR1-k1-AC1` -- the contract file carries exactly C-GOLD-FIELDS, nullability as ruled, a claim per field, no `approved`.

<criterion id="TR1-k1-AC2" cell_refs="TR-k-1"><invocation>python -m pytest data/transcripts/scripts/tests/test_outlook_gold.py -q -p no:cacheprovider</invocation><expect>passed</expect></criterion>
`TR1-k1-AC2` -- the derivation on synthetic silver, conforming to the contract, refusing a violation.

<expected_criteria>TR1-k1-AC1,TR1-k1-AC2</expected_criteria>

Dry-run at the base 2026-09-30 14:0xZ: AC1 GOLD-CONTRACT-BAD unreadable, AC2 "no tests ran" -- FAIL as expected.

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file.
- **SERVED class, but YOUR order writes nothing to the bucket:** the real gold build is the issuer's run at the drain.
- **No AI anywhere in this cell.** The slicer (TR-q-1) is the next order in your queue and reads gold by the contract's names.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row
  (id `NFRA_TRNSPT-W4-S<k>`), and do not weaken the test to pass.

<paths>
org/standards/NFRA_TRNSPT_COMMENTARY_GOLD_CONTRACT.json
data/transcripts/scripts/outlook/gold.py
data/transcripts/scripts/tests/test_outlook_gold.py
org/missions/D9/NFRA/NFRA_TRNSPT/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_TRNSPT/decompositions/NFRA_TRNSPT_DECOMP.md</decomp_doc> (round 1), cell `TR-k-1`.
<owned_cells>TR-k-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: TR1-k1-AC1, TR1-k1-AC2. Instance at `org/missions/D9/NFRA/NFRA_TRNSPT/deliverables/0.9.0_WK_NFRA_TRNSPT~4/NFRA_TRNSPT.TO-TR-k1.gold-contract-and-derivation.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> TR1-k1-AC1,TR1-k1-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** the field table (name, type, nullable, claim), what 17c required, the variant and alias rules, the check line, the pytest line, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- thread round; the gold Lambda (PRD section 4) is a later release.
comp-iam: RUN -- infra/aws/terraform/transcripts/main.tf read at the cut: 1 KMS key policy with 2 statements and 1 reader principal (arn:aws:iam::313476888478:user/Andrew_Berman, the var.reader_principal_arns default), 1 bucket policy with 2 Deny statements (TLS-only, key-only); BLIND: the live IAM plane outside this root was not scanned (0 of the account's roles read). The issuer's real build runs under that one grantee; this cell adds no principal.
comp-adversary: DECLARED-NOT-APPLICABLE -- thread round.
lane: the <paths> block IS the grant; org/standards/ carries the one contract file C-GOLD-FIELDS names.
</preflight>

Source: PRD v0.1 C-GOLD-FIELDS, S15, ruling 6.7, section 3 communications item 4; decomposition round 1 cell TR-k-1.
