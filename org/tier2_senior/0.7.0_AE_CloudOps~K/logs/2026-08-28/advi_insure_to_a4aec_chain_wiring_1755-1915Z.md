# INSURE becomes the canonical 49F session chain's THIRD runner target — 0.7.0_AE_CloudOps~K

**Serial:** 0.7.0_AE_CloudOps~K
**Session:** 2026-08-28 17:55Z – 19:15Z
**TO:** ADVI_INSURE.TO-A4-AEC (cell INS-a-5, decomp vintage `6a634f2f6f`)
**Archetype:** DEPLOYMENT (AE lane — Lambda code + Terraform + IAM + EventBridge)

## Objective

Wire the daily 49F insurance pull onto the canonical bd-pipeline 49F session chain as its third
runner target, rather than standing up a separate scheduler. Andrew-direct at the CTO terminal
17:40Z, verbatim: *"Yeah this would be a pipeline function, not an agent, we would need to build it
in the same bd api lambda route that is canonical in data/assets/docs/ or wherver"*. CTO ledger row
14 identified that route as this chain. Acts (a)–(d); the chain-wiring half only — the reporting-pull
Lambda's own code and env belong to 0.6.0_AE_PartnerETL under TO-A3-AE (c').

## Compiler Tools

| Tool | Command | Result | Note |
|---|---|---|---|
| comp-blast | `comp-blast bd-49f-session-trigger` | PASS | Rule-20 QUERY, never rebuild. Provenance read: kuzu_nessie_db 27054 nodes/58251 edges, Nessie HEAD current, built 18:08:30Z age 0.0h. Radius = runner + fees-runner, NOT reporting-pull — the graph agreeing this is a new edge. |
| comp-blast | `comp-blast <the .tf>` | HOLD surfaced | Citation READ, not skipped: the 20260702T1835Z modemarker-getobject ledger — status CLOSED, 5/5 legs proven. Not an active hold. |
| comp-iam | `comp-iam service bd-49f-session-trigger` | ADVISORY | 9 calls/9 statements: 2 GRANTED, 2 GRANTED-BROAD, 5 UNRESOLVABLE-RESOURCE — `lambda:InvokeFunction` at `:211` among them. Recorded as a FLOOR: it cannot see which ARN, so it cannot confirm or falsify the new grant. |
| comp-iam | `comp-iam gaps` (after the iam edit) | PASS-for-scope | 14 action-plane findings estate-wide, **0 naming this TO's subjects**. Necessary-not-sufficient, stated. |
| commit-gate.sh | on the `.py` | PASS | 1 of 1 clean (py_compile + ds-precommit + ruff py39). |
| terraform | `fmt -check` / `validate` | PASS | rc=0 / "Success!". `fmt -diff` never run — it WRITES; formatting resolved on a scratchpad COPY and diffed back. |
| deploy_ledger.py | `open` … `close` | PASS | Opened at deploy-START with 5 legs; CLOSED all 5 proven. |
| build-and-upload.sh | `bd-pipeline bd-49f-session-trigger` | PASS | import-closure OK; SHA256 `YZ3FHmwt…`; "write VERIFIED: size=7104, sha256 metadata match". |
| proof-of-spec-check.py | instance + expected-id list | VALID rc=0 | violations=0; alignment 5/5 criteria→cell, 1/1 cell_ref resolves, 1/1 declared cell reachable. |

## Deployment Sequence

