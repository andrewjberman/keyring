# AMGT_RESAPP task order -- `AMGT-ww-4` -- THE EXPORT'S WORDS COME FROM ONE SERVED DEFINITION THAT MATCHES THE PAGE'S

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-ww-4</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~171</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no new read or write; the served fields reach the Lambda at ww-1.
comp-adversary: RUN by the issuer at the cut -- AC1 parses the page's own map and runs the page's own formulaInWords in node at check time, so a copy that drifts FAILS; AC2 rebuilds the export from this tree and runs FWD-30's harness, so a change that blinds the harness FAILS.
EGRESS CLASS, declared: NONE beyond read-only invokes of Opal's deployed function (AC2's captures). No vendor, no write.
</preflight>

## 1. THE CELL -- `AMGT-ww-4` (round 48, decomposition s.56)

The page names each Model line in words (`portal/src/pages/SecurityAnalysis/modelSheet.ts` `LINE_NAMES`, 25 entries, e.g.
`PX_LAST: 'Share price (last close)'`, `SALES_REV_TURN: 'Revenue'`) and prints each case formula through
`formulaInWords` (`portal/src/pages/SecurityAnalysis/tabs/ModelTab.tsx`: drop every `\b[A-Z][A-Z0-9]*_[A-Z0-9_]+\b` token, then close
up the brackets it leaves -- five `.replace` steps, then `.trim()`). The export (`lib/research/print/render_pack.py`) prints the
mnemonic instead: `_figures_table` (`| Mnemonic | Rendered |`). The rule (CTO ruling W4-S1 (b)): ONE definition, served, read by
both the page and the export. This project writes the server side and the export; the page's switch is DSGN_AMGTV1's.

**Build:**
1. ONE server-side definition in `lib/research/api/` (a module of your choice, e.g. `model_words.py`): the line-name map, equal
   entry for entry to the page's `LINE_NAMES` today, and `formula_words(formula)`, a port of `formulaInWords` returning the same
   string for the same input. Expose them as `scoped_amgt._model_line_names()` and `scoped_amgt._formula_words(formula)`.
2. The `/thesis` payload carries the definition: `model.line_names` (the map), and every served case in `model.cases` that carries
   a `formula` also carries `formula_words`. Nothing else in the payload moves.
3. The export reads it: `render_pack._figures_table` becomes `| Mnemonic | Line | Rendered |`, `Line` = the served name for a
   mapped mnemonic, else the figure's own `basis.definition`, else `A line this pack does not name` (the page's fallback order,
   `lineName` in modelSheet.ts). **The mnemonic stays the FIRST cell:** FWD-30's harness (DSGN_AMGTV1's file, which you do not
   edit) keys each row on a single-token first cell. **The case line (`_model_case_line`) does NOT change in this cell:** the
   harness compares it byte for byte with the served formula; its words wait on DSGN_AMGTV1's harness change.
4. Tests pinning: the map equals a parse of `modelSheet.ts` at test time; `formula_words` on the four strings AC1 uses; the
   table's three columns and fallback order.

**Begin only when** `AMGT-ww-2` is drained (it also edits `scoped_amgt.py`; keep its changes). The issuer spawns you then.

## 2. BOUNDS

1. No page file, no harness file (`portal/**` is read-only to you), no Terraform, no deploy, no number moved.
2. Standing: no install, no push, no promote, no vendor call. REFUSE, do not rescue.
3. Python from the repo root with `PYTHONPATH="$(pwd)"`; node for AC1.

## 3. SURFACES

<paths>
lib/research/api/scoped_amgt.py
lib/research/api/*.py
lib/research/api/tests/**
lib/research/print/render_pack.py
lib/research/print/tests/**
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~171/**
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the whole repository including `portal/`; the deployed function (AC2's captures).

## 4. PROOF OF SPEC (literal; timeout 120)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-ww-4"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round48/checks/ww-4.AC1.py; echo "exit=$?"</invocation><expect>line names: page 25, served 25; each fixture reads mapped lines N, named in words N; THE EXPORT'S WORDS COME FROM ONE SERVED DEFINITION THAT MATCHES THE PAGE'S: YES -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-ww-4"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; bash org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round48/checks/ww-4.AC2.sh; echo "exit=$?"</invocation><expect>rebuilt export vs page: EXPORT-COMPARE OK on 3 of 3; sweep rc=0 -- and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-ww-4"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; bash org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round48/checks/api-suite.sh; echo "exit=$?"</invocation><expect>pytest reports N passed and 0 failed -- and exit=0</expect></criterion>
</proof_of_spec>

AC1 the built behaviour against the page's own source; AC2 the seam (FWD-30's harness over the rebuilt export); AC3 the bound.

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~171/AMGT_RESAPP.TO-AMGT-ww-4.the-exports-words-from-one-served-definition.proof_of_spec.json`. Report once: what you changed and where, the payload field names, the commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round-47 analysis s.4 row 3 (@657b9283a2), ruling W4-S1 (b). Base: AC1 FAIL (no `_model_line_names`, no
`_formula_words`), AC2 PASS (3 of 3; cases 9 of 9), AC3 PASS (308). The case line in words and the page reading the served map
are asked of DSGN_AMGTV1 through its round at the issuance. SERVED: reaches the Lambda at ww-1.

<status>pending</status>
<round>48</round>
<slot>~171</slot>
<fabric>site-z</fabric>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
