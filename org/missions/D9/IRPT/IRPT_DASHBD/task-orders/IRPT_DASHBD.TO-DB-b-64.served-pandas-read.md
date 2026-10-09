# TO IRPT_DASHBD.TO-DB-b-64 -- E2: the activity-and-lot release measured on the SERVED runtime (pandas 2.2.3) -- the deployed package and layer read; one dry_run QA invoke only if the lots producer is packaged; else the refusal measured

<to_id>IRPT_DASHBD.TO-DB-b-64</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~41</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-09</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>33</round>
<workstream>BD</workstream>

**Directive:** D9 | **Fabric:** laptop (placement DELL2) | **Ordered by:** 1.0.0_SA_CTO~DELL2's round-32 ADDENDUM 1 @78928255f6 (on ADJUDICATION_v17), enrichment item E2 | **Decomp cell:** `DB-b-64` (decomposition section 35) | **outcome_ref:** FWD-8 | **depends_on:** none open (the deployed function is live).

---

## WORKER FACE

Your worktree is `C:/dev/wk-irpt-dashbd-41`; run everything from its root. Your folder is
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~41/`.

**The cell (`DB-b-64`).** The activity-and-lot release (rows S31-S33, W27-S2, W31-S2) is withheld until the lots stage's peak memory
is known on the SERVED pandas 2.2.3. It was measured on pandas 3.0.6 (dell2: batch 1000, p95 652 s, lots peak <= 1,763 MB against
2,048 MB) and on 2.3.3. The CTO ruled: measure on the served runtime itself, not by inference from those two versions. One ad-hoc QA
invoke of the deployed function, pinned to its own layer, is permitted. If the function cannot run the fixture as served, the cell
reports the measured refusal, and only then does a 2.2.3 kit request follow (the issuer routes it).

**The served function:** `irpt-49f-reporting-gold-lambda` (us-east-1), 2,048 MB, 900 s, layer
`arn:aws:lambda:us-east-1:313476888478:layer:irpt-performance-native-layer:1`. Its declared package
(`infra/aws/lambda/ci/lambda-source-map.json`, key `irpt-49f-reporting-gold-lambda`) lists `handler.py` and
`data/assets/scripts/gold/irpt_reporting/account_return_daily.py`, but NOT `account_activity_lots.py`. The declaration is not the
deployed bytes: read the deployed artifact.

1. **Read the deployed artifact (no invoke):**
   - `.tools/aws lambda get-function-configuration` gives the code sha, last modified and layers.
   - `.tools/aws lambda get-function` gives `Code.Location`; download that zip to `.scratch/` and list its members.
   - `.tools/aws lambda get-layer-version --layer-name irpt-performance-native-layer --version-number 1` gives the layer zip; read the
     pandas version from its `pandas-*.dist-info` (or `pandas/__init__.py`).

   Write `deployed` {function, code_sha256, last_modified, layers}, `layer_pandas_version`, `packaged_modules` (the zip's .py members,
   repo-relative as packaged), and `lots_producer_packaged`.
2. **The branch rule (stated in the check before the run):**
   - **Lots producer packaged:** make ONE `.tools/aws lambda invoke` with payload `{"dry_run": true}` (dry_run is the handler's "compute
     and print, write nothing"). Read `Max Memory Used` from its REPORT line in `/aws/lambda/irpt-49f-reporting-gold-lambda`. Write
     `invoke` {dry_run: true, request_id, max_memory_used_mb, duration_ms, log_tail}, and `verdict` FITS (<= 2,048) or BREACH.
   - **Lots producer NOT packaged:** make NO invoke. `invoke` is null, `verdict` is REFUSED, and `refusal` states the measured reason
     (what the deployed package lacks, with the pandas version present). This is the measured refusal the CTO named.
3. Print the result beside the 3.0.6 and 2.3.3 figures in `SERVED_PANDAS_E2.md` (COUNTS ONLY). Write `SERVED_PANDAS_E2.json` with all
   of the above plus `files_read`. Delete the downloaded zips from `.scratch/` when done; they are never committed.

<criterion id="DB33-2-AC1" cell_refs="DB-b-64"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r33/p33_round33.py" . DB33-2-AC1</invocation><expect>DB33-2-AC1 PASS</expect></criterion>
`DB33-2-AC1` -- the deployed function, code sha, layer pandas version and packaged modules are read from the deployed artifact; lots_producer_packaged follows from the module list. Base: FAIL.

<criterion id="DB33-2-AC2" cell_refs="DB-b-64"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r33/p33_round33.py" . DB33-2-AC2</invocation><expect>DB33-2-AC2 PASS</expect></criterion>
`DB33-2-AC2` -- the branch rule holds: a packaged lots producer gives exactly one dry_run invoke with its peak and FITS/BREACH; an absent one gives no invoke and a measured REFUSED. Base: FAIL.

<expected_criteria>DB33-2-AC1,DB33-2-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited.
- **Served output does not move.** No edit under `data/`, `infra/` or `portal/`.
- **The one AWS act beyond reads:** at most ONE `lambda invoke` of `irpt-49f-reporting-gold-lambda`, with payload `{"dry_run": true}`,
  and only on the packaged branch. Never an invoke without dry_run, never a second invoke, never a configuration, code or layer change.
  The download of the deployed zips is a read of Opal's own artifact, not a package download.
- **AWS:** S3 reads only unless this face says otherwise. NO Black Diamond or vendor call, no secret read, no S3 write, no deploy, no bun,
  no download of any package, script or program.
- **Refusal clause.** A vendor call, a secret read, an S3 write, a deploy, an edit outside the grant, a filled figure, or an account
  number, name or balance in a committed `.md` is a defect: stop and file a row.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~41/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-64.served-pandas-read.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 35 (round 33), cell `DB-b-64`.
<owned_cells>DB-b-64</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB33-2-AC1, DB33-2-AC2. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~41/IRPT_DASHBD.TO-DB-b-64.served-pandas-read.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB33-2-AC1,DB33-2-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** commit hashes, each criterion's last line, the deployed sha, the layer's pandas version, the packaged modules, the branch taken and its verdict, and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: RUN -- the only act that touches the function is one dry_run invoke on the packaged branch; dry_run writes nothing (handler.py line 62: compute and print, write nothing); blast radius = one execution of irpt-49f-reporting-gold-lambda, no S3 write, no schedule change.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: dell2's identity reads Lambda config/code/layer and invokes; no role changes.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route changes.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: the daily schedule irpt-49f-reporting-gold-daily is not touched; the QA invoke is ad-hoc and is not production evidence.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- DB33-2-AC1/AC2 base FAIL at base beca8909cd (no record); positive control on a planted REFUSED record PASS (the FITS/BREACH branch is graded by the same rule, not exercised on a plant).
lane: the <paths> block IS the grant.
</preflight>