| Step | Action | Result |
|---|---|---|
| 1 | Read source map BEFORE build (Rule 4) | `bd-49f-session-trigger` → files `["lambda_function.py"]`, tf_resource `module.bd_49f_session_trigger…` |
| 2 | Act (a) code + 3-arm exercise + RED arm | **14/14 green**, RED arm reachable |
| 3 | Commit acts (a)+(b) | `a57461f191` (msg-verify MATCH len=5429) |
| 4 | build-and-upload.sh | SHA256 `YZ3FHmwtWwag53zlm6XwbyNq8331A0TZpygqatswIJs=`, 7104 B, write VERIFIED |
| 5 | Saved `-target`'d plan (5 targets) | **3 to add, 2 to change, 0 to destroy** |
| 6 | CVO cert P2-i + P2-ii adopted, re-plan | same 3/2/0; commit `f526a00753` |
| 7 | FIRST REPORT + plan diff → CTO plan-gate | msgs 78671 / 78672 |
| 8 | CTO GO (read the diff, not the description) | msg 78677 |
| 9 | NEVER#6 ledger OPEN at deploy-START | `20260828T1840Z_advi-insure-a4aec-chain-wiring…` |
| 10 | `safe-apply` the SAVED plan file (HALT_ACK after reviewing 5 base-inbox msgs) | **"Apply complete! Resources: 3 added, 2 changed, 0 destroyed."** == plan exactly |
| 11 | 0-diff re-plan, on-target AND untargeted | both "No changes." — no foreign change in the root |
| 12 | Act (c) IAM, 5 arms, separate invocations | 3 allowed / 2 implicitDeny, all as predicted |
| 13 | Live read-backs | rule ENABLED cron(35 4); target input JSON; env var + CodeSha256 == build sha |
| 14 | record-deploy + source-map fix + tag | `17db393744`, `19c0f0c53b`, tag `bd-v2.56.0` |
| 15 | Ledger CLOSED 5/5 | "all 5 legs proven; sentinel removed" |

## Decisions Made

| Decision | Rationale |
|---|---|
| `_PAYLOAD_BY_TARGET` lives **inside** `_fire_runner`, keyed on TARGET | `_fire_runner` is the ONE path shared by the Lever-A skip leg (`:253`) and the runner-run leg (`:310`). Keying on target rather than on the firing leg means CTO's Lever-A indistinguishability condition survives by construction, not by care. |
| A target with no map entry gets **no `Payload` kwarg at all**, not an empty one | Those are different API calls; only the first is byte-identical to the pre-change invocation. Makes the main/fees invariant structural — no code path can give a non-insurance target a payload. |
| Adopted CVO P2-i: cross-root ARN by `data.aws_lambda_function` lookup | A literal ARN with a typo plans and applies cleanly and fails only at invoke, inside an unattended 04:35Z fire. The lookup fails AT PLAN. |
| Adopted CVO P2-ii and re-measured on BOTH transports | I had inherited "cot 02:00Z" from the file's own comment and asserted it as measured. It was copied. Corrected to the real neighbours. |
| Fixed the rule's `description` too, not just the comments | The description is a LIVE attribute shipped to AWS — the only carrier that actually deploys. A comment-only fix leaves the stale claim where readers see it. |
| Did NOT patch `record-terraform-deploy.sh` | Out of lane. Surfaced to CVO; corrected only my own function's map entry so Rule 4 is true. |
| Did NOT force-move tag `bd-v2.56.0` | `git tag -d` denied at this seat; not forced. The tag contains all four deploy commits, so it is valid if imprecise. Left for the integrator. |

## Files Modified

| File | Change | Committed |
|---|---|---|
| `infra/aws/lambda/bd-pipeline/bd-49f-session-trigger/lambda_function.py` | third target + payload map + conditional invoke kwargs | Yes — `a57461f191` |
| `infra/aws/terraform/bd-pipeline/bd-49f-session-chain.tf` | env var, ONE invoke ARN, new rule/target/permission, stagger census | Yes — `a57461f191`, `f526a00753` |
| `infra/aws/lambda/ci/lambda-source-map.json` | artifact sha (tool) + `last_deployed_commit` correction (hand) | Yes — `17db393744`, `19c0f0c53b` |
| `infra/aws/terraform/bd-pipeline/CHANGELOG.json` | deploy record | Yes — `17db393744` |
| `org/critical_paths/change_management/20260828T1840Z_…_deploy_completion.md` | NEVER#6 ledger, CLOSED 5/5 | Yes — `19c0f0c53b` |
| `org/tier2_senior/0.7.0_AE_CloudOps~K/deliverables/ADVI_INSURE.TO-A4-AEC_PROOF_OF_SPEC.json` | AC5 instance, VALID rc=0 | this commit |

