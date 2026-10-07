# LGIC_BLANKFIX -- surprise channel, INVESTIGATION v1 (laptop fabric)

**Opened by:** `2.0.0_SA_COO~G`. **Home:** the project tree's channel; the gate `.tools/surprise-row-gate.py` validates every NEW
row (schema `org/surprise_channel/schemas/investigation_item.schema.json`). Lane `ANY`. A seat's row is `LGIC_BLANKFIX-S<k>`; a
worker's is `LGIC_BLANKFIX-W<n>-S<k>`. **Append-only during the round.** Never edit an existing row.

## LGIC_BLANKFIX-S1 -- the naming library's tests are red at the base: 6 of 93 fail

```json
{
  "id": "LGIC_BLANKFIX-S1",
  "project": "LGIC_BLANKFIX",
  "fabric": "laptop",
  "surfaced_by": "2.0.0_SA_COO~G",
  "surfaced_at": "2026-10-07T12:30Z",
  "one_line": "The naming library's tests are red at the base: 6 of 93 fail before this project writes anything, so 'must stay green' (PRD C-CHECK) cannot be the bar a cell is graded on.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "python -m pytest lib/tests/test_opal_naming.py -q at HEAD ce2f42661d, laptop, 2026-10-07: 6 failed, 87 passed",
      "failing: test_grade_agrees_with_every_worked_case[inf-silver-chain|LAMBDA], [opal-portal-data-proxy-api|API_GW], [Inflection-SilverChain-DimConversionFailure|CW_ALARM], [wsb-49f-model-aua-pull-daily|SCHEDULE], [inf/otp-relay/token|SECRET]; test_lambda_plane_consumers_is_import_aware_not_a_bare_substring (assert 8 == 7)",
      "org/missions/D14/LGIC/LGIC_BLANKFIX/decompositions/LGIC_BLANKFIX_DECOMP.md base measurement 7"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "PRD v0.2 C-CHECK: a change to the grader lands in lib/opal_naming.py under LGIC_ENFORCE's existing tests, which must stay green.",
  "world_is": "Those tests are not green at the base. Five worked cases grade differently from their recorded answers (one prints 'portal/inf/otp-relay/token' where the case records '{system}/inf/otp-re...') and one consumer count reads 8 against a recorded 7. Cause not investigated; the registry was edited three times on 2026-10-07 after the cases were recorded. Round 1's cells are graded on 'no failure outside these six'. The owner of the six is LGIC_ENFORCE (held at stop)."
}
```

## LGIC_BLANKFIX-W2-S1 -- Neither .tools/naming-gate.py nor .tools/naming-apply-gate.py has a --self-test

```json
{
  "id": "LGIC_BLANKFIX-W2-S1",
  "project": "LGIC_BLANKFIX",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_LGIC_BLANKFIX~2",
  "surfaced_at": "2026-10-07T12:29:02Z",
  "one_line": "Neither .tools/naming-gate.py nor .tools/naming-apply-gate.py has a --self-test, so BF-t-2's step 3 ('each gate's own --self-test gains one arm') has nothing to extend; I added a --self-test to each (two arms: s3-access IAM_POLICY takes the fourth verdict and passes, pipeline-chain IAM_POLICY still refuses).",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "comp: python .tools/naming-gate.py --help at base 2894923538 lists only --diff, --enforce, --post-from-index (add_argument at .tools/naming-gate.py:1901-1903)",
      "python .tools/naming-apply-gate.py: add_argument at .tools/naming-apply-gate.py:379-382 lists dir, --plan-json, --enforce only",
      "after the edit: python .tools/naming-gate.py --self-test -> NAMING-GATE-SELF-TEST: PASS; python .tools/naming-apply-gate.py --self-test -> NAMING-APPLY-GATE-SELF-TEST: PASS"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO LGIC_BLANKFIX.TO-BF-t-2 build step 3 and BF2-AC3: each naming gate has its own --self-test that gains one arm and still passes.",
  "world_is": "Neither gate carried a --self-test. BF2-AC3 'both naming gates still pass their self-tests with the new arm' is therefore met by a self-test this order created, not by an existing one: it proves the two judge() paths handle the fourth value and keep refusing a group-B name, and says nothing about any prior self-test coverage because there was none. Both gates edited inside the order's paths; no other behavior changed."
}
```

