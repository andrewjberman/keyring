# AMGT_RESAPP task order -- `AMGT-ee-4` -- THE STORE HALF: RE-CUT THE FIVE STORED 20-F NAMES WITH THE MERGED CUTTER, ASML NA FIRST, AND RE-ANALYZE THEM

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-ee-4</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~321</issued_to>
<issued_by>2.0.0_SA_COO~R1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence; five hand runs under one pair.
comp-iam: RUN by the drafting read (round81_prep/GROUP_STORE_NOTES.md @2a2b247b7c) -- dell1's identity reads the model key's secret; it writes the silver part, the analysis and the drafting document under existing grants. No grant moves.
comp-adversary: RUN at the cut -- dd-1's census reads 0 of 5 stored 20-F names with a business section and 4 of 5 risk items from the removed fallback; all 5 at parser 1.0.0. r81_ee4_census.py and r81_store.py AC1/AC2 FAIL at the base.
EGRESS CLASS, declared: SEC EDGAR GETs (one filing per name) and one Anthropic model call per name -- open under CLAUDE.md Agent Autonomy (law edit 4d77a9c3ea, egress open except Bloomberg). No Bloomberg call.
</preflight>

**Your worktree:** the spawn names it (branch `wk-AMGT_RESAPP-321`, cut from the issuance commit). Work and commit only there. Start every shell call with `cd` into that path: a call that starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout.

## 1. THE ACT -- `AMGT-ee-4` (round 81, decomposition s.89)

Five stored 20-F names (ASML_NA_Equity, BABA_US_Equity, NU_US_Equity, PBR_US_Equity, SAP_GY_Equity) were cut by parser 1.0.0,
which kept the wrong text (ASML NA: share capital, not the business). The merged cutter (parser opal-filings-fetch/2.0.0) cuts a
business section from its own heading. Re-cut each name and re-analyze it so the served pages read the right text. ASML NA FIRST:
complete and check it before the other four.

**Begin only when** the GO names: the commit carrying AMGT-ee-3 (fetch and analyze import on this box), both halves of the pair, and
the change-management entry's slug. Read BOTH halves (their sha256 into the entry) before the first live act; STOP with a BLOCKING row
if either is absent. Read `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round81_prep/GROUP_STORE_NOTES.md` whole first.

Per name, in this order (run each command with `py -3.12`, whose anthropic SDK reads `output_config`; report the version):
1. Record the PRE-ACT state in the entry: the analysis key's and the drafting key's current VersionIds (head-object), and the
   silver filing_source parts listed for the name.
2. Fetch + silver: `python -m lib.research.filings.fetch --security-key <KEY> --form 20-F --cik <CIK> --write-pool` (CIK MEASURED from
   the stored row's `filing_identity`, never typed from memory; ASML NA's is 937966).
3. Analyze + draft: export `ANTHROPIC_API_KEY` from `comp-secrets get anthropic-api-key --reveal` IN THE SAME CALL, then
   `python -m lib.research.filings.analyze --security-key <KEY> --source-json <the fresh source.json from step 2> --write-pool`.
   ALWAYS pass `--source-json`: without it a cached parser-1.0.0 copy may be re-analyzed.
4. Read whether `drafting_build.py`'s splices (`--splice-driver`, `--hold-unspanned`) ran on the name's prior draft (the notes,
   section 1.3); if they did, re-run them on the new draft and say so.
5. After ASML NA: run AC1 and AC2. If either reads NO, STOP and roll ASML NA back (below) before touching another name.

