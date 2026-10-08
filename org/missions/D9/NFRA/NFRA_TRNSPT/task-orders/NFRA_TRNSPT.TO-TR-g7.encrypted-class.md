# TO NFRA_TRNSPT.TO-TR-g7 -- the ENCRYPTED_UNVERIFIED class in the mail pull

<to_id>NFRA_TRNSPT.TO-TR-g7</to_id>
<project>NFRA_TRNSPT</project>
<issued_to>0.9.0_WK_NFRA_TRNSPT~1</issued_to>
<issued_by>2.0.0_SA_COO~T2</issued_by>
<issued_date>2026-10-08</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>7</round>
<workstream>communications</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Decomp cell:** `TR-g-7` (`decompositions/NFRA_TRNSPT_DECOMP_R7.md`) |
**outcome_ref:** FWD-7 | **depends_on:** none

---

## WORKER FACE

### THE CELL

`TR-g-7` (CTO round-6 analysis @57d1574255, E2; rulings msgs 1480/1482): "an email that passes the author AND client tests but carries
only an encrypted attachment lands in bronze as `ENCRYPTED_UNVERIFIED`, held out of silver and gold ... (1) a fake-route test: an
author+client email with only an encrypted attachment lands in bronze with that class and `held_out` in silver; an author email failing the
client test does not land; (2) no gold row ever carries the class."

**Why:** the 2026-08-11 feedback emails carried one ~13.5 MB `.asc` attachment typed `application/octet-stream`. The YCharts test
(`data/transcripts/scripts/outlook/criterion.py:153-157`: non-inline `application/pdf` of >= `PDF_MIN_BYTES`, or `BODY_WORDS` at :17)
cannot see inside it, so today such an email is a `near_miss` and nothing of it is kept.

**The code you change (read each first):**
- `criterion.py` -- `classify(message, attachments, authors, client_domains)` at :139 returns the flags (`sender_ok`, `client_recipient`,
  `ycharts_pdf`, `trade_update_excluded`, `near_miss`, `ingest`); `_attachment_list` at :125.
- `pull.py` -- `run()` at :134: with `admitted_only` it skips any candidate whose `cls["ingest"]` is false.
- `land_bronze.py` -- writes the message, its attachment list and a sidecar recording the flags (see :120-130).
- `silver.py` -- `ingest_of(sidecar)` at :138 decides which bronze messages become rows; `to_row` at :143 sets `held_out` (:167).
- `gold.py` -- `build` at :285 builds gold from silver.

**Build (the class semantics are ruled; do not widen them):**
1. `criterion.py`: an attachment is ENCRYPTED when it is non-inline AND (its name ends, case-insensitive, with `.asc`, `.pgp`, `.gpg` or
   `.p7m`, OR its `contentType` is `application/pgp-encrypted`, `application/pkcs7-mime` or `application/x-pkcs7-mime`).
   `encrypted_only` = at least one non-inline attachment AND every non-inline attachment is ENCRYPTED. Add to `classify`'s result
   `"encrypted_only"` and `"admission_class"`: `"FEEDBACK"` when `ingest` is true; `"ENCRYPTED_UNVERIFIED"` when `sender_ok AND
   client_recipient AND encrypted_only AND NOT trade_update_excluded` (and `ingest` false); otherwise `None`. Do NOT change `ingest`'s
   existing meaning.
2. `pull.py`: with `admitted_only`, ALSO land a candidate whose `admission_class` is `"ENCRYPTED_UNVERIFIED"` (no PDF fetch for it: its
   attachment is not a PDF); count it in a new run-record field `encrypted_unverified`. Everything else unchanged.
3. `land_bronze.py`: record `admission_class` and `encrypted_only` in the sidecar.
4. `silver.py`: a bronze message whose sidecar `admission_class` is `"ENCRYPTED_UNVERIFIED"` becomes a silver row with `held_out` TRUE
   and its class recorded in a new column `admission_class` (schema updated); FEEDBACK rows are unchanged.
5. `gold.py`: gold never emits a row whose `admission_class` is `"ENCRYPTED_UNVERIFIED"` (filter at the source rows).
6. `data/transcripts/scripts/tests/test_encrypted_class.py` (new), using the existing test patterns (the replay / stub-client and fake s3
   fixtures in `test_outlook_bronze.py`, `test_outlook_silver.py`, `test_outlook_gold.py`, `test_gateway_mail.py`). It must hold, by name:
   - `test_encrypted_author_client_lands_class_held_out` -- an author sender, a client-domain recipient, ONE non-inline `.asc`
     `application/octet-stream` attachment: `pull.run(..., admitted_only=True)` lands it in bronze with sidecar `admission_class ==
     "ENCRYPTED_UNVERIFIED"`, and its silver row has `held_out` TRUE;
   - `test_encrypted_author_nonclient_not_landed` -- the same email to a non-client domain: nothing lands;
   - `test_no_gold_row_carries_class` -- gold built over silver holding one ENCRYPTED_UNVERIFIED row and one FEEDBACK row emits no row
     with that class.
   Use synthetic addresses only (e.g. `author@example-firm.test`); never a real address.

