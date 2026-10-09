# TO IRPT_DASHBD.TO-DB-b-67 -- E2: the activity-and-lot release's lots peak measured on the pandas 2.2.3 kit (Python 3.12, numpy 1.26.4, pyarrow 14.0.2) -- FITS or BREACH against 2,048 MB, beside 3.0.6

<to_id>IRPT_DASHBD.TO-DB-b-67</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~44</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-09</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>34</round>
<workstream>BD</workstream>

**Directive:** D9 | **Fabric:** laptop (placement DELL2) | **Ordered by:** 1.0.0_SA_CTO~DELL2's round-33 ADDENDUM 2 @47c849d75b (msg 2116, on ADJUDICATION_v18), enrichment item E2 | **Decomp cell:** `DB-b-67` (decomposition section 36) | **outcome_ref:** FWD-8 | **depends_on:** DB-b-64 (merged @9e9b3c49f2) and the kit's arrival (laptop NFRA_CTLPLN.TO-CT-k-2 AMENDMENT 10, Taildrop, ETA ~02:1xZ).

---

## WORKER FACE

Your worktree is `C:/dev/wk-irpt-dashbd-44`; run everything from its root. Your folder is
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~44/`.

**The cell (`DB-b-67`).** The activity-and-lot release (rows S31-S33) is withheld until its lots stage's peak is known on the served
pandas 2.2.3. Round 33's DB-b-64 measured that the served function `irpt-49f-reporting-gold-lambda` runs pandas 2.2.3 (layer
`irpt-performance-native-layer:1`: numpy 1.26.4, pyarrow 14.0.2) but packages no lots producer, so it cannot run the fixture (REFUSED).
Per the CTO's ruling, a Windows kit with the same versions comes from the laptop (NFRA_CTLPLN.TO-CT-k-2 AMENDMENT 10), as one zip of wheels
plus a hash-pinned requirements file.

**The kit's local path** is written by the issuer, when it lands, into
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/relay/KIT_PATH_PY312_PANDAS223.txt` (one line: the absolute path of the
zip). Read it there.

1. Extract the zip into `.scratch/kit/` and create a venv with dell2's Python 3.12
   (`C:/Users/Test/AppData/Local/Programs/Python/Python312/python.exe`) in `.scratch/venv312/`. Install OFFLINE from the kit only:
   `pip install --no-index --find-links <kit dir> -r <its pinned requirements>`. Never reach the network. If the install refuses (a
   missing wheel), stop: record the refusal and file a row.
2. In that venv, run the extended reporting-gold handler's `--local` full run over its own population for 2026-10-06 at the producer's
   default batch (`DEFAULT_BATCH_SIZE` in `data/assets/scripts/gold/irpt_reporting/account_activity_lots.py`, 1000 today). Reuse round 30's
   runner `deliverables/0.9.0_WK_IRPT_DASHBD~31/lots_750_run.py` in its `default` mode with the venv's python. Print the runtime versions
   from the run's own process.
3. Write `KIT_PEAK_E2.json`:
   - `runtime` {python, pandas, numpy, pyarrow};
   - `population_count`, `accounts_run`, `lots_stage_completed`, `batch_size`;
   - `lots_peak_mb`, `total_wall_seconds`;
   - `verdict` FITS (<= 2,048) or BREACH;
   - `reference_3_0_6_peak_mb` 1763.4 (round 30, DB-b-55), plus the kit's sha256 and the machine.

   Write `KIT_PEAK_E2.md` (COUNTS ONLY), with the 2.2.3 peak printed beside 3.0.6. The venv and the extracted kit stay in `.scratch/`,
   never committed.

<criterion id="DB34-2-AC1" cell_refs="DB-b-67"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r34/p34_round34.py" . DB34-2-AC1</invocation><expect>DB34-2-AC1 PASS</expect></criterion>
`DB34-2-AC1` -- the run's own runtime reads Python 3.12 / pandas 2.2.3 / numpy 1.26.4 / pyarrow 14.0.2, over >= 7,000 accounts at the HEAD default batch, lots completed. Base: FAIL.

<criterion id="DB34-2-AC2" cell_refs="DB-b-67"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r34/p34_round34.py" . DB34-2-AC2</invocation><expect>DB34-2-AC2 PASS</expect></criterion>
`DB34-2-AC2` -- the lots peak is printed with FITS iff <= 2,048 MB, beside the 3.0.6 reference. Base: FAIL.

<expected_criteria>DB34-2-AC1,DB34-2-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited.
- **Served output does not move.** No edit under `data/`, `infra/` or `portal/`.
- **No network.** The kit is installed offline from the delivered zip only (`--no-index`); no other download.
- **AWS:** S3 reads only unless this face says otherwise. NO Black Diamond or vendor call, no secret read, no S3 write, no deploy, no bun,
  no download of any package, script or program.
- **Refusal clause.** A vendor call, a secret read, an S3 write, a deploy, an edit outside the grant, a filled figure, or an account
  number, name or balance in a committed `.md` is a defect: stop and file a row.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~44/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-67.kit-peak.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 36 (round 34), cell `DB-b-67`.
<owned_cells>DB-b-67</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB34-2-AC1, DB34-2-AC2. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~44/IRPT_DASHBD.TO-DB-b-67.kit-peak.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB34-2-AC1,DB34-2-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** commit hashes, each criterion's last line, the runtime versions, the lots peak, the verdict, the run time, and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: project-owned reconciliation code and records; nothing served, deployed or written to S3.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: S3 reads only, from this box; no role changes.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route changes.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- DB34-2-AC1/AC2 base FAIL at base 5baf94294f (no record); positive control on a planted record PASS. The worker is spawned when the kit lands and the issuer has written its path.
lane: the <paths> block IS the grant.
</preflight>
