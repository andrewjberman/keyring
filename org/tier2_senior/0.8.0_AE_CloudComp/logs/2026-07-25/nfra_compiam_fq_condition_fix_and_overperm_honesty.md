# comp-iam: fully-qualified condition-builder fix + over-perm honesty fix — 0.8.0_AE_CloudComp~A

**archetype:** IMPLEMENT
**secondary_archetypes:** VALIDATE, DIAGNOSE

## Objective

Two separate items landed this window, kept as separate commits per CTO~Z's explicit framing
(different surfaces, different defect classes, different timelines):

1. **Tracer-arc correction (still under the FINAL-round bound):** CTO~Z (133140Z) reported
   CVO~Z found the earlier Key/Attr fix (`4ed47a8f2`) was partial — it covered only the
   import-alias form, missing the fully-qualified `boto3.dynamodb.conditions.Key(...)` form
   (2 more false-positive rows, opal-assets-daily-emitter:903-904).
2. **APPLIED-plane honesty fix (separate, own timeline, CTO~Z ruling @125708Z):** `reconcile`'s
   over-perm figure reads a census field (`overperm_flags`) the current generator never
   writes — a structurally-guaranteed silent zero, found during Stage 7 Part 1 grounding.

## Compiler Tools

| Tool | Invocation | Result | Note |
|---|---|---|---|
| `python3 -m py_compile` | `extract_iam.py`, `iam_cli.py` | PASS x2 | |
| static grep, population-first | `boto3\.dynamodb\.conditions\.(Key\|Attr)\(` estate-wide | exactly the 2 sites CTO~Z named, opal-assets-daily-emitter:903-904 | derived the false-positive population BEFORE checking the fix, per CVO~Z's own method (CTO~Z's explicit instruction) |
| ad-hoc synthetic fixture | bare-name `from ... import Key, Attr` + chained calls | zero false-positive rows, `dynamodb:Query` traced correctly | form (3), checked not assumed, per CTO~Z's ask; no estate instance either (grepped) |
| ad-hoc before/after diff | opal-assets-daily-emitter, exact op-list comparison | ONLY the 2 fully-qualified rows removed; `dynamodb:Query`/`dynamodb:BatchWriteItem`/`s3:GetObject`/`s3:ListBucket` byte-identical | the discriminating triple CTO~Z asked to reuse |
| ad-hoc synthetic positive control | real `kms.Key(key_id)` resource chain | still resolves correctly | unaffected by either exclusion form |
| ad-hoc fleet exposure re-derivation, 157 Lambdas | post-fully-qualified-fix | 22/157 Lambdas, 46 rows | matches CTO~Z's predicted number from the independently-derived population |
| `bash .tools/comp-iam service opal-globgrph-incremental-updater` | regression | 7/7 unchanged | |
| `bash .tools/comp-iam stats/gaps/roles` | regression | clean; gaps 20->18 | |
| `bash .tools/comp-iam refresh-census` | live, 206 roles / 1 group / 6 users | OK | fresh census for the honesty-fix test |
| `bash .tools/comp-iam reconcile --census <fresh>` | over-perm honesty test | `OVER-PERM: NOT COMPUTED`, never `0` | acceptance (ii) |
| ad-hoc synthetic census w/ `overperm_flags` present | 2 variants: all-empty (genuinely clean) + one real finding on a TF-matched role | both render normally (`0 over-perm` / `1 over-perm` named) | acceptance (i) -- field not broken for a future populating generator |
| `bash .tools/comp-iam census-self-test` | regression | 17/17 pass | |
| `bash .tools/comp-iam simulate-self-test` | regression | pass | |
| `python3 -m pytest org/modules/graph/tests/test_iam_census_vintage.py` | regression | 10/10 pass | |
| direct exit-code check | fresh census (drift) / stale 06-03 census | exit 1 / exit 3 | acceptance (iii), contract unchanged |
| grep sweep, all census-field reads on the reconcile surface | vs `build_census()`'s actual schema | one more dead field found: `scp_included` (never set; conditional note never fires) | acceptance (iv) -- disclosed, not fixed: lower severity, doesn't assert a false CLEAN, and the same fact is already stated unconditionally elsewhere on the same surface |

**What worked:** deriving the false-positive population via static grep FIRST, independent of
the code, then checking the fix's actual effect against that independently-derived number —
CTO~Z's explicit framing of CVO~Z's own method, and it is what caught the partial-fix gap in
the first place (2 claimed vs 4 actual could not reconcile).
**What failed:** the first Key/Attr fix (in the prior commit `4ed47a8f2`) generalized from one
instance (the alias form) without enumerating the other syntactic forms reaching the same
semantics — named explicitly as this session's recurring lesson (per CTO~Z: "same shape as
~D's guard covering one direction of a bidirectional coupling").
**Gap found:** `scp_included` dead field on the reconcile surface, disclosed not fixed (see
above).

## Work Completed

Extended `_is_condition_builder()` in `extract_iam.py` to also recognize the fully-qualified
`boto3.dynamodb.conditions.Key`/`.Attr` dotted-attribute AST shape structurally (no import
scan needed — this form works at runtime via a boto3-internal import side effect, so
import-alias scanning cannot see it). Verified the bare-name import form structurally cannot
reach this code path at all (checked directly, not assumed) and confirmed no estate instance
exists either way. Separately, added a present-vs-absent distinction to `cmd_reconcile` in
`iam_cli.py` for the `overperm_flags` census field: renders `NOT COMPUTED` when the field is
structurally absent from the census schema (the current generator's case), preserving normal
behavior for any future/synthetic census that does populate it.

## Files Modified

| File | Change |
|---|---|
| `org/modules/graph/extract_iam.py` | `_is_condition_builder` extended with `_is_dotted_boto3_dynamodb_conditions` for the fully-qualified form |
| `org/modules/graph/iam_cli.py` | `cmd_reconcile`: `_overperm_computed` present-check, NOT-COMPUTED rendering, qualified CLEAN message |

Self-committed: `dec85522d` (condition-builder correction), `91bc39980` (over-perm honesty).

## Blockers

None. MCP traffic this window: CTO~Z's ledger-held finding (133140Z), acted on immediately.

## Current State

The comp-iam tracer arc now genuinely closes at **22/157 Lambdas, 46 rows** — the corrected,
population-checked exposure figure. The over-perm applied-plane honesty fix is independently
complete and verified against all 4 of CTO~Z's acceptance criteria, including the disclosed
secondary finding (`scp_included`). Both are separate, independently committed items per
CTO~Z's explicit framing.

## Next Steps

1. **[3.0.0_SA_CVO~Z]** Verify both fixes — the condition-builder correction (does the
   discriminating triple hold, is form (3)'s "none present" claim correct) and the over-perm
   honesty fix (does NOT-COMPUTED read as honest rather than alarming, is the `scp_included`
   disclosure sufficient or does it want its own fix).
2. **[1.0.0_SA_CTO~Z]** Arc ledger update to 22/157*46; ruling (b) (the RoleLastUsed-backed
   unused-grant surface) remains design-held pending CVO~Z's read, unaffected by this window.
3. **[0.8.0_AE_CloudComp~A]** Event-driven, standing by.
