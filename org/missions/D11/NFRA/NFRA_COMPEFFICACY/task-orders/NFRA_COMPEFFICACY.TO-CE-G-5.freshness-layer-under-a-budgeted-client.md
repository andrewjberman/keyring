# TO NFRA_COMPEFFICACY.TO-CE-G-5 -- the FRESHNESS LAYER under a budgeted client: a killed client never orphans the rebuild it started; a caller that finds a rebuild in progress is served stale immediately, labeled; the two waits reconciled; the cadence measured

<to_id>NFRA_COMPEFFICACY.TO-CE-G-5</to_id>
<project>NFRA_COMPEFFICACY</project>
<issued_to>0.8.0_AE_CloudComp</issued_to>
<issued_by>2.0.0_SA_COO</issued_by>
<issued_date>2026-09-03</issued_date>
<status>complete (self-marked, 2026-09-03T05:21:06Z; committed by the assignee itself under the tree task-orders/** -> ANY lane grant @f9c97a52ce) -- proof-of-spec VALID (rc=0) at org/missions/D11/NFRA/NFRA_COMPEFFICACY/deliverables/0.8.0_AE_CloudComp/NFRA_COMPEFFICACY.TO-CE-G-5.freshness-layer-under-a-budgeted-client.proof_of_spec.json; G5-AC1..AC6 self-assessed PASS (deliverable comp-kuzu.freshness.result.md at the tree home, fix commit 173dd335f4, deliverable+proof commit 9852efdfb3). CVO grade pending -- certifier != author. No surprises filed under this cell. Push state MEASURED in the DELIVERABLE REPORT to 2.0.0_SA_COO, not asserted here. Prior history: pending -- GO paired at cut. Authority: the L10 route of round 1 -- 3.0.0_SA_CVO's stamp, row NFRA_COMPEFFICACY-S6 @f659b4edd2, DECOMP_INVALIDATING -> L5, owner 2.0.0_SA_COO -- taken at L5 as decomp v0.2 @f54000091d (cell CE-g-5 ADDED), on Andrew's words on the loop (@10a4beaffb: the remediation pass runs from L5 for a decomp issue, then re-dispatches; @de2d6d643c: fresh and/or remediated task orders in dependency order). ROUND 2's FIRST task order; the aws corpus is unusable at the default budget until it lands.</status>

**Directive:** D11 · **Fabric:** laptop · **PRD:** `../prd/NFRA_COMPEFFICACY_PRD.md` v0.4 @`19bf1c7322` (s.4.4 RULE T's FORM -- the client side, ratified; FWD-7 / AC-7 the stale-served age bounded or stated) · **Decomp cell:** `CE-g-5` (v0.2 @`f54000091d`; STAGE fence "ROUND 2: CE-g-5 FIRST") · **Lane:** `infra/aws/globgrph/**` (the comp-kuzu engine, the seat's own per CE-t-22 @`dffbee781c`) + `.tools/tests/**` (TOOL_BATTERIES); the deliverable at `org/missions/D11/NFRA/NFRA_COMPEFFICACY/deliverables/0.8.0_AE_CloudComp/` (owner by path). Lanes MEASURED at cut with `owned-paths-validate --check-agent`: `_canonical.py`, `kuzu_cli.py`, the battery file, the deliverables folder -- 4 of 4 PERMITTED for `0.8.0_AE_CloudComp`. **Rule 27 seating:** `0.8.0_AE_CloudComp` BASE holds NFRA_COMPEFFICACY only (TO-CE-T-1 terminal @`fc5ec7106c`; this is continuity on the same project).

---

## THE CELL -- what round 1 found (S2, S3, S5, S6) and why it is a DECOMP cell, not a spec error

Rule T's client-side form (PRD s.4.4, landed on comp-find @`2718cffc45`) behaved every time: an honest `BUDGET
REACHED` prefix at 90 s, rc 0, never a hang. What it did NOT see is the layer beneath it: `infra/aws/globgrph/_canonical.py`
`ensure_fresh()` (:534) runs a synchronous rebuild-and-wait under a mkdir-mutex (:566) INSIDE the same `kuzu_cli.py`
subprocess that comp-find budgets. When the budgeted client that WON the mutex is killed at its budget,
`subprocess.run(timeout=)` kills only the direct child; the grandchild `kuzu_nessie_load.py` survives HOLDING THE LOCK,
unsupervised, past its own 600 s ceiling (INCREMENTAL_TIMEOUT_S :67 -- enforced only by a live parent). Every later
caller waits MUTEX_WAIT_S 180 s (:44) > the 90 s default and prints `BUDGET REACHED ... scanned 0 of 1`; at
ORPHAN_LOCK_S 900 s (:47) the next caller steals the lock, starts a new rebuild, and is killed at 90 s -- the cycle.
Three windows in one hour (03:16Z worker, 03:53Z CVO, 04:07Z live: PID 25896, parent dead, 743 s past its ceiling).
The decomp v0.1.2 had no cell for this (CE-t-22 closes on the KUZUSPLIT PRD half; CE-g-2 on the served AGE); v0.2 adds
CE-g-5. **Rule T's 90 s default is PRD-ratified and is NOT the subject.**

## DELIVERABLE -- one code change at the engine, one measurement, one file, the T-16 shape

1. **CODE, in `_canonical.py` (and `kuzu_cli.py` only if the process-group change needs it):**
   (a) **A killed client never orphans the rebuild it started.** Either the winner's rebuild runs in a process group
       the client's kill reaches (the loser-safe path), or the rebuild is DETACHED BY DESIGN and writes a status the
       losers read (state + started_at + pid + a heartbeat), so that a dead client leaves a supervised rebuild, not an
       orphan holding the lock. One of the two, stated in the file's docstring; not both.
   (b) **Serve stale immediately while a rebuild is in progress.** A caller that finds the lock held is served the
       EXISTING DB at once, labeled stale with its age (FWD-7 / AC-7: "bounded or stated, never silent"), instead of
       polling MUTEX_WAIT_S. No caller waits on another caller's rebuild.
   (c) **Reconcile the two waits.** MUTEX_WAIT_S 180 s and the client's 90 s default cannot both be right: either the
       engine's wait derives from the caller's `remaining()` (the s.4.4 form: every subprocess timeout derives from the
       budget) or one carrier states which bounds the other. Under (b) the wait may become zero; say so.
   (d) **Measure the rebuild cadence.** Why three rebuilds in one hour: the staleness predicate that triggers
       `ensure_fresh` (what "stale/BEHIND/unstamped" reads), with the count of triggers per hour over the last 24 h of
       whatever log carries it, denominator printed. A measurement, not a change: if the cadence itself is a defect,
       that is a FINDING in the deliverable with an owner, not this cell's edit.
2. **THE DELIVERABLE FILE** `org/missions/D11/NFRA/NFRA_COMPEFFICACY/deliverables/0.8.0_AE_CloudComp/comp-kuzu.freshness.result.md`:
   one fenced JSON block + prose in the T-16 shape for the fields that apply (identity of the engine path, the
   disclosure the losers now print, the 4.4 bounds with the ceiling EXERCISED, the measurement in (d)); every field
   present or explicitly ABSENT.
3. **THE BATTERY:** `.tools/tests/test_comp_find_battery.py` stays GREEN on production (the 3b arms + round 1's expiry
   arms), plus ONE new arm: a rebuild PLANTED in progress (a temp DB, a held lock) and a `--budget 1` client -- after the
   client's kill NO surviving rebuild process (process table read by pid), and a second caller returns `WITHIN BUDGET`
   inside the default budget carrying the stale label and age. Its planted mutant (an implementation that still waits
   or still orphans) must go RED.

## ACCEPTANCE -- criterion ids minted at cut; the assignee files the proof instance

<criterion id="G5-AC1" cell_refs="CE-g-5"/> `G5-AC1` -- NO ORPHAN: with a rebuild planted in progress and a `--budget 1` client killed at its budget, the process table read AFTER the kill shows no surviving `kuzu_nessie_load.py` (or, under the detach design, a supervised rebuild with a readable status the losers use); rc 0; the pair (before/after) shown.
<criterion id="G5-AC2" cell_refs="CE-g-5"/> `G5-AC2` -- SERVE STALE IMMEDIATELY: a second caller during a held lock returns `WITHIN BUDGET` inside the default budget with the stale label AND the age on the line (AC-7), never `BUDGET REACHED ... scanned 0`; the line quoted.
<criterion id="G5-AC3" cell_refs="CE-g-5"/> `G5-AC3` -- THE TWO WAITS RECONCILED: one carrier states the relationship between the engine's wait and the caller's budget (derived from `remaining()`, or zero under AC2, or a stated bound); `comp-read --enumerate 'MUTEX_WAIT_S'` shows the constant and its consumer agree; cited `file:line @ commit`.
<criterion id="G5-AC4" cell_refs="CE-g-5"/> `G5-AC4` -- THE CADENCE MEASURED: the trigger predicate named at `file:line`, the count of rebuild triggers per hour over the last 24 h with its denominator and the log it was read from; a FINDING with an owner if the cadence is a defect, no edit to it under this cell.
<criterion id="G5-AC5" cell_refs="CE-g-5"/> `G5-AC5` -- BATTERY + MUTANT: the existing arms stay GREEN on production at the FILE grain (directory grain stated as it reads, CTO's three files noted if still aborting); the new arm GREEN; its planted mutant RED; production sha before/after stated.
<criterion id="G5-AC6" cell_refs="CE-g-5"/> `G5-AC6` -- PUSH STATE MEASURED at report (ls-remote + is-ancestor). Under Andrew's push hold (LD-0522) the expected reading is LOCAL; say which state was read. The proof instance is VALID with every `surprises` entry resolving to a row (the SURPRISES limb) BEFORE the complete flip -- which the seat commits itself (lane ANY on task-orders/** @`f9c97a52ce`).

<expected_criteria>G5-AC1, G5-AC2, G5-AC3, G5-AC4, G5-AC5, G5-AC6</expected_criteria>

## SURFACES

`infra/aws/globgrph/_canonical.py` @`f659b4edd2`: `:44` MUTEX_WAIT_S=180.0 · `:47` ORPHAN_LOCK_S=900.0 · `:51` the winner-dies comment · `:67` INCREMENTAL_TIMEOUT_S (env GLOBGRPH_INCREMENTAL_TIMEOUT_S, default 600) · `:534` `ensure_fresh` · `:566` `os.mkdir(lock)` · `:590-598` the loser loop (CVO S6's read) · `infra/aws/globgrph/kuzu_cli.py` (the subprocess comp-find budgets) · `.tools/comp-find:184` `GLOBGRPH_KUZU_INCREMENTAL_REFRESH` default "1" · `.tools/_compbudget.py` (the form's one shared module) · surprise rows S2, S3, S5, S6 in `../surprise-channel/investigations/INVESTIGATION_v1.md` @`f659b4edd2`.

## BOUNDS

- **Rule T's client-side form does NOT change** (PRD s.4.4 is ratified; the 90 s default is not the subject). comp-find's search semantics and pagination do not change.
- **No new dependency; no new file outside `_canonical.py` (+ `kuzu_cli.py` if needed), the battery, the deliverable and the proof instance.** No gate, no monitor (CLAUDE.md s.5).
- **Do NOT kill the live rebuild** (PID 25896 or its successor) to make room: the 900 s steal covers a dead one; a planted rebuild on a TEMP DB is the test fixture. The interim `--budget >= 300` on aws-corpus pulls (issuer's note 93095) stands until this lands.
- **A spec-vs-world divergence is a ROW** at `../surprise-channel/investigations/INVESTIGATION_v1.md` (lane ANY), then keep working; never a message. The L8 seat reads the file.
- **Certifier != author:** the s.7 row-state word is the L4 owner's version bump on the L8/L9 seat's documentation, read from the record.

<decomp_ref>
<decomp_doc>org/missions/D11/NFRA/NFRA_COMPEFFICACY/decompositions/NFRA_COMPEFFICACY_DECOMP.md</decomp_doc> @f54000091d (v0.2), cell CE-g-5 (s.1b, ADDED on the round-1 L10 route; STAGE fence "ROUND 2: CE-g-5 FIRST").
<owned_cells>CE-g-5</owned_cells>
Read-dependencies, NOT claimed: CE-t-22 (the engine's code half, met), CE-t-1 (the client-side form, met @fc5ec7106c), CE-g-2 (the served AGE bound -- AC2's label is its instrument, but G-2 closes on its own row).
</decomp_ref>

<preflight>
comp-schedule: RUN -- GATES ARMED 19 across 5 carriers (C1 sentinel denominator 21 -> 5, C2 deploy-ledger 2 -> 2, C3 moratoria 12 -> 12, C4 scope-guard 20 SEMI-DECIDABLE -> 0, C5 project-blocking 337 NOT-DECIDABLE -> 0); 139 prose blocking fields NEEDS-READ; 0 armed gates name NFRA_COMPEFFICACY, comp-kuzu, globgrph or _canonical (read at 2026-09-03 04:36Z).
comp-iam: DECLARED-NOT-APPLICABLE -- the subject is process supervision, serving and a wait constant inside a repo-local Python engine over a LOCAL kuzu DB; no AWS principal, policy or resource is created, changed or newly read by this cell (the rebuild's existing read calls are unchanged), so the lens has an empty population at this subject grain.
comp-adversary: RUN -- rc 0 at read-vintage @f54000091d (2026-09-03T04:39:04Z, 20 s); 9 commits, 5 repo paths, 0 file:line cites (the `:NN` pins are inside backticks), 6 tool mentions; cited commits 9 attempted / 9 verified / 0 UNVERIFIABLE; cited paths 5 attempted / 3 stable / 2 flagged (both flagged = GONE at read-vintage: the deliverable file and the proof instance this TO CREATES -- expected, not stale); uncited siblings 68 in infra/aws/globgrph/ with the cap (25) declared; DEFERRED bucket not printed (--no-packet: stage 4 disabled by the caller, disclosed); 5 declared exclusions (v1 contract). Instrument: comp-adversary CLEARED @bbba0db0e9, run from a seat that did not fix it.
</preflight>

<proof_of_spec>
Criterion ids minted at cut by the issuer: `G5-AC1`..`G5-AC6`. The ASSIGNEE fills a `PROOF_OF_SPEC.schema.json`
instance at `org/missions/D11/NFRA/NFRA_COMPEFFICACY/deliverables/0.8.0_AE_CloudComp/NFRA_COMPEFFICACY.TO-CE-G-5.freshness-layer-under-a-budgeted-client.proof_of_spec.json`
and validates it with `.tools/proof-of-spec-check.py` BEFORE the complete flip, which the assignee commits itself.
G5-AC1's before/after pair and G5-AC5's planted mutant are the controls that must be able to FAIL; every `surprises` entry
opens with a row id that resolves in the project's channel (the SURPRISES limb refuses the flip otherwise).
</proof_of_spec>

<compiler_tools_mandate>
BEFORE WRITE: `comp-read infra/aws/globgrph/_canonical.py --for "how a rebuild winner is supervised, what a loser does while the lock is held, and where the wait constants are consumed"` and `--enumerate 'MUTEX_WAIT_S|ORPHAN_LOCK_S|INCREMENTAL_TIMEOUT_S|remaining'`. BEFORE COMMIT: `.tools/commit-gate.sh` on every .py touched; the battery direct AND under pytest at the FILE grain. AFTER COMMIT: one real `comp-find --corpus aws <pattern>` at the DEFAULT budget from this seat with the lock planted -- the line must read WITHIN BUDGET + stale label (AC2) -- and the same from any other seat that reads the record (FWD-9).
</compiler_tools_mandate>

**DELIVERABLE REPORT:** to `2.0.0_SA_COO` (the sequencer; the L8 seat reads the record, not a message) with per-criterion evidence, the production sha before/after, the battery numbers at both grains, the cadence number with its denominator, and push state as MEASURED (LOCAL expected under the hold). GO = this TO + the dispatch message.
