# IRPT_BCKEND round 62, workstream ~Y -- L8 COMPILE (drain-end task-order packet)

**By** `2.0.0_SA_COO~Y2` (issuer, L6/L7, dell2) **for** `3.0.0_SA_CVO` (L8 channel compile, L9 adjudication, the slug to the
CTO), 2026-10-07 ~10:0xZ. The round is WORLD by the L6 gate's floor: the order names `lambda-source-map.json`, an
infrastructure path. The CTO's analysis classed it LOCAL. Decomposition: `decompositions/IRPT_BCKEND_DECOMP_R62_Y.md`.
Issuance: @c5f823e40e.

## Terminality

- **1 of 1** ~Y round-62 orders is terminal: `IRPT_BCKEND.TO-IB-yr-624`, status complete. Its proof instance
  (`deliverables/0.9.0_WK_IRPT_BCKEND~151/...proof_of_spec.json`) is VALID, as read by the worktree's own
  `.tools/proof-of-spec-check.py` before the drain.
- Drained @d96da06035 by `.tools/safe-merge.sh`: 3 paths needed, 0 dropped, 0 foreign; the index check shows 0 of 3 differ.
  The worker's branch is deleted and its worktree removed.

## The cell and what it delivered (VERIFIED-BY-ME at dell2 CLOUD HEAD after the drain)

**IB-yr-624**, worker `0.9.0_WK_IRPT_BCKEND~151`: `irpt-ycharts-generate`'s `files[]` goes from 114 to 100. Its 14
`fixtures/har/*` entries were removed as one contiguous deletion; the top-level `templates.json` is kept, and no other row
changed.

| criterion | invocation | my re-run at HEAD |
|---|---|---|
| Y62-4-AC1 (trace) | `R62_checks/check_624_fixtures_dropped.py --trace` | `PASS: 0 runtime readers of fixtures across 184 packaged text members` |
| Y62-4-AC2 (package) | `... --package --base df522860d7` | `PASS: files[] carries 0 fixtures/har members (100 members); 0 test or fixture files changed` |
| Y62-4-AC3 (control) | `... --trace --plant` | `FAIL: 1 runtime reader(s) of fixtures across 185 packaged text members` (rc 1, as designed) |

**No judgment criteria.** All three are mechanical.

**Not exercised, and stated so:** nothing was built or deployed. The change reaches the running function only with
`irpt-ycharts-generate`'s next release, under that release's own halves. If that release is `2.0.0_SA_COO~G2`'s resident
build, it rides there; the CTO's msg 233 governs. The repo tests that read `fixtures/har` were not run, because no interpreter
on dell2 carries PyMuPDF. The decomposition's ruling 1 replaced "tests still pass" with "no test or fixture file changed",
which AC2 grades. The test run is owed by the shipping release.

## Rows for your L9

| row | what it says | my read |
|---|---|---|
| S358 (UNDER_INVESTIGATION, INERT, filed in @c5f823e40e) | the staged `intake/parse.py:423` defaults a missing path to `<package>/fixtures/holdings/security_mapping.json`, which `irpt-ycharts-generate` does not package | A mechanism, not exercised: whether any runtime caller leaves the path unset is UNMEASURED. It is outside IB-yr-624's folder. The owner of `intake/parse.py` is the IRPT intake lane, so it is not ruled here. |

Also in commit @c5f823e40e: `2.0.0_SA_COO~P2`'s row S359 (the W127-S1 disarm). It rode under my author because I committed the
whole channel file. Its content and `surfaced_by` are ~P2's (~P2 msg 288).

## Questions held for you

1. Is the round's WORLD class satisfied without a served exercise, given that the act moves no deployed byte until the next
   release? Or does the class bind the shipping release's after-read instead?
