# TO NFRA_OPSEC202609.TO-OP-S-15-19 -- THE TABLE BECOMES TRUTH AND A HUMAN CAN UNDO A BLOCK: `opal-ipset-reconciler` drives the WAF IP sets from the S16 table and NOTHING ELSE EVER CALLS `UpdateIPSet` (C-2), and an audited CLI lifts a block by flipping the ROW so the address reaches us again within minutes (C-11) -- built together because the unblock path is meaningless without the reconciler that enacts it (OP-s-15 + OP-s-19, FWD-14 + FWD-17)

<to_id>NFRA_OPSEC202609.TO-OP-S-15-19</to_id>
<project>NFRA_OPSEC202609</project>
<issued_to>0.7.0_AE_CloudOps~T</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<issued_date>2026-09-03</issued_date>
<status>staged</status>

⛔ **BLOCKERS, NAMED: `OP-s-18` (the IP sets must exist to be reconciled INTO) and `OP-s-22` (the IAM verdict runs BEFORE any of these roles is deployed -- PRD s.9 item 7).** `OP-s-16` is DONE. **GO CONDITION: `TO-OP-S-4-18` terminal. THAT IS THE WHOLE CONDITION.**

⛔ **CORRECTED 2026-09-04 00:4xZ ON ROW Z-S114: THIS GATE WAS SELF-CONTRADICTING AND `0.7.0_AE_CloudOps~W` REFUSED TO START ON IT.** It read *"and `TO-OP-S-22`'s verdict returned for the roles this face declares"* -- **but `TO-OP-S-22` verdicts the APPLIED roles, and the roles do not exist until THIS face declares and applies them.** The verdict cannot return before its subject exists. **This face's own deliverable 5 states the real sequence and always did:** declare and apply the ROLES, hand the applied ARNs to `TO-OP-S-22`, wait for the verdict, **then deploy the CODE.** The verdict gates the **code deploy**, which is inside the face, not the face's start.

> **That is the same defect as the Z-S14 bar earlier tonight: a gate demanding a state that the gated work itself produces.** I wrote the resolution into the body and then wrote the unsatisfiable version into the gate, four lines apart. The ordering is circular only in appearance: **declare the roles in Terraform first, run the verdict on the declared-then-applied roles, then deploy the code.** That sequence is stated in deliverable 5.

**Directive:** D12 - **Fabric:** site-z - **PRD:** `../prd/NFRA_OPSEC202609_PRD.md` **v0.12 @3619ebecd9** (ENDPOINT FWD-14, FWD-17; C-2, C-5, C-7, C-11) - **Decomp cells:** `OP-s-15` + `OP-s-19` (v0.1.11, s.1a) - **Lane:** AE lane - **Round:** 3.

---

## THE ONE INVARIANT THAT OUTLIVES THIS FACE

**C-2: the TABLE is truth, and NOTHING other than the reconciler ever calls `UpdateIPSet`.** Every other cell in this chain is written assuming it. **A convenience path that writes an address directly to a set -- a script, a console click, a "just this once" -- silently makes the table a lie**, and the next full reconcile will erase whatever was written outside it. That is not a bug to be fixed later; it is the design working as specified.

**So this face must leave the estate ABLE to keep that invariant**, which means the reconciler's identity is the only principal with `wafv2:UpdateIPSet` on those sets, and that is verified rather than assumed.

## DELIVERABLE

