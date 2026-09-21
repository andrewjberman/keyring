# AMGT_RESAPP task order -- `AMGT-rk-89` -- the AMGT Security Analysis page is promoted from portal DEV to PROD by the DT seat's own /prod-deploy procedure: DEV `f22e369c` or later (rk-78's fallback-roster render and rk-80's text fixes) lands on PROD, CI concludes success, the served bytes carry the new text, and the PROD access gate (`src/App.tsx`, Dev + admin only) is byte-identical before and after -- no manager is given access by this act

<!-- ===================== ASSIGNEE FACE -- this is the WHOLE of the assignee's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-rk-89</owned_cells>
</decomp_ref>
<issued_to>0.2.0_DT_PortfolioAnalytics</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- this order arms no cron, alarm, monitor or cadence and reads or writes no
  schedule. It OPENS one deploy-ledger entry with .tools/deploy_ledger.py BEFORE the PROD push and CLOSES it on the
  served read (AC2, AC7); the only CI it touches is the portal repo's own deploy.yml, which the PROD push triggers
  exactly as every prior promote (v2.1.181 @07d5af72 the last).
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS role, policy, grant or resource is read or changed by the assignee; the
  server deploy is performed by the portal repo's CI under its own existing identity, exactly as every prior promote.
  The access gate this order protects is APPLICATION code (src/App.tsx), asserted byte-identical in AC1 and AC4.
comp-adversary: DECLARED-NOT-APPLICABLE -- this is a task-order specification, not a produced artifact; the
  validator-context declaration applies to the assignee's own deliverable at drain, not to the order that
  specifies it.
</preflight>

**You are `0.2.0_DT_PortfolioAnalytics`, the portal DT seat.** This order is executed by YOUR `/prod-deploy` procedure
(`.claude/skills/prod-deploy/SKILL.md`, Steps 0-8), unchanged; this face adds the criteria that grade it and the three
AMGT-specific limits in section 4. Run every command from the workspace root (`WS="$(git rev-parse --show-toplevel)"`,
quoted -- the path has a space). **Never read, show, diff or check out branch `wk-amgt-14-50` or `C:/tmp/wk-amgt-14-50`
-- it holds an exposed credential.** No non-ASCII in anything you write.

## 1. THE CELL, inlined in full -- `AMGT-rk-89` (the round-22 PROD promote)

**The ruling of record, verbatim -- `1.0.0_SA_CTO~Z`, `ledger/ROUND_ANALYSIS.round21.md` @739eb5f288, s.3 (`:41`):**
*"**PROD promote** | a task order to `0.2.0_DT_PortfolioAnalytics`: `/prod-deploy` the AMGT page, portal DEV `f22e369c`
or later to PROD, with the access gate untouched. It cites the standing adjudication @`c7bbb53f2a` item 1. PROD was
measured at `07d5af72`, which lacks it (tick 17). | served page, DT's own deploy law"* -- and s.4 (`:62`):
*"`0.2.0_DT_PortfolioAnalytics` | the PROD promote, on its order"*.

