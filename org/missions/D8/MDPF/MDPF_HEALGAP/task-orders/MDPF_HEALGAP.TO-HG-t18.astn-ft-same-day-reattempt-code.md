# TO MDPF_HEALGAP.TO-HG-t18 -- round 5 HG-t-18: the ASTN FT same-day re-attempt, the code half (run.py, store.py, the orchestrator Lambda's new mode)
<to_id>MDPF_HEALGAP.TO-HG-t18</to_id>
<project>MDPF_HEALGAP</project>
<issued_to>0.9.0_WK_MDPF_HEALGAP~15</issued_to>
<issued_by>2.0.0_SA_COO~G1</issued_by>
<issued_date>2026-10-13</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>5</round>
**Directive:** D8 | **Fabric:** laptop (placement dell1) | **Decomp cell:** `HG-t-18` (`decompositions/MDPF_HEALGAP_DECOMP.md`, ROUND 5) |
**outcome_ref:** FWD-6 (D1-W14-S3), CTO round-4 analysis item 1 | **depends_on:** none

---

## WORKER FACE

### THE CELL

`HG-t-18`. The ASTN morning brief (`tools/astn_wsjft/scripts/run.py`) fetches WSJ and FT at 3 AM ET. When the FT fetch raises, the run
degrades to WSJ-only: `run()` writes a warning that starts `FT fetch failed`, the brief is sent without FT, and nothing ever refills the day (the
12-hour freshness window drops the missed window on later runs). This cell adds the FT-only re-attempt that the CTO ruled
(`ledger/ROUND_ANALYSIS.round4.md` section 2, D1-W14-S3): a second, later invocation that fetches FT only, widens the window ONLY to "since the
last successful run", sends ONLY articles no earlier digest already carried, and does nothing on a complete day. **This is the CODE half.** The
schedule resource that invokes it is NOT in this cell (no Terraform at all): its name waits on a registry row the CTO has routed.

**The estate, read at the base.**
- `tools/astn_wsjft/scripts/run.py`: `run()` runs refresh-holdings, fetch WSJ, fetch FT (a raise becomes the warning
  `FT fetch failed (session expired? -> run harvest_ft_session): ...`), `_fresh` 12 h, `analyze.analyze_all`, `store.put_digest(date, digest)`,
  `compile_email.render`, `store.put_email`, `send_ses.send(html, date)`, `store.discard_raw(date)`. The digest is
  `{"by_section": {section: [article, ...]}, "total_articles_in", "total_articles_out", "warnings": [...], "date"}`; each article carries `url`.
- `store._id(url)` is the article id: `sha256(url)[:16]`. `store.load_digest(date)` raises on an absent object.
- `infra/aws/lambda/astn-wsjft-orchestrator/lambda_function.py`: modes `run` (default) and `absence_check`. `_run_digest` starts the box,
  waits SSM Online, runs `su - ec2-user -c 'cd /opt/astn-wsjft/scripts && python3 run.py'` by SSM, polls, ALWAYS stops the box in `finally`
  (except on budget expiry, where it leaves it running by design), and after an SSM Success reads the digest to alert on "no usable brief".
- The code reaches the box from S3 by `infra/aws/ec2/astn-wsjft/deploy.sh`: that upload and the Lambda's deploy are the issuer's acts at the drain.

**Build -- the issuer prepared and pre-validated reference patches against the HEAD you start from (they apply cleanly to a pristine checkout, and
both criteria read OK on them). Apply them, run the criteria, and fix minimally only if something differs in your tree:**
1. `git apply org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_HEALGAP_G1/R5_PATCHES/t18_tools.patch` -- `store.try_load_digest(date)` (None on
   NoSuchKey, anything else raises) and in `run.py`: `ft_reattempt(date, now_utc, dry_run=False)` with its helpers, and the `__main__` switch
   `--ft-reattempt` / `--dry-run`. `run()` itself is not touched.
2. `git apply org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_HEALGAP_G1/R5_PATCHES/t18_orchestrator.patch` -- mode `ft_reattempt` (and `dry_run`
   in the event) through `_run_command` and `_run_digest(hard_deadline, mode, dry_run)`; the `run` command line stays byte-identical; the
   finally-stop and the budget-expiry branch are shared; after an SSM Success a refill does not run the "usable brief" digest guard.
3. Run the two criteria. If a patch does not apply or a criterion reads BAD on it, stop: write the reason and a surprise row; do not weaken a check.

The behaviour, from the producer's own rule (what the gate arms pin): `ft_reattempt` returns SKIP-COMPLETE when `digest/<date>-ftsup` exists or
today's digest carries no `FT fetch failed` warning; NO-PRIOR-DIGEST when today's digest is absent or empty (the absence guard owns that alert);
otherwise it fetches FT once (a raise propagates, nothing is sent), keeps articles fresh within the window (hours since 07:00Z of the newest earlier
day, back to 7 days, whose digest has output and no FT failure; 12 h when none) that no known digest carried (compared by `store._id(url)`),
analyses them, persists `digest/<date>-ftsup`, sends ONE email whose subject carries `FT supplement`, and discards raw. `--dry-run` does everything
but persist and send.

### ACCEPTANCE

