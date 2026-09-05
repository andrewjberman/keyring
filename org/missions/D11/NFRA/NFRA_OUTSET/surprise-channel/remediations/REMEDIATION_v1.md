# NFRA_OUTSET -- surprise channel, REMEDIATION v1 (round 1, laptop fabric)

**Home:** the project tree's remediation document (`org/ref/SURPRISE_CHANNEL_PROTOCOL.md` section 5; lane `TREE_CVO`).
**Who writes:** `3.0.0_SA_CVO`. One row per GRADUATED seat-form item, keyed by the item's id; the clocks (`disarm`,
`remediation`, `closed`) advance in place and only forward. Form: spine v3 -- no route token; the CTO routes every round
from the slug. Worker-form items (`W<n>-S<k>`) carry their clocks on the adjudication rows that graduate them
(`../adjudications/ADJUDICATION_v1.md` C-S3, C-S4).
**Denominator at this write:** 8 rows -- S1, S4, S8 REMEDIATED, DISARMED and closed on the issuer's and workers' in-round
acts; S2, S6 OPEN (comp-find, owner `0.8.0_AE_CloudComp` by the tool's lane, routed by the CTO); S3 OPEN (an IAM instrument
trap for the doctrine, owner `1.0.0_SA_CTO`); S13 OPEN (the decomposition's false claim, owner `2.0.0_SA_COO` at the recut);
S14 OPEN (COMMITTED is not SERVED: the estate-report runner's deploy has no owner, owner `1.0.0_SA_CTO` at L10).

## S1 -- O6-AC1 invoked a bash forwarder through python; amended and re-armed; closed

```json
[
  {
    "id": "NFRA_OUTSET-S1",
    "project": "NFRA_OUTSET",
    "fabric": "laptop",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "mechanism": "TO-OS-s-6's O6-AC1 ran `python .tools/comp-iam --help`; .tools/comp-iam is a #!/bin/bash forwarder, so python parsed it as Python and exited 1 with zero matches for 'usage' -- the criterion could not pass as cut.",
    "evidence": [
      "Amended by 2.0.0_SA_COO @8d13fc6b80 (the invocation `comp-iam --help`); re-armed (msg 94322); re-run by 0.7.0_AE_CloudOps~W: rc=0, 1 match for 'usage', stable across two same-input repeats, with the superseded form still failing as the negative control; TO-OS-s-6 `<status>complete` at HEAD.",
      "S5 (2.0.0_SA_COO) is the disarm ACK, measured at that seat; C-S1 at this seat graded O6-AC2/O6-AC3 on the same order."
    ],
    "remedy": "EXECUTED: the face's invocation corrected to the forwarder's own name; the order completed against the amended face.",
    "owner": "2.0.0_SA_COO",
    "round": "v1",
    "disarm": {"state": "DISARMED", "owner": "2.0.0_SA_COO", "at": "2026-09-05T01:12Z"},
    "remediation": {"state": "REMEDIATED", "owner": "2.0.0_SA_COO", "round": "v1"},
    "closed": true
  }
]
```

## S2 -- comp-find CONTENT mode times out at rc=124 with zero bytes; a timed-out search reads as a clean zero

```json
[
  {
    "id": "NFRA_OUTSET-S2",
    "project": "NFRA_OUTSET",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "comp-find CONTENT mode returns rc=124 with ZERO bytes on stdout and stderr when its internal deadline fires, suppressing the printed denominator CLAUDE.md Rule 21 relies on; a positive control on a certain token failed identically; S6 adds that --budget is accepted and no budget line is printed.",
    "evidence": [
      "S2 and S6 at HEAD (0.7.0_AE_CloudOps~W; 4.0.0_SA_CRO): the measurements and the positive control; recorded to this seat's memory as an instrument trap on 2026-09-04.",
      "The tool is a comp-tool in the registry's lane; no order of this round names it."
    ],
    "remedy": "comp-find prints a BUDGET REACHED / ANSWER-STATE line and exits with a non-clean, non-124 verdict when its deadline fires (Rule T's terminal line), and prints its budget disclosure when --budget is given; disarm on one timed-out run at this seat printing the line with a denominator.",
    "owner": "0.8.0_AE_CloudComp",
    "round": "v1",
    "disarm": {"state": "ARMED", "owner": "0.8.0_AE_CloudComp", "at": null},
    "remediation": {"state": "OPEN", "owner": "0.8.0_AE_CloudComp", "round": "v1"},
    "closed": false
  }
]
```

## S3 -- a third simulate-principal-policy false-deny mode: a wrong-grain resource ARN

```json
[
  {
    "id": "NFRA_OUTSET-S3",
    "project": "NFRA_OUTSET",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "simulate-principal-policy returns implicitDeny, with no error, for a resource ARN at the wrong grain for the action (logs:GetLogEvents against a log-stream-grain ARN) even for a principal holding AdministratorAccess; it fails in the under-granted direction and is invisible against a narrowly scoped principal.",
    "evidence": [
      "S3 at HEAD (0.7.0_AE_CloudOps~W): the four-form measurement and the */* control; the two known modes were both mitigated and neither prevents this one.",
      "Recorded to this seat's memory 2026-09-04 beside the conditioned-grant and multi-ARN modes; not yet in the estate's IAM trap doctrine (/cloud-ops)."
    ],
    "remedy": "Add the wrong-grain mode to the IAM traps section the /cloud-ops doctrine carries beside the two known modes, with the mitigation (pass the ARN at the action's own resource grain; run a */* control beside any deny you act on); disarm on the doctrine line landing.",
    "owner": "1.0.0_SA_CTO",
    "round": "v1",
    "disarm": {"state": "ARMED", "owner": "1.0.0_SA_CTO", "at": null},
    "remediation": {"state": "OPEN", "owner": "1.0.0_SA_CTO", "round": "v1"},
    "closed": false
  }
]
```

## S4 -- sixteen faces named the proof instance by a stem the gate does not glob; closed on the population

```json
[
  {
    "id": "NFRA_OUTSET-S4",
    "project": "NFRA_OUTSET",
    "fabric": "laptop",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "mechanism": "16 of 17 faces named their proof_of_spec instance by the short to_id stem while .tools/to-pipeline-gate.py globs the full face stem; an assignee following its face literally wrote a file the gate could not see and the complete flip was refused.",
    "evidence": [
      "S5 (2.0.0_SA_COO) is the disarm ACK; the population fact at this seat: 17 of 17 orders `<status>complete` at HEAD, each flip admitted by the gate against an instance it could glob, so the stem is correct on every face that flipped.",
      "The same defect on ETFS_GUARDRAIL (W1-S3, W2-S2, W3-S2) was repaired on all 14 faces @83d8175729; the cut lesson is carried in both rounds' analyses."
    ],
    "remedy": "EXECUTED: the faces amended to the gate's form; every order flipped complete through the gate.",
    "owner": "2.0.0_SA_COO",
    "round": "v1",
    "disarm": {"state": "DISARMED", "owner": "2.0.0_SA_COO", "at": "2026-09-05T13:40Z"},
    "remediation": {"state": "REMEDIATED", "owner": "2.0.0_SA_COO", "round": "v1"},
    "closed": true
  }
]
```

## S8 -- OS-s-2's battery arm F was a flaky red with two mechanisms; both fixed; closed

```json
[
  {
    "id": "NFRA_OUTSET-S8",
    "project": "NFRA_OUTSET",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "Arm F compared scoped and unscoped answers for age parity; a commit landing between its two passes moved one file's age (mechanism 1, the mtime race), and comp-heat's age_days is quantised to 0.01 d while the arm's tolerance was 0.01 (mechanism 2), so adjacent quanta compared as greater; the arm printed its failure count beside an empty key list.",
    "evidence": [
      "W1-S12 (0.9.0_WK_NFRA_OUTSET~1) removed the mtime race; S9 (2.0.0_SA_COO) acknowledged it; S11 (2.0.0_SA_COO) corrected S9 as OVERCLAIMED because the falsifier covered one mechanism; W1-S18 (the same worker) found and fixed the quantisation tolerance and re-ran 3 of 3 clean, filed against itself.",
      "Read as a pair at this seat: the two corrections are what make the closure trustworthy -- each mechanism has its own falsifier now."
    ],
    "remedy": "EXECUTED in two acts by the worker: the race removed, the tolerance widened past the quantum, both re-run clean.",
    "owner": "2.0.0_SA_COO",
    "round": "v1",
    "disarm": {"state": "DISARMED", "owner": "2.0.0_SA_COO", "at": "2026-09-05T09:07Z"},
    "remediation": {"state": "REMEDIATED", "owner": "2.0.0_SA_COO", "round": "v1"},
    "closed": true
  }
]
```

## S6 -- comp-find accepts --budget and prints no budget disclosure line

```json
[
  {
    "id": "NFRA_OUTSET-S6",
    "project": "NFRA_OUTSET",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "comp-find CONTENT mode accepts --budget and prints no disclosure of the budget or of whether it bound the scan, so a bounded search and an unbounded one print identically; with S2 this is the second Rule T gap on the estate's default search instrument.",
    "evidence": [
      "S6 at HEAD (4.0.0_SA_CRO): the measured invocation with --budget and the absent line.",
      "The tool's lane is the comp-tool registry's; carried with S2 as one remedy."
    ],
    "remedy": "With S2: a Rule T terminal line on every comp-find content run that names the budget, the scan denominator and the answer state; disarm on one budgeted run at this seat printing it.",
    "owner": "0.8.0_AE_CloudComp",
    "round": "v1",
    "disarm": {"state": "ARMED", "owner": "0.8.0_AE_CloudComp", "at": null},
    "remediation": {"state": "OPEN", "owner": "0.8.0_AE_CloudComp", "round": "v1"},
    "closed": false
  }
]
```

## S13 -- the decomposition asserted a manifest lane the PRD does not contain

```json
[
  {
    "id": "NFRA_OUTSET-S13",
    "project": "NFRA_OUTSET",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "The decomposition states 'OS-s-17 IS THE CVO's. Its lane in the manifest is CVO' while the PRD manifest at HEAD reads lane=CloudComp, verb=build; the issuance did not follow the decomposition here and is correct, so the frozen decomposition carries a false sentence about the document it cites.",
    "evidence": [
      "S13 at HEAD (2.0.0_SA_COO, filed against its own L5): the two texts side by side; the issuer names it the second instance of reasoning from an unverified claim about a document's contents (the first was the dep_stage flip).",
      "This seat's read: OS-s-17 was issued to and executed by 0.9.0_WK_NFRA_OUTSET~1 and graded by this seat at L9 (O17-AC1, C-S2), which is the spine's shape; the CVO did not hold the cell."
    ],
    "remedy": "At the recut (the decomposition is frozen mid-round): correct the sentence to the manifest's lane and verb, citing this row; disarm on the corrected decomposition text at HEAD.",
    "owner": "2.0.0_SA_COO",
    "round": "v1",
    "disarm": {"state": "ARMED", "owner": "2.0.0_SA_COO", "at": null},
    "remediation": {"state": "OPEN", "owner": "2.0.0_SA_COO", "round": "v1"},
    "closed": false
  }
]
```

## S14 -- COMMITTED is not SERVED: the estate-report runner's deploy is a single S3 upload no cell owns

```json
[
  {
    "id": "NFRA_OUTSET-S14",
    "project": "NFRA_OUTSET",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "The report host boots whatever bytes sit at s3://opal-estate-report/code/estate_report_runner.py; those bytes are 125,857 B dated 2026-08-25T05:36:35Z while HEAD carries 159,687 B, and the served file contains none of OS-s-10's seam (_outset_read, OUTSET_ANSWER_STATE_TO_STATUS), none of OS-s-17's citation gate (tool_row_cited) and the pre-project _stratum_cochange. Three cells changed the runner (OS-s-9, OS-s-10, OS-s-11, then OS-s-14 and OS-s-17) and none is running; the PRD costs the work and places no deploy step; every published day the project reasoned about was produced by the pre-project code.",
    "evidence": [
      "3.0.0_SA_CVO at this seat, 13:4xZ: `s3api head-object` 125,857 B / 2026-08-25T05:36:35Z; the object downloaded and grepped against `git show HEAD:infra/aws/ec2/estate-report-runner/estate_report_runner.py` (159,687 B): _outset_read served 0 / HEAD 4; OUTSET_ANSWER_STATE_TO_STATUS 0 / 3; tool_row_cited 0 / 7; _stratum_cochange 2 / 4; the two tokens S14 called dead arms (rerun_recipe, tool_invocation) read 0 at HEAD too.",
      "W1-S25 (0.9.0_WK_NFRA_OUTSET~1) the finding; S14 (2.0.0_SA_COO) the confirmation with the instrument correction; W1-S26 the consequence for FWD-4 (a green criterion that cannot reach a published day); W1-S27 the worker's own instrument correction. The completion report @a483609584 leads with it."
    ],
    "remedy": "Name the owner of the runner's deploy step (an S3 upload of code/estate_report_runner.py under a NEVER-2 ledger entry, after the round's edits are judged safe to serve together), then deploy once and verify the served bytes equal HEAD's at the deploy commit; the same owner holds the seam's publishing step (W1-S19, W1-S20, W2-S15). Disarm on the served object's sha256 equalling the repo file's at the deploy commit, read at this seat.",
    "owner": "1.0.0_SA_CTO",
    "round": "v1",
    "disarm": {"state": "ARMED", "owner": "1.0.0_SA_CTO", "at": null},
    "remediation": {"state": "OPEN", "owner": "1.0.0_SA_CTO", "round": "v1"},
    "closed": false
  }
]
```
