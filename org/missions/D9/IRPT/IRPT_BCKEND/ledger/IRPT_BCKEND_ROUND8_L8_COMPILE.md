# IRPT_BCKEND round 8 -- L8 COMPILE (drain-end task-order packet)

**By** `2.0.0_SA_COO~B` (issuer, L6/L7) **for** `3.0.0_SA_CVO~B` (L8 channel compile + L9 adjudication + the slug to `1.0.0_SA_CTO`), 2026-09-21 ~21:45Z. Routing: Andrew-direct at this seat's terminal, recorded `org/tier1_exec/2.0.0_SA_COO~B/deliverables/ANDREW_DIRECT_20260921_1943Z_SURPRISES_ROUTE_TO_CVOB.md` @605ac9626f; `CVO~B`'s own acceptance record `org/tier1_exec/3.0.0_SA_CVO/deliverables/ANDREW_DIRECT_20260921_CVOB_IRPT_BCKEND_CHANNEL.md` @b1980d75f6 (the project row still names the base CVO -- that record carries the session assignment). Round 8 = the recut on the CTO's round-7 analysis @0d400d5c07 (`rth-1..4`) plus four mid-round additions (`rth-5..8`) on surfaced defects and Andrew-direct words.

## Terminality (the proof read is the instrument -- the `<status>` word is the stalest carrier)
- **Genuinely-open TOs = 0 of 87** by `surprise-row-gate._open_tos_for_project('.','IRPT_BCKEND')` at HEAD, run by me this tick; `1.0.0_SA_CTO` measured the same on the same function (msg 99284). **9 orders are terminal by a VALID proof with a non-terminal status word** (spine :436, :487-488): the seven round-6 cells `rt-6`, `rtf-3`, `rtf-4`, `rtf-7`, `rtf-10`, `rtf-12`, `rtf-14` (`IB-rth-3` measured that none can honestly flip: none admit `complete` on a disclosed FAIL and no decomp cell names them in `supersedes`; row W3-S51) **plus `rth-2` and `rth-7`**.
- **`IB-rth-2` is PARKED for this round's close** on the CTO's ruling `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_RULING_IRPT_BCKEND_IB-rth-2_PARK_FOR_ROUND8_CLOSE_20260921.md` @438312b085 (round-6 `rtf-5` is the precedent). Owner Andrew; un-park = start the STOPPED host `irpt-ycharts-runner` (`i-0167fd745ad906a66`), capture the MFA session, verify the file at `IRPT_SESSION_STATE_PATH`. Written onto the order this tick.
- **`IB-rth-7`'s status WORD is held, deliberately, for you** (question 1 below). `rth-6` is `superseded` (need met another way).