### ACCEPTANCE

<criterion id="TR7-g7-AC1" cell_refs="TR-g-7"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_TRNSPT_T2/R7_CHECKS/r7_checks.py g7-class</invocation><expect>R7-G7-CLASS-OK</expect></criterion>
`TR7-g7-AC1` -- the author+client encrypted-only email lands with the class and is held out in silver; the non-client one does not land.

<criterion id="TR7-g7-AC2" cell_refs="TR-g-7"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_TRNSPT_T2/R7_CHECKS/r7_checks.py g7-gold</invocation><expect>R7-G7-GOLD-OK</expect></criterion>
`TR7-g7-AC2` -- no gold row carries the class.

<expected_criteria>TR7-g7-AC1, TR7-g7-AC2</expected_criteria>

Dry-run at the base (CLOUD 4839b6f2d2): AC1 and AC2 `FAIL absent` -- FAIL as expected. The full outlook test suite is the issuer's drain
check: keep `test_outlook_*.py`, `test_mail_*.py` and `test_gateway_mail.py` green (`python -m pytest data/transcripts/scripts/tests -q
-p no:cacheprovider -k "outlook or mail or encrypted"`).

### AMENDMENT 1 (issuer 2.0.0_SA_COO~T2, 2026-10-08) -- reopened for the silver test pin (row NFRA_TRNSPT-D2-W1-S1)

The ruled `admission_class` silver column makes the row 20 columns; `data/transcripts/scripts/tests/test_outlook_silver.py` pins 19
(`test_row_columns_and_types`, `test_the_wipes_limits_travel_inside_the_parquet`). That file is now in your grant. Update exactly those
two expectations (add `admission_class` to the expected column set; 19 -> 20) and nothing else in it. Then run
`python -m pytest data/transcripts/scripts/tests -q -p no:cacheprovider -k "outlook or mail or encrypted" --ignore=data/transcripts/scripts/tests/test_eod_voice.py`
(the ignore is an unrelated collection error), which must read 0 failed; re-run AC1 and AC2; update the instance; flip to complete only
then. The issuer ACCEPTS the `landed_dates` addition in `pull.run` (an ENCRYPTED_UNVERIFIED landing builds its silver partition).

## BOUNDS

- **Grant.** The six files above, this order's file, your deliverables folder and the investigation file. Nothing else.
- **LOCAL.** No gateway, Graph, HTTP or AWS call; no deploy; fakes and stubs only. Do not edit another order's proof instance.
- **Refusal clause.** If a ruled semantic cannot be met without changing `ingest`'s meaning or an existing test's expectation, stop on
  that criterion and file a surprise row (id `NFRA_TRNSPT-D2-W1-S<k>`, next unused across every document under `surprise-channel/`).

<paths>
data/transcripts/scripts/outlook/criterion.py
data/transcripts/scripts/outlook/pull.py
data/transcripts/scripts/outlook/land_bronze.py
data/transcripts/scripts/outlook/silver.py
data/transcripts/scripts/outlook/gold.py
data/transcripts/scripts/tests/test_encrypted_class.py
data/transcripts/scripts/tests/test_outlook_silver.py
org/missions/D9/NFRA/NFRA_TRNSPT/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant (your deliverables folder is granted by the tree convention). Everything else named here you READ.

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_TRNSPT/decompositions/NFRA_TRNSPT_DECOMP_R7.md</decomp_doc> (round 7), cell `TR-g-7`.
<owned_cells>TR-g-7</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: TR7-g7-AC1, TR7-g7-AC2. Instance at `org/missions/D9/NFRA/NFRA_TRNSPT/deliverables/0.9.0_WK_NFRA_TRNSPT~1/NFRA_TRNSPT.TO-TR-g7.encrypted-class.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> TR7-g7-AC1,TR7-g7-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** the class rule as built (one line), the three test names, the two check lines, the outlook/mail suite line, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- code and tests only; the served Lambda is not redeployed this round.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call.
comp-adversary: RUN -- 5 outlook modules and 4 existing test files read for the seams (criterion :125-173, pull :134-190, silver :138-167, gold :285); BLIND to the served Lambda bundle (not redeployed here). Traps: widening ingest's meaning (the face forbids it), a real address in a fixture, and gold leaking the class.
lane: five outlook modules, one new test, the investigation file.
</preflight>

Source: CTO round-6 analysis @57d1574255 E2; rulings msgs 1480/1482; decomposition round 7 cell TR-g-7 and issuer rulings 2-3.
