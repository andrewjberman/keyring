# ETFS_RIVALS task order -- `RIV-au-1` -- ROUND 12 (ENRICHMENT): THE AUDIT TRAIL COMES OFF THE PAGE INTO ITS OWN DATED OBJECT SO THE MAIN PAGE KEEPS EVERY SECURITY DIALOG; THE OVER-CAP FALLBACK STOPS BEING SILENT

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/ETFS/ETFS_RIVALS/decompositions/ETFS_RIVALS_DECOMP.md</decomp_doc>
<owned_cells>RIV-au-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_ETFS_RIVALS~1</issued_to>
<issued_by>2.0.0_SA_COO~RV</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule, cron or trigger is added or moved by this cell
comp-iam: DECLARED-NOT-APPLICABLE the new object sits under the page prefix the publish role already writes (homes.page); no IAM grant, role or policy changes in this cell
comp-adversary: DECLARED-NOT-APPLICABLE the validator-context composer profiles RETURNED work for the L8/L9 packet; at the cut nothing is returned, and the issuer's evidence context is this order's check files
</preflight>

**Project:** ETFS_RIVALS (D5/ETFS, fabric site-z) -- *rivalfunds*: daily holdings of rival active ETFs in two peer groups (IDVZ, PFOE), each fund's trade schedule, the A1 rankings, buying trend, input census and AI accounts, and a served page grouped by Opal fund (13 funds, package `data/etfs/scripts/rivalfunds/`, served by the opal-gateway at `mcp.opalinvest.dev/rivalfunds`, which refuses a page over 2 MB). **Round 12** (narrowed, on Andrew's word "Any mention of a security by ticker should be hyperlinked to the modal popup for that fund's engagement with that security"): the main page has lost every security link because its audit trail no longer leaves room for the dialogs. Andrew's order of work: "1.) Pull audit off the page 2.) Get those linking schemas up and running 3.) Make an audit gateway after 2.) is done" -- this order is steps 1 and 2; the audit trail is still written every day as its own object, but nothing links or serves it yet. Nothing in round 12 deploys, merges, flips a gate or calls Bloomberg/OpenAI from a worker. Work ONLY in the worktree your spawn line names; every path below is relative to that root.

## 1. YOUR CELL (inlined verbatim from the decomposition)

### `RIV-au-1` -- the audit trail comes off the main page into its own dated object; every security mention links in-document; the over-cap fallback is loud (row Z-S47)
- Measured 2026-10-06 (2.0.0_SA_COO~RV): the served 2026-10-05 and 2026-10-06 pages (1,798,995 B and 1,813,001 B) carry
  `data-holding-dialogs="off"`, 0 `data-sec-dialog`, 0 `data-sec`. `render.render_page` (render.py:1796-1803) re-renders the
  whole page without holding dialogs once the with-dialogs render crosses `DIALOG_SOFT_CAP` (1,950,000 B, set under the
  gateway's 2 MB refusal). The closed `<details id="audit">` block is 1,119,671 B of the 10-06 page (holdings 454,238 B across
  13 funds, trade log 370,517 B across 221 trade panels).
- Interface:
  - `render.render_page(ctx)` returns the MAIN page with no audit block and NO link to the audit trail (the link lands with the
    gateway route in a later round, never a 404);
  - `render.render_audit_page(ctx)` returns the AUDIT page: a whole self-contained document (same shell and theme, no script)
    carrying the trades, holdings, refused and status sections and its OWN `_sec_dialogs` for the securities it names; every
    `data-sec` button on either page resolves to a `data-sec-dialog` element in the SAME document;
  - `render.validate` grades the main page (components lead, self-contained, no audit block) and a validator for the audit page
    grades what the closed block graded before (trades and holdings once each, one trace per trade);
  - `publish_page` writes `homes.page(day, "audit.html")` with read-back beside `index.html`, keeps a changed prior audit.html
    under `revisions/<ts>/` as it does index.html, and the manifest carries `audit_uri`, `audit_sha256`, `audit_bytes`,
    `holding_dialogs` ("on" | "off");
  - over `DIALOG_SOFT_CAP` the day still publishes, but the manifest and the run result's `detail` read
    `holding_dialogs: "off"` and the stage prints `FAIL: holding dialogs off ...` to stdout.
- **Organic trigger:** the 07:00 ET marker publish (publish-page stage).

## 2. WHAT YOU NEED TO KNOW (measured at the cut, base CLOUD 56de423b4d)

- The check files' docstrings are the exact interface they read: read all three under `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round12/checks/` (`au-1.AC1.py`, `au-1.AC2.py`, and `_common.py`) before you build.
- Today: `render._render_page_body` (render.py ~1831) builds `audit = '<details id="audit">...'` (trades = the `_group` blocks, `_holdings_section`, `_refused_section`, `_status_section`) and appends `_sec_dialogs(ctx)`; `render.validate` (render.py ~1857) REQUIRES that closed audit block on the page and counts `<details class="trace"` against the trade count; `publish_page.handler_entry` (publish_page.py ~719-799) renders, validates, checks `MAX_PAGE_BYTES`, then writes `index.html` + `manifest.json` with read-back and revision-keeping.
- `_sec_dialogs` writes one dialog per key in the module-global `_SEC_IDS`, which the body's buttons fill as they render, inside `_render_page`'s try/finally that resets the globals. The audit page needs the same discipline: its own pass that fills `_SEC_IDS` from the audit sections and emits only those dialogs.
- Keep the round-9 RIV-ln-1 two-pass name resolution and round-8 fc-1 behaviour (`tests/test_r8fc1_*`, `tests/test_r9ln1_*`, `tests/test_crorv_layout.py`). Existing tests that assert the audit block on `index.html` (`test_p1_page_and_guardrails.py`, `test_p2_page_grouped_by_fund.py`, `test_crorv_layout.py`, `test_r8fc1_security_dialog.py`, and any other your suite run names) are amended to read the audit page instead; state each changed assertion in your report.
- Keep `DIALOG_SOFT_CAP` and the binary fallback (the cap still guards a page that would cross it); this cell makes the fallback LOUD, not partial.
- The main page carries NO link to the audit trail in this round (a later round adds the gateway route, then the link). Do not leave a dangling reference to it in the page text either.

