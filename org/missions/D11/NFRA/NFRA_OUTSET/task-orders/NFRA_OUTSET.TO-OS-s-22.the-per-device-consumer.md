# TO NFRA_OUTSET.TO-OS-s-22 -- THE PER-DEVICE CONSUMER: group A composes every device's drift key, renders each with its own vintage and ceiling, and retires the single-key read with the composition

<to_id>NFRA_OUTSET.TO-OS-s-22</to_id>
<project>NFRA_OUTSET</project>
<issued_to>0.7.0_AE_CloudOps~W</issued_to>
<issued_by>2.0.0_SA_COO</issued_by>
<issued_date>2026-09-09</issued_date>
<status>pending -- GO paired at cut (a seat order is dispatched by its issuance). Authority: PRD **v0.5** @`1ac8679844` (mid-round addendum on the S23 ruling @`98722f9355`, on Andrew's 2026-09-03 scope-change word), s.7 row OS-s-22; decomposition v0.5 s.19-s.22. BUILDABLE NOW against the key layout the ruling names; its ACCEPT reads on a served day after both this deploy and a device publish under OS-s-21 have landed.</status>

**Directive:** D11 · **Fabric:** laptop · **PRD:** `../prd/NFRA_OUTSET_PRD.md` v0.5 (s.7 row OS-s-22) · **Decomp cell:** `OS-s-22` (`../decompositions/NFRA_OUTSET_DECOMP.md` v0.5, s.19-s.22) · **outcome_ref:** FWD-3 · **verb:** wire · **depends_on:** OS-s-21 (the key layout `outset/<device>/comp_heat_drift.json`, named on that face and in the row), OS-s-19 (COMPLETE @`9e023d20b5` -- the runner's deploy path this cell reuses)

---

## THE CELL

`OS-s-22` (PRD s.7, evidence **absent**): `estate_report_runner.py:1844` composes ONE key, `<prefix>/comp_heat_drift.json`. Under the S23 ruling drift is a property of a DEVICE and is keyed per device; two devices writing one key is last-writer-wins, a confident partial. Until this cell lands the single key carries one device's artifact with its `device` field, read as that device's, never as the estate's.

⛔ **THE SHAPE, as the ruling's sharpening 3 writes it**: group A composes EVERY `outset/<device>/comp_heat_drift.json`, renders each device's drift with THAT device's vintage and its own 26 h ceiling, reads QUIET (n=0 with `tracked_total` > 0: the device reported a clean tree) and SILENT (no report inside the ceiling: `INSTRUMENT_FAILED` for that device ONLY, the others still render) as DIFFERENT states, and NEVER sums devices into one n. **The single-key read is RETIRED WITH the composition, not beside it** -- a consumer that reads both is a duplicate path.

⛔ **A ZERO OVER AN EMPTY POPULATION IS OUT-OF-CORPUS** (the PRD's bound for every row of this seam): an artifact whose `tracked_total` is 0, or that lacks the `device` field, is not a QUIET reading -- it is refused as evidence and rendered as such.

## DELIVERABLE

`org/missions/D11/NFRA/NFRA_OUTSET/deliverables/0.7.0_AE_CloudOps~W/the-per-device-consumer.result.md` -- what you measured, what you changed, each criterion's invocation and its output verbatim with rc and denominator, and any row you filed.

## BOUNDS

- **Your write surface is the paths named in `<paths>` below, as your LANES admit them** -- see the S18 note under the block. A path you need that neither names is a CUT DEFECT: file a BLOCKING row and stop that criterion. It is never an override.
- **EVERY invocation is bounded.** Run each under the `timeout` its criterion names and a timeout is RECORDED AS THE OUTPUT.
- **NEVER `git push`**, under this or any order. Report push state as MEASURED (`git ls-remote`).
- **NEVER bare `terraform apply`** -- `safe-apply` only. **NEVER `aws lambda update-function-code`.**
- **No alarm, monitor, freshness-checker or SNS** (standing moratorium). **NEVER-AUTO-DELETE (PRD R-5) is absolute**: the R2 probe and any planted control artifact stay where they are after the exercise.
- **A spec-vs-world divergence is a ROW** at `org/missions/D11/NFRA/NFRA_OUTSET/surprise-channel/investigations/INVESTIGATION_v1.md`, minted `NFRA_OUTSET-S<k>` for a seat -- append, cite `path@commit`, never edit an existing row, keep working.
- **A commit report states its PUSH STATE as a MEASURED value.**

⛔ **THIS IS A NEVER-2 CELL, THE OS-s-19 SHAPE EXACTLY: a runner code change and ONE S3 upload of `code/estate_report_runner.py`.** It does NOT replace the host (no `user_data` change; the host pulls the runner at every boot, `instance.tf:215`). Open a change-management entry in `org/critical_paths/change_management/` and COMMIT IT OPEN before the upload; close it after, in a second commit. The entry names the served object's pre-state (head-object: size, ETag, VersionId -- read live), the one functional consumer (the host's ExecStartPre pull; the orchestrator reads no code key), the window (the host self-stopped after the creation-boot run at 15:32:42Z today; the next fire is 2026-09-10 13:00Z; state plainly that the upload lands outside it), and the rollback (one `copy-object` from the prior VersionId, in session). ⛔ **Before acting on ANY open or red entry you find, MEASURE THE ARTIFACT.** ⛔ **The upload is `git show HEAD:<path>`'s bytes, compared, not assumed equal to the worktree** (Rule 22a; the autocrlf trap).

⛔ **THE CONTROL THAT CAN FAIL IS A PLANTED SECOND-DEVICE ARTIFACT, AND IT IS QA.** Plant it under a name that cannot be a real device (`outset/_os22_probe_device/comp_heat_drift.json`, the R2 probe's pattern), carrying the ruling's fields with a distinct `device` value and a small non-zero n; the composition must render it as a SECOND row and never merge it into the real device's n; then leave it in place under R-5. It is never counted as a reporting device in the accept's headline.

## ACCEPTANCE

One clause per criterion. A mechanical criterion carries exactly one `<invocation>` and one `<expect>`, so its pass is decided by the MATCH and never by your opinion. A `judgment="true"` criterion is RECORDED with its evidence and NO verdict -- `3.0.0_SA_CVO` grades it at L9.

<criterion id="O22-AC1" cell_refs="OS-s-22"><invocation>timeout 300 python org/missions/D11/NFRA/NFRA_OUTSET/deliverables/0.7.0_AE_CloudOps~W/test_os22_per_device_consumer.py</invocation><expect>OS22-PER-DEVICE-CONSUMER</expect></criterion>
`O22-AC1` -- a battery you write, proving THE ACCEPT AS THE PRD WRITES IT on a SERVED DAY: group A shows each reporting device by name with its vintage; a device silent past its ceiling reads `INSTRUMENT_FAILED` for that device while the others render; the planted second-device artifact renders as a second row and never merges into the first's n; the single-key read is retired (a battery arm proves the composed group A does not read `outset/comp_heat_drift.json` -- the served bytes carry the per-device composition and not the single-key read, by token census with a positive control per token, W1-S27). ⛔ **THE NEGATIVE ARMS**: an artifact with `tracked_total` 0 or no `device` field renders as OUT-OF-CORPUS, never QUIET; a mutant that sums two devices into one n is DETECTED (a planted mutant in a COPY of the runner, anchor uniqueness asserted first). Read the served day's report from the bucket, never a local render. **This criterion CANNOT pass before the first scheduled fire after BOTH this deploy and a real device publish under OS-s-21 have landed; that is correct.**

<criterion id="O22-AC2" cell_refs="OS-s-22" judgment="true"/>
`O22-AC2` -- THE DEPLOY UNDER ITS LEDGER AND THE RETIREMENT: the entry opened-before and closed-after (both commits cited), the window as measured, the served object's pre- and post-state, the consumer census, the rollback stated before the act, and the retirement of the single-key read shown in the served bytes rather than asserted. Evidence with vintage. NO VERDICT.

<expected_criteria>O22-AC1, O22-AC2</expected_criteria>

<paths>
infra/aws/ec2/estate-report-runner/
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D11/NFRA/NFRA_OUTSET/deliverables/0.7.0_AE_CloudOps~W/
org/missions/D11/NFRA/NFRA_OUTSET/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>
⛔ **FOR A SEAT, THIS BLOCK IS NOT A GRANT -- THE LANE REGISTRY IS** (row `NFRA_OUTSET-S18`, RULED @`cb43d05200`). Every path above resolved PERMITTED for `0.7.0_AE_CloudOps~W` at the issuer's seat on this round's census (the runner directory, both ledger folders, this deliverables folder by clause 4, the channel by lane ANY). Your battery lives in your deliverables folder. `org/modules/heatmap/outset_seam.py` is NOT named (lane NFRA_HEATMAP): the consumer reads keys the seam module publishes and imports nothing new from it; if the composition needs a change there, that is a BLOCKING row.

<decomp_ref>
<decomp_doc>org/missions/D11/NFRA/NFRA_OUTSET/decompositions/NFRA_OUTSET_DECOMP.md</decomp_doc> v0.5, cell `OS-s-22`.
<owned_cells>OS-s-22</owned_cells>
</decomp_ref>

<preflight>
comp-schedule: RUN at this issuance, 2026-09-09 ~15:3xZ -- WITHIN BUDGET, scanned 5 of 5 carriers, 21.812 s of a 90 s default. GATES ARMED: 25. REACHED-DENOMINATORS C1=23, C2=6, C3=12, C4=20, C5=335. ZERO of the 25 armed gates names NFRA_OUTSET, the estate-report host or runner, the consumption seam or comp-heat (0 hits for those tokens across the ledger output). BLIND SPOT, stated: this lens reads the GATE LEDGER and cannot say whether an S3 upload of the runner is otherwise constrained -- comp-iam's plane, required of the assignee below; the served object's own ledger (OS-s-19's entry, CLOSED) is the precedent this cell repeats.
comp-iam: DECLARED-NOT-APPLICABLE as an ISSUER preflight, and REQUIRED OF THE ASSIGNEE as the cell's own instrument -- the runner's role must still read every per-device key (`outset/*` GetObject, granted under OS-s-18 and EXERCISED); re-read it on the APPLIED plane after a census refresh (24 h TTL). FOUR false-deny modes are live (a CONDITIONED grant, a batched multi-ARN call, a WRONG-GRAIN resource ARN, and the census's role-only reach per S20). Positive-control any deny you intend to act on.
comp-adversary: DECLARED-NOT-APPLICABLE -- a fresh cut with no prior artifact to validate against.
lane: for a SEAT the lane registry is the grant and the `<paths>` block only narrows it (row S18, RULED @`cb43d05200`); every path above resolved PERMITTED for `0.7.0_AE_CloudOps~W` at the issuer's seat, plus this seat's own deliverables folder by clause 4.
</preflight>

<proof_of_spec>
Criterion ids minted at cut by the issuer: `O22-AC1`, `O22-AC2`. The ASSIGNEE fills a `PROOF_OF_SPEC.schema.json` instance at
`org/missions/D11/NFRA/NFRA_OUTSET/deliverables/0.7.0_AE_CloudOps~W/NFRA_OUTSET.TO-OS-s-22.the-per-device-consumer.proof_of_spec.json`
and validates it with `python .tools/proof-of-spec-check.py <instance> O22-AC1,O22-AC2` BEFORE the complete flip, which the assignee commits itself.
⛔ **The path above is the FULL FACE STEM.** `.tools/to-pipeline-gate.py:1261-1270` globs `deliverables/*/<full-stem>.proof_of_spec.json`; a short-stem name is REFUSED.
⛔ **A `complete` flip is the end of the order**: flip only when the MECHANICAL criterion PASSES on a SERVED DAY and the instance validates rc=0. The deploy lands when the code is ready; the flip waits for the served day. A mis-flip is REOPENED by the issuer, never re-cut.
</proof_of_spec>

**REPORT:** to `2.0.0_SA_COO`, TWICE on this order: once when the deploy has landed and its ledger entry is CLOSED (the act; the accept still pending the served day), and once at the flip. Per-criterion evidence, denominators, and push state as MEASURED. If something in this face is wrong or missing, that is a CUT DEFECT and it is the issuer's -- file the row and say so; do not work around it.
