# ETFS_RIVALS task order -- `RIV-gw-1` -- ROUND 13 (ENRICHMENT): THE GATEWAY SERVES THE DAY'S AUDIT PAGE AT /rivalfunds/YYYY-MM-DD/audit

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/ETFS/ETFS_RIVALS/decompositions/ETFS_RIVALS_DECOMP.md</decomp_doc>
<owned_cells>RIV-gw-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_ETFS_RIVALS~1</issued_to>
<issued_by>2.0.0_SA_COO~RV</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule, cron or trigger is added or moved by this cell
comp-iam: DECLARED-NOT-APPLICABLE no IAM grant, role or policy changes in this cell (the gateway's read policy already covers the page prefix)
comp-adversary: DECLARED-NOT-APPLICABLE the validator-context composer profiles RETURNED work for the L8/L9 packet; at the cut nothing is returned, and the issuer's evidence context is this order's check files
</preflight>

**Project:** ETFS_RIVALS (D5/ETFS, fabric site-z) -- *rivalfunds*: a daily research page on rival active ETFs (13 funds, two peer groups), published to S3 by the package `data/etfs/scripts/rivalfunds/` (five AWS stage Lambdas) and served signed-in by the opal-gateway (Starlette app under `infra/aws/ec2/opal-gateway/app/`) at `mcp.opalinvest.dev/rivalfunds`. Andrew's word: "Any mention of a security by ticker should be hyperlinked to the modal popup for that fund's engagement with that security" and "1.) Pull audit off the page 2.) Get those linking schemas up and running 3.) Make an audit gateway after 2.) is done". Round 12 took the audit trail off the page into a daily `audit.html` and linked every ticker. **Round 13** (main workstream): the audit route and link, and every mention opening its fund's engagement. Nothing here deploys, merges or calls a vendor. Work ONLY in the worktree your spawn line names; every path below is relative to that root.

## 1. YOUR CELL (inlined verbatim from the decomposition)

### `RIV-gw-1` -- the gateway serves the day's audit page at GET /rivalfunds/YYYY-MM-DD/audit (ADDENDUM 4 step 3; round-11 analysis item 1)
- Measured 2026-10-06: `infra/aws/ec2/opal-gateway/app/rivalfunds_view.py` serves only `<key_prefix>date=<day>/index.html`
  (`object_key`, `_PAGE_NAME`); server.py mounts `/rivalfunds`, `/rivalfunds/`, `/rivalfunds/archive`, `/rivalfunds/{day}`. The
  publisher has written `audit.html` beside index.html every day since round 12 (10-06: 1,326,857 B). The read policy
  (`gen_rivalfunds_location.py` `policy_doc`) already grants GetObject on `<key_prefix>*`: no new grant.
- Interface: `audit_key(day)` = `<key_prefix>date=<day>/audit.html` from the generated location (never typed) and the handler
  `rivalfunds_audit(request)`: no viewer 401; a bad date 400; a missing object 404 naming the day's audit page with a link to the
  day's page; otherwise the bytes with `_HEADERS`, under the same 2 MB cap and TTL cache as the page. The server.py Route line is
  the issuer's hookup at the merge; the gateway release is the issuer's act under a never-widen pair, BEFORE lk-1's link deploys.
- **Organic trigger:** a signed-in viewer following the main page's audit link.

## 2. WHAT YOU NEED TO KNOW (measured at the cut, base CLOUD 365f0a59e1)

- The check file's docstring is the exact interface it reads: read `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round13/checks/gw-1.AC1.py` (and `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round13/checks/_common.py`) before you build.
- Follow `rivalfunds_day` / `_serve_day` (rivalfunds_view.py ~154-196): the same `_viewer` identity read, `valid_day`, `_cached` + `_fetch_capped`, `_OverCap` -> 502, NoSuchKey -> 404, other S3 errors -> 502, `audit.log_call(email, "rivalfunds_view", {...}, ...)` on each outcome (add `"route": "audit"`). Prefer generalising `_serve_day` over a copy.
- AMENDMENT 1 (issuer, 2026-10-06 ~20:3xZ): the route hookup is YOURS, not the issuer's -- `infra/aws/` is an AE lane the issuer cannot write. In `app/server.py` add `Route("/rivalfunds/{day}/audit", rivalfunds_view.rivalfunds_audit, methods=["GET"]),` on the line BEFORE `Route("/rivalfunds/{day}", ...)`; in `tests/test_principal_cutover.py` declare `"/rivalfunds/{day}/audit": "access-layer"` in ROUTE_CLASS beside `"/rivalfunds/{day}"` (the route census tests `test_oga2_ac04` and `test_ogz1_ac08` FAIL naming an undeclared route otherwise). Touch nothing else in either file.
- Gateway unit tests: `infra/aws/ec2/opal-gateway/app/tests/test_rivalfunds_view.py` (S3 and the viewer stubbed). Run from `infra/aws/ec2/opal-gateway`: `python -m pytest app/tests/test_rivalfunds_view.py -q` (0 failed).

