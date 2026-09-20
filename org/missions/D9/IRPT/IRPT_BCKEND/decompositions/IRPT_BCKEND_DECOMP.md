# IRPT_BCKEND -- L5 decomposition -- round 3 -- v0.3

**v0.2** (2026-09-11 ~11:5xZ, `2.0.0_SA_COO~B`, the ROUND-2 RECUT on the CTO's round-1 analysis `ledger/ROUND_ANALYSIS.round1.md` @`0d57ceb2f9` and the CVO's slug `surprise-channel/remediations/REMEDIATION_v1.md` @`27e67fa6a5`, against PRD v0.13 @`e6ba5d9878`, ADMITTED with both L4-R halves SIGNED). Round 1 (v0.1.1, 19 cells) closed at ROUND_CLOSE with 0 of 10 REALIZED; its cells are retained below by id (section 0) so every round-1 instance's `cell_refs` still resolves in this document's id space. Round 2 is twelve cells, `IB-rt-<n>` and the battery `IB-rtb-1`, cut to the CTO's eight rulings in his order: the seam and the guards first, the three declared producers next, then export, YCharts on the v0.9 mechanism, intake controls, records.

```json
{
  "project": "IRPT_BCKEND",
  "directive": "D9",
  "fabric": "laptop",
  "round": 7,
  "decomp_version": "0.7",
  "prd_ref": "org/missions/D9/IRPT/IRPT_BCKEND/prd/IRPT_BCKEND_PRD.md@b8e98d5a4d",
  "prd_version": "v0.14",
  "round1_analysis_ref": "org/missions/D9/IRPT/IRPT_BCKEND/ledger/ROUND_ANALYSIS.round1.md@0d57ceb2f9",
  "round2_analysis_ref": "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/1.0.0_SA_CTO/IRPT_BCKEND_ROUND2_ANALYSIS.md@cfe3a33a9b",
  "round2_slug_ref": "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/adjudications/ADJUDICATION_v2.md@c1a8cd2543 (the L8/L9 commit; msg 97752)",
  "round1_slug_ref": "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/remediations/REMEDIATION_v1.md@27e67fa6a5",
  "brief_ref": "docs/briefs/investor-reporting-ir-bk-brief-20260910.md@2acf23d8fd",
  "endpoint_ref": "org/tier1_exec/1.0.0_SA_CTO/deliverables/ENDPOINT_FWD_IRPT_BCKEND_20260910.md",
  "endpoint_outcomes": [
    "FWD-1",
    "FWD-2",
    "FWD-3",
    "FWD-4",
    "FWD-5",
    "FWD-7",
    "FWD-8",
    "FWD-9",
    "FWD-10",
    "FWD-11"
  ],
  "owns_grade": [
    "FWD-2",
    "FWD-7",
    "FWD-9",
    "FWD-10"
  ],
  "cells_round2": 12,
  "cells_round3": 5,
  "cell_id_shape": "IB-rtc-<n> (round 3, the recut on the round-2 analysis); IB-rt-<n>/IB-rtb-1 (round 2, retained by id)",
  "worker_serial": "0.9.0_WK_IRPT_BCKEND~<slot> (the round-1 subagents, continued) and 0.4.0_DS_ClientPlatform~X (one DS-lane cell, the rule-13 act)",
  "cut_head_round2": "67ef99e5c2",
  "cut_head": "cfe3a33a9b (the round-2 analysis commit; HEAD at the cut is stated in the issuance commit)",
  "counterpart_decomp": "org/missions/D9/IRPT/IRPT_FNTEND/decompositions/IRPT_FNTEND_DECOMP.md",
  "round3_analysis_ref": "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/1.0.0_SA_CTO/IRPT_BCKEND_ROUND3_ANALYSIS.md @5c59f68d70",
  "cells_round4": 8,
  "cell_id_shape_round4": "IB-rtd-<n>",
  "round4_analysis_ref": "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/1.0.0_SA_CTO/IRPT_BCKEND_ROUND4_ANALYSIS.md @561d6e1cc9",
  "cells_round5": 6,
  "cell_id_shape_round5": "IB-rte-<n>",
  "cells_round6": 14,
  "cell_id_shape_round6": "IB-rtf-<n>",
  "round5_analysis_ref": "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/1.0.0_SA_CTO/IRPT_BCKEND_ROUND5_ANALYSIS.md@81472c3a47",
  "round6_analysis_ref": "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/1.0.0_SA_CTO/IRPT_BCKEND_ROUND6_ANALYSIS.md@fa2ff4f0dd",
  "cells_round7": 4,
  "cell_id_shape_round7": "IB-rtg-<n>"
}
```

**One carrier, two sources.** Each round-2 face inlines VERBATIM the PRD v0.13 candidate row it serves and the CTO's ruling it executes; this document adds the ORDER, the ROOTS, the SEATING, the FENCE, the BATTERY and the round-2 findings. It restates no PRD row and re-cuts nothing round 1 delivered: the ten converged roots, the eleven live routes, the CloudFront path, the status envelope and recovery arms, the extraction and certification, and nineteen VALID instances stand and are BUILT ON (each face's "WHAT ROUND 1 DELIVERED" section names what).

---

## R7. ROUND 7 -- THE RECUT ON THE ROUND-6 ANALYSIS (@fa2ff4f0dd, msg 98554; v0.7, 2026-09-20, `2.0.0_SA_COO~B`)

