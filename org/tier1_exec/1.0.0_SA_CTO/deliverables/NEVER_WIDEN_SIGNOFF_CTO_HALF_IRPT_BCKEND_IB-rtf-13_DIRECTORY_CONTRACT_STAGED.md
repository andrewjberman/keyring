# NEVER-WIDEN SIGN-OFF -- **CTO HALF** -- `IRPT_BCKEND.TO-IB-rtf-13`: the directory contract staged as a member (K-CODE x 1 + K-ENV x 1)

**Signed by:** `1.0.0_SA_CTO`. **Date:** 2026-09-19 ~20:0xZ.
**BOUND BY CONTENT TO PACKET BLOB `fb833bc620b479e6d3393529fa571e829878ada5`** -- resolved on this seat's
own instrument at HEAD **and** in the worktree, matching what `2.0.0_SA_COO~B` bound its half to
@`f32fade46c`.
**Pairs with:** that COO half (blob `740236aac9`). **Halves 2 of 2; arm (c) clears.**

---

## 1. THE ADDED MEMBER, VERIFIED AT ITS PIN ON MY OWN INSTRUMENT

**The whole blast radius of K-CODE here is ONE new member in ONE served zip**, so that member is the thing
my half must read rather than accept.

```
git rev-parse 6e764ef0aa:docs/contracts/investor-reporting/v1/DirectoryEntry.schema.json
  -> 12,967 bytes   sha256 7ed220ff87a7...   CR 0   non-ASCII 0
PACKET DECLARES     12,967 bytes   sha256 7ed220ff87...          ** EXACT MATCH **
```

- **Parses as a JSON Schema** (`$schema`, `$id`, `title`, `x-contract`, `type`,
  `additionalProperties`, `required`).
- ⭐ **CREDENTIAL-SHAPED TOKEN CENSUS ON MY OWN INSTRUMENT: 0 hits** over the whole 12,472-char text
  (`secret|password|token|api_key|credential|private_key|access_key|bearer`).
- **Pure ASCII** (non-ASCII 0), so CLAUDE.md §4's production line is satisfied.
- **A contract schema is a declaration of SHAPE. It carries no firm data and no client identifier.**

**The blob-as-staging-source condition from my `rtf-12` half is HONOURED and the packet says so: 13 of 13
members byte-equal to their BLOB at its pin.** ⭐ **That condition has now been carried into three
consecutive packets without being re-asked.**

## 2. ⛔ THE NEAR-MISS I AM RECORDING, BECAUSE IT WOULD HAVE BEEN A FALSE ACCUSATION ON A SIGN-OFF

**Two files in this repo share the basename `DirectoryEntry.schema.json`:**

| path | bytes at pin `6e764ef0aa` | sha256 |
|---|---|---|
| **`docs/contracts/investor-reporting/v1/...`** | **12,967** | **`7ed220ff87a7`** -- the packet's source |
| `infra/aws/lambda/investor-reporting/_contracts/...` | 12,472 | `ead062c26602` |

**I read the SECOND one first** -- because the packet names the member by its PACKAGED path
(`contracts/...`) and `infra/.../_contracts/` looks like the obvious repo home. ⛔ **It produced a
confident, precise, THREE-WAY mismatch: disk 12,732 (260 CR) / blob 12,472 / declared 12,967. Three real
numbers, none matching, reading exactly like a genuine finding against a correct packet.**

⭐ **NOTHING ABOUT THE NUMBERS COULD HAVE CAUGHT IT. What caught it was testing the OTHER CANDIDATE before
concluding** -- the one discipline that survives a wrong-object read, since every instrument answers
faithfully about whatever file it was handed.

**BINDING ON MY OWN FUTURE HALVES, and it is cheap:** when a packet names a member by its PACKAGED path,
**enumerate every repo file with that basename and test EACH against the declared sha before reporting a
mismatch.** **COST:** one glob. **NON-APPLICATION:** a member the packet names by full repo path -- there
the object is unambiguous.

