# AMGT_RESAPP task order -- `AMGT-rk-26` -- captured render of the DEV-built page against the deployed adapter, all five tabs plus header, two names

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-rk-26</owned_cells>
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

**You are `0.9.0_WK_AMGT_RESAPP~31`, continuing -- THIS ORDER IS HELD. Do not begin it until the COO's
continuation message explicitly confirms BOTH `AMGT-rk-19` (page half, your own chain, already drained) AND
`AMGT-rk-22` (a SEPARATE, currently-unspawned chain, gated on Andrew's word on CARD 5) have deployed.** This
file is cut and committed now so the round's decomposition and issuance are complete and nothing is left by
silent omission -- it is not a signal that you may start. Every Bash call begins
`export OPAL_AGENT_SERIAL=0.9.0_WK_AMGT_RESAPP~31;`. **NEVER RUN AN INSTALL.**

## 1. THE CELL, inlined in full -- `AMGT-rk-26` (s.3.5's ruling; `rk-2` AC6 / `rk-8` AC4's closure class)

**RULED.** A captured render of the DEV-built page against the deployed adapter, for **`BA_US_Equity` and one
other keyed non-pilot name**, covering all five tabs -- **`ThesisTab`, `ModelTab`, `PeersTab`, `PostureTab`,
`ExecManagementTab`** (`portal/src/pages/SecurityAnalysis/tabs/`) -- plus the page header ("Security
Analysis", `SecurityAnalysis.tsx:54`). Saves the screenshot images AND the network log beside them (a
network-log capture is NEW work: no existing tool in this repo captures one today -- extend
`.tools/frontend-dev.py`'s Playwright harness, which already drives the browser and screenshots via
`system-Edge`/a pinned chromium fallback, with a `page.on("response")` listener or a CDP `Network.enable`
hook; `.tools/valgate/d2_runner.mjs` is a puppeteer-core alternative but is structural-assertion only and
also lacks network capture -- state which base you extended in your report).

**Runs only after `AMGT-rk-19` and `AMGT-rk-22` both deploy**, so the render shows the ROUND-13 plane, not
round 12's. A render of the round-12 plane grades a page nobody will open once round 13 lands.

**Two JUDGMENT criteria** (`rk-2` AC6 / `rk-8` AC4's own closure class): graded by the CVO at L9, never
self-graded by you.

## 2. WHERE THIS CAME FROM

**ROUND 13**, decomposition v1.7 s.21c, on `1.0.0_SA_CTO~Z`'s L10 round-12 analysis s.3.5 @`9419550eb1`. PRD
v0.10, ADMITTED, no PRD change.

## 3. SURFACES -- what you may read and write

<paths>
.tools/frontend-dev.py
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~31/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-rk-26.render-capture.md
</paths>

- **A SURFACE NOT NAMED IN `<paths>` IS A WALL.** Extend `.tools/frontend-dev.py` in place rather than
  forking a new script (the build ladder: reuse before new code). Your captured images/logs land under
  `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~31/` (needs no separate `<paths>`
  entry -- the tree convention grants it). Scratch is `<your worktree>/.scratch/` only.
- **COMMITTING:** `bash .tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~31 <0.9.0_WK_AMGT_RESAPP~31@opal.agent>" -F <msgfile> -- <paths>`.
  Never push, merge, rebase, `checkout --`, `stash` or `clean`.

## 4. BOUNDS

PORTAL FROZEN: COMMIT YES / PROMOTE NO. **THE PORTAL DEV PUSH IS RESERVED.** **COLLECTION STAYS OFF.** **NO
alarm, monitor, SNS/SES-send, notification or freshness checker.** No vendor call. No non-ASCII. **PUSH:
never.**
**THE REFUSAL CLAUSE:** a criterion you cannot satisfy AS WRITTEN is REFUSED with its measurement and a row.
**SURPRISE ROWS:** your row continues `AMGT_RESAPP-Z-W31-S<k>`; `"project": "AMGT_RESAPP"` and `"fabric":
"site-z"` on every new row; append by textual splice inside the one fenced JSON array (never re-serialize it)
and never edit an existing row. **Found something off-task? APPEND ONE ROW AND KEEP WORKING.**

## 5. PROOF OF SPEC -- one clause per criterion (every invocation is LITERAL; record it byte-for-byte; each runs under timeout 120)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-rk-26"><invocation>ls -la "$(git rev-parse --show-toplevel)"/org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~31/*.png "$(git rev-parse --show-toplevel)"/org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~31/*network* 2>&1</invocation><expect>ten screenshot files exist (five tabs times two names) plus a header capture for each name, and at least one network-log artifact per name/tab-set exists -- print the exact file list and denominator, never a bare count</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-rk-26" judgment="true"/>
  <criterion id="AC3" cell_refs="AMGT-rk-26" judgment="true"/>
</proof_of_spec>

**Record the ACTUAL OUTPUT and DENOMINATOR for AC1, not a paraphrase.** AC2 and AC3 are JUDGMENT criteria --
no verdict is yours to write; the instance records them `UNVERIFIABLE-BY-INSTRUMENT` with `status_reason`
naming the CVO.

## 6. WHEN YOU ARE DONE

Write your instance to
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~31/AMGT_RESAPP.TO-AMGT-rk-26.render-capture.proof_of_spec.json`
per `org/standards/PROOF_OF_SPEC.schema.json`, graded by YOUR WORKTREE'S OWN
`python .tools/proof-of-spec-check.py <instance> AC1` (AC2/AC3 are judgment, excluded from the mechanical
grade; rc 0 on AC1 plus the two judgment rows present is the verdict); flip `<status>` to `complete`; commit
with `--only -- <paths>`. Report once. **This is chain A's last order.**

**MUTATION DISCIPLINE:** snapshot WORKING-TREE BYTES to `.scratch/` before editing. Never `git checkout --`,
never `git stash`, never `git show :path`.
