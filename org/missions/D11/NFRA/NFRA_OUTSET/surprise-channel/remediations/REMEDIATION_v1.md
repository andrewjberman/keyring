# NFRA_OUTSET -- surprise channel, REMEDIATION v1 (round 1, laptop fabric)

**Home:** the project tree's remediation document (`org/ref/SURPRISE_CHANNEL_PROTOCOL.md` section 5; lane `TREE_CVO`).
**Who writes:** `3.0.0_SA_CVO`. One row per GRADUATED seat-form item, keyed by the item's id; the clocks (`disarm`,
`remediation`, `closed`) advance in place and only forward. Form: spine v3 -- no route token; the CTO routes every round
from the slug. Worker-form items (`W<n>-S<k>`) carry their clocks on the adjudication rows that graduate them
(`../adjudications/ADJUDICATION_v1.md` C-S3, C-S4).
**Denominator at this write:** 12 rows -- round 2 (2026-09-09 ~14:2xZ): S18 REMEDIATED and closed (remedy (c) @cb43d05200), S3 REMEDIATED and closed (the fourth false-deny mode in /cloud-ops @4e22065278, pointer @e9f7c03b0c), S16 and S17 OPEN as the CTO's placed addendum rows OS-s-20 / OS-s-21 (lane CloudOps, edge order OS-s-19 -> OS-s-20 -> OS-s-21 on the accepts), S20 OPEN (comp-iam's census carries no users or groups, owner 0.8.0_AE_CloudComp); round 1: 8 rows -- S1, S4, S8 REMEDIATED, DISARMED and closed on the issuer's and workers' in-round
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

## S3 -- a third simulate-principal-policy false-deny mode: a wrong-grain resource ARN; landed as the FOURTH mode in /cloud-ops @4e22065278; closed 2026-09-09

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
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO",
      "at": "2026-09-09T13:03Z"
    },
    "remediation": {
      "state": "REMEDIATED",
      "owner": "1.0.0_SA_CTO",
      "round": "v1"
    },
    "closed": true
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

## S18 -- a seat-addressed order's <paths> block is not a grant; remedy (c) moved the invocation paths; closed

```json
[
  {
    "id": "NFRA_OUTSET-S18",
    "project": "NFRA_OUTSET",
    "fabric": "laptop",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "mechanism": "A <paths> block is a grant only for a 0.9.0_WK_* serial (owned-paths-validate.py:123 _WORKER_SERIAL_RE, :387); both round-2 orders were seated on 0.7.0_AE_CloudOps~W and named .tools/tests/ (lane TOOL_BATTERIES) and org/modules/heatmap/outset_seam.py (lane NFRA_HEATMAP) as the mechanical criteria's invocation targets, so neither battery could be committed by the seat that had to run it.",
    "evidence": [
      "S18 (0.7.0_AE_CloudOps~W, 13:35Z): 13 paths censused at once, 3 REFUSED / 10 PERMITTED, negative control on 0.9.0_WK_NFRA_OUTSET~1 returning a different and larger refusal set; safe-commit's refusal hit, not predicted.",
      "Remedy (c) ruled by 2.0.0_SA_COO @cb43d05200 (13:30Z): O18-AC1's and O19-AC1's invocation paths moved into the seat's deliverables folder (clause 4), expects unchanged, registry not widened, cells not re-seated.",
      "S19 (the assignee's disarm ack, 13:55Z): lineage merge-base --is-ancestor cb43d05200 HEAD YES; the battery passes at the new path on both grains; the one changed line (the workspace-root derivation) disclosed.",
      "Exercised at this seat: proof-of-spec-check on the OS-s-18 instance with O18-AC1,O18-AC2 -> VALID rc=0; both orders complete at HEAD (@0c1c0110ae, @9e023d20b5). The DESIGN FACT (a seat-addressed tree order's <paths> is not a grant) is carried by 1.0.0_SA_CTO to the brief-to-cut chain's L4 @e18317d0e0 as an FWD-1 instance; nothing is built on it now."
    ],
    "remedy": "EXECUTED: remedy (c) -- the invocation paths moved to the seat's own deliverables folder; both orders completed against the amended faces.",
    "owner": "2.0.0_SA_COO",
    "round": "v2",
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO",
      "at": "2026-09-09T13:30Z"
    },
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO",
      "round": "v2"
    },
    "closed": true
  }
]
```

## S16 -- the consumer never looks: ESTATE_OUTSET_SEAM_PREFIX unset on the host; PLACED as OS-s-20 (after OS-s-19); OPEN

