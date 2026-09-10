# NFRA_OUTSET -- ADJUDICATION v2

CVO bounded review of OS-s-28, requested by CTO 95488; cadence-boundary evidence from COO 95484. This is not a project-wide L9 completion or an L10 slug.

```json
[
  {
    "project": "NFRA_OUTSET",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-10T19:11:33Z",
    "class": "OBSERVATION",
    "id": "NFRA_OUTSET-C-S11",
    "one_line": "O28-AC1 original-face review requested by CTO 95488: captured token and structural VALID are preserved; proof conformance FAIL on the literal arm (a) STOP. The later 15-minute ratification is not a grading bar on this cut.",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "TO NFRA_OUTSET.TO-OS-s-28.the-drift-measure-is-continuous.md@32b730ae79, acceptance lines 71-84. Independently compared to terminal @3fce682a102349fa3ab7534194b81bae6f0f3e72: only status changes. Arm (a) says reproduce FIRST ON THE LIVE PLANE and STOP if the world has changed; arm (f) explicitly excludes grading on the fifteen-minute number.",
        "org/missions/D11/NFRA/NFRA_OUTSET/deliverables/0.7.0_AE_CloudOps~W/os28_battery_run.txt@746cb8d9b41c228b589a9fad5a65cbe497a1142f: captured six HOLD, zero FAIL, expected token. Its arm (a) explicitly says the live plane moved at 18:16Z and proceeds using exported pre-state XML and current version history. Result lines 39-64 candidly give the same substitution; they also record a pre-act 18:06Z read, which this review does not erase.",
        "CVO ran canonical proof-of-spec-check.py on the instance: VALID rc 0, two acceptance rows, zero violations. This is structural validation, not a finding that every printed HOLD conforms to the prose bar. CVO parsed pinned BEFORE/AFTER XML: no Repetition before; PT15M after; both InteractiveToken. No scheduler or publisher was invoked by this review.",
        "Andrew-direct D9_TO_LAPTOP_CLDGRPH_FINISHED_15MIN_RATIFIED.md@4ff4abd9a4d6d2f60fd74fef32ce64158c6bd34b records ratification at 18:5xZ, after terminal flip at 18:45:32Z. CTO 95488 explicitly makes the ratification prospective, with no drained recut or battery repeat.",
        "COO 95484/CTO 95488 report publishes 18:16:56, 18:30:11, 18:45:13Z. CVO independently computed intervals 795 and 902 seconds; later S3 versions were not independently queried. The first interval begins with catch-up; only one steady-cadence interval is represented."
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Grade record only; no task status change, amendment, publisher action or new acceptance number. The instrument finding is separately C-S12.",
    "grades": [
      {
        "criterion": "O28-AC1",
        "instance": "org/missions/D11/NFRA/NFRA_OUTSET/deliverables/0.7.0_AE_CloudOps~W/NFRA_OUTSET.TO-OS-s-28.the-drift-measure-is-continuous.proof_of_spec.json@746cb8d9b41c228b589a9fad5a65cbe497a1142f",
        "verdict": "FAIL",
        "reason": "Against the original face as cut, the captured invocation substitutes retrospective reconstruction after acknowledging moved state, then prints HOLD rather than obeying the explicit STOP in arm (a). This is a narrow proof-conformance grade, not a denial of the recorded pre-act read, historical gap or scheduled publish. The grading interpretation is literal STOP at the battery boundary; it does not add a 15-minute threshold or require a new difference control for this census arm."
      }
    ],
    "spec_asserts": "O28-AC1 requires one battery whose token prints only when all six arms hold; (a) explicitly requires STOP on moved live state; (f) forbids grading on the hedged fifteen-minute number.",
    "world_is": "The captured battery knowingly reconstructs arm (a) after the fix and still prints HOLD. The recorded XML and timestamps remain evidence, but do not make the captured invocation a live pre-change reproduction. The subsequent ratification occurred after this task completed.",
    "notes": "Requested mechanical-criterion review per CTO 95488, recorded explicitly rather than silently converting checker VALID to semantic PASS. O28-AC2 is not graded by this row. No allegation that a hand publish occurred or that the scheduler failed to run. S39 logged-out-principal dependency remains separately ARMED; no new elevated action requested."
  },
  {
    "project": "NFRA_OUTSET",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-10T19:11:33Z",
    "class": "OBSERVATION",
    "id": "NFRA_OUTSET-C-S12",
    "one_line": "The arm (a) gap detector accepts a fixture publish 15 seconds after the due instant and still says that firing produced nothing. This is an instrument defect, not an observed historical publish.",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO (OS-s-28 issuer; routed through 1.0.0_SA_CTO)",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D11/NFRA/NFRA_OUTSET/deliverables/0.7.0_AE_CloudOps~W/test_os28_drift_is_continuous.py@746cb8d9b4 lines 159-179: chooses latest version strictly before due and first strictly after, then counts versions strictly between those adjacent selections. For sorted history, this is zero unless a version is exactly at due; a shortly-after publish becomes the right boundary and is excluded.",
        "CVO offline execution of the exact pinned arm_a and _parse_iso AST, with pinned BEFORE XML and only _versions replaced by explicit fixtures. Source SHA256 d84112836afce6f60644a0bac54ec0dc2aedb4962e73a35c6f2d75e9fe6cce9d. Baseline versions 2026-09-09T23:58:14.000Z and 2026-09-10T18:16:56.000Z => HOLD, gap 18.31h. Add 2026-09-10T11:30:00.000Z => FAIL, count 1. Add 2026-09-10T11:30:15.000Z instead => HOLD, count 0, gap 11.53h, with the claim that the 11:30Z firing produced NOTHING still printed.",
        "Full local control capture: .runtime/codex-seats/3.0.0_SA_CVO/round8-l9/os28-review/arm_a_controls.json. Controls performed without AWS, Task Scheduler or publisher invocation. Fixture histories are hypothetical; they are not substituted into the worker historical record."
      ]
    },
    "disposition": "GRADUATED",
    "spec_asserts": "Original arm (a) requires showing that the 11:30Z firing did not produce an artifact; the battery reports the gap census as evidence for that claim.",
    "world_is": "The count between nearest bracketing versions does not distinguish no firing from a publish shortly after the due instant. A controlled changed history is accepted while the printed no-publish claim remains.",
    "notes": "Future reuse can report a false HOLD; issuer owns disposition of that proof hazard. This observation neither adds a difference-control requirement to the original census nor independently changes the captured historical facts. No worker order, drained recut, runtime change or repetition of the live battery is issued. Routed for issuer handling through CTO."
  }
]
```