<criterion id="HG5-t18-AC1" cell_refs="HG-t-18"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_HEALGAP_G1/R5_CHECKS/hg_t18_run_gate.py</invocation><expect>GATE-OK</expect></criterion>
`HG5-t18-AC1` -- thirteen stub arms on `run.py`: the default run is unchanged (one send, no subject, digest under the date, the warning text intact); a sent supplement, an absent or empty digest and a day without an FT failure are no-ops; the FT-failed day fetches once, windows since the last ok day (28 h, 12 h default, the newest ok day not an FT-failed one), de-duplicates by article id, persists `-ftsup` and sends one `FT supplement`; an all-duplicate fetch and a 0-survivor analysis send nothing; a fetch that raises and an unreadable digest raise; a dry run writes and sends nothing.

<criterion id="HG5-t18-AC2" cell_refs="HG-t-18"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_HEALGAP_G1/R5_CHECKS/hg_t18_orch_gate.py</invocation><expect>GATE-OK</expect></criterion>
`HG5-t18-AC2` -- the orchestrator's `run` command line is byte-identical; `ft_reattempt` runs `... python3 run.py --ft-reattempt` (`--dry-run` with the event key), makes no digest-guard read, alerts on a failed run, always stops the box, and leaves it running on budget expiry as `run` does; `absence_check` makes no SSM call.

<expected_criteria>HG5-t18-AC1 HG5-t18-AC2</expected_criteria>

Run each invocation from the worktree root. Both FAIL at the base (`GATE-BAD ...`).

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Scaffolding goes under `.scratch/`, uncommitted.
- **No AWS write, no Lambda invoke, no SES send, no EC2 start, no vendor call, no `terraform` of any kind, no `safe-apply`, no S3 upload.** The
  code reaches the box and the Lambda only by the issuer's drain act under its own never-widen pair. There is NO Terraform file in this cell.
- **NEVER ADD** an alarm, SNS topic, SES identity, freshness checker or monitor (standing moratorium). The supplement uses the brief's own
  `send_ses.send`; the `ASTN_FT_REATTEMPT` log lines are the record.
- **Do not edit** `analyze.py`, `compile_email.py`, `config.py`, `fetch_ft.js`, `send_ses.py` or anything under `infra/aws/ec2/astn-wsjft/`
  or `infra/aws/terraform/`. `run()` and the `run` command line stay byte-identical (the gate pins both).
- **Restore mechanisms (CTO round-1 analysis 2.2):** you arm no timer, background task or OS task.
- **Refusal clause.** If a criterion cannot be met as written (a patch does not apply, a gate refuses), stop, write the reason in your report and
  a surprise row (id `MDPF_HEALGAP-D1-W15-S<k>`, `fabric` `dell1`, `surfaced_at` = `date -u +%FT%TZ`, class `OBSERVATION` or `BLOCKING`) in the
  investigation file below, and do not weaken a check. Rows are APPEND-ONLY: never edit an existing row. Write the file with LF line endings and
  check `git diff --stat` shows only your added lines before committing.

<paths>
tools/astn_wsjft/scripts/run.py
tools/astn_wsjft/scripts/store.py
infra/aws/lambda/astn-wsjft-orchestrator/lambda_function.py
org/missions/D8/MDPF/MDPF_HEALGAP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_HEALGAP/decompositions/MDPF_HEALGAP_DECOMP.md</decomp_doc> (round 5, the enrichment), cell `HG-t-18`.
<owned_cells>HG-t-18</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: HG5-t18-AC1, HG5-t18-AC2. Instance at `org/missions/D8/MDPF/MDPF_HEALGAP/deliverables/0.9.0_WK_MDPF_HEALGAP~15/MDPF_HEALGAP.TO-HG-t18.astn-ft-same-day-reattempt-code.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> HG5-t18-AC1,HG5-t18-AC2 --governing-order <this order file>` BEFORE the flip.
</proof_of_spec>

**REPORT:** the files, every check's output, commits, and every row you filed.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE this order adds no schedule: the one it needs is a Terraform resource held on a naming-registry row (CTO msg 4966); the code half is invoked only by a deliberately driven `{"mode":"ft_reattempt"}` until then.
comp-iam: DECLARED-NOT-APPLICABLE this order changes no role, grant or policy: the scraper instance role already writes `digest/` and `email/` on `opal-data-astn` and reads the FT session; the orchestrator role already sends SSM and starts/stops the one instance.
comp-adversary: RUN -- `comp-adversary compose` over this order 2026-10-13 17:2xZ: 0 cited commits, 9 cited paths (1 GONE: this order's own proof instance, not yet written), 0 proof instances, 0 unproven dependencies; it has no view of the box or the Lambda's live behaviour. The failure it cannot see is the one the gates pin: a refill that re-sends an article already sent, or one that fires on a complete day. A refill at 07:00 ET cannot rescue a day whose FT cookie is still dead (the fetch raises: loud, nothing sent); named residual.
risk: WORLD -- a Lambda handler under infra/ and code that runs on a production scraper that emails the CEO; the upload, the Lambda deploy and any driven run are the issuer's at the drain.
direct_act: false -- the class is WORLD.
</preflight>

Source: CTO round-4 analysis `ledger/ROUND_ANALYSIS.round4.md` sections 2 and 3 item 1, msgs 4962 and 4966; row D1-W14-S3; decomposition round 5.
