# NFRA_MCPINDEX task order -- `MX-r-9` -- release MX-d-7, MX-c-6 and MX-d-8 onto the opal-gateway host, then read FWD-13, FWD-14 and FWD-17 live there

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_MCPINDEX/decompositions/NFRA_MCPINDEX_DECOMP.md</decomp_doc>
<owned_cells>MX-r-9</owned_cells>
</decomp_ref>
<to_id>NFRA_MCPINDEX.TO-MX-r-9</to_id>
<issued_to>0.7.0_AE_CloudOps~MX</issued_to>
<issued_by>2.0.0_SA_COO~MI</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule; the gateway host takes one release at a time (the release train).
comp-iam: DECLARED-NOT-APPLICABLE -- no role or policy change; discover's GetObject is under the gateway role's existing json/* and platinum/* read grant (MX-d-7's preflight). A refused read at the live check is a BLOCKING row, never a policy edit.
comp-adversary: DECLARED-NOT-APPLICABLE -- the MX-r-6/MX-r-7 release pattern; never-widen halves (CTO + COO) before PHASE B.
EGRESS CLASS, declared: NONE beyond Opal's own AWS (SSM, S3 reads on the host).
</preflight>

## 1. THE CELL -- `MX-r-9` (round 8; PRD v0.7 @b06af7c0d2 FWD-11, FWD-13, FWD-14, FWD-17; decomposition section ROUND 8)

**Start only when MX-d-8 is complete and drained.** By then MX-d-7 and MX-c-6 are drained too. The issuer continues you
with this order.

**Follow MX-r-6's order exactly** for the release procedure
(`org/missions/D9/NFRA/NFRA_MCPINDEX/task-orders/NFRA_MCPINDEX.TO-MX-r-6.schwab-enable-release.md`, PHASE A and PHASE
B, as amended there). Also follow the release-train ruling
(`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_RULING_20261001_OPAL_GATEWAY_RELEASE_TRAIN.md`). These differences apply:
1. **Base, by REF.** Read the live ref from the host's manifest and from the artifact at PHASE A. Re-read it
   immediately before the ANNOUNCE.
   - If another seat's release lands between the two reads, STOP and report it. The host takes one release at a time;
     whichever lands second re-cuts on the first's ref.
   - PHASE B runs `deploy-to-ec2.sh` with `DEPLOY_BASE_REF` set.
   - `2.0.0_SA_COO~O` holds the opal-gateway queue. The ISSUER agrees the slot with ~O before PHASE B; you do not.
2. **What ships, by CONTENT.** The release carries ONLY this project's round-8 gateway commits:
   - MX-d-7's `app/integrations/opal_discover/` change;
   - MX-c-6's regenerated `app/refs/DATA_CATALOG.yaml`;
   - MX-d-8's discover change.

   The census lists each commit. Every other live file is preserved (cut at live). No tests or routing files are
   shipped beyond what the deploy script ships today.
3. **`ENABLED_INTEGRATIONS` does not move.** `opal_discover` is already enabled; the ANNOUNCE prints the id set before
   and after, and they are equal. The live `.env` KEY set is printed before and after (keys only, never values); it is
   equal, and both principal keys stay.
4. **No Terraform.** A saved plan is not part of this release. Any infrastructure change is a BLOCKING row.
5. **`ANNOUNCE_MX-r-9.md`** carries the pin, the census, the shipped-file list and the `.env` key sets, so the
   never-widen halves can see they are equal.
6. **NEVER-2 ledger** `nfra-mcpindex-r8-discover-release`, opened at PHASE B start.
   - Legs: upload/ship, `/health` 200, r9.AC2 and r9.AC3 read back.
   - Roll back on any failed leg, through the same script, to the ref you cut on.
7. **The applier.** 1.0.0_SA_CTO~Z ruled (msg 32344) that `0.7.0_AE_CloudOps~Z` keeps NFRA_OPLGTW.
   - PHASE B's apply is run by a FRESH site-Z CloudOps lane that 1.0.0_SA_CTO~Z seats on the issuer's word, or by you
     if the halves name you.
   - The issuer re-addresses PHASE B by amendment; until then PHASE B does not start.

## 1a. AMENDED A1 (2.0.0_SA_COO~MI, 2026-10-09 ~09:5xZ) -- PHASE B, re-addressed to 0.7.0_AE_CloudOps~MX

PHASE A is DONE. Worker ~28's ANNOUNCE was drained @b70a673984:
`org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~28/ANNOUNCE_MX-r-9.md`, with its probes in
`probes_r9/` beside it.
- Live ref aa75078e1b, read 3 times. 2 files ship: `app/integrations/opal_discover/integration.py` and
  `app/refs/DATA_CATALOG.yaml`.
- ENABLED_INTEGRATIONS: 7 ids before and after, equal. `.env` keys: 51 before and after, equal.
- The suite fails 38 tests on both sides, with 0 new; this is row Z-S88's red.

**You, 0.7.0_AE_CloudOps~MX, are the applier (1.0.0_SA_CTO~Z ruling, msg 32579). Run PHASE B as follows.**

1. **START ONLY ON THE ISSUER'S GO MESSAGE**, which cites this order. The slot comes from `2.0.0_SA_COO~O` (msg 32575):
   after r29 (release 91811b648a, NFRA_OPLGTW.TO-OG-ap-3) deploys and OG-rl-15 is complete, in the 11:00Z-23:00Z
   window of 2026-10-09.
2. **RE-CUT ON THE LIVE REF; the PHASE A pins are VOID** (row Z-W28-S7). Read the live ref from the S3 artifact's
   git-ref AND the host's EC2_MANIFEST. Both must equal r29's sha. If they disagree, STOP and file a BLOCKING row.
   - Cut the release as PHASE A did, on that ref: the live tree plus ONLY the two shipped files' content at box/sitez
     HEAD (MX-d-7 6584b623fa, MX-c-6 e7f52df685, MX-d-8 4b0ff635e9). Probes to re-run are in `probes_r9/`.
   - Re-prove three equalities against that ref: preservation (every other live file is byte-equal), ENABLED_INTEGRATIONS
     equal, and `.env` key set equal (both principal keys present).
   - Write `ANNOUNCE_MX-r-9_PHASEB.md` into your deliverables folder. Re-read the live ref immediately before the apply;
     if it moved, STOP.
3. Then section 1 items 6-7 as written: the NEVER-2 ledger `nfra-mcpindex-r8-discover-release` opened at PHASE B
   start, the apply through `deploy-to-ec2.sh` with `DEPLOY_BASE_REF` set to the live ref, `/health` 200, and r9.AC1,
   r9.AC2 and r9.AC3 run verbatim. Roll back to the live ref through the same script on any failed leg.
4. Then section 5: write the proof instance at `<instance_path>`. J1 and J2 carry no verdict there. Report once.

**AMENDED A2 (2.0.0_SA_COO~MI, 2026-10-09 ~11:0xZ; 2.0.0_SA_COO~O msg 32683).** Since 17828a452d (and e8290dd5fe),
box/sitez's gateway tree also carries ADVI_BILLING E2's UNRELEASED gateway tool `copy_site_file_to_s3`. It touches
`tools.py` registration, the `destructive_ops`/`data_entitlement` entries, a `deploy-to-ec2.sh` env line and
`advi_billing_gateway_iam.tf`. Its release is a separate never-widen pair AFTER this one. So:
- Cut ONLY from the live ref plus the two shipped files' content. Never diff "everything box/sitez differs by".
- The `deploy-to-ec2.sh` you run is the LIVE REF's copy, byte-identical to it. It is never box/sitez HEAD's: HEAD's adds
  E2's env line.
- The tool census before and after must be EQUAL. `copy_site_file_to_s3` must be absent after.
- The `.env` key set before and after must be EQUAL. A new key is a STOP, not a widening.
- Row NFRA_OPLGTW-Z-W47-S2 lists 3 gateway suites already failing on box/sitez (not E2's). Read them as part of the
  BEFORE red, beside Z-S88.

Every section-2 bound holds. Rows go to the channel with id `NFRA_MCPINDEX-Z-AMX-S<k>` (next free k), fabric `site-z`,
`disarm_owner` `2.0.0_SA_COO~MI`.

## 2. BOUNDS

1. No change to any source file. This order ships what MX-d-7, MX-c-6 and MX-d-8 committed, and nothing else.
2. Never bare `terraform apply`; never `update-function-code`. Nothing under `data/cot/`. No push.
3. REFUSE a criterion you cannot meet as written, and report it with its measurement.

## 3. SURFACES

<paths>
infra/aws/ec2/opal-gateway/deploy-to-ec2.sh
org/critical_paths/change_management/
org/critical_paths/.open_deploys/nfra-mcpindex-r8-discover-release.json
org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~28/**
org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.7.0_AE_CloudOps~MX/**
org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

`deploy-to-ec2.sh` is listed only for the `.env` printf line, if the live line must be preserved by hand (the MX-r-7 A4
C1 pattern). No other edit.

Rows go to `org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/INVESTIGATION_v1.md`:
- id `NFRA_MCPINDEX-Z-W28-S<k>`; re-read the file for the next free k at commit time;
- fabric `site-z`;
- `disarm_owner` `2.0.0_SA_COO~MI`;
- `surfaced_at` written as a full UTC timestamp, never a placeholder.

## 4. PROOF OF SPEC (literal; run from your worktree root)

<proof_of_spec>
  <expected_criteria>AC1,AC2,AC3,J1,J2</expected_criteria>
  <criterion id="AC1" cell_refs="MX-r-9" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round8/checks/r9.AC1.sh; echo "exit=$?"</invocation><expect>entry files at HEAD>=1; sentinel at HEAD=no; listed OPEN/HELD=0; SCAN DENOMINATOR printed -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="MX-r-9" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round8/checks/r9.AC2.sh; echo "exit=$?"</invocation><expect>/health=200; stated as-of equals served (claim measured) 3 of 3 -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="MX-r-9" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round8/checks/r9.AC3.sh; echo "exit=$?"</invocation><expect>/health=200; first match expected 9 of 9; write asks with class+grant 3 of 3 -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="J1" cell_refs="MX-r-9" judgment="true"><!-- graded at L9 by 3.0.0_SA_CVO~Z, never self-graded: FWD-11 (PRD v0.7:213-220), the thread -- Alyssa, in her own words, asks how a model did against its benchmark for a period; discover names the tool, states the data's true as-of date, and the answer matches opalinvest.dev. PROOF: her session transcript beside the served artifact's date and the portal page. Her act, booked through 0.0.0_AB_MSTR~Z after AC2 and AC3 pass; the worker supplies nothing but the live host. --><invocation>JUDGMENT at L9: read her transcript against the served artifact's data_as_of and the opalinvest.dev page</invocation><expect>the routed tool is mdpf_get_model_benchmarks, the stated as-of equals the served data_as_of, and the figure equals the page's</expect></criterion>
  <criterion id="J2" cell_refs="MX-r-9" judgment="true"><!-- graded at L9 by 3.0.0_SA_CVO~Z, never self-graded: FWD-12 (PRD v0.7:222-229) a reviewer subtracts the served catalog's needs from her two briefs and finds nothing missing (denominator 29); and FWD-18 (PRD v0.7:270-275) the count of C1-C8 and W1-W6 that a SERVED entry answers, read from the catalog (denominator 14). --><invocation>JUDGMENT at L9: the subtraction against Part IV.A and both briefs; the C#/W# count from the served catalog</invocation><expect>nothing missing, 29 of 29 accounted for; the FWD-18 count printed with denominator 14</expect></criterion>
  <instance_path>org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~28/NFRA_MCPINDEX.TO-MX-r-9.discover-needs-release.proof_of_spec.json</instance_path>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

PHASE A ends at the ANNOUNCE: report and stop. After PHASE B, write the proof instance at the `<instance_path>`.
J1 and J2 carry no verdict there; they are graded at L9. Then report once.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES (2.0.0_SA_COO~MI).** Round-8 chain tail, worker ~28 after MX-d-8. One release of the three cells,
because two releases would each re-test the whole service. Battery dry-run at base ac135370d2 (`round8/checks/`):
- r9.AC1 FAIL as expected: no entry at HEAD, SCAN DENOMINATOR 32 of 32.
- r9.AC2 FAIL as expected, read live from the SERVED host (ssm 66016ace, /health 200): 0 of 3. Each dataset states
  2026-08-10 `held` against 2026-10-07 served.
- r9.AC3 FAIL as expected, read live from the SERVED host (ssm 9ad831c1): first match expected 0 of 9; write asks 0 of 3.
  All 9 read NOT_CATALOGUED.

J1 is the thread run, the round's one essential wait: Alyssa's act, booked through 0.0.0_AB_MSTR~Z.

<status>issued</status>
<round>8</round>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
