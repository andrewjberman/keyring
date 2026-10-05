# AMGT_RESAPP task order -- `AMGT-av-3` -- THE DRIVER-CHART POINTS SERVE THEIR PASSAGES (FWD-18)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-av-3</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~239</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence; request-time code and tests only.
comp-iam: DECLARED-NOT-APPLICABLE for this cell -- the route reads the drafting document it already reads. The drafting REBUILD is av-8's store-write leg under a pair.
comp-adversary: RUN by the issuer at the cut -- r72 c42 FAILS on deployed: 0 of 6 driver-chart points (BA P0276-8, ASML P0086 x3) serve passage text.
EGRESS CLASS, declared: NONE. No vendor or model call; stored inputs only.
</preflight>

**Your worktree:** `C:/tmp/r72-239` (branch `wk-AMGT_RESAPP-239`, cut from the issuance commit). Work and commit only there. Start every shell call with `cd /c/tmp/r72-239`: a call that starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout.

## 1. THE ACT -- `AMGT-av-3` (round 72, decomposition s.80)

PRD v0.39 FWD-18 DONE WHEN (PRD `:660-661`): a filing figure is clicked through to its passage.

The route `thesis_driver_chart` (`lib/research/api/scoped_amgt.py` ~`:3395-3418`) serves each point's `passage_id` but no text. The
drafting document's `evidence_records` lack those ids (BA has 86 records, ASML 11; only the driver's source passages are present), so
the page finds nothing.
1. **Producer:** `lib/research/filings/drafting_build.py` (~`:233-264`) adds every driver-chart point's passage to
   `evidence_records`, built from the stored filing text it already reads.
2. **Route:** each point with a `passage_id` serves `passage_text` (and its cite) from the drafting document; a point whose passage
   cannot be found serves a plain `passage_reason`.
3. **Plant tests:** `lib/research/filings/test_driver_point_passages.py` and `lib/research/api/tests/test_driver_chart_passage.py`.
4. **Dry build, no write:** build BA's and ASML_NA's drafting documents in memory with the new producer and print, per name, the
   points and points whose passage resolves. Save it as `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~239/dry_build_passages.txt`. **Name the exact store keys a rebuild
   would write** (for av-8's pair).

Run `lib/research/api/tests/` before your commit and report its last line. If one api test fails only because it reads a portal function absent at this worktree's portal ref, name it in your report and file no row; the issuer grades the suite on the shared tree. **Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing.** Rows: id form `AMGT_RESAPP-Z-W239-S<k>`, `disarm_owner` `2.0.0_SA_COO~Z`.

## 2. BOUNDS

1. Write only the paths below. No deploy, no store write, no table, no schedule, no vendor or model call, no portal write.
2. NO drafting or store write (the rebuild is av-8's). No other evidence record changes.
3. Any reason you serve is in plain words. Do not use identity, unresolved, security key, crosswalk, dossier, landed, model block, estate, stage or input ledger.
4. Standing: no S3 delete, no push of shared branches.

## 3. SURFACES

<paths>
lib/research/filings/drafting_build.py
lib/research/filings/test_driver_point_passages.py
lib/research/api/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~239/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 1800)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-av-3"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python -m pytest -v -p no:cacheprovider lib/research/filings/test_driver_point_passages.py lib/research/api/tests/test_driver_chart_passage.py; echo "exit=$?"</invocation><expect>every plant case passes; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-av-3"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; cat "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~239/dry_build_passages.txt"; echo "exit=$?"</invocation><expect>BA points 3 resolved 3 and ASML_NA points 3 resolved 3, the store keys a rebuild writes named; and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~239 <0.9.0_WK_AMGT_RESAPP~239@opal.agent>" -F <msgfile> -- <paths>`
(message file written with the Write tool; confirm with `git log -1`). Instance at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~239/AMGT_RESAPP.TO-AMGT-av-3.driver-chart-passages.proof_of_spec.json`.
Run `python .tools/proof-of-spec-check.py <instance>` on the committed bytes and report its verdict line. Do not stage `portal`.
Report once:
- the commit hash;
- every criterion's output lines;
- the filings and api suites' last lines;
- the store keys a rebuild writes;
- any row.

The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** CTO round-71 analysis item 3b; rows Z-W235-S3. The rebuild is av-8's leg; c42 grades on deployed after it.

<status>pending</status>
<round>72</round>
<slot>0.9.0_WK_AMGT_RESAPP~239</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
