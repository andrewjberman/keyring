# AMGT_RESAPP task order -- `AMGT-pp-3` -- REBUILD THE PEERS OBJECTS AGAINST THE CURRENT SCANNER

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-pp-3</owned_cells>
</decomp_ref>
<issued_to>0.7.0_AE_CloudOps~RA1</issued_to>
<issued_by>2.0.0_SA_COO~R1</issued_by>
<to_id>AMGT_RESAPP.TO-AMGT-pp-3.rebuild-the-peers-objects-against-the-current-scanner</to_id>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- two operator-run store writes, no schedule is created or changed.
comp-iam: DECLARED-NOT-APPLICABLE -- the caller's own credentials write two prefixes the batch already writes (`universe/v1/`, `peers/v1/`); no role or policy moves.
comp-adversary: RUN at the cut -- the producer's own `engine.peers` over the freshly built universe, in memory, for 243 keyed names against each name's latest stored object (round91_prep/PEERS_REBUILD_DRYRUN_20261011.json): DERIVED 156 -> 194, ABSENT 78 -> 49, 158 member sets change, 0 derived -> absent; r91_peers_rebuilt.py FAILs P1-P5 at the base and PASSes P6.
EGRESS CLASS, declared: NONE (S3 reads of the scanner and pool, S3 puts of two new object families; no vendor, SEC or model call).
</preflight>

## 1. THE ACT -- `AMGT-pp-3` (round 91, decomposition s.99)

CTO~DELL1 round-90 analysis item 3 (FWD-38). The stored peers objects were built against scanner vintage 2026-08-06; the six scanner
files now read asOf 2026-10-02. Rebuild them with the producer's own entry points, in this order, each preceded by the dry run the pair
names, from the repository checkout at the GO's pin (the producer is unchanged by this round's code cells):

1. **Universe.** `python -m lib.research.peers.universe --refresh` (rebuilds from the six scanner files and the model-block headers,
   writes the local read-cache, lands the same bytes at the pool home, reads back). Print the receipt.
2. **Dry run.** `python -m lib.research.peers.engine --as-of <D> --write-as-of <D>T<HHMM>Z` WITHOUT `--write-pool`, where `<D>` is today's
   UTC date and `<D>T<HHMM>Z` sorts AFTER `2026-10-02T1543Z`. Its `DERIVED`, `ABSENT` and `SHARED-DEFECT` lines must equal the pair's table
   (DERIVED 194, ABSENT 49, N 243, 0 violations) before the next step; a difference is a STOP to `2.0.0_SA_COO~R1`.
3. **Write.** The same command WITH `--write-pool`, the same `--write-as-of`. Every object is a NEW key; a put that would overwrite one
   is a STOP. Print `UPLOADED 243 of 243 ... read-back 243 of 243`.

BEFORE step 1, record for each of the 243 subjects the key of its latest stored `peers/v1/` object and the latest `universe/v1/` key
(the rollback list, in the change-management entry), read the six scanner files' `asOf` and sweep every live worktree's open deploys
for entries naming `peers/v1` or `universe/v1` (print the per-tree denominator). Open a change-management entry first and close it
last. Rollback, if the CTO names it: re-publish the recorded prior content under a still-later partition for the named subjects; never a
delete.

## 2. BOUNDS

1. The two store writes named, and nothing else: no function, role, route, schedule or other prefix.
2. No S3 delete, ever; no overwrite of an existing key.
3. No Bloomberg, SEC or model call. No `bun`, `npm` or `pip install`.
4. Standing: no push of shared branches.
5. If the scanner's asOf at the act is not 2026-10-02 on all six files, STOP and tell the issuer: the pair's table is for that vintage.

## 3. SURFACES

<paths>
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.7.0_AE_CloudOps~RA1/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 3600)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-pp-3"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round91_prep/checks/r91_peers_rebuilt.py"; echo "exit=$?"</invocation><expect>PASS P1 (every latest peers object is a new dated object, 243 of 243), PASS P2 (one write partition), PASS P3 (basis equals the dry run's, 243 of 243), PASS P4 (member tickers equal the dry run's, in order, 243 of 243), PASS P5 (every scanner-sourced member cap_vintage is 2026-10-02, with the one named model-block-only exception), PASS P6 (every prior object still in place); R91 PEERS REBUILT: YES; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-pp-3"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round90_prep/reads/r90_whole_page_read.py" "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.7.0_AE_CloudOps~RA1/PP3_WHOLE_PAGE_READ.md" ASML_NA_Equity BA_US_Equity ROG_SW_Equity; echo "exit=$?"</invocation><expect>on the live function the verdicts table reads FWD-8 identity YES on all three names; the `peers /members[]/cap_vintage` row reads 2026-10-02 (45 trading days behind the header before, 5 after) and `peers //vintage` reads the new write partition's date; and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

The instance is genre DEPLOY, with a NAMED rollback and the prior-key list as the discriminating control, at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.7.0_AE_CloudOps~RA1/AMGT_RESAPP.TO-AMGT-pp-3.rebuild-the-peers-objects-against-the-current-scanner.proof_of_spec.json`.
`proof-of-spec-check` must read VALID on the committed bytes. Close the change-management entry. Report once:
- the three commands' output lines named above;
- the 243 prior keys' file path and the new partition string;
- every criterion's output lines;
- the change-management entry's slug and state;
- any row.

Flip `<status>` to `complete` only if every criterion PASSES.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** CTO~DELL1 round-90 analysis @b462a02d8a section 3 item 3. Pair: COO half `ledger/NEVER_WIDEN_ROUND91_PEERS_REBUILD_COO_HALF.md` (this issuance); the CTO's half is owed. STAGED. THE GO WAITS ON ALL OF: (1) the CTO half SIGNED, and the CTO's word on the measured gap below; (2) the issuer's re-run of the in-memory dry run on the day of the GO (a scanner or crosswalk change re-opens the table); (3) no other seat holds an open deploy on `peers/v1` or `universe/v1`. **THE GAP THE CTO'S CLOSE DID NOT KNOW:** the analysis closes this item on `members[].cap_vintage` within one trading day of the header. The scanner's latest asOf is 2026-10-02 (it has published at 2026-02-26, 05-18, 05-19, 05-21, 08-06, 10-02), five trading days behind the header's 2026-10-10, so no rebuild from this source reaches one day. The act moves the peer caps from 45 trading days behind to 5; the criteria are cut on what the producer can deliver (cap_vintage equals the scanner's asOf, the gap printed). Whether FWD-38 grades REALIZED on "or says on the page why it is not" (the per-member `cap_vintage` is printed, the subject's `cross_vintage_caveat` names the two vintages) or waits for a fresher scanner is the CTO's call, asked in the round's one message. Checks dry-run at the base: AC1 FAIL (P1-P5; P6 PASS); AC2's cap_vintage row reads 2026-08-06.

<status>staged</status>
<round>91</round>
<slot>0.7.0_AE_CloudOps~RA1</slot>
<fabric>dell1</fabric>
<risk>WORLD</risk>
<proof_genre>DEPLOY</proof_genre>
<worker_class>worker</worker_class>
