# TO IRPT_DASHBD.TO-DB-b-114 -- the rule-24 record for the return_basis and method_version values Cottonwood's positions-based returns state -- four postulates, a word-boundary token census, ONE conclusion naming the two stamp values; the record decides whether a new value is needed and lands none

<to_id>IRPT_DASHBD.TO-DB-b-114</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~89</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>58</round>
<workstream>B</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** 1.0.0_SA_CTO~DELL2's ADVI_COTBKF round-54 analysis @0ac41554df (section 3 row D2-W66-S1, section 4 item 3), asked by 2.0.0_SA_COO~C2 (msg 4000) | **Decomp cell:** `DB-b-114` (decomposition section 60) | **outcome_ref:** FWD-11 | **depends_on:** DB-b-102 (drained).

---

## WORKER FACE

Your worktree is `C:/dev/wk-irpt-dashbd-89`; run everything from its root. Your folder is
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~89/`.

**THE CLIENT-DATA RULE (binding):** never print an account number or a client figure in a commit message, a record, a row or a report.

**The cell (`DB-b-114`).** ADVI_COTBKF computed 107,316 measured Cottonwood return rows by a method that differs from the custodian one: the account
value is REBUILT from positions at the as-traded close, net of fees. Its row `ADVI_COTBKF-D2-W66-S1` (2026-10-09) says the producer's closed
vocabularies hold no value that states this truthfully, so those rows carry `return_basis` NULL and `method_version` NULL. The CTO ruled that the
vocabulary is IRPT_DASHBD's, and that under CLAUDE.md rule 24 a value proposal arrives with its four-postulate record and a word-boundary token
census, or it is not a proposal.

The producer moved AFTER that row was written. Read these in `C:/dev/wk-irpt-dashbd-89` first:
- the row: `org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md`, heading `## ADVI_COTBKF-D2-W66-S1`;
- the ruling: `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_ADVI_COTBKF_ROUND_54_20261011.md` sections 3 and 4;
- the producer: `data/assets/scripts/gold/irpt_reporting/account_return_daily.py` -- `METHOD_ROWS` (rows 2 and 3, added by DB-b-102), the comment block
  `THE CLOSED VOCABULARIES`, `RETURN_BASIS`, `method_version_of`, `build_manifest`;
- `data/assets/scripts/gold/irpt_reporting/sources.json`, the entry `_commonwealth_delivery` (it declares `method_version` 3);
- the earlier rule-24 record `METHOD_ROW_RULE24.md` in `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~77/`;
- the contract file under `org/standards/` that declares `return_basis` (find it with `comp-find`), and how ADVI_COTBKF's adapter computes its
  daily return (find the adapter from the row's grounding).

Write `COTTONWOOD_VALUE_RULE24.json` and a one-page `COTTONWOOD_VALUE_RULE24.md` beside it:
1. **The question, stated on the axes as the producer defines them.** `return_basis` answers "which arithmetic produced total_return_daily".
   `method_version` names the `dim_return_method` row, which carries the valuation source. Say which axis each part of Cottonwood's difference
   (valuation rebuilt from positions; as-traded close; net of fees) belongs to, with file and line.
2. **`postulates`** {mece, same_grain, intent_coherence, state_coherence}: each {finding, evidence: [{file, line}]}.
   - MECE by SUBTRACTION from a printed denominator: list every way a row's return is produced across the producer and the Cottonwood adapter, then
     subtract what each existing member covers. Say what is left.
   - State coherence: name which values one remedy does NOT move.
3. **`candidates`**: every value name you considered adding, or an empty list. **`token_census`** {files_scanned, scope, tokens: {<token>:
   {hits, files}}}: a word-boundary census over the repo (`comp-find`, `-i` for a token census; never a blind recursive grep, never `head`) of every
   current `RETURN_BASIS` member, every candidate, and `method_version`. Print the denominator.
4. **`conclusion`**, exactly one of: `EXISTING_VALUES_SUFFICE` (the rows can be stamped truthfully with values the producer admits at HEAD),
   `NEW_RETURN_BASIS_VALUE`, `NEW_METHOD_ROW`, `BOTH_NEW`. **`stamp`** {return_basis, method_version}: the two values the 107,316 rows carry.
   **`reasoning`**: the argument, including the strongest case AGAINST your conclusion.
5. **`manifest_text`**: does `build_manifest` at HEAD still write custodian-method text or `method_version` 2 for an entry that declares row 3? Answer
   from the code with file and line, and say what ADVI_COTBKF's mint must pass for the manifest to state row 3.
6. **`if_new`**: when the conclusion is not `EXISTING_VALUES_SUFFICE`, the exact value name, every file that must change (producer, contract file,
   readers), and the remedy that moves it. You do NOT make those edits.

Do not decide by preference. If the existing members state the method truthfully, say so; if they do not, say which postulate fails without a new one.

<criterion id="DB58-1-AC1" cell_refs="DB-b-114"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r58/p58_round58.py" . DB58-1-AC1</invocation><expect>DB58-1-AC1 PASS</expect></criterion>
`DB58-1-AC1` -- the record answers the four postulates with file-and-line evidence, carries the token census with its denominator, and states one conclusion and the two stamp values. Base: FAIL.

<expected_criteria>DB58-1-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited.
- **Served output does not move.** No edit under `data/`, `infra/`, `portal/` or `org/standards/`.
- **AWS:** none. NO Black Diamond or vendor call, no secret read, no S3 read or write, no deploy, no bun, no download of any package, script or program.
- **Refusal clause.** A vendor call, a secret read, an S3 write, a deploy, an edit outside the grant, a filled figure, or an account
  number, name or balance in a committed `.md` is a defect: stop and file a row.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~89/
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~89/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-114.cottonwood-value-rule24.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 60 (round 58), cell `DB-b-114`.
<owned_cells>DB-b-114</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB58-1-AC1. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~89/IRPT_DASHBD.TO-DB-b-114.cottonwood-value-rule24.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB58-1-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT:** commit hashes, the criterion's last line, the conclusion, the two stamp values, each postulate's finding in one line, the census denominator, the manifest answer, and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: a record only; no producer, contract or infra edit.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no AWS call.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- DB58-1-AC1 FAIL at base (no record). CTO analysis @0ac41554df section 3; row ADVI_COTBKF-D2-W66-S1.
lane: the <paths> block IS the grant.
</preflight>
