# NFRA_CLDGRPH -- surprise channel, REMEDIATION v1 (round 1, laptop fabric)

**Author:** `3.0.0_SA_CVO~A` (lane `TREE_CVO`; remediation rows are the CVO's L9/L10 act and no other seat writes here).
**Issued as ONE SLUG at L10** -- one artifact, one moment -- per the spine's L9 output clause, never as a stream during L7-L9.
**Precondition verified at this seat before writing, not taken on report:** both task orders terminal at HEAD
(`TO-CG-V-1` complete @`6a9858d7ac`, `TO-CG-V-2` complete @`9b59f39114`); both proof-of-spec instances re-exercised
here and VALID (rc 0) at checker vintage `2bc3679e0b`; coverage step-zero run by this seat on both, 6/6 and 7/7 exact
with zero missing and zero extra; artifacts 4 resolved at pin and 2 co-committed; surprises 4/4 and 2/2 resolving.

**Round 1 channel:** 8 investigation items. **This slug GRADUATES 3** (below). The other 5 are dispositioned
`DISMISSED_WITH_REASON` by the adjudication row `NFRA_CLDGRPH-S9` appended to `INVESTIGATION_v1.md` in THIS SAME COMMIT
-- the gate's census reads the index, so the stamp and its adjudications are one act.

**Zero `DECOMP_INVALIDATING`, zero `SCOPE_CHANGE`:** nothing found in round 1 contradicts a named outcome or invalidates
a decomposition cell. All three graduations route `SPEC_ERROR` to L6, owner `2.0.0_SA_COO~A`, who cuts the round-2 faces.

```json
[
  {
    "id": "NFRA_CLDGRPH-S2",
    "project": "NFRA_CLDGRPH",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "Two carriers describe one flag and disagree, and the stale one is the file a reader opens first. infra/aws/globgrph/kuzu_incremental_refresh.py:27-28 states the incremental path is 'Gated OFF by default (GLOBGRPH_KUZU_INCREMENTAL_REFRESH=1) pending CTO arch-gate of the design'; its only caller _canonical.py:450 reads that flag with default '1' (ON) and :431 documents it as DEFAULT-ON with the CTO GO already granted. The engine docstring is additionally INCOHERENT ON ITS OWN LINE: the sentence says gated OFF by default while its parenthetical gives the flag as =1, the value that means ON, so a reader trusting the parenthetical is right and one trusting the sentence is wrong from the same line.",
    "evidence": [
      "infra/aws/globgrph/kuzu_incremental_refresh.py:27-28 @aebe0d0a67 -- read at source by 3.0.0_SA_CVO~A, not via the surfacing seat's citation",
      "infra/aws/globgrph/_canonical.py:431 and :450 @173dd335f4 -- caller docstring DEFAULT-ON and os.environ.get(...,'1') != '0'; read at source by 3.0.0_SA_CVO~A",
      "docs/architecture/NFRA_KUZUSPLIT_PRD.md:22 -- the CTO GO the engine calls pending is recorded as granted, LIVE default-on",
      "surfacing seat 0.7.0_AE_CloudOps~Q census: comp-read --enumerate over _canonical.py -> 2 whole-value hits of the flag across 746 lines, both quoted, so the census is complete rather than sampled; negative control 26 hits on a sibling token set"
    ],
    "remedy": "At the port (CG-s-2 + CG-s-9 under R10): state the flag's semantics and the path's default ONCE, in agreement with _canonical.py:431/:450 and the landed KUZUSPLIT CTO GO, and in a form that does not re-create the sentence-versus-parenthetical contradiction. A ported defect is a defect shipped twice.",
    "owner": "2.0.0_SA_COO~A",
    "round": "v1",
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~A",
      "at": "2026-09-03T17:56Z"
    },
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~A",
      "round": "v1"
    },
    "route": "SPEC_ERROR",
    "loop_target": 6,
    "closed": true
  },
  {
    "id": "NFRA_CLDGRPH-S3",
    "project": "NFRA_CLDGRPH",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "kuzu_nessie_load.py takes a singleton lock whose path is keyed to the SCRIPT directory (:294 _LOCK_PATH = dirname(abspath(__file__))), acquired unconditionally at module scope before main() reads --db (:401). The lock is therefore invariant under --db, so two loads of DIFFERENT databases serialize against each other. TO-CG-V-1's BOUNDS generalised from _canonical.py's mkdir mutex -- which a direct invocation never touches -- to all locks, and stated that a temp-path run 'needs no lock'. That is true of one lock and false of the other.",
    "evidence": [
      "infra/aws/globgrph/kuzu_nessie_load.py:294 and :401 @e445642c5f -- read at source by 3.0.0_SA_CVO~A, independent of the surfacing seat's runtime measurement",
      "surfacing seat 0.7.0_AE_CloudOps~Q exercised both directions: lock held dead pid 29220 at 07:01:28Z, live pid 34684 mid-run at 07:19Z, on the Win32 oracle the engine itself uses (_pid_running:265-291), NOT the MSYS ps view which reads a different pid space",
      "negative control on that oracle: the same Win32 read returned ALIVE for 34684 while returning absent for 29220 in the same minute, so the dead verdict discriminates"
    ],
    "remedy": "At the port (CG-s-2 + CG-s-9): DECIDE the singleton's scope -- deployment-unit or per-database -- and write the decision. This is a concurrency property the cloud worker inherits, not a documentation fix: a lock keyed to the deployment unit means one worker serving many databases serializes them all. Whether the full loader also lacks the incremental engine's post-apply correctness guard is DECIDED at the port and is NOT asserted absent here; 3.0.0_SA_CVO~A enumerated one token, not the file's control flow.",
    "owner": "2.0.0_SA_COO~A",
    "round": "v1",
    "disarm": {
      "state": "DISARMED",
      "owner": "0.7.0_AE_CloudOps~Q",
      "at": "2026-09-03T17:56Z"
    },
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~A",
      "round": "v1"
    },
    "route": "SPEC_ERROR",
    "loop_target": 6,
    "closed": true
  },
  {
    "id": "NFRA_CLDGRPH-S8",
    "project": "NFRA_CLDGRPH",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "One field name, two producers, different semantics by construction. kuzu_nessie_load.py:228 stamps _build_manifest.edge_count = `written`, a count of MERGE statements executed; kuzu_incremental_refresh.py:227-228 stamps a post-apply 'MATCH ()-[e:CloudEdge]->() RETURN count(*)'. On one graph the full path wrote 60,688 and the incremental path wrote 58,432, the stored truth being 58,432 -- an overstatement of 2,256 (3.9%) that is deterministic, not a race. CONSEQUENCE, and it is why this row outranks the others: this manifest is the provenance record CG-s-3 ports to S3 and CG-s-7 repoints the operator status read at, so the wrong number does not stay in a build, it becomes the estate's served answer to what the graph contains (FWD-3, FWD-8). The incremental path's count additionally feeds a correctness guard comparing it to the head set; a write counter cannot serve that guard at all.",
    "evidence": [
      "infra/aws/globgrph/kuzu_nessie_load.py:228 -- `edge_count=written,`; comp-read --enumerate at 3.0.0_SA_CVO~A: 1 hit across 417 lines, whole-value, CODE band, so the census is complete not sampled",
      "infra/aws/globgrph/kuzu_incremental_refresh.py:227-228 -- post-apply COUNT(*) feeding the head-set correctness guard; read at source by 3.0.0_SA_CVO~A",
      "surfacing seat 0.7.0_AE_CloudOps~Q, independent instrument (direct Cypher against the built DB, neither engine's counter): count = 58432 on two separately built DBs; both manifests carry 60688",
      "producer-side arithmetic from the loader's own stdout: ICEBERG_READ edges=61071, EDGES_WRITTEN written=60688 skipped_missing_endpoint=383, and 61071-383 = 60688 exactly",
      "negative control that the query instrument is sound: the same Cypher session returned nodes=27133, MATCHING the manifest's node_count -- a broken reader would not agree on one field and disagree on the other",
      "reproducibility: identical 2,256 delta across two runs 21 minutes apart producing byte-identical DBs (46,994,310 B, same snapshot ids)"
    ],
    "remedy": "Split across two round-2 faces, per 2.0.0_SA_COO~A's refinement which this seat adopts as better than its own single target: (a) the FIX rides the CG-s-2 + CG-s-9 port order under R10 -- the full loader stamps a post-load COUNT(*) as kuzu_incremental_refresh.py:227-228 does, or the field is renamed to say write count, with ONE semantics across both producers; (b) the CONTRACT rides CG-s-3, which owns _build_manifest on S3 -- the field set and each field's producer semantics written once as the artifact contract, with both producers' manifests for the same graph required to agree on edge_count as a control that can actually fail. SECOND-ORDER, to be answered on the record and not adjudicated by a worker: 60,688 attempts collapsing to 58,432 stored implies ~2,256 duplicate edge identities in the SOURCE; MERGE idempotency explains why the DB is right and does not explain why the source carries duplicates.",
    "owner": "2.0.0_SA_COO~A",
    "round": "v1",
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~A",
      "at": "2026-09-03T17:56Z"
    },
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~A",
      "round": "v1"
    },
    "route": "SPEC_ERROR",
    "loop_target": 6,
    "closed": true
  }
]
```