**The standing authority, verbatim -- `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ADJUDICATION_AMGT_RESAPP_20260921T191xZ.md`
@c7bbb53f2a, item 1 (`:14-17`):** *"**1. Portal promote -- RULED: STANDING, for AMGT page features, while PROD stays
gated to Andrew alone.** His ~17:2xZ reason ("as its gated to only me on PROD anyway") holds for every such promote, not
only the first. R19-D's page change promotes after its drain through the DT owner, with no new card. **The limit:** the
moment the gate widens (managers named), this standing reading lapses and a promote needs a word again."* That reason is
Andrew-direct ~17:2xZ 2026-09-21, recorded at
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260921_172xZ_AMGT_RESAPP_PROMOTE_IF_FEATURES_NO_WATER_IN_PIPES_BACKFILL_HELD_FOR_BRONZE_SILVER_SHAPE.md`
@e70b949ba0: *"might as well just push DEV to PROD if there are new features as its gated to only me on PROD anyway"*.
**So the authority holds ONLY while the gate is unchanged** -- AC1 and AC4 prove it is.

**THE MEASURED STATE, read by the issuer at 2026-09-21 ~23:3xZ (portal `git fetch origin` first). RE-READ every line
in AC1 before acting; any difference is a STOP (section 4), never a substitution:**
- `origin/DEV` = `f22e369c`; `origin/PROD` = `07d5af72` (tag `portal-v2.1.181`, your own promote at 17:29Z).
- `f22e369c` IS an ancestor of `origin/DEV` and is NOT an ancestor of `origin/PROD`.
- `origin/PROD..origin/DEV` = **2 commits**, both AMGT page work:
  `f22e369c 0.9.0_WK_AMGT_RESAPP~80 | fix(ExecManagementTab, AMGT-rk-80): one period on the CEO line, subtitle names the Bloomberg fallback`
  and `95d96edb 0.9.0_WK_AMGT_RESAPP~78 | feat(... AMGT-rk-78 ...): Exec Management tab renders the Bloomberg fallback ...`.
- The tree diff `origin/PROD..origin/DEV` is **8 files, all 8 under `src/pages/SecurityAnalysis/`** (+1044/-9).
- `src/App.tsx` is **identical** on `origin/PROD` and `origin/DEV` (0 diff lines); the gate commit `d8135e0a` IS an
  ancestor of `origin/PROD`.
- The main-tree portal checkout is on `DEV` at `95d96edb` (BEHIND `origin/DEV` -- your Step 1 pull case).
- The workspace `SITEZ` gitlink `portal` = `95d96edb`.
- **Served today** (`https://opalinvest.dev/`): index `Last-Modified: Mon, 21 Sep 2026 17:29:27 GMT`, entry
  `index-DTWT90UL.js`. A walk of the served JS (53 chunks) finds the positive control
  `Officers from the filing, with tenure against the pool` in `index-6d09s_NA.js`, and **0 of 3** new literals:
  `Officers from the Bloomberg fallback list`, `This table is the Bloomberg fallback`, `per Bloomberg, not the filing`.

**THE ACT:** `/prod-deploy`, Steps 0-8, promoting `origin/DEV` (which must contain `f22e369c`) to PROD. Expected
tag `portal-v2.1.182` (whatever your CI mints next -- record the real one).

## 2. WHERE THIS CAME FROM

