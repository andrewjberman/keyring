# TO NFRA_CTLPLN.TO-CT-t-3 -- round 6 THREAD CT-t-3: every script and data file that lists boxes reads the register instead; a fixture box needs no edit

<to_id>NFRA_CTLPLN.TO-CT-t-3</to_id>
<project>NFRA_CTLPLN</project>
<issued_to>0.9.0_WK_NFRA_CTLPLN~53</issued_to>
<issued_by>2.0.0_SA_COO~C</issued_by>
<issued_date>2026-10-09</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>6</round>
<workstream>THREAD</workstream>

**Directive:** D0 | **Fabric:** laptop | **Decomp cell:** `CT-t-3` (`decompositions/NFRA_CTLPLN_DECOMP.thread6.md`) | **outcome_ref:** FWD-2 |
**depends_on:** none

---

## WORKER FACE

### THE CELL

FWD-2: Andrew adds a box once, in one place, and every tool knows its name and its role. ACCEPT clause: "nobody edits a script
that lists boxes by hand". The analysis found the dell rows were added by editing the gate enum, two fabric readers and four id
grammars by hand. MEASURED at the cut with `comp-find '(dell1|DELL1).{0,80}(dell2|DELL2)'` over `.tools lib org/devices`, corpus
default (1,262 files): the source hits are `.tools/open-calls-scan.py`, `.tools/to-pipeline-gate.py`, `.tools/fabric-activity.py`,
`.tools/open-calls-scan-schedule.ps1` and `org/devices/kit_python_install.py`, plus 5 tests. The analysis also names
`.tools/remote-job.py` (`DEVICES`). The ONE register is `org/devices/DEVICES.json`, read through `lib/devices.py`.

### BUILD

1. `.tools/box-list-census.py`: the census. It finds every file under `.tools`, `lib` and `org/devices` (tests excluded and listed
   apart) that names two or more box ids or box placement values from the register in one literal list, set, dict, regex
   alternation, `case` or `ValidateSet`. Box ids come from the register, never typed, and the tool prints the denominator of files
   scanned. It writes nothing.
   LAST line: `BOX-LIST-CENSUS scanned=<n> hand_listed=<k> files=<comma list or ->`.
2. For each file that the census lists AND that is in this order's `<paths>`, replace the literal list with a read of
   `lib/devices.py`. Add a small function to `lib/devices.py` if one is missing, for example ids, placement values or an id regex
   built from the register. Keep each file's behaviour byte-identical on today's register: run its own test or self-test before and
   after and print both. A file the census lists that is NOT in `<paths>` is not edited; file one row naming it.
   - `.tools/to-pipeline-gate.py` is a commit gate. Change only how it obtains the box list. Run its self-test before and after. If it
     has none, prove the gate on two staged fixture orders in a scratch repository: one valid box, and one unknown box refused.
   - `.tools/open-calls-scan-schedule.ps1` is PowerShell 5.1. It reads the register by calling `python -c` on `lib/devices.py`, or
     by parsing `DEVICES.json` with `ConvertFrom-Json`.
3. `.tools/tests/test_no_hand_listed_boxes.py`:
   - the census over a fixture tree finds a planted hand list and passes a register read;
   - with a FIXTURE register holding a fifth box, each edited tool's box-aware path accepts the fifth box with no code edit;
   - the census over the real tree, after your edits, lists none of your files.
   LAST line: `NO-HAND-LISTED-BOXES-TEST cases=<k>/<n> ok=<True|False>`.

### RULES FOR THIS CELL

**Nothing you run changes the live fabric.** You do not start, stop or message any seat. You do not push, merge or rebase. You run
no `terraform` against a backend and no `aws` call. You send nothing on the agent bus. Reads of git refs (`git log`, `git show`,
`git for-each-ref`, including `origin/box/*` and `origin/CLOUD` after one `git fetch`) are allowed. Tests run in temporary
directories or temporary git repositories. The law files `CLAUDE.md` and `org/XXX.md` are LOCKED. `.claude/settings.json` is in
no grant. No non-ASCII in any file you write. Python: standard library only; ruff clean. The device register is read only through
`lib/devices.py`; no tool types a box name, a serial of a particular box, or a path under a user's home.
FOUND SOMETHING ODD OFF-TASK? Append ONE row (`spec_asserts` + `world_is`) to
`org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md` (id `NFRA_CTLPLN-W<slot>-S<k>`) and keep working.

### ACCEPTANCE

<proof_of_spec>
<criterion id="CTt3-AC1" cell_refs="CT-t-3"><invocation>python .tools/tests/test_no_hand_listed_boxes.py</invocation><expect>NO-HAND-LISTED-BOXES-TEST cases=</expect></criterion>
`CTt3-AC1` -- every case passing; the line reads `ok=True`.

<criterion id="CTt3-AC2" cell_refs="CT-t-3"><invocation>python .tools/box-list-census.py</invocation><expect>BOX-LIST-CENSUS scanned=</expect></criterion>
`CTt3-AC2` -- the census over the real tree after the edits. The issuer reads `hand_listed` and the files left, each of which has a row.
</proof_of_spec>

<expected_criteria>CTt3-AC1,CTt3-AC2</expected_criteria>

Each invocation runs from the worktree root under `timeout 120`. Write the proof instance to
`org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~53/NFRA_CTLPLN.TO-CT-t-3.no-hand-listed-boxes.proof_of_spec.json`, validate it with
`python .tools/proof-of-spec-check.py <instance> CTt3-AC1,CTt3-AC2`, and flip `<status>` to `complete` only when every mechanical criterion
passes and the instance is VALID.

<decomp_ref>
<decomp_doc>org/missions/D0/NFRA/NFRA_CTLPLN/decompositions/NFRA_CTLPLN_DECOMP.thread6.md</decomp_doc>
<owned_cells>CT-t-3</owned_cells>
</decomp_ref>

<paths>
.tools/box-list-census.py
.tools/tests/test_no_hand_listed_boxes.py
lib/devices.py
.tools/open-calls-scan.py
.tools/to-pipeline-gate.py
.tools/fabric-activity.py
.tools/open-calls-scan-schedule.ps1
org/devices/kit_python_install.py
.tools/remote-job.py
.tools/tests/test_fabric_enum_dell.py
.tools/tests/test_fabric_readers_dell.py
org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE this cell schedules nothing.
comp-iam: DECLARED-NOT-APPLICABLE no AWS call and no policy.
comp-adversary: RUN -- a commit gate broken for every commit by the edit (its self-test, or two scratch fixtures, before and after); a behaviour change hidden as a refactor (each file's own test before and after on today's register); the census itself hand-listing boxes (ids from the register); BLIND: a box named in prose or a comment (only literal lists are counted).
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: L10 round analysis `org/missions/D0/NFRA/NFRA_CTLPLN/ledger/ROUND_ANALYSIS.20261009.md` @333d2b37b3 (1.0.0_SA_CTO msg 107787); PRD `prd/NFRA_CTLPLN_PRD.md` v0.22 @333d2b37b3, ratified-text SIGNED (current).