## LGIC_BLANKFIX-W2-S2 -- One worked case in GRADING_RULE.md contradicts the fourth verdict: pandas-pyarrow-layer|LAMBDA_LAYER is record

```json
{
  "id": "LGIC_BLANKFIX-W2-S2",
  "project": "LGIC_BLANKFIX",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_LGIC_BLANKFIX~2",
  "surfaced_at": "2026-10-07T12:29:02Z",
  "one_line": "One worked case in GRADING_RULE.md contradicts the fourth verdict: pandas-pyarrow-layer|LAMBDA_LAYER is recorded OUT-OF-PATTERN with canonical {system}-pandas-pyarrow-layer, and grade() now returns NO-SYSTEM-ASKED with pandas-pyarrow-layer; the case is not in lib/tests/test_opal_naming.py, so I restated it there.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D14/LGIC/LGIC_NAMING/deliverables/GRADING_RULE.md worked_cases: {name pandas-pyarrow-layer, type LAMBDA_LAYER, verdict OUT-OF-PATTERN, canonical_form {system}-pandas-pyarrow-layer, why 'R1.e ... so {system}'}",
      "python -m pytest lib/tests/test_opal_naming.py before restating it: 8 failed (the six at base + this case + test_iv3_controls[CloudWatchLogs-IAM_POLICY-...]); after: 6 failed, the same six",
      "lib/tests/test_opal_naming.py _FOURTH_VERDICT_CASES (one entry) and test_iv3_controls CloudWatchLogs row updated to NO-SYSTEM-ASKED"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO LGIC_BLANKFIX.TO-BF-t-2: where a worked case in lib/tests/test_opal_naming.py records OUT-OF-PATTERN for a group-A name, update that case to the fourth value.",
  "world_is": "The worked cases live in GRADING_RULE.md, outside this order's grant, not in the test file. I did not edit GRADING_RULE.md; test_opal_naming.py overrides the one case at load time and names why. GRADING_RULE.md still says R1.e yields {system} for a library layer and its V-2 wording is stale; its owner is LGIC_NAMING / the issuer."
}
```

## LGIC_BLANKFIX-W2-S3 -- infra/logic/render_naming_section.py renders only grade.ALIAS and grade.OUT-OF-PATTERN as verdict sentences (l

```json
{
  "id": "LGIC_BLANKFIX-W2-S3",
  "project": "LGIC_BLANKFIX",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_LGIC_BLANKFIX~2",
  "surfaced_at": "2026-10-07T12:29:02Z",
  "one_line": "infra/logic/render_naming_section.py renders only grade.ALIAS and grade.OUT-OF-PATTERN as verdict sentences (line 324), so the new grade.NO-SYSTEM-ASKED sentence is not carried into the canon's generated section; the verdicts closed list (line 322) does follow the schema and will show four.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "infra/logic/render_naming_section.py:322-326: verdicts list read as a whole, then for field in ('ALIAS','OUT-OF-PATTERN') each sentence rendered; no other verdict key is read",
      "python infra/logic/render_naming_section.py --check at this worktree: CHECK: STALE -- 3 failure(s), section stamp NAMING_SCHEMA v1.10 vs render v1.15 (the section was already 4 versions behind v1.14 at the base, so staleness is not caused by this order)",
      "--content-diff after the edit: CONTENT-DIFF 30, includes /grade/not_graded and /grade/unplaceable as DROPPED; the renderer reads no /grade/NO-SYSTEM-ASKED key, so that sentence is not rendered"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO LGIC_BLANKFIX.TO-BF-t-2: read each outside reader of a verdict; for any that would mishandle the fourth value, file one row naming file and line.",
  "world_is": "The renderer does not fail on the fourth value, but it will print a four-value verdict list with no sentence saying what the fourth means, until its field tuple at line 324 gains NO-SYSTEM-ASKED. Also read, no row owed: lib/opal_lgctfm.py:251-278 records the verdict verbatim and TENSION_VERDICTS (line 1157) leaves NO-SYSTEM-ASKED out, so such a name raises no TENSION row, consistent with 'no remedy owed' (the comment at 1151-1157 does not name it); .tools/safe-apply.sh:92-94 is a comment and delegates to the two gates; infra/logic/registry/exemptions.json lines 33 and 192 mention OUT-OF-PATTERN only inside prose reasons."
}
```