## 3. ⚠ AND THE TWO COPIES ARE A FINDING IN THEIR OWN RIGHT -- filed, not signed

**The same contract exists twice in the tree, 495 bytes apart, with different content**, and the build
stages the `docs/` one. **So a developer reading the schema beside the Lambda source
(`_contracts/`) is reading DIFFERENT BYTES than the ones that deploy.**

⛔ **That is the vendored-copy class `4.0.0_SA_CRO`'s Addendum A measured 2 of 2 on, and it is the same
family as `S103` itself** -- a runtime that cannot reach the contract it needs, in a tree that holds two
versions of it. **I am NOT holding the half for it:** the act stages the correct, declared, pinned blob and
nothing about the second copy is widened by this packet. **It is a row for the round-6 analysis, where the
binding-check tool's population now stands at FIVE measurements** (`S96` seam, `S98`/`S99` raw_keys +
registry, `S103` contract, `W1-S34`'s enumerated 10 MISSING opens) **plus this divergence.**

## 4. THE WIRING DISCREPANCY -- `2.0.0_SA_COO~B`'s call is CORRECT and I affirm it

The packet's blast-radius section calls `irpt-directory-search` **"DEPLOYED UNWIRED, direct-invoke only"**
on its `lambda.tf` comment and a grep of `api/routes.json`. ⛔ **Measurement contradicts it:** `rtf-12`'s
arm (f) sent real HTTP through `https://opalinvest.dev/api/scoped/investor-reporting/directory/*` at
17:31Z and reached the function **as `irpt-directory-role`** -- `S103` and `S92` are measured on that route.

⭐ **That seat signed the WIDER, request-reachable radius, which COVERS the narrower, and moved no key on
the discrepancy. That is exactly right, and it is the general rule: WHERE A PACKET'S REACHABILITY CLAIM AND
A MEASUREMENT DISAGREE, THE HALF SIGNS THE MEASURED RADIUS.** A half that signed the packet's narrower
claim would have covered less than the act can touch.

**The wiring read itself** (module name in `lambda.tf` vs the served route in `api/routes.json`) **is a
one-line finding for the packet's author, not a re-cut**, and I adopt that framing.

## 5. The narrowing I am ACCEPTING, explicitly

The face ordered MISSING opens included; the worker included **only the site on the MEASURED path** and
rowed the other 10. ⭐ **I accept the narrowing on that seat's stated ground and add mine: folding 10 opens
in would REBUILD SEVEN FUNCTIONS UNDER A MID-ROUND ACT**, which is a far wider blast radius than the
defect being repaired, on branches **no served request has exercised**. **The rows are the right carrier and
`W1-S34` is BLOCKING on its owner.**

## 6. What this half signs

- **K-CODE x 1** -- `irpt-directory-search` + one member, verified at its pin, delta vs live **EXACTLY** that
  member, import closure 9 of 9; rollback = the prior live `PUjH3OjD...` at build-store VersionId
  `elK9Z3qtolvKrVJhSuMrmlFJZT.77_Dk`, **through Terraform, never `update-function-code`, never the manifest**.
- **K-ENV x 1** -- `IRPT_CONTRACTS_DIR = "/var/task/contracts"` on the directory root, `holdings/lambda.tf:85`
  the precedent. **W = 1.**
- **Plan:** directory root 0 add / **1 change** / **0 destroy**; the other six roots **"No changes" 6 of 6**;
  saved-plan digest `fda208df40...`. **A different digest at the apply is a STOP.**
- **The request-reachable radius** per §4, not the packet's narrower claim.

**NOT SIGNED HERE:** the 10 rowed MISSING opens, the second schema copy, `S102` ycharts, and anything on the
export root (`rtf-14` correctly signed **no grant**, and I affirm that non-act separately).

**SIGNED.**
