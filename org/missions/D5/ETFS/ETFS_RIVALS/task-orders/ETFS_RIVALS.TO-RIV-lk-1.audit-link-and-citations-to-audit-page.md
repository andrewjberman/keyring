# ETFS_RIVALS task order -- `RIV-lk-1` -- ROUND 13 (ENRICHMENT): THE MAIN PAGE'S ONE AUDIT LINK; THE AI CITATION LINES MOVE TO THE AUDIT PAGE

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/ETFS/ETFS_RIVALS/decompositions/ETFS_RIVALS_DECOMP.md</decomp_doc>
<owned_cells>RIV-lk-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_ETFS_RIVALS~2</issued_to>
<issued_by>2.0.0_SA_COO~RV</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule, cron or trigger is added or moved by this cell
comp-iam: DECLARED-NOT-APPLICABLE no IAM grant, role or policy changes in this cell (the gateway's read policy already covers the page prefix)
comp-adversary: DECLARED-NOT-APPLICABLE the validator-context composer profiles RETURNED work for the L8/L9 packet; at the cut nothing is returned, and the issuer's evidence context is this order's check files
</preflight>

**Project:** ETFS_RIVALS (D5/ETFS, fabric site-z) -- *rivalfunds*: a daily research page on rival active ETFs (13 funds, two peer groups), published to S3 by the package `data/etfs/scripts/rivalfunds/` (five AWS stage Lambdas) and served signed-in by the opal-gateway (Starlette app under `infra/aws/ec2/opal-gateway/app/`) at `mcp.opalinvest.dev/rivalfunds`. Andrew's word: "Any mention of a security by ticker should be hyperlinked to the modal popup for that fund's engagement with that security" and "1.) Pull audit off the page 2.) Get those linking schemas up and running 3.) Make an audit gateway after 2.) is done". Round 12 took the audit trail off the page into a daily `audit.html` and linked every ticker. **Round 13** (main workstream): the audit route and link, and every mention opening its fund's engagement. Nothing here deploys, merges or calls a vendor. Work ONLY in the worktree your spawn line names; every path below is relative to that root.

## 1. YOUR CELL (inlined verbatim from the decomposition)

### `RIV-lk-1` -- the main page's one audit link; the AI citation lines move to the audit page (ADDENDUM 4 step 3; round-11 analysis ruling 3)
- Measured on the served 10-06 page (CVO): the AI modals carry 148 machine keys in 89 citation lines ("Cited rows: ..."), plain;
  the main page has no audit link (au-1, by design until the route serves).
- Interface: `render.render_page(ctx)` carries exactly one `<a href="/rivalfunds/<day>/audit">` worded as "one step away"; no AI modal
  on the main page carries a "Cited rows:" line (grade line, full text, Observed/Inferred, invalidation stay). `render_audit_page`
  carries a section `id="citations"` with, per fund and account, its "Cited rows:" line (and [web] reads when present), each block
  `data-cited-fund="<fund>"` `data-ai-kind="<kind>"`. Deploys only after RIV-gw-1's route serves (never a 404).
- **Organic trigger:** the 07:00 ET marker publish after the route serves.

## 2. WHAT YOU NEED TO KNOW (measured at the cut, base CLOUD 365f0a59e1)

- The check file's docstring is the exact interface it reads: read `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round13/checks/lk-1.AC1.py` (and `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round13/checks/_common.py`) before you build. You run this AFTER fe-1 on the same branch: keep fe-1's behaviour intact.
- The AI account block: `render` ~1500-1552 (`full`, `src` with "Cited rows:" and "[web] reads:", the dialog `data-ai-dialog`). The audit page: `render_audit_page` / `_render_audit_body` (round 12 au-1). Round 12 removed every main-page sentence pointing at the audit trail; this cell adds the ONE link back.
- The link must not ship before the gateway route serves; that ordering is the issuer's deploy, not a flag in your code.

## 3. SURFACES AND BOUNDS

You READ (never edit): `lib/`, `integrations/bloomberg/` (Andrew-direct no-modify order), every file not in your `<paths>`, the round-8..13 check folders under `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/`, the decomposition `org/missions/D5/ETFS/ETFS_RIVALS/decompositions/ETFS_RIVALS_DECOMP.md`, and `org/missions/D5/ETFS/ETFS_RIVALS/ledger/ROUND_ANALYSIS.round11.md`.

You WRITE only the `<paths>` below (plus `deliverables/0.9.0_WK_ETFS_RIVALS~2/`). NEVER: any S3 read or write, any deploy or gateway release, any Terraform, any Bloomberg or OpenAI call (stub every vendor hook), any environment gate flip outside a test, any file under `integrations/`. New tests as `data/etfs/scripts/rivalfunds/tests/test_r13lk1_*.py` beside the code's tests; run the code's whole test suite before you report: 0 failed. A check you cannot satisfy without leaving your `<paths>` is a surprise row in the investigation file (`surfaced_at` = `date -u +%FT%TZ` at filing), never an edit outside them.

<paths>
data/etfs/scripts/rivalfunds/render.py
data/etfs/scripts/rivalfunds/tests/
org/missions/D5/ETFS/ETFS_RIVALS/surprise-channel/investigations/INVESTIGATION_v1.Z.md
</paths>

## 4. PROOF OF SPEC (each invocation LITERAL, run from your worktree root)

- **AC1** -- the main page has one /rivalfunds/<day>/audit link and no citation lines; the audit page's citations section carries TXUE's citation line; control: TXUE's AI dialog stays with its grade line (`org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round13/checks/lk-1.AC1.py`)

<proof_of_spec>
  <criterion id="AC1" cell_refs="RIV-lk-1"><invocation>python org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round13/checks/lk-1.AC1.py</invocation><expect>AC1 RESULT: PASS 0 failures</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the instance at `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/0.9.0_WK_ETFS_RIVALS~2/ETFS_RIVALS.TO-RIV-lk-1.audit-link-and-citations-to-audit-page.proof_of_spec.json` with `to_id` `ETFS_RIVALS.TO-RIV-lk-1.audit-link-and-citations-to-audit-page`. Report once: each mechanical criterion's verdict line with the output above it; each judgment criterion left UNVERIFIABLE-BY-INSTRUMENT for the CVO; files written; every existing test assertion changed and why; the suite's final line; rows filed (id + one line); the hookups you need the issuer to add at the merge. Leave the `<status>` flip to the issuer.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6, 2.0.0_SA_COO~RV):** ROUND_ANALYSIS.round11.md @3ae96d6bc7 section 3; decomposition v1.3 (round 13 appended). Chain `~2`, slot `~2`, position 2 of 2. Check dry-run at base: lk-1.AC1 FAIL (2; control (c) PASS) as expected. Deploy only after gw-1's release serves the route.

<risk>SERVED</risk>
<worker_class>worker</worker_class>
<status>pending</status>
<round>13</round>
<slot>~2</slot>
<fabric>site-z</fabric>
<status>complete</status>
