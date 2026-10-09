# TO ADVI_COTBKF.TO-CB-aq-1.cottonwood-sources-entry -- round 43 CB-aq-1: Cottonwood's channel entry, TWR rows, local rebuild

<to_id>ADVI_COTBKF.TO-CB-aq-1</to_id>
<project>ADVI_COTBKF</project>
<issued_to>0.9.0_WK_ADVI_COTBKF~70</issued_to>
<issued_by>2.0.0_SA_COO~C2</issued_by>
<issued_date>2026-10-09</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>43</round>
<workstream>~C2</workstream>

**Directive:** D8 | **Fabric:** laptop (placement DELL2) | **Decomp cell:** `CB-aq-1` (`decompositions/ADVI_COTBKF_DECOMP.round43.md`) |
**outcome_ref:** FWD-3 | **depends_on:** none

---

## WORKER FACE

### THE CELL

ADVI_COTBKF's adapter `data/assets/scripts/silver/commonwealth_account_return_daily.py` (round 38, CB-al-1) builds Cottonwood's
`account_return_daily` days locally through the table's one producer, `data/assets/scripts/gold/irpt_reporting/account_return_daily.py`.
- It writes 3,325 days and 1,691,729 rows under `.scratch/advi_cotbkf/ard_cottonwood/`.
- `return_basis` is NULL on measured rows, because no admitted value then stated the method (row D2-W66-S1).

IRPT_DASHBD has since changed its producer (TO-DB-b-96, drained @ce9f482be0; CTO IRPT_DASHBD ADDENDUM 13.1):
- the manifest reads `valuation_source`, `fee_treatment` and `price_basis` from the source's entry in
  `data/assets/scripts/gold/irpt_reporting/sources.json`;
- a source without them writes `absent`;
- `return_basis` stays `TWR` / `NOT_MEASURABLE`, with no enum edit.

`sources.json` has no Cottonwood channel. Its own doc says a new firm channel is a new entry, never a code branch. No firm token
appears in the file: an entry resolves its firm through `lookup(registry_key)`.

**Your item.** No S3 write and no deploy.

1. **Add ONE entry to `sources.json` for Cottonwood's channel.**
   - Key it by its custody source (the Commonwealth delivery), with no firm token.
   - `registry_key` resolves to the Cottonwood scope via `lookup()`.
   - Method fields: `valuation_source=positions_x_as_traded_close`, `fee_treatment=net_of_fees`, `price_basis=as_traded`. Check each
     against the vocabularies the producer admits for these fields (IRPT_DASHBD's record:
     `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~71/SOURCES_FIELDS.json`). A value it does not admit is a
     BLOCKING row; do not invent a value.
   - Add only what the manifest needs. Mark the entry so the producer's custodian compute path does not treat it as a channel to
     compute, using whatever structural switch the producer already honours. If none exists, STOP and file a BLOCKING row. Do not edit
     the producer.
2. **Prove the producer is safe with the entry present.**
   - Run IRPT_DASHBD's producer tests (`data/assets/scripts/gold/irpt_reporting/tests/`) and the reporting-gold handler's tests, if
     present. All must stay green.
   - Show that `declared_sources()` and the scheduled handler path do not try to compute the Cottonwood entry.
3. **Re-point the adapter.**
   - `return_basis = "TWR"` on measured rows, and `NOT_MEASURABLE` on blank ones.
   - `emit_day(upload=False)` is called with the Cottonwood source, so the manifest carries the entry's three method fields.
   - Rebuild all days locally into `.scratch/advi_cotbkf/ard_cottonwood_r43/`, with a manifest of each file's sha256.
   - Read one built manifest back, and print its `valuation_source`, `fee_treatment` and `price_basis` (none may be `absent`) and its
     method fields.
4. **Rule first.** Commit the entry and the adapter change in its OWN commit before the first rebuild run.