**Input:** round 6 CLOSED at L10 (0 open of 75; 47/47 AC2 PASS; 52 rows disposed, 40 graduated incl. S110). This recut's whole subject is the round's headline: THE SCOPE PLANE AND THE DATA PLANE HAVE DIVERGED -- the advisor is identified, firm-bound, scope-resolved and told exactly how much of the book is withheld (the refusal vocabulary WORKS), then served NO DATA on any tab (the data paths do NOT). No PRD addendum -- round 7 re-attempts FWD-2 (the serving/data half) and FWD-5, both existing. Scope determined by investigation a7edd66ed0: FOUR of the five residual data-plane defects are IRPT_BCKEND BACKEND handler cells; the fifth (the ownership-map count) is DS. The four carries stand (S110's vacuous negative control taints the REFUSAL side of rtf-10/rtf-12 arm-(f), served-path grants unaffected; the grant moved to 44/19; the ledger-retroactive EXPOSURE; the headline).

### R7.1 The rectangle (4 cells, id shape `IB-rtg-<n>`)

| cell | owes | assignee | serves | supersedes |
|---|---|---|---|---|
| IB-rtg-1 | EXPORT S105+S106 (ONE cell, CTO ruling @0110b9de01): align `export/entry.py:63-64,100` `RECEIPT_KEY_TEMPLATE` to the writer's `firms/{firm}/generations/.../exports/{rev}/` family AND write the receipt beside the bundle in `export/handler.py:126-130`, AND rewrite `export/entry.py:104-105`'s `except` to decide refusal off `exc.response['Error']['Code']` + HTTP status not the class name. S106 FIRST-OR-WITH S105, never after; `IRPT_EXPORT_RECEIPT_KEY` Terraform override REFUSED. Packet + halves BEFORE the deploy; acceptance on a REAL wire error (403/AccessDenied -> policy code; 404/NoSuchKey -> NOT_FOUND), never a constructed stub | WK | FWD-2 | -- |
| IB-rtg-2 | STATUS: write the real `status_loader` in `ops/` (reads TenantLease/checkpoint + `ops/manifests.py` against the backend's OWN `irpt-jobs` store) and wire it into `ops/entry.py` in place of `ops/status.py:338`'s always-raising `_default_status_loader`. Packet + halves; acceptance: an exercised status-summary for a real job returns a validated StatusEnvelope, not UNSUPPORTED_OPERATION | WK | FWD-2 | -- |
| IB-rtg-3 | PERFORMANCE (W2-S27): reconcile `performance/tenants.py:81-101` `route_for` to the id space the boundary binds on via the ESTATE'S EXISTING `_ids` normalizer -- NEVER a fourth firm-token mapping. BOUND: if the fix cannot be done without minting a new lookup, it is FirmBinding's axis (W2-S9) and is ROUTED to the CTO, not cut ad hoc. Packet + halves; acceptance: an authorized, scope-resolved performance request for each of the 3 registry firms resolves a TenantRoute, 0 fourth-id-space literals | WK | FWD-2 | -- |
| IB-rtg-4 | HOLDINGS S100 (this seat's own row): make `holdings/entry.py:88` `_load_directory` FOLLOW the `latest.json` pointer the way `_authz/loaders.py:71-78` does (holdings reads the pointer doc as the artifact). Packet + halves; acceptance: an exercised holdings request for an account the principal's own resolve granted reads a scope-resolved answer, never FIRM_BINDING with firm_id absent | WK | FWD-5 | -- |

**Not cells of this project:** the OWNERSHIP-MAP COUNT (44/19 live vs 33/18) -- DS gold, `data/assets/scripts/gold/runners_49f/d08_firm_ownership_map.py`; backend only READS it (object-scoped GetObject) and round 7's cells RE-DERIVE the count at build/measure time, NEVER inherit 33/18. FWD-11 / rtf-5 -- PARKED on Andrew's security re-scope (un-park condition + owner on the order @919a261242, not re-opened here). The S100/S110 control-repair EVIDENCE (not a cell) un-taints when IB-rtg-4 moves S100.

### R7.2 Edges and fanout
Four INDEPENDENT chains (four different handlers, disjoint write surfaces): A `rtg-1`; B `rtg-2`; C `rtg-3`; D `rtg-4`. **fanout: 4 of 4 chains, cap 8.** No cross-cell dependency (the S106-first-or-with-S105 ordering is INTERNAL to rtg-1). Each is a served-path handler deploy and STOPs at its never-widen halves on the first pass (the rtf-13 shape).

### R7.3 Bounds carried
NEVER-1 (packet + CTO+COO halves at HEAD BEFORE every deploy -- all four change served behaviour); the arm-(d) SUBTRACTION gate (the W1-S37 lesson: compare `resource_changes` per root minus a CLOSED PRINTED volatile set, never a whole-planfile digest); THE 44/19 RE-DERIVE CONSTRAINT (read the ownership map live and print the count, never inherit 33/18); R-40 (content hash per run/artifact); S56 vintage pins; the forward-looking-criterion bar; the reader-census bar; the LEDGER OPENED BEFORE the act (the W1-S41 / rtf-3 exposure -- no principal/apply cycle without a pre-opened change-management ledger); no served bytes committed as source; the identity bar (arm (e) runs the DEPLOYED role + bytes).

### R7.4 Not decided here
Whether IB-rtg-3's reconciliation needs a new firm-token mapping (if so -> the CTO, W2-S9 axis, not cut here); the status_loader's manifest shape (rtg-2's judgment, Rule 24 record); the ownership-map producer's re-key (DS, d08's owner); anything about FWD-11 (Andrew).

### R7.5 Four-postulate record (Rule 24 over the round-7 cell set)
(i) MECE over the DECLARED domain = round-6 residue section 5 MINUS {parked, DS, evidence-not-cells}: the owed set is {export S105/S106, status, performance, holdings S100, ownership-map count}; SUBTRACT the ownership-map count (DS) and FWD-11 (Andrew, parked) and the S110 evidence (un-taints via holdings) -> the four backend cells remain, none uncovered. (ii) SAME GRAIN: each cell is one handler's served-behaviour fix. (iii) INTENT COHERENCE: one axis -- make the DATA paths serve. (iv) STATE COHERENCE: a cell realizing its serving does NOT move FWD-11 (parked) or the DS count (re-derived, not fixed here).

## R6. ROUND 6 -- THE RECUT ON THE ROUND-5 ANALYSIS (@81472c3a47, msg 98115; v0.6, 2026-09-19 ~03:4xZ, `2.0.0_SA_COO~B`)

**Input:** six judgment PASS, 17 rows disposed (16 graduated with carriers, 3 dismissed), NO PRD addendum -- round 6 is a recut. Four round-5 orders closed on truthful FAILs and each FAIL is a cell here; S77 (the CVO) is the finding of the round: the cross-firm fence is stale while its stated cause is false, because the generator was never re-run after the flip -- the reader-census bar (the mirror of the writer census) is adopted on every face. The L4 rulings carried: @457cf494c6 (no-source members: measure, then branch), @61627f39f9 (partial projection: admit and disclose, three conditions). Corrections adopted: registry rows are the CRO's lane (`PLATFORM_LOGIC_DOCS`), landed @845343f925; a blob pin is written `blob <hash>`; no `memory/` path is cited on a face (S78).

### R6.1 The rectangle (5 cells, id shape `IB-rtf-<n>`)

| cell | owes | assignee | serves | supersedes |
|---|---|---|---|---|
| IB-rtf-1 | round-5 analysis s.5 item 1: the no-source members MEASURED then BRANCHED (W4-S34/S35 + W1-S26's six members + the 3 UNRESOLVED); DELTA=0 declares, DELTA!=0 packets and stops | WK~4 | provenance of every served function | IB-rte-4 |
| IB-rtf-2 | s.5 item 2 / W1-S27: the ordering inversion in `enforce.py` with the disclosure field NON-OPTIONAL, the IRPT_FNTEND consumer-obligation row, the empty branch refusing; packet + halves BEFORE the deploy (a STOP at (d) is the expected first pass) | WK~1 | FWD-1, 2, 5 | IB-rte-6 |
| IB-rtf-3 | IB-rte-2's re-cut: the principal created, the four outcomes exercised on the DISCLOSED-PARTIAL path, deleted | AE `~N` (staged, behind rtf-2) | FWD-1, 2, 5, 11 | IB-rte-2 |
| IB-rtf-4 | s.5 item 3 / S77: every generated block re-derived from the registry at HEAD, the fence proven both signs, the flag's readers censused | WK~3 | FWD-1, 7, 10 | -- |
| IB-rtf-5 | s.5 items 4-5: IB-rte-3's re-hand -- the re-apply after Andrew's step 4 under both halves naming the 4 tainted resources + the last 2 of 10 + the regenerated fence; the host control EXERCISED or UNEXERCISED, never simulated | WK~3 (staged, behind step 4 + rtf-4 + halves) | FWD-1, 7, 10 | IB-rte-3, IB-rte-7 |

**Not cells of this project:** (b) of the partial-projection ruling (the ownership-map producer re-keyed to the Schwab spine) -- DS-owned, carried to `d08_firm_ownership_map.py`'s owner; the IRPT_FNTEND rendering obligation -- the CTO's L4 carrier in FNTEND's PRD (rtf-2 files the row); FWD-11's SSM roster parameter -- a separate act with its own sign-off; IB-rtd-7's port -- still superseded behind rtf-5, both halves and the FNTEND reader cell; starting host `i-02448edb624a7a7cf` -- operational, outside every cell (a REC to the CTO: it is the only closer of W3-S44).

### R6.2 Edges and fanout

Chains: A `rtf-1`; B `rtf-2 -> rtf-3`; C `rtf-4 -> rtf-5` (rtf-5 also behind Andrew's step 4 and both halves). **fanout: 3 of 3 chains, cap 8.** Handed now: rtf-1, rtf-2, rtf-4. rtf-3 on rtf-2's drain with arm (e) passing; rtf-5 on step 4 (the issuer measures `get-bucket-policy` at the hand-off), rtf-4's drain, and both halves. The DS lane holds no round-6 order.

### R6.3 Bounds carried

R-40, R-42, R-44, R-45; the forward-looking-criterion bar; S56's vintage pins; Rule 30; NEVER-1 on every served-behaviour change (rtf-2's deploy, rtf-5's apply: both halves at HEAD BEFORE the act); the reader-census bar; `blob <hash>` notation; no `memory/` citation on a face; no served bytes committed as source on any branch (rtf-1); the empty-set branch refuses on every path (rtf-2); nothing written to either bucket (rtf-5); no host start by any cell.

### R6.5 MID-ROUND ADDITIONS (~06:4xZ 2026-09-19) -- on rows W4-S41 / W1-S29 and the Andrew-direct ~06:3xZ

`IB-rtf-6` (WK~4, `wk-irpt-6-4b`): the manifest re-pinned after the shared-surface drains. rtf-1 pinned the shared `_authz/` files to `c28c728a30`'s blobs; rtf-2 changed `enforce.py`/`served.py` and deployed through `rte6_package_deploy.py`, which bypasses the pins -- the declared source and the served bytes disagree, and a `build-and-upload.sh` from HEAD would stage the PRE-inversion bytes (a regression of @61627f39f9 by build). Re-pin to the served-matching HEAD blobs, prove the regression on the mutant, deploy nothing; the diverged `holdings/enforce.py` (W1-S29) is rowed, never pinned. Grant: `infra/aws/lambda/ci/` + the channel. The two-packager class is R63-AC2's for L4.
`IB-rtf-7` (AE `~V`, first on that seat): Andrew-direct ~06:3xZ (record `ANDREW_DIRECT_20260919_063xZ_STEP4_BUCKET_POLICY_AE_ATTEMPT_THEN_PROCEED.md`, verbatim *"have an AE deal with it. if they cant for whateve rreason, proceed and note it for later"*): step 4 -- the bucket ACCESS POLICY removed, never the bucket -- attempted with every identity the seat holds, each response verbatim under a ledger entry; success unblocks rtf-5 that tick; AccessDenied everywhere is the truthful result (only root escapes a `Principal: *` Deny), the round proceeds, and "step 4 -- Andrew at the console when next present" is carried on the drain-end packet and the slug as a PARKED item with owner and un-park condition.
`IB-rtf-3` RE-ADDRESSED `~N` -> `~V`: the /mstr-spawn 1d census found `~N` encumbered by `ETFS_POSITIONING.TO-14-AE` (site Z, 2026-08-29, ACTIVE) -- the Tier-2 one-project rule; `~V` reads 0 orders / 0 processes / 0 markers / 0 armed disarm rows / no inbox. Chains now: A `rtf-1 -> rtf-6`; B `rtf-2 -> rtf-7 -> rtf-3` (one AE seat, rtf-7 first); C `rtf-4 -> rtf-5` (rtf-5 behind step 4, whichever hand performs it). fanout 3 of 3 chains, cap 8.

### R6.6 MID-ROUND ADDITION (~08:1xZ 2026-09-19) -- on the CTO's ruling S82 (@b37fdfd5cd, msg 98178)

`IB-rtf-8` (WK~1, `wk-irpt-6-1c`): holdings' forked enforcer folded onto the shared module. The per-route census (7 `entry.py`, `os.walk`) found EXACTLY ONE local `enforce.py` -- `holdings/` -- bound by `holdings/snapshot.py:44` (`blob 8f849457be`, 635 lines, the pre-ruling refusal order, `unprojected_grant` never populated) while the shared `served.py` supplies the field present at zero: on that route a real gap renders as NO gap and no absence guard can see it -- Rule 22's shared-dependency blindness INVERTED (seven routes share `served.py`; one does not share `enforce.py`). The CTO's ruling: FOLD, never patch the fork; the fold also closes W1-S27's residual on the same route (S81: disarmed on the shared path, live on holdings). Shape: diff the fork before deleting it (a load-bearing fork-only behaviour is a STOP, never a silent drop), re-bind, re-declare the manifest member, the census as the acceptance instrument, packet + halves BEFORE the deploy (the rtf-2 shape), then the live holdings request reading `count > 0` where the fork read zero. Chains: B `rtf-2 -> rtf-8` beside `rtf-7 -> rtf-3`; fanout 3 of 3 chains, cap 8. The Surprises clause on this face names the channel's PREVAILING EOL (CRLF, measured at HEAD every line; W4-S44) rather than round 1's "LF".

### R6.7 MID-ROUND ADDITION (~08:5xZ 2026-09-19) -- on row S86 (IB-rtf-3's STOP @f60b3f0942)

`IB-rtf-9` (AE `~V`, declare-only): the two-key test-principal packet on the REAL mint path. IB-rtf-3 stopped before any write: the deployed auth-handler mints the token's advisor claim ONLY from `opal-partner-<firm>` keyed by e-mail; the first packet's K1 field (`advisorKey` on the user row) is never read, so K1 + K2 would mint a 49financial session with NO advisor claim -- UNKNOWN on the scoped routes. The CTO half's own rule (s.1 @482b2c627e): a discovered key is a STOP and a NEW packet. rtf-9 re-declares three keys (K1 the user item as the reader reads it, K1b the partner-table binding with its OWN writer/reader census and `DeleteItem` rollback, K2 the ephemeral session), both branches per key, the exercise plan restated on the two keys, `0` writes measured; both halves re-sign against its blob; IB-rtf-3 is then re-handed against that packet. Andrew's 17:3xZ approval covers the bounded principal under both halves; the partner binding is the part the first packet mis-located, not a new act. The exposure rtf-3 named (a firm login with no book admitted by firmId on the older portal routes) is the CTO's. Chain B: `rtf-2 -> rtf-7 -> rtf-9 -> rtf-3`. fanout 3 of 3 chains, cap 8.

### R6.8 MID-ROUND ADDITION (~11:2xZ 2026-09-19) -- on rows S90 (BLOCKING) and S92 (IB-rtf-3's re-hand @dddf5ef318)

The first authenticated requests ever sent through the REAL path (the bounded principal minted by the real login, rtf-3 re-hand) were refused UNEXPECTED before the scope resolved, 12 of 12 -- an OUTAGE, not a policy refusal. Two causes: the directory role bans `platinum/` by design (IB-s-1) while the `_authz` loader reads the ownership map from there; `irpt-status`/`irpt-holdings` carry no `IRPT_DIRECTORY_BUCKET_MAP`. Every earlier "SERVED" proof ran in-process under operator credentials (rtf-2 (e), rtf-8 (e) `declared_exclusions`) -- the deployed roles were never exercised. Two cells, NOT paired (infra vs code; they share nothing but the route): `IB-rtf-10` (AE `~V`): the census of the 7 serving functions' grants/environments, the PACKET (object-scoped GetObject on each client firm's `ownership_map.json`, derived from the registry; the bucket map on every serving function), plan with `0 to destroy`, STOP at the halves on the first pass, then apply under ledger and PROVE the path under the deployed roles with the bounded principal (rtf-9 blob, new epoch). The design question (the deliberate `platinum/` ban vs the map's home) is pitched to the CTO with the issuer's recommendation; the CTO half on the packet is the ruling. `IB-rtf-11` (WK~1): `directory/entry.py` reads `q`/`limit`/`selection` from the payload-2.0 shape the integration sends, proven on a real fixture with the pre-fix entry as the mutant; no deploy (rides rtf-10's second pass). Chain D: `rtf-3 (FAIL S90) -> rtf-11 -> rtf-10 -> rtf-3 (third hand, same packet, new epoch)`. fanout 4 of 4 chains, cap 8. S91 (the None error sink) is the CTO's. Also carried, not cut: `holdings/entry.py`'s `_no_grant` wiring (IB-rt-7's decision) means the deployed holdings route serves nothing even after S90 -- rtf-8's live proof was in-process for that reason (declared exclusion); the CTO's round-6 analysis reads rt-7.

### R6.9 MID-ROUND ADDITION (~15:1xZ 2026-09-19) -- on row S98 (IB-rtf-10's fourth pass @4ce6319d03)

rtf-10's grants APPLIED exactly as signed (7 of 7 roots, 0-diff after; map allowed 18 of 21, directory 21 of 21, bucket map 7 of 7, negatives denied 27 of 27, `CodeSha256` 7 of 7) and the live proof under the deployed roles STILL read UNEXPECTED 9 of 10: S90's THIRD cause -- `_ids/ids.py` opens `raw_keys.json` beside itself at runtime and that file is in 0 of 7 deployed zips and 0 of 7 manifest entries (every zip flattens `ids.py` without it; every in-process proof passed because the repo has the file beside the module). `IB-rtf-12` (AE `~V`, the S96 shape): the premise re-measured incl. a census of every `__file__`-relative open under `_ids/`; the file DESCRIBED for the halves (shape, firm-attributability, credential NONE, writers); ONE sibling-identical `staged_from` object per function (7); the seven rebuilt under a build ledger with the per-function served delta verified as EXACTLY the added member; a NEW never-widen packet (K-CODE x 7, rollback = the prior live `CodeSha256` per function); STOP at the halves; on the re-hand apply + rtf-10's arm (f) unchanged. rtf-10's apply stands. Chain D becomes `rtf-3 -> rtf-11 -> rtf-10 -> rtf-12 -> rtf-3 (third hand)`. fanout 4 of 4 chains, cap 8. Carried for the analysis: a build-time check that a `__file__`-relative open is a staging member by construction (the binding-check class @3580608505, a third population row); the identity bar's "deployed BYTES" clause.

### R6.10 MID-ROUND ADDITION (~18:1xZ 2026-09-19) -- on rows S103/S104 (IB-rtf-12's third pass @7db8f2c67b)

rtf-12 applied the six as signed and the scope now RESOLVES on 8 of 8 counted requests (S90's three causes closed on the deployed path); two defects that lived in the prior live bytes became reachable: S103 -- directory search reads `DirectoryEntry.schema.json` from the checkout path or `IRPT_CONTRACTS_DIR`, and `irpt-directory-search` has neither (the S98/S96 class a third time, outside rtf-12's `_ids/` census); S104 -- the export receipt route's evidence-bucket read fails under `irpt-export-render-role` only (an IAM/key-prefix question; under operator credentials the read is NOT_FOUND). The rollback on rtf-12 was ruled NOT executed: the apply did what the halves signed and rolling back regresses resolve; a defect made reachable is an exposure the act uncovered. Two cells, disjoint surfaces, in parallel: `IB-rtf-13` (WK~1, the manifest + the directory root): a census of EVERY runtime file open across the seven functions against their staged members (the class-ending arm), the contract staged as a member with `IRPT_CONTRACTS_DIR` set the way holdings does, ONE rebuild under a packet (K-CODE + K-ENV), STOP at the halves, apply + prove search/resolve under the deployed role and bytes. `IB-rtf-14` (AE `~V`, the export root): the cause MEASURED (the concrete receipt key vs the policy's ARNs; the swallowed denial printed as the role; the receipt's existence), the narrowest grant as a packet (or the no-grant case rowed for the CTO), STOP at the halves, apply + prove the receipt route as the role. Chain D: `... -> rtf-12 -> rtf-13 -> rtf-3 (third hand)`; chain E: `rtf-12 -> rtf-14`. fanout 5 of 5 chains, cap 8.

### R6.4 Not decided here

Whether `firm_registry.json` becomes a builder output (rtf-1's judgment); the disclosure field's `kinds` taxonomy (rtf-2's judgment, Rule 24 record); whether `bucket_managed_by` becomes a closed enum and whether generators re-run at commit time (rtf-4's judgment -- proposals for the CTO, never gates built here); what rtd-7's port lacks after rtf-5 (rtf-5's judgment).

## R5. ROUND 5 -- THE RECUT ON THE ROUND-4 ANALYSIS (@561d6e1cc9, msg 98036) AND ANDREW'S 17:3xZ APPROVAL (@af794c77e3)

**Input:** seven judgment PASS, zero of ten FWDs REALIZED (all ten advisor-facing; the structural blocker is that no principal has ever existed to exercise them), S56 and S68 CLOSED, no PRD amendment; s.8 names six owed items; Andrew's verbatim *"Approved"* adopts the two `/open-calls` RECs (the two LGIC firm buckets NOW, creation only; a bounded test principal under both halves). The CTO's correction on W1-S20/W2-S59 changes the remedy: declare the true source in `files[]` / stage from a pinned blob, never a third copy.

### R5.1 The rectangle (5 cells, id shape `IB-rte-<n>`)

| cell | owes | assignee | serves |
|---|---|---|---|
| IB-rte-1 | s.8 item 1 / Andrew call 2: the bounded test principal DECLARED -- identity plane measured, keys, exercise plan, never-widen packet; creates nothing | WK~1 | FWD-1, 2, 5, 11 |
| IB-rte-2 | the principal CREATED under both halves, the four outcomes EXERCISED at a live session by artifact hash, DELETED as the cell's last arm | WK~1 (after rte-1 + halves) | FWD-1, 2, 5, 11 |
| IB-rte-3 | s.8 item 2 / Andrew call 1: `opal-data-inflection` + `opal-data-cottonwood` CREATED EMPTY via `name()`, in the 49 Financial bucket's shape, gate enumerations regenerated, fence proven; no objects, no cut-over | WK~3 | FWD-1, 7, 10 |
| IB-rte-4 | s.8 item 4 / W1-S20, W2-S59: the served members declared from their TRUE sources (no third copy), served zips verified member-for-member, clean-checkout builds with 0 manual steps | WK~4 | provenance of every served function |
| IB-rte-5 | s.8 item 6 / W2-S57 residual: the manifest-history census (rtd-2's Q2), FWD-7's FIVE arms on the controlled clock against the deployed code, the fresh-dispatch case named or driven | WK~2 | FWD-7 |

**Not cells of this project:** s.8 item 3 (S68's cause, the `.gitattributes eol=lf` act) is MDPF's owner's -- the CTO's own, by its word. s.8 item 5 (IRPT_FNTEND's per-firm as-of consequence) is a CARRY: sent to `2.0.0_SA_COO~F` 11:55Z (QUEUED, no live session) and now escalated to `1.0.0_SA_CTO` to land in FNTEND's PRD at L4, which is the only carrier that does not decay. IB-rtd-7 (the port) stays SUPERSEDED until rte-3's buckets, both halves and the FNTEND reader cell exist -- re-cut then, not now.

### R5.2 Edges and fanout

Chains: A `rte-1 -> rte-2`; B `rte-3`; C `rte-4`; D `rte-5`. **fanout: 4 of 4 chains, cap 8.** Handed now: rte-1, rte-3, rte-4, rte-5. rte-2 on rte-1's merge + both halves at HEAD (the COO half is this seat's on the packet; the CTO half is asked the same tick the packet drains). The DS lane holds no round-5 order (nothing Rule-13-shaped is cut); it stays seated for the port's bundle work.

### R5.3 Bounds carried

R-40, R-42, R-44, R-45; the forward-looking-criterion bar and S56's vintage pins on every face; Rule 30 on every name (builder output or a drafted registry row); NEVER-1 on the principal (both halves before creation; deletion inside the same order); creation-only on the buckets (no object, no cut-over, no legacy retirement -- Andrew's prior word stands); no third copy of a served member; read-only on every served bucket in rte-5 (a reconciliation is declared, never performed).

### R5.5 MID-ROUND ADDITION on row W1-S22 (IB-rte-1 @01ba67fe65) -- the issuer's ruling, ~22:0xZ

`IB-rte-6` -- the served path admits a projected advisor grant. Today EVERY live FIRM_ADVISOR request is refused `UNPROJECTED_GRANT`: 0 of 13 entry points pass `id_projection`, and 0 of 22,646 ownership grants join the directory even with the projection applied (custodian keys vs the crosswalk id the directory mints from). RULED: the wiring half ADJUDICABLE (L5/L6) and cut; the id-space half PITCHED to `1.0.0_SA_CTO` with REC (a) -- resolve custodian keys through `dim_identity_crosswalk` (already readable under K2) -- carried on the face as arm (b), a MEASUREMENT the ruling confirms or re-cuts. Seat WK~1 (`wk-irpt-5-1b`). Edge: `rte-6 -> rte-2` (the exercise cannot pass on a path that refuses every advisor). fanout stays 4 of 4 chains, cap 8 (rte-6 is chain A's new middle). Carried INERT: W1-S21 (advisor ids are raw ownership-map keys, never opaque-minted -- my face assumed otherwise), W1-S24 (cottonwood's termination field unpopulated). The live incident on IB-rte-3 (W3-S42/S43/S44: the new buckets' Deny fence locked out the applying identity; ledger OPEN RED) is ESCALATED `[STUCK]` to the CTO + MSTR (98062/98063) -- root `delete-bucket-policy` + two registry edits outside any worker's grant; rte-3 stays open and is re-handed after.

### R5.6 MID-ROUND ADDITION on the CTO's registry-deadlock record (@9eeb9a70a8, msg 98087) -- the issuer's ruling, ~00:1xZ 2026-09-19

`IB-rte-7` -- the LGIC firm buckets survive the registry flip. The CTO answered the rte-3 incident's registry half by RUNNING the gate: the two registry edits are mutually blocking -- `s3-lgic-firm-buckets.tf:70-73` selects on `bucket_provisioned == false` (flipping it stages a DESTROY of the 8 landed resources), and the naming gate refuses an exemption row for a bucket whose flag is false. Its remedy is five steps and step 1 is a Terraform change: a cell, RULED adjudicable at L5/L6 and cut. The issuer's measurement that re-shapes step 1: `scopes.json` @ea5edd1fe4 carries FOUR FIRM rows and two of them (`49financial`, `demo`) are `bucket_provisioned: true` with their buckets declared elsewhere IN THE SAME ROOT (`s3-49financial.tf`, `s3.tf`), so the CTO's "block keyed on PROVISIONED FIRM rows, with `moved` blocks" would plan `2 to add` -- the membership is re-keyed on a DRAFTED registry field (read with `lookup`, absent-safe) OR the unflipped flag, instance keys unchanged, no `moved` block, no state verb; proven by three plans (HEAD-identical; the flip applied locally reading `0 add / 0 destroy / <=2 policy changes`; the mutant on HEAD's Terraform reading the destroy) and never applied. Seat WK~3 (`wk-irpt-5-3b`, cold start). Grant: the one Terraform file + the channel; the registry is deliberately NOT granted (Rule 30, the CTO's, and its stated intent at 98087 -- it lands steps 2-3 on rte-7's drafted delta). Chain B becomes `rte-7 -> [CTO registry] -> [Andrew step 4, delete-bucket-policy] -> rte-3 re-hand (step 5)`; fanout stays 4 of 4 chains, cap 8. rte-3 stays open by its own FAIL; its ledger entry and sentinel stay OPEN RED. Carried to the CTO the same tick: the `demo`/`49financial` measurement, so its step-1 shape is re-cut on the fact and not on the record.

### R5.4 Not decided here

Whether one bounded identity serves FWD-11 or a second is needed (rte-1's judgment); whether `_authz/` becomes a shared package (rte-4's judgment, L4's); whether the D14 register already names the two buckets (rte-3's judgment); the fresh-dispatch design (rte-5's judgment).

## R4. ROUND 4 -- THE RECUT ON THE ROUND-3 ANALYSIS (@5c59f68d70, msg 97944)

**Input:** the CTO's round-3 analysis: nine judgment PASS, zero of ten FWDs REALIZED, no PRD amendment, round 4 unblocked; s.9 names six owed items and s.4 ADOPTS the forward-looking-criterion bar. The issuer adds ONE carried row (W1-S16, the first round-4 cut per S57) and excludes S73 (an estate-instrument defect, routed elsewhere by the CTO).

### R4.1 The rectangle (8 cells, id shape `IB-rtd-<n>`)

| cell | owes | assignee | serves |
|---|---|---|---|
| IB-rtd-1 | s.9 item 1: the 13:00Z organic fire graded on what it ACTUALLY loaded (bundle VersionId + CodeSha256 at invocation; artifacts by hash; the scheduler as invoker) | WK~2 | FWD-7 organic arm |
| IB-rtd-2 | s.9 item 4 / W2-S57: `last_manifest()` finds the COMPLETED manifest at the runner's date; the no-op branch fires on its positive case; deployed; driven after the organic fire | WK~2 (after rtd-1) | FWD-7 |
| IB-rtd-3 | s.7 / s.9 item 5 (S71): the holdings contract aboard the bundle; the two-schema diff recorded; the re-arm trigger guarded by a test | DS~X | FWD-5, FWD-7 |
| IB-rtd-4 | s.6 / s.9 item 5 (S68): the route-bindings drift measured by content, consumers + writers censused, the never-widen packet written -- declares only | WK~3 | deploy discipline |
| IB-rtd-5 | S68 resolved under both halves (CTO = MDPF's owner + COO), root converged | WK~3 (after rtd-4 + halves) | deploy discipline |
| IB-rtd-6 | s.9 item 2: the LGIC address built (`address()`, refusals -> drafted registry rows), readers/writers censused across both projects, the port planned, the write-grant packet written -- declares only | WK~4 | FWD-1, FWD-7, FWD-10 |
| IB-rtd-7 | the port under both halves + the CTO's registry rows + FNTEND's reader cell, one window, legacy retired | WK~4 (after rtd-6 + 3 gates) | FWD-1, FWD-7, FWD-10 |
| IB-rtd-8 | W1-S16: `Enforcer.covers()` firm check restored on BOTH enforcer copies (`_authz/enforce.py:351`, `holdings/enforce.py:319` @5c59f68d70), six-swap tests, deployed, proven on live routes | WK~1 | FWD-2, FWD-11 |

**Not a cell:** s.9 item 3 (the per-firm as-of consequence for IRPT_FNTEND) is a COO carrier -- a message to `2.0.0_SA_COO~F` with the fact and its consequence for the API/as-of display, sent with this issuance. S56's vintage pins and the forward-looking bar are BOUNDS on every face, graded at the drain (bare `:NNN` citations `0 of N`).

### R4.2 Edges and fanout

Chains: A `rtd-1 -> rtd-2`; B `rtd-3`; C `rtd-4 -> rtd-5`; D `rtd-6 -> rtd-7`; E `rtd-8`. **fanout: 5 of 5 chains, cap 8.** Handed now: rtd-3, rtd-4, rtd-6, rtd-8. rtd-1 is handed ~12:5xZ so the worker reads the 13:00Z fire rather than predicts it (the hand-off timing is the issuer's; the cell has no calendar wait beyond the event it grades -- the CTO ruled the organic arm correctly shaped, s.4). rtd-2 after rtd-1 merges (a deploy must not change what the organic fire loads). rtd-5 after rtd-4 + both halves (or SUPERSEDED if the packet recommends no apply). rtd-7 after rtd-6 + the CTO's registry rows + both halves + FNTEND's reader cell.

### R4.3 Bounds carried

R-40, R-42, R-44, R-45 on every face; the forward-looking-criterion bar (s.4); S56's vintage-pin bar on every judgment record; S73 excluded by name; Rule 30 on every address (builder output or a drafted registry row, never a typed path); NEVER-1 sign-off on every widening (rtd-5, rtd-7 gated on both halves); no shadow/dual-write on the port. Worker rows mint `IRPT_BCKEND-W<slot>-S<k>`; the DS mints `IRPT_BCKEND-D-S<k>`.

### R4.4 Not decided here

Which HoldingsSnapshot schema is the contract (L4's); whether the port is this project's conformance or a D14 rider (rtd-6's judgment record puts the evidence in front of the CTO); the enforcer consolidation (rtd-8's judgment record); the `eol=lf` attribute (a row).

## R3. ROUND 3 -- THE RECUT ON THE ROUND-2 ANALYSIS (v0.3, 2026-09-18 ~01:5xZ, `2.0.0_SA_COO~B`)

**Input:** the CTO's round-2 analysis @cfe3a33a9b (on the CVO's L8/L9 @c1a8cd2543, msg 97752): 11 PASS / 1 FAIL across
twelve judgment criteria, ZERO outcomes REALIZED because no round-2 cell was cut to exercise one; five items the round
carries (RT5-AC2's one-paragraph repair; W4-S25/W4-S28 re-owned under R-42 with W4-S28's disarm act as a BYTES
comparison; the ACROSS-INPUTS renderer control before FWD-3/4/8 are narrowed again; W4-S23's re-cut bar and S32's
stale batteries retired; the 53 graduated ARMED rows' intake against LIVE owners). Plus this seat's own carries from the
drain (S53/S54/S55): the wall behind IB-rt-6 is narrower than round 2 recorded, and FWD-1/FWD-7 cannot wait on
ADVI_FIRMBKTS. **The choice: RE-ISSUE against the frozen v0.2 rectangle, not a re-decomposition** -- every round-3 cell
is a repair, an exercise or a control on a round-2 surface; no PRD row is newly served and no surface is added.

### R3.1 THE RECTANGLE -- five round-3 cells

| cell | executes | serves | write surface | verb | deploys | live arm |
|---|---|---|---|---|---|---|
| `IB-rtc-1` | RT5-AC2's repair (analysis s."THE ONE FAIL") | FWD-1, FWD-5, FWD-7 | IB-rt-5's proof instance (the RT5-AC2 row gains the sibling's host reading, cited and hashed) | record | no | no |
| `IB-rtc-2` | row W2-S51 (the bundle's closure), the Rule 13 DS act | FWD-1, FWD-7, FWD-5 | `.tools/safe_deploy_core.py` CODE_TREES; the re-mint through `--mint-bundle`; on-host import proof | deploy (DS lane) | S3 mint | no |
| `IB-rtc-3` | FWD-7's exercise on the deployed dispatch for inf and cot; the 49f arm measured BLOCKED on the control | FWD-7 own, FWD-1 | none (the runner and the dispatch as deployed; artifacts land in the firm buckets) | exercise | no | no |
| `IB-rtc-4` | W4-S28 (bytes), S32 (retire), W4-S23 (vendor bar), W1-S17 (layer fetch) | FWD-4, FWD-3, FWD-8, FWD-2 | rt2_verify_deployed.py; two result headers; RT8's census bar | repair | no | no |
| `IB-rtc-5` | W4-S19's across-inputs renderer control; the real-path arm HUMAN-GATED | FWD-8, FWD-3, FWD-4 | none (the renderer as built; fixtures under the worker's home) | verify | no | no |

**Outcome coverage, run not asserted:** FWD-1 (rtc-1, rtc-2, rtc-3), FWD-2 (rtc-4), FWD-3 (rtc-4, rtc-5), FWD-4 (rtc-4, rtc-5),
FWD-5 (rtc-1, rtc-2), FWD-7 (rtc-1, rtc-2, rtc-3), FWD-8 (rtc-4, rtc-5): **7 of 10 outcomes have a round-3 cell.** FWD-9 and
FWD-10 read ADVANCED cleanly and carry nothing this round. **FWD-11 and the EXERCISED bars of FWD-1/2/5 are NOT cut**,
deliberately: each bars at a live session (a granted advisor; a restricted advisor; an Opal user across firms), which is
the test principal RT2 recorded HUMAN-GATED -- the reserved card at Andrew (restated to `0.0.0_AB_MSTR` at this
issuance). A cell that "exercises" them without the principal would be the self-wrapping harness bound 12 forbids.

**HELD, named:** the 49 Financial directory build (FWD-1/FWD-7's third firm). Its source read is behind
`DenyForeignFirmPrincipals` on `opal-data-49financial`, a CONTROL not a gap; the remedy is a DESIGN decision (run that
firm's build under a 49 Financial principal, or another shape) pitched to `1.0.0_SA_CTO` with this seat's rec at this
issuance. `IB-rtc-3` measures the refusal on this vintage and does not work around it.

### R3.2 THE EDGES AND THE FENCE

```
  edges (1):  IB-rtc-2 -> IB-rtc-3      (the closure must be aboard the bundle before any build)
  heads at spawn = 4 : IB-rtc-1 IB-rtc-2 IB-rtc-4 IB-rtc-5      leaves = 4 : IB-rtc-1 IB-rtc-3 IB-rtc-4 IB-rtc-5
  M, maximal paths = 4          components = 4          depth = 2 (IB-rtc-2 -> IB-rtc-3)         acyclic: trivially
```

| wave | cells | reason |
|---|---|---|
| 1 | `IB-rtc-1` `IB-rtc-2` `IB-rtc-4` `IB-rtc-5` | four heads, four seats, from the first hand-off |
| 2 | `IB-rtc-3` | after the DS lane's mint merges |

### R3.3 SEATING AND THE FAN-OUT

```
fanout: 4 of 4 chains, cap 8, reason: four independent heads and one dependent exercise; four worker
        subagents cold-started (the round-2 subagents died with their sessions -- slot 1: IB-rtc-1;
        slot 2: IB-rtc-3 after IB-rtc-2 merges; slot 3: IB-rtc-4; slot 4: IB-rtc-5) and the DS lane
        0.4.0_DS_ClientPlatform~X re-seated by the issuer under /mstr-spawn for the one act no worker
        may take (IB-rtc-2, Rule 13); the single cross-slot wait is IB-rtc-3 on IB-rtc-2.
```

Each hand-off is a fresh worktree from `HEAD` at hand-off time (`git worktree add -b wk-irpt_bckend-3-<n> /c/tmp/wk-irpt-3-<n> HEAD`;
the DS lane `/c/tmp/wk-irpt-3-ds`), `.tools/terraform.exe` provisioned by the issuer where a root is read.

### R3.4 BOUNDS CARRIED, AND ONE ADDED

Items 1-13 of s.8 stand verbatim on every face. Added on every round-3 face: **R-40** (`1.0.0_SA_CTO` @233f5fd5e4) --
a criterion whose subject is a run or a produced artifact records that artifact's CONTENT HASH beside its run id and is
graded against the hash; and **R-42** -- a `disarm_owner` is a SEAT SERIAL, never a cell, an order or a condition.

### R3.5 WHAT THIS RECUT DOES NOT DECIDE

- The 49 Financial build's principal (a design fork, the CTO's); the test principal (Andrew's card); the scheduled fire
  that is FWD-7's acceptance (the schedule is ENABLED and untouched; the cell's manual invoke is QA).
- The 53 graduated ARMED rows' intake: an OWNER'S word, not a cell's. The 36 owned by `2.0.0_SA_COO~B` are given in
  this seat's own rows during the round; the CTO's 7 and the CVO's 2 are theirs; the 5 owned by terminated worker slots
  carry their carve-outs and are re-placed on `2.0.0_SA_COO~B` under R-42 when this seat gives its word on each.

### R3.6 AMENDMENT 1 (2026-09-18 ~03:1xZ) -- on R-44 and R-45 @57bc083d45, the two calls this round pitched

**Why an amendment and not a round:** both rulings answer calls this seat pitched mid-round on measurements the
round's own cells produced (rows S57->S62, S58, S59 from IB-rtc-2's first pass; S53 from the drain). The rectangle's
cells are the same repairs, exercises and controls; two are RE-CUT to carry the ruled shape, and two are ADDED for the
principal R-44 rules, split at the signature so no cell waits for a seat.

| cell | change | serves | slot |
|---|---|---|---|
| `IB-rtc-2` | RE-CUT: the guard's member-level DISTRIBUTION flag, the 8-file closure with S58's two members ADMITTED, R-45's two-leg consistency control with a one-leg mutant, the re-mint, the on-host repo-shaped import proof | FWD-1, FWD-7, FWD-5 | DS `~X`, re-handed |
| `IB-rtc-3` | RE-CUT: gains the repo-shaped unpack in `refresh.py` and the directory root's apply under ledger before the inf/cot exercise | FWD-7 own, FWD-1 | `~2`, after rtc-2 |
| `IB-rtc-6` | NEW: the 49 Financial principal DECLARED (builder-named role, trust from the host role, five dimension reads and nothing else), the runner's 49F source set through the assumed role, the writer census, plans with 0 destroys, the never-widen sign-off PACKET; NO apply | FWD-1, FWD-7 | DS `~X`, after rtc-2 |
| `IB-rtc-7` | NEW: both halves at HEAD, the two applies under ledger, the NEGATIVE CONTROL (another firm's prefix DENIED, the destination write DENIED, the name off the denied prefixes), then the 49f build through the dispatch -> 3 of 3 directories | FWD-1, FWD-7 | `~1`, after rtc-3, rtc-6 and both halves |

```
  edges (amended): IB-rtc-2 -> IB-rtc-3   IB-rtc-2 -> IB-rtc-6   IB-rtc-3 -> IB-rtc-7   IB-rtc-6 -> IB-rtc-7   (+ the two sign-off halves -> IB-rtc-7)
  heads at this hand-off = 1 : IB-rtc-2      leaves = 1 : IB-rtc-7      depth = 3
  fanout (amended): 1 of 3 chains at the hand-off, cap 8, reason: the DS lane holds rtc-2 then rtc-6 in sequence (Rule 13 on both),
                    slot ~2 takes rtc-3 on rtc-2's merge, slot ~1 takes rtc-7 last; the sign-off halves are the seats' acts, not a cell's
```

**The sign-off split, stated once:** a never-widen act needs CTO+COO halves naming blast radius and rollback per key
(CLAUDE.md NEVER-1). A cell cannot wait for a signature, so `IB-rtc-6` writes the PACKET and stops, the two seats sign,
and `IB-rtc-7` applies. The COO half is `2.0.0_SA_COO~B`'s and is written from the packet, never before it.

**ADDED ~06:4xZ on the packet (IB-rtc-6's NEVER_WIDEN_SIGNOFF_PACKET, step 5) and rows S65/S68:** `IB-rtc-8` -- the `investor_reporting` bundle re-minted through the guard after IB-rtc-6's runner edit merged, so the host runs the K5 runner (a Rule 13 DS act; verified on the served object and on the host, no apply). Edge: `IB-rtc-8 -> IB-rtc-7`. `IB-rtc-7` is amended to re-read the packet's blob hash against the COO half, to apply the mdpf-pipeline root TARGETED to K3 (the one departure from s.6's `-target` never, signed in the COO half because that root also plans an unrelated `mdpf_route_bindings` change, row S68), and to wait on `IB-rtc-8`. `IB-rtc-3` was amended a second time (AMENDMENT 2, @af7d39d96f) on row W2-S55: the dispatch passes no explicit `--as-of`; upheld by `1.0.0_SA_CTO` at 97857 on the PRD's own REUSE row for `lib/trading_calendar.py`.

**ADDED ~07:5xZ on row W2-S56 (IB-rtc-3 AMENDMENT 2's real fires, drained @a4db909717 as FAIL-measured):** `IB-rtc-9` -- both gold runners call jsonschema 4.x-only API (`Draft202012Validator`, `ValidationError.json_path`) on a host running 3.2.0, so every firm's build dies at validation the moment it passes the date check; the two call sites are made version-tolerant in the DS lane (never by mutating the shared MDPF host), pinned by a test with a mutant-environment control, the bundle re-minted, the fix exercised ON THE HOST with the pre-cell tarball as the positive control of the defect. Issuer's ruling: ADJUDICABLE (L5/L6), a code defect in a DS file. Edges: `IB-rtc-9 -> IB-rtc-7`; `IB-rtc-9 -> IB-rtc-3 (AMENDMENT 3: the battery re-run only, no code)`. The eleven contracts use no 2019/2020-only keyword (0 of 11 at HEAD), so draft-7 grading on 3.2.0 is the same grading. IB-rtc-3's instance @a4db909717 is INVALID at HEAD on a CCX pin (an artifact pinned PENDING-THIS-COMMIT that an earlier commit carried); it is replaced by AMENDMENT 3's run.

**Bounds carried:** R-40 and R-42 on every face; R-45's added control (two legs, one mutant) on `IB-rtc-2`; R-44's three
conditions split across `IB-rtc-6` (1, the packet of 2) and `IB-rtc-7` (the apply of 2, and 3).

---

## 0. ROUND 1, CLOSED -- the nineteen cells retained by id

| cell | PRD | round-1 status | what round 2 does with it |
|---|---|---|---|
| `IB-s-18` | B18 | DONE | the eleven schemas move under one versioned artifact (`IB-rt-1`); `AnalysisReport` gains an optional `date_claim` (`IB-rt-10`) |
| `IB-s-17` | B17 | DONE | key constructors typed (`IB-rt-4`) |
| `IB-s-5` | B5 | DONE | the execution-role trust is CloudOps' (carried, s.9) |
| `IB-s-1` | B1 | DONE | ids through one normalizer (`IB-rt-3`); the runner minted (`IB-rt-5`) and built on the schedule (`IB-rt-6`) |
| `IB-s-2` | B2 | DONE | the grain agreed and the projection on the served path (`IB-rt-3`, `IB-rt-2`) |
| `IB-s-3` | B3 (library) | DONE | the wrapper on the six dispatched handlers (`IB-rt-2`) |
| `IB-s-4` | B4 | DONE | a real `build_fn` (`IB-rt-6`) |
| `IB-s-12` | B12 | DONE | the handler and the holdouts (`IB-rt-7`); the prefix removed (`IB-rt-3`) |
| `IB-s-8` | B8 | DONE (wrong mechanism at v0.9) | RECUT to the fixed cloud chain (`IB-rt-9`) |
| `IB-s-6` | B6 | DONE | intake controls (`IB-rt-11`); the poller stays DISABLED (bound 1) |
| `IB-s-7` | B7 | DONE | currency/unit controls (`IB-rt-11`) |
| `IB-s-9` | B9 | DONE | a real request handler on the analysis route (`IB-rt-2`); eviction/self-healing on the broker (`IB-rt-9`) |
| `IB-s-10` | B10 | DONE | glyphs and dates (`IB-rt-10`) |
| `IB-s-11` | B11 | DONE | guarded (`IB-rt-2`); ids normalized (`IB-rt-3`) |
| `IB-s-13` | B13 | DONE | guarded (`IB-rt-2`); the layer rebuilt to five contracts (`IB-rt-8`) |
| `IB-s-14` | B14 | DONE (renderer absent) | the worker renders (`IB-rt-8`) |
| `IB-s-16` | B16 | DONE | unchanged; its stand-in export arm re-measured at `IB-rtb-1` |
| `IB-s-15` | B15 | DONE (after the ruling on W2-S12) | the contract published (`IB-rt-1`); S15-AC3 reissued (`IB-rt-1`) |
| `IB-sb-3` | B3 (battery) | DONE | re-run authenticated on the real path (`IB-rtb-1`) |

---

## 1. THE RECTANGLE -- twelve round-2 cells

| cell | PRD | ruling | slug rows closed | serves | write surface | verb | tf root(s) | deploys | live arm |
|---|---|---|---|---|---|---|---|---|---|
| `IB-rt-1` | B15/B18 | 1, 8 | C-S72, C-S77 | FWD-2 own, FWD-3, FWD-11 | `docs/contracts/investor-reporting/v1/` (routes.json + 11 schemas + CONTRACT.md); the api root reading it; the paired producer-to-consumer tests; the S15-AC3 reissue | build | api (plan clean) | no | no |
| `IB-rt-2` | B3 | 2 | W1-S10, W2-S7 (served half), W2-S9 (handler half) | FWD-2 own, FWD-11 | `guard()` + `FirmBinding` on the six dispatched handlers; a real request handler on `POST /analysis`; a real export-status operation; the unguarded census with its control; the test principal from the existing authorizer's path or a HUMAN-GATED record | build+deploy | directory, performance, ycharts, narrative, export | yes | no |
| `IB-rt-3` | B2/B17 | 4 (ids, grain) | W1-S7, W1-S9, W2-S11, W2-S2 | FWD-1, FWD-2, FWD-5 | `_ids/` (one normalizer, declared raw keys per firm); the runners, handlers and the projection on it; the grain fixtures; the layer carrying `_ids` | build+deploy | performance, narrative (layer) | yes | no |
| `IB-rt-4` | B17 | 4 (keys, exceptions) | W3-S12, W2-S10 | FWD-10 own, FWD-2 | `_keys` typed at every constructor; the one error envelope on every handler error path; injected negatives | build+deploy | directory, intake, ycharts, export, ops | yes | no |
| `IB-rt-5` | B1/B12 | 3(c) | W1-S8, W2-S5 | FWD-1, FWD-5, FWD-7 (dependency) | `.tools/safe_deploy_core.py` CODE_TREES bundle `investor_reporting`; the mint through `--mint-bundle`; artifact verification | deploy (DS lane) | none | S3 mint | no |
| `IB-rt-6` | B4/B1 | 3(a) | C-S73 (refresh) | FWD-7 own, FWD-1 | a real `build_fn` (SSM dispatch of the minted runner on the mdpf daily-runner host, the accrual-trigger pattern); three production builds; four arms on the real path | build+deploy | directory | yes | no |
| `IB-rt-7` | B12 | 3(b), 7 | C-S73 (holdings), C-S75, W2-S11 (holdings) | FWD-5, FWD-2 | `holdings/` handler + root; the api integration; attribution holdouts, distinct clocks, the redistribution difference control | build+deploy | holdings (new), api | yes | no |
| `IB-rt-8` | B14/B13 | 5 | W4-S9, W4-S10, W4-S12, W4-S13, C-S76 | FWD-8, FWD-3, FWD-4 | the render controller + host dispatch on the estate's browser-host pattern; the layer at 5 of 5 contracts; stable export identity; the synthetic PDFs inventoried and reader-excluded | build+deploy | export, ycharts (host), performance, narrative (layer) | yes | no |
| `IB-rt-9` | B8 | 6 | W3-S1, W3-S2 | FWD-4 | the session broker on the packets (cutover, fencing, rotation, eviction on fixtures); the research root absorbed; the host STOPPED | build+deploy | ycharts (+ research root retired) | yes | **qualified** (arm 5 is L10's) |
| `IB-rt-10` | B10 | 6 | W3-S10, W3-S11 | FWD-4, FWD-3 | per-document font mapping; `date_claim` provenance (optional contract property) | build | none | no | no |
| `IB-rt-11` | B7 | 7 | C-S74 | FWD-9 own, FWD-4 | currency/unit validation; quarantine over relabeling; correction provenance | build | none | no | no |
| `IB-rtb-1` | B3 (battery) | 2 (proof) | W1-S10 (measurement) | FWD-2 own, FWD-11, FWD-1, FWD-5, FWD-8 | the authenticated replay across every v1 route on the real path (or HUMAN-GATED beside the post-authorizer plane) | verify | none | no | no |

**Outcome coverage, run not asserted: 10 of 10 `FWD-n` in the PRD header have >= 1 round-2 cell** (FWD-1: rt-3 rt-5 rt-6 rtb-1; FWD-2: rt-1 rt-2 rt-3 rt-4 rt-7 rtb-1; FWD-3: rt-1 rt-8 rt-10; FWD-4: rt-8 rt-9 rt-10 rt-11; FWD-5: rt-3 rt-5 rt-7 rtb-1; FWD-7: rt-5 rt-6; FWD-8: rt-8 rtb-1; FWD-9: rt-11; FWD-10: rt-4; FWD-11: rt-1 rt-2 rtb-1). **Slug coverage: 25 of 25 OPEN remediation rows are closed by a cell or carried by name in section 9** (W1-S4, W3-S3 carried to CloudOps with the CTO as gate; every other row in the table above).

**Placement axis:** `laptop`, every cell.

**Cell vocabulary (Rule 24):** as v0.1.1 -- `status` = DONE / IN-FLIGHT / OPEN / HELD / NOT-EVALUATED. Every round-2 cell reads OPEN at v0.2.

---

## 2. WHAT L5 ADDS PER CELL

Inlined on each face under "What L5 adds (decomposition v0.2 s.2, s.6, s.9)"; the faces are the carrier. Two additions bind every cell and are s.8 bounds 12 and 13: **no self-wrapping harness as evidence** (an arm's subject is the real route file, the real dispatcher, the deployed function, the served object) and **typed, issued identifiers at every boundary** (a display name, an e-mail, a raw upstream key or a request-controlled firm token is refused and never echoed).

---

## 3. THE CHAIN READ -- computed from the edge set, not chosen

```
  edges (9, keyed to OBSERVED completion of the source cell):
    IB-rt-3 -> IB-rt-6    IB-rt-3 -> IB-rt-7    IB-rt-5 -> IB-rt-6
    IB-rt-1 -> IB-rtb-1   IB-rt-2 -> IB-rtb-1   IB-rt-4 -> IB-rtb-1
    IB-rt-6 -> IB-rtb-1   IB-rt-7 -> IB-rtb-1   IB-rt-8 -> IB-rtb-1

  heads releasable at spawn (no incoming edge) = 9 :  IB-rt-1 IB-rt-2 IB-rt-3 IB-rt-4 IB-rt-5 IB-rt-8 IB-rt-9 IB-rt-10 IB-rt-11
  leaves (no outgoing edge)                     = 4 :  IB-rt-9 IB-rt-10 IB-rt-11 IB-rtb-1
  M, maximal paths through the edges            = 10
  edge-connected components                     = 4 (the battery pole; rt-9; rt-10; rt-11)
  longest dependency depth (cells)              = 3 :  IB-rt-3 -> IB-rt-6 -> IB-rtb-1  (also IB-rt-5 -> IB-rt-6 -> IB-rtb-1)
  acyclic: checked (the chain script refuses a cycle)
```

**THE BINDING FACTS.** (a) Round 2 is WIDE and SHALLOW where round 1 was narrow and deep: nine heads, depth three. The useful width is therefore the slot count, not the pole count: five seats work from the first hand-off. (b) The one shared dependency is `IB-rt-3` (the normalizer): `IB-rt-6` and `IB-rt-7` consume it and it is finished BEFORE either is handed. (c) `IB-rt-5` is a DS-lane act on a shared tool; the refresh build waits on it by an edge, so no worker is asked to do a DS act.

---

## 4. THE ROUND FENCE -- the dependency waves inside ONE issuance

| wave | cells | the fence's reason |
|---|---|---|
| 1 | `IB-rt-1` `IB-rt-3` `IB-rt-4` `IB-rt-5` `IB-rt-8` | the seam, the ids, the keys, the mint, the renderer: five heads, five seats, the CTO's "seam first" |
| 2 | `IB-rt-2` `IB-rt-7` `IB-rt-9` | the guards (after the seam's v1 file), the holdings handler (after the normalizer), the broker (after the keys) |
| 3 | `IB-rt-6` `IB-rt-10` | the refresh build (after the mint and the normalizer), glyphs and dates |
| 4 | `IB-rt-11` | intake controls |
| 5 | `IB-rtb-1` | the authenticated replay across everything |

The fence is a plan, not a commitment; a wave is the dependency order inside a queue and the order in which the COO hands cells across queues at the drain.

---

## 5. SEATING AND THE FAN-OUT L6 WILL CARRY

**Eleven cells are worker cells** (`0.9.0_WK_IRPT_BCKEND~n`, the four round-1 subagents CONTINUED with their context intact -- the spine's "no respawn, no cold start"; Opus at high effort, the model passed explicitly at every resume until the definition's own value is trusted again), **and one cell is a DS-lane cell** (`0.4.0_DS_ClientPlatform~X`, seated by the issuer with `/mstr-spawn` for this order alone; the rule-13 act the CTO's ruling 3(c) opened). Under RULING 1 a seat's write surface is exactly the `<paths>` its order names.

```
fanout: 5 of 10 chains, cap 8, reason: the round is nine heads wide and three deep, so every seat
        works from the first hand-off; four are the round-1 worker subagents resumed on the surfaces
        they already own (slot 1 ids-holdings-replay: IB-rt-3, IB-rt-7, IB-rtb-1; slot 2 seam-guards-
        refresh: IB-rt-1, IB-rt-2, IB-rt-6; slot 3 keys-broker-extract-intake: IB-rt-4, IB-rt-9,
        IB-rt-10, IB-rt-11; slot 4 export: IB-rt-8) and the fifth is the DS lane for the one act no
        worker may take (IB-rt-5); the cross-slot waits are IB-rt-6 on IB-rt-3 and IB-rt-5, IB-rt-7 on
        IB-rt-3, and IB-rtb-1 on rt-1, rt-2, rt-4, rt-6, rt-7, rt-8 -- hand-offs the COO sequences at
        the drain.
```

| seat | queue (dependency order) | cross-slot waits the COO sequences at the drain |
|---|---|---|
| `~1` | `IB-rt-3` -> `IB-rt-7` -> `IB-rtb-1` | `IB-rtb-1` after `IB-rt-1`, `IB-rt-2`, `IB-rt-4`, `IB-rt-6`, `IB-rt-8` merge |
| `~2` | `IB-rt-1` -> `IB-rt-2` -> `IB-rt-6` | `IB-rt-6` after `IB-rt-3` and `IB-rt-5` merge |
| `~3` | `IB-rt-4` -> `IB-rt-9` -> `IB-rt-10` -> `IB-rt-11` | none |
| `~4` | `IB-rt-8` | none |
| DS `~X` | `IB-rt-5` | none; its merge releases `IB-rt-6` |

Each hand-off is a fresh worktree from `HEAD` at hand-off time (`git worktree add -b wk-irpt_bckend-2-<n> /c/tmp/wk-irpt-2-<n> HEAD`; the DS lane `/c/tmp/wk-irpt-2-ds`), `.tools/terraform.exe` provisioned by the issuer, the halt-gate serial file written by the worker before any apply, the OPEN sentinel committed before any act (round-1 rule W3-S4).

---

## 6. TERRAFORM ROOTS, STATE AND THE DEPLOY DISCIPLINE

The ten round-1 roots stand (s.6 of v0.1.1; state keys unchanged; every provider cache was purged estate-wide on 2026-09-11 so every plan begins with `init` on the vendored binary). Round 2 adds ONE root and retires one:

| root | state key | cells | change |
|---|---|---|---|
| `holdings/` (new) | `investor-reporting/holdings/tfstate` | `IB-rt-7` | the holdings handler Lambda + role |
| `ycharts-research-20260911/` (retired) | its own | `IB-rt-9` | absorbed into `ycharts/` by `state mv` under the ledger, then removed from the tree |
| `api/` | unchanged | `IB-rt-1`, `IB-rt-7` | reads the v1 contract path; gains the holdings integration |
| `directory/`, `performance/`, `narrative/`, `export/`, `intake/`, `ops/`, `ycharts/` | unchanged | as the rectangle says | code/hash changes and the layer version only; plans show nothing else |
| `portal-auth/` | not this project's | none | the WAF read artefact is CloudOps' (CTO item 4); no cell touches it |

Every apply is `.tools/safe-apply.sh` under a change-management entry whose OPEN sentinel is committed BEFORE the act and whose close is committed BEFORE the grading reads; served bytes verified as `CodeSha256`; `-target` never; two worktrees never apply one state (the seating above keeps each root in one slot; `api` is shared by `IB-rt-1` and `IB-rt-7` in dependency order across slots, handed only after the earlier merges).

---

## 7. THE BATTERY -- run at L5, with each instrument's blindness stated

| instrument | disposition | result | what it does NOT cover |
|---|---|---|---|
| the chain read | RUN | 9 edges, 9 heads, 4 leaves, M=10, 4 components, depth 3, acyclic (section 3) | trusts this document's edges; a missing edge shows as false width |
| outcome + slug coverage | RUN | 10 of 10 `FWD-n` served; 25 of 25 OPEN slug rows closed by a cell or carried by name (section 1, section 9) | a served outcome is not a REALIZED one; two rows are carried to another lane, not closed |
| ruling coverage | RUN | 8 of 8 rulings map to >= 1 cell (1: rt-1; 2: rt-2, rtb-1; 3: rt-5, rt-6, rt-7; 4: rt-3, rt-4; 5: rt-8; 6: rt-9, rt-10; 7: rt-7, rt-11; 8: rt-1 + section 9) | the mapping is this document's reading of the rulings; the CTO's L10 read is the check |
| surface re-pin | RUN at `67ef99e5c2` | every round-1 surface the faces build on PRESENT (the ten roots, `_authz`, `_scope`, `_keys`, the runners, the packets, the layer); the new homes ABSENT as they must be (`_ids/`, `holdings/`, `docs/contracts/investor-reporting/`) | existence, not content |
| the gold-execution pattern | RUN (comp-find) | `infra/aws/lambda/mdpf-pipeline/mdpf-accrual-trigger/lambda_function.py` runs a minted bundle on the mdpf daily-runner host by SSM (`tar -xzf` into `/opt/mdpf/scripts/gold/`, `python3 ...`) -- the pattern `IB-rt-6` reuses | whether that host carries the runner's dependencies is measured by `IB-rt-6` arm (d), not here |
| the browser-host pattern | RUN (read at the round-1 drains) | the BD auto-login host and the YCharts host carry a browser runtime; the export renderer reuses that STYLE (`IB-rt-8`) with zero egress | whether either host's runtime renders the counterpart's package is `IB-rt-8` arm (a); a HUMAN-GATED reading is admitted |
| `comp-schedule`, `comp-iam` | INHERITED from the round-1 cut; re-run per cell where a schedule target or a role changes (rt-6, rt-2, rt-3, rt-4, rt-7, rt-8, rt-9) and recorded in each instance | a ledger of gates; DESIRED plane only |
| lane read | RUN | the worker serials hold no open order on any other pipeline project (round 1 is 19 of 19 complete); the DS lane `~X` is fresh; the round-1 model flip is repaired at HEAD (`worker.md` `model: opus`, 0d57ceb2f9) and the model is still passed explicitly at every resume | the seating lint at commit is the enforcement |

---

## 8. BOUNDS THAT BIND EVERY ORDER, inlined at L6

Items 1-11 of v0.1.1 s.8 stand verbatim on every face (no live vendor call, the mailbox read and a YCharts login or capture included; no monitor; cross-firm both shapes; deploys under ledger with the OPEN sentinel committed before the act; Andrew's fixed constraints plus the v0.9 fixed YCharts mechanism; no credential; no served output touched; the spec frozen with the row as the only off-spec act; every invocation terminates; the commit gate; scratch). Two are added:

12. **NO SELF-WRAPPING HARNESS AS EVIDENCE** (rows W1-S10, S24): an arm's subject is the real route file, the real dispatcher, the deployed function, the served object; a census prints its denominator and a `0 of 0` reads VACUOUS; every manifest of hashes is re-derived by its battery every run (row W3-S9).
13. **TYPED, ISSUED IDENTIFIERS AT EVERY BOUNDARY** (rows W2-S9/S11, W1-S7, W3-S12): a display name, an e-mail, a raw upstream key or a request-controlled firm token is refused at every function boundary and never echoed.

And the round-1 qualification stands: a live arm is an express qualification on the face, read by the CTO at L10 on Andrew's per-use word, never a mechanical criterion (v0.1.1 s.8 item 1). One cell carries one: `IB-rt-9` (arm 5 of v0.9, Comparison and Multi-Comparison live).

---

## 9. ROUND-2 FINDINGS AND CARRIES, for the CTO's L10 read

1. **Two OPEN slug rows are not this project's to close and are carried by name with the CTO as gate:** `W1-S4` (the IRPT roots' provider-lock policy -- `0.7.0_AE_CloudOps`; the lock files are tracked at HEAD and every root plans clean on 5.100.0, so the row is a policy question, not a drift) and `W3-S3` (the per-firm execution roles' trust -- `0.7.0_AE_CloudOps`; `IB-rt-2`'s guards do not depend on assuming them).
2. **The rule-13 act is seated, not absorbed:** `IB-rt-5` is issued to `0.4.0_DS_ClientPlatform~X`, a DS lane this issuer spawns for that order under `/mstr-spawn` (COO function, Andrew-direct 2026-08-28); the face is under this project's `task-orders/` with a pointer in the lane's own `task_orders/` home so the receiver rule (`AGENTS.md`) is met.
3. **Deletion of the four synthetic PDFs is Andrew's word** and stays carried (`IB-rt-8` proves reader exclusion and inventories; it moves nothing).
4. **The optional `date_claim` property on `AnalysisReport`** is the one contract edit of the round (`IB-rt-10`), additive under `additionalProperties:false`; it is the L5 proposal the slug asked for and the CTO reads it at L10.
5. **The unguarded three were protected by accident** (a consent gate, an identity-less request shape, an absent operation); `IB-rt-2` replaces accident with the wrapper and the judgment names which accidental protection changed.
6. **The counterpart's round-2 seam cell regenerates against `IB-rt-1`'s artifact**; the two lanes share FILES (`docs/contracts/investor-reporting/v1/`), never messages; a consumer fixture that disagrees with II.3 fails the paired test on this side and is a row, never a schema change.

---

## 10. CROSS-PROJECT SEAMS (no cell is jointly owned)

| seam | this project | the counterpart | graded inside |
|---|---|---|---|
| the contract artifact `docs/contracts/investor-reporting/v1/` | `IB-rt-1` publishes; the paired producer-to-consumer tests | its round-2 seam cell regenerates the typed client against it | FWD-1, 2, 3, 5, 11 |
| `RenderPackage` (versioned, `runtime: 'browser'`) | `IB-rt-8` executes the counterpart's real package | its F9 produces it (the FNTEND slug's W2-S4) | FWD-8, FWD-3, FWD-4 |
| the browser request half of `AnalysisRequest` (v0.10) | `IB-rt-2`'s analysis request handler consumes it and builds the `resolved` half server-side | its F5 sends it | FWD-4 |
| `date_claim` on `AnalysisReport` | `IB-rt-10` adds the optional property | its consumer reads it | FWD-4, FWD-3 |
| `StatusEnvelope` reason codes (closed enum) | `IB-rt-4`'s error envelope | its status panel | FWD-6 (its), FWD-10 |

---

## 11. WHAT THIS DECOMPOSITION DOES NOT DECIDE

- **The `<paths>` block of any order** -- L6's, per order; under RULING 1 it IS the grant.
- **Which existing host renders** (`IB-rt-8`) and **which host runs the minted runner** (`IB-rt-6`): the cells read the estate's patterns and choose inside the bounds; a host that needs egress is a HUMAN-GATED arm.
- **Whether a test principal exists** (`IB-rt-2`): the first read is the measurement; HUMAN-GATED is an admitted reading.
- **The live YCharts arms** (arm 5 of v0.9): the CTO's qualified read on Andrew's per-use word.
- **The DS lane's own tooling choices inside the guard** (`IB-rt-5`): the guard's shape is copied, its tests are the control.
