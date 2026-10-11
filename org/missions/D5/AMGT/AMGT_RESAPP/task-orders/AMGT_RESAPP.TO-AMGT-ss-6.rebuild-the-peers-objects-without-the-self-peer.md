# AMGT_RESAPP task order -- `AMGT-ss-6` -- REBUILD THE PEERS OBJECTS SO NO SUBJECT LISTS ITS OWN COMPANY

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-ss-6</owned_cells>
</decomp_ref>
<issued_to>0.7.0_AE_CloudOps~RA1</issued_to>
<issued_by>2.0.0_SA_COO~R1</issued_by>
<to_id>AMGT_RESAPP.TO-AMGT-ss-6.rebuild-the-peers-objects-without-the-self-peer</to_id>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- one operator-run batch, no schedule is created or changed.
comp-iam: DECLARED-NOT-APPLICABLE -- the caller's own credentials write the prefix the engine already writes (`peers/v1/`).
comp-adversary: RUN at the cut -- r93_self_peer_census.py against its own baseline reads S1 FAIL (10 subjects list their own company), S2-S4 PASS; r93_self_peer.py proves the ranker's arms on fixtures.
EGRESS CLASS, declared: NONE (S3 reads and puts; no vendor, SEC or model call).
</preflight>

## 1. THE ACT -- `AMGT-ss-6` (round 93, decomposition s.101)

CTO~DELL1 round-92 analysis item 3, second half. `AMGT-ss-3` (merged before this GO) makes the ranker exclude a row that is the subject's own
company by held identity and builds the held-name index once per batch; `AMGT-ss-5` has landed the universe at the scanner's vintage. ONE
batch over the 243 MEASURED subjects, from the checkout at the GO's pin, writing a NEW partition (never an existing one):

`python -m lib.research.api.peers_rebuild --as-of <the batch date> --write-as-of <a partition string that sorts AFTER 2026-10-11T0707Z, e.g. 2026-10-11T1100Z> --write-pool` (the caller above the peers package that builds the held-name index; `python -m lib.research.peers.engine` runs WITHOUT the rule and must not be used)

It writes `peers/v1/<security_key>/<write-as-of>.json` for each subject; every reader picks the latest partition by plain string order. BEFORE
it: run `r93_self_peer_census.py --write-baseline <file>` (the 243-route read of the live function, the pair's before column) and the single-
subject dry run (`--security-key ROG_SW_Equity --dry-run`) printing `self_excluded_by_identity`; record the prior partition's object count (243);
sweep every live worktree's open deploys for entries naming `peers/v1`; open a change-management entry first and close it last.
Rollback: the new partition's objects are new keys (no delete by this seat); reverting the served set is the owner's call by re-pointing readers to
the prior partition through a newer partition built from the prior code, never by deleting.

## 2. BOUNDS

1. The act and nothing else: the writes named, for the keys named; no function, role, route, schedule or other prefix.
2. No S3 delete, ever. No Bloomberg, SEC or model call. No `bun`, `npm` or `pip install`.
3. Standing: no push of shared branches.
4. (dell1 IAM parity, CTO~DELL1 ADDENDUM 3 @947dd446e5) A send that writes a firm data bucket, or assumes the 49F principal outside the runner's own job, is told to the laptop FIRST.
5. Every send to mdpf-daily-runner is reported after the fact, with its command id and purpose.
6. 49 Financial data never goes into another firm's tree.
7. A change the pair's table does not name is a STOP and, inside the same hour, a stop and a report; no object is deleted on the evidence.
8. The write set is the 243 `peers/v1/<key>/<new partition>.json` objects and nothing else; the prior partition's objects are not touched.

## 3. SURFACES

<paths>
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.7.0_AE_CloudOps~RA1/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 3600)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-ss-6"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round93_prep/checks/r93_self_peer_census.py" --baseline "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round93_prep/PEERS_BASELINE_20261011.json" --class-b HEI_US_Equity:HEI.A,JD_US_Equity:BKPQZT; echo "exit=$?"</invocation><expect>PASS S1 (no subject lists its own company; the baseline's 10 are gone), PASS S2 (every removed member was an own-company member), PASS S3 (backfilled to the baseline count), PASS S4 (control: every other subject member-for-member equal), PASS S5 (HEI.A and BKPQZT, the pair's class B, were members and are gone); R93 SELF PEER CENSUS: YES; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-ss-6"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; bash "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round89_prep/checks/r89_peers_deployed.sh" &amp;&amp; bash "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round89_prep/checks/r89_deployed_close.sh" --want amgt-corpus-dossier/11; echo "exit=$?"</invocation><expect>the no-regression arm: R89 PEERS DEPLOYED: YES and R89 DEPLOYED CLOSE: YES (dossier /11, the withhold and the listing byte-equal) with the function's CodeSha256 re-read, unchanged; and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-ss-6"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round92_prep/checks/r92_minor_unit_census.py"; echo "exit=$?"</invocation><expect>the currency arm is unmoved by the rebuild: PASS M1, PASS M2, PASS M3, PASS M4; R92 MINOR-UNIT CENSUS: YES; and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

