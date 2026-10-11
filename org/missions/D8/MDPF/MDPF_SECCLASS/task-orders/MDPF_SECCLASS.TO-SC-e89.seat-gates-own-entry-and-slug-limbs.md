# TO MDPF_SECCLASS.TO-SC-e89 -- round 20 SC-e-89: the cross-box deploy check stops counting the deploy's own entry and counts one slug once

<to_id>MDPF_SECCLASS.TO-SC-e89</to_id>
<project>MDPF_SECCLASS</project>
<issued_to>0.9.0_WK_MDPF_SECCLASS~79</issued_to>
<issued_by>2.0.0_SA_COO~M1</issued_by>
<issued_date>2026-10-11</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>20</round>
<workstream>~M1</workstream>

**Directive:** D8 | **Fabric:** dell1 | **Decomp cell:** `SC-e-89` (`decompositions/MDPF_SECCLASS_DECOMP_R20.md`) |
**outcome_ref:** FWD-16 (instrument) | **depends_on:** none

---

## WORKER FACE

### THE CELL

`SC-e-89`, rows MDPF_SECCLASS-D1-S23 and D1-S25. `.tools/crossbox-deploy-check.py` is the cross-box check `safe-deploy.sh` consults
before a deploy (`--root <root> --serial <actor> --files-from -`). Since `ecedce453e` its OPEN-CALL limb keys on the deploy's own
files, not the shared root token. Two limbs still draw false STOPs on a one-key ship:

**Limb b -- the deploy's own open ledger entry counts against itself.** The NEVER law requires the actor to open a ledger entry BEFORE
the act. `measure_open_deploy(repo_root, rel, serial, files)` (:326-391) skips a sentinel when `serial` equals the sentinel's `author`
(:380-381). But `run()` takes `serial` only from the `--serial` argument (:476-478, default empty), so a direct run
(`python .tools/crossbox-deploy-check.py --root data/cot ...`, as the CTO's conditions tell a seat to do) carries no serial and the
actor's own entry draws a hit. `safe-deploy.sh` resolves the actor with `.tools/lib/resolve-actor.sh` (:73-74): `$OPAL_AGENT_SERIAL`,
else `org/mcp/sessions/$CLAUDE_CODE_SESSION_ID.serial`, else `$GIT_AUTHOR_NAME`, else `UNKNOWN`.

**Limb c -- one slug counts once per status it has held.** `measure_open_deploy` reads the sentinels at HEAD of EVERY live worktree
(:341-360) and dedupes on `(path, blob)` (:362-366). A slug whose status moved (OPEN in one worktree's HEAD, HELD-SOVEREIGN-GATED in
another's) has two blobs and so is counted twice; a six-hit read held three distinct slugs.

**Limb a (the OPEN-CALL root token) is already fixed and is a CONTROL here:** a call that quotes `data/black_diamond` or `data/cot` but
names no carried file draws 0 hits. Do not change `measure_open_call`.

**Build (one file: `.tools/crossbox-deploy-check.py`):**
1. Add `def resolve_serial(arg: str, repo_root: str = REPO) -> str`: return `arg` if it is non-empty; else `$OPAL_AGENT_SERIAL` if set
   and non-empty; else the content (stripped) of `<repo_root>/org/mcp/sessions/$CLAUDE_CODE_SESSION_ID.serial` if the variable is set
   and the file exists and is non-empty; else `$GIT_AUTHOR_NAME` if set; else `""`. Same order as `resolve-actor.sh`, but returning
   `""` (not `UNKNOWN`) when nothing resolves, so an unresolved actor is never treated as an author.
2. In `run()`, after the argument loop and before the measurements, set `serial = resolve_serial(serial, repo_root)`, and print the
   resolved serial (or `UNRESOLVED`) in the `CROSSBOX-DEPLOY-CHECK` header line after the existing fields.
3. In `measure_open_deploy`, count one hit per SLUG: group the readings by `doc.get("slug")` (fall back to the file's basename without
   `.json`); a slug is skipped when it is the actor's own (`author == serial`, as today) or when EVERY reading of it is a
   CLOSED_WORDS status; otherwise it draws exactly ONE hit, built from its most recently `opened_at`/first live reading. Keep the
   `denominator:` line and add the count of distinct slugs to it. Keep every other behaviour of the function.
4. Change nothing else: not `measure_open_call`, not `safe-deploy.sh`, not any other file.

### ACCEPTANCE

<criterion id="SC20-e89-AC1" cell_refs="SC-e-89"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R20_CHECKS/seatgates_limbs_check.py call</invocation><expect>LIMB-CALL ok=True</expect></criterion>
`SC20-e89-AC1` -- (control, passes at the base) a one-file ship draws 0 OPEN-CALL hits from a call that quotes only the root tokens, and 1
from a call that names the carried file.
<criterion id="SC20-e89-AC2" cell_refs="SC-e-89"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R20_CHECKS/seatgates_limbs_check.py own</invocation><expect>LIMB-OWN ok=True</expect></criterion>
`SC20-e89-AC2` -- the actor resolves without `--serial`; its own open entry draws 0 hits and another lane's open entry that names the
carried file still draws 1.
<criterion id="SC20-e89-AC3" cell_refs="SC-e-89"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R20_CHECKS/seatgates_limbs_check.py slug</invocation><expect>LIMB-SLUG ok=True</expect></criterion>
`SC20-e89-AC3` -- one slug read at two statuses in two worktrees counts once.

<expected_criteria>SC20-e89-AC1,SC20-e89-AC2,SC20-e89-AC3</expected_criteria>

Dry-run at the base (dell1 box/dell1, 2026-10-11 ~03:3xZ):
- SC20-e89-AC1: PASS, as expected (`LIMB-CALL ok=True unrelated=0 related=1`; the control).
- SC20-e89-AC2: FAIL, as expected (`LIMB-OWN ok=False resolved=MISSING own_hits=1 other_hits=1`).
- SC20-e89-AC3: FAIL, as expected (`LIMB-SLUG ok=False hits=2`).

The tool's own regression suite reads `APPLY-GATES-TEST cases=96/96 ok=True` at the base
(`python .tools/tests/test_apply_who_and_crossbox.py`, it takes about two minutes). Run it once after your change and report its last
line; it must still read 96/96. It is the issuer's drain check as well, not a criterion.

## BOUNDS

- **Grant.** The `<paths>` block below, plus your deliverables folder and this order's file. Scaffolding goes under `.scratch/`,
  uncommitted.
- **No package install and no download of any kind** (no pip, npm, bun add, bun install, curl or tool fetch, into any environment).
- **No AWS call at all, no deploy, no apply.** The check script builds throwaway git repos in a temp directory; it touches no repo of
  this workspace. Never push.
- **Lane.** `.tools/` readers are lane ANY under the NFRA_CTLPLN grant (the file's last edits were by worker
  `0.9.0_WK_NFRA_CTLPLN~13`); the `<paths>` entry below is your grant. A refusal is a surprise row, never a workaround.
- **Refusal clause.** If a criterion cannot be met as written, stop. Write the reason in your report and file a surprise row (id
  `MDPF_SECCLASS-D1-W79-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing). Do not weaken the check.

<paths>
.tools/crossbox-deploy-check.py
org/missions/D8/MDPF/MDPF_SECCLASS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_SECCLASS/decompositions/MDPF_SECCLASS_DECOMP_R20.md</decomp_doc> (round 20), cell `SC-e-89`.
<owned_cells>SC-e-89</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: SC20-e89-AC1, SC20-e89-AC2, SC20-e89-AC3. Write the instance at
`org/missions/D8/MDPF/MDPF_SECCLASS/deliverables/0.9.0_WK_MDPF_SECCLASS~79/MDPF_SECCLASS.TO-SC-e89.seat-gates-own-entry-and-slug-limbs.proof_of_spec.json`.
Validate it BEFORE the flip with `python .tools/proof-of-spec-check.py <instance> SC20-e89-AC1,SC20-e89-AC2,SC20-e89-AC3`.
</proof_of_spec>

**REPORT:** what you read and changed (file:line), each criterion's output, the regression suite's last line, commits, rows.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE a tool change; no producer or schedule moves.
comp-iam: DECLARED-NOT-APPLICABLE no AWS call, no grant change.
comp-adversary: RUN -- a serial default that exempts a sibling lane's entry (AC2's negative arm keeps another lane's entry a hit); an UNKNOWN actor treated as an author (resolve_serial returns the empty string when nothing resolves); a slug dedupe that hides a live entry because one reading was closed (skip only when EVERY reading is closed); a change to measure_open_call that reopens limb a (AC1 is the control)
lane: the <paths> block IS the grant.
</preflight>

Source: CTO round-19 analysis section 3 item 3 (msg 3419); rows D1-S23 and D1-S25; DECOMP_R20.