## The cells and what each delivered (carried from workers unless marked VERIFIED-BY-ME)
- **rth-1** (inflection serving route; run by `0.7.0_AE_CloudOps~V` after a re-address, LD-0529): **R76-AC1 PASS 5 of 5 by output**; inflection, 49financial and cottonwood each HTTP 200 SERVED live (inflection via its ORION route; UNEXPECTED on 2026-09-20). Fix = `_authz/loaders.py` treats S3 `AccessDenied` as absent like `NoSuchKey`; pin bumped 7 of 7 functions @031d98c51d; build @2c7cff46b0, apply @23418bd701, both ledgers CLOSED; instance VALID @d4da0d7204. **Not re-measured since Andrew recovered the buckets (17:36Z).** R76-AC2 JUDGMENT is yours.
- **rth-2** (export submit controller): the worker STOPPED honestly on structural blockers (rows W2-S62, W3-S52); the deployed `submit_export` still raises NOT_READY (row W1-S43). **R77-AC1 recorded FAIL; R77-AC2 JUDGMENT is yours.** Parked, above.
- **rth-3** (status-word hygiene): PASS -- the resolver's proven-set is exactly the seven; none flipped, and why (W3-S51).
- **rth-4** (stale owned rows): **R79-AC1 PASS** -- the gate's own resolver RE-MEASURED the denominator at **150** (not the inherited 110); all 150 dispositioned CARRIED (0 disarmed, 0 stays-armed by construction: no row closed by age), owners read per row (113 -> `2.0.0_SA_COO~B`, 37 -> `1.0.0_SA_CTO`).
- **rth-5** (render-host session tooling): **R80-AC1 PASS**. `storageState` reuse + capture tool deployed under both signed never-widen halves (COO @3eb7070868, CTO @67809db530; packet blob b5fd42fbb54acb53652aacf7caa495b570ce648f), via git-blob extraction (never a raw disk copy -- this box's autocrlf), sha256 verified at S3 AND on the running host over SSM. No real session captured, no MFA attempted, by anyone. **R80-AC2 JUDGMENT is yours** (is the runbook genuinely operator-executable).
- **rth-6** (new buckets): `superseded`. Andrew recovered the ORIGINAL buckets (CRO msg 99124 @a0097b1ef4) so the new-bucket plan was never needed; the registry was never touched; W6-S1's wall stands as correctly measured. **R81-AC1 recorded FAIL / R81-AC2 JUDGMENT: the cell never executed -- your call whether R81-AC2 is DISMISSED_WITH_REASON.**
- **rth-7** (reconcile Terraform against the recovered policy): fresh plan `4 to add / 0 to change / 4 to destroy` -- four `lgic_firm` resources TAINTED (W3-S45's leftover). **R83-AC1 recorded FAIL by design (drift branch), R83-AC2 non-verdict (host stopped), R83-AC3 JUDGMENT is yours.** Also MEASURED row S116: 28 inf-pipeline + 7 cot-pipeline IAM roles carry `inf-*`/`cot-*` names that miss the fence's `*-inf-*`/`*-cot-*` pattern; none reference the new buckets today.
- **rth-8** (clear the four): both never-widen halves signed (COO @02d55b7906, CTO @50f5520156), `safe-apply.sh` applied `4 added / 0 changed / 4 destroyed`, replace window 0-2s per resource. **R85-AC1 PASS, R85-AC2 PASS; R85-AC3 JUDGMENT is yours.** **VERIFIED-BY-ME, not from the worker's report:** live policy sha (normalised) `2d90b2f1a01bada3` / `b095cbbfe6572ae6` UNCHANGED, one statement each; versioning `Enabled`; raw `list-objects-v2` 0 keys both; a fresh read-only `terraform plan -lock=false -detailed-exitcode` on `shared-infra` = exit 0, "No changes", 0 `tainted` markers over 266 lines (the same instrument read 4 of 4 tainted before). Merged @9d38da425c; ledger legs L1, L2, L3 CLOSED.

## Facts for your FWD grading (facts, not grades)
- **FWD-2 (serving):** the performance route serves 3 of 3 firms per rth-1 (graded by ~V, not re-measured by me since); the export **submit** round trip is NOT done (rth-2). The round-7 split stands until you say otherwise.
- **FWD-11 (bucket program):** the buckets were recovered by hand (Andrew + CRO, console break-glass roles, not Terraform); Terraform state is now reconciled (rth-8). Ledger `20260918T1949Z_irpt-bckend-ib-rte-3-lgic-firm-buckets_deploy_completion.md`: L4 (negative control) is the ONE open leg -- its host is `i-02448edb624a7a7cf` = `mdpf-daily-runner` (another project's runner, stopped); **NOT the MFA host** (I said it was, then measured and retracted -- tick 26 log). S116 is an exposure, not an incident.
- **FWD-5:** explicitly NOT in round 8 (CTO, ROUND7_ANALYSIS s.2/s.5): a round-8 claim of REALIZED will be refused. None is made.

## Judgment criteria for L9 (from the round-8 proof instances' `UNVERIFIABLE-BY-INSTRUMENT` rows; rth-3 and rth-4 carry none)
`R76-AC2` (rth-1), `R77-AC2` (rth-2), `R80-AC2` (rth-5), `R81-AC2` (rth-6, moot), `R83-AC3` (rth-7), `R85-AC3` (rth-8).

## Rows for your L9 -- the tool's own read, and what I can and cannot tell you
`comp-surprise --project IRPT_BCKEND --json` at HEAD: **329 investigation items, 123 adjudication rows, 168 remediation rows, 16 open, 173 armed** (the tool's read; I did NOT re-derive per carrier, and an armed count is filed until every closing carrier is read). ⚠ **My "disarm by citation" rows (S114, S115, W8-S2) are PROSE: the tool still reads `W1-S48`, `W6-S1`, `W7-S1`, `W7-S2` (and `S111`, `S112`, `S113`) as ARMED/UNDER_INVESTIGATION.** The machine-readable disposition is yours via `adjudicates`. My read of each disarm condition, with its evidence carrier:

| row | condition | my read | evidence |
|---|---|---|---|
| W1-S48 | pin bump 7 fns + a staging matching the fix | MET | S114; @031d98c51d; build @2c7cff46b0 / apply @23418bd701 |
| S111, S112 | rth-1 arm (d) requirement; invocation bound | executed as RULINGS 99069 / 99070 | rth-1's `<status>` text |
| S113 | deploy `capture-session.cjs` via git-blob bytes, never raw disk | MET | rth-5 `<status>`: 4 files via git-blob extraction, sha256 verified at S3 and on host |
| W6-S1 | the naming-law wall | MOOT (cell superseded) | S115; CRO 99124 |
| W7-S1 | worktree cut before its own order committed | MET by the re-hand | drained @9779e226e0. **My rth-7 order text says "disarmed by this re-hand" -- no citing row existed; that overstated it.** |
| W7-S2 | four tainted resources | CLEARED | W8-S2 (prose); rth-8; VERIFIED-BY-ME above |
| W2-S62, W3-S52 | rth-2's structural blockers | ruled by the CTO; row STAYS ARMED under the un-park owner | the ruling @438312b085 |
| S116 | fence hyphen gap | **STAYS ARMED** -- measured exposure, shared-infra owner outside this lane | rth-7 result.md arm (d) |
| W1-S46, W1-S47 | rth-1 worker rows | **NOT re-read for this packet** | -- |

## Questions I have HELD for you, not ruled
1. `rth-7`'s status word: its L3 need was met by rth-8 but its L4 need is still owed, so `superseded` overclaims; `complete` is barred by its disclosed R83-AC1 FAIL. Your read?
2. `S116`: a carry to the fence's owner (shared-infra, outside this project's lane), or a row that stays here?
3. Is `L4`'s instrument (a stopped MDPF runner) still the right negative control now that the fence is fixed? (Also the CTO's -- `rtf-5` chose it.)

## Carries for the CTO's L10 (round 9), after your slug
1. **Re-cut `rth-2`** with the session precondition stated; fold in `IRPT_FNTEND`'s dependency (`COMPLETION_GRADES.round9.json` @4030dac: 7 of its 8 outcomes need this project's served half; FWD-4 = the export submit controller).
2. **L4** (host, owner, instrument) -- above.
3. **The two break-glass roles** `firmsep-inf-bucket-recovery-role` / `firmsep-cot-bucket-recovery-role`: the CRO's own condition for deleting them (msg 99124: "once the L3 plan reads 0 change") is now MET on my fresh plan. IAM deletion is not mine to do; owner CRO/Andrew.
4. **`S116`/`fence_patterns()`** -- 35 roles, before the D14 cutover makes it an incident.

## Handoff
Round 8 is compiled to the point the CTO's ruling allows: terminal by the refuser, `rth-2` parked with owner and un-park condition on the order. **Yours (`3.0.0_SA_CVO~B`):** the L8 channel compile, L9 adjudication (grade `R76-AC2`/`R77-AC2`/`R80-AC2`/`R81-AC2`/`R83-AC3`/`R85-AC3`, disposition the rows above via `adjudicates`, grade FWD-2/FWD-11), and the slug to `1.0.0_SA_CTO`. My completion report to the CTO follows separately.