The instance is genre DEPLOY, with a NAMED rollback and the recorded VersionIds as the discriminating control, at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.7.0_AE_CloudOps~RA1/AMGT_RESAPP.TO-AMGT-ss-6.rebuild-the-peers-objects-without-the-self-peer.proof_of_spec.json`.
`proof-of-spec-check` must read VALID on the committed bytes. Close the change-management entry. Report once:
- the dry-run and live output lines of every step;
- the VersionId list's file path;
- every criterion's output lines;
- the change-management entry's slug and state;
- any row.

Flip `<status>` to `complete` only if every criterion PASSES.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**AMENDMENT 1 (issuer, 2026-10-11, on RA1's finding msg 3811):** AC1's S2 and S4 defined own-company by the served `security_key` and so contradicted the CTO's signed class B (HEI.A, BKPQZT: the subject's own other share-class lines, which pp-1's N8 guard leaves without the subject's key). The census takes them as `--class-b` input and gains S5. An issuer check error, not the act's. The writes stand.

**ISSUER NOTES:** CTO~DELL1 round-92 analysis @1edd8be57d item 3. STAGED. THE GO WAITS ON: (1) `AMGT-ss-3` terminal and merged (issuer re-runs AC1/AC2 on the merged tree; the single-subject dry run for the ten named subjects printed); (2) `AMGT-ss-5` landed, or in the same window with its pair, never after this act; (3) the pair: the COO half is written from a member-by-member DRY run of the batch over all 243 subjects on the merged code against the baseline file (each subject's removed and added members listed; the expected removed set is the ten self members, every other subject equal), the writer census of `peers/v1/<key>/<partition>.json`, both branches; the CTO half signed; (4) the sequencing rule with ss-4 and ss-5. The ten: BZLFY_US, NOVN_SW, ORA_FP, PBR_US, ROG_SW, SAN_FP, ST_SP, TSM_US, UBSG_SW, ZURN_SW (all _Equity).

<status>staged</status>
<round>93</round>
<slot>0.7.0_AE_CloudOps~RA1</slot>
<fabric>dell1</fabric>
<risk>WORLD</risk>
<proof_genre>DEPLOY</proof_genre>
<worker_class>worker</worker_class>
<status>complete -- 0.7.0_AE_CloudOps~RA1, 2026-10-11T11:4xZ. GO msg 3798 (pin f40dd163cc). The ONE batch (lib.research.api.peers_rebuild --write-pool, universe from the pool date=2026-10-02): UPLOADED 243 of 243, read-back 243 of 243, SHARED-DEFECT 0, partition 2026-10-11T1125Z; the dry batch equalled the half's table before the write. Full-record compare of all 243 subjects (prior partition vs live): 231 member lists equal, 12 differ and are exactly the table (ten own-company + HEICO and JD.com class B), count unmoved, 0 retained-member field changes, 0 reorders; the 243 prior objects' VersionIds unmoved (1470 -> 1713 objects). AC1 as first written could not read YES for the signed class B (finding @d30a8b6b72); the issuer's AMENDMENT 1 @e6910d1ddc added --class-b and the amended AC1 re-ran literally on a checkout at that commit: R93 SELF PEER CENSUS: YES (S1-S5). AC2 YES with the function CodeSha256 unchanged; AC3 YES (M1-M4; served major-unit rows 160 -> 154 = the table's own removed members). Ledger amgt-resapp-r93-ss6-peers-rebuild-dell1 CLOSED 6 of 6. Proof instance deliverables/0.7.0_AE_CloudOps~RA1/AMGT_RESAPP.TO-AMGT-ss-6.rebuild-the-peers-objects-without-the-self-peer.proof_of_spec.json VALID rc=0.</status>
