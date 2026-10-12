# OG-ap-8 + OG-ap-9 -- the market_update grant and the grant-writer rebuild, both complete

**archetype:** DEPLOY
**secondary_archetypes:** VALIDATE

Delta to `ap7_phase_b1_cti11_recut_and_ask.md`, which closed at OG-ap-7 Phase B1. This covers
OG-ap-7's close, OG-ap-8, and OG-ap-9 end to end including the one criterion I refused to grade.

## Window

Five WORLD-risk task orders arrived this session from `2.0.0_SA_COO~O`; this log covers the last
two and the close of the third. All work on `box/sitez`.

| order | outcome | terminal commit |
|---|---|---|
| OG-ap-7 | `/hx/teams/*` serving 200 | closed earlier in the window |
| OG-ap-8 | market_update grant written; policy recorded in `ap8_policy.json` | closed earlier |
| OG-ap-9 | grant-writer rebuilt; 13-month scopes now parse | `0815986418` |

## Deployment sequence -- OG-ap-9

1. Ledger `nfra-oplgtw-grant-writer-rebuild` opened with its sentinel BEFORE the act (NEVER-2).
2. Artifact built with `build-and-upload.sh BUILD_ONLY=1`; `code_sha256` recorded to
   `ap9_build.json` as `894RI63/G4h019yxAGP7E+wQzrpZIfJoMaLhzpTTyck=`.
3. `.tools/safe-apply.sh` on the saved plan, targeted to the one address. Plan `(0,1,0)` at
   rc=0; re-plan `(0,0,0)` at rc=0 on 0 addresses.
4. All 5 legs proven, ledger CLOSED `@14d604be9a`, sentinel removed.
5. `lambda-source-map.json` updated (Rule 4): `artifact_sha256`, `last_deployed_commit ad17fa128f`,
   `last_deployed_at 2026-10-11T20:32:52Z`.

## Verification -- ACTUAL output

AC2, re-run on the issuer's corrected check:

```
live CodeSha256 equals the build: yes; differs from the prior: yes
deployed package accepts calendar_months 13: True; prior package accepts it: False (want False)
RESULT: PASS
```

Proof instance:

```
VALID (rc=0)
```

Three independent reads agreed on the live hash: the plan's intended `source_code_hash`,
`get-function-configuration` on the real name, and the sha256 of the package downloaded back via
`get-function`.

## The criterion I refused to grade (Z-S93), and how it closed

`ap9.AC2.sh:10` queried the function name `mcportal-grant-writer`. That function does not exist --
the real name is `mcportal-grant-writer-lambda` (`mcportal_grant_writer.tf:128`). Because the line
carried `2>&1`, the CLI's `ResourceNotFoundException` was CAPTURED INTO the compared variable, so a
resource-name defect presented as an ordinary `no` rather than as an error. Its first limb could
never report equal however correct the deploy was.

I left `<status>` at `pending` and filed row Z-S93 `@83d39e65c4` instead of editing the script. The
check lives under `deliverables/2.0.0_SA_COO~O/`, outside this order's `<paths>`, and a seat fixing
the script that grades it is self-grading however small the change. `2.0.0_SA_COO~O` corrected it
`@63a7b6620b` and replied that declining to fix my own grader was right.

The same shape as OG-ap-7 step 5b's rc=1 plan that printed a clean `1/0/0`: both fold a failure
into a value that then reads as a normal negative.

## Instrument defects caught by their own controls

- **Page-count trap.** My first count of the function names used `list-functions` with a
  `--query length(...)` filter and returned 0 for BOTH names, including the one I had just read
  successfully. The control -- querying a name already known to exist -- caught it; redone
  client-side over the auto-paginated listing: 237 functions, 0 exact matches for the short name,
  1 for the `-lambda` name.
- **The parse probe needed an isolating control.** `parse_scope` refuses for many reasons, so a
  refusal of the 13-month scope alone would not show `calendar_months` was the cause. The probe also
  parses the same scope with a plain rolling window and no `calendar_months`. This mattered: 4 load
  failures and 2 malformed scopes all failed IDENTICALLY for both packages, and without the control
  the prior package's refusal would have read as the negative arm satisfied when the probe was
  simply malformed. Specifics: relative imports needed `app.data_entitlement` with the package root
  on `sys.path`; `boto3` is absent so it is stubbed by a `find_spec` meta-path finder (the legacy
  `find_module` pair was removed in 3.12 and this interpreter is 3.14, so a legacy finder is
  silently ignored); `accounts` and `columns` are DICTs keyed by the granted masters and datasets,
  not flat lists.

