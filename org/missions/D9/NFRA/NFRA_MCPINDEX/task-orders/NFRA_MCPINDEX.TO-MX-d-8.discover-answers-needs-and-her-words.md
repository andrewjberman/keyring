# NFRA_MCPINDEX task order -- `MX-d-8` -- discover reads the catalog's `needs:`, answers a GAP entry with its owner and a write entry with the caller's grant, and Alyssa's own words route on the first try

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_MCPINDEX/decompositions/NFRA_MCPINDEX_DECOMP.md</decomp_doc>
<owned_cells>MX-d-8</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_MCPINDEX~28</issued_to>
<issued_by>2.0.0_SA_COO~MI</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule.
comp-iam: DECLARED-NOT-APPLICABLE -- discover reads the catalog and the caller's existing grant decision; no role, policy or grant changes.
comp-adversary: DECLARED-NOT-APPLICABLE -- the MX-d-5/d-6 discover pattern; the battery dry-run is the control (d8.AC1 reads 0 of 9 at base).
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `MX-d-8` (round 8; PRD v0.7 @b06af7c0d2 FWD-14, FWD-17, contract 1; decomposition section ROUND 8)

**Start only when MX-d-7 (your own previous order) AND MX-c-6 (worker ~29) are complete and drained.**
- Merge `CLOUD` into your branch first. MX-c-6 adds the catalog's `needs:` section (29 entries E-1..E-29, from need
  source files under `workflows/atom_decomposition/catalog_entries/need_*.yaml`).
- Each entry carries `id`, `need`, `source`, `status`, `tool`, `owner`, `retires`, `op_class`, `example_questions`, and
  for E-19 `live_error`.
- The issuer continues you with this order when both have drained.

**What the user sees at the base.** Alyssa's phrasings land as "not catalogued", or on a dataset whose meaning is a
different need:
- "cost basis", "statement", "stress test" and "download the attachment" answer "not catalogued".
- "account counts by partner" lands on a row whose own meaning names account counts only in passing (brief Part VI.3).
- "save an attachment", "move mail" and "send a Teams message" are not catalogued at all.
- PRD v0.7 FWD-17: discover must answer each with "the entry, its read or write class, and whether the caller's grant
  allows it". ACCEPT: "a write tool is never implied to be available when the grant refuses it."

**The act:**
1. **Discover reads `needs:`.** A need entry is reached by its own text (`need`, `example_questions`), by the same
   own-text rule `silver_datasets` rows use (MX-d-6, `_own_text_hit`). It answers as a match carrying:
   ```
   need: {id, status, op_class, owner, tool, also_tools, retires, live_error?, grant}
   ```
   - For a SERVED need whose tool reads a catalogued dataset, the match also names that tool as `next_tool`.
   - Rank so that a need entry whose own text the ask names comes first, before a channel artifact selected by a
     looser keyword. Measure; do not guess.
2. **GAP entries (contract 1).** A GAP need answers with its `owner` (a project or `unowned`) and NO `next_tool`.
   FWD-1's "not catalogued ... names nothing" now applies only to a subject absent from every entry.
3. **Write entries and the CALLER's grant (FWD-17).** For an `op_class: write` need, `grant` is
   `{allowed: true|false, reason}`. It is decided by the gateway's EXISTING per-principal decision for that tool,
   `app/data_entitlement.py`'s `tool_denial(name, principal)` / `visible_tools`, called with the caller's resolved
   principal; never a second rule.
   - A write tool is never shown as available when that decision refuses it.
   - A need with tool null answers `allowed: false` with the reason "no tool".
4. **The routing harness** (`infra/aws/ec2/opal-gateway/tests/routing/`). Add 9 questions, each quoted from PRD v0.7
   (`source: org/missions/D9/NFRA/NFRA_MCPINDEX/prd/NFRA_MCPINDEX_PRD.md:<line>`), asker "Alyssa Keith (her two briefs,
   via PRD v0.7)":
   - Q28 "account counts by partner" -> E-16
   - Q29 "cost basis" -> E-4
   - Q30 "statement" -> E-9
   - Q31 "stress test" -> E-20
   - Q32 "download the attachment" -> E-21
   - Q33 "S&P YTD" -> E-19
   - Q34 "save an attachment" -> E-21
   - Q35 "move mail" -> E-23
   - Q36 "send a Teams message" -> E-24

   Extend `run_routing.py` so `expected_tool: NEED:<id>` is a HIT when the FIRST match is that need entry. Keep its
   `--plant-mislabel` control working.
5. **Tests**: the three named in d8.AC2, in `tests/test_opal_discover.py`. Every existing test in that file still
   passes.

## 2. BOUNDS

1. You change `app/integrations/opal_discover/`, `tests/test_opal_discover.py` and `tests/routing/` only. The catalog
   is MX-c-6's: if an entry's words or status must change for a route to hold, that is a BLOCKING row naming the entry,
   never your edit.
2. No change to `data_entitlement.py`, any role, grant, tool or route. You CALL its decision; you never change it.
3. Nothing under `data/cot/`. No push. No deploy (MX-r-9 releases this). REFUSE a criterion you cannot meet as written,
   and report it with its measurement.

## 3. SURFACES

<paths>
infra/aws/ec2/opal-gateway/app/integrations/opal_discover/integration.py
infra/aws/ec2/opal-gateway/tests/test_opal_discover.py
infra/aws/ec2/opal-gateway/tests/routing/questions.yaml
infra/aws/ec2/opal-gateway/tests/routing/run_routing.py
org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~28/**
org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Rows go to `org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/INVESTIGATION_v1.md`:
- id `NFRA_MCPINDEX-Z-W28-S<k>`; re-read the file for the next free k at commit time;
- fabric `site-z`;
- `disarm_owner` `2.0.0_SA_COO~MI`;
- `surfaced_at` written as a full UTC timestamp, never a placeholder.

## 4. PROOF OF SPEC (literal; run from your worktree root)

<proof_of_spec>
  <expected_criteria>AC1,AC2</expected_criteria>
  <criterion id="AC1" cell_refs="MX-d-8" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round8/checks/d8.AC1.sh; echo "exit=$?"</invocation><expect>her phrasings + write asks: present 9 of 9, routed 9 of 9 on the first try; original asks routed n of 27 with n >= 24 -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="MX-d-8" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round8/checks/d8.AC2.sh; echo "exit=$?"</invocation><expect>pytest rc=0; named tests passed 3 of 3; failed/error tests 0 -- RESULT: PASS -- exit=0</expect></criterion>
  <instance_path>org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~28/NFRA_MCPINDEX.TO-MX-d-8.discover-answers-needs-and-her-words.proof_of_spec.json</instance_path>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the proof instance at the `<instance_path>`. Report once, in your final message, naming:
- where each of the 9 asks landed at your start and at your end;
- the ranking change and its measured effect on the original 27.
Do not edit this task order beyond your status flip. After this order, the issuer continues you with MX-r-9.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES (2.0.0_SA_COO~MI).** Round-8 join of the two chains, worker ~28 after MX-d-7. Battery dry-run at base
ac135370d2 (`round8/checks/`):
- d8.AC1 FAIL as expected: present 0 of 9, routed 0 of 9; the original 27 at 24, so the floor held.
- d8.AC2 FAIL as expected: named tests passed 0 of 3.

<status>issued</status>
<round>8</round>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
