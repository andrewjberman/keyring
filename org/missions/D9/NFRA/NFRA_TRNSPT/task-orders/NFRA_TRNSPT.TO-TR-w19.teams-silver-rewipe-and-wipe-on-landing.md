# TO NFRA_TRNSPT.TO-TR-w19 -- W1-S7: a Teams-silver re-wipe tool + wipe-on-landing in parse_silver

<to_id>NFRA_TRNSPT.TO-TR-w19</to_id>
<project>NFRA_TRNSPT</project>
<issued_to>0.9.0_WK_NFRA_TRNSPT~2</issued_to>
<issued_by>2.0.0_SA_COO~T2</issued_by>
<issued_date>2026-10-09</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>19</round>
<workstream>communications</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Decomp cell:** `TR-w-19` (`decompositions/NFRA_TRNSPT_DECOMP_R19.md`) | **outcome_ref:** FWD-5 |
**depends_on:** none

---

## WORKER FACE

### THE CELL

`TR-w-19` (CTO ADDENDUM 8 item 2 and 8.1 item 2b, row NFRA_TRNSPT-D2-W1-S7): Teams silver is UNWIPED
(`data/transcripts/scripts/teams/parse_silver.py:5-6` "No PII wipe on transcripts this round") while PRD C-TIERS says silver is wiped. No reader is
added on teams/transcripts/* until BOTH ship: the re-wipe of existing objects (a served rewrite, under a pair, run later by the applier) and
wipe-on-landing.

**Build:**
1. `data/transcripts/scripts/teams/rewipe_silver.py` (new): lists every Teams silver key per series (auto-paginated) and, per key, re-applies the MAIL
   source's wipe (`data/transcripts/scripts/outlook/wipe.py` `wipe_blocks`, with the securities allowlist the Research fold uses,
   `research_fold.widened_assets`) to the `text` column, keeping the schema and row count and marking held-out rows the way `research_fold.py` does.
   `--dry-run` (the default) prints only the key list and per-key row counts; `--apply` writes (the applier runs it later, never you).
2. Wipe-on-landing: `parse_silver.py` runs the same wipe on `text` before writing silver (rewrite its header lines 5-6 to say so), with the
   held_out marking.
3. `data/transcripts/scripts/tests/test_rewipe_teams_silver.py` (new, fakes only): `test_dry_run_lists_every_key` (a fake S3 with 2 pages of keys:
   every key listed, nothing written); `test_rewipe_uses_mail_wipe_rule` (the function called is outlook/wipe.py's);
   `test_wipe_on_landing_planted_token` (a planted email/phone/person-name token in a synthetic WebVTT never reaches the silver text parse_silver
   writes).

### ACCEPTANCE

<criterion id="TR19-w19-AC1" cell_refs="TR-w-19"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_TRNSPT_T2/R19_CHECKS/r19_checks.py w7</invocation><expect>R19-W7-OK</expect></criterion>
`TR19-w19-AC1` -- the three named tests pass and the file is green.

<expected_criteria>TR19-w19-AC1</expected_criteria>

Dry-run at the base (box/dell2 6ab360052a): `R19-W7-FAIL absent` -- FAIL as expected.

## BOUNDS

- **Grant.** The paths below, this order's file, your deliverables folder.
- **LOCAL.** Fakes and synthetic fixtures only; no AWS, HTTP, plan or apply; no transcript, email or client content anywhere.
- **Refusal clause.** A builder refusal for a new name or address: add nothing typed; file a surprise row (`NFRA_TRNSPT-D2-W2-S<k>`, next unused across every document under `surprise-channel/`) and stop that piece.

<paths>
data/transcripts/scripts/teams/rewipe_silver.py
data/transcripts/scripts/teams/parse_silver.py
data/transcripts/scripts/tests/test_rewipe_teams_silver.py
data/transcripts/scripts/tests/test_parse_silver.py
org/missions/D9/NFRA/NFRA_TRNSPT/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant (your deliverables folder is granted by the tree convention). Everything else named here you READ.

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_TRNSPT/decompositions/NFRA_TRNSPT_DECOMP_R19.md</decomp_doc> (round 19), cell `TR-w-19`.
<owned_cells>TR-w-19</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: TR19-w19-AC1. Instance at `org/missions/D9/NFRA/NFRA_TRNSPT/deliverables/0.9.0_WK_NFRA_TRNSPT~2/NFRA_TRNSPT.TO-TR-w19.teams-silver-rewipe-and-wipe-on-landing.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> TR19-w19-AC1` BEFORE the flip. Commit code first, then pin.
</proof_of_spec>

**REPORT:** what was built and where, any address or name with its builder call, the test names, the check line, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a local build, no schedule created.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call and no grant change.
comp-adversary: RUN -- sources: CTO ADDENDUM 8 @c592051597 (+ 8.1 @3cbbddbe24), R18_COVERAGE.md @ed84ea7977 and the modules named in the face; BLIND to live data (fakes only). Traps: content in output or fixtures, a typed address, a behavior change in an existing reader; the face and the three named tests fix each.
lane: the paths block.
</preflight>

Source: CTO msgs 2938, 2946 (ADDENDUM 8, 8.1); decomposition round 19 cell TR-w-19.
