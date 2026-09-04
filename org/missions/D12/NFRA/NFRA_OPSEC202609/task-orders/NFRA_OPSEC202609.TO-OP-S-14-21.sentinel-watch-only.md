# TO NFRA_OPSEC202609.TO-OP-S-14-21 -- `opal-sentinel`, ARMED WATCH-ONLY: logs to counter to ALLOW-check to a WATCH row to a case file to ONE email, with the daily digest a FILE and not a send -- and every case file and report carrying the COVERAGE BOUND that says what the sentinel cannot see, so a quiet week is never read as a safe one (OP-s-14 + OP-s-21, FWD-14 + FWD-15)

<to_id>NFRA_OPSEC202609.TO-OP-S-14-21</to_id>
<project>NFRA_OPSEC202609</project>
<issued_to>0.7.0_AE_CloudOps~S</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<issued_date>2026-09-03</issued_date>
<status>complete</status>

⛔ **BLOCKERS, NAMED -- this cell has the most in the project and they are not interchangeable:**
| blocker | state | why it gates |
|---|---|---|
| `OP-s-18` | in flight (`TO-OP-S-4-18`) | the sets a BLOCK row would reach |
| `OP-s-20` | **not started, and it is the hard one** | **C-4: arming BLOCK with ZERO ALLOW rows is a VIOLATION, not a phase** |
| `OP-s-22` | staged | the IAM verdict runs before this code deploys (s.9 item 7) |
| `OP-s-16`, `OP-s-17`, `OP-s-5` | DONE | the table, the evidence store, the logs |
| `OP-s-3` | DONE | governs the `OP-s-21` coverage-bound string's removal |

**GO CONDITION: `TO-OP-S-4-18` terminal.** The `OP-s-22` verdict is sequenced inside deliverable 6, not before the GO.

