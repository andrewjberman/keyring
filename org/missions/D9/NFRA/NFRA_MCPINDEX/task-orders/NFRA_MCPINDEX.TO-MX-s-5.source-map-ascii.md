# NFRA_MCPINDEX task order -- `MX-s-5` -- the Lambda source map goes ASCII, so step 7 of the canonical Lambda deploy runs on site Z (row NFRA_MCPINDEX-Z-S12)

<!-- ===================== WORKER FACE -- this is the WHOLE of the seat's context for this order ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_MCPINDEX/decompositions/NFRA_MCPINDEX_DECOMP.md</decomp_doc>
<owned_cells>MX-s-5</owned_cells>
</decomp_ref>
<issued_to>0.7.0_AE_CloudOps~I</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a data-file and reader repair; no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM surface.
comp-adversary: DECLARED-NOT-APPLICABLE -- an encoding repair.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `MX-s-5` (supplementary; your own row Z-S12, ruled by the issuer)

**Measured by the issuer at 10:5xZ:** `infra/aws/lambda/ci/lambda-source-map.json` (288,159 bytes) holds 23 non-ASCII
characters. They are mojibake: a dash encoded twice (e.g. `Container image \xc3\x83\xc2\xa2... CI updates`, at byte
32218). `infra/aws/lambda/ci/record-terraform-deploy.sh` (step 7 of the canonical Lambda deploy) reads the file with the
default code page and raises UnicodeDecodeError there. That is your row Z-S12, from MX-s-3.

CLAUDE.md's rule for a file carrying non-ASCII: the only safe moves are ALL non-ASCII out, or EVERY reader explicit
UTF-8, never a subset. This order takes the first.

Do:
1. Replace each of the 23 characters with the ASCII text it was meant to be (the mojibake dashes become `--`). List
   each one, with its key, in your result. Change nothing else in the file; it must still parse as JSON.
2. Census the file's WRITERS (`comp-find` for its name), and say which one wrote the mojibake, if the history shows it.
   If a writer will re-introduce non-ASCII, file one row naming it. Do not fix other tools here.
3. Re-run MX-s-3's step-7 record with the recorder itself, not by hand, and show it exits 0.

## 2. BOUNDS

1. The one data file, plus the recorder re-run. No other file changes.
2. Standing: no push. REFUSE a criterion you cannot meet as written, and report the refusal with its measurement.

## 3. SURFACES

<paths>
infra/aws/lambda/ci/lambda-source-map.json
org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.7.0_AE_CloudOps~I/**
org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/**
</paths>

## 4. PROOF OF SPEC (literal; run from the workspace root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="MX-s-5"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~O/round2/checks/s5.AC1.sh; echo "exit=$?"</invocation><expect>nonascii_chars=0 json=ok -- RESULT: PASS -- exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the instance to
`org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.7.0_AE_CloudOps~I/NFRA_MCPINDEX.TO-MX-s-5.source-map-ascii.proof_of_spec.json`.
Report once to `2.0.0_SA_COO~O`:
- the 23 replacements;
- the writer census;
- the recorder re-run exit;
- any row.

<!-- ===================== RECORD FACE ===================== -->

# pipeline-override: supplementary repair on the issuer's ruling of row NFRA_MCPINDEX-Z-S12 (filed under MX-s-3): step 7 of the canonical Lambda deploy cannot run on site Z while the shared source map carries mojibake; one data file, same issuer, same seated lane.

**ISSUER NOTES:** Queued on 0.7.0_AE_CloudOps~I AFTER MX-s-3 closes (step 3 of this order re-runs MX-s-3's record) and
before or beside MX-s-4. Dry-run at base: s5.AC1 FAIL (nonascii_chars=23 json=ok).

<status>pending</status>
<direct_act>true</direct_act>
<slot>~I</slot>
<fabric>site-z</fabric>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
