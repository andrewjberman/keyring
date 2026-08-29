# 1.0.0_SA_CTO~Z -- D1_CATVIEWS increment 2: staged to the sovereign gate (0210-0300Z)

**archetype:** COORDINATE
**secondary_archetypes:** VALIDATE, DIAGNOSE

Lane `~Z` (site Z). Window: 0210Z -> 0300Z, 2026-08-29.

## Outcome

Andrew's increment-2 ask (*"client residual sorted out on Global and Cottonwood, populate SMAs for
49F at L1, get the Tax SMA accounts in"*) is BUILT, DEPLOYED and VERIFIED except item 3, and the
whole sequence is HELD at one sovereign decision: a reserved-category delete of 16 dated gold keys.

```
  items 1 (cottonwood + global legs) . 2 . d-1   committed, pushed, packaged, deployed, VERIFIED
  5-leg acceptance predicate                     GREEN across TWO planes (zip + function config)
  16 conflict-held keys                          ENUMERATED, put to Andrew, UNTOUCHED
  portal DEV                                     clean; D-3 colours + D-4 fee panel ALREADY on PROD
  item 3 (Tax SMA -> ALT Strategies)             RULED OUT tonight -- STRUCTURAL, reported as such
  OUTSTANDING                                    ANDREW'S YES/NO. Nothing else has a waiting owner.
```

## Current State (zero-prior-context handoff)

- **`mdpf-gold-lambda`** @ `CodeSha256 U/87M1NBA/xG98kQ3Zaik5O2jgH/GY8Ps2doIRzLchA=`,
  `LastModified 2026-08-29T02:55:49Z`, pin **`73c2dea263aa31a5b8906e2685902061d1a34d78`**.
  22/22 packaged modules identical to `git show <pin>:<repo_path>`.
  `Environment.MDPF_GOLD_COMMIT == 73c2dea263...` (was stale at `7604f2b4bd` through TWO rebuilds).
- **`infra/aws/terraform/mdpf-pipeline/gold-lambda.tf:222`** now carries the pin literal. Applied via
  `safe-apply` (env-only: CodeSha256 correctly did NOT move).
- **Ledger** `org/critical_paths/change_management/20260829T0214Z_d1-catviews-second-reland-tonight_deploy_completion.md`
  OPEN, all legs OPEN, 6h window. Opened BEFORE the act by `0.7.0_AE_CloudOps~Z`.
- **Delete set**: 16 keys, 4 artifact types x 4 scopes under `portal/gold/mdpf/`, as_of 2026-08-27
  (account-distribution 08-28 for 49financial/inflection/global). Enumerate with
  `python .claude/skills/mdpf-refresh/mdpf_refresh.py --reland` (dry-run).
- **Business figures that will render**: cottonwood Client 0.76% Opal-Supervised
  ($2,253,034.08 of $294,905,777.43); global Client 100% ($267,632,047.22) -- the latter FOLLOWS from
  49financial's `CLIENT_L1_ALL_SUPERVISED` rule plus basis B (global's Client population is 49F-only).
- **`CLIENT_L1_HELD == ['cottonwood']` MUST NOT BE LIFTED.** `global_client_l1_blockers()` returning
  `[]` reaches an unconditional `raise` in `client_l1_split(GLOBAL_SCOPE)`. Blocking item owner
  `1.0.0_SA_CTO~Z`, ARMED->DISARMED same-turn.

## Rulings issued

| # | Ruling | Note |
|---|---|---|
| 1 | Hyphen misses in `CANONICAL_KEY` are ON-CONTRACT; wire item 1 | positive control superseded by the account_count denominator |
| 2 | Global aggregation shape **(B)**, constituent set DERIVED not literal | superseded COO 15438's bar, with reasons |
| 3 | `CLIENT_L1_HELD` not lifted | the entry is load-bearing for an unbuilt branch |
| 4 | Delete is CERTAIN not conditional; floor cannot land item 1 | same trading day -> same as_of -> conditional_put conflict |
| 5 | On a NO: ledger closes SUPERSEDED **for the reland legs only**; 2 portal AC5 commits RE-HOMED, not auto-promoted | pre-decided so it never reaches Andrew |
| 6 | 22-member rule STANDING: any commit to a packaged member re-stales the lambda | "commit is the deploy" is FALSE of the zip |
| 7 | D4 completion text must name SATURDAY by date; AC4 stays OPEN | a green fire is not an after-image |

## Compiler Tools

| Tool | Use | Result |
|---|---|---|
| `comp-find` (via rail) | census `MDPF_GOLD_COMMIT` | PASS -- count=1 in consolidator, 5 estate-wide |
| rail `# rail-checked:` | build-script sourcing + .tf literal reads | PASS -- no comp-tool reads a build script's source-selection or a literal's value |
| `mdpf_refresh.py --reland` | dry-run enumeration | PASS -- 16 keys named |
| boto3 `get-function` | 5-leg predicate, ONE read | PASS -- all five green |

**What worked:** pinning config+code to a SINGLE `get-function` response. **What failed:** a grep
marker taken from the `+` side of a diff that the OLD code also emitted -- a false all-clear on a
stale lambda. **Gap found:** a 4-leg gate entirely inside ONE carrier (the zip) could not see the
env-var plane; LEG 5 added.

## Blockers

- **BLOCKED at Andrew (evidence-cited):** reserved-category delete of the 16 enumerated keys.
  Both limbs coherent -- YES serves tonight at as_of 2026-08-27; NO serves Monday on the scheduled
  run at a NEW dated key (`existing is None` -> clean write), zero reserved acts.
- **NOT blocked, ruled out:** item 3. Gold artifact has no member axis (86 cols at
  Segment/Asset/Account/Class grain). No producer edit reaches it.

## Next Steps

- [`0.7.0_AE_CloudOps~Z`] On YES: `--reland --confirm` against the 16, then floor, publish, L4.
  On NO: close ledger SUPERSEDED naming the reland legs ONLY.
- [`0.4.0_DT_ClientPlatform~Z`] Promote after L4 (YES) or await a separate decision (NO).
- [open, unowned] Derive `MDPF_GOLD_COMMIT` from the packaged manifest -- the hand-edited literal is
  a two-carrier design that will drift again.
- [open] `unmapped_leaves` is in-process only, not on the emitted artifact.
- [open] 3-of-4 `process_time` exemption defect; `r7_comparator.py:284` second unguarded subscript.
