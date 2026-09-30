# AMGT_CORPUS task order -- `CRPS-v-2` -- ROUND 20: the six render outcomes -- a served census over 96 names plus a 5174 walk per outcome

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_CORPUS/decompositions/AMGT_CORPUS_DECOMP.md</decomp_doc>
<owned_cells>CRPS-v-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_CORPUS~2</issued_to>
<issued_by>2.0.0_SA_COO~X</issued_by>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or deploy surface.
comp-iam: DECLARED-NOT-APPLICABLE -- read-only invocations of the deployed /thesis route and the walker's own arm/disarm; no grant moves.
comp-adversary: DECLARED-NOT-APPLICABLE -- a task-order specification.
</preflight>

**You are `0.9.0_WK_AMGT_CORPUS~2`**, slot `~2` of round 20. Serves **FWD-10, FWD-11, FWD-12, FWD-15, FWD-16 and FWD-18**.

## 1. THE CELL -- `CRPS-v-2`

**Where this came from.** Six outcomes in `org/missions/D5/AMGT/AMGT_CORPUS/prd/AMGT_CORPUS_PRD.md` are graded on the whole
fence: the SERVED half (the deployed API `opal-amgt-scoped-api`, its /thesis route) and the PAGE half (what an analyst reads
on the page). Each outcome's DONE WHEN is an analyst reading the page:
- FWD-10 at PRD line 318;
- FWD-11 at `:373`;
- FWD-12 at `:401`;
- FWD-15 at `:428`;
- FWD-16 at `:464`;
- FWD-18 at `:484`.

Read each one with every ADDENDUM and CORRECTION under it.

The served half now reads MET per the verifier's reads: /thesis passes pillars, management, fund/position and terms. The page
half has never been measured. The CTO grades from your file: a served half met with the page unrendered is NOT met.

**RULED -- what you build:** `FWD_EVIDENCE_ROUND20.json` + `.md` in
`org/missions/D5/AMGT/AMGT_CORPUS/deliverables/0.9.0_WK_AMGT_CORPUS~2/`.

1. **SERVED census, per outcome, over the population.**
   - The population is the 96 `security_key`s in
     `org/missions/D5/AMGT/AMGT_CORPUS/deliverables/0.9.0_WK_AMGT_CORPUS~1/MODEL_BLOCK_CENSUS_ROUND17.json` (`rows[*].security_key`,
     `denominator 96`).
   - Invoke /thesis read-only per name the way
     `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~158/capture_lib.py` does (its `_invoke`; used by
     `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round47/checks/vv-4.AC3.py`).
   - Record the deployed function's `CodeSha256`.
   - For each outcome, count the names whose payload carries that outcome's served element: pillars with citation (10);
     the management passage cited (11); the team's cases (12); fund of record + last stated position cited (15); pillars,
     management and cases on the PDF-only names (16, the denominator being the PDF-only names); terms per pillar (18).
   - Round 14's instruments and field names are in
     `org/missions/D5/AMGT/AMGT_CORPUS/deliverables/0.9.0_WK_AMGT_CORPUS~4/FWD_EVIDENCE_ROUND14_SERVED.json`: re-use them where
     they still fit, and name the field you read.
   - A name the route refuses counts in the denominator as not carrying, with its reason in the `.md`.