```json
[
  {
    "id": "NFRA_OUTSET-S16",
    "project": "NFRA_OUTSET",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "ESTATE_OUTSET_SEAM_PREFIX is set nowhere in Terraform (instance.tf:130-151 sets eleven variables, not this one), so the served runner's _stratum_propagation returns INSTRUMENT_UNAVAILABLE without composing a key; the seam is published-to and readable and no consumer looks. Setting it is an instance REPLACEMENT (instance.tf:83 user_data_replace_on_change = true), a NEVER-2 act neither round-2 order names.",
    "evidence": [
      "S16 (0.7.0_AE_CloudOps~W, 13:20Z): comp-find 5 of 5 hits inside estate_report_runner.py, 0 under infra/aws/terraform/; the eleven-variable heredoc read 11 of 11.",
      "PLACED by 1.0.0_SA_CTO @e18317d0e0 (94483) as manifest row OS-s-20 for the L10 addendum v0.4: lane CloudOps, verb deploy, AFTER OS-s-19 (the host pulls the runner at boot, instance.tf:94-96 and :215), replace sequenced outside the run window under its own NEVER-2 entry naming host, pinned runner bytes and rollback.",
      "ACCEPT per the CTO's sharpening (2): on a SCHEDULED 13:00Z run of the replaced host, the published report's propagation stratum returns an answer state other than INSTRUMENT_UNAVAILABLE with the seam artifact's vintage disclosed; the env line present in the live runtime.env is DESIRED -> APPLIED and a control, never the accept.",
      "At this seat 14:0xZ: the served runner is at HEAD (C-S6, O19-AC2) and carries the consumer (5 LIVE tokens per O19-AC1 arm D), so the switch is the only remaining member between FWD-3 and REALIZED besides the cadence (S17)."
    ],
    "remedy": "OS-s-20 (PLACED, not yet cut): set ESTATE_OUTSET_SEAM_PREFIX in runtime.env and replace the host under a NEVER-2 entry, after OS-s-19; disarm on the accept above read from a served day's report.",
    "owner": "0.7.0_AE_CloudOps (lane per 1.0.0_SA_CTO @e18317d0e0; the row is cut by 2.0.0_SA_COO at the round-2 recut)",
    "round": "v2",
    "disarm": {
      "state": "ARMED",
      "owner": "0.7.0_AE_CloudOps",
      "at": null
    },
    "remediation": {
      "state": "OPEN",
      "owner": "0.7.0_AE_CloudOps (lane per 1.0.0_SA_CTO @e18317d0e0; the row is cut by 2.0.0_SA_COO at the round-2 recut)",
      "round": "v2"
    },
    "closed": false
  }
]
```

## S17 -- the publish has no cadence and the 26 h ceiling convicts it; PLACED as OS-s-21 (gated on OS-s-20's accept); OPEN

```json
[
  {
    "id": "NFRA_OUTSET-S17",
    "project": "NFRA_OUTSET",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "The seam publish was by hand at 2026-09-09T13:03:50Z; OUTSET_SEAM_MAX_AGE_HOURS defaults to 26 and runtime.env does not override it, so the artifact reads STALE -> INSTRUMENT_FAILED from about 2026-09-10T15:03Z (R5 arm exercised at 999.0 h). The producer org/modules/heatmap/outset_seam.py is a CLI with no caller and no schedule.",
    "evidence": [
      "S17 (0.7.0_AE_CloudOps~W, 13:21Z): s3api listing 2 of 2 objects at the prefix; :1645 the 26 h default; the R5 arm's conviction live; no scheduler, EventBridge rule, systemd unit or CI step names the producer.",
      "PLACED by 1.0.0_SA_CTO @e18317d0e0 as manifest row OS-s-21: lane CloudOps, verb build, a scheduled publish of the two producers before the 13:00Z run, on the producer's side; a pipeline trigger is not a monitor and the moratorium does not reach it; the trigger is the producer's OWN schedule, never success-of-upstream alone.",
      "ACCEPT per the CTO's sharpening (2): on a real day the artifact's vintage precedes that day's 13:00Z run and the served stratum reads FRESH with age < 26 h disclosed; with the schedule disabled the R5 arm still convicts at > 26 h; a hand publish is QA, never the exercise. GATED on OS-s-20's accept (a scheduled publish into a prefix the consumer never reads is a duplicate output path with a timer on it); the two may be BUILT in parallel.",
      "At this seat 14:0xZ: prefix holds 3 objects -- the two published (27060 B 13:03:50Z, 63822 B 13:03:49Z) and the battery's R2 probe outset/_os18_red_arm_probe.json (1028 B, 13:34:40Z, a FAILED-shaped artifact at a fixed key the exact-key consumer never composes; PRD R-5 never-auto-delete)."
    ],
    "remedy": "OS-s-21 (PLACED, not yet cut): a producer-side scheduled publish of the two seam artifacts before the 13:00Z run; disarm on the accept above read from a served day, with the negative arm (schedule disabled -> R5 convicts).",
    "owner": "0.7.0_AE_CloudOps (lane per 1.0.0_SA_CTO @e18317d0e0; the row is cut by 2.0.0_SA_COO at the round-2 recut)",
    "round": "v2",
    "disarm": {
      "state": "ARMED",
      "owner": "0.7.0_AE_CloudOps",
      "at": null
    },
    "remediation": {
      "state": "OPEN",
      "owner": "0.7.0_AE_CloudOps (lane per 1.0.0_SA_CTO @e18317d0e0; the row is cut by 2.0.0_SA_COO at the round-2 recut)",
      "round": "v2"
    },
    "closed": false
  }
]
```

## S20 -- comp-iam's census carries no users or groups; a reach read from it is role-only; OPEN

```json
[
  {
    "id": "NFRA_OUTSET-S20",
    "project": "NFRA_OUTSET",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "comp-iam refresh-census writes a census whose summary counts users (7) and groups (1) and whose body carries roles only; a who-can-reach read from the file is role-only and reads as complete.",
    "evidence": [
      "S20 (3.0.0_SA_CVO, this write): keys _meta/summary/roles; 224 roles; no users or groups arrays; _meta.managed_policies_resolved false. The population census at C-S6 is stated as roles-only because of it.",
      "Same family as S2/S6 (an instrument whose disclosure is narrower than its coverage); comp-iam is in 0.8.0_AE_CloudComp's lane."
    ],
    "remedy": "comp-iam refresh-census records users and groups with their statements, or prints an UNCOVERED line with the denominator (users N, groups M) on every read that answers a reach question; disarm on one census file at this seat carrying them or on the UNCOVERED line printing.",
    "owner": "0.8.0_AE_CloudComp",
    "round": "v2",
    "disarm": {
      "state": "ARMED",
      "owner": "0.8.0_AE_CloudComp",
      "at": null
    },
    "remediation": {
      "state": "OPEN",
      "owner": "0.8.0_AE_CloudComp",
      "round": "v2"
    },
    "closed": false
  }
]
```
