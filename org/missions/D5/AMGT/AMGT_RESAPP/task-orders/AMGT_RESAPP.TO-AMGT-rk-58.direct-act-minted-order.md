# AMGT_RESAPP task order -- `AMGT-rk-58` -- a co-signed DIRECT act carries a MINTED order: `.tools/direct-act-order.py` mints the worker's grant from the signed never-widen pair, bounded to the paths the pair names, and never emits an order the L6 gate would refuse

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-rk-58</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~58</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- this order builds one repository tool and its test; it arms no cron,
  alarm, monitor or cadence, reads no schedule and writes none; the standing no-monitor moratorium is
  unaffected. (The round's gate ledger was read at the cut: comp-schedule 2026-09-18 ~15:55Z scanned 5 of 5
  carriers, C1=23 C2=6 C3=12 C4=21 C5=334, 25 gates armed -- none is a gate on a .tools/ edit.)
comp-iam: DECLARED-NOT-APPLICABLE -- this order performs NO live AWS act of any kind: no invoke, no read of a
  live policy, no Terraform, no deploy. Its only reads outside the worktree are `git show HEAD:<path>` of two
  committed ledger files. It grants no permission and provisions no resource.
comp-adversary: DECLARED-NOT-APPLICABLE -- this is a task-order specification, not a produced artifact; the
  validator-context declaration applies to the worker's own deliverable at drain, not to the order that
  specifies it.
</preflight>

**You are `0.9.0_WK_AMGT_RESAPP~58`.** Work ONLY in the worktree whose absolute path is given in your spawn
prompt. Your first act prints `git rev-parse --abbrev-ref HEAD` and tests that `org/`, `.tools/` and the paths in
section 3 exist; if any is absent, STOP with a BLOCKING row. Every Bash call begins
`export OPAL_AGENT_SERIAL=0.9.0_WK_AMGT_RESAPP~58;`. **NEVER RUN AN INSTALL.**

## 1. THE CELL, inlined in full -- `AMGT-rk-58` (R14-T4; row `AMGT_RESAPP-Z-W34-S2`; process)

**The analysis row, verbatim (`ROUND_ANALYSIS.round13.md` s.4 @9c8e04cd9a, row R14-T4 `:144`):** *"W34-S2: a
co-signed direct act either carries a minted order or the lane gate reads a signed pair as a grant"* -- serves
process; co-sign no. Chain T (tools). Carried from the round-13 slug by s.6 `:207` (*"W34-S2 -> T4"*).

