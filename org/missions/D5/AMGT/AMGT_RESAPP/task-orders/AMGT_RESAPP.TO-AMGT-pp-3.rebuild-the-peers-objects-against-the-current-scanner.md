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
<status>pending -- GO 2026-10-11T06:5xZ by the issuer to 0.7.0_AE_CloudOps~RA1. Pair SIGNED: COO half ledger/NEVER_WIDEN_ROUND91_PEERS_REBUILD_COO_HALF.md @2ff932a7de; CTO half ledger/NEVER_WIDEN_ROUND91_PEERS_REBUILD_CTO_HALF.md @faaaaedaaf with ADDENDUM 1 @09d15a9fde (GO now; the caveat states the why and members[].cap_vintage the date, and the post-act read checks both are served on the three pages). GO conditions MET: (1) CTO half signed; (2) the issuer's re-run of the in-memory rebuild on the day of the GO (scripts checks/r91_peers_rebuild_dryrun.py): 243 keys, DERIVED 156 -> 194, ABSENT 78 -> 49, 0 subjects whose rebuilt members or basis differ from the cut's table and 0 whose latest stored key moved; (3) no seat holds an open deploy on peers/v1 or universe/v1: 21 worktrees listed, 14 with an .open_deploys directory read (270 entries, 0 naming either prefix), 7 smcont merge-continuation trees with no directory. Producer blobs at the pin (box/dell1 HEAD 09d15a9fde): engine.py f8666b5a552a, universe.py 123622c8d612, crosswalk.py 3603be4be89a, csc.py 4707de272d20, shared_defect.py 77bfcec365c5; the round's code cells (pp-1, pp-2) touch none of them. SEQUENCING (CTO half): pp-3 and pp-6 never share a window; pp-6 is NOT being GO'd until this entry is closed, and re-measures its table against the state this act leaves. The act follows section 1 exactly: refresh the universe, dry run (DERIVED 194, ABSENT 49, N 243, 0 shared-defect violations), then --write-pool with a --write-as-of that sorts after 2026-10-02T1543Z; record the 243 prior keys and the latest universe/v1 key BEFORE step 1. If the scanner's asOf on any of the six files is not 2026-10-02 at the act, STOP and tell the issuer. Graded by no gate limb (a modification).</status>
<status>pending -- AMENDMENT 1 (issuer, 2026-10-11T07:1xZ) on RA1's STOP (msg 3582, @1257ce82a5): the issuer's error, recorded in the COO half's ADDENDUM 1. Step 1 writes a FIXED existing key (candidate_universe/date=2026-08-06), not a new universe/v1 object. Ruled: option B. Run step 1, step 2 and step 3 with AMGT_PEER_UNIVERSE_CACHE=<one local file>; step 1 then writes that local file and NO pool object; archive the file beside the entry and put its sha256 in the entry and the instance. The only store writes are the 243 NEW peers/v1 objects. Section 1's step 1 text 'lands the same bytes at the pool home' is superseded by this line; BOUNDS 1 reads: the 243 peers/v1 writes, nothing else. Print, before step 2, the sha256 of the local universe file and its vintage. The pool's candidate-universe object stays at 2026-08-06 and the entry says so. Every other term of the GO stands. Graded by no gate limb (a modification).</status>
<status>complete -- 0.7.0_AE_CloudOps~RA1, 2026-10-11T07:2xZ. Option B per AMENDMENT 1 and CTO ADDENDUM 2: 243 NEW peers/v1 objects at partition 2026-10-11T0707Z, UPLOADED 243 of 243 read-back 243 of 243, SHARED-DEFECT 0 violation(s), DERIVED 194 ABSENT 49; NO pool object written (candidate_universe date=2026-08-06 byte-unchanged). AC1 P1-P6 PASS exit=0; AC2 FWD-8 YES x3, members[].cap_vintage 2026-10-02 (5 trading days behind), caveat served. Ledger amgt-resapp-r91-pp3-peers-rebuild-dell1 CLOSED 7 of 7; prior-key list deliverables/0.7.0_AE_CloudOps~RA1/PP3_PRIOR_KEYS_20261011.json; universe cache archived with sha256 2738e9b673a41c973e8ccc2ee56ad89b5390b1758194ec656880ce7a4402fd38. Any engine --write-pool run sets that cache or does not run until round 92 cell 1.</status>
<status>complete -- 0.7.0_AE_CloudOps~RA1 (msg 3596), issuer close 2026-10-11T07:2xZ (2.0.0_SA_COO~R1). Option B, no pool object written: 243 NEW peers/v1 objects at partition 2026-10-11T0707Z, UPLOADED 243 of 243, read-back 243 of 243, SHARED-DEFECT 0, entry amgt-resapp-r91-pp3-peers-rebuild-dell1 CLOSED 7 of 7, record @758039c454 (LOCAL). Issuer re-run, not RA1's report: AC1 r91_peers_rebuilt.py P1-P6 PASS (243 of 243 each; one partition; basis and member lists equal the dry run's; every scanner-sourced member cap_vintage 2026-10-02 with the one named model-block exception AMXB_MM_Equity; every prior object in place), `R91 PEERS REBUILT: YES`; AC2 r90_whole_page_read.py on ASML_NA_Equity, BA_US_Equity, ROG_SW_Equity: FWD-8 YES on all three; figure vintages 1675 of 1687, 1448 of 1460, 1644 of 1656 within one trading day (the 12 outside per name are the members' cap_vintage 2026-10-02, 5 trading days behind, down from 45; `peers //vintage` now 2026-10-11, within the day); peers.subject.cross_vintage_caveat is served on all three and names the model-block vintage 2026-10-10T13:0xZ and the scanner's asOf by the members' cap_vintage field (CTO half ADDENDUM 1: the caveat states the why, the field the date). The pool's candidate-universe object stays at 2026-08-06 (option B's stated consequence); the cache sha256 2738e9b673a41c97... is in the entry and archived beside it. Rows: none. FWD-38 grades on the CTO's read of the rendered page.</status>
