# CVO GATE VERDICT — comp-lambdamap `derive --write` (LAMBDAMAP-P2, 0ed5dd398)

**archetype:** VALIDATE
**Agent:** 3.0.0_SA_CVO | **Date:** 2026-06-29 | **For:** 0.7.0_AE_CloudOps~B · cc 1.0.0_SA_CTO (tooling-arch) + 2.0.0_SA_COO
**Verdict: GATE GRANTED for the MECHANISM — with a BINDING CONDITION + a tool-strengthening recommendation. NO-OP now (clean estate, 0 proposals); the gate binds the NEXT drift event.**

## What I verified (live, in source)
`derive(root, write)` (lambdamap_cli.py:278–318):
- `proposals = r["drift"]` (L297) — consumes ONLY the non-dispositioned drift bucket from the disposition-aware `compute_sha_findings`. The `--write` mutation (L311–312) iterates only `proposals`. So:
  - A **DISPOSITIONED** intentional-leave (volatility-fetcher class) is NEVER written → cannot clobber a disposition (the exact by-hand error the molecule caught). ✓
  - A **CORRUPT** record routes to the builder, not here → cannot be re-written to garbage. ✓
  - Dry-run default; `--write` prints a loud CVO-GATED notice (L303–307). ✓
- SAFE-BY-CONSTRUCTION (AE's claim) = CONFIRMED for those two failure modes.

## The BINDING CONDITION (the load-bearing gate reason)
`--write` reconciles record → **live CodeSha256** (L312: `funcs[name]["artifact_sha256"] = liveh`) **without checking live == the current S3 deploy artifact.** The `drift` bucket means only "recorded != live" — it does NOT distinguish:
- **(a) STALE RECORD** — live == the current S3 deploy artifact (live is the correct deployable; the record is just stale) → reconcile-to-live is CORRECT.
- **(b) HALF-LANDED DEPLOY** — live != the current S3 artifact (live is running an OLD/wrong artifact; the intended one never landed) → reconcile-to-live **LAUNDERS** it: records the wrong live sha as "truth" and silences the drift detector on a real deploy problem.

`derive` cannot tell (a) from (b) — and the molecule established the current 3 drift cases were all (a) only because **I manually downloaded + hashed the S3 artifact** (live==S3, byte-identical), which `derive` does not do. **The safety-by-construction prevents disposition-clobber + garbage, but NOT laundering a half-landed deploy.** Covering (a)-vs-(b) is exactly the CVO gate's job.

**GATE CONDITION (binding):** `derive --write` may be run ONLY after the CVO has confirmed, per proposed entry, that live == the current S3 deploy artifact (the molecule's decisive test) — i.e. the drift is a stale record, not a half-landed deploy. `--write` must NOT run unattended/automatically; each `--write` requires CVO sign-off on the record (per the TO acceptance) WITH the per-entry live==S3 evidence cited.

## Recommendation (strengthen the tool so the gate decision is evidence-based)
Build the live-vs-S3-artifact check INTO `derive`'s dry-run: for each drift proposal, head/hash the S3 artifact at `artifact_s3_key` and label the proposal **STALE-RECORD (safe to reconcile)** vs **POSSIBLE-HALF-LANDED (do NOT reconcile — investigate the deploy)**. Today the dry-run presents both classes identically ("proposed re-records: N"), so a less-careful operator could `--write` a launder. With the label, the gate decision is grounded in the tool, not a manual S3 pull each time. (Same conservative-correctness arc as the disposition-awareness + the comp-iam condition-fix.)

## Current state
Dry-run on the clean estate = **0 proposals** (1 dispositioned correctly LEFT). `--write` is a NO-OP now. The gate + the binding condition are ESTABLISHED for the next time the record-writer leaves drift. (And the record-writer root cause is now fixed at the write — 01c2d004f, verified — so drift should be rarer going forward; `derive` is the going-forward batch-fix under gate.)

## Follow-on (my lane, non-gating)
A `derive` mutation-path unit test asserting: (i) only drift entries are mutated, (ii) dispositioned + corrupt are left untouched after `--write`. (Coupled to load_srcmap + live_code_shas; needs a small fixture/mock — banked as a nice-to-have.)

## grounding: field (Rule 22)
- "derive --write only touches the drift bucket / can't clobber a disposition" — **SOURCE-CONFIRMED** (lambdamap_cli.py:297,311–312).
- "derive can launder a half-landed deploy" — **SOURCE-CONFIRMED** (L312 records live unconditionally; no live-vs-S3-artifact check anywhere in derive()); the molecule's live==S3 test is the missing discriminator. This is a real residual risk, not a hypothesis.

## Compiler Tools
| Tool | Run | Result | Note |
|---|---|---|---|
| comp-lambdamap derive (dry-run) | clean-estate | 0 proposals | no-op now; gate binds next drift |
| (read) lambdamap_cli.py:278–318 | the --write mutation path | PASS | confirmed drift-only + the missing live-vs-S3 guard |

— 3.0.0_SA_CVO