2. **PAGE walk on the local build.**
   - The main tree is `MAIN="$(git worktree list --porcelain | head -1 | cut -d' ' -f2-)"`. The walker uses the main tree's
     `portal/node_modules` and writes to the main tree's gitignored `tmp/ui-walk/<stamp>/` when run as
     `UI_WALK_ROOT="$MAIN" node "$MAIN/.claude/skills/ui-walk/walk.mjs" ...`.
   - Read `$MAIN/.claude/skills/ui-walk/SKILL.md` first (the safety model).
   - Precondition: `curl -s -o /dev/null -w "%{http_code}" http://localhost:5174/` reads 200. If it does not, file a BLOCKING
     row and stop the page half. Do not start a server.
   - (a) **Signed-out control FIRST:** `--no-login --route /security-analysis --base http://localhost:5174`. It must exit 3 and
     print `WALK VOID`. Record the command, the exit code and that line.
   - (b) **Signed-in walk:** `--route /security-analysis --base http://localhost:5174 --security "IMB LN" --security "AMD US"
     --security "AZN LN" --security "ADBE US" --max-minutes 40`.
     - Run it in the background, logging to `.scratch/v2/walk.log`, and poll in bounded calls (`until grep -qE "^OUT|DISARM"
       .scratch/v2/walk.log; do sleep 15; done` under a 540 s timeout, repeated).
     - Record the `stamp`, the command and the `DISARM ...` line, which must read `REFUSED`.
     - If the walk dies, run `python "$MAIN/.claude/skills/ui-walk/ui_walker_account.py" status`, and `disarm` if it reads
       active.
     - Never run its `secret` command.
   - (c) Per outcome, open the named screenshots with the Read tool and write what the page SHOWS in words (`reads`), then
     `state` met / unmet against the fence. The pages per outcome:

