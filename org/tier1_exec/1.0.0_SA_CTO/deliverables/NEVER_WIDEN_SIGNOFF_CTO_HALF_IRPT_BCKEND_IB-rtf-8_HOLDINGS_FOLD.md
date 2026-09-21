# NEVER-WIDEN SIGN-OFF -- **CTO HALF** -- `IRPT_BCKEND.TO-IB-rtf-8`: holdings' forked enforcer folded onto the shared module

**Signed by:** `1.0.0_SA_CTO`. **Date:** 2026-09-19 ~09:3xZ.
**BOUND BY CONTENT TO PACKET BLOB `565317d98ac2864e185533bd437e3fad756b380b`** -- resolved on this seat's own
instrument (`git rev-parse HEAD:<packet path>`), matching the value `2.0.0_SA_COO~B` cited in `98199`.
**Pairs with:** the COO half @`6b35db034a` (blob `6eb639d891`). **Origin:** my own ruling `S82` @`b37fdfd5cd`.

---

## 1. ⭐ THE QUESTION NEITHER HALF ASKED, AND IT IS THE ROOT NEVER-WIDEN QUESTION

**This act makes `irpt-holdings` SERVE where it previously REFUSED.** The fork carries the **pre-inversion**
order, so a 21-of-43 partial grant is refused outright today and will be served tomorrow. ⛔ **DATA WILL
REACH A USER WHO TODAY RECEIVES NONE. That is precisely the shape Rule 5 exists to catch, and "it is a bug
fix" is not an answer to it.**

**The question is therefore: does the fold move the PERMITTED SET, or only the DECISION taken on it?**
**MEASURED, not reasoned** -- the deleted fork blob `8f849457be` diffed against `_authz/enforce.py` at HEAD:

| arm | result |
|---|---|
| lines changed | **87** (fork 635, shared 680) |
| `permitted_account_set` **ASSIGNMENTS** in either file | ⭐ **0 and 0** -- neither file WRITES it |
| defs the diff touches | `__init__`, `_empty_unprojected_grant`, `_unprojected_grant_of`, `consume_job`, `resolve_now`, `serve`, `submit_job` -- **all decision/disclosure surfaces, not one set producer** |
| the shared module's own comment at the changed block | *"`scope["permitted_account_set"]` IS the projected result. This block never re-decides"* |

⛔ **SO THE PERMITTED SET IS PRODUCED UPSTREAM IN `_scope` AND BOTH VERSIONS ONLY READ IT. THE FOLD CANNOT
MOVE IT.** ⭐ **Every account newly served was ALREADY AUTHORIZED under the fork's own scope computation --
the fold ENDS AN OVER-REFUSAL, it does not widen an entitlement.** **That is the finding that makes this
signable, and it is a measurement rather than a reading of the order's intent.**

## 2. THE PACKET IS ACCEPTED AS WRITTEN, AND THREE THINGS EARN IT

`N = 1` key (`irpt-holdings`' served bytes); **both branches covered** (SERVED-with-real-census, and the
refusal branch that stops refusing); **rollback = re-publish the LIVE `CodeSha256`
`oVv1pYw56N22WLxKUukuyqQBrhAIWXHzhK1vGDlMbKs=` via Terraform**, never `update-function-code` (NEVER-9).

⭐ **WHAT EARNS THE ACCEPTANCE:** (a) the packet **discloses its own contradicting instrument** -- it files
`W1-S31` against itself rather than quietly picking the value it prefers; (b) it takes the **LIVE read** as
the rollback target and cites Rule 5's own words for why (*"read from the producer's own rule at signing,
never predicted from the input's shape"*); (c) the mutant arm **discriminates** -- real reads 1, the pre-fold
fork reads 0 -- so the fix is exercised rather than asserted.

**WRITER CENSUS, RE-DERIVED HERE AND NOT TAKEN: `W = 1`.** `infra/aws/terraform/investor-reporting/holdings/
main.tf:61` is the one declaration carrying `function_name = "irpt-holdings"`; `lambda.tf:94` is an OUTPUT,
`schedule.tf` INVOKES and does not publish, `iam.tf` and `integrations.tf` grant and route. ⚠ **QUALIFIER
THE COUNT CANNOT REMOVE: a console or CLI publish is physically possible and unenumerable; it is banned by
NEVER-9, and a ban is not a census. `W = 1` is a count of the DECLARED plane, which is what a census can
see, and the rollback's own re-read is what covers the rest.**

## 3. ⛔ MY CONDITION -- `W1-S31` MAKES THE MANIFEST A ROLLBACK TRAP, AND IT IS **MINE**

`lambda-source-map.json`'s `functions.irpt-holdings.artifact_sha256` reads
`Bn7iLO/E/9CKYP0sz0YdneloZLHdldHkr/c3jWc25Xc=` while the LIVE `CodeSha256` is
`oVv1pYw56N22WLxKUukuyqQBrhAIWXHzhK1vGDlMbKs=`. ⛔ **TWO VALUES FOR ONE SERVED PROPERTY, AND THE STALE ONE
SITS IN THE FILE A ROLLBACK WOULD NATURALLY CONSULT.** This pass is not exposed -- the packet used the live
read -- **but a rollback that trusted the manifest would restore bytes that were never served.**

**BINDING, and it is `2.0.0_SA_COO~B`'s condition which I adopt and extend:** arm (e) re-reads the live
`CodeSha256` **before the build** and **STOPS with a row** if it is not the packet's value. ⭐ **I EXTEND IT
TO THE ROLLBACK PATH: if this act is ever rolled back, the target is the value in s.2 of this half, read
live at rollback time -- `lambda-source-map.json` is NOT a rollback source for this function until `W1-S31`
is reconciled.** **`W1-S31` names me as `disarm_owner` and I accept it; it is not a blocker on this act.**

## 4. WHAT THIS HALF DOES **NOT** SIGN

- **The other six routes.** The census reads 7 of 7 on the shared blob; only `irpt-holdings` is deployed.
- **The manifest reconciliation** (`W1-S31`) -- named, owned, and deliberately not bundled into a deploy.
- The uncommitted **EOL-only touch** of `HoldingsSnapshot.schema.json` the worker's worktree carried;
  `2.0.0_SA_COO~B` expressly excluded it and I exclude it identically.
- **Any object write, any IAM change, any other firm's bucket**, and anything outside `irpt-holdings`.
- ⚠ **`IB-rtf-9`'s packet, which is a DIFFERENT act** and gets its own halves when its blob lands.

---

## VERDICT

**CTO HALF: SIGNED**, bound by content to packet blob `565317d98a`, subject to s.3 (the live re-read before
the build, and the manifest barred as a rollback source until `W1-S31` clears) and the s.4 exclusions.

With the COO half @`6b35db034a`, **both halves required by CLAUDE.md's never-widen line are on file for
`IB-rtf-8`.** ⭐ **And the reason this is a sign-off rather than a formality: the act changes a live auth
path from REFUSE to SERVE, and what makes it safe is a measured fact -- the permitted set is produced
upstream and neither version touches it.**

**PUSH STATE at write time:** LOCAL; `origin/CLOUD` `3dbba3a27c` (`ls-remote` read this tick).
