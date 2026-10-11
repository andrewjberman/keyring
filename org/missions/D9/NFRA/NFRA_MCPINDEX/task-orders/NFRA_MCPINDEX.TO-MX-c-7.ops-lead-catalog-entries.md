# NFRA_MCPINDEX task order -- `MX-c-7` -- the catalog's one writer adds the operations lead's six needs (E-30..E-35), two from the readers' census and four GAP, unowned; and corrects Alyssa's retire tags, phrasings and E-13 guidance (round-8 analysis E2)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_MCPINDEX/decompositions/NFRA_MCPINDEX_DECOMP.md</decomp_doc>
<owned_cells>MX-c-7</owned_cells>
</decomp_ref>
<to_id>NFRA_MCPINDEX.TO-MX-c-7</to_id>
<issued_to>0.9.0_WK_NFRA_MCPINDEX~30</issued_to>
<issued_by>2.0.0_SA_COO~MI</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule.
comp-iam: DECLARED-NOT-APPLICABLE -- catalog source files and the regenerated catalog only; no role, grant or tool change.
comp-adversary: DECLARED-NOT-APPLICABLE -- the MX-c-6 pattern; the battery dry-run is the control (c7.AC1 0 of 6, c7.AC2 0 of 8 at base).
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `MX-c-7` (round 9; PRD v0.8 @0eff9e0e6d FWD-19, contract 4; decomposition section ROUND 9)

**Start only when MX-o-1 (your own previous order), MX-o-2 (worker ~31) AND MX-x-6 (worker ~32) are complete and
drained.** MX-x-6 changes the emitter you run. Merge `box/sitez` into your branch first. Both censuses are then at
`org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~30/census_trade_rec.json` and
`.../0.9.0_WK_NFRA_MCPINDEX~31/census_billing.json`. A SERVED reader's tool name is the `TOOL` constant in
`infra/aws/ec2/opal-gateway/app/integrations/ops_trade_rec/integration.py` (or `ops_billing/`).

**What the user sees at the base.** The catalog's `needs:` list holds E-1..E-29, Alyssa's needs. None of the
operations lead's six items is there, so discover answers each with NOT_CATALOGUED.

**The act.** Add six need source files, `workflows/atom_decomposition/catalog_entries/need_E-30.yaml` ..
`need_E-35.yaml`, in the exact shape of the existing `need_E-*.yaml` files. Then regenerate
`infra/aws/ec2/opal-gateway/app/refs/DATA_CATALOG.yaml` through the ONE emitter (`emit_catalog_v02.py`, C1):

| id | need | status / tool / owner |
|---|---|---|
| E-30 | trade reconciliation: Opal's trade status against the custodian's | census SERVED: `SERVED`, the reader's `TOOL`, its owner. Census GAP: `GAP`, tool null, owner = the census owner |
| E-31 | billing: AUM, fee rate, fee and paid status per account and period | the same rule from the billing census |
| E-32 | post model update rec | `GAP`, tool null, owner `unowned` |
| E-33 | high cash account alert FA | `GAP`, tool null, owner `unowned` |
| E-34 | assets transfer alert FA | `GAP`, tool null, owner `unowned` |
| E-35 | restricted account alert FA | `GAP`, tool null, owner `unowned` |

- Every entry is `op_class: read`. None retires one of Alyssa's C1-C8 / W1-W6, so each carries a `retires_none` reason
  naming the operations lead.
- E-33..E-35 are under the standing alert moratorium (contract 4): catalogued, never built.
- Each entry's `example_questions` carries the operations lead's own phrasing, so discover's own-text rule reaches it
  first: "trade reconciliation" and "did the custodian settle our trades" (E-30); "billing" and "which households have
  unpaid fees" (E-31); the item names for E-32..E-35.
- **Emitter input (row Z-W29-S1; fixed by MX-x-6):** run the emitter from YOUR worktree with no `--census-dir`. Its
  default is this checkout's own census, and MX-x-6 makes it refuse a foreign one. The regenerated catalog then
  differs from base only in `needs:` and the built-by stamp. Print that diff summary in your report.

**E2 -- Alyssa's entries, corrected (`ledger/ROUND_ANALYSIS.round8.md` @d2eb6c471b, section 4 E2 and ruling 2a).**
Measured at the issuance base, from the served catalog: FWD-18 reads 4 of 14 (C1, C2, W5, W6). That is one too many:
E-25 claims C1, the YCharts report, which is GAP. And no entry carries C3, although E-4, E-5 and E-9 are its needs.
In the same one-writer pass:
1. `need_E-25.yaml`: drop `C1` from `retires`.
2. `need_E-4.yaml`, `need_E-5.yaml`, `need_E-9.yaml`: add `C3` to `retires`. All three are GAP, so FWD-18 then reads
   3 of 14 (C2, W5, W6) with C3 carried.
