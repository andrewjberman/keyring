# TO NFRA_TRNSPT.TO-TR-i19 -- FWD-6: market-update intake, byte-exact, re-saved copy recognised

<to_id>NFRA_TRNSPT.TO-TR-i19</to_id>
<project>NFRA_TRNSPT</project>
<issued_to>0.9.0_WK_NFRA_TRNSPT~4</issued_to>
<issued_by>2.0.0_SA_COO~T2</issued_by>
<issued_date>2026-10-09</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>19</round>
<workstream>communications</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Decomp cell:** `TR-i-19` (`decompositions/NFRA_TRNSPT_DECOMP_R19.md`) | **outcome_ref:** FWD-6 |
**depends_on:** none

---

## WORKER FACE

### THE CELL

`TR-i-19` (CTO ADDENDUM 8 item 5; PRD FWD-6 "someone places a market update and later gets back the identical deck; a re-saved copy is
recognisable as the same deck"): no act exists (coverage row FWD-6).

**Build:**
1. `data/transcripts/scripts/updates/intake.py` (new package `updates/`): `place(path, *, s3, apply)` lands the file's bytes unchanged at a bronze
   address from `address()` (series `market_update`; a builder refusal = a row, nothing typed) with a sidecar `{sha256, size, original_name,
   placed_at, deck_fingerprint}`; `get(key)` returns the exact bytes; `deck_fingerprint(bytes)` = sha256 over the ordered slide TEXT of the .pptx
   (python-pptx if installed, else the zip's `ppt/slides/slideN.xml` text nodes via zipfile), so a re-saved copy with new container bytes matches.
2. `data/transcripts/scripts/tests/test_market_update_intake.py` (new, synthetic .pptx built in the test): `test_lands_byte_exact_with_sha256`;
   `test_resaved_copy_recognised` (same slides, re-zipped with different metadata -> same fingerprint, different sha256);
   `test_different_deck_not_matched`.

### ACCEPTANCE

<criterion id="TR19-i19-AC1" cell_refs="TR-i-19"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_TRNSPT_T2/R19_CHECKS/r19_checks.py i6</invocation><expect>R19-I6-OK</expect></criterion>
`TR19-i19-AC1` -- the three named tests pass and the file is green.

<expected_criteria>TR19-i19-AC1</expected_criteria>

Dry-run at the base (box/dell2 6ab360052a): `R19-I6-FAIL absent` -- FAIL as expected.

## BOUNDS

- **Grant.** The paths below, this order's file, your deliverables folder.
- **WORLD by path floor (a registry row), LOCAL in act.** Fakes and synthetic fixtures only; no AWS, HTTP, plan or apply; no transcript, email or client content anywhere.
- **Refusal clause.** A builder refusal for a new name or address: add nothing typed; file a surprise row (`NFRA_TRNSPT-D2-W4-S<k>`, next unused across every document under `surprise-channel/`) and stop that piece.

<paths>
data/transcripts/scripts/updates/__init__.py
data/transcripts/scripts/updates/intake.py
data/transcripts/scripts/updates/NAMES.json
data/transcripts/scripts/tests/test_market_update_intake.py
infra/logic/registry/series.json
org/missions/D9/NFRA/NFRA_TRNSPT/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant (your deliverables folder is granted by the tree convention). Everything else named here you READ.

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_TRNSPT/decompositions/NFRA_TRNSPT_DECOMP_R19.md</decomp_doc> (round 19), cell `TR-i-19`.
<owned_cells>TR-i-19</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: TR19-i19-AC1. Instance at `org/missions/D9/NFRA/NFRA_TRNSPT/deliverables/0.9.0_WK_NFRA_TRNSPT~4/NFRA_TRNSPT.TO-TR-i19.market-update-intake.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> TR19-i19-AC1` BEFORE the flip. Commit code first, then pin.
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

Source: CTO msgs 2938, 2946 (ADDENDUM 8, 8.1); decomposition round 19 cell TR-i-19.