Write `cottonwood_sources_entry.md`. LAST line exactly:
`ARD-COTTONWOOD-R43 days=<n> rows=<r> return_basis_twr=<m> manifest_fields_absent=<0|n> producer_tests=<passed>`.

### ACCEPTANCE

<criterion id="CB43aq1-AC1" cell_refs="CB-aq-1"><invocation>python data/assets/scripts/silver/commonwealth_account_return_daily.py --out org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~70</invocation><expect>ARD-COTTONWOOD</expect></criterion>
`CB43aq1-AC1` -- the rebuild runs through the Cottonwood entry, and the R43 line prints `manifest_fields_absent=0`.

<criterion id="CB43aq1-AC2" cell_refs="CB-aq-1" judgment="true"/>
`CB43aq1-AC2` -- JUDGMENT, graded by 3.0.0_SA_CVO at L9 and never self-graded:
- one entry added, no firm token, values admitted;
- the producer's compute path is proven not to pick it up;
- IRPT_DASHBD's tests are green.

<expected_criteria>CB43aq1-AC1,CB43aq1-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below, plus your deliverables folder and this order's file. Built files go under `.scratch/`,
  uncommitted.
- **In `sources.json`, the edit is ONE added entry.** No existing entry or key changes. The producer `account_return_daily.py` and the
  handler are never edited.
- **No S3 write and no deploy.** Reads are limited to the served FWD-3 tables. Never read or list `opal-data-bd`,
  `opal-data-49financial`, `opal-data-inf`, `opal-data-inflection` or `opal-data-demo`.
- **Refusal clause.** If the criterion cannot be met as written, stop. Write the reason in your report and a NEW surprise row (id
  `ADVI_COTBKF-D2-W70-S<k>`, `"fabric": "dell2"`). Do not weaken the test.

<paths>
data/assets/scripts/gold/irpt_reporting/sources.json
data/assets/scripts/silver/commonwealth_account_return_daily.py
org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_COTBKF/decompositions/ADVI_COTBKF_DECOMP.round43.md</decomp_doc> (round 43), cell `CB-aq-1`.
<owned_cells>CB-aq-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CB43aq1-AC1, CB43aq1-AC2. Instance at
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~70/ADVI_COTBKF.TO-CB-aq-1.cottonwood-sources-entry.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> CB43aq1-AC1,CB43aq1-AC2` BEFORE the flip. Mechanical: CB43aq1-AC1. A
judgment criterion is recorded as PENDING-ADJUDICATION, never PASS.
</proof_of_spec>

**REPORT:**
- the ARD-COTTONWOOD-R43 line;
- the entry as added;
- how the compute path skips it;
- the producer and handler test lines;
- one manifest's method fields;
- commits, with the rule commit first.

---

## RECORD FACE

<preflight>
comp-schedule: RUN -- 1 scheduled consumer of sources.json named (the reporting-gold Lambda, infra/aws/lambda/investor-reporting/reporting-gold/handler.py, packaging sources.json by staged_from pins); BLIND: any other scheduled reader of sources.json outside that handler and the producer -- the cell names it if found; a repo edit reaches no deployed Lambda until IRPT_DASHBD redeploys.
comp-iam: DECLARED-NOT-APPLICABLE no AWS write.
comp-adversary: RUN -- one entry only, through the declared extension point; values admitted or BLOCKING; the compute path proven to skip it; IRPT_DASHBD's tests green; BLIND: an IRPT_DASHBD consumer that iterates sources.json outside the producer (named in the report if found).
lane: the <paths> block IS the grant (worker RULING 1); sources.json is IRPT_DASHBD's file, and the one-entry add is its declared extension point (~D2 msg 3452).
</preflight>

Source: CTO IRPT_DASHBD ADDENDUM 13.1 @49293e07e9 (msg 3414); `2.0.0_SA_COO~D2` msg 3452 (TO-DB-b-96 @ce9f482be0); row D2-W66-S1.