**ROLLBACK, no delete (R2):** for each overwritten key, re-write the prior VersionId's bytes as the newest version (copy-object from
that VersionId). A new silver part is never deleted: it is superseded by re-appending the prior row's content as a newer part.
A failing criterion is the rollback trigger for that name.

Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing. Rows: id form `AMGT_RESAPP-D1-W321-S<k>` (dell1's registered coordinate is D1), `disarm_owner` `2.0.0_SA_COO~R1`.

## 2. BOUNDS

1. The act and nothing else: the three keys per name the notes name, no other store write, no deploy, no schedule.
2. No S3 delete, ever: rollback re-writes the prior version.
3. No Bloomberg call. No `bun`, `npm` or `pip install`.
4. Standing: no push of shared branches.

## 3. SURFACES

<paths>
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~321/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 3600)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-ee-4"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round81_prep/checks/r81_store.py" --crit AC1; echo "exit=$?"</invocation><expect>ASML NA's latest stored source carries a business section cut from its own heading; S1-S3 PASS; R81 STORE AC1 SERVED: YES; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-ee-4"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round81_prep/checks/r81_store.py" --crit AC2 --where deployed; echo "exit=$?"</invocation><expect>the live /thesis for ASML NA answers 200, serves the share-capital refusal sentence 0 times and cites a business section; T1-T3 PASS; R81 STORE AC2 SERVED: YES; and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-ee-4"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round81/checks/r81_ee4_census.py"; echo "exit=$?"</invocation><expect>the census names the five stored 20-F names, all at parser opal-filings-fetch/2.0.0, ASML NA's business from its own heading, no risk item from the fallback heading; E1-E4 PASS; R81 EE4 CENSUS: YES; and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~321 <0.9.0_WK_AMGT_RESAPP~321@opal.agent>" -F <msgfile> -- <paths>`
(message file written with the Write tool; confirm with `git log -1`). Instance at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~321/AMGT_RESAPP.TO-AMGT-ee-4.the-store-half-five-20f-names.proof_of_spec.json`.
Run `python .tools/proof-of-spec-check.py <instance>` on the committed bytes and report its verdict line. Do not stage `portal`.
Report once:
- the commit hash;
- per name: the pre-act VersionIds, the new ones, the silver part written, the model call count and tokens;
- every criterion's output lines;
- the change-management entry's slug and state;
- any name that could not be re-cut, and why;
- any row.

The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** CTO~DELL1 round-80 analysis @6d8d699c09 enrichment item 1, R1 (runs on dell1) and R2 (no-delete rollback); ADDENDUM 1 (opens after the lazy-import cell). STAGED: waits for AMGT-ee-3's merge (a site-Z deploy under 1.0.0_SA_CTO~Z's half) and this act's own pair (COO + 1.0.0_SA_CTO~DELL1). Checks dry-run at the base: AC1 base: FAIL as expected (S1-S3 FAIL); AC2 base: FAIL as expected (T2, T3 FAIL on live OUOsYXa); AC3 base: FAIL as expected (5 of 5 at parser 1.0.0; E2-E4 FAIL).

<status>staged</status>
<round>81</round>
<slot>0.9.0_WK_AMGT_RESAPP~321</slot>
<fabric>dell1</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<status>staged -- pair COMPLETE: COO half @ede6ff8d46, CTO half @83812df206 (1.0.0_SA_CTO~DELL1 msg 1723) with four conditions: (1) GO only after AMGT-ee-3 merges under 1.0.0_SA_CTO~Z's half and the import check (fetch and analyze import on this box) is printed; (2) NO HALF-LANDED NAME: if a name's model call fails or the analysis refuses, that name's silver part is rolled back in the same act (a newer part re-carrying the prior row), so served text never sits beside an analysis built from different text; (3) the ASML NA gate (AC1, AC2 YES before the other four); (4) the change-management entry, with the prior silver row and both prior VersionIds per name recorded before the first write. Graded by no gate limb (a modification).</status>
<status>pending -- GO 2026-10-09T06:1xZ by the issuer. Condition 1 MET: AMGT-ee-3 merged @74132a59ba under 1.0.0_SA_CTO~Z's half @603bc77c1d (ledger CLOSED); the import check printed on the merged tree: `import lib.research.filings.fetch, lib.research.filings.analyze` -> IMPORT-OK under py3.12 and py3.14 on dell1. Pair: COO @ede6ff8d46 + CTO @83812df206 (four conditions, recorded @2f2fe33df5). Worktree C:/tmp/r81-321 (branch wk-AMGT_RESAPP-321) cut from the HEAD carrying ee-3. Open your own change-management entry with slug amgt-resapp-r81-ee4-store-half-dell1 before the first write and commit it at once (a staged entry holds every merge on the box).</status>
<status>cancelled -- ISSUER RULING 2026-10-09T06:4xZ (2.0.0_SA_COO~R1): the act STOPPED correctly at ASML NA's fetch (drained @24435e4c59, proof VALID in its worktree): the merged cutter (opal-filings-fetch/2.0.0) cut no item -- business, risk or mdna -- from ASML's 20-F (asml-20251231.htm), every pattern matching only a contents line, so the fetch returned UNRESOLVED-SOURCE and the CTO's condition 3 (ASML gate) held the other four. No served key moved (heads re-read equal to the pre-act VersionIds; silver 1 part; 0 model calls); ledger amgt-resapp-r81-ee4-store-half-dell1 CLOSED. One write outside the pair's three keys: fetch.persist wrote the NEW state key amgt/harvest/state/filing_attempt/security_key=ASML_NA_Equity/UNRESOLVED-SOURCE.json (VersionId XCTQo1uW..., 2338 B), not served while ASML's drafting status is SERVED; left in place (no delete); disclosed to 1.0.0_SA_CTO~DELL1. The repair -- 20-F heading patterns that match each filing's own headings -- is a producer change outside this frozen round: carried to round 82 by row AMGT_RESAPP-D1-W321-S1.</status>