3. Her two phrasings move into catalog text, and the folds retire. Add "statement" to `need_E-9.yaml`'s
   `example_questions`, and "S&P YTD" to `need_E-19.yaml`'s. Then, in
   `infra/aws/ec2/opal-gateway/app/integrations/opal_discover/integration.py`, remove the two need-local word folds
   MX-d-8 added (`_YTD` and `_AMP_WORD`, used in `_need_words` and `_need_head`, docstring `:61`). Without them,
   "S&P YTD" has the single content word `ytd`. If an ask then reaches no need, you may add ONE general rule: an ask
   whose content words equal one of a need's `example_questions`' content words names that need. Never a
   word-specific mapping. Keep `test_own_text_rule_does_not_catalogue_chatter` passing ("How's it going?" and "fees"
   stay uncatalogued).
4. E-13's unknown-model guidance (ruling 2a: discover routes, the answer asks). E-13's entry must carry this
   guidance: when the asked model is not one of the five served models (UST, ST, INT, LT, ULT), the answer lists
   those five and asks which one, and never gives a figure for the unnamed model. Put it in `need_E-13.yaml`'s `note`.
   If discover's match for E-13 does not carry the note, surface the need's `note` in the match, which is a
   discover change inside this cell. Claude reads the match; no tool code changes.

## 2. BOUNDS

1. You change only the files in `<paths>`:
   - `need_E-3[0-5].yaml` (new), and `need_E-4`, `E-5`, `E-9`, `E-13`, `E-19`, `E-25.yaml` (E2);
   - the regenerated `DATA_CATALOG.yaml`;
   - `workflows/atom_decomposition/tests/`;
   - `opal_discover/integration.py` and `tests/test_opal_discover.py`, for E2 items 3 and 4 only.
   An ops-lead phrasing that does not route first with words alone is a BLOCKING row naming the ask and its first
   match. It is never another discover edit.
2. No tool, grant, route or `.env` change. No deploy (MX-r-10). No push.
3. REFUSE a criterion you cannot meet as written, and report it with its measurement.

## 3. SURFACES

<paths>
workflows/atom_decomposition/catalog_entries/
workflows/atom_decomposition/tests/
infra/aws/ec2/opal-gateway/app/refs/DATA_CATALOG.yaml
infra/aws/ec2/opal-gateway/app/integrations/opal_discover/integration.py
infra/aws/ec2/opal-gateway/tests/test_opal_discover.py
org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~30/**
org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Rows go to `org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/INVESTIGATION_v1.md`:
- id `NFRA_MCPINDEX-Z-W30-S<k>`; re-read the file for the next free k at commit time;
- fabric `site-z`;
- `disarm_owner` `2.0.0_SA_COO~MI`;
- `surfaced_at` written as a full UTC timestamp, never a placeholder.

## 4. PROOF OF SPEC (literal; run from your worktree root)

<proof_of_spec>
  <expected_criteria>AC1,AC2,AC3</expected_criteria>
  <criterion id="AC1" cell_refs="MX-c-7" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round9/checks/c7.AC1.sh; echo "exit=$?"</invocation><expect>ops lead entries present 6 of 6; earlier entries kept 29 of 29; duplicates 0; violations 0 -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="MX-c-7" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round9/checks/c7.AC2.sh; echo "exit=$?"</invocation><expect>ops lead asks routed 10 of 10 on the first try (the 8 ops-lead asks plus "statement" -> E-9 and "S&P YTD" -> E-19) -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="MX-c-7" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round9/checks/c7.AC3.sh; echo "exit=$?"</invocation><expect>FWD18 served 3 of 14 (C2 W5 W6); C3 carried 3 of 3; E25 claims C1 False; FOLDS references 0; GUIDE first=E-13 with 5 of 5 model codes; E2 catalog checks held 5 of 5 -- RESULT: PASS -- exit=0</expect></criterion>
  <instance_path>org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~30/NFRA_MCPINDEX.TO-MX-c-7.ops-lead-catalog-entries.proof_of_spec.json</instance_path>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the proof instance at the `<instance_path>`, then flip `<status>` to complete and commit the instance,
deliverables and flip together. Report once, naming each entry's status and tool, the catalog diff summary, and each
ask's first match. After this order the issuer continues you with MX-r-10's PHASE A.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES (2.0.0_SA_COO~MI).** Round 9 join of the two reader chains, worker ~30 after MX-o-1. STAGED UNISSUED
2026-10-09 ~10:2xZ (1.0.0_SA_CTO~Z @ff362e8444). Battery dry-run at base 1dd356991a (`round9/checks/`):
- c7.AC1 FAIL as expected: 0 of 6 present, 29 of 29 kept, 12 violations.
- c7.AC2 FAIL as expected: 0 of 8, all NOT_CATALOGUED.

ISSUED 2026-10-10 ~23:4xZ in round 9's ONE issuance, from `ledger/ROUND_ANALYSIS.round8.md` @d2eb6c471b. Battery re-dry-run at issuance base bf8492f48f: every check of this order FAILS there as a build check must.

<status>complete</status>
<round>9</round>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
