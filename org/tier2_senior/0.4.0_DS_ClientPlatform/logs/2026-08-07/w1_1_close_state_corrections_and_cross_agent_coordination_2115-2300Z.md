# W1-1 post-delivery: three record corrections, a de-escalated Tier-0 escalation, and two cross-agent unblocks

**archetype:** VALIDATE
**secondary_archetypes:** COORDINATE, SCRIBE

**Agent:** `0.4.0_DS_ClientPlatform` · **Window:** 2026-08-07 ~2115Z -> ~2300Z
**Prior log:** `mdpf_remed_w1_1_custody_repoint.md` @1f7525ca5b (this window is the delta since it)
**Commits:** `200c326df4`, `b6134a454c`, `9e32d95831` (all record-only; no code, no config, no S3)

---

## Summary

Zero code changed this window. It was entirely **verification and record integrity** on work already
delivered — and it moved the W1-1 verdict twice, in both directions.

The window's spine: **I de-escalated a Tier-0 escalation with a measurement, then narrowed my own
closure claim when Tier-0 corrected me back.** Both were right, and neither was deference.

## 1. The Lambda residual: escalated as a hard fail, measured as coherent

MSTR grounded the half I had correctly refused to claim — `scheduled-floor.tf:128`,
`cron(0 9 * * ? *)` America/New_York targeting `aws_lambda_function.mdpf_gold` — establishing that
**the 09:00 fire is the LAMBDA and the EC2 runner I QA'd is not the production path.** That part was
correct and stands.

They then escalated to CTO framing it as a hard 09:00 failure landing on `build_mdpf_spine.py:92`.
I pulled and unzipped the deployed package (`LastModified 2026-08-07T03:51:21Z`, sha
`XuLlClWT6kr6n5TCG7keFmzVd8KEafMuAIQutJB+utQ=`, 648,182B):

| packaged leg | state |
|---|---|
| `route_bindings.yaml` -> `ddb-cohort` / `opal-assets-daily-aua` | OLD |
| `build_mdpf_spine.py` -> asserts `spine.DDB_AUA_TABLE` | OLD |
| `dim_mdpf_aggregate_aua_timeseries.py` -> defines `DDB_AUA_TABLE` | OLD |

**All three OLD => internally coherent => `assert_bindings_current` PASSES.** The described failure
needs NEW code against OLD bindings, which is structurally impossible in a package that embeds both
and was never re-cut (`build_package.py` PACKAGE = 16 modules + `trading_calendar` + 3 configs at zip
root; no runtime S3 code pull). My S3 uploads cannot reach it — which is exactly *why* it is coherent
rather than mixed.

**Correct characterisation: stale-artifact hygiene, not an outage.** Corrections sent to MSTR 2150Z
and CTO 2152Z before anyone spent a night Terraform apply.

**MSTR retracted at 2157Z and re-derived it independently rather than accepting my de-escalation on
trust** — different legs (per-module `DDB_AUA_TABLE` ref counts, the packaged tie row at `:66`, plus
a repo-HEAD control I had not run). Two instruments, different derivations, same verdict.

**MSTR's own diagnosis is the transferable part:** they verified the artifact's VINTAGE correctly and
then read its BEHAVIOR out of the REPO — deployed-vs-repo substitution. And their hedge ("I have not
traced whether the invocation reaches the assertion in-process") pointed away from the binding gap,
which was *"is the packaged CODE also old?"* **A caveat that is not the binding one buys the
credibility of having hedged while the real hole stays open, and makes the claim harder to challenge
rather than easier.**

## 2. Then MSTR corrected ME, and they were right

At 2246Z MSTR walked back their own "hygiene / normal Terraform item" framing: **the re-cut is the
step that makes the W1-1 fix REAL**, and "unhurried" is not "optional." Concrete ask: do not mark
W1-1 complete-and-live.

Correct, and it is my own standard pointed at my own closure claim. Amended @9e32d95831 —
**CORRECT AND VERIFIED, NOT YET REACHING THE PRODUCTION PATH.**

Also re-framed by CTO's ruling, and recorded rather than smoothed over: **the EC2 leg I QA'd is
CUTOVER RESIDUE being retired**, not a production path (`scheduled-floor.tf:128` self-describes as
"cutover leg 2, same-apply atomic swap"; starter `ScheduleExpression` null on an INF marker dead
since 07-31; instance stopped). My QA exercised the only path my change could reach — a sanctioned
ad-hoc read, still the right call — but it is **not** evidence about the 09:00 path. Two claims,
neither substituting for the other.

## 3. Cross-agent (the coordination half)

- **`0.7.0_AE_CloudOps` UNBLOCKED (2241Z)** — they held their Andrew-direct W1-4 chain exercise on
  whether my deploy was imminent. Answer: landed ~2h prior. **But their premise needed correcting:
  my deploys cannot reach the Lambda they were invoking** (self-contained package). Gave them the
  step-1 `CodeSha256` start-pin, and pre-registered that **step 1 passes for the OLD reason — a green
  step 1 is NOT evidence my repoint works.** Plus the falsifiable expectation: 49F custody identical
  to served, any movement is a finding.
- **`0.8.0_AE_CloudComp` — my answer overturned their finding.** They had written that R-12 "names
  the wrong mechanism"; I showed the producer is the portal publisher (`R12_EXTRA_PAIRS`, named after
  their own register row, in a file outside the tree they censused) and that the gold/served
  spelling split (`account_units` vs `account-units`) is real at the gold->served boundary. They
  retracted and amended @0699c00b8f. **Their diagnosis: a correct measurement over the wrong
  domain** — exhaustive within `data/mdpf`, and the producer was never in `data/mdpf`. Denominators
  and named blind spots could not have caught it; only corroborating outside the instrument's domain.
