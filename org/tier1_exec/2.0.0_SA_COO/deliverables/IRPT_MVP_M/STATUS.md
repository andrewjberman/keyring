# IRPT Holdings -- status

Seat `2.0.0_SA_COO~M` (CLAUDE, successor to the Codex seat since 2026-09-23 ~22:47Z). Contract
`org/tier1_exec/1.0.0_SA_CTO/deliverables/IRPT_MVP_COMPLETION_20260922/CONTRACT.md` v1.4. Reviewer `3.0.0_SA_CVO~M` (not live).
As of 2026-09-24T07:1xZ. ALL THREE FIRMS SERVE LABELLED HOLDINGS (CTO GO 100401 executed): 49F 3d59c80b (manifest EvNOT_ocng -> 9Vtkh61A,
etag ea06a1a0, 06:58:45Z; 176 creates + 1 IfMatch; 7c0e7ce3 retained), INF d03e91a4 (J_FeUeEA -> .vBFsThYv, etag d866755b, 07:04:38Z; 35 creates +
1 IfMatch; 1ebc7696 retained), COT dec293d6 (06:20Z). Each built with its retained capture (49F tax snapshot sha 032c68db.., INF Eclipse map
789dd95d.., 860 rows) and identical to the prior served tree to the node plus display. Served labels: 49F 151,582 of 151,697; INF 33,327 of
33,328; COT 16,740 of 16,749. Receipts HOLDINGS_49F/INF_LABELLED_PUBLICATION_RECEIPT_20260924.json; overlays HOLDINGS_49F/INF/COT_MODEL_SNAPSHOT
regenerated on the served revisions (49F 7 models / 7,475 accounts / 180 assets all labelled; INF 18 / 624 / 2,166 all labelled; COT 7 / 521 / 119).
NEXT: the CUSTODY_UNITS fill for 49F/INF is built @d96513bc40 (tests per firm) -- its republish is its own GO; Andrew's page retest is the
exercised arm; /verify of the goal runs now.
Earlier state follows.
As of 2026-09-24T07:0xZ. CORRECTION: the 06:2xZ 49F/INF candidates (aa6efd45 / 4a50ac5f) were built WITHOUT the two env-var retained
captures the served builds consumed (IRPT_49F_TAX_MEMBERSHIP_SNAPSHOT, IRPT_INF_ECLIPSE_MEMBERSHIP_SNAPSHOT) -- regressions, not code
vintage. I halted the 49F publish before its index write (served manifests unchanged; 158 unreferenced aa6efd45 objects stay); the CTO
withdrew GO 100370 (100390). REBUILT WITH BOTH CAPTURES (sha verified against the served provenance): 49F 3d59c80b and INF d03e91a4 are the
served trees to the node (0 ids added/removed) plus display (+ the ticker fact on 5,748 49F custody rows); labelled 151,582 of 151,697
and 33,327 of 33,328; CAS checks PASS with zero writes. GO re-requested per firm. Census: HOLDINGS_49F_INF_LABELLED_CANDIDATE_CENSUS_20260924.json.
Earlier state follows.
As of 2026-09-24T06:5xZ. 49F/INF LABELLED CANDIDATES PREPARED AND GO REQUESTED (CTO 100368; census
HOLDINGS_49F_INF_LABELLED_CANDIDATE_CENSUS_20260924.json; producer change @eaf4c43b59: ACCOUNT labels from the directory, CASH labels,
Schwab custody ticker fact): 49F aa6efd45 labelled 151,582 of 151,697 (27 accounts absent from the directory, 88 CUSIP-only rows),
INF 4a50ac5f labelled 33,288 of 33,293; same eight receipts as the served revisions; CAS checks PASS with zero writes over the live
manifests (49F etag f3ea427b / version EvNOT_ocng, INF etag 4283ce90 / version J_FeUeEA); one act per GO, 49F then INF. Portal DEV is
7c542fd2 (MSTR 100365: candidate 2 = 7975c3bb + labels pin e5dd8487 + hop 11 + 'Performance' label), so DSGN_IRPTV1 L6 condition (b) is met.
Earlier state follows.
As of 2026-09-24T06:3xZ. LABELLED COT RE-CUT dec293d6 IS SERVED (CTO GO 100337 executed 06:20:00-06:20:12Z; receipt
COT_LABELLED_PUBLICATION_RECEIPT_20260924.json): 27 immutable creates + ONE IfMatch write on the served manifest
s3://opal-data-cottonwood/irpt/cottonwood/platinum/holdings/current/manifest.json (version .VLcr1BCE -> mSFR0vat, etag d81c9213),
row 2026-09-22 dec293d6 <- 2d067b4d (retained; rollback = re-point under a fresh IfMatch). Served now: display on 16,740 of 16,749
nodes (model names, the Client residual sleeve, security symbol + description; 9 directory-absent ACCOUNT nodes omit it),
CUSTODY_UNITS on 13,656 of 14,426 securities, zero price facts; Anna's selection reads 75 nodes on the new revision (library under
user; Andrew's retest is the exercised arm). DSGN_IRPTV1 L6 condition (a) lands with this act (COO~D re-measures). NEXT: 49F/INF
labelled candidates are prepared (49F c34c28fe, INF 4247a63a; same receipts as the served revisions) but NOT GO-ready: ACCOUNT
nodes carry no directory label outside build_cot (49F 0 of 7,522, INF 0 of 876) and CUSTODY_UNITS is COT-only -- wiring the
directory label into build_snapshot for 49F/INF, then a CAS publisher variant, then ONE GO per firm.
Earlier state follows.
As of 2026-09-24T06:2xZ. P's schema pin b3e3bcb044 MERGED here @550789f51d (display + CUSTODY_UNITS admitted in both copies; one
conflict in P's _scope lane resolved to P's side). X10 registry row ACTIVE @7262571e4c (batch 27 M act; enforcement_ref 0a101a6668..; 63 tests).
LABELLED COT RE-CUT CANDIDATE dec293d6 PREPARED over the 841 accepted accounts (COT_LABELLED_CANDIDATE_CENSUS_20260924.json):
16,740 of 16,749 nodes labelled (9 ACCOUNT nodes absent from the directory, display omitted), CUSTODY_UNITS on 13,656 of 14,426
securities (every OBSERVED one; the 770 ASSIGNED components without are unheld), reconcile exact, both schema copies validate,
publisher check PASS with zero writes. GO REQUESTED from the CTO: CAS over COT index version .VLcr1BCE (etag ffa30e5b), row 2026-09-22
replaced, prior 2d067b4d retained; P's step-3 repackage is APPLIED (CodeSha kZygK57y.. 06:00:10Z, 100327) and DEV carries 7975c3bb, so
the republish executes on the GO. Portal UI stopped at labels pin e5dd8487 (CALL 1(c)); L2-by-model rows and the Client sleeve are DSGN_IRPTV1 C3/C4.
Earlier state follows.
As of 2026-09-24T03:5xZ. ANDREW'S ANNA SCREEN RENDERS (CTO 100044, fixes EXERCISED). Andrew-direct ~03:1xZ (CTO 100063) corrected the
COT tree: the Rebalancer Strategy is a WRAPPER and the MODELS are its constituents; CTO ruling IRPT-COT-HOLDINGS-TREE-20260924 (100094)
fixed the shape; build_cot is RE-CUT on this branch as a CANDIDATE (no publication; census COT_TREE_CANDIDATE_CENSUS_20260924.json with
the CTO). The 46-model overlay artifact is WITHDRAWN as an overlay of models until the re-cut publishes. UI: coverage counter
b0e2d9ad (CTO-accepted) + drill affordance / deeper first screen / strategy label 67158601 on codex/irpt-m-ui for CTO review.
Earlier state follows.
As of 2026-09-24T02:12Z. FENCE APPLIED 02:04:06Z (P 99963, ledger irpt-holdings-fence-20260924 CLOSED @7220e4a4f3), CTO re-simulation 6 of 6
allowed (99969); this seat's own re-simulation on the 49F and INF indexes and a part each: allowed 4 of 4, matched the role's identity
policy, role named once in each bucket policy (HOLDINGS_ROLE_ARM_RESIM_20260924.json). The function can now read all three publications;
Andrew's Anna retest at localhost:5174 is the EXERCISED arm and MSTR is asking him now. GO A and GO B EXECUTED (CTO 99931). CTO dda3b7ab42 (batch 12): Andrew's Anna NOT_READY ROOT CAUSE is the firm-bucket fence
(DenyForeignFirmPrincipals on all three opal-data-<firm> buckets denies irpt-holdings-role; this seat's two measurements ran as the
exempted user and the identity-only simulate, so neither could see it). Remedy: CRO exemption rows, P shared-infra plan (0/3/0),
CTO sign, P apply, Andrew retest. GO requests A (49F) and B (INF) are under the CTO's independent verification.

