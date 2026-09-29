# AMGT_RESAPP task order -- `AMGT-ww-3` -- THE TABLE'S OWN WRITER GAINS THE RESEARCH LIBRARY AS A UNIVERSE

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-ww-3</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~172</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence; the writer stays a hand-run script.
comp-iam: DECLARED-NOT-APPLICABLE for this cell (a dry-run reads only). The real write is the ISSUER's act at the drain, under a never-widen pair (COO + CTO halves) naming both branches: CREATE a row the table does not hold, PRESERVE a row it holds.
comp-adversary: RUN by the issuer at the cut -- AC1 derives the expected CREATE set live from the table, so a plan that touches a held row or misses an absent one FAILS, and it refuses an all-caps or ticker name; AC2 is the byte bound on the 36 held rows.
EGRESS CLASS, declared: NONE beyond read-only DynamoDB scan/GetItem on `etf-classifications` and S3 GET of Opal's own stored model blocks. No vendor, NO TABLE WRITE by the worker.
</preflight>

## 1. THE CELL -- `AMGT-ww-3` (round 48, decomposition s.56)

DynamoDB `etf-classifications` (us-east-1, key `ticker` = the BARE ticker) is the canonical classification table. Its writer for
single-security rows is `infra/aws/lambda/v2_portal/yang_pipeline/seed-etf-constituents.py`; its one universe today is the served
ETF positioning artifact. The research library holds 95 names (`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round48/checks/fixtures/library95.json`,
`{security_key, bare}`); at the cut the table holds 36 of the 95 bare tickers and not 59.

**Build** a second universe on that writer: `--universe amgt-library` (default `positioning`, whose behaviour must not change):
1. The universe is the LIVE research library, read with the estate's own readers: `lib.research.corpus.library.list_folders(library.library_root())`
   -> `lib.research.identity.crosswalk.harvester_key(folder, crosswalk.load_pilots())[0]` -> `lib.research.api.scoped_amgt.resolve_identity(...)["security_key"]`
   -> `scoped_amgt.read_model_block(security_key)`. Bare ticker = `security_key.split("_")[0].replace("/", "")` (`BP/_LN_Equity` -> `BP`).
   Derive the repository root at run time (never a hard-coded path) so the script runs from the root with `PYTHONPATH="$(pwd)"`.
2. Each row: `ticker` = bare; `asset_class` = `"equity"`; `sub_asset_class` = the block's own `GICS_SECTOR_NAME` figure value, as
   written; `sector` NOT written (existing values there are ETF style buckets); `management_style` = `"unknown"`; `last_updated`;
   `updated_by` = `"seed-etf-constituents --universe amgt-library (AMGT_RESAPP round 48, 2.0.0_SA_COO~Z)"`.
3. **The name.** Andrew-direct 2026-08-25 requires this table's names "properly capitalized (no all caps)", and the writer rejects
   title-casing as lossy. The block's `NAME` is ALL-CAPS ("ADVANCED MICRO DEVICES"), so for this universe the name is
   `NAME_CORRECTIONS.get(bare)` if present, else WITHHELD (the attribute is not written). Never the ticker, never a re-cased string.
4. **Write safety.** `None` and `""` values are dropped before a put (the `sub-asset-class-index` GSI refuses an empty string).
   This universe writes each row with `ConditionExpression="attribute_not_exists(ticker)"`, so a held row can never be
   overwritten, and `--force-names` with `--universe amgt-library` is refused with a message. The dry-run prints the writer's own
   `PLAN: <c> create / <u> update / <k> preserve-existing` line and one `CREATE` line per row in the existing format.
5. A block that cannot be read, or carries no `GICS_SECTOR_NAME`, is printed as `SKIP <ticker> <reason>` and never written.
6. Tests (a stubbed table and stubbed readers, the script loaded by path): the row shape, the withheld name, the condition on the
   put, the `--force-names` refusal, the SKIP branch, and the positioning universe's plan unchanged.

**Do NOT run the writer without `--dry-run`.** The real write is the issuer's.

## 2. BOUNDS

1. This one script and its tests. No other writer, no Terraform, no table write, no deploy.
2. The shared tree carries an uncommitted edit to this file by another author; you work on your own branch from `HEAD` and do
   not reproduce or depend on that edit (row `Z-S301`, the issuer's at the drain).
3. Standing: no install, no push, no promote, no vendor call. REFUSE, do not rescue.

## 3. SURFACES

<paths>
infra/aws/lambda/v2_portal/yang_pipeline/seed-etf-constituents.py
infra/aws/lambda/v2_portal/yang_pipeline/tests/**
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~172/**
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the whole repository; DynamoDB `etf-classifications`; the S3 inputs the readers above read.

## 4. PROOF OF SPEC (literal; timeout 120)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-ww-3"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round48/checks/ww-3.AC1.py; echo "exit=$?"</invocation><expect>PLAN equals the live absent/held split (59 create / 0 update / 36 preserve-existing at the cut); THE TABLE'S WRITER PLANS EXACTLY THE LIBRARY'S MISSING ROWS: YES -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-ww-3"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round48/checks/ww-3.AC2.py; echo "exit=$?"</invocation><expect>held rows compared: 36, changed: 0; THE 36 HELD ROWS ARE UNCHANGED: YES -- and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-ww-3"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" timeout 115 python -m pytest -q -p no:cacheprovider infra/aws/lambda/v2_portal/yang_pipeline/tests; echo "exit=$?"</invocation><expect>pytest reports N passed and 0 failed, N at least 6 -- and exit=0</expect></criterion>
</proof_of_spec>

AC1 the built behaviour against the real table; AC2 the bound; AC3 the branches the real table cannot exercise without a write.

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~172/AMGT_RESAPP.TO-AMGT-ww-3.the-tables-writer-gains-the-research-library.proof_of_spec.json`. Report once: what you changed and where, the dry-run's PLAN line and named/withheld counts, any SKIP, the commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round-47 analysis s.4 row 2 ("POSN's writer moves the AMGT rows under a never-widen pair that names both
branches"). Both POSN projects read `status: closed`, so this round carries the writer's edit. Base: AC1 FAIL (no `--universe`),
AC2 PASS (36 of 36 unchanged), AC3 FAIL (no tests dir). At the drain the issuer writes the COO half against the landed writer
(its dry-run over every live name), gets the CTO half, runs the real write, then `ww-3.AC3.py` (95 of 95 held; FAIL at the cut,
36) and AC2 again. Rows Z-S300 (59 names withheld) and Z-S301 (the uncommitted edit on the shared tree).

<status>pending</status>
<round>48</round>
<slot>~172</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