## 3. SURFACES AND BOUNDS

You READ (never edit): `lib/`, `integrations/bloomberg/` (Andrew-direct no-modify order), every file not in your `<paths>`, the round-8..13 check folders under `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/`, the decomposition `org/missions/D5/ETFS/ETFS_RIVALS/decompositions/ETFS_RIVALS_DECOMP.md`, and `org/missions/D5/ETFS/ETFS_RIVALS/ledger/ROUND_ANALYSIS.round11.md`.

You WRITE only the `<paths>` below (plus `deliverables/0.9.0_WK_ETFS_RIVALS~1/`). NEVER: any S3 read or write, any deploy or gateway release, any Terraform, any Bloomberg or OpenAI call (stub every vendor hook), any environment gate flip outside a test, any file under `integrations/`. New tests as `app/tests/test_r13gw1_*.py` beside the code's tests; run the code's whole test suite before you report: 0 failed. A check you cannot satisfy without leaving your `<paths>` is a surprise row in the investigation file (`surfaced_at` = `date -u +%FT%TZ` at filing), never an edit outside them.

<paths>
infra/aws/ec2/opal-gateway/app/rivalfunds_view.py
infra/aws/ec2/opal-gateway/app/tests/test_rivalfunds_view.py
infra/aws/ec2/opal-gateway/app/server.py
infra/aws/ec2/opal-gateway/tests/test_principal_cutover.py
org/missions/D5/ETFS/ETFS_RIVALS/surprise-channel/investigations/INVESTIGATION_v1.Z.md
</paths>

## 4. PROOF OF SPEC (each invocation LITERAL, run from your worktree root)

- **AC1** -- GET /rivalfunds/2026-10-06/audit serves the stored audit.html under the view's headers; no viewer 401, bad date 400, missing 404; control: /rivalfunds/2026-10-06 still serves index.html (`org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round13/checks/gw-1.AC1.py`)

<proof_of_spec>
  <criterion id="AC1" cell_refs="RIV-gw-1"><invocation>python org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round13/checks/gw-1.AC1.py</invocation><expect>AC1 RESULT: PASS 0 failures</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the instance at `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/0.9.0_WK_ETFS_RIVALS~1/ETFS_RIVALS.TO-RIV-gw-1.gateway-serves-audit-page.proof_of_spec.json` with `to_id` `ETFS_RIVALS.TO-RIV-gw-1.gateway-serves-audit-page`. Report once: each mechanical criterion's verdict line with the output above it; each judgment criterion left UNVERIFIABLE-BY-INSTRUMENT for the CVO; files written; every existing test assertion changed and why; the suite's final line; rows filed (id + one line); the hookups you need the issuer to add at the merge. Leave the `<status>` flip to the issuer.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER AMENDMENT 1 (2.0.0_SA_COO~RV, 2026-10-06 ~20:3xZ):** <paths> gains app/server.py and tests/test_principal_cutover.py; the hookup moves from the issuer to the worker because lane CLOUD_OPS_OR_ETL refused the issuer's commit (measured: safe-commit rc=1, owned-paths violation on both files). No criterion changes; the gate does not grade a modification (LIMB 6 fires on new orders only).

**ISSUER NOTES (L5/L6, 2.0.0_SA_COO~RV):** ROUND_ANALYSIS.round11.md @3ae96d6bc7 section 3; decomposition v1.3 (round 13 appended). Chain `~1`, slot `~1`, position 1 of 1. Check dry-run at base: gw-1.AC1 FAIL (2; control (c) PASS) as expected. Issuer acts after the drain: server.py Route hookup; the gateway release (NFRA_OPLGTW release path, last rel-nfra-oplgtw-r20) under a never-widen pair, before lk-1's link deploys.

<risk>WORLD</risk>
<worker_class>worker-light</worker_class>
<status>pending</status>
<round>13</round>
<slot>~1</slot>
<fabric>site-z</fabric>
<status>complete</status>
