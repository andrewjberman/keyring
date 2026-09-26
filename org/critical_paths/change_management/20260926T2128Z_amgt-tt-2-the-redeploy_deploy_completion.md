# Deploy Completion Record
**Date opened:** 2026-09-26T21:28:45.600302+00:00
**Status:** OPEN
**Deploy:** AMGT_RESAPP tt-2: the redeploy -- opal-amgt-scoped-api carries tt-1's posture two-form rule (render_pack._posture_markdown). Under BOTH never-widen halves: COO @52128e2a19 (5 stop limbs) + CTO @392fee249c (adds limbs 6 the FOUR EXACT STRINGS and 7 no widening into branches 1/2/5). Prior artifact VersionId T9JIi3D.nKZ5zd_bNaHzOh4_mQWF8.80 = the rollback, re-read at build; deployed CodeSha256 BEFORE = LK9h47juBfZPaAyfztAxDe9z65W2ZtEw6H2IJ/DcO4s=.
**Authored by:** 0.7.0_AE_CloudOps~A
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | closure diff at --build-only against the DEPLOYED build input (s3 VersionId T9JIi3D.nKZ5zd_bNaHzOh4_mQWF8.80, content-sha256 == live CodeSha256 LK9h47juBfZPaAyfztAxDe9z65W2ZtEw6H2IJ/DcO4s=), COO limbs 1-4 graded CLEAR BEFORE any upload (limb 5 is graded on OUTPUT at L2/L8) | file-by-file closure diff printed with a denominator on both sides + a per-limb verdict for limbs 1-4, each with a control that FIRED |  | OPEN |
| L2 | verify | CTO limb 5 BASELINE: the served /print pdf OUTPUT captured BEFORE the apply, content-stream digest (a served pdf raw sha can move per request on /CreationDate, so the content stream is the oracle) | pre-apply pdf content-stream digest recorded over a multi-currency sample + an instrument control reading STABLE across two captures of one unchanged deployment |  | OPEN |
| L3 | verify | CTO limbs 6+7 BASELINE: the served /print?format=rich posture sections captured BEFORE the apply, each name classified by its branch -- branch 3 (non-SERVED) and branch 4 (SERVED+absent) feed limb 6, branches 1 (no posture), 2 (READ_FAILED) and 5 (SERVED non-absent) feed limb 7 | pre-apply posture-section bytes recorded per name with its branch class named, denominator printed per class; a class with zero members is reported as such and never read as a pass |  | OPEN |
| L4 | s3-prefix | ONE artifact write s3://opal-313476888478-lambda-artifacts/research/opal-amgt-scoped-api.zip -- act A of both halves; rollback = the prior VersionId RE-READ at build time (the GO records T9JIi3D.nKZ5zd_bNaHzOh4_mQWF8.80; a VersionId pinned at signing would be stale), preserved by bucket versioning, never a delete | head-object new VersionId + uploaded content-sha256 metadata == the locally computed sha256 of the graded zip |  | OPEN |
| L5 | activation | ONE safe-apply on infra/aws/terraform/harvest/ moving ONLY opal-amgt-scoped-api's code -- act B; a plan touching a second resource is a REFUSAL | plan 0 to add 1 to change 0 to destroy in-place naming only last_modified, s3_object_version and source_code_hash + apply complete + 0-diff replan, the verdict read by token and never from a positional slice |  | OPEN |
| L6 | verify | AC1 -- the deployed code MOVED off round 44's LK9h47juBfZPaAyfztAxDe9z65W2ZtEw6H2IJ/DcO4s= and the last update is Successful | tt-2.AC1.py exit=0, CodeSha256 differs from the prior AND equals the uploaded object's content-sha256 metadata |  | OPEN |
| L7 | verify | AC2 -- served /print?format=rich swept over the LIVE research library read FRESH with its read time printed; a name arriving with no identity is reported, held and routed to the issuer, never counted as an export failure | tt-2.AC2.sh exit=0: absences missing=0 on N of N names, EXPORT-COMPARE OK on N of N, sweep rc=0, denominator and read time printed |  | OPEN |
| L8 | verify | CTO limb 5 AFTER: the served /print pdf re-captured post-apply and graded on OUTPUT, not on the diff | post-apply content-stream digest == the L2 baseline on every comparable key, the before/after pair reading DIFFERENT CodeSha256 so it is a real pair |  | OPEN |
| L9 | verify | CTO limb 6 -- THE FOUR EXACT STRINGS, NOT THE COUNT: the post-apply served export for a branch-3 and a branch-4 name carries two absence lines byte-identical to the four strings, with the 'Nothing is rendered in its place.' tail and the machine disclaimer on the correct arms (they run in OPPOSITE directions between the two arms) | per-arm byte comparison against the landed rule at render_pack.py :701 and :703 (non-SERVED) and :711 and :715 (SERVED+absent); a line-count match alone is NOT proof and is recorded as such |  | OPEN |
| L10 | verify | CTO limb 7 -- NO SILENT WIDENING into branches 1, 2 or 5: every name in those three states is byte-identical in its posture section before and after the apply | per-name byte diff against the L3 baseline with the denominator printed per branch class; a single differing byte is the STOP |  | OPEN |

## Log

- 20260926T212845Z OPENED by 0.7.0_AE_CloudOps~A with 10 leg(s)