ROUND 22, decomposition s.30 (cut by `2.0.0_SA_COO~Z`), on `1.0.0_SA_CTO~Z`'s round-21 analysis @739eb5f288 (msg 24119).
The promote was due after round 20 (rk-80's DEV push); it rides this slug as an ORDER because a Tier-2 seat hears an
act only as a task order (LD-0529) and round 21 was already issued (the ~15:12Z one-slug word; CTO msg 24116 accepted
the routing). Row `AMGT_RESAPP-Z-S201` (the page text) disarms on the rendered PROD page.

## 3. SURFACES -- what you may write

<paths>
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.2.0_DT_PortfolioAnalytics/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-rk-89.portal-prod-promote.md
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
portal
</paths>

- **The portal repo** is written ONLY by `/prod-deploy`'s own acts: the PROD merge + push from the ephemeral
  `.runtmp/portal-promote-*` worktree (GATE 5 admits a DT serial pushing PROD in the portal repo), and the Step-1
  DEV sync IF local DEV is behind (pull only -- see section 4 on a DEV push).
- **`portal` (the workspace gitlink)** is committed ONLY IF, at Step 6, the SITEZ gitlink is not already the
  promoted DEV head -- as ONE LOCAL commit on `SITEZ` via `.tools/safe-commit.sh`, **NEVER pushed** (on this fabric
  the workspace push is `0.0.0_AB_MSTR~Z`'s, LD-0522). Your v2.1.181 report did exactly this; do the same.
- **SURPRISE ROWS:** `AMGT_RESAPP-Z-DT89-S<k>`, `"project": "AMGT_RESAPP"`, `"fabric": "site-z"`, appended by textual
  splice inside the one fenced JSON array; never edit an existing row. `disarm_owner` names `2.0.0_SA_COO~Z` (a
  seat outside the project cannot hold it past the drain).

## 4. BOUNDS

- **THE ACCESS GATE IS NOT TOUCHED.** `src/App.tsx` must be byte-identical on the promoted PROD head and on the
  pre-act `origin/PROD` (AC1, AC4). No edit to any route guard, role check or ProtectedRoute prop. **Managers' access
  is NOT widened** -- their names are Andrew's (CTO adjudication item 6). If the payload you are about to promote
  changes App.tsx or any file outside `src/pages/SecurityAnalysis/`, **STOP**: the standing authority covers AMGT
  page features only, and a wider payload is a new call, not this order.
- **THE PAYLOAD IS FROZEN BY STATEMENT:** `/prod-deploy` merges LIVE `origin/DEV` at GO time. AC1 records the exact
  `origin/PROD..origin/DEV` list you promote; at Step 4 the merge's second parent MUST equal the `origin/DEV` AC1
  read. If DEV moved in between, STOP and re-run AC1 (a moved DEV is a new payload, graded afresh).
- **FREEZE WINDOW:** this order IS the COO's dispatch -- the freeze is active from your first act (Step 0's "If COO
  dispatched this promote" case). `2.0.0_SA_COO~Z` holds all portal/DEV pushes until your Step-8 report.
- **NO DEV PUSH BY YOU.** Your Step 1a covers local-ahead DEV; here origin/DEV already carries the payload. If Step 1
  finds local DEV AHEAD of origin/DEV, that is another seat's unpublished work -- STOP and route it to
  `0.0.0_AB_MSTR~Z` (your skill's own Step-1a rule).
- **THE DEPLOY LEDGER IS OPENED BEFORE THE PUSH.** Your v2.1.181 promote wrote its ledger entry AFTER the push (your
  own report, msg 23996 point 2) -- CLAUDE.md's NEVER-list requires it at the START. Here AC2 opens it, and AC3's
  push may not run until AC2 has printed the entry OPEN.
- **ABORT PATH:** your skill's own. On any gate failure STOP, tear down, leave PROD untouched; if the push landed
  but CI failed, report to `2.0.0_SA_COO~Z` and `1.0.0_SA_CTO~Z` at once -- never re-push or revert on your own.
- **THE REFUSAL CLAUSE:** a criterion you cannot satisfy AS WRITTEN is REFUSED with its measurement and a row; never
  repaired, widened or routed around. No `--force`, no `never-override` (you are admitted by GATE 5 as a DT serial).
- **PUSH:** portal PROD only (your promote). The workspace branch is never pushed by you.
- NO alarm, monitor, SNS/SES-send, notification or freshness checker. No secrets are needed.

## 5. PROOF OF SPEC -- one clause per criterion (every invocation is LITERAL; run each from the workspace root; record it byte-for-byte)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-rk-89"><invocation>git -C portal fetch origin && echo "DEV $(git -C portal rev-parse origin/DEV) PROD $(git -C portal rev-parse origin/PROD)" && (git -C portal merge-base --is-ancestor f22e369c origin/DEV && echo dev_has_f22e369c True) && (git -C portal merge-base --is-ancestor f22e369c origin/PROD && echo prod_has_f22e369c True || echo prod_has_f22e369c False) && (git -C portal merge-base --is-ancestor d8135e0a origin/PROD && echo gate_commit_on_prod True) && git -C portal log --format='%h %an | %s' origin/PROD..origin/DEV && echo "files $(git -C portal diff --name-only origin/PROD origin/DEV | wc -l) outside_security_analysis $(git -C portal diff --name-only origin/PROD origin/DEV | grep -vc '^src/pages/SecurityAnalysis/')" && echo "app_tsx_diff_lines $(git -C portal diff origin/PROD origin/DEV -- src/App.tsx | wc -l)"</invocation><expect>DEV a sha containing f22e369c (measured f22e369c at the cut), PROD 07d5af72; dev_has_f22e369c True; prod_has_f22e369c False; gate_commit_on_prod True; the log lists ONLY AMGT page commits by 0.9.0_WK_AMGT_RESAPP~* (2 at the cut: f22e369c, 95d96edb) and integrator merges; files 8 or more with outside_security_analysis 0; app_tsx_diff_lines 0. ANY outside_security_analysis above 0, any App.tsx diff, or any author outside the AMGT workers and the integrator: STOP, promote nothing (section 4)</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-rk-89"><invocation>python .tools/deploy_ledger.py open --slug amgt-rk89-portal-prod-promote --title "AMGT_RESAPP rk-89: portal DEV to PROD promote (rk-78 + rk-80)" --author 0.2.0_DT_PortfolioAnalytics --leg "L1|git|portal PROD|merge sha + peeled tag" --leg "L2|verify|served opalinvest.dev|index Last-Modified + 3 of 3 literals + App.tsx identical" && python .tools/deploy_ledger.py list</invocation><expect>"OK: OPENED deploy ledger" naming amgt-rk89-portal-prod-promote with legs L1 and L2, and the list shows it OPEN -- run BEFORE AC3's push and record the time; an AC3 push timestamp earlier than this entry's open time FAILS this criterion (the v2.1.181 promote's after-the-push ledger is the defect this bars)</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-rk-89"><invocation>your /prod-deploy Steps 0-5 exactly as the skill writes them, recording: the Step-4 merge command and its output, `git -C "$WORKTREE" rev-parse HEAD HEAD^2`, the parity check `git -C "$WORKTREE" diff origin/DEV HEAD | wc -l`, and the `git push origin PROD` output with its UTC time</invocation><expect>the merge is a --no-ff merge of origin/DEV onto origin/PROD; HEAD^2 EQUALS the origin/DEV sha AC1 printed (else STOP -- DEV moved); the parity diff is 0 lines; the push is accepted (no GATE-5 or VALGATE refusal) at a time AFTER AC2's open</expect></criterion>
  <criterion id="AC4" cell_refs="AMGT-rk-89"><invocation>git -C portal fetch origin --tags && echo "PROD $(git -C portal rev-parse origin/PROD)" && (git -C portal merge-base --is-ancestor f22e369c origin/PROD && echo prod_has_f22e369c True) && (git -C portal merge-base --is-ancestor d8135e0a origin/PROD && echo gate_commit_on_prod True) && T=$(git -C portal describe --tags --exact-match origin/PROD) && echo "tag $T peeled $(git -C portal rev-parse "$T^{commit}")" && echo "app_tsx_diff_vs_pre_act_prod $(git -C portal diff 07d5af72 origin/PROD -- src/App.tsx | wc -l)"</invocation><expect>PROD equals AC3's merge sha; prod_has_f22e369c True; gate_commit_on_prod True; a tag portal-v2.1.* (portal-v2.1.182 expected) whose peeled commit EQUALS the PROD sha; app_tsx_diff_vs_pre_act_prod 0</expect></criterion>
  <criterion id="AC5" cell_refs="AMGT-rk-89"><invocation>gh -R Opal-Capital/portal run list --json databaseId,headSha,workflowName,status,conclusion --limit 30 && gh repo view Opal-Capital/portal --json nameWithOwner</invocation><expect>EVERY run whose headSha equals the PROD merge sha is listed by workflowName with status completed and conclusion success (at least 1; the Deploy to Production workflow among them); nameWithOwner Opal-Capital/portal (the -R positive control, so an empty list can never read as a pass)</expect></criterion>
  <criterion id="AC6" cell_refs="AMGT-rk-89"><invocation>python -c 'import urllib.request as u; b = "https://opalinvest.dev"; r = u.urlopen(b + "/", timeout=30); h = r.read().decode("utf-8", "replace"); print("index", r.status, "Last-Modified", r.headers.get("Last-Modified")); todo = sorted({p.split(chr(34))[0] for p in h.split("/assets/")[1:] if p.split(chr(34))[0].endswith(".js")}); done = set(); lits = ["Officers from the Bloomberg fallback list", "This table is the Bloomberg fallback", "per Bloomberg, not the filing", "Officers from the filing, with tenure against the pool"]; hits = {l: 0 for l in lits}
while todo:
    a = todo.pop()
    if a in done: continue
    done.add(a)
    try: body = u.urlopen(b + "/assets/" + a, timeout=30).read().decode("utf-8", "replace")
    except Exception: continue
    for l in lits: hits[l] += l in body
    todo += [n for n in (q.split("/")[-1] for q in body.split(chr(34))) if n.endswith(".js") and "-" in n and " " not in n and len(n) < 80 and n not in done]
print("chunks", len(done)); [print(repr(l), hits[l]) for l in lits]'</invocation><expect>index 200 with a Last-Modified LATER than AC3's push time (it read Mon, 21 Sep 2026 17:29:27 GMT before the act); chunks 50 or more; each of the first three literals found at least once (0 of 3 before the act -- the negative control); the fourth, the RESOLVED-roster subtitle, still found at least once (the positive control that the walk reaches the tab chunk). NOTE the invocation is multi-line on purpose (a python -c with no backslash escapes and chr(34) for the quote character, per rows Z-S207/W84-S1: an escape-bearing inline criterion does not survive this device's tool transport)</expect></criterion>
  <criterion id="AC7" cell_refs="AMGT-rk-89"><invocation>python .tools/deploy_ledger.py close-leg --slug amgt-rk89-portal-prod-promote --leg-id L1 --proof "<AC4 PROD sha + tag>" && python .tools/deploy_ledger.py close-leg --slug amgt-rk89-portal-prod-promote --leg-id L2 --proof "<AC6 Last-Modified + literal counts>" && python .tools/deploy_ledger.py close --slug amgt-rk89-portal-prod-promote && git -C portal branch --show-current && git -C portal status --porcelain | wc -l && git ls-tree HEAD portal && git log --oneline -1 -- portal</invocation><expect>both legs closed with their proofs and the entry CLOSED (sentinel removed); the main-tree portal branch prints DEV with 0 porcelain lines (your Step 7 -- the main tree never left DEV); the SITEZ gitlink `portal` is either the promoted DEV head committed LOCALLY by you (its commit authored 0.2.0_DT_PortfolioAnalytics, NOT pushed) or unchanged because it already matched -- print which; `.runtmp/portal-promote-*` may persist physically (Filename too long) and is left for a human's word</expect></criterion>
</proof_of_spec>

**Record each criterion's ACTUAL OUTPUT and its DENOMINATOR, not a paraphrase.** No judgment criterion on this order.

## 6. WHEN YOU ARE DONE

Write your instance to
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.2.0_DT_PortfolioAnalytics/AMGT_RESAPP.TO-AMGT-rk-89.portal-prod-promote.proof_of_spec.json`
per `org/standards/PROOF_OF_SPEC.schema.json`, graded by `python .tools/proof-of-spec-check.py <instance>
AC1,AC2,AC3,AC4,AC5,AC6,AC7` (rc 0 is the verdict); flip the order's status to complete; commit with
`bash .tools/safe-commit.sh --author "0.2.0_DT_PortfolioAnalytics <0.2.0_DT_PortfolioAnalytics@opal.agent>" -F <msgfile written by the Write tool> -- <paths>`.
Then send your Step-8 RAVC report to `2.0.0_SA_COO~Z` (it releases the portal/DEV freeze), carrying your skill's own
table (PROD commit, tag peeled, CI run + conclusion, workspace pointer LOCAL or unchanged, main tree on DEV) plus AC6's
served line and literal counts, and citing this order id `AMGT_RESAPP.TO-AMGT-rk-89`.

<!-- ===================== RECORD FACE -- does NOT travel to the assignee ===================== -->

<status>pending</status>
<round>22</round>
<slot>~89</slot>
<fabric>site-z</fabric>

**Issuer notes (record face):**
- **Addressee check, measured at the draft (2026-09-21 ~23:3xZ):** `.tools/to-decomp-ref-lint.py`'s own
  `_open_to_index` (3094 tracked TO files scanned, 190 open holdings across 22 seat instances, 56 pipeline-registered
  projects) finds **0 open TOs held by `0.2.0_DT_PortfolioAnalytics` on any pipeline project**, and a direct
  `<issued_to>` census over `org/missions/**/task-orders` finds 0 orders ever issued to it. So the one-project-per-
  Tier-2-seat lint passes by construction. This is the FIRST tree order addressed to a DT seat; the only prior
  non-worker addressees in the tree are AE lanes (0.7.0_AE_CloudOps~*, 0.8.0_AE_CloudComp*, 0.4.0_DS_ClientPlatform~X).
- **Slot `~89`** continues the AMGT id sequence; the assignee is a seat, not a worker slot, so no worktree is issued.
- **Send:** the GO to `0.2.0_DT_PortfolioAnalytics` cites this order's id, which is what LD-0529 needs.
- **Drain:** grade from the committed instance; the page screenshot (`/frontend-dev` on the PROD render is not
  possible headlessly behind the Dev+admin gate) is replaced by AC6's served-bytes check; Andrew's own look is the
  managers'-review acceptance. Row `Z-S201` disarms on AC6's literal counts.