1. **`opal-ipset-reconciler`, driven by the S16 table's stream**, plus a **once-daily full reconcile**. The stream path gives latency; the daily pass gives convergence after any missed event. **Both, not either.**
2. **IDEMPOTENCE IS A DESIGN REQUIREMENT AND A MEASURED ONE (C-7):** applying the table twice yields the same set. State how the reconciler achieves it and prove it.
3. **THE REMOVE EVENT UNBLOCKS (C-5):** a row leaving BLOCKED state must remove the address from the set by the same path. **An unblock that requires the daily pass is not an unblock; C-11 says the address reaches us again within MINUTES.**
4. **`.tools/opal-ipblock allow <addr> --reason` -- an AUDITED CLI that edits the ROW, NEVER the IP set (C-11).** The `--reason` is mandatory and recorded. **The portal Admin page is explicitly a LATER increment and is not in this face.**
5. **THE ROLE SEQUENCE, and it is how the `OP-s-22` circularity resolves:** declare the reconciler's and the CLI's IAM roles in Terraform and apply them; **hand those APPLIED role ARNs to `TO-OP-S-22` and wait for its verdict; deploy the code only after.** Do not deploy a function whose permissions have not been verdicted -- that is what s.9 item 7 means.
6. **A short-TTL fixture for the lapse behaviour:** the cell's `closes on` requires that **a block nobody renews lapses by itself.** Build the TTL and demonstrate it on a fixture, not on a real address.
7. **Deploy-ledger entries** per applied root (`safe-apply`, never bare), rollbacks named before each act.
8. **The proof-of-spec instance** at `../deliverables/0.7.0_AE_CloudOps~T/NFRA_OPSEC202609.TO-OP-S-15-19.reconciler-and-unblock-path.proof_of_spec.json`, VALID with the expected ids BEFORE the complete flip.

## ACCEPTANCE -- criterion ids minted at cut

<criterion id="S15-AC1" cell_refs="OP-s-15"/> `S15-AC1` -- A BLOCKED ROW REACHES THE SET WITHIN THE STREAM'S LATENCY, MEASURED: a fixture address written BLOCKED to the table; `get-ip-set` polled until it appears; **the elapsed time stated as a measured number with the poll interval.** "It appeared" without a latency is half the criterion.
<criterion id="S15-AC2" cell_refs="OP-s-15"/> `S15-AC2` -- IDEMPOTENT, DEMONSTRATED NOT ASSERTED (C-7): the full reconcile run twice against an unchanged table; the set's contents byte-compared across both runs and shown identical; **and the set's `LockToken` or version behaviour stated**, so a no-op reconcile is distinguishable from a rewrite that happens to produce the same list.
<criterion id="S15-AC3" cell_refs="OP-s-15"/> `S15-AC3` -- NOTHING ELSE CAN WRITE THE SETS (C-2), VERIFIED ON THE LIVE PLANE: an enumeration of every principal holding `wafv2:UpdateIPSet` on these two sets, printed with its denominator and its instrument, showing **only the reconciler's role**. **A DESIRED-plane read alone files `UNCOMPUTABLE`** -- this is the invariant the whole chain rests on and it deserves the applied plane.
<criterion id="S19-AC1" cell_refs="OP-s-19"/> `S19-AC1` -- THE CLI EDITS THE ROW AND NOT THE SET (C-11): the CLI's source showing it writes the table only, cited `file:line @ <commit-ish>`, **plus a live demonstration that the set is unchanged at the instant the CLI returns** and changes only after the reconciler acts. **That gap is the proof the CLI is not a second writer.**
<criterion id="S19-AC2" cell_refs="OP-s-19"/> `S19-AC2` -- AN UNBLOCK REACHES US AGAIN WITHIN MINUTES: a fixture address blocked, confirmed refused at the edge, lifted via the CLI, and confirmed **reaching us again**, with the elapsed time stated. **The refusal BEFORE is the positive control** -- without it the final success proves nothing.
<criterion id="S19-AC3" cell_refs="OP-s-19"/> `S19-AC3` -- THE AUDIT AND THE LAPSE BOTH WORK: a CLI invocation's audit record pasted showing actor, address, reason and timestamp; and a short-TTL fixture block shown to **lapse without anyone renewing it**, with before and after reads.
<criterion id="S1519-AC4" cell_refs="OP-s-15,OP-s-19"/> `S1519-AC4` -- ROLES WERE VERDICTED BEFORE CODE WAS DEPLOYED, AND NOTHING ELSE RODE: the `TO-OP-S-22` verdict referenced by its instance for the roles this face declares, with its date preceding the function deployment; per root the unscoped baseline, the enumerated changed-resource list, the unscoped re-plan 0-diff, ledgers CLOSED, push state MEASURED.

