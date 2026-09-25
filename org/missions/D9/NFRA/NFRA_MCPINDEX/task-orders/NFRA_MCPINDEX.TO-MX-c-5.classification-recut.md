# NFRA_MCPINDEX task order -- `MX-c-5` -- ROUND 2, E3: the 9 non-Schwab tools declare their class; AC11 closes at 44 + 5 HELD

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_MCPINDEX/decompositions/NFRA_MCPINDEX_DECOMP.md</decomp_doc>
<owned_cells>MX-c-5</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_MCPINDEX~1</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a build cell; no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM surface; nothing is deployed.
comp-adversary: DECLARED-NOT-APPLICABLE -- the CVO's round-1 rows are the input.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `MX-c-5` (round 2, decomposition section R2.1)

Your worktree is `/c/tmp/mx-1`, on the HELD branch `wk-nfra_mcpindex-1-1d`. It carries MX-c-4's build
(`119a49eef0`): classification and registration compose from each integration's own declaration, and a tool with no
declaration is refused. It also carries your own round-1 probe, `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~1/probes/mx_c_4.py`.
Under AC11's two-limb text, that probe measured 14 of 49 registered tools with no `destructive_ops` class: 9
ycharts/opal_portal/globgrph tools and 5 schwab tools.

The CTO ruled (D-3, `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/1.0.0_SA_CTO~O/ROUND1_RULINGS.md` R-1 @9c70622d13,
READ IT):
1. Each of the **9 ycharts / opal_portal / globgrph tools** declares its class in its OWN integration directory
   (`infra/aws/ec2/opal-gateway/app/integrations/{ycharts,opal_portal,globgrph}/`), through the same declaration MX-c-4
   built. Read each tool's code before you choose, and state the reason for each class in your result.
2. The **5 schwab tools are HELD** behind Andrew's OPLGTW stop: registered but not enabled. They are NOT classified, and
   `integrations/schwab/` is never edited.
3. **Conform your probe's AC11** to the ruling: it prints the 49-name denominator and reports
   `44 classified + 5 HELD`, naming the 5 HELD tools, and PASSES only then. A HELD name is a schwab tool that is
   registered but absent from `ENABLED_INTEGRATIONS`.
4. **The interpreter is `python`** (device-neutral, row W1-S6), never `py -3.12`.

## 2. BOUNDS

1. Nothing is deployed. The branch stays HELD until the CVO grades AC4 (R-5).
2. `integrations/schwab/` is read, never edited. The gateway suite adds no failure.
3. Standing: no push, no install, no vendor call, no AWS. REFUSE a criterion you cannot meet as written, and report the
   refusal with its measurement. Never repair a criterion, widen it, or meet it by a route this face does not name.

## 3. SURFACES

<paths>
infra/aws/ec2/opal-gateway/app/integrations/ycharts/
infra/aws/ec2/opal-gateway/app/integrations/opal_portal/
infra/aws/ec2/opal-gateway/app/integrations/globgrph/
infra/aws/ec2/opal-gateway/tests/test_tool_classification_composition.py
infra/aws/ec2/opal-gateway/tests/test_entitlement_admin.py
org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~1/**
org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/**
</paths>

Rows: `org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/INVESTIGATION_v1.md`, id
`NFRA_MCPINDEX-Z-W1-S<k>` (site-Z rows carry `Z-`), fabric `site-z`.

## 4. PROOF OF SPEC (literal; run from /c/tmp/mx-1, after your commit)

<proof_of_spec>
  <criterion id="MXC5-AC1" cell_refs="MX-c-5"><invocation>cd /c/tmp/mx-1 && timeout 120 python org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~1/probes/mx_c_4.py AC11</invocation><expect>(?m)^VERDICT: PASS-MXC4-AC11(?![0-9])</expect></criterion>
  <criterion id="MXC5-AC2" cell_refs="MX-c-5"><invocation>cd /c/tmp/mx-1 && timeout 120 python org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~1/probes/mx_c_4.py AC6</invocation><expect>(?m)^VERDICT: PASS-MXC4-AC6(?![0-9])</expect></criterion>
  <criterion id="MXC5-AC3" cell_refs="MX-c-5"><invocation>cd /c/tmp/mx-1 && timeout 120 python org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~1/probes/mx_c_4.py AC10</invocation><expect>(?m)^VERDICT: PASS-MXC4-AC10(?![0-9])</expect></criterion>
  <criterion id="MXC5-AC4" cell_refs="MX-c-5" judgment="true"/>
</proof_of_spec>

- `MXC5-AC1`: the amended AC11, 49 = 44 classified + 5 HELD.
- `MXC5-AC2`: the 40 tools that already resolved keep their class; the 9 newly classified are listed with their class
  and reason.
- `MXC5-AC3`: no gateway test that passed at this cell's base fails.
- `MXC5-AC4` is a JUDGMENT, carried from MX-c-4's AC8 (R-5). `3.0.0_SA_CVO~O` grades it at L9 BEFORE this branch
  drains. Record it UNVERIFIABLE-BY-INSTRUMENT with a status_reason naming the CVO; never PASS or FAIL. The question:
  `read_teams_attachment`'s classification, and each of the 9 new classes, is correct for what the tool does, widens
  no tier, and does not read as a write.

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~1/NFRA_MCPINDEX.TO-MX-c-5.classification-recut.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance>`. Report once:
- the 9 classes with their reasons;
- the 5 HELD names;
- the commit hash;
- any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** E3, R-5, D-3. Chain A's root, on the held branch. After it: MX-d-2 and MX-t-8, cut from the held
branch's head.

<status>complete</status>
<round>2</round>
<slot>~1</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