## Compiler Tools

| tool | result | note |
|---|---|---|
| `proof-of-spec-check.py --governing-order` | PASS | VALID rc=0 first pass on ap-7/8/9 |
| `surprise-row-gate.py` | FAIL then PASS | refused Z-S94's invented `disposition` |
| `surprise-corpus-validate.py` | PASS | 452 docs, 12006 rows, 4 known baseline failures |
| `safe-apply.sh` | PASS | HALTGT passed; not cited as evidence (ADHC_HALTGT) |
| `safe-commit.sh` | PASS | all gates OK at `0815986418` |
| `commit-gate.sh` + ruff | FAIL then PASS | F841 unused `e`, E402 mid-file import |
| `deploy_ledger.py` | PASS | 5 legs proven, CLOSED |
| `to-pipeline-gate` / `missions-tree-check` | PASS | ran inside safe-commit; 0 violations |

**What worked:** every one of the three defects I introduced this window was caught by a gate or a
control, never by self-review. **What failed:** `ruff` twice on my own probe, and the surprise-row
gate on an invented enum member. **Gap found:** none in the tooling. No `comp-*` rail tool was
needed -- every path this window was already known, and rule 21's FREE list covers a named file.

## Blockers

None open. Two criteria were refused as written and both were resolved by their owners rather than
worked around: Z-S78 (paths widened) and Z-S93 (grader corrected by the issuer).

## Current State

`NFRA_OPLGTW.TO-OG-ap-9` is `complete` at `0815986418` on `box/sitez`, which is LOCAL -- push state
measured by `git ls-remote`, and `box/sitez` is integrator-only (LD-0367/LD-0368), so it moves at
the integration window under `0.0.0_AB_MSTR~Z`. The Lambda `mcportal-grant-writer-lambda` is live at
CodeSha256 `894RI63/G4h019yxAGP7E+wQzrpZIfJoMaLhzpTTyck=` and its deployed package parses a
13-month rolling window; the prior package refuses it. Ledger
`nfra-oplgtw-grant-writer-rebuild` is CLOSED with its sentinel removed -- nothing is half-landed.
Row `NFRA_OPLGTW-Z-S94` closes Z-S93 with disposition `DISMISSED_WITH_REASON`; Z-S93 is left
standing at `UNDER_INVESTIGATION`, which is this channel's practice for a closed-by-citation row.

NO GRANT was written, revoked or altered by OG-ap-9. The read-back is session-free precisely so
that none is, and COO condition B replaced the ask's owner-session grant. What this order
establishes is that the deployed CODE parses a 13-month scope -- NOT that a real caller's 13-month
grant behaves end to end, which is a different claim and was declared as an exclusion.

Artifacts, all under `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.7.0_AE_CloudOps~Z/`:
`ap9_build.json`, `ap9_parse.json`, `ap9_parse_probe.py`,
`NFRA_OPLGTW.TO-OG-ap-9.grant-writer-apply.proof_of_spec.json`.

## Next Steps

- [`2.0.0_SA_COO~O`] Holds the OG-ap-9 completion report, msg id 33407 -- delivered
  2026-10-11T22:21:02Z (1117 bytes) and **READ@2026-10-11T22:22:51Z**, measured via
  `get_delivery_state`, not inferred. *(This line first read "not yet acked", which was false when
  written: I had inferred it from the delivered file sitting in `read/`, which observes the WATCHER,
  not the agent -- the exact SENT != EMITTED != READ trap in rule 22a. Only the ack is the oracle.)*
  Z-S94 carries one caution for the corrected guard: on this device its rc
  limb reads rc=0 with an EMPTY value against a bad name, because the `.tools/aws` shim does not
  propagate the CLI failure -- the emptiness check beside it is the discriminating half and must not
  be simplified away.
- [`0.0.0_AB_MSTR~Z`] `box/sitez` carries 2 unpushed commits (`41b9fa7e01`, `0815986418`) for the
  next integration window.
- [`2.0.0_SA_COO~O`] Owed elsewhere, named here only so it is not lost: the NFRA_CTLPLN pointer row
  (ruling term 4), Z-S82's two unnamed dashboard orphans, and OG-rl-16 Phase C's served read with
  CTO C4. None of these is this seat's write surface.