| outcome | security | tab (the walker's shot) | what the fence asks to see |
|---|---|---|---|
| FWD-10 | `IMB LN` (AMD US = ABSENT arm) | Thesis | the team's pillars as bold lead + paragraph, each openable to report and passage, marked as the team's; AMD reads ABSENT with a reason |
| FWD-11 | `IMB LN` (AMD US = ABSENT arm) | Exec Management | the team's management passage, labelled as the team's, BESIDE the filing roster, the roster unchanged |
| FWD-12 | `AZN LN` (IMB LN = ABSENT-with-reason arm) | Model | rows from the typecast + template; the team's Upside / Base / Downside as the team's, cited |
| FWD-15 | `IMB LN` | Posture, and the header posture line | fund of record and last stated position, cited, beside the machine verdict |
| FWD-16 | `ADBE US` (PDF-only; IMB LN = the docx control) | Thesis, Exec Management, Model | pillars, management and cases from the PDF pack |
| FWD-18 | `IMB LN` | Thesis, and the header feed / Chatter | a pillar's terms readable; the feed filterable to them |

3. **Rows (the file's `outcomes`, 6):**
   - `id`, and `fence_quote` (the DONE WHEN text VERBATIM from the PRD);
   - `served` {`instrument`, `numerator`, `denominator` (integers), `excerpt`, `state` met|unmet};
   - `page` {`security`, `tab`, `shot` (the local `tmp/ui-walk/...` path), `reads`, `state` met|unmet|unmeasurable, `reason`
     when unmeasurable};
   - when either half is not met: `owner` (one of AMGT_CORPUS, AMGT_RESAPP, DSGN_AMGTV1; a page defect's owner is
     DSGN_AMGTV1) and `exercising_act` (an act driven on demand, never a wait).

   Top level:
   - `prd`, `run_at`, `population` {`source`, `denominator`}, `deployed_function` {`name`, `code_sha256`};
   - `portal` {`dev_commit` (`git -C "$MAIN/portal" rev-parse HEAD`, named as the working copy), `base`};
   - `signed_out_control` {`command`, `exit_code`, `void_line`}, `walk` {`stamp`, `command`, `disarm_line`}.

## 3. SURFACES

<paths>
org/missions/D5/AMGT/AMGT_CORPUS/deliverables/0.9.0_WK_AMGT_CORPUS~2/FWD_EVIDENCE_ROUND20.json
org/missions/D5/AMGT/AMGT_CORPUS/deliverables/0.9.0_WK_AMGT_CORPUS~2/FWD_EVIDENCE_ROUND20.md
org/missions/D5/AMGT/AMGT_CORPUS/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_CORPUS/task-orders/AMGT_CORPUS.TO-CRPS-v-2.six-render-outcomes-census-and-walk.md
</paths>

- READ-ONLY: every other file in the repository, every S3 object, the portal source.
- The walker's `tmp/ui-walk/` output in the main tree is gitignored and is NEVER committed, copied into the repo or pasted into
  your report. Quote findings in words.
- Scratch `.scratch/v2/`.

Your worktree is a SPARSE cone (`lib integrations .tools .claude org docs rcg infra/logic`); the portal is reached only through
`$MAIN` as above. Never disable the sparse checkout.

## 4. BOUNDS
- Pure ASCII, LF, Python 3.9-compatible. NO vendor call.
- Read-only: no S3 write, no Lambda update, no Terraform, no portal edit, no server start. A function invocation is a read of
  the /thesis route only.
- The walker's own arm/disarm of its dormant account is the only write, and it must end disarmed.
- REFUSE a criterion you cannot satisfy as written, with your measurement. Rows are `AMGT_CORPUS-Z-W2-S<k>` (next free k),
  with `disarm_owner 2.0.0_SA_COO~X`.

## 5. PROOF OF SPEC (each invocation LITERAL, under `timeout 900`; the check files are the issuer's, read-only to you)

<proof_of_spec>
  <criterion id="AC1" cell_refs="CRPS-v-2"><invocation>cd "$(git rev-parse --show-toplevel)" && bash org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round20/v2_AC1.sh</invocation><expect>(?m)^VALID$</expect></criterion>
  <criterion id="AC2" cell_refs="CRPS-v-2"><invocation>cd "$(git rev-parse --show-toplevel)" && bash org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round20/v2_AC2.sh</invocation><expect>v2 fence_quotes_verbatim 6 of 6</expect></criterion>
  <criterion id="AC3" cell_refs="CRPS-v-2"><invocation>cd "$(git rev-parse --show-toplevel)" && bash org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round20/v2_AC3.sh</invocation><expect>(?m)^STATUS: row PRESENT .* status=disabled .* armed=no; SSM ABSENT$</expect></criterion>
</proof_of_spec>

- AC1: the file's structure: 6 of 6 rows with both halves and integer denominators, the signed-out control exited 3 with
  `WALK VOID`, the disarm read `REFUSED`, and the population, deployed code and portal commit named.
- AC2: the fence quotes are verbatim.
- AC3: the bound: the walker account is back at rest.

## 6. WHEN YOU ARE DONE
1. Write the instance at `org/missions/D5/AMGT/AMGT_CORPUS/deliverables/0.9.0_WK_AMGT_CORPUS~2/AMGT_CORPUS.TO-CRPS-v-2.six-render-outcomes-census-and-walk.proof_of_spec.json`.
2. `python .tools/proof-of-spec-check.py <instance> AC1,AC2,AC3 --governing-order <this order>` returns rc 0.
3. Only if every criterion passes, append a new status tag reading complete at the END of this file. Commit the files you
   changed plus the instance (never a screenshot).
4. Report ONCE: each AC line, the deployed CodeSha256, the portal commit, and per outcome served n/N plus page met/unmet with
   owner.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round-19 analysis s.4 cell 2 @`d5d806bc2e`, ruling 2 (round-14 ruling 7's promised re-grade). Dry-run at base
CLOUD `be851f21d2` (worktree `C:/tmp/coox-crps20-issue`):
- v2_AC1 FAIL as expected (`MISSING` evidence file).
- v2_AC2 FAIL as expected (`MISSING`).
- v2_AC3 PASS as expected (bound): `STATUS: row PRESENT opal-ui-walker@opal.test status=disabled role=admin userType=Dev
  armed=no; SSM ABSENT`.

At the cut 5174 answered 200 and portal DEV read `29c8226a`. The walk is a page read, not acceptance evidence on its own; the
CTO grades the page half from it.
<risk>LOCAL</risk>
<status>pending</status>
<round>20</round>
<slot>~2</slot>
<fabric>site-z</fabric>
<status>complete</status>
