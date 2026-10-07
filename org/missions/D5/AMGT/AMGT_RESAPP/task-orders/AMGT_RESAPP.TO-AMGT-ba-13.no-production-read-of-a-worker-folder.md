# AMGT_RESAPP task order -- `AMGT-ba-13` -- PRODUCTION CODE NO LONGER READS A WORKER'S DELIVERABLES FOLDER (ROW Z-W37-S2)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-ba-13</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~279</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence; file homes and the lines that read them.
comp-iam: DECLARED-NOT-APPLICABLE -- no new S3 address is read or written; an object already in S3 keeps its address.
comp-adversary: RUN by the issuer at the cut -- r77_ba13 AC1 at the base: C1 FAIL (19 production files under lib/, 44 lines, name a worker folder), C2 FAIL (the two packaging scripts, 3 lines), C3 control PASS (the five integrations/bloomberg files).
EGRESS CLASS, declared: NONE. No vendor, SEC or model call.
</preflight>

**Your worktree:** `C:/tmp/r77-279` (branch `wk-AMGT_RESAPP-279`, cut from the issuer's tree AFTER every other cell of round 77 has drained, with `--portal-ref 13509c52`, the portal DEV head at the cut (the api suite reads a portal fixture)). Work and commit only there. Start every shell call with `cd /c/tmp/r77-279`: a call that starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout.

## 1. THE ACT -- `AMGT-ba-13` (round 77, decomposition s.85)

Row Z-W37-S2, ruled by the issuer (`deliverables/2.0.0_SA_COO~Z/round76/COO_ADJUDICATION_REMEDIATION_ROWS_ROUND76.md` @fb9ca91ad5,
section B): **a worker's deliverables folder is a record, not a data home.** Production code under `lib/` still names
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~<n>/` in 19 files. You run LAST in the round because these
files belong to other cells' surfaces; they have all drained into your base.

**The census at the cut** (file: lines naming a worker folder; re-run it first and work from YOUR base's lines):

| file | lines | what the line is |
|---|---|---|
| lib/research/identity/coverage_pass.py | 9 | reads ~3 universe.json and ~9 sa_ids.json; writes ~4 universe.json and RESIDUAL_REPORT.md |
| lib/research/identity/crosswalk.py | 4 | the coverage source path (~4) and provenance text |
| lib/research/identity/build_universe.py | 2 | writes ~3 universe.json |
| lib/research/coverage/run_reader.py | 3 | reads ~9, writes under ~3 |
| lib/research/coverage/run_sa_reexercise.py | 2 | writes under ~2 |
| lib/research/drafting/run_drafting.py | 3 | writes a drafted-sections file under ~3; reads a ~1 model block |
| lib/research/social/collect.py | 3 | two folder paths (~19, ~22) and a generated_by string |
| lib/research/freshness/build_view.py | 2 | reads ~3 universe.json; a ~7 coverage_freshness.json path |
| lib/research/metrics/chatter_axis.py | 2 | reads ~4 universe.json |
| lib/research/peers/universe.py | 2 | a ~1 folder path |
| lib/research/peers/engine.py | 1 | reads ~4 universe.json |
| lib/research/posture/packs.py | 2 | reads ~1 model_block_<key>.json |
| lib/research/posture/fit.py | 1 | reads ~21 scanner_factor_metadata.json |
| lib/research/provenance/render_print.py | 1 | a ~1 folder path |
| lib/research/price/backfill_legacy_generation.py | 1 | docstring (a record copy under ~6) |
| lib/research/price/generation.py | 1 | docstring (who surfaced a row) |
| lib/research/rules/figure.py | 1 | comment (the original path of packaged data) |
| lib/research/lists/build_lists.py | 1 | an `added_by` value |
| lib/research/lists/impostor.py | 1 | docstring |

Packaging, which must move in step (2 files, 3 lines): `infra/aws/terraform/harvest/build-and-upload-scoped-amgt.sh:219,222`
(packages `~5/lists/publishers.json` and `social_accounts.json`) and `infra/aws/terraform/harvest/lambda_src/build_zip.py:107`
(packages `~4/universe.json`).

**NOT touched, and listed so nobody chases them:** five production files under `integrations/bloomberg/` name a worker folder
(`auth/bbg_credentials.py`, `research/build_unit_map.py`, `research/derive_fye_fixed.py`, `research/price_axis_pull.py`,
`research/pull_baba_daily_px.py`). Andrew's no-modify order on `integrations/bloomberg/` stands. `price_axis_pull.py` READS
`~4/universe.json` and writes under `~6`, so **every file a worker folder holds today STAYS where it is**: you COPY, you never
move or delete.

**What to do, per line.**
1. **A READ of a data file** (universe.json, sa_ids.json, model_block_<key>.json, scanner_factor_metadata.json, the two list
   files): the file gets a canonical home and the code reads it from there.
   - If the same object is already in S3 at a `lib/opal_naming.py address()` home and the module already has a reader for it,
     use that reader.
   - Otherwise it becomes a package data file beside the module that owns it (a `data/` folder in that package, as
     `lib/research/rules/data/` already does), with a one-line `_source` note of where it came from. Copy the bytes; the copy is
     byte-equal to the original at your base.
   - One home per file: two modules that read the same file read the same copy.
2. **A WRITE into a worker folder** by a producer script: the output's home becomes the same canonical home its readers now use
   (or, for a report nobody reads, the producer's own package `out/` path given on the command line with no default into a
   worker folder).
3. **A comment, docstring or provenance string**: reword it so it no longer spells the folder (for example "the round-N worker
   deliverable, see git history"), keeping its meaning. A stored provenance VALUE that other code compares against is a READ:
   treat it under 1 and say so.
4. **The two packaging scripts** package from the new home.

**Equality, before any edit.** Write `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~279/equal_reads.py`. It
loads, through each module's OWN loader, every object whose read you move (at least: the crosswalk document and its 237
records' keys, the peers universe, the posture model block for BA_US_Equity, the scanner factor metadata, the freshness
universe, the two list files) and prints a sha256 per object. Run it at your base into `before/reads.json`. After your edits it
prints `EQUAL n of n` against that file. A loader that needs AWS reads only; no write.

Run `lib/research/` tests for every package you touch before your commit and report each last line. If one api test fails only because it reads a portal function absent at this worktree's portal ref, name it in your report and file no row; the issuer grades the suite on the shared tree. **Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing.** Rows: id form `AMGT_RESAPP-Z-W279-S<k>`, `disarm_owner` `2.0.0_SA_COO~Z`.

## 2. BOUNDS

1. Write only the paths below. No deploy, no store write, no table, no schedule, no vendor, SEC or model call, no portal write.
2. NO file under `org/missions/` other than your own deliverables is moved, edited or deleted. Nothing under `integrations/bloomberg/` is edited.
3. No served value changes: every moved read returns the same object (AC2).
4. A line you cannot move without changing behaviour is a row naming the file, the line and why; the count then reads what is left, and you say so. Do not force the count to 0 by deleting a read.
5. Standing: no S3 delete, no push of shared branches.

## 3. SURFACES

<paths>
lib/research/identity/
lib/research/coverage/
lib/research/drafting/
lib/research/social/
lib/research/freshness/
lib/research/metrics/
lib/research/peers/
lib/research/posture/
lib/research/provenance/
lib/research/price/
lib/research/rules/
lib/research/lists/
infra/aws/terraform/harvest/build-and-upload-scoped-amgt.sh
infra/aws/terraform/harvest/lambda_src/build_zip.py
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~279/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 3600)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-ba-13"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round77/checks/r77_ba13.py" --crit AC1 --where local; echo "exit=$?"</invocation><expect>0 production files under lib/ name a worker folder (19 at the cut); the two packaging scripts name none; the integrations/bloomberg list is the same five; C1-C3 PASS; R77 BA13 AC1 SERVED: YES; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-ba-13"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~279/equal_reads.py"; echo "exit=$?"</invocation><expect>EQUAL n of n with n at least 8; and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~279 <0.9.0_WK_AMGT_RESAPP~279@opal.agent>" -F <msgfile> -- <paths>`
(message file written with the Write tool; confirm with `git log -1`). Instance at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~279/AMGT_RESAPP.TO-AMGT-ba-13.no-production-read-of-a-worker-folder.proof_of_spec.json`.
Run `python .tools/proof-of-spec-check.py <instance>` on the committed bytes and report its verdict line. Do not stage `portal`.
Report once:
- the commit hash;
- every criterion's output lines;
- a table: each moved file, its old path, its new home, and who reads it;
- the test suites you ran and each last line;
- every line you could not move, with its row;
- what the next redeploy's package now carries from a new path;
- any row.

The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** RISK is WORLD by the gate's path floor only (two packaging scripts under `infra/`); it applies nothing. STAGED until ba-20 (the redeploy) closes: it changes what the Lambda package reads from, so it rides the NEXT redeploy with its own content-diff, never this one. CTO round-76 analysis item 10 (the COO's own cell); COO adjudication @fb9ca91ad5 section B, row Z-W37-S2. Wave 2, last: its write surface spans other cells' packages, so it is cut after they drain (dispatch Step 1: a batch cell that touches many cells' files runs last). The row's own census counted 24-25 files across `lib/`, `integrations/` and `infra/`; at the cut that is 19 under `lib/`, 5 under `integrations/bloomberg/` (untouched) and 2 packaging scripts. It changes what the Lambda package reads from, so it lands AFTER this round's redeploy or rides the next one with its own content-diff; it never rides a deploy silently. Checks dry-run at the base: ba-13 AC1 base FAIL as expected (control C3 PASS); AC2 is the worker's own script (absent at the base, FAIL as expected).

<status>staged</status>
<round>77</round>
<slot>0.9.0_WK_AMGT_RESAPP~279</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
