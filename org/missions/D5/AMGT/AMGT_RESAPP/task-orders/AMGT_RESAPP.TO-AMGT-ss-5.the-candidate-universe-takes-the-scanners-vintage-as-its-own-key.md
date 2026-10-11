# AMGT_RESAPP task order -- `AMGT-ss-5` -- THE CANDIDATE UNIVERSE'S POOL OBJECT TAKES THE SCANNER'S VINTAGE AS ITS OWN NEW DATED KEY

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-ss-5</owned_cells>
</decomp_ref>
<issued_to>0.7.0_AE_CloudOps~RA1</issued_to>
<issued_by>2.0.0_SA_COO~R1</issued_by>
<to_id>AMGT_RESAPP.TO-AMGT-ss-5.the-candidate-universe-takes-the-scanners-vintage-as-its-own-key</to_id>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- one operator-run refresh, no schedule is created or changed.
comp-iam: DECLARED-NOT-APPLICABLE -- the caller's own credentials; the refresh's GETs and the one put-if-absent are to the prefixes the module already writes.
comp-adversary: RUN at the cut -- r93_universe_pool.py reads U1 FAIL (no dated key), U2 FAIL, U3 PASS, U4 FAIL (the loader raises the CSC refusal) at the base against the live pool; `r92_universe_home.py` (fake S3) proves the writer's arms H1-H5 on the merged code.
EGRESS CLASS, declared: NONE (S3 reads of the scanner bucket and the pool; no vendor, SEC or model call).
</preflight>

## 1. THE ACT -- `AMGT-ss-5` (round 93, decomposition s.101)

CTO~DELL1 round-92 analysis item 4. The pool holds the candidate universe only at `date=2026-08-06`; the scanner is at asOf 2026-10-02, and the
loader REFUSES that old document against the newer scanner (`REFUSED: CSC carry scanner vintage differs for sp500`), so every rebuild since
round 91 has run from a local cache file. `AMGT-qq-2` (merged @9d4236533c) made a refresh write `date=<the document's own vintage>`, head the
target first and never overwrite. ONE write, from the checkout at the GO's pin:

`python -m lib.research.peers.universe --refresh`

It re-reads the six scanner files, writes the local read-cache and lands the pooled payload at
`amgt/harvest/gold/candidate_universe/date=2026-10-02/candidate_universe.json` (a NEW key; absent -> put, same bytes -> no second put, other
bytes -> refused). BEFORE it: record the current VersionId of `date=2026-08-06` (`D.ZdXaKfQXNoHYeZ7.58h0t7peUmVcKB` at the cut, one version),
print the dry reading of the scanner files' asOf (all six must carry 2026-10-02 or the refresh REFUSES), and sweep every live worktree's open
deploys for entries naming `candidate_universe` (print the per-tree denominator). Open a change-management entry first and close it last.
Rollback: the new key is a new object; its removal is the owner's call and is NOT done by this seat (no delete); the old key is untouched.

## 2. BOUNDS

1. The act and nothing else: the writes named, for the keys named; no function, role, route, schedule or other prefix.
2. No S3 delete, ever. No Bloomberg, SEC or model call. No `bun`, `npm` or `pip install`.
3. Standing: no push of shared branches.
4. (dell1 IAM parity, CTO~DELL1 ADDENDUM 3 @947dd446e5) A send that writes a firm data bucket, or assumes the 49F principal outside the runner's own job, is told to the laptop FIRST.
5. Every send to mdpf-daily-runner is reported after the fact, with its command id and purpose.
6. 49 Financial data never goes into another firm's tree.
7. A change the pair's table does not name is a STOP and, inside the same hour, a stop and a report; no object is deleted on the evidence.
8. Do NOT run the refresh with `--cache` or with `AMGT_PEER_UNIVERSE_CACHE` set: that is the local override that skips every pool write.

## 3. SURFACES

<paths>
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.7.0_AE_CloudOps~RA1/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 3600)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-ss-5"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round93_prep/checks/r93_universe_pool.py" --prior-version-id D.ZdXaKfQXNoHYeZ7.58h0t7peUmVcKB; echo "exit=$?"</invocation><expect>PASS U1 (the dated key for 2026-10-02 exists), PASS U2 (vintage, rows and document-sha256), PASS U3 (date=2026-08-06 untouched: current VersionId equals the prior), PASS U4 (the loader returns 2026-10-02); R93 UNIVERSE POOL: YES; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-ss-5"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; bash "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round89_prep/checks/r89_peers_deployed.sh" &amp;&amp; bash "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round89_prep/checks/r89_deployed_close.sh" --want amgt-corpus-dossier/11; echo "exit=$?"</invocation><expect>the no-regression arm: R89 PEERS DEPLOYED: YES and R89 DEPLOYED CLOSE: YES (dossier /11, the withhold and the listing byte-equal) with the function's CodeSha256 re-read, unchanged; and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

The instance is genre DEPLOY, with a NAMED rollback and the recorded VersionIds as the discriminating control, at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.7.0_AE_CloudOps~RA1/AMGT_RESAPP.TO-AMGT-ss-5.the-candidate-universe-takes-the-scanners-vintage-as-its-own-key.proof_of_spec.json`.
`proof-of-spec-check` must read VALID on the committed bytes. Close the change-management entry. Report once:
- the dry-run and live output lines of every step;
- the VersionId list's file path;
- every criterion's output lines;
- the change-management entry's slug and state;
- any row.

Flip `<status>` to `complete` only if every criterion PASSES.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** CTO~DELL1 round-92 analysis @1edd8be57d item 4: "It runs before or with item 3's rebuild, never after it, so peers are not rebuilt twice on two universes." STAGED. THE GO WAITS ON: the pair (the COO half names the scanner's six files and their asOf as read at the GO, the document's expected `vintage` and row count from a dry build, the writer census of the key, the new-key rollback); and the sequencing rule with ss-4 and ss-6. The peers rebuild (`AMGT-ss-6`) runs AFTER this act or in the same window, never before. The act's served effect is none on its own: the function reads peers objects, not the universe.

<status>staged</status>
<round>93</round>
<slot>0.7.0_AE_CloudOps~RA1</slot>
<fabric>dell1</fabric>
<risk>WORLD</risk>
<proof_genre>DEPLOY</proof_genre>
<worker_class>worker</worker_class>
