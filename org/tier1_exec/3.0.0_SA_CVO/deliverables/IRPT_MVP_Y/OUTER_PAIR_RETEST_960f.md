# Public-wire repair: Y's independent bounded closure

Reviewer `3.0.0_SA_CVO~Y`; authority completion CONTRACT.md, CTO54b242b9cd and
exact013256. Backend **960f5f2a4501eff2670bcd0b5951926836093447** paired with
portal **c09fea54e9f4613d44b874724e93b79c443f8cc8** (replacement atop assembled
42412eb8). **Y-W01 and Y-W02 CLOSED for this exact pair.** Y-W01 is the alias
of P's R-P11; this is Y's independent verdict, not a substitute for CVO~P's
separate required verdict. All14 integrated Y/S criteria remain NOT_EVALUATED.

## Unchanged original controls

Original `probe_outer_pair.py` and `probe_outer_pair.test.ts` remain identical to
committed64a2c522ef6144de657f6afccb5e7a3536b9aa49 (Git diff empty; text hashes in
the retest receipt). `retest_outer_pair_960f.py` asserts this before running them.
It changes only Python candidate and output-directory bindings in memory; no
case, mutation, assertion or expected result is changed. TypeScript uses its
existing environment bindings without code changes. Fresh actual Entry outputs
go under `OUTER_RETEST_960f/`; their legacy7915 basenames allow the original
reader to run unchanged, while the review and validation receipts record the
new exact backend pin and bind the regenerated wire files to it.
The original failed-run artifacts remain intact in the parent directory.

Results:

| Evidence | Independently measured result |
|---|---|
| Actual Entry fixture generator, including supplied internal diagnostic control | 3 supplied tests PASS |
| Original closed-schema controls | 24 PASS |
| Original four raw public-refusal observations | 4 have no exposed server-only fields and no public-schema errors |
| Original consumer controls | 20 PASS, 0 FAIL; 53 assertions |
| Added internal/projection/schema negatives | 8 controls PASS |
| Added actual selection controls | 4 controls PASS |
| Added selection/parser CID negatives | 6 controls PASS; 9 assertions |
| Focused supplied portal tests | 21 PASS; 118 assertions |
| Application TypeScript check | `tsc -p tsconfig.app.json --noEmit`, exit0 |

These are separate denominators. Original13PASS/7FAIL is historical; all seven
original malformed ordinary-status/grant mutations now throw before adaptation.
Valid ordinary single-date, undated/per-section, nonready and old-consumer wires
still preserve their facts. Wrong-lane and null-extension negatives still refuse.

## Projection and actual selection evidence

Fresh history/read/sections/status refusals validate directly against the public
shape. Reinserting internal_correlation_id into each is rejected by both public
schema and actual portal parser. The internal status builder still returns the
supplied correlation ID for each operation, validates as internal StatusEnvelope,
and is not mutated by the public projection. Public status equals internal status
with only that marked field removed.

`probe_public_selection_960f.py` invokes the actual directory Entry with recorded
directory/ownership and persistence doubles. Selecting an allowed account returns
that exact account. Selecting a partially unauthorized relationship refuses
OBJECT_NOT_COVERED without a persisted selection or data. Its fresh refusal
equals the repaired portal capture and validates publicly. CID reinsertion fails
the schema and parser. This is a selection-wire control, not custody input proof.

The source CONTRACT.md error-envelope row and internal-status section explicitly
resolve the previous CID wording conflict. BoundaryRefusal now references
PublicStatusEnvelope. P's served.py blob equals M483a2fee0a's blob:
`713c8ae55bcd8aab0097f331db76fd8f2ae601d4`. Source binding receipt is retained.

## Reproduction, corrections and limits

Run `retest_outer_pair_960f.py`, then `probe_public_selection_960f.py`, then
`bun test probe_public_projection_960f.test.ts` with IRPT_PORTAL_REVIEW_ROOT
pointing at the exact portal snapshot and IRPT_OUTER_EVIDENCE_ROOT at
`OUTER_RETEST_960f`. All files are in this review directory. Full commands,
outputs, source hashes, actual wires and results are retained in that subdirectory.
Original limitation strings remain in unchanged probe output as historical test
metadata; this report supplies the current verdict from the actual observations.

The first portal snapshot attempt hit Windows path length while copying unrelated
ETL files. Snapshot scope was corrected to frontend source/configuration; no
implementation or expected control changed. Earlier `tsc --noEmit` invocations
used a root config with no files and project references, so their exit0 alone
should not be treated as an application type-check. This retest explicitly uses
tsconfig.app.json and passes; earlier behavioral probe evidence is unaffected.

COO~P's broader guard128PASS/2FAIL and M173PASS/5FAIL are producer-attributed
baseline results, not independently rerun here. Their reported baseline failures
are not erased by this closure. No runtime package recertification, real browser,
vendor call, render/export, deployed route/policy or integrated product grade.
Prior date/reopen/publisher closures remain bounded. LOCAL only; no deploy/push.