<expected_criteria>S15-AC1, S15-AC2, S15-AC3, S19-AC1, S19-AC2, S19-AC3, S1519-AC4</expected_criteria>

<decomp_ref>
<decomp_doc>org/missions/D12/NFRA/NFRA_OPSEC202609/decompositions/NFRA_OPSEC202609_DECOMP.md</decomp_doc> (v0.1.11), cells `OP-s-15` (manifest S15; FWD-14, FWD-17) and `OP-s-19` (manifest S19; FWD-17), both EXERCISED.
<owned_cells>OP-s-15,OP-s-19</owned_cells>
Read-dependencies, NOT claimed: `OP-s-16` (DONE -- the table), `OP-s-18` (the sets, GO condition), `OP-s-22` (the verdict, sequenced inside deliverable 5), `OP-s-14` (the sentinel WRITES the rows this face enacts -- it is downstream, not a dependency).
</decomp_ref>

<preflight>
comp-schedule: RUN 2026-09-03 19:1xZ -- GATES ARMED 21 over 5 carriers (C1 SENTINEL denominator 21 -> 5 gates; C2 DEPLOY-LEDGER 4 -> 4; C3 MORATORIA 12 -> 12; C4 SCOPE-GUARD 20 -> 0; C5 PROJECT-BLOCKING 336 -> 0). **The SENTINEL carrier's 5 gates are about this chain and the assignee re-reads them rather than taking this summary.** This face builds no notification: the sentinel's ONE email is OP-s-14's, not this face's.
comp-iam: DECLARED-NOT-APPLICABLE as a SUBSTITUTE -- the IAM question for these roles is `OP-s-22`'s own cell and is answered by `simulate-principal-policy` on the APPLIED roles, which is a live-plane instrument. `comp-iam` may be run for orientation but **its silence is never an ALLOW signal**, which is that cell's own binding clause.
comp-adversary: DECLARED-NOT-APPLICABLE -- this face pins no commit-scoped claim at cut; its source citations are required to carry `file:line @ <commit-ish>` in the PROOF (S19-AC1).
</preflight>

<proof_of_spec>
Criterion ids minted at cut by the issuer: `S15-AC1`, `S15-AC2`, `S15-AC3`, `S19-AC1`, `S19-AC2`, `S19-AC3`, `S1519-AC4`. The ASSIGNEE fills a `PROOF_OF_SPEC.schema.json` instance at `org/missions/D12/NFRA/NFRA_OPSEC202609/deliverables/0.7.0_AE_CloudOps~T/NFRA_OPSEC202609.TO-OP-S-15-19.reconciler-and-unblock-path.proof_of_spec.json` and validates it with `.tools/proof-of-spec-check.py <instance> "S15-AC1,S15-AC2,S15-AC3,S19-AC1,S19-AC2,S19-AC3,S1519-AC4"` BEFORE the complete flip. **The controls that must be able to FAIL: `S19-AC2`'s pre-unblock refusal, and `S15-AC3`'s principal enumeration, which is the only thing standing between C-2 and a silent second writer.** Every `surprises` entry opens with a row id that resolves in the project's channel.
</proof_of_spec>

<compiler_tools_mandate>
  <phase id="1" when="before write">Confirm the IP sets exist with the identifiers `TO-OP-S-4-18` actually created. Re-read the S16 table's stream configuration -- a stream that is not enabled makes deliverable 1 impossible and is a ROW before any code is written.</phase>
  <phase id="2" when="before deploying code">The roles applied and the `TO-OP-S-22` verdict in hand. Deploying first and verdicting after inverts s.9 item 7.</phase>
  <phase id="3" when="after deploy">Every fixture cleaned up -- no fixture address left in a live block list -- and the cleanup itself read back.</phase>
</compiler_tools_mandate>