## 3. SURFACES AND BOUNDS

You READ (never edit): `lib/`, `integrations/bloomberg/` (under an Andrew-direct no-modify order), the package's other modules, `infra/aws/ec2/opal-gateway/` (the gateway route is a later round), the round-12 and earlier rounds' check folders under `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/`, the decomposition `org/missions/D5/ETFS/ETFS_RIVALS/decompositions/ETFS_RIVALS_DECOMP.md`, and the analysis `org/missions/D5/ETFS/ETFS_RIVALS/ledger/ROUND_ANALYSIS.round10.md` (ADDENDUM 3 and ADDENDUM 4).

You WRITE only the `<paths>` below (plus `deliverables/0.9.0_WK_ETFS_RIVALS~1/`). NEVER: any S3 read or write, any deploy, any Bloomberg or OpenAI call (stub every vendor hook in tests), any environment gate flip outside a test, any gateway file. New tests go beside the code as `tests/test_r12au1_*.py`, run with `python -m pytest <file> -q` from `data/etfs/scripts/`; run the whole package suite (`python -m pytest rivalfunds/tests -q` from `data/etfs/scripts/`) before you report: it must read 0 failed. A check you cannot satisfy without leaving your `<paths>` is a surprise row in the investigation file (`surfaced_at` = `date -u +%FT%TZ` at filing), never an edit outside them.

<paths>
data/etfs/scripts/rivalfunds/render.py
data/etfs/scripts/rivalfunds/publish_page.py
data/etfs/scripts/rivalfunds/tests/
org/missions/D5/ETFS/ETFS_RIVALS/surprise-channel/investigations/INVESTIGATION_v1.Z.md
</paths>

## 4. PROOF OF SPEC (each invocation LITERAL, run from your worktree root)

- **AC1** -- the main page carries no audit trail and no audit link yet; `render_audit_page` returns a whole audit document with its own resolving dialogs (Apple linked in its trade log); control: every button resolves in its own document (`org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round12/checks/au-1.AC1.py`)
- **AC2** -- the publisher writes audit.html beside index.html and names it in the manifest; over the cap the day publishes with `holding_dialogs: "off"` in the manifest and detail and a `FAIL: holding dialogs off` stdout line; control: a normal publish prints no FAIL line (`org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round12/checks/au-1.AC2.py`)

<proof_of_spec>
  <criterion id="AC1" cell_refs="RIV-au-1"><invocation>python org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round12/checks/au-1.AC1.py</invocation><expect>AC1 RESULT: PASS 0 failures</expect></criterion>
  <criterion id="AC2" cell_refs="RIV-au-1"><invocation>python org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round12/checks/au-1.AC2.py</invocation><expect>AC2 RESULT: PASS 0 failures</expect></criterion>
  <criterion id="J1" cell_refs="RIV-au-1" judgment="true"/>
</proof_of_spec>

J1 (graded by 3.0.0_SA_CVO~RV at L9 on the issuer's real 10-06 render, never self-graded): every ticker mention on the main page opens that security's modal for the fund's engagement with it, and the page reads whole without the audit trail.

## 5. WHEN YOU ARE DONE

Write the instance at `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/0.9.0_WK_ETFS_RIVALS~1/ETFS_RIVALS.TO-RIV-au-1.audit-trail-own-page-every-dialog-kept.proof_of_spec.json` with `to_id` `ETFS_RIVALS.TO-RIV-au-1.audit-trail-own-page-every-dialog-kept`. Report once: each mechanical criterion's verdict line with the output above it; each judgment criterion left UNVERIFIABLE-BY-INSTRUMENT for the CVO; files written; every existing test assertion changed and why; the package suite's final line; rows filed (id + one line); the hookups you need the issuer to add at the merge. Leave the `<status>` flip to the issuer.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6, 2.0.0_SA_COO~RV):** ROUND_ANALYSIS.round10.md ADDENDUM 3 @8f1c1a9e6e route B as re-sequenced by ADDENDUM 4 @56de423b4d (steps 1-2); Andrew-direct records @05c469e083 and @56de423b4d; decomposition round 12 v1.0 (narrowed, 1 cell). Chain `~1`, slot `~1`, position 1 of 1. Checks dry-run at base CLOUD 56de423b4d: au-1.AC1 FAIL (2; control (c) PASS) as expected; au-1.AC2 FAIL (2; control (c) PASS) as expected. Bounds: the publisher deploy is the issuer's act under a never-widen pair (CLOUD HEAD also carries undeployed ok-1 + gt-1); ADDENDUM 4 withdrew the gateway-first ordering; the issuer's one real run renders the 10-06 inputs and prints the main page's bytes against DIALOG_SOFT_CAP (>= 20% headroom) and 0 dead mentions on both pages.

<risk>SERVED</risk>
<worker_class>worker</worker_class>
<status>pending</status>
<round>12</round>
<slot>~1</slot>
<fabric>site-z</fabric>
<status>complete</status>
