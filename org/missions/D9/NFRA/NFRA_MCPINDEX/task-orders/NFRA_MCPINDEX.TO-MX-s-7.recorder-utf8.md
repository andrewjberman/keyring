# NFRA_MCPINDEX task order -- `MX-s-7` -- the Lambda deploy recorder reads and writes the source map as UTF-8, so it stops manufacturing mojibake (row NFRA_MCPINDEX-Z-S13)

<!-- ===================== WORKER FACE -- this is the WHOLE of the seat's context for this order ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_MCPINDEX/decompositions/NFRA_MCPINDEX_DECOMP.md</decomp_doc>
<owned_cells>MX-s-7</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_MCPINDEX~6</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a reader/writer encoding repair; no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM surface.
comp-adversary: DECLARED-NOT-APPLICABLE -- an encoding repair.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `MX-s-7` (supplementary; row Z-S13, ruled by the issuer)

Row Z-S13 measured the loop: `infra/aws/lambda/ci/record-terraform-deploy.sh` reads
`lambda-source-map.json` with a bare `open()` (cp1252 on site Z), then writes it back. One U+2014 becomes three
characters on every pass, so the ASCII property MX-s-5 restored is enforced by nothing.

**Measured by the issuer at 04:4xZ:**
- The script's python heredocs hold 3 `open()` calls, and all 3 are bare: `:259` (read), `:340` (write) and `:450`
  (the native source-map read).
- Site Z takes the python path because the bun path at `:218` names another device's profile.
- Running the script's own first python block on a temp map holding one U+2014 returns 3 mojibake characters.

Do:
1. Give each of the 3 python `open()` calls `encoding='utf-8'`. Change nothing else in the script.
2. Run both criteria below.

## 2. BOUNDS

1. The one script. No data file changes and no recorder run against the real source map.
2. The hardcoded bun path at `:218` is out of scope. Do not touch it; the issuer files it separately.
3. Standing: no push. REFUSE a criterion you cannot meet as written, and report the refusal with its measurement.

## 3. SURFACES

<paths>
infra/aws/lambda/ci/record-terraform-deploy.sh
org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~6/**
org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/**
</paths>

## 4. PROOF OF SPEC (literal; run from the workspace root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="MX-s-7"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~O/round2/checks/s7.AC1.sh; echo "exit=$?"</invocation><expect>python open() calls=3 bare=0 -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="MX-s-7"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~O/round2/checks/s7.AC2.sh; echo "exit=$?"</invocation><expect>block rc=0 em-dash round-trip=intact -- RESULT: PASS -- exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the instance to
`org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~6/NFRA_MCPINDEX.TO-MX-s-7.recorder-utf8.proof_of_spec.json`.
Report once to `2.0.0_SA_COO~O`:
- the diff (3 lines);
- AC1 and AC2 literal output;
- any row.

<!-- ===================== RECORD FACE ===================== -->

# pipeline-override: supplementary repair on the issuer's ruling of row NFRA_MCPINDEX-Z-S13 (filed under MX-s-5): the deploy recorder re-arms the mojibake MX-s-5 removed; one script, same issuer, same seated lane.

**AMENDMENT A1 (2.0.0_SA_COO~O, 2026-09-27 06:4xZ):** re-pointed from 0.7.0_AE_CloudOps~I to worker 0.9.0_WK_NFRA_MCPINDEX~6. Measured: 0 of 7 live claude.exe carry the AE~I serial (control: 7 of 7 carry a serial), 0 inbox watchers, and the issuance message is unread. The seat is dead. `<paths>` and the instance path move with the assignee; no criterion changes.

**ISSUER NOTES:** Dry-run at base: s7.AC1 FAIL (calls=3 bare=3); s7.AC2 FAIL (mojibake chars=3). Positive control: a
sed-fixed copy through `RTD_FILE=` reads PASS on both. Z-S13 disarms at this order's complete flip. The seat is held on
MX-s-4 until Monday, so this order does not contend with it.

<status>pending</status>
<direct_act>true</direct_act>
<slot>~6</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>

<status>complete</status>
<!-- flipped by the issuer 2026-09-27T07:1xZ after the drain @ce2587a5e5 (worker commits 981d0e931c, f82c698bec).
     s7.AC1 PASS (calls=3 bare=0) and s7.AC2 PASS (em-dash round-trip intact) re-run on CLOUD; instance VALID (rc=0).
     Diff: 3 insertions, 3 deletions, one file. -->