## Verification

- **Apply counts == plan counts**, read from the apply's own line: 3 added / 2 changed / 0 destroyed.
- **0-diff twice**: on-target and untargeted. The untargeted clean is the stronger claim — no foreign
  change pending anywhere in bd-pipeline (CTO 78677 item 2 discharged).
- **Deployed bytes == build input**: live `CodeSha256` `YZ3FHmwt…` is byte-identical to the sha256
  `build-and-upload.sh` printed. Resolved through the source map, never by filename (Rule 22a).
- **IAM, 5 arms, 5 separate invocations, one `--resource-arns` each** (the 2+-ARN false-deny trap):
  reporting-pull allowed; bd-49f-runner allowed (positive control); fees-runner allowed; gold-dispatch
  implicitDeny (resource-axis fence); an unrelated role → reporting-pull implicitDeny (principal-axis
  fence). The action-name trap is self-discriminated — a nonexistent action can never return `allowed`.
- **Ordering dependency re-measured here, not accepted on report**: `INSURANCE_EGRESS="1"` live,
  LastModified 2026-08-28T18:09:29Z.

## Blockers

None at this seat. **AC4 is not blocked — it is not yet due.**

## Current State

Acts (a), (b), (c) COMPLETE and verified on the live plane. Ledger CLOSED, nothing half-landed.
The chain now carries three runner targets: main 00:00Z, insurance 04:35Z, fees 22:20Z MON-FRI.
AC1/AC2/AC3/AC5 PASS; AC4 **UNCOMPUTABLE pending the scheduled fire** (not FAIL, not
UNCOMPUTABLE-BY-CONSTRUCTION — nothing structural prevents it, only elapsed time).

## Next Steps

1. **2026-08-29T04:35Z — the first scheduled fire is the single acceptance** for both this TO and
   TO-A3-AE. Read both Lambdas' own logs, head-object per page, and the same day's 00:00Z main run
   as the negative control. No manual invoke — it would spend the acceptance.
2. Report AC4 to 2.0.0_SA_COO + 1.0.0_SA_CTO; 3.0.0_SA_CVO reads the fire once for both TOs.
3. Integrator: `bd-v2.56.0` is unpushed and may be re-pointed to `19c0f0c53b` if the change-commit
   precedent is preferred.

## Surprises Surfaced (INERT — routed, not chased)

1. `record-terraform-deploy.sh`'s source-map write **silently no-ops on this device and still
   commits** — `bun` is picked by an absolute-path test, then shells `git -C "/cygdrive/c/…"`, which
   a native Windows binary cannot resolve; it throws and falls back. A commit titled "ci: record
   deploy" lands while the record was not written. Same MSYS-argument class CLAUDE.md names for
   Python/PowerShell; bun is a third, uncovered caller.
2. That tool's docstring describes pre-ADHC_DRIFTD.001 behaviour the code no longer has. Reading the
   docstring alone would have produced a false hazard report; reading the code corrected it.
3. The `.tf` did not pass `fmt -check` at HEAD before this TO (rc=3, measured on a pristine copy) —
   6 pre-existing drift lines normalised, disclosed rather than claimed.
4. **Attribution:** `17db393744` carries 0.6.0_AE_PartnerETL's reporting-pull artifact sha, swept from
   the shared tree under my author line. Value true, authorship wrong; that seat was told directly.
5. **My own hold violation, owned:** commit `a57461f191` (18:22:21Z) landed 49s after window 17's OPEN
   reached my inbox (18:21:32Z). MSTR was right. The notice arrived mid-tool-call and surfaces only
   when the call returns, and `safe-commit` has no window check — so the hold binds only in the gaps
   between calls. Surfaced via COO per LD-0116; no gate built (not mine to install).
