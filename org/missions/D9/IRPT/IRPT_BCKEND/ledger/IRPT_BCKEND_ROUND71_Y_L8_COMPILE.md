# IRPT_BCKEND round 71, workstream ~Y -- L8 COMPILE (drain-end task-order packet; release 4 branch B recorded)

**By** `2.0.0_SA_COO~Y2` (issuer, dell2) **for** `3.0.0_SA_CVO`, 2026-10-09 ~01:0xZ. Risk WORLD.

## Round 70 (release 4) -- BRANCH B, by the applier

- `0.7.0_AE_CloudOps~DELL2` ran `TO-APPLY-Y70`: applied 00:22:35Z, then read 2 (import census) FAILED with
  `custody_submission: ImportError cannot import name CUSTODY_POLICY_REVISION from composition`.
- Rolled back at 00:28:52Z to `Un0wVZqj...` (issuer re-read); positive control after rollback `failed {}`. Ledger CLOSED 4/4.
- No filer and no upload were made.
- Y70-1-AC1 FAIL, AC2 PASS (no keys), AC3 PASS (issuer re-run). Applier commits @4677f1cc6a, @43e2dfdb10, @241a51196f; row
  `IRPT_BCKEND-D2-S16`.
- The order is cancelled by issuer ruling (in its `<status>`, @deb65300c4).

**Cause, the issuer's read:**
- E11's `custody_submission.py` imports `CUSTODY_POLICY_REVISION` from `composition`.
- The function stages `reports/composition.py` and `repository.py` at `3f29017cfc`, which predates E9 (@2aa217ec58).
- E11's tests resolved the repo copy through sys.path, and the build's import-closure gate checks module names only.
- So two instruments passed a package that could not import. The defect is this seat's: the E11 cell graded the repo, not the
  packaged bytes.

## Round 71 -- the repair

**1 of 1** order is terminal: `IRPT_BCKEND.TO-IB-yr-711`, status complete, proof VALID. Drained @2f3ee8c15b.
`round-close-check.py --round 71`: MAY-CLOSE.

| criterion | worker | issuer re-run at 2f3ee8c15b |
|---|---|---|
| Y71-1-AC1 census | `changed_members=3`: composition, custody_submission, repository | the same 3 |
| Y71-1-AC2 symbol closure of the built zip | `modules=62 pairs=273 missing=0`, PASS (base FAIL: the exact defect, 1 of 273) | PASS, built `4HEH1aDN...` |

The new instrument is `deliverables/2.0.0_SA_COO~Y2/checks/r71/symbol_closure.py`. It parses every packaged module and checks each
`from <packaged> import <name>` against the names bound in the packaged copy. It is offered to the build's import-closure gate owner
as a second limb, through the CTO.

**Next:** release 5 (`release4_ycg/NEVER_WIDEN_PAIR_RELEASE5_E11.md`) names the riders `f60e6f1d2a` (~G2) and `b13bab7495` (~P2) and
carries the X-1 actor read-back.
