# Deploy Completion Record
**Date opened:** 2026-09-25T18:03:34.972519+00:00
**Status:** OPEN
**Deploy:** AMGT_RESAPP rq-2: the redeploy -- opal-amgt-scoped-api carries rq-1's export rule
**Authored by:** 0.7.0_AE_CloudOps~A
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | activation | module.scoped_amgt_api.aws_lambda_function.this (opal-amgt-scoped-api) | CodeSha256 AFTER differs from BEFORE pmH20bb+L1Kcejf4MKS4tVt+tCIPgeHwSZAsTe+nXZo= and LastUpdateStatus=Successful (AC1); prior artifact VersionId VTj2mj_gOKupat_bPjetck3HPD0N6PIJ recorded as the rollback |  | OPEN |
| L2 | verify | the served /print?format=rich body across the 89-name snapshot | AC2 served over 89 of 89 folders: OK 89, NOT_OK 0, CAPTURE_FAILED 0, exit=0 |  | OPEN |

## CLOSURE DIFF vs the deployed build input f3de463222 -- enumerated BEFORE the apply (order act 1)

Build commit: HEAD 33f6531550 (the order permits "9b7b146d9a or later"). Beyond 9b7b146d9a the closure
gains only `lib/research/corpus/backlog.py` + one test; neither ships (below), so building at HEAD is
equivalent to building at the named commit for everything that reaches the function.

`--build-only` rc=0: 203 zip entries, 856314 bytes; VERIFY missing []; VERIFY-SCOPE module-scope [] and
function-scope []; ISOLATED 3 of 3 arms OK.

### LIMB 1 -- SUBTRACTION against the built package (denominator 14 changed files, 203 zip entries)
**3 of 14 changed files SHIP; 11 do not.** The shipping set is EXACTLY the COO half's declared table:

| ships | file | the half's stated served effect |
|---|---|---|
| YES | lib/research/print/render_pack.py | rq-1's change -- the act's purpose |
| YES | lib/research/api/_harvest_prefixes.py | hash-only restamp; the four prefix constants byte-identical |
| YES | lib/research/identity/crosswalk.py | build/writer code only; no served route moves |

Shipping files NOT in the half's table: **NONE**. Half's table entries that did not ship: **NONE**.
`lib/research/corpus/backlog.py`, which entered the diff AFTER the issuer's 05:4xZ closure read and is
therefore outside the table, **does NOT ship** -- the closure walk packages no corpus member, so it
reaches no route and limb 1 does not fire on it.

**The half's crosswalk carve-out, VERIFIED rather than taken** (it is a self-report, and NEVER-law says
verify against the artifact). AST-extracted function bytes at f3de463222 vs HEAD, 33 defs as the
denominator: the SIX functions the Lambda calls -- `load_crosswalk`, `resolve`, `aliases`,
`security_key_partition`, `security_key_from_slash_safe`, `loaded_from` -- are **6 of 6 IDENTICAL**.
CONTROL, proving the comparator can see change: 3 functions DID change
(`_research_folders_for_disclosure`, `build_crosswalk`, `main`), none of them Lambda-called.
ONE SMALL DISCREPANCY IN THE HALF, recorded because a wrong list ages into a wrong belief: the half
names the changed set as `build_crosswalk`, `main`, `write_pool`. Measured, `write_pool` is UNCHANGED and
`_research_folders_for_disclosure` changed instead. Neither is Lambda-called, so the verdict is unmoved.

### LIMB 2 (the issuer's) -- is `build_pack` changed? **NO.**
AST-extracted `build_pack` is BYTE-IDENTICAL across the diff: deployed L242-359 sha 11d26e85b4e906e0,
HEAD L242-359 sha 11d26e85b4e906e0. NEGATIVE CONTROL on the same instrument: `build_rich_text` reads
CHANGED (deployed L687-805 f9d94a7ba575a52c -> HEAD L788-941 7bfd5a48f275f152), which is rq-1's whole
purpose -- so IDENTICAL above is a measurement, not a blind comparator.

### LIMB 3 (the CTO's, the load-bearing one) -- does the diff touch `scoped_amgt.py`'s pdf branch? **NO.**
`git diff --stat f3de463222 HEAD -- lib/research/api/scoped_amgt.py` is EMPTY: the file is untouched
entirely, so neither the `if fmt == "rich":` gate (:4138) nor the `build_pack(display_form, block)` call
(:4166) can have moved. The CTO half's reachable-state concern -- a byte-identical `build_pack` whose
ADAPTER call site newly passes a `thesis_bundle` -- is excluded at the strongest available grain.

**ALL THREE STOP LIMBS CLEAR. The act proceeds.**

### THE OUTCOME READ THE CTO HALF DEFERRED TO THIS ENTRY (its section 4)
The CTO signed before rq-1 landed and explicitly did NOT certify the rich-body outcome wording, leaving
it to be read from rq-1's LANDED rule here. rq-1 is now complete and drained at 9b7b146d9a. Its rule
lives in the changed `build_rich_text` (L788-941 at HEAD), and the served effect it produces is what AC2
grades over all 89 names. This entry records that the deferred read was performed at the build, against
the landed bytes, rather than inherited from the half's sentence.

PRE-ACT BASELINE, measured live (not inherited from the check's pin): deployed CodeSha256
pmH20bb+L1Kcejf4MKS4tVt+tCIPgeHwSZAsTe+nXZo=, LastUpdateStatus Successful, LastModified
2026-09-24T23:54:02Z. Artifact VersionId VTj2mj_gOKupat_bPjetck3HPD0N6PIJ, 848867 bytes -- the rollback
both halves name, confirmed as the CURRENT version by an unversioned head-object returning the same id.
AC1's pin equals this live value, so AC1 is a live discriminator for this act.

## Log

- 20260925T180334Z OPENED by 0.7.0_AE_CloudOps~A with 2 leg(s)