- **Sequencing collision flagged to CTO (2249Z), already prevented.** CTO had confirmed no-apply
  tonight to AE at 224305Z, before their start. Redundant — and still the right call: raised twice
  costs one message, raised zero times costs a mixed-vintage result wearing a clean verdict.
- **My same-commit constraint on the re-cut was adopted verbatim** into the re-cut instruction and
  landed in the register at **R-31**: after the re-cut, step 1 must pass for the NEW reason (bindings
  + spine + consolidator repointed together); a partial pick-up IS the mix that hard-fails.

## Compiler Tools

| Tool | Invocation | Result | Note |
|---|---|---|---|
| `comp-find` | `account.units` / `non.model.assets` | PASS | Located `R12_EXTRA_PAIRS` in the portal publisher + both gold producers — the answer that overturned AE_CloudComp's finding. |
| raw `aws` (operational) | `lambda get-function` + zip pull/unzip | PASS | The decisive measurement: deployed package contents, not repo. `# rail-checked:` n/a — operational, not inspection. |
| raw `aws` (operational) | `events list-rules` -> **materialised 139 rules client-side** | PASS | Deliberately NOT a per-page `--query`; printed the denominator before reasoning over it. |
| `safe-commit.sh` | 3 record commits | PASS | risk-reflex CLEAN each time (measured vs 1,659 danger nodes). |

**Why no comp-pipescript / comp-validate / comp-blast this window:** zero code or config changed —
record corrections only. The Phase-1/2/3 mandates rode the implementing commit `f999fb25f6` and are
logged in the prior entry.

**What worked:** `comp-find` answered a peer's blocking question in one call by finding a producer in
a tree neither of us was censusing.

**Gap found (already routed, restated only because it recurred):** none new this window.

## My own errors, recorded

**None new this window** — but two of my prior claims were narrowed by me after acceptance:
the Lambda residual (from "would fail there" to "coherent, hygiene") and the close-state (from
"complete" to "not reaching production"). Both amendments were made after the work had already been
accepted, which is the only time narrowing costs anything.

## Blockers

**None.** W1-1's remaining step is outside the DS lane by rule and is explicitly no-night-action.

## Current State (zero-prior-context handoff)

- **`MDPF_COTTONWOOD.FIX1`: CLOSED COMPLETE** @e0a7a3ccbb (COO withdrew criterion 4 as their own
  mis-scoping). The fix is deployed and INERT ($0.00) pending a bronze-harvest ruling now sitting
  with Andrew as a sovereign call.
- **`MDPF_REMED.W1-1`: CORRECT AND VERIFIED, NOT COMPLETE-AND-LIVE.** Code @f999fb25f6; S3 scripts +
  `code/config/route_bindings.yaml` deployed and byte-verified; QA delta 0 of 439 dates with a
  negative-controlled comparator. **Reaches production only on the `mdpf-gold-lambda` re-cut.**
- **The re-cut** (CTO, Terraform-only, package + recorded sha256): unhurried, **CTO confirmed NO
  APPLY TONIGHT at 224305Z**. Constraint in register R-31: cut at a HEAD containing `f999fb25f6` so
  all four files land together.
- **EC2 leg = cutover residue**, being retired (R-19/R-20 ordering, reader before object). Not to be
  "fixed" or re-scheduled.
- **UNPUSHED: 2 commits** — `9e32d95831` (mine, close-state amendment) and `1dbfcdac90` (not mine,
  MDPF R-31/R-32 register). Lanes commit, integrators push.
- **Memory banked:** `feedback_an_atomic_commit_is_not_an_atomic_deploy_config_has_no_leg.md` —
  `safe-deploy`'s PIPELINE_MAP covers `scripts/*.py` only, so a config member of the same commit
  deploys as NOTHING, silently. Ungated; gate CANDIDATE routed to COO (nobody implements without
  Andrew's word).

## Next Steps

1. **[1.0.0_SA_CTO]** Re-cut `mdpf-gold-lambda` at a HEAD containing `f999fb25f6` (R-31). Unhurried;
   no served value moves when it lands.
2. **[integrator]** Push `9e32d95831`.
3. **[2.0.0_SA_COO]** Adjudicate W1-1 closure against the amended close-state (not complete-and-live).
4. **[2.0.0_SA_COO]** The `safe-deploy` config-leg gap — gate candidate only, pending Andrew.
