# AMGT_RESAPP task order -- `AMGT-qq-4` -- RE-VERIFY THE STORED DRIVERS AND SPLICE THEM INTO THE DRAFTING OBJECTS

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-qq-4</owned_cells>
</decomp_ref>
<issued_to>0.7.0_AE_CloudOps~RA1</issued_to>
<issued_by>2.0.0_SA_COO~R1</issued_by>
<to_id>AMGT_RESAPP.TO-AMGT-qq-4.reverify-the-stored-drivers-and-splice-them-into-the-drafting-objects</to_id>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- two operator-run store writes, no schedule is created or changed.
comp-iam: DECLARED-NOT-APPLICABLE -- the caller's own credentials write two prefixes the producers already write (`filings/v1/`, `drafting/v1/`); no role or policy moves.
comp-adversary: RUN at the cut -- the production re-verification in dry-run over all 12 stored analysis objects against the checkout's code: 3 names change (ASML 1 -> 0 points, BABA 0 -> 2, SAP 1 -> 3), 9 are equal; AMENDMENT 1 (issuer, 2026-10-11): SAP is HELD out of the write (its three expected points mix EUR millions, 2023 and 2024, with EUR billions, 2025) so the write set is ASML and BABA; r92_driver_reverified.py `--hold SAP_GY_Equity` reads NO at the base (R1) and PASSes R2 and R4.
EGRESS CLASS, declared: NONE (S3 reads and puts; no vendor, SEC or model call).
</preflight>

## 1. THE ACT -- `AMGT-qq-4` (round 92, decomposition s.100)

CTO~DELL1 round-91 analysis item 4. Round 91's pp-2 and this round's `AMGT-qq-3` make the verifier locate the points the filing states and
bound a block at another year's label; they change what `reverify_stored_thesis_driver` computes, but no stored object has been rewritten,
so the live chart is unchanged. The served `thesis_driver` is the DRAFTING object's, spliced from the newest analysis. Two writes, in
order, from the repository checkout at the GO's pin, each preceded by its dry run:

1. **Re-verify the analysis objects.** For each name the GO's table lists as CHANGED: `python -c "from lib.research.filings import analyze;
   print(analyze.reverify_stored_thesis_driver('<key>', '<accession>', dry_run=False)[2])"`. It rewrites
   `filings/v1/<key>/<accession>.analysis.json` at its OWN key through `crosswalk.write_pool` (ETag-conditional: an OVERWRITE of an existing
   object, which bucket versioning keeps as a VersionId). Names whose expected points equal the stored ones are NOT written.
   **HELD, do not write: `SAP_GY_Equity`.** Its dry run keeps three points (2023 = 13,745 and 2024 = 18,078 stated in EUR millions, 2025 = 21.05
   stated in EUR billions): one series on two scales, 1,000 times apart. The write set is `ASML_NA_Equity` and `BABA_US_Equity` and nothing else.
2. **Splice the drivers.** `python -m lib.research.filings.drafting_build --splice-driver --dry-run --only-keys <the CHANGED keys>`; its
   lines must read `served_validator=True` for every key and print the moved keys (`thesis_driver`, `thesis_driver_provenance` and nothing
   else). Then the same with `--pre-act-dir <dir>` and without `--dry-run`: the ONE writer (`analyze.write_outputs`, drafting only)
   overwrites `drafting/v1/<key>.json` for exactly those keys.

BEFORE step 1 record, for every key to be written, the VersionId of its current `filings/v1/.../analysis.json` and `drafting/v1/<key>.json`
(the rollback list, in the change-management entry), run the pair's dry-run table, and sweep every live worktree's open deploys for
entries naming `filings/v1` or `drafting/v1` (print the per-tree denominator). Open a change-management entry first and close it last.
Rollback, if the CTO names it: restore each key to its recorded VersionId (a copy of the prior version to the same key, never a delete).

## 2. BOUNDS

1. The writes named, for the CHANGED keys only: no function, role, route, schedule or other prefix, no other key.
2. No S3 delete, ever. No Bloomberg, SEC or model call. No `bun`, `npm` or `pip install`.
3. Standing: no push of shared branches.
4. If the dry run's CHANGED set differs from the pair's table, or any key reads `served_validator=False`, STOP and tell the issuer.

## 3. SURFACES

<paths>
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.7.0_AE_CloudOps~RA1/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 3600)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-qq-4"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round92_prep/checks/r92_driver_reverified.py" --hold SAP_GY_Equity --write-set ASML_NA_Equity,BABA_US_Equity; echo "exit=$?"</invocation><expect>every analysis object is listed; ASML_NA_Equity and BABA_US_Equity read CHANGED ... OK (served points equal the re-verified expectation), SAP_GY_Equity reads HELD ... OK (its stored points still served) and each expected-same name reads OK; PASS R1, PASS R2, PASS R4, PASS R5; R92 DRIVER REVERIFIED: YES; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-qq-4"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; bash "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round89_prep/checks/r89_peers_deployed.sh" &amp;&amp; bash "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round89_prep/checks/r89_deployed_close.sh" --want amgt-corpus-dossier/11; echo "exit=$?"</invocation><expect>the no-regression arm: R89 PEERS DEPLOYED: YES and R89 DEPLOYED CLOSE: YES (dossier /11, the withhold and the listing byte-equal) with the function's CodeSha256 re-read; and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

The instance is genre DEPLOY, with a NAMED rollback and the recorded VersionIds as the discriminating control, at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.7.0_AE_CloudOps~RA1/AMGT_RESAPP.TO-AMGT-qq-4.reverify-the-stored-drivers-and-splice-them-into-the-drafting-objects.proof_of_spec.json`.
`proof-of-spec-check` must read VALID on the committed bytes. Close the change-management entry. Report once:
- the dry-run and live output lines of both steps for every key;
- the VersionId list's file path;
- every criterion's output lines;
- the change-management entry's slug and state;
- any row.

Flip `<status>` to `complete` only if every criterion PASSES.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** CTO~DELL1 round-91 analysis @f6eb45c478 item 4: "a store write under its own never-widen pair, ordered after item 5". STAGED. THE GO WAITS ON ALL OF: (1) `AMGT-qq-3` (the block bound) terminal and merged, with the issuer's dry-run re-verification over all stored analysis objects re-read on the merged code (a point verified at the base and held after, or a changed set that differs from this order's, is a STOP to the CTO); (2) the pair: the COO half is written from that re-read, member by member (key, accession, stored points, expected points), and names the writer census (`analyze.write_pool` path for `filings/v1`, `analyze.write_outputs` drafting-only for `drafting/v1`: N writers read and printed), both branches, the VersionId rollback; the CTO half signed; (3) the round-92 redeploy (`AMGT-qq-5`) and this act never share a window, the second re-measures against the state the first left (the CTO's round-91 sequencing rule). The visible effect, for the pair: a chart for BABA (2 verified points) and SAP (3) on the Opal-internal Security Analysis page, and ASML's single point that the old pattern verified on the last digit of `12.4` leaves its driver. Precedent for the splice: round 52 AMGT-ab-1 (`lib/research/filings/tests/test_splice_driver.py`). Checks dry-run at the base: AC1 FAIL (R1: ASML, BABA, SAP; R2 PASS); AC2 PASS.

<status>staged</status>
<round>92</round>
<slot>0.7.0_AE_CloudOps~RA1</slot>
<fabric>dell1</fabric>
<risk>WORLD</risk>
<proof_genre>DEPLOY</proof_genre>
<worker_class>worker</worker_class>
