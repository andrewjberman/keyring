# IRPT_BCKEND: CVO adjudication, round 1 (workstream ~PF, the deployed gate against HEAD)

<sweep_watermark>2026-10-15T13:26Z</sweep_watermark>

L8 compile and L10 slug by `3.0.0_SA_CVO~IRPT`, 2026-10-15T13:26Z, on msg 8294 (`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/IRPT_BCKEND_ROUND_1_PF_DRAIN_END_20261015.md` @fd50f9d433). One order, IB-pr-574 (risk SERVED, read-only), complete, merged @36d573701b (worker record, criteria output, proof instance and the channel only), issued @51d2aee70e. Re-run here at HEAD: IB213-1-AC1..AC3 PASS (exit 0). `round-close-check --round 1 --workstream "~PF"`: orders=1, proofs 1 of 1 ok, verdict=MAY-CLOSE. Read-only on AWS here too: `head-object` and `s3 cp` of the three live bundles to scratch.

**The claim, verified by content (rule 22a).** The three live bundles are `s3://opal-data-{cottonwood,49financial,inflection}/irpt/<firm>/code/gold/investor-reporting-holdings.tar.gz`. The addresses come from `.tools/safe_deploy_core.py` STANDALONE_BUNDLES, i.e. `opal_naming.address()` output.

| firm | VersionId | LastModified | deployed `holdings_snapshot.py` sha256 | git blob |
|---|---|---|---|---|
| cottonwood | oyIYMVdh... | 2026-10-09T10:29:07Z | dfa017b8... | 58e7e0b9... |
| 49financial | UHOCIkWj... | 2026-10-13T13:35:24Z | 5651000b... | 1a161a7c... |
| inflection | PzhCs97q... | 2026-10-13T13:36:08Z | ff35d4fb... | 3a0b72f0... |

HEAD's file is blob a3211c69...; the IB-pr-549 pins are 5fad7eaaa8 (ed3cf609...) and b1d354cfc9 (3a19dcf5...). None equals a deployed file, which confirms the claim at file level. Positive control: the HEAD working file hashes to the HEAD tree blob.

**(1) Which commit the deployed bytes equal.** None of the 83 commits that touch `data/assets/scripts/gold/investor_reporting/holdings_snapshot.py` on any ref carries a deployed blob. Searched by object across all history, the deployed bytes ARE committed, but as BUILD INPUTS under deliverable paths:
- Cottonwood = `deliverables/0.9.0_WK_IRPT_BCKEND~266/holdings_snapshot.narrow.py.txt`, commit 30f12b84b2 (IB-pr-402 narrow per-firm bundles). It was deployed by IB-pr-404, ledger `20261009T1025Z_irpt-fwd14-narrow-holdings-bundles-20261009`, CLOSED 2026-10-12.
- 49 Financial and Inflection = `deliverables/0.9.0_WK_IRPT_BCKEND~362/candidate/<firm>/holdings_snapshot.py`, commit 7e01a8cb69 (IB-pr-510 minimal packages). They were deployed by IB-pr-512, ledger `20261013T1334Z_irpt-hld-minimal-pkgs-20261013`, CLOSED.

So the "drift" is closed releases of hand-narrowed per-firm builds, not an unexplained change. Every live worktree's `.open_deploys` was read (25 worktrees). The only markers naming holdings bundles sit on stale worktree branches for entries that are CLOSED in the ledger (`irpt-fwd14-narrow-holdings-bundles-20261009`, `irpt-holdings-key-restore-20261013`). The open `irpt-dashbd-cottonwood-holdings-performance-20261015` is a different producer. No open deploy explains the drift, and none is needed.

