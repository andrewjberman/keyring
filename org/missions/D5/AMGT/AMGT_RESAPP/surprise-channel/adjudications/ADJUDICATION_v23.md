# AMGT_RESAPP round 21: CVO adjudication

**Seat:** `3.0.0_SA_CVO~Z`. **Written:** 2026-09-21T23:3xZ at HEAD `98456d5664`. LOCAL on SITEZ.
**Inputs:** the COO's packet `ledger/ROUND21_L8_PACKET_20260921.md` @`98456d5664`; the six orders; rk-82's pair
(`NEVER_WIDEN_ROUND21_RK82_{COO,CTO}_HALF.md`); the channel census; read-only instruments from this seat over live IAM,
the live bucket, and a file-run of rk-84 AC3.

## Round state

**6 of 6 terminal** (rk-81 H0-store, rk-82 H0-iam, rk-83 H1, rk-84 H2, rk-85 H3, rk-86 H6). Acceptance **PASS 43 / FAIL
0 / UNVERIFIABLE 0 of 43 over 6 orders**; the order files carry 43 criterion ids (7+7+7+7+8+7); **judgment census 0 of
6.** The four round-14 orders superseded by the round-20 analysis read `superseded` (rk-32, rk-50, rk-51, rk-52), so the
project's only open order is rk-49, held on the Lusha key rotation.

## rk-82 -- the round's one live act (IAM), measured against its pair on the live policies

| the pair's claim | read live (`iam get-role-policy`) |
|---|---|
| `opal-amgt-scoped-api-grants`: 4 statements, 21 harvest GetObject resources | 4 statements, 21 |
| `amgt-resapp-chatter-axis-lambda-policy`: 4 statements, 8 harvest GetObject resources | 4 statements, 8 |
| each role's GetObject ARN set equals its `s3:prefix` list (both limbs of the grant) | equal in both roles |
| the grant is read-only | no S3 write action in either policy (the DynamoDB/logs write actions are other, unchanged statements) |
| the new prefixes are empty, so the added grant reads nothing yet | 8 new-grammar prefixes, 0 of 8 hold an object |

## The four channel writers wrote nothing -- measured over the whole bucket, all time

`opal-data-harvest` holds **0 objects** under any `*/harvest/bronze/` or `*/harvest/silver/` path, and 0 written since
the round-21 issuance (2026-09-21T23:21:02Z). "Code-only and off by default" holds as a population fact, not a per-cell
claim.

## rk-84 AC3 re-run from a FILE (the grader note on row W84-S1)

Typed inline, AC3's `b"\r\n"` escape is mangled by this box's tool transport, so the worker recorded a compensated run.
This seat wrote the invocation's Python to a file unchanged and ran it: `as_received_defs 1 vendor_source_defs 1`;
`m1 test_bronze_bytes_as_received rc 1 ... 1 failed`; `m2 test_vendor_source_routes rc 1 ... 1 failed`. The mutant file
carries a correct `b"\r\n"`. **Positive control added:** both arms against the unmutated module, rc 0, 1 passed each.
AC3 discriminates on its own literal invocation, not only on the compensated form.

```json
[
  {
    "id": "AMGT_RESAPP-Z-C-S367",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-21T23:35Z",
    "one_line": "L9 GRADE RECORD for round 21: 6 of 6 terminal, acceptance 43/0/0 of 43, no judgment criterion; rk-82's live IAM change matches its pair on every count; the channel writers wrote nothing (0 objects under any harvest bronze/silver path); rk-84 AC3 discriminates run from a file.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "Order files at 98456d5664: 43 criterion ids over 6 orders; parser reads the same; judgment=\"true\" in 0 of 6; --acceptance --round 21: PASS 43 / FAIL 0 / UNVERIFIABLE 0 of 43.",
        "iam get-role-policy, both roles: 4 statements each; 21 and 8 harvest GetObject resources; ARN set == s3:prefix set in both; no S3 write action; 8 new-grammar prefixes, 0 non-empty.",
        "list_objects_v2 over opal-data-harvest: 0 objects under */harvest/bronze/ or */harvest/silver/; 0 since 2026-09-21T23:21:02Z.",
        "rk-84 AC3 run from a file: m1 rc 1 and m2 rc 1 (1 failed each); control against the unmutated module rc 0 (1 passed each)."
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "spec_asserts": "Spine v3 L9: the CVO grades the round against the criteria that bound it.",
    "world_is": "Every criterion passes, and the one live act and the off-by-default writers are confirmed on the served planes.",
    "notes": "Grade carrier only.",
    "dismissal_reason": "Grade record: this row carries the round-21 L9 grade and dispositions no item; the enum has no record value."
  },
  {
    "id": "AMGT_RESAPP-Z-C-S368",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-21T23:35Z",
    "one_line": "DISMISSED: rk-84 AC3's inline b\"\\r\\n\" escape is mangled by this box's tool transport; run from a file exactly as written it discriminates (both mutants fail, both controls pass).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "W84-S1: typed inline, the invocation raises SyntaxError; the worker recorded a compensated run; disarmed by Z-S207.",
        "This seat's file run of the literal invocation: m1 rc 1, m2 rc 1; unmutated controls rc 0."
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "spec_asserts": "AC3's literal invocation runs as written.",
    "world_is": "It runs as written from a file; only the inline transport mangles it.",
    "notes": "An instrument trap of this device's transport, not a defect of the criterion or the cell. A criterion carrying a backslash escape inside a quoted python -c is safer written as a file the invocation runs.",
    "adjudicates": [
      "AMGT_RESAPP-Z-W84-S1"
    ],
    "dismissal_reason": "Graded on a file run of the literal invocation; it discriminates."
  },
  {
    "id": "AMGT_RESAPP-Z-C-S369",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-21T23:35Z",
    "one_line": "GRADUATED: a repo-wide import-identity trap -- lib/ has no __init__.py, so a test file can load a module as a bare top-level package, and two imports of one file become two module objects.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "1.0.0_SA_CTO~Z",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "W85-S1 (worker ~85), ARMED: lib/ carries no __init__.py; a test file loads as a bare package (packet s.1, drain message msg 24117).",
        "Routed by 2.0.0_SA_COO~Z to 1.0.0_SA_CTO~Z as a round-22 candidate."
      ]
    },
    "disposition": "GRADUATED",
    "spec_asserts": "A module has one identity however it is imported.",
    "world_is": "Depending on the import path, one file can be two modules, so state or patches set on one are invisible to the other.",
    "notes": "Remedy held by 1.0.0_SA_CTO~Z to rule into a round (a package marker or a single import convention, with a test that fails on a second identity). Repo-wide, so its blast radius is every suite, not this project's alone.",
    "adjudicates": [
      "AMGT_RESAPP-Z-W85-S1"
    ]
  }
]
```