**The row this cell closes, `AMGT_RESAPP-Z-W34-S2` (`INVESTIGATION_v1.md:8701-8723`, BLOCKING, ARMED, disarm owner
`2.0.0_SA_COO~Z`), verbatim in its two binding fields.** `spec_asserts` (`:8720`): *"This worker's dispatch prompt's
own <paths> block: 'infra/aws/terraform/harvest/scoped-amgt-api.tf' is a granted write/commit surface, and its own
procedure step 9 instructs committing the Terraform change in the same session."* `world_is` (`:8721`): *"The
mechanical owned-paths lane gate that actually decides commit admission reads grants from task-order files only, and
grants issued via an inline dispatch prompt (never materialized as a task-order markdown under this project's
task-orders/ directory) are invisible to it. The live infrastructure change is APPLIED and independently verified ...
only the SOURCE FILE'S commit to git is blocked."* The `notes` (`:8722`): *"ARMED because the same gap will refuse
any future worker dispatched the same way (a signed co-sign's own worker-face prompt, with no companion task-order
file) on any infra/aws/terraform/** or other owned-paths-enumerated surface."*

**THE MEASURED STATE, at HEAD (cite these lines; do not re-derive them from memory):**
- The residue of the row is ALREADY CLEARED and is NOT this cell's work: the `scores/v1/` list entry landed at
  `3c2a6e47ca` (2026-09-17, author `2.0.0_SA_COO~Z`, *"grant(AMGT_RESAPP round 13 ...): scores/v1/ added ... one
  Terraform locals-list entry"*) and sits at `infra/aws/terraform/harvest/scoped-amgt-api.tf:161` at HEAD. What
  remains is the MECHANISM the row names: the next direct act must not hit the same wall.
- The gate, `.tools/owned-paths-validate.py` @4e3142cfb3: the rule verbatim at `:114-122` (*"THE TASK ORDER IS THE
  WORKER'S GRANT ... admitted to exactly the paths that a NON-TERMINAL task order under <CODE>, issued_to that
  serial, names in its <paths> block AT HEAD -- and to nothing else"*, Andrew-direct 2026-09-04 ~04:58Z, record
  @9ef9a40aae); the census `_worker_orders()` `:176-206` reads `git ls-files -- org/missions/D*/*/<CODE>/task-orders/*.md`
  and `git show HEAD:<p>` -- HEAD, never the worktree (`:197`: *"a task order staged but absent at HEAD grants nothing
  yet"*); `_order_grants()` `:162-173` (exact / glob only with `*?[` / directory prefix ending `/`); the refusal text
  `:421-424`. The registry switch `worker_grant:` at `.owned-paths.yaml:44-46` (`serial_glob: "0.9.0_WK_*"`,
  `source: task-order-paths`). **There is exactly ONE grant source and it is the ORDER.** This cell does NOT add a
  second one: reading a signed pair inside the lane gate would widen a mechanical gate against the ratified
  single-source rule, and every seat that reads the gate would then have to read the pair's prose too.
- What the L6 gate refuses on a NEWLY-ADDED tree order, `.tools/to-pipeline-gate.py` @458fbb65ba: only paths staged
  `A`/`R` are graded (`_newly_added()` `:1757-1782`); `check_file(root, rel)` `:2402` is the per-file grader and is
  importable; the preflight enum `:31-35`, `:65-67` with the denominator rule `:77-83` (`COVERAGE_WORD_RE`);
  `<placeholders>` line-anchored `:165`; `<issued_to>` tier limb `:95-109`; the non-empty `<paths>` limb
  `:110-119`; `<owned_cells>` tokens graded against the decomposition `:246-331`; LIMB 6 sign-off `:2170-2260`.
- Where a direct act is written today: the round-13 pair
  `org/missions/D5/AMGT/AMGT_RESAPP/ledger/NEVER_WIDEN_ROUND13_SCORES_PREFIX_GRANT_COO_HALF.md` (`:13-15` names the
  one file, `infra/aws/terraform/harvest/scoped-amgt-api.tf:118`, as the whole act; `:29-30` requires the
  change-management entry committed) and `..._CTO_HALF.md`. Both are at HEAD. They are the fixture AC2 mints from.
- The spawn discipline, `.claude/skills/dispatch/SKILL.md:208-224`: *"THE TASK ORDER IS THE WORKER'S GRANT -- SO
  THE <paths> BLOCK IS A PERMISSION, NOT A HINT"*; it says nothing about a DIRECT act (an act spawned off a signed
  pair with an inline worker face and no order), which is the gap W34-S2 fell through.

**RULED, what you build (one tool, one test, one sentence):**
1. **`.tools/direct-act-order.py`** -- the MINTER. Verbs: `mint` and `--self-test`. `mint` takes `--code <CODE>`,
   `--slot <n>`, `--cell <cell-id>`, `--title "<text>"`, `--coo-half <repo-rel path>`, `--cto-half <repo-rel path>`,
   `--section "<heading text both halves carry>"`, one or more `--path <repo-rel entry>`, `--preflight-file <path>`
   (the three preflight lines the ISSUER wrote after running the batteries), `--criteria-file <path>` (a ready
   `<proof_of_spec>...</proof_of_spec>` block the ISSUER wrote from the pair's own discriminators), `--round <n>`,
   and `--dry-run`. It:
   (a) resolves the project tree root by glob `org/missions/D*/*/<CODE>/` (exactly one match or REFUSE), reads
   `project.json`'s `fabric`, and names the decomposition `decompositions/<CODE>_DECOMP.md` and the NEWEST
   `surprise-channel/investigations/INVESTIGATION_v<N>.md`;
   (b) reads BOTH halves AT HEAD (`git show HEAD:<path>` -- the pair is committed, never staged, per the COO half's own
   item 7); REFUSES (rc 2) if either is absent at HEAD or carries no heading line containing `--section`; prints
   `PAIR: COO sha256=<hex> CTO sha256=<hex>` over the HEAD bytes;
   (c) validates every `--path` against the `<paths>` grammar the two gates read (no leading `/`, no `..`, a glob only
   with `*?[`, a directory entry ends in `/`) and REFUSES (rc 2) any entry that NEITHER half names verbatim --
   `REFUSED: path not named by either half: <entry>` -- so the minted grant is bounded by the signed pair. This is the
   substance of "the lane gate reads a signed pair as a grant", delivered WITHOUT touching the gate: the pair bounds,
   the order grants;
   (d) REFUSES unless `OPAL_AGENT_SERIAL` starts with `2.0.0_SA_COO` (the issuer is the COO, base or lane), unless
   the decomposition text contains the `--cell` token (the gate's `<owned_cells>` limb would refuse it), and unless the
   preflight file carries all three tools each as `RUN -- (` with a digit on its line or `DECLARED-NOT-APPLICABLE `
   followed by a reason, and unless every criterion element in the criteria file carries exactly one invocation
   element and one expect element (or is `judgment="true"` with no children) and `cell_refs` equal to `--cell`;
   (e) renders the order with BOTH faces, in the shape of THIS order: the title line
   `# <CODE> task order -- \`<cell>\` -- DIRECT ACT: <title>`, the WORKER FACE marker, `<decomp_ref>`,
   `<issued_to>0.9.0_WK_<CODE>~<slot></issued_to>`, `<issued_by>` = `OPAL_AGENT_SERIAL`, `<placeholders>NONE</placeholders>`,
   the preflight block, sections 1-6 where section 1 INLINES the `--section` section of BOTH halves verbatim, section 3's
   `<paths>` = the validated `--path` entries plus the five standing entries (the worker's deliverables folder, the
   newest investigation file, the order's own path, `org/critical_paths/change_management/`,
   `org/critical_paths/.open_deploys/`), section 5 = the criteria block, the RECORD FACE marker, then
   `**ISSUER CLOSE-OUT, 2.0.0_SA_COO~Z, 2026-09-24 ~16:2xZ (round 14's face, closed late).** Flipped by the ISSUER. The worker's
final instance (@ca98c0829b, 2026-09-19 00:42Z, after the issuer's AC2 repair @7a5c818ff1 and the worker's unrounded-minter fix
@ad30266d3c) re-validated at HEAD by this seat in the shared tree: 5 of 5 criteria PASS, proof-of-spec rc=0 VALID, 9 of 9 artifact
rows resolved at pin, 2 of 2 surprises entries (W58-S1, W58-S2) resolving to channel rows. The face stayed `pending` for five days
after the work was terminal -- a stale face over finished work (R-78's class), found by the R-78 census on this serial, not by any
gate. W58-S1 (the fixture filename the gate refuses on its basename) was remedied by the issuer's repair; W58-S2 (GATE (x)'s
round-issuer limb lives in main(), invisible to check_file()) stands as a true statement about the gate, carried to the sweep's
carrier row rather than re-opened here. Nothing else moves: the minter and its test are on CLOUD since round 14.

<status>complete</status>`, `<round><n></round>`, `<slot>~<slot></slot>`, `<fabric><project.json fabric></fabric>`;
   the output path is `<tree root>/task-orders/<CODE>.TO-<cell>.<slug>.md` with the slug derived from `--title`
   (2-5 lowercase hyphenated words);
   (f) with `--dry-run` prints the rendered order to stdout and writes NOTHING; without it, writes the file, then
   imports `.tools/to-pipeline-gate.py` by `importlib.util.spec_from_file_location` (the gate's own pattern for
   `prd_signoff_lib`, `to-pipeline-gate.py:2185-2190`) and calls `check_file(root, rel)`; ANY violation deletes the
   file it just wrote and exits 3 printing the violations verbatim -- **the minter never leaves behind an order the gate
   would refuse**; on 0 violations it prints `MINTED: <rel path> sha256=<hex> gate_violations 0`.
   `--self-test` runs the PURE arms with a printed denominator (`RESULT: <f> arm(s) failed of <n>`): grammar refusals
   (leading slash, `..`, a bracket that is not a glob), the pair-subset refusal, the missing-heading refusal, the
   non-COO issuer refusal, the preflight-grammar refusal (a `RUN --` line with no digit), the criterion-shape refusal
   (two invocation elements in one criterion), and a positive arm that renders a fixture and finds exactly one
   invocation element and one expect element per criterion and the five standing paths-block entries.
   Plain ASCII throughout (`OK:`/`WARN:`/`ERROR:`/`REFUSED:`), stdlib only, Python 3.9-compatible, Git Bash 3.6.7-safe
   argv (no unix binary names in argv beyond `git`).
2. **`.tools/tests/test_direct_act_order.py`** -- pytest arms over the same pure functions plus one END-TO-END
   `--dry-run` mint in a temporary git repository the test builds itself (a `project.json` with `fabric`, a
   decomposition naming the cell, two committed halves with one shared heading naming one path), asserting the
   rendered order's tags, the pair hashes line, the subset refusal and the non-COO refusal. No arm touches the real
   project tree, S3, DynamoDB or a broker.
3. **`.claude/skills/dispatch/SKILL.md`** -- ONE sentence appended to the grant paragraph at `:208-224`: *"A
   co-signed DIRECT act (an act spawned off a signed never-widen pair with an inline worker face) is spawned with an
   order MINTED by `python .tools/direct-act-order.py mint ...` from that pair, or it is not spawned -- the minted
   order is the grant and the pair bounds it (row `AMGT_RESAPP-Z-W34-S2`, cell `AMGT-rk-58`)."* Nothing else in that
   file moves.

**What this cell does NOT change:** `.tools/owned-paths-validate.py` (read only -- the single grant source stands);
`.tools/to-pipeline-gate.py` (read only -- it is CALLED, never edited); `.owned-paths.yaml`; any existing task order;
any ledger half; the round-13 act (already landed at `3c2a6e47ca`). No live AWS act, no deploy, no vendor call.

**THE VALIDATION BAR (`C-VALIDATION-NAMES`, PRD v0.13 @1699960261 `:1652-1658`):** this is a process cell with no
security population; it is proven on a DRY RUN (AC2, AC3: `--dry-run` writes nothing; the one fixture AC2 writes is a
hidden untracked file under `task-orders/` that the same invocation deletes in `finally`) and on the tool's own
self-test. `C-PRODUCTION-HOME` (`:1643-1650`): the tool reads no worker's deliverables folder; its inputs are the
committed pair at HEAD and the issuer's two input files.

## 2. WHERE THIS CAME FROM

**ROUND 14**, decomposition s.22 (cut by `2.0.0_SA_COO~Z`), on `1.0.0_SA_CTO~Z`'s L10 round-13 analysis
`org/missions/D5/AMGT/AMGT_RESAPP/ledger/ROUND_ANALYSIS.round13.md` @9c8e04cd9a s.4 row R14-T4 (`:144`) and s.6
(`:207`); the row `AMGT_RESAPP-Z-W34-S2` (`surprise-channel/investigations/INVESTIGATION_v1.md:8701-8723`, filed
2026-09-18T02:45Z by `0.9.0_WK_AMGT_RESAPP~34`). PRD v0.13 @1699960261: `C-PRODUCTION-HOME` (`:1643-1650`),
`C-VALIDATION-NAMES` (`:1652-1658`). Law: ADHC_OWNPTH.005 (`.tools/owned-paths-validate.py:114-122` @4e3142cfb3);
`/dispatch` Step 4 (`.claude/skills/dispatch/SKILL.md:208-224`).

## 3. SURFACES -- what you may read and write

<paths>
.tools/direct-act-order.py
.tools/tests/test_direct_act_order.py
.claude/skills/dispatch/SKILL.md
org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-rk-58-fixture.direct-act.md
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~58/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-rk-58.direct-act-minted-order.md
</paths>

- **A SURFACE NOT NAMED IN `<paths>` IS A WALL.** A READ needs no grant (read `.tools/owned-paths-validate.py`,
  `.tools/to-pipeline-gate.py`, `.tools/prd_signoff_lib.py`, `.owned-paths.yaml`, the two round-13 scores-prefix
  halves and `org/missions/D5/AMGT/AMGT_RESAPP/project.json` freely); this block governs WRITES. The
  `AMGT_RESAPP.TO-AMGT-rk-58-fixture.direct-act.md` entry exists so AC2 can hand the gate a file at a tree path; it is NEVER
  committed -- it is deleted by the invocation that writes it, and a `git status --short` that shows it after AC2 is a
  FAIL of AC2. Scratch is `<your worktree>/.scratch/` only.
- **COMMITTING:** `bash .tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~58 <0.9.0_WK_AMGT_RESAPP~58@opal.agent>" -F <msgfile> -- <paths>`
  (message file written by the Write tool). Never push, merge, rebase, `checkout --`, `stash` or `clean`. Every `.py`
  you commit passes `.tools/commit-gate.sh` (py_compile + ds-precommit + ruff py39) inside safe-commit.

## 4. BOUNDS

**NO LIVE AWS ACT, NO DEPLOY, NO VENDOR CALL** -- none is named. PORTAL FROZEN (not your surface). **COLLECTION
STAYS OFF.** **NO alarm, monitor, SNS/SES-send, notification or freshness checker.** Secrets through `comp-secrets`
only. No non-ASCII in anything you write. **PUSH: never.** Your work is LOCAL; LD-0522 puts the push with
`0.0.0_AB_MSTR~Z`.
**THE GATE IS CALLED, NEVER EDITED.** If `check_file` refuses the AC2 fixture for a reason the minter could not have
known (LIMB 6 reading a sign-off as STALE, a decomposition token missing), that is a ROW naming the limb and its text,
never an edit to the gate and never a `# pipeline-override:` line.
**THE REFUSAL CLAUSE:** a criterion you cannot satisfy AS WRITTEN is REFUSED with its measurement and a row; never
repaired, widened, or satisfied by a route this order did not name.
**A COUNT BAR IS READ FROM THE LIVE STORE AT THE CUT and PRINTS its denominator** -- the task-orders directory count
AC3 prints is re-measured at spawn (`ls` before and after; equal is the bar).
**SURPRISE ROWS:** your row is `AMGT_RESAPP-Z-W58-S<k>`, `<k>` restarting at 1; `"project": "AMGT_RESAPP"` and
`"fabric": "site-z"` on every new row; append by textual splice inside the one fenced JSON array (never
re-serialize it) and never edit an existing row. **Found something off-task? APPEND ONE ROW AND KEEP WORKING.**

## 5. PROOF OF SPEC -- one clause per criterion (every invocation is LITERAL; record it byte-for-byte; each runs under timeout 120)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-rk-58"><invocation>cd "$(git rev-parse --show-toplevel)" && python .tools/direct-act-order.py --self-test 2>&1 | tail -20</invocation><expect>the final line reads "RESULT: 0 arm(s) failed of N" with N at least 8, and the arm names printed above it include a leading-slash refusal, a ".." refusal, a bracket-that-is-not-a-glob refusal, a path-not-named-by-either-half refusal, a missing-section-heading refusal, a non-COO issuer refusal, a preflight RUN line with no digit refused, a two-invocation criterion refused, and one positive render arm counting exactly one invocation and one expect per criterion and the five standing paths entries</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-rk-58"><invocation>cd "$(git rev-parse --show-toplevel)" && export OPAL_AGENT_SERIAL=2.0.0_SA_COO~Z && python -c "
import io, os, subprocess, sys, importlib.util, hashlib
root = os.getcwd()
T = lambda s: '<' + s + '>'
pre = 'comp-schedule: DECLARED-NOT-APPLICABLE fixture -- no schedule\ncomp-iam: RUN -- (fixture: 13 of 13 entries per limb read)\ncomp-adversary: DECLARED-NOT-APPLICABLE fixture -- a specification\n'
crit = T('proof_of_spec') + '\n  ' + T('criterion id=\"AC1\" cell_refs=\"AMGT-rk-58\"') + T('invocation') + 'echo fixture' + T('/invocation') + T('expect') + 'prints fixture' + T('/expect') + T('/criterion') + '\n' + T('/proof_of_spec') + '\n'
io.open('.scratch/rk58_preflight.txt', 'w', encoding='utf-8', newline='\n').write(pre)
io.open('.scratch/rk58_criteria.txt', 'w', encoding='utf-8', newline='\n').write(crit)
cmd = [sys.executable, '.tools/direct-act-order.py', 'mint', '--code', 'AMGT_RESAPP', '--slot', '58', '--cell', 'AMGT-rk-58', '--title', 'scores prefix grant fixture', '--coo-half', 'org/missions/D5/AMGT/AMGT_RESAPP/ledger/NEVER_WIDEN_ROUND13_SCORES_PREFIX_GRANT_COO_HALF.md', '--cto-half', 'org/missions/D5/AMGT/AMGT_RESAPP/ledger/NEVER_WIDEN_ROUND13_SCORES_PREFIX_GRANT_CTO_HALF.md', '--section', 'scores/v1/', '--path', 'infra/aws/terraform/harvest/scoped-amgt-api.tf', '--preflight-file', '.scratch/rk58_preflight.txt', '--criteria-file', '.scratch/rk58_criteria.txt', '--round', '14', '--dry-run']
r = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8', errors='replace', timeout=100)
out = r.stdout + r.stderr
print(out[-3000:])
print('mint_rc', r.returncode)
pair = [l for l in out.splitlines() if l.startswith('PAIR: COO sha256=')]
print('pair_line', len(pair), 'of 1')
rendered = out.split('---BEGIN ORDER---', 1)[1].split('---END ORDER---', 1)[0] if '---BEGIN ORDER---' in out else ''
print('invocation_tags', rendered.count(T('invocation')), 'expect_tags', rendered.count(T('expect')), 'paths_block', rendered.count('\n' + T('paths') + '\n'))
fx = 'org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-rk-58-fixture.direct-act.md'
try:
    io.open(fx, 'w', encoding='utf-8', newline='\n').write(rendered)
    spec = importlib.util.spec_from_file_location('togate', '.tools/to-pipeline-gate.py')
    g = importlib.util.module_from_spec(spec); spec.loader.exec_module(g)
    v, notes = g.check_file(root, fx)
    print('gate_violations', len(v), 'of 1 fixture'); [print('  V:', x) for x in v]
finally:
    if os.path.exists(fx): os.remove(fx)
print('fixture_remains', os.path.exists(fx))
"</invocation><expect>mint_rc 0; pair_line 1 of 1 with two 64-hex sha256 values over the HEAD bytes of the two round-13 scores-prefix halves; the rendered order (between the ---BEGIN ORDER--- and ---END ORDER--- markers the dry run prints) carries invocation_tags 1, expect_tags 1, paths_block 1, and its paths block names infra/aws/terraform/harvest/scoped-amgt-api.tf plus the five standing entries; gate_violations 0 of 1 fixture from the L6 gate's own check_file on the rendered bytes at a tree path; fixture_remains False -- the dry run wrote nothing and the fixture is gone ISSUER REPAIR (2.0.0_SA_COO~Z, on row W58-S1): the fixture is named in PROJECT.TO-NAME form so the gate's project-name limb can resolve it; AND because GATE (x) (one issuer per round, AMGT-rk-55, drained @432033882e) now refuses a newly-added order into a round that already has orders at HEAD, the minted fixture must be UNROUNDED -- a DIRECT act is outside every round -- so gate_violations 0 holds only if the minter emits no <round> element (if it emits one, that is the minter's defect to fix, not the criterion's); the fixture is removed and the index restored after the run</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-rk-58"><invocation>cd "$(git rev-parse --show-toplevel)" && export OPAL_AGENT_SERIAL=2.0.0_SA_COO~Z && python -c "
import os, subprocess, sys
d = 'org/missions/D5/AMGT/AMGT_RESAPP/task-orders'
before = sorted(os.listdir(d))
cmd = [sys.executable, '.tools/direct-act-order.py', 'mint', '--code', 'AMGT_RESAPP', '--slot', '58', '--cell', 'AMGT-rk-58', '--title', 'scores prefix grant negative', '--coo-half', 'org/missions/D5/AMGT/AMGT_RESAPP/ledger/NEVER_WIDEN_ROUND13_SCORES_PREFIX_GRANT_COO_HALF.md', '--cto-half', 'org/missions/D5/AMGT/AMGT_RESAPP/ledger/NEVER_WIDEN_ROUND13_SCORES_PREFIX_GRANT_CTO_HALF.md', '--section', 'scores/v1/', '--path', 'infra/aws/terraform/harvest/scoped-amgt-api.tf', '--path', 'lib/research/api/scoped_amgt.py', '--preflight-file', '.scratch/rk58_preflight.txt', '--criteria-file', '.scratch/rk58_criteria.txt', '--round', '14']
r = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8', errors='replace', timeout=100)
out = r.stdout + r.stderr
print(out[-1500:])
print('mint_rc', r.returncode)
print('refusal_line', sum(1 for l in out.splitlines() if l.startswith('REFUSED: path not named by either half: lib/research/api/scoped_amgt.py')), 'of 1')
after = sorted(os.listdir(d))
print('task_orders_before', len(before), 'after', len(after), 'unchanged', before == after)
"</invocation><expect>mint_rc 2 (a REFUSAL, distinct from the gate's rc 3); refusal_line 1 of 1 naming lib/research/api/scoped_amgt.py as a path neither half names -- the planted negative: a path outside the signed pair's write set is never granted; task_orders_before N after N unchanged True (re-measure N at spawn; nothing was written by a refused mint, so the directory count is the same before and after)</expect></criterion>
  <criterion id="AC4" cell_refs="AMGT-rk-58"><invocation>cd "$(git rev-parse --show-toplevel)" && python -m pytest .tools/tests/test_direct_act_order.py -q 2>&1 | tail -15</invocation><expect>a final line "N passed" with N at least 6 and 0 failed, the arms covering the pure grammar and subset refusals plus one end-to-end --dry-run mint inside a temporary git repository the test creates (a project.json with fabric, a decomposition naming the cell, two committed halves sharing one heading that names one path) asserting the rendered tags, the PAIR line, the subset refusal and the non-COO issuer refusal; no arm reads the real project tree</expect></criterion>
  <criterion id="AC5" cell_refs="AMGT-rk-58"><invocation>cd "$(git rev-parse --show-toplevel)" && python -c "
import io
for f in ('.tools/direct-act-order.py', '.tools/tests/test_direct_act_order.py', '.claude/skills/dispatch/SKILL.md'):
    b = io.open(f, 'rb').read()
    print(f, 'non_ascii_bytes', len(b) - len(b.decode('utf-8')), 'crlf', b.count(b'\r\n'), 'mentions_minter', b.count(b'direct-act-order.py'))
"</invocation><expect>the two NEW files print non_ascii_bytes 0 and crlf 0 (pure ASCII, LF only); SKILL.md prints mentions_minter at least 1 (0 at HEAD -- the one appended sentence) and its non_ascii_bytes figure is whatever it was at HEAD (that file already carries non-ASCII glyphs and this order does not add or remove any; print HEAD's figure beside it with git show HEAD:.claude/skills/dispatch/SKILL.md and state that the two are equal)</expect></criterion>
</proof_of_spec>

**Record each criterion's ACTUAL OUTPUT and its DENOMINATOR, not a paraphrase.** No judgment criterion on this
order. AC2 and AC3 use `.scratch/` for the two issuer input files; the AC2 fixture path is the ONE tree path this
order lets you write and it must not survive the invocation.

## 6. WHEN YOU ARE DONE

Write your instance to
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~58/AMGT_RESAPP.TO-AMGT-rk-58.direct-act-minted-order.proof_of_spec.json`
per `org/standards/PROOF_OF_SPEC.schema.json`, graded by YOUR WORKTREE'S OWN
`python .tools/proof-of-spec-check.py <instance> AC1,AC2,AC3,AC4,AC5` (rc 0 is the verdict); flip `<status>` to
`complete`; commit with `--only -- <paths>`. Report once, naming the minter's exact `mint` argument list so the COO can
mint the next direct act from it.

**MUTATION DISCIPLINE:** snapshot WORKING-TREE BYTES to `.scratch/` before editing. Never `git checkout --`,
never `git stash`, never `git show :path`.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

<status>complete</status>
<round>14</round>
<slot>~58</slot>
<fabric>site-z</fabric>
