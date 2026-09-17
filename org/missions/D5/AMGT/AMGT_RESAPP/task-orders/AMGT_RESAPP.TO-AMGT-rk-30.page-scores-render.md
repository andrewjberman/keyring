# AMGT_RESAPP task order -- `AMGT-rk-30` (page half) -- the Model tab renders Robustness, Peers V and Divergence D

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-rk-30</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~31</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- this order arms no cron, alarm, monitor or cadence; the standing
  collection-stays-off / no-monitor moratorium is unaffected and no schedule is read or written.
comp-iam: DECLARED-NOT-APPLICABLE -- this order writes only to already-provisioned resources (the existing
  S3 bucket/prefixes and DynamoDB table this project already reads and writes) under the existing Lambda
  execution role; it grants no new permission and provisions no new resource.
comp-adversary: DECLARED-NOT-APPLICABLE -- this is a task-order specification, not a produced artifact; the
  validator-context declaration applies to the worker's own deliverable at drain, not to the order that
  specifies it.
</preflight>

**You are `0.9.0_WK_AMGT_RESAPP~31`, continuing.** Second of chain A's queue. **BEFORE YOU BEGIN, confirm
BOTH chain B's `AMGT-rk-30` adapter half AND chain SP's `AMGT-rk-30` producer half have drained** -- if
either has not, STOP and file a row. Every Bash call begins
`export OPAL_AGENT_SERIAL=0.9.0_WK_AMGT_RESAPP~31;`. **NEVER RUN AN INSTALL.**

## 1. THE CELL, inlined in full -- `AMGT-rk-30` page half (ADDENDUM 1: R13-L)

**RULED.** `portal/src/pages/SecurityAnalysis/tabs/ModelTab.tsx` gains a new render block for the three score
fields the adapter now serves at `bundle.scores` (`robustness`, `peers_v`, `divergence`), each rendered as
its MEASURED value or its ABSENT reason -- **a score that renders nothing because its field is missing is NOT
MET.** Divergence D renders its ABSENT reason ("house forecast does not serve") for every name; this is
CORRECT and expected, not a bug to work around.

## 2. WHERE THIS CAME FROM

**ROUND 13**, decomposition v1.7 s.21c, on `1.0.0_SA_CTO~Z`'s **ADDENDUM 1** @`509f3f7335`. The adapter half
(`AMGT_RESAPP.TO-AMGT-rk-30.scores-adapter-model-tab.md`, chain B) and producer half
(`AMGT_RESAPP.TO-AMGT-rk-30.scores-producer-runner.md`, chain SP) both feed this order; both must have landed
before this order's criteria can pass.

## 3. SURFACES -- what you may read and write

<paths>
portal/src/pages/SecurityAnalysis/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~31/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-rk-30.page-scores-render.md
</paths>

- **A SURFACE NOT NAMED IN `<paths>` IS A WALL.** Scratch is `<your worktree>/.scratch/` only.
- **COMMITTING:** `bash .tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~31 <0.9.0_WK_AMGT_RESAPP~31@opal.agent>" -F <msgfile> -- <paths>`.
  Never push, merge, rebase, `checkout --`, `stash` or `clean`.

## 4. BOUNDS

PORTAL FROZEN: COMMIT YES / PROMOTE NO. **THE PORTAL DEV PUSH IS RESERVED.** **COLLECTION STAYS OFF.** **NO
alarm, monitor, SNS/SES-send, notification or freshness checker.** No vendor call. No non-ASCII. **PUSH:
never.**
**THE REFUSAL CLAUSE:** a criterion you cannot satisfy AS WRITTEN is REFUSED with its measurement and a row;
never repaired, widened, or satisfied by a route this order did not name.
**SURPRISE ROWS:** your row continues `AMGT_RESAPP-Z-W31-S<k>` from your prior order; `"project":
"AMGT_RESAPP"` and `"fabric": "site-z"` on every new row; append by textual splice inside the one fenced
JSON array (never re-serialize it) and never edit an existing row. **Found something off-task? APPEND ONE
ROW AND KEEP WORKING.**

## 5. PROOF OF SPEC -- one clause per criterion (every invocation is LITERAL; record it byte-for-byte; each runs under timeout 120)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-rk-30"><invocation>cd portal && python -c "
import io, glob
fs = glob.glob('src/pages/SecurityAnalysis/tabs/ModelTab.tsx')
j = ''.join(io.open(f, encoding='utf-8', errors='replace').read() for f in fs)
for t in ('robustness', 'peers_v', 'divergence'):
    print(t, j.lower().count(t))
"</invocation><expect>all three field names occur at least once in ModelTab.tsx, each nonzero, all read 0 before this order lands</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-rk-30"><invocation>cd portal && npx tsc -b 2>&1 | tail -30</invocation><expect>no NEW TypeScript errors attributable to this order's edited files</expect></criterion>
</proof_of_spec>

**Record the ACTUAL OUTPUT and DENOMINATOR, not a paraphrase.** No judgment criterion on this order.

## 6. WHEN YOU ARE DONE

Write your instance to
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~31/AMGT_RESAPP.TO-AMGT-rk-30.page-scores-render.proof_of_spec.json`
per `org/standards/PROOF_OF_SPEC.schema.json`, graded by YOUR WORKTREE'S OWN
`python .tools/proof-of-spec-check.py <instance> AC1,AC2` (rc 0 is the verdict); flip `<status>` to
`complete`; commit with `--only -- <paths>`. **Report once, then STOP and WAIT.** `AMGT-rk-26` is your
queue's third item but is HELD -- do not begin it until the COO confirms both `AMGT-rk-22` (CARD 5) and this
chain's own upstream are ready; that confirmation is a separate continuation, not implied by this order's
completion.

**MUTATION DISCIPLINE:** snapshot WORKING-TREE BYTES to `.scratch/` before editing. Never `git checkout --`,
never `git stash`, never `git show :path`.
