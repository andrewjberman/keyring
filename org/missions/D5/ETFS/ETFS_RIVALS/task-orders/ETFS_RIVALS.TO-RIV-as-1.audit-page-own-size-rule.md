# ETFS_RIVALS task order -- `RIV-as-1` -- ROUND 14 (ENRICHMENT): THE AUDIT PAGE'S OWN LOUD SIZE RULE

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/ETFS/ETFS_RIVALS/decompositions/ETFS_RIVALS_DECOMP.md</decomp_doc>
<owned_cells>RIV-as-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_ETFS_RIVALS~1</issued_to>
<issued_by>2.0.0_SA_COO~RV</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule, cron or trigger is added or moved by this cell (the sweep's own step order changes inside one invocation)
comp-iam: DECLARED-NOT-APPLICABLE no IAM grant, role or policy changes in this cell (the daily role already runs produce_a1 inside the publish step)
comp-adversary: DECLARED-NOT-APPLICABLE the validator-context composer profiles RETURNED work for the L8/L9 packet; at the cut nothing is returned, and the issuer's evidence context is this order's check files
</preflight>

**Project:** ETFS_RIVALS (D5/ETFS, fabric site-z) -- *rivalfunds*: a daily research page on rival active ETFs (13 funds, two peer groups): rankings, buying trend, AI accounts per fund, and since round 12-13 a separate audit page; published to S3 by the package `data/etfs/scripts/rivalfunds/` (five AWS stage Lambdas; the 09:00 ET sweep runs the AI step and republishes) and served signed-in by the opal-gateway. **Round 14**: an AI account must agree with the panels beside it or say on its badge that it does not; the audit page gets its own size rule. Nothing here deploys, merges or calls a vendor (stub every OpenAI and Bloomberg hook). Work ONLY in the worktree your spawn line names; every path below is relative to that root.

## 1. YOUR CELL (inlined verbatim from the decomposition)

### `RIV-as-1` -- the audit page's own loud size rule (row Z-W1-S48; round-13 analysis ruling 4)
- Measured 2026-10-07: the served audit.html is 1,381,244 B against the gateway's 2,097,152 B read cap (34.1% under); the trade
  log grows every day; `publish_page` checks only index.html against MAX_PAGE_BYTES and writes audit.html unconditionally.
- Interface: `render.AUDIT_SOFT_CAP` (bytes, default 1_950_000). `render.render_audit_page(ctx)` returns a document of at most
  that size when a cut can achieve it: trade trace panels are dropped OLDEST first (by window end) until it fits, and the page
  then carries one element `data-audit-cut="<count left out>"` stating in plain words how many trades were left out and the
  oldest window end still shown; with nothing cut the attribute is absent. `publish_page`: the manifest carries
  `audit_trades_left_out` (0 when none) and, when it is > 0, the stage prints a line starting `FAIL: audit page over cap` (the
  day still publishes). The gateway never refuses the audit page silently.
- **Organic trigger:** the 07:00 ET marker publish.

## 2. WHAT YOU NEED TO KNOW (measured at the cut, base CLOUD 330067f27b)

- The check file's docstring is the exact interface it reads: read `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round14/checks/as-1.AC1.py` (and `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round14/checks/_common.py`) before you build. You run this AFTER RIV-ab-1 on the same branch: keep ab-1's behaviour intact.
- `render.render_audit_page` / `_render_audit_body` (rounds 12-13) build the audit document: the trades section (`_group` blocks with one `<details class="trace"` per trade), holdings, refused, citations, status, then its own `_sec_dialogs`. `DIALOG_SOFT_CAP` and its dialogs-off fallback already apply to the audit page; this cell adds the trade cut BEFORE that fallback has to fire, and keeps the fallback as the last resort.
- The cut drops whole trade trace panels, oldest window end first, across all funds; holdings, citations and status are never cut. If dropping every trade still leaves the page over the cap, keep the existing fallback and say so in the cut statement.
- `publish_page`: the audit document is written with read-back beside index.html; add `audit_trades_left_out` to the manifest and the `FAIL: audit page over cap` line the same way `FAIL: holding dialogs off` is printed.

## 3. SURFACES AND BOUNDS

You READ (never edit): `lib/`, `integrations/bloomberg/` (Andrew-direct no-modify order), every file not in your `<paths>`, the round-8..14 check folders under `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/`, the decomposition, and `org/missions/D5/ETFS/ETFS_RIVALS/ledger/ROUND_ANALYSIS.round13.md`.

You WRITE only the `<paths>` below (plus `deliverables/0.9.0_WK_ETFS_RIVALS~1/`). NEVER: any S3 read or write, any deploy, any OpenAI or Bloomberg call (stub every vendor hook), any environment gate flip outside a test, any file under `integrations/` or `infra/`. New tests as `data/etfs/scripts/rivalfunds/tests/test_r14as1_*.py`; run the whole package suite (`python -m pytest rivalfunds/tests -q` from `data/etfs/scripts/`) before you report: 0 failed. A check you cannot satisfy without leaving your `<paths>` is a surprise row in the investigation file (`surfaced_at` = `date -u +%FT%TZ` at filing), never an edit outside them.

<paths>
data/etfs/scripts/rivalfunds/render.py
data/etfs/scripts/rivalfunds/publish_page.py
data/etfs/scripts/rivalfunds/tests/
org/missions/D5/ETFS/ETFS_RIVALS/surprise-channel/investigations/INVESTIGATION_v1.Z.md
</paths>

## 4. PROOF OF SPEC (each invocation LITERAL, run from your worktree root)

- **AC1** -- over its cap the audit page shows the newest trades that fit and states how many were left out; control: at the default cap all trades show and nothing is cut (`org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round14/checks/as-1.AC1.py`)

<proof_of_spec>
  <criterion id="AC1" cell_refs="RIV-as-1"><invocation>python org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round14/checks/as-1.AC1.py</invocation><expect>AC1 RESULT: PASS 0 failures</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the instance at `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/0.9.0_WK_ETFS_RIVALS~1/ETFS_RIVALS.TO-RIV-as-1.audit-page-own-size-rule.proof_of_spec.json` with `to_id` `ETFS_RIVALS.TO-RIV-as-1.audit-page-own-size-rule`. Report once: each mechanical criterion's verdict line with the output above it; each judgment criterion left UNVERIFIABLE-BY-INSTRUMENT for the CVO; files written; every existing test assertion changed and why; the suite's final line; rows filed (id + one line); the hookups you need the issuer to add at the merge. Leave the `<status>` flip to the issuer.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6, 2.0.0_SA_COO~RV):** ROUND_ANALYSIS.round13.md @594d1be8f8; decomposition v1.4 (round 14 appended). Chain `~1`, slot `~1`, position 2 of 2. Check dry-run at base: as-1.AC1 FAIL (1; control (b) PASS) as expected.

<risk>SERVED</risk>
<worker_class>worker</worker_class>
<status>pending</status>
<round>14</round>
<slot>~1</slot>
<fabric>site-z</fabric>
<status>complete</status>