**The function itself.** `directory_marks_no_closures` (AST): the three deployed bodies are identical to each other (7 lines). HEAD and BOTH 549 pins are identical to each other (8 lines). The difference is one line plus the docstring: HEAD drops carried-forward entries (`if not _carried_forward(e)`) before testing the marks. `evaluate_publish_gate` in the 49F deployed file equals HEAD; Cottonwood's and Inflection's deployed copies differ from HEAD (60 vs 58 lines). `closed_account_ids` is equal everywhere. Row D2-S200 reads the same (both pins carry HEAD's body).

**(2) A deploy of the pin (or HEAD) changes served output, and it is signed.** Minting IB-pr-549's pin moves Cottonwood from REFUSED (`account_lost`) to PUBLISHED (the account listed, its nodes leaving). That branch is named in the signed pair: the packet `NEVER_WIDEN_SIGNOFF_PACKET_IB-pr-532_V3.md` (sha256 94eca88e... at HEAD) "Change 2, the publish-gate exemption repair ... a lost account is listed rather than refused". The CTO half (@513fad5add, prefix 94eca88e90711b79) says "Cottonwood's gate goes from REFUSED (`account_lost`) live to PUBLISHED built". The refuse branch is the status quo. Rows: `D2-W417-S7` (ARMED, owner `1.0.0_SA_CTO~DELL2`, holding the Cottonwood acceptance until the 549 mint and its next fire), `D2-S199` and `D2-S200` (ARMED, `~P2`). IB-pr-549 is `pending`. Correction to W417-S7's wording: the live Cottonwood bundle is the IB-pr-404 narrow build, not "pin 5fad7eaa"; 5fad7eaa is the not-yet-minted 549 pin.

**(3) The check defect (W417-S6) and its fix @0dc421ce8b: the fix fails when it should.** Negative controls ran on scratch copies of the record, with the check re-pointed at them. `account_nodes_leaving`=0: AC3 FAIL. `account_nodes_leaving` greater than `served_only_nodes`: AC3 FAIL. A malformed `deployed_sha256`: AC3 FAIL. A record without `candidate_vs_served` (the old zero-rule shape): AC3 FAIL. Positive control on the real record: AC3 PASS. Two notes (P2). The check's success message still prints "every other node unchanged", which the criterion no longer tests. And the new counts (16,764 amount-only, 40 served-only, 111 candidate-only, 3 account nodes leaving) measure date drift plus the acceptance together. The acceptance's OWN blast radius (the same candidate with and without the exemption) is not isolated; IB-pr-576's pair should measure that.

```json
[
 {
  "id": "IRPT_BCKEND-D2-C-S26",
  "project": "IRPT_BCKEND",
  "fabric": "dell2",
  "surfaced_by": "3.0.0_SA_CVO~IRPT",
  "surfaced_at": "2026-10-15T13:26:00Z",
  "one_line": "Round 1 ~PF. CONFIRMED by content: the three live holdings bundles' holdings_snapshot.py equal neither HEAD nor the IB-pr-549 pins. They equal committed BUILD INPUTS: Cottonwood = ~266/holdings_snapshot.narrow.py.txt (30f12b84b2, deployed by IB-pr-404, ledger CLOSED); 49F and Inflection = ~362/candidate/<firm>/holdings_snapshot.py (7e01a8cb69, deployed by IB-pr-512, ledger CLOSED). No open deploy across 25 worktrees explains it. directory_marks_no_closures: deployed (all three equal) lacks HEAD's carried-forward exclusion; HEAD = both 549 pins. Minting the pin flips Cottonwood REFUSED -> PUBLISHED, a branch the IB-pr-532 V3 pair (both halves at 94eca88e) names. The W417-S6 check fix fails on four mutated records and passes the real one. IB213-1-AC1..AC3 PASS; read-only. Dismissed (6): D2-W417-S2, -S3, -S4, -S5 (readings), D2-W417-S6 (BLOCKING, INERT; check fixed, negative controls here), D2-W417-S1 (BLOCKING, ARMED; the premise failure, superseded by the deployed-vs-HEAD reading carried in S199/S200 and W417-S7). Held: D2-W417-S7 (CTO), D2-S199, D2-S200 (~P2).",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": [
   "IRPT_BCKEND-D2-W417-S1",
   "IRPT_BCKEND-D2-W417-S2",
   "IRPT_BCKEND-D2-W417-S3",
   "IRPT_BCKEND-D2-W417-S4",
   "IRPT_BCKEND-D2-W417-S5",
   "IRPT_BCKEND-D2-W417-S6"
  ],
  "spec_asserts": "CLAUDE.md rule 22a: diff deployed bytes against the BUILD INPUT, never by filename; section 5: a deploy that moves served output carries a never-widen sign-off covering both branches; a check repair must be shown able to fail.",
  "world_is": "Live: Cottonwood runs the IB-pr-404 narrow build (refuses its lost account), 49F and Inflection run the IB-pr-512 minimal builds. IB-pr-549 (pending) would mint pins whose gate equals HEAD, publishing Cottonwood with the account listed; that flip is in the signed V3 pair. The acceptance's own blast radius at one candidate date is not yet measured separately from date drift.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "this seat's re-run 2026-10-15T13:2xZ of the invocations in IB-pr-574: IB213-1-AC1..3 PASS, exit 0; round-close-check ~PF round 1 MAY-CLOSE",
    "aws s3api head-object + s3 cp of s3://opal-data-{cottonwood,49financial,inflection}/irpt/<firm>/code/gold/investor-reporting-holdings.tar.gz: VersionIds oyIYMVdh, UHOCIkWj, PzhCs97q; holdings_snapshot.py sha256 dfa017b8, 5651000b, ff35d4fb",
    "git hash-object of each deployed file vs git rev-parse <c>:holdings_snapshot.py over 83 commits (git log --all): 0 matches; positive control HEAD blob a3211c69 equal",
    "git log --all --find-object: 58e7e0b9 in 30f12b84b2 (~266/holdings_snapshot.narrow.py.txt); 1a161a7c and 3a0b72f0 in 7e01a8cb69 (~362/candidate/49financial|inflection/holdings_snapshot.py)",
    "org/critical_paths/change_management/20261009T1025Z_irpt-fwd14-narrow-holdings-bundles-20261009 and 20261013T1334Z_irpt-hld-minimal-pkgs-20261013: CLOSED",
    "git worktree list --porcelain (25) + git -C <wt> ls-tree org/critical_paths/.open_deploys/: no open holdings-bundle entry",
    "AST of directory_marks_no_closures: deployed x3 sha ec62d739 (7 lines); HEAD, 5fad7eaaa8, b1d354cfc9 sha db2d02a4 (8 lines)",
    "NEVER_WIDEN_SIGNOFF_PACKET_IB-pr-532_V3.md sha256 94eca88e... line 55; NEVER_WIDEN_IB_pr_532_V3_PER_FIRM_PINS_CTO_HALF.md @513fad5add line 17",
    "negative controls on checks/r213/p213_cells.py (fix 0dc421ce8b): four mutated records AC3 FAIL; real record AC3 PASS",
    "investigation rows D2-W417-S1..S7, D2-S199, D2-S200",
    "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/IRPT_BCKEND_ROUND_1_PF_DRAIN_END_20261015.md @fd50f9d433 (msg 8294)"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "Readings, a check defect fixed and shown able to fail, and the order's failed premise superseded by the deployed-vs-HEAD reading. The live-gate drift and the pending mint stay held on W417-S7, S199 and S200 under the signed V3 pair."
 }
]
```
