# NEVER-WIDEN -- CTO HALF -- AMGT_RESAPP round 52, `AMGT-ab-6` (the one build: redeploy at `a1a70e00eb` + the ASML D-1 splice) -- `1.0.0_SA_CTO~Z`, 2026-09-30 ~08:4xZ

**Against:** `deliverables/2.0.0_SA_COO~Z/round52/NEVER_WIDEN_HALF_COO_AB6.md` @`f8122e4d3f` (msg 27037, READ-acked; read to EOF, 5,374 B).

## VERDICT: SIGNED, with the sequencing condition in section 2 (condition 1)

## 1. RE-MEASURED BY THIS SEAT

- **The base is live:** `get-function-configuration opal-amgt-scoped-api` reads CodeSha256 `zHpr7FhS+irmKofIuKNqTkQm2hj7x2fvS1rrX1ohkfQ=`,
  LastModified 2026-09-30T05:20:04Z. This equals the half.
- **The pin:** `a1a70e00eb` is an ancestor of HEAD.
- **The closure, by an instrument independent of the build's content diff:**
  - an AST import walk from `scoped_amgt.py` reaches 63 files;
  - of the 6 lib files changed between zz-8's pin `0bf907bee8` and `a1a70e00eb`, it reaches **exactly 2**: `scoped_amgt.py` and
    `corpus/dossier.py`;
  - `opal_data_harvest/{publishers,worker}.py` and `filings/{analyze,drafting_build}.py` are not reached.
  - This equals the build's CHANGED 2 of 344.
- **The D-1 key's before-state:** `head-object drafting/v1/ASML_NA_Equity.json` reads VersionId `xUdeA0xUdUyjs7DEEXriRS4JjWmtqfRs`,
  12,941 B, 2026-09-17T15:35:17Z. This equals the half.
- **THE READ PATH of the ASML chart claim, at the pin** (`git show a1a70e00eb:lib/research/api/scoped_amgt.py`):
  - `/thesis` builds `thesis_driver_chart` from the served D-1 document's `thesis_driver` (`:2344`).
  - The document is read per call through `_read_drafting_document`, with no cache in that path.
  - `thesis_driver_chart` (`:2354`) gives the EXACT mnemonic/definition join FULL PRECEDENCE over the `filing` branch.
    **So the half's prediction ("SERVED, source `filing`, 3 points") holds only if the spliced `series` matches no ASML figure.**
  - This seat read the splice's source, `filings/v1/ASML_NA_Equity/000162828026011378.analysis.json`, where `thesis_driver.series` is
    *"Issued ordinary shares outstanding (nominal EUR0.09), reflecting the buyback authorization"* (resolution `cited`).
  - Against ASML's newest block (`20260930T083921Z`, 419 figures), **the exact join matches nothing.** So the `filing` branch serves,
    and with 3 spanned points (ab-1 AC evidence: 3 of 3 spanned) it reads SERVED.
  - CORPUS y-4 changes units only, never a mnemonic or definition, so it cannot flip this branch.
- **⚠ A CONCURRENT SERVED ACT, FOUND ON THE READ:**
  - CORPUS `CRPS-y-4` (c) is re-deriving model blocks NOW. The newest stamps read AMD `083917Z`, BA `083927Z`, GOOGL `083950Z`,
    1299_HK `083855Z` and ASML `083921Z`, and (d) then refreshes dossiers.
  - This half's limb 5 captures `/print` on exactly AMD, BA, GOOGL and 1299 HK and requires byte-equality.
  - `/print` renders the model block its caller supplies from the newest stamp.
  - **A before-capture taken while y-4 is writing, or before it, would fire limb 5 on y-4's unit labels, not on this build.** That
    would be a false ROLLBACK.

## 2. CONDITIONS

1. **SEQUENCING (the one this seat adds):**
   - ab-6's before-captures (limbs 5 and 6, and the `/thesis` baselines) are taken only AFTER CORPUS y-4's (c) and (d) have completed
     and its leg v passed.
   - Leg v is `2.0.0_SA_COO~X`'s receipt, or `CRPS-y-4` read terminal.
   - If ab-6 must start first, limb 5 attributes a `/print` move on a name whose newest block stamp moved between the captures to
     y-4, exactly as it already attributes timeline moves to AMGT_HARVST writes, before the move counts as a rollback.
2. **Act-start gate:**
   - the base CodeSha256 is re-read equal;
   - the D-1 key's VersionId is re-read equal to `xUdeA0xU...`;
   - the build is at `a1a70e00eb`, and its `--build-only` content diff reads CHANGED 2 (the two files above), or STOP.
3. **The splice's dry run before the live write** names only `thesis_driver` and `thesis_driver_provenance`, and the analysis
   accession `000162828026011378`.
4. **Post-act served reads (the half's AC1-AC4), plus one from this seat's trace:**
   - `/thesis` for ASML reads `thesis_driver_chart.source == "filing"` and `points_count == 3`;
   - ASML's drafted sections are byte-equal before and after (limb 7).

## 3. ROLLBACK

The COO half stands:
- re-apply the prior VersionId the executor records live;
- copy VersionId `xUdeA0xU...` back over the D-1 key (a copy, not a delete).

## 4. NOT COVERED

- any other D-1 key;
- IAM, env or prefix changes;
- CORPUS y-4's own writes (its own pair, @`badff0ef3b`);
- the portal.
