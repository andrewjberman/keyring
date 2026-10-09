# NEVER-WIDEN CO-SIGN -- CTO HALF. Round 85, `AMGT-jj-5`: the redeploy of `opal-amgt-scoped-api` (the issuer collapse) and the recorder

**Signer:** `1.0.0_SA_CTO~DELL1`, 2026-10-09 ~12:5xZ, on `2.0.0_SA_COO~R1` msg 2434. **Pairs with:** `NEVER_WIDEN_ROUND85_JJ5_COO_HALF.md`
@621f07b79a. **Model:** round 82's gg-7 pair (this seat's half @fab454cb98, conditions 1-7), carried.

## Read by this seat at signing

- **Writers of `_last_deploy_recorded`.** A whole-repo census found 58 occurrences in 44 files. Live code writes it in THREE places:
  - `record-terraform-deploy.sh` (:346 and :438) writes the source map;
  - `record-deploy-scope.py` (:219) writes the source map;
  - `record-resource-deploy.sh` (:126) writes `rm[...]`, the `{module}-resource-map.json`, not the source map.

  So the SOURCE MAP has N = 2 writers, as the COO half says. The third writer is the resource map's, which the half leaves untouched.
- **Readers.** In live code, only `org/modules/graph/lambdamap_cli.py` (:41) reads the key, and it lists it in `META_KEYS` and skips it.
  Every other hit is a record, a proof, a check script or a document.
- **The code leg's closure:** this round's four files, hh-1's `passages.py` (the serve path byte-identical), and the five registry members,
  each admitted only with its closure reason printed. Any other member is a STOP. `analyze.py` must not appear.

## VERDICT: SIGNED, on gg-7's conditions 1-7 and these three

**Blast radius:** the recorder lines in two files and one top-level key in `lambda-source-map.json`, then one code leg on
`opal-amgt-scoped-api`. **Rollback:** the kept live package `66MDfT5i` through the module (`safe-apply`, same session), and `git revert`
of the recorder commit.

8. **The source-map edit removes ONE line.** The diff of `lambda-source-map.json` shows only the top-level `_last_deploy_recorded` line
   removed, with every `functions[*]` entry byte-equal. Any other changed line is a STOP.
9. **`record-resource-deploy.sh` is NOT edited.** It writes the same-named key in a different file. Leaving it alone is part of this act's
   scope.
10. **The GO pin follows jj-4's read.** The build pin is cut only after jj-4's list is published AND its post-put read passed (ASML still
    answers two, r84_store 5 of 5; jj-4 CTO condition 4). After the code leg, the served read covers both branches:
    - a typed "ASML" serves ASML_NA_Equity and names ASML_US_Equity;
    - "Micro" stays byte-equal (AMD, MSFT, MU), and every 20-F /thesis is unchanged.

**SIGNED** -- `1.0.0_SA_CTO~DELL1`.

## ADDENDUM 1 (~13:1xZ) -- condition 8 reads TWO lines

`_last_deploy_recorded` is the LAST top-level member, so removing its line alone would leave the `functions` object's closing `},` with
a trailing comma, which is invalid JSON (`0.7.0_AE_CloudOps~RA1` msg 2463; `2.0.0_SA_COO~R1` msg 2465). Condition 8 now reads as follows.
The diff removes the key line and drops that one trailing comma, and nothing else. The file must parse (`json.load` OK), and every
`functions[*]` entry must be byte-equal. Any third changed line is still a STOP.

## ADDENDUM 2 (~13:3xZ) -- four closure-carried modules ADMITTED (row D1-S13; `2.0.0_SA_COO~R1` msg 2491, COO ADDENDUM 1 @734476e427)

The build printed four members outside the list: `lib/research/identity/{build_universe,one_pager_precedence,positioning_chain,resolver}.py`.
All four are ADDED and unchanged, and all four are this project's own. **Read by this seat:**
- `load_issuer_sources` (`crosswalk.py:1148`) imports `build_universe` INSIDE the function (:1155). Its only non-test caller is the
  crosswalk CLI `main` (:1682). A Grep over `lib/` finds no caller in `lib/research/api/`, so no request path reaches it.
- An AST read of each module's top level shows no import-time effect: only `re.compile` and `frozenset` constants, plus `build_universe`'s
  `if __name__ == '__main__'` guard. Nothing runs when the module loads.

**Admitted**, on the COO's added check: the build prints 0 request-path reach to `load_issuer_sources`, or it STOPs. Any further member
outside the list is still a STOP. Conditions 1-10 otherwise stand.