Standing directive (Andrew-direct ~22:4xZ, record `org/tier1_exec/2.0.0_SA_COO/deliverables/ANDREW_DIRECT_20260923_224xZ_COO_M_GOAL_HOLDINGS_SNAPSHOT_MODEL_OVERLAY_LOOP_20M.md` @6890584d29; Step 1b-F row landed by the CTO @d78fdb2f1c):
Holdings end to end for every 49 Financial and Inflection client, meshed across SmartX/Schwab and Eclipse/Orion, with a
SNAPSHOT model overlay (which clients own which models, what assets are in those models; NO model time series), and a
structurally correct Cottonwood pipeline bounded by Black Diamond's data window. `/loop 20m` armed at this seat (cron fcf016cf).

## Pins

| What | Value |
|---|---|
| Working branch / worktree | `codex/irpt-m-completion` at `../ajb_irpt_m` |
| Workspace candidate pin | this commit (INF meshed builder; its two pre-LGIC silver prefixes are read through the producers' own key builders because the naming gate refuses them as new hand-kept carriers); 21f696e19a (49F meshed builder + COT reader matrix); 5f3651db41 (COT receipt) |
| Portal integration pin | P integration c70855f30d at `../portal-local-live-20260923` (the 5174 screen); CTO 99866: P's NOT_READY render fix c1ac41ec merges there next |
| Deployed artifact pin | irpt-holdings Lambda: repaired loader 3e913e9ce9 APPLIED by P 23:00:52Z (CodeSha l/GQrFcE...), CTO-verified d78fdb2f1c |
| Accepted COT publication | SUPERSEDED by 2d067b4d (row above) at 03:56:55Z; ac3adb97f5e76a5f044d4b0d12ffda3bebccd235915aed661315e98432729d5a (membership in the tree, retained), index version XbWnSWxMFRs9jNOUtj6ZOELvpemDQP73 at 00:37:11Z under CTO GO 99856; prior 93f930c265 / grwnbLkeu retained. The 20-vs-18 create-count deviation was disclosed and ACCEPTED by the CTO (99866): the blast radius (new revision's key prefix + one index row) is what was written; future GO requests print the publisher's measured write plan |
| Portal candidate pin (M UI) | `codex/irpt-m-ui` at `../ajb_irpt_m_portal`: Holdings tab now renders a sleeve's taxonomy path, a model node's name and the producer's facts (withheld drill, membership conflict) when the adapter carries them; inert until P lands HOLDINGS_ADAPTER_PATCH_20260924.md (shared client surface); typecheck + eslint clean, `__tests__/m-overlay/slices-extras.mjs` 10 assertions |
| 49F candidate (UNPUBLISHED) | revision a860115ecaf5336ac5db4491d76cf5b60780f8a9c257c579defaf62351ba6a1f, business date 2026-09-22 / overlay 2026-09-23 (CTO findings 3c8392cf2f closed) |
| INF candidate (UNPUBLISHED, GO requested) | revision dc5d5e237d3ea304c470d74393b1e7da4fefd9e0e06fde6ddd3c8d3131eb2d31, business date 2026-09-22 (Orion key 2026-09-23 holds the prior close) / overlay 2026-09-23; supersedes 21279569 by consuming the CRO's retained Eclipse membership capture (138fad2935, sha256 789dd95d...) for the 74 sleeve accounts the export never exposed: 624 model leaves (553 whole incl. 35 from the capture, 71 split), 252 Client (16 no membership anywhere, 176 no model, 60 non-tying split); measured write plan 34 immutable creates + index CAS |
| 49F PUBLISHED (GO A, IRPT-49F-HOLDINGS-PUBLICATION-GO-20260924) | revision 7c0e7ce3bef21ccf63541d766a94fa9a71668e7457955eedcf850ec2b18f5cc0 for 2026-09-22, index opal-data-49financial/irpt/49financial/platinum/holdings/current/manifest.json version EvNOT_ocng2dG0yqDqpXUDFBCPO1ovwK created with IfNoneMatch * at 01:46:02Z; 159 immutable creates (gold parquet, header, 156 parts, manifest) + 1 index = 160 writes, every version read back; reader matrix under the USER: 3 selections x {None, 2026-09-22} READ_OK, 2026-09-23 refused, unknown account refused; role arm: irpt-holdings-role explicitDeny (ResourcePolicy) on the index -> proof class LIBRARY_UNDER_USER until the fence rows apply. Receipt HOLDINGS_49F_PUBLICATION_RECEIPT_20260924.json |
| INF PUBLISHED (GO B, IRPT-INF-HOLDINGS-PUBLICATION-GO-20260924) | revision 1ebc7696d6e52be01c3fc431b222c80d9baf3f967f0681cf3879115e5ad476fa for 2026-09-22, index opal-data-inflection/irpt/inflection/platinum/holdings/current/manifest.json version J_FeUeEAd0jRBCN0lgMoixLY_m3o9QHM created with IfNoneMatch * at 01:48:29Z; 34 immutable creates (31 parts) + 1 index = 35 writes, every version read back; same matrix shape READ_OK / refused; role arm explicitDeny -> LIBRARY_UNDER_USER. Receipt HOLDINGS_INF_PUBLICATION_RECEIPT_20260924.json |
| PREPARED for GO (exact bytes + receipts, ATTESTED) -- now PUBLISHED as above | 49F revision 7c0e7ce3bef21ccf63541d766a94fa9a71668e7457955eedcf850ec2b18f5cc0: 7,522 accounts, 151,697 nodes, reconcile 1,835,875,624.28, 156 parts = 159 immutable creates + index create (IfNoneMatch *, no index exists), 8 source receipts; INF revision 1ebc7696d6e52be01c3fc431b222c80d9baf3f967f0681cf3879115e5ad476fa: 876 accounts, 33,328 nodes, reconcile 209,358,359.48, 31 parts = 34 creates + index create, 8 receipts. Bytes and receipts under .runtime/holdings-journey-20260923/prepared_49f and prepared_inf; a rebuild changes the revision (clocks.as_of_timestamp), so the GO names THESE bytes and the publisher writes them |
| Currency | Andrew attested 49F and INF USD (CTO 99877, ANDREW_49F_INF_USD_20260924.md); P writes the two records into CurrencyAuthorities.json; both candidates publish under exact-write GOs on those records |
| COT membership candidate | PUBLISHED as above (receipt COT_MEMBERSHIP_PUBLICATION_RECEIPT_20260923.json); reader matrix on the live publication: 0698 / d486 / combined READ_OK with 1 / 1 / 2 model leaves, 2026-09-23 refused, excluded account refused |
| COT RE-CUT PUBLISHED (CTO GO 100147) | revision 2d067b4d7097f0762e69ac635f75db77591a9a2774ce8138914e134185caa859 for 2026-09-22, index version .VLcr1BCEMXLODKeFWA00C31rlgnUBAr created by CAS (IfMatch ab460faa over XbWnSWxM) at 03:56:55Z; 22 immutable creates + 1 index = 23 writes, every version read back; prior ac3adb97 objects + index version retained and re-read; reader matrix LIBRARY-UNDER-USER READ_OK 0698 41 / d486 75 / combined 116 nodes with wrappers + leaves, 2026-09-23 refused, excluded account refused. Receipt COT_RECUT_PUBLICATION_RECEIPT_20260924.json. Andrew's retest = the function's own read |
| COT RE-CUT PREPARED for GO (CTO 100123 accepted the shape) | revision 2d067b4d7097f0762e69ac635f75db77591a9a2774ce8138914e134185caa859 for 2026-09-22 over the accepted 841-account census: 16,749 nodes (ACCOUNT 841 / MODEL_WRAPPER 462 / MODEL_LEAF 521 over 7 constituent models / SLEEVE 499 / SECURITY 14,426), reconcile 548,412,662.59 exact, 0 of 841 account pies off, 46 of 46 assigned strategies carry a definition, 0 UNRESOLVED, 2,145 shared securities under >1 constituent, 672 uncovered observed positions (20,642,062.66 USD) carried as Client facts; write plan 19 parts = 22 immutable creates + ONE index CAS (IfMatch etag ab460faa / version XbWnSWxM, row 2026-09-22 ac3adb97 -> 2d067b4d, prior retained); 8 versioned receipts incl. fact_model_definition; bytes under .runtime/holdings-journey-20260923/prepared_cot; publisher publish_cot_live.py <go> check|publish |
| COT TREE RE-CUT (CTO 100094) | this commit: ACCOUNT > MODEL_WRAPPER (strategy, ASSIGNED whole account) > MODEL_LEAF per Opal/SMA blend child (ASSIGNED = value x absolute_allocation; Models > Primary / Models > Custom / SMA by the MDPF registry rule; is_opal by name) + SLEEVE Client (the plug, ASSIGNED) > SECURITY (fact_model_definition components at value x weight; observed custody position as a fact). Anna: 0698 41 nodes = OCG 60.7% + OUSTI 20% (Primary) + OFI 16% (Custom) + Client 3.3% (PHYS); d486 75 nodes adds DIVZ SMA 7%; combined 116; reconcile exact, 0 partitions off. CANDIDATE; the CTO GOes the publication (CAS create over ac3adb97) |
| Registry act (CTO dda3b7ab42 item 3) | ORIGINAL_HOLDINGS family row committed 58ee5b36dd on this branch: tier state, table original_holdings (tables must be distinct; prospect_inputs is ORIGINAL_CSV's), extension csv (the validator admits only csv/json/pdf; xlsx would refuse the whole registry), 30 / 2555; policy_sha256 of irpt-x10-v1 moves cb9c4e6e -> 7a7ed8f6 (before value = P's X10 matrix pin); exact-family census test updated in the same commit, 63 passed; sent to CTO + Y for acceptance |
| Push state | LOCAL; origin/CLOUD b475b96309 (ls-remote read 23:27Z by CTO); shared pushes are 0.0.0_AB_MSTR's |

## Live thread

State: COT LIVE AT HOP 3 of 4 (source -> accepted publication -> deployed reader library, `COT_DEPLOYED_READER_MATRIX_20260923.json`),
and since 02:04Z the function's ROLE is allowed on all three buckets (fence applied; CTO 99969 + this seat's re-simulation), so hop 3 is
no longer user-only. Hop 4 (Andrew's signed-in screen) is the only unexercised arm; expected render for the combined Anna selection:
93 nodes, custody USD 46,009,147.02 at 2026-09-22 (CTO 99969).
Hop 4, the signed-in Anna selection + Holdings screen + reload at localhost:5174, is Andrew's act (asked at the M terminal;
last real attempt 22:17Z FAILED NOT_READY against the pre-repair loader and the single-account publication, both replaced).
49F and INF are now at hop 2 (accepted publications live in their firm buckets); hop 3 for all three firms is the
library-under-user proof only until the fence exemption rows apply to irpt-holdings-role.

## Acceptance IDs

| ID | State | Evidence |
|---|---|---|
| M1 census incl. non-model/zero/closed/missing | COT live; 49F CANDIDATE (7,522 accounts); INF CANDIDATE (876 accounts; 82 accounts / 1,709 positions outside the census reported) | HOLDINGS_*_MESHED_CANDIDATE_20260923.json |
| M2 unique positions, supported grain | COT live (13,793); 49F candidate (Schwab rows, SmartX assets TARGET); INF candidate (30,881 native Orion rows) | same |
| M3 Models/SMAs/Client(plug) reconciliation | 49F: 5,908 / 7 / 1,607; INF: 518 whole + 71 split / 0 / 287; both reconcile to the cent, difference control discriminates | same |
| M4 accepted Gold -> Platinum, atomic index | COT, 49F and INF LIVE (three indexes, each created/advanced by CAS) | the three publication receipts |
| M5 grants / exact subset / API | COT: reader library PASS on deployed bytes; authorizer hop not exercised | COT_DEPLOYED_READER_MATRIX_20260923.json |
| M6 visible taxonomy + drill on screen | NOT LIVE (Andrew's re-test pending) | -- |
| M7 fresh source -> screen, three firms | COT hop 3; 49F hop 2 + role allowed; INF hop 2 + role allowed; hop 4 = Andrew's retest | receipts + HOLDINGS_ROLE_ARM_RESIM_20260924.json |
| Snapshot model overlay (Andrew 22:4xZ) | 49F: 7 models (assets TARGET at SmartX clock); INF: 17 Eclipse models with OBSERVED Orion assets; COT: 46 Rebalancer models over the ACCEPTED publication (462 of 841 accounts assigned, 379 unnamed), assets OBSERVED, blend composition TARGET | HOLDINGS_49F/INF/COT_MODEL_SNAPSHOT_20260923.json |

Offline-only work grades nothing until the live thread is live.

## Write claims

`data/assets/scripts/gold/investor_reporting/{holdings_49f.py, holdings_inf.py, inf_positions.py, holdings_snapshot.py}` and their tests;
`org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/*`. No shared auth/schema/package/IAM edits (P).

## Next proof

(1) Andrew's signed-in Anna Holdings screen (hop 4). (2) On Andrew's currency attestation for 49F and INF (the binder
accepts only ANDREW_ATTESTATION; P writes the records), publish both candidates through the existing publisher under
CTO review, then their reader matrices. (3) COT membership candidate ac3adb97 is built and its GO requested (the
d940022b06 shape: 18 immutable creates + index CAS on the precondition above, prior revision retained); on the GO,
publish it and run the deployed reader matrix again. (4) Holdings tab render of MODEL_LEAF children, taxonomy grouping
and withheld-drill facts in the M UI worktree (the wire contract carries all three; slices.ts renders none yet).

## Dependencies

| Needs | From (owner) | Interface / pin | State |
|---|---|---|---|
| 49F + INF firm report currency attestation | Andrew (via P's CurrencyAuthorities.json) | firm-currency-attestation-v1 record | ASKED at the M terminal |
| CTO read of the two publication receipts | 1.0.0_SA_CTO | receipts + this commit | HANDED OFF |
| Firm-bucket fence exemption rows for irpt-holdings-role (three buckets) | 4.0.0_SA_CRO rows, 2.0.0_SA_COO~P plan + apply, 1.0.0_SA_CTO sign | 0/3/0 applied 02:04:06Z, ledger CLOSED @7220e4a4f3 | DONE (CTO 99969) |
| Acceptance of registry row 58ee5b36dd | 1.0.0_SA_CTO | 99931 | ACCEPTED |
| NOT_READY reason render with a defined code | 2.0.0_SA_COO~P | contract addendum 2cdbe2bd60 (P 99816) | IN CTO REVIEW |
| Independent journey review | 3.0.0_SA_CVO~M | pinned candidates | seat not live |
| Eclipse account-membership batch read | Andrew per-use word via 4.0.0_SA_CRO | accounts/simple/list | NOT AUTHORIZED; one-to-one portfolio grain used |

## Parked

| Question (off-thread) | Owner | Un-parks when |
|---|---|---|
| Models > Primary / Custom placement for SmartX and Eclipse models (crosswalk) | 2.0.0_SA_COO~M | first live 49F or INF screen |
| Tax runtime (store d3a8c3e7e3, runner c354c33a92); Tax membership read from CRO~M's retained workbook projection | 2.0.0_SA_COO~M | canonical Silver landing of the workbook |
| 140 COT refused accounts | 2.0.0_SA_COO~M | BD lands active rows (CRO re-check October 2026) |
| 2 traded Tax accounts absent from custody; 17 SmartX accounts absent from Schwab 0833; 82 Orion accounts outside accounts_v2 | 4.0.0_SA_CRO~M | a landed master or source correction |
| SmartX prefix "smartx/platform/silver/" grades RAISE at the naming gate ('platform' is not a tier) | 1.0.0_SA_CTO (registry) | registry row |

## Limits

No authenticated browser PASS yet (Andrew's retest is the exercised arm). The two publication receipts carry the PRE-fence role arm
(explicitDeny) as measured at publication time; the post-fence flip is HOLDINGS_ROLE_ARM_RESIM_20260924.json, not a rewrite of the receipts. 49F multi-model leaf dollars are apportioned and claimed inferred (2,862 of 7,475). INF: 71 split accounts'
drills withheld, 60 model-named accounts in Client because their excluded part does not tie. No CVO verdict on any ID.
No shared CLOUD push by this seat.