⛔ **CORRECTED 2026-09-03 22:0xZ ON ROW Z-S90: THIS FACE NO LONGER WAITS ON `TO-OP-S-20`, AND MY ORIGINAL GATE WAS OVER-STRICT.** C-4 forbids **ARMING BLOCK** with zero ALLOW rows. **It does not forbid BUILDING the sentinel in WATCH mode, which is all this face does** -- the BLOCK arm is explicitly a later, separate act on measured evidence. I gated the build on the list and I should have gated only the arm. **`TO-OP-S-20` has stopped at its own GO condition and may not be buildable as decomposed at all** (the WAF layer carries no field attributing an address to a FIRM: `Cookie` reads REDACTED by `OP-s-5`'s deliberate redaction, and the handler is IP-blind per brief F4 -- so a per-firm census there is INEXPRESSIBLE, not merely sparse). **Had this gate stood, the largest cell in the project would have waited on a cell that may never complete in its current shape.** The BLOCK arm still waits on the ALLOW list and that has not moved.

**Directive:** D12 - **Fabric:** site-z - **PRD:** `../prd/NFRA_OPSEC202609_PRD.md` **v0.12 @3619ebecd9** (ENDPOINT FWD-14, FWD-15; C-1, C-3, C-4, C-6) - **Decomp cells:** `OP-s-14` + `OP-s-21` (v0.1.11, s.1a; the cell places S21's statement *"inside OP-s-14's format"*, which is why they are one face) - **Lane:** AE lane - **Round:** 3.

---

## ⛔ WATCH-ONLY. THE BLOCK ARM IS NOT IN THIS FACE.

The cell says it in terms: *"armed WATCH-only first; BLOCK arm only after OP-s-20 (C-4) and OP-s-3 (C-1)."* **This task order builds the sentinel and arms it to WATCH. It does not arm BLOCK.** The BLOCK arm is a later, separate act on measured evidence -- the ALLOW list existing with its denominator, and a month of WATCH rows for C-3.

>> **C-4 IS THE CLAUSE THAT MAKES THIS NON-NEGOTIABLE: arming BLOCK with 0 ALLOW rows is a VIOLATION, not a phase.** One partner office typically leaves through ONE address. **A false positive is a locked-out firm**, and the ALLOW list is the only thing standing between a rate trip and that outcome. <<

## THE PIPELINE, AND EACH STAGE IS GRADED

Subscription filter per scope -> parse -> counter with TTL -> **ALLOW check** -> WATCH row -> case file in the evidence store -> **ONE email** -> **daily digest FILE**.

**Two things about the notification half, because the moratorium is live and this is its narrowest exception:**
- **ONE email PER EVENT (C-6). Not a batch, not a cadence, not a dashboard.**
- **THE DAILY DIGEST IS A FILE, NOT A SEND.** The cell says *"daily digest FILE"*. **Writing a digest email is outside the exception.**

## THE `OP-s-21` HALF -- THE COVERAGE BOUND

The sentinel reads logs. **Whatever does not appear in those logs, it cannot see** -- specifically the raw `execute-api` addresses until FWD-2 fully lands. **Every case file and every daily report carries a bound string naming what the sentinel could not have seen.**

**Its removal is CONDITIONAL and MEASURED, not scheduled:** the cell ties it to `OP-s-3`, which is **DONE**; but FWD-2 also depends on `OP-s-1`, which is **IN FLIGHT**. **Measure the actual state at your vintage and state which addresses are and are not covered.** Removal, when it comes, is a **versioned change** -- the bound leaves the format by an edit that is recorded, never by quietly ceasing to be emitted.

>> **THE REASON THIS CLAUSE EARNS ITS OWN CELL: a "no incidents" week is never read as a quiet week.** Without the bound, an empty report is indistinguishable from complete coverage finding nothing -- the same absence-versus-not-looking failure this project has now hit three times on three different surfaces. <<

## DELIVERABLE

1. **The sentinel, end to end**, one subscription filter per scope, a counter with TTL, and the ALLOW check **before** any row is written.
2. **WATCH rows only.** No BLOCK row is written by this face, and the code path that would write one is present but **not armed** -- state how it is gated so the later arm is a config change and not a code change.
3. **Case files into the evidence store** (`opal-security-evidence`, under `cases/`), each carrying the coverage bound.
4. **ONE email per event**, to the recipient named for `OP-s-6`. **If that recipient is still unnamed, this face has the same gap and the same instruction: row, ask, build everything else, leave the subscription open.**
5. **The daily digest as a FILE** in the evidence store under `reports/`, carrying the bound.
6. **THE ROLE SEQUENCE:** declare and apply the sentinel's role, hand its applied ARN to `TO-OP-S-22`, wait for the verdict, then deploy the code.
7. **Deploy-ledger entries** per root, rollbacks named. **The proof-of-spec instance** at `../deliverables/0.7.0_AE_CloudOps~S/NFRA_OPSEC202609.TO-OP-S-14-21.sentinel-watch-only.proof_of_spec.json`, VALID with the expected ids BEFORE the complete flip.

## ACCEPTANCE -- criterion ids minted at cut

<criterion id="S14-AC1" cell_refs="OP-s-14"/> `S14-AC1` -- THE PIPELINE RUNS END TO END ON A FIXTURE: a staged burst under `OP-x-1` produces, in order and each pasted: a parsed event, a counter increment, an ALLOW check result, a **WATCH** row in the table, and a case file in the evidence store. Denominator: stages evidenced of stages in the pipeline.
<criterion id="S14-AC2" cell_refs="OP-s-14"/> `S14-AC2` -- NO BLOCK ROW EXISTS AND THE ARM IS OFF: a census of rows written by this face showing **BLOCK count = 0** with its denominator, and the gate that holds the BLOCK path shown in its off state. **A single BLOCK row written by this face is a FAIL.**
<criterion id="S14-AC3" cell_refs="OP-s-14"/> `S14-AC3` -- THE ALLOW CHECK IS CONSULTED AND CANNOT BE OVERRIDDEN (C-4): a fixture address present in the ALLOW list, driven hard enough to trip the counter, producing **no** WATCH row; and the same burst from a non-allowed fixture producing one. **The pair is the criterion** -- a single arm shows only that something happened.
<criterion id="S14-AC4" cell_refs="OP-s-14"/> `S14-AC4` -- ONE EMAIL, AND THE DIGEST IS A FILE: the send record for exactly one email for one event, with a census showing **one per event and no batch**; and the daily digest present as an OBJECT in the evidence store with its key pasted. **A digest delivered by email is a FAIL against C-6 and the moratorium.** If the recipient is unnamed, the email limb files `UNCOMPUTABLE-BY-CONSTRUCTION` citing its row and the digest limb still PASSES on its own.
<criterion id="S21-AC1" cell_refs="OP-s-21"/> `S21-AC1` -- THE COVERAGE BOUND IS PRESENT AND IS TRUE AT YOUR VINTAGE: the bound string quoted from a real case file AND from a real daily report -- both, not one -- **and a measured statement of which addresses the sentinel can and cannot see**, derived from what the subscription filters actually cover rather than from this face's expectation. **A bound string that is present but stale is worse than none.**
<criterion id="S1421-AC5" cell_refs="OP-s-14,OP-s-21"/> `S1421-AC5` -- VERDICTED BEFORE DEPLOY, AND NOTHING ELSE RODE: the `TO-OP-S-22` verdict for the sentinel's role referenced by instance with its date preceding deployment; per root the unscoped baseline, the enumerated changed-resource list, the unscoped re-plan 0-diff, ledgers CLOSED, push state MEASURED; and every fixture cleaned up with the cleanup read back.

<expected_criteria>S14-AC1, S14-AC2, S14-AC3, S14-AC4, S21-AC1, S1421-AC5</expected_criteria>

<decomp_ref>
<decomp_doc>org/missions/D12/NFRA/NFRA_OPSEC202609/decompositions/NFRA_OPSEC202609_DECOMP.md</decomp_doc> (v0.1.11), cells `OP-s-14` (manifest S14; FWD-14, FWD-15; EXERCISED) and `OP-s-21` (C-1; a coverage STATEMENT carried inside S14's format).
<owned_cells>OP-s-14,OP-s-21</owned_cells>
Read-dependencies, NOT claimed: `OP-s-15` and `OP-s-19` (they ENACT and UNDO the rows this face writes -- downstream), `OP-s-20` (the ALLOW list, a GO condition), `OP-s-22` (the verdict), `OP-s-23` (the threshold review this face's WATCH rows will feed).
</decomp_ref>

<preflight>
comp-schedule: RUN 2026-09-03 19:1xZ -- GATES ARMED 21 over 5 carriers (C1 SENTINEL denominator 21 -> 5 gates; C2 DEPLOY-LEDGER 4 -> 4; C3 MORATORIA 12 -> 12; C4 SCOPE-GUARD 20 -> 0; C5 PROJECT-BLOCKING 336 -> 0). **Both the SENTINEL and the MORATORIA carriers bind this face directly and the assignee re-reads all of them in phase 1** -- this is the cell those 5 sentinel gates were written for.
comp-iam: DECLARED-NOT-APPLICABLE as a substitute -- the sentinel role's permissions are `OP-s-22`'s verdict on the APPLIED role, and that cell's binding clause is that comp-iam silence is never an ALLOW.
comp-adversary: DECLARED-NOT-APPLICABLE -- this face pins no commit-scoped claim at cut; its dependency states are live reads the assignee re-takes in phase 1.
</preflight>

<proof_of_spec>
Criterion ids minted at cut by the issuer: `S14-AC1`, `S14-AC2`, `S14-AC3`, `S14-AC4`, `S21-AC1`, `S1421-AC5`. The ASSIGNEE fills a `PROOF_OF_SPEC.schema.json` instance at `org/missions/D12/NFRA/NFRA_OPSEC202609/deliverables/0.7.0_AE_CloudOps~S/NFRA_OPSEC202609.TO-OP-S-14-21.sentinel-watch-only.proof_of_spec.json` and validates it with `.tools/proof-of-spec-check.py <instance> "S14-AC1,S14-AC2,S14-AC3,S14-AC4,S21-AC1,S1421-AC5"` BEFORE the complete flip. **The controls that must be able to FAIL: `S14-AC3`'s allowed-fixture arm (it must produce NO row) and `S14-AC2`'s BLOCK census.** Every `surprises` entry opens with a row id that resolves in the project's channel.
</proof_of_spec>

<compiler_tools_mandate>
  <phase id="1" when="before write">Confirm `OP-s-20`'s ALLOW list exists with a non-zero denominator -- C-4 makes an empty list a violation, so its absence is a STOP before any code, not a condition to work around. Re-read what the subscription filters can actually cover for the S21 bound.</phase>
  <phase id="2" when="before deploying code">The role applied and the `TO-OP-S-22` verdict in hand.</phase>
  <phase id="3" when="after deploy">Every fixture removed, the BLOCK census run, and the coverage bound read out of a REAL case file rather than from the template.</phase>
</compiler_tools_mandate>
