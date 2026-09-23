# IRPT paired integration for Andrew visual smoke

CTO record, measured 2026-09-23 04:25-04:32 UTC. Authority: ANDREW_DIRECT_VISUAL_SMOKE_20260923.md at 683c36c277.

## Measured inputs

| Repository/surface | Exact input | Disposition |
|---|---|---|
| Backend Y integrated code | cdbd4de74d86c03463eed8068e57c41e0bf8abc1 | Includes P d91b2bdd10, M 8e2ba78303 and B 2506c70874 by ancestry. Use as assembly input. |
| Backend X10 | 8909d8a77bbbaea2e8864ff6b2472fa078c57888 | Three unique commits: ffbffcac50, 40a1ced34e, 8909d8a77b. Reconcile two owned stamps with newer runner/loaders. PENDING_ENFORCEMENT remains. |
| Portal Y integrated code | 7a5b24e705f79d5df872f9a443b6a552e9de62b9 | Includes P 7411ada335 and final F 8e6e2e38cc by ancestry. |
| Portal M | d4fca0e5692730e9f79c3fa013159ffa63ba5b6b | All three unique M commits patch-equivalent in Y; verify behaviors, do not duplicate replay. |
| Portal origin DEV | b3d5f59b4534eb653105f9bedc9e178384111c9f | Must preserve newer remote SecurityAnalysis/MFA changes and IRPT admin/internal/Dev page, print and nav restrictions. |
| Portal shared local DEV | 8e6e2e38cc299c4415d42b0fe627edc50ec35e1b | 110 local-only / 28 origin-only commits; not current P/M/Y candidate. Preserve untracked local artifacts. |
| F89/F90 backend worktrees | 4d967ed8279b83131203a377f3e06213e1b91391 / 3fd911306d9e943f75f4f785272c053038b87033 | Unique root changes are evidence/proof/task-order records, 12/4 files. Portal counterparts already in final F baseline. Preserve completion evidence. |

M/P/Y confirm no active source writers at the supplied pins. Review-only worktrees and M rp10 scratch contain no additional unique delivery; preserve them. v-irpt-l4probe has no unique committed delta versus CLOUD and no tracked dirty source. Excluded mstr-naming-waiver history remains excluded. Do not integrate unrelated worktree branches.

## Serving and CI evidence

Latest production pin is f2ff7a0af2245cac624ff8a340d5d5e0b10e14aa. Portal run 35764794492 reports successful build, S3/CloudFront deployment and tag on 2026-09-22 at 18:04-18:07 UTC. Annotated portal-v2.1.183 peels to that exact pin. This is the existing production deployment, not the new integration.

DEV CI run 35764483180 at b3d5f59b failed Run ESLint: five errors in SentimentGauge unused imports (2), IRPT pre-envelope unused import, alias-probe constant expression, and ExportButton mutation rule. P is authorized to repair surviving narrow errors on the assembled candidate, preserving runtime/test semantics and without disabling checks. Current production deploy success does not erase DEV lint failure.

## Execution ownership

P constructs an isolated paired candidate, reconciles remote changes and X10, validates lint/typecheck/build and relevant consumer tests, and supplies exact merge pins and validation receipts. CTO checks scope and conflicts. MSTR executes coordinated shared integration/push and portal promotion under the repository procedure, preserving unrelated working changes and the DEV main checkout. No shared write race. The source manifest must account for unique worktree changes and equivalent patches.

The earlier local-preview request is SUPERSEDED by Andrew's direct instruction relayed by COO~P in the exact 20260923T044628Z inbox message: "i dont need all that, i can manage the visual smoke, i need the most completed version pushed to DEV and then DEV promoted to PROD in canonical form (/prod-deploy claude skill)." Stop preview work. Publish the validated completed candidate to DEV, then promote DEV to PROD through the canonical procedure. Andrew performs visual smoke; do not add another visual-review or approval gate. Preserve the existing M port 5440 listener.

At 04:46:28 UTC, P reports Portal 3e5a6813 includes Y 7a5b24e7 and remote DEV b3d5f59b, with lint zero errors / 106 warnings, typecheck/build PASS, 80 focused tests plus mounted header/holdings PASS. Backend cd8d118254 includes Y cdbd4de7, X10 and F89/F90 evidence. These are candidate receipts, not proof of shared publication or deployment. CTO acknowledged P and routed publication coordination to MSTR at 04:50 UTC; final full pins and remote/deployment receipts remain to be recorded.

Full custody/economic, maintained-source production wiring, current policy/IAM, vendor/effecting worker, rendering/export and E2E verdicts remain separate. No keys, live vendor action or backend deployment is authorized merely by a frontend build. Final shared origin and production receipts are pending at this record; Andrew's visual smoke follows publication.
