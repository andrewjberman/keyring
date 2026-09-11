# IRPT_BCKEND -- L5 decomposition -- round 2 -- v0.2

**v0.2** (2026-09-11 ~11:5xZ, `2.0.0_SA_COO~B`, the ROUND-2 RECUT on the CTO's round-1 analysis `ledger/ROUND_ANALYSIS.round1.md` @`0d57ceb2f9` and the CVO's slug `surprise-channel/remediations/REMEDIATION_v1.md` @`27e67fa6a5`, against PRD v0.13 @`e6ba5d9878`, ADMITTED with both L4-R halves SIGNED). Round 1 (v0.1.1, 19 cells) closed at ROUND_CLOSE with 0 of 10 REALIZED; its cells are retained below by id (section 0) so every round-1 instance's `cell_refs` still resolves in this document's id space. Round 2 is twelve cells, `IB-rt-<n>` and the battery `IB-rtb-1`, cut to the CTO's eight rulings in his order: the seam and the guards first, the three declared producers next, then export, YCharts on the v0.9 mechanism, intake controls, records.

```json
{
 "project": "IRPT_BCKEND",
 "directive": "D9",
 "fabric": "laptop",
 "round": 2,
 "decomp_version": "v0.2",
 "prd_ref": "org/missions/D9/IRPT/IRPT_BCKEND/prd/IRPT_BCKEND_PRD.md@e6ba5d9878",
 "prd_version": "v0.13",
 "round1_analysis_ref": "org/missions/D9/IRPT/IRPT_BCKEND/ledger/ROUND_ANALYSIS.round1.md@0d57ceb2f9",
 "round1_slug_ref": "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/remediations/REMEDIATION_v1.md@27e67fa6a5",
 "brief_ref": "docs/briefs/investor-reporting-ir-bk-brief-20260910.md@2acf23d8fd",
 "endpoint_ref": "org/tier1_exec/1.0.0_SA_CTO/deliverables/ENDPOINT_FWD_IRPT_BCKEND_20260910.md",
 "endpoint_outcomes": ["FWD-1", "FWD-2", "FWD-3", "FWD-4", "FWD-5", "FWD-7", "FWD-8", "FWD-9", "FWD-10", "FWD-11"],
 "owns_grade": ["FWD-2", "FWD-7", "FWD-9", "FWD-10"],
 "cells_round2": 12,
 "cell_id_shape": "IB-rt-<n> (round 2, ruling-cut); IB-rtb-1 (the round-2 replay battery)",
 "worker_serial": "0.9.0_WK_IRPT_BCKEND~<slot> (the round-1 subagents, continued) and 0.4.0_DS_ClientPlatform~X (one DS-lane cell, the rule-13 act)",
 "cut_head": "67ef99e5c2",
 "counterpart_decomp": "org/missions/D9/IRPT/IRPT_FNTEND/decompositions/IRPT_FNTEND_DECOMP.md"
}
```

**One carrier, two sources.** Each round-2 face inlines VERBATIM the PRD v0.13 candidate row it serves and the CTO's ruling it executes; this document adds the ORDER, the ROOTS, the SEATING, the FENCE, the BATTERY and the round-2 findings. It restates no PRD row and re-cuts nothing round 1 delivered: the ten converged roots, the eleven live routes, the CloudFront path, the status envelope and recovery arms, the extraction and certification, and nineteen VALID instances stand and are BUILT ON (each face's "WHAT ROUND 1 DELIVERED" section names what).

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
