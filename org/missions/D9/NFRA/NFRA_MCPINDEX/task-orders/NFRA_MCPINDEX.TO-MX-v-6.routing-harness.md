# NFRA_MCPINDEX task order -- `MX-v-6` -- ROUND 2, E4: a routing harness scored on REAL asks

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_MCPINDEX/decompositions/NFRA_MCPINDEX_DECOMP.md</decomp_doc>
<owned_cells>MX-v-6</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_MCPINDEX~2</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a harness run on demand; no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- offline; no AWS.
comp-adversary: DECLARED-NOT-APPLICABLE -- the harness IS the adversary read of routing; its planted-mislabel control is AC2.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `MX-v-6` (round 2, decomposition section R2.1)

Your branch carries the discover family (`app/integrations/opal_discover/`, MX-d-2), which names the next tool for a
question, and the portal tools (`app/integrations/portal_index/`, MX-t-8). The workspace already learned how a tool
index must be tested. `.tools/comp-which-routing-test.py`'s docstring records it: probes drawn from a catalog entry's
own words measure nothing. Read that docstring first.

Build:
1. **`infra/aws/ec2/opal-gateway/tests/routing/questions.yaml`**: at least 20 questions staff actually asked. Draw them
   from the Analyst's thread memory (`org/tier0_utility/0.0.3_BG_BBGTerminal/threads/**`, real colleague asks), and
   from any other real-ask record you find; record in your result where you looked, including for "the CRO's question
   lists". Each item has `id`, `question` (quoted or minimally anonymised: no client name, account number or balance),
   `source` (the repo path it came from, optionally `:line`) and `expected_tool`: the tool a correct router picks, or
   `NOT_CATALOGUED` for a subject the catalog does not hold. No question may reuse the catalog's own description words.
2. **`infra/aws/ec2/opal-gateway/tests/routing/run_routing.py`**, offline:
   - routes every question through the discover family's routing and prints one line per question: id, routed tool,
     expected, hit or miss;
   - ends with `ROUTING: <k> of <n> routed to the expected tool`;
   - `--plant-mislabel` swaps one question's expected tool, so the same run reports exactly one fewer hit (the control
     that the score can fall).

No accuracy bar is set: this round measures the router. The live cold run with a non-author asker is G-B, Andrew's.

**Standing rules (R-6):** the interpreter is `python`; no S3 is read; nothing served is written.

## 2. BOUNDS

1. Nothing is deployed; no gateway code outside `tests/routing/` changes. A routing defect you find is a ROW, never a
   fix here.
2. Standing: no push, no install, no vendor call, no AWS. REFUSE a criterion you cannot meet as written, and report the
   refusal with its measurement. Never repair a criterion, widen it, or meet it by a route this face does not name.

## 3. SURFACES

<paths>
infra/aws/ec2/opal-gateway/tests/routing/
org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~2/**
org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/**
</paths>

Read (never write): `.tools/comp-which-routing-test.py`, `org/tier0_utility/0.0.3_BG_BBGTerminal/threads/`,
`app/integrations/opal_discover/`, `app/integrations/portal_index/`, `app/refs/DATA_CATALOG.yaml`.

Rows: `org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/INVESTIGATION_v1.md`, id
`NFRA_MCPINDEX-Z-W2-S<k>`, fabric `site-z`.

## 4. PROOF OF SPEC (literal; run from your worktree root, after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="MX-v-6"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~O/round2/checks/v6.AC1.sh; echo "exit=$?"</invocation><expect>questions>=20; sources_at_head equals questions; expected_tools equals questions; catalog_overlap=0 -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="MX-v-6"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~O/round2/checks/v6.AC2.sh; echo "exit=$?"</invocation><expect>plain run rc=0 ROUTING k of n (n>=20); planted-mislabel run rc=0 ROUTING k-1 of n -- RESULT: PASS -- exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~2/NFRA_MCPINDEX.TO-MX-v-6.routing-harness.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance>`. Report once:
- the score and every miss;
- where the questions came from;
- the commit hash;
- any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** E4. SPAWN ONLY after MX-d-2 AND MX-t-8 are merged INTO the held branch. Cut from its head, then
merge back into it. The live cold run is G-B, at the close.

<status>complete</status>
<round>2</round>
<slot>~2</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
