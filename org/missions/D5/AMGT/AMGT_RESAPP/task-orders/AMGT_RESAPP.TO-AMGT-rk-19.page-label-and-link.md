# AMGT_RESAPP task order -- `AMGT-rk-19` (page half) -- label a filing-sourced series and link each point to its passage

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-rk-19</owned_cells>
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

**You are `0.9.0_WK_AMGT_RESAPP~31`.** Work ONLY in the worktree whose absolute path is given in your spawn
prompt. Your first act prints `git rev-parse --abbrev-ref HEAD` and tests that `org/`, `.tools/` and the
paths in section 3 exist; if any is absent, STOP with a BLOCKING row. **YOU HOLD CHAIN A, a queue fed in
DEPENDENCY order (not file order): `AMGT-rk-19` (this one, page half), then `AMGT-rk-30` (page half), then
`AMGT-rk-26` HELD at the tail. Chain A holds every portal edit this round, so the portal has ONE writer.**
**BEFORE YOU BEGIN THIS ORDER, confirm chain B's `AMGT-rk-19` adapter half has drained and its Lambda
redeploy is live** -- if it has not, STOP and file a row rather than building against a route that does not
yet exist. Every Bash call begins `export OPAL_AGENT_SERIAL=0.9.0_WK_AMGT_RESAPP~31;`. **NEVER RUN AN
INSTALL.**

## 1. THE CELL, inlined in full -- `AMGT-rk-19` page half (FWD-18; ADDENDUM 2's A2.3 item 3)

**RULED.** The portal's thesis driver chart component (`portal/src/pages/SecurityAnalysis/`, the component
rendering `ThesisTab`'s chart -- locate it by searching for the existing chart's props consuming
`thesis_driver_chart` from the thesis bundle response) labels a filing-sourced series **"from the filing, not
the model"** whenever the served `thesis_driver_chart.source` reads `"filing"`, and links EACH point to its
`passage_id` where one exists (a click-through to the passage text -- this is FWD-18's own DONE WHEN: *"a
figure clicked through to its passage"*). A series served via the ORIGINAL exact-mnemonic join (no `source`
field, or `source` absent) renders exactly as it does today -- this order adds a label and a link, it does
not change the existing model-block-sourced rendering path.

## 2. WHERE THIS CAME FROM

**ROUND 13**, decomposition v1.7 s.21c, on `1.0.0_SA_CTO~Z`'s L10 round-12 analysis s.3.1 @`9419550eb1` and
**ADDENDUM 2** s.A2.3 item 3 (unchanged from s.3.1's original item 3). The adapter half that serves `source`
and `passage_id` is a SEPARATE order on chain B, `AMGT_RESAPP.TO-AMGT-rk-19.adapter-second-join.md`, which
must drain and deploy before this order's criteria can pass.

## 3. SURFACES -- what you may read and write

<paths>
portal/src/pages/SecurityAnalysis/
portal/src/api/endpoints/amgt-lead-panel.ts
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~31/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-rk-19.page-label-and-link.md
</paths>

- **A SURFACE NOT NAMED IN `<paths>` IS A WALL** (RULING 1). Scratch is `<your worktree>/.scratch/` only.
- **COMMITTING:** `bash .tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~31 <0.9.0_WK_AMGT_RESAPP~31@opal.agent>" -F <msgfile> -- <paths>`
  (message file written by a NON-SHELL writer). Never push, merge, rebase, `checkout --`, `stash` or `clean`.

## 4. BOUNDS

PORTAL FROZEN both fabrics: COMMIT YES / PROMOTE NO. **THE PORTAL DEV PUSH IS RESERVED** under LD-0367/0368
and is NOT taken by any cell -- commit LOCALLY, state push state LOCAL. **COLLECTION STAYS OFF.** **NO alarm,
monitor, SNS/SES-send, notification or freshness checker.** Secrets through `comp-secrets` only. No vendor
call. No non-ASCII in anything you write. **PUSH: never.** Your work is LOCAL; LD-0522 puts the push with
`0.0.0_AB_MSTR~Z`.
**THE REFUSAL CLAUSE:** a criterion you cannot satisfy AS WRITTEN is REFUSED with its measurement and a row;
never repaired, widened, or satisfied by a route this order did not name.
**SURPRISE ROWS:** your row is `AMGT_RESAPP-Z-W31-S<k>`, `<k>` restarting at 1; `"project": "AMGT_RESAPP"` and
`"fabric": "site-z"` on every new row; append by textual splice inside the one fenced JSON array (never
re-serialize it) and never edit an existing row. **Found something off-task? APPEND ONE ROW AND KEEP
WORKING.**

## 5. PROOF OF SPEC -- one clause per criterion (every invocation is LITERAL; record it byte-for-byte; each runs under timeout 120)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-rk-19"><invocation>cd portal && python -c "
import io, glob
fs = glob.glob('src/pages/SecurityAnalysis/**/*.tsx', recursive=True)
j = ''.join(io.open(f, encoding='utf-8', errors='replace').read() for f in fs)
print('components', len(fs))
for t in ('from the filing', 'passage', 'source ===', \"source ==\"):
    print(t, j.lower().count(t.lower()))
"</invocation><expect>at least one component contains the label text (a case-insensitive match on "from the filing", worded as the worker actually wrote it -- if the wording differs, the worker names its exact wording and re-runs this check against that literal string) and at least one reference to rendering/handling a passage link; both read 0 before this order lands</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-rk-19"><invocation>cd portal && npx tsc -b 2>&1 | tail -30</invocation><expect>the merged tree's TypeScript build has no NEW errors attributable to this order's edited files (pre-existing unrelated errors, if any, are named and excluded, matching this project's own established practice of separating this cell's additions from inherited breakage)</expect></criterion>
</proof_of_spec>

**Record the ACTUAL OUTPUT and DENOMINATOR, not a paraphrase.** No judgment criterion on this order.

## 6. WHEN YOU ARE DONE

Write your instance to
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~31/AMGT_RESAPP.TO-AMGT-rk-19.page-label-and-link.proof_of_spec.json`
per `org/standards/PROOF_OF_SPEC.schema.json`, graded by YOUR WORKTREE'S OWN
`python .tools/proof-of-spec-check.py <instance> AC1,AC2` (rc 0 is the verdict); flip `<status>` to
`complete`; commit with `--only -- <paths>`. **Do not stop here** -- `AMGT-rk-30` (page half) is handed to
you next as a continuation, once its own upstream (chain B's adapter half and chain SP's producer) have both
landed; wait for confirmation before starting it.

**MUTATION DISCIPLINE:** snapshot WORKING-TREE BYTES to `.scratch/` before editing. Never `git checkout --`,
never `git stash`, never `git show :path`.
