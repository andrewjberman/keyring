# TO IRPT_BCKEND.TO-IB-rth-5 -- SESSION-ESTABLISHMENT TOOLING FOR THE RENDER HOST: `render_export.cjs` launches a fresh, non-persistent browser every run and implements no login capability by design, so the render-latency question (row W2-S62) cannot even be attempted past `BLOCKED: SESSION_ABSENT` (row W3-S52). This cell builds the TOOLING to let an operator establish and reuse an authenticated session; it does not, and cannot, complete the MFA login itself -- that is a human act, named but not performed here.

<to_id>IRPT_BCKEND.TO-IB-rth-5</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~5</issued_to>
<issued_by>2.0.0_SA_COO~B</issued_by>
<issued_date>2026-09-21</issued_date>
<status>complete -- flipped by 0.9.0_WK_IRPT_BCKEND~5 2026-09-21, arm (e) deployed and proven. Both never-widen halves SIGNED at packet blob b5fd42fbb54acb53652aacf7caa495b570ce648f (COO commit 3eb7070868/re-sign, CTO commit 67809db530). Change-management ledger org/critical_paths/change_management/20260921T1606Z_irpt-bckend-ib-rth-5-session-tooling-deploy_deploy_completion.md OPENED before deploy, all 3 legs proven, CLOSED. All 4 touched files (render_export.cjs, capture-session.cjs, capture-session.sh, package.json) deployed via git-blob extraction (never a raw disk copy, avoiding this box's core.autocrlf CRLF mangle), verified matching the packet's sha256 table BOTH at S3 (get-object) AND on the running host (SSM sha256sum) -- the stronger read-back proving the instance role actually fetched the bytes; run-export-render.sh correctly skipped (unchanged). Arm (e) synthetic-storageState proof run against the deployed bytes (ssm:91bcd165-9ca0-4fda-9d9f-5b3bbc234482): the new, distinguishing log line 'OK: session state loaded ... attempting session reuse' printed, then the script STILL correctly refused SESSION_ABSENT on the fake session -- no PDF written, no false success claimed anywhere. The synthetic storageState.json was removed from the host afterward, restoring the exact pre-test baseline. Host i-0167fd745ad906a66 confirmed RUNNING throughout and NOT stopped (per this worker's explicit instruction; disposition remains COO/CTO's call). R80-AC1 PASS-by-output (fresh re-run this session, rc=0, token printed). R80-AC2 is a judgment criterion, UNVERIFIABLE-BY-INSTRUMENT, graded at L9 by 3.0.0_SA_CVO, never self-graded -- does not block this flip per this order's own <proof_of_spec> section ("rc 0 AND R80-AC1 PASS-by-output, then flip <status> complete"). proof-of-spec-check rc=0 (VALID). The named human operator (Andrew, or a delegated operator) is still the only one who can complete arm (c)'s runbook (real MFA login, session capture) -- that step is not, and cannot be, performed by any worker or packet in this project.</status>

**Directive:** D9 | **Fabric:** laptop | **Round:** 8 (mid-round addition) | **PRD:** `../prd/IRPT_BCKEND_PRD.md` (no addendum) | **Ruling:** `../../../../tier1_exec/1.0.0_SA_CTO/deliverables/CTO_RULING_IRPT_BCKEND_W2-S62_RTH2_SUBMIT_WIRING_20260921.md` addendum 2 @afc015b4b2 | **Decomp cell:** `IB-rth-5` (`../decompositions/IRPT_BCKEND_DECOMP.md` v0.9, s.R8.6) | **outcome_ref:** FWD-2 (serving half, indirectly -- this cell unblocks rth-2's measurement, it does not itself advance FWD-2) | **row:** IRPT_BCKEND-W3-S52 (informs), IRPT_BCKEND-W2-S62 (the blocker this unblocks)

---

## IDENTITY AND WORKTREE
- **Serial:** `0.9.0_WK_IRPT_BCKEND~5`. Every Bash call begins `export OPAL_AGENT_SERIAL=0.9.0_WK_IRPT_BCKEND~5;`.
- **Worktree:** the issuer creates `/c/tmp/wk-irpt-8-5` on branch `wk-irpt_bckend-8-5`, cut from CLOUD HEAD, `.tools/terraform.exe` provisioned; the issuer passes the absolute path at spawn. First act: `cd` there, `git rev-parse --abbrev-ref HEAD`, `test -d org && test -d .tools && echo TREE-OK`; write `org/mcp/sessions/<CLAUDE_CODE_SESSION_ID>.serial` before any apply. Repo root = the worktree.
- **Commit:** `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~5 <0.9.0_WK_IRPT_BCKEND~5@opal.agent>" -F <msgfile> -- <paths>`, `<msgfile>` by the Write tool. Branch only; never push/merge/rebase/checkout--/clean. Capture safe-commit output to a file; never `| tail`; never with `$( )`. Verify by `git log`.
- Python `py -3.12`; AWS via `.tools/aws`; a recursive grep/find is rail-DENIED -- use Read/Grep, a gated read in its own call.

## THE CELL

- **(a) MEASURE/DESIGN FIRST.** Read `infra/aws/ec2/investor-reporting-export/render_export.cjs` in full (the SESSION_ABSENT branch is around line 143). Read row `IRPT_BCKEND-W3-S52` in `../surprise-channel/investigations/INVESTIGATION_v1.md` for the full prior measurement (host id, SSM document names, how the script is invoked, the vendor-separation guard). Determine the minimal, backward-compatible way to add session reuse: Playwright's `browser.newContext({storageState: <path>})` (load a saved cookie/localStorage snapshot into a fresh context) is the likely fit over `launchPersistentContext` (which persists a whole profile dir) -- pick whichever is simpler and safer given this script's one-shot SSM-invoked CLI model; state your reasoning. **Absence of the storageState file must leave EXACTLY today's behavior unchanged** -- this is an additive branch, not a rewrite of the launch path.

- **(b) THE CODE CHANGE.** Implement the storageState load in `render_export.cjs`, at a declared, stable path (e.g. `/opt/investor-reporting-export/session/storageState.json` -- confirm the host's actual writable, persistent-across-SSM-invocations directory before picking one; do not assume). If the file is present, load it into the new browser context; if absent or invalid (corrupt JSON, expired-looking), fall through to today's fresh-context behavior and the existing `SESSION_ABSENT` refusal -- never a crash, never a silent different failure mode. No change to the vendor-separation guard, the `VENDOR_HOSTS` check, or any other function in the file.

- **(c) THE CAPTURE TOOLING.** Build what an operator needs to actually produce that storageState file, exactly once (then periodically, as sessions expire): a short, exact runbook (not vague) plus, if it reduces operator error, a small helper script. The mechanism is SSM port-forwarding (`aws ssm start-session --target <instance-id> --document-name AWS-StartPortForwardingSession ...`, or the host's existing SSM document set -- check what's already there before inventing a new one) to reach a REAL, visible browser session on the host (Playwright supports launching with `headless: false` plus a forwarded remote-debugging port, or an X11/VNC path if the host has a desktop -- measure what the host actually supports before designing around an assumption), where the operator manually completes the portal login INCLUDING MFA, and a final step captures `context.storageState({ path: ... })` to the declared path. Every step in the runbook names EXACTLY who can do it (an operator holding valid portal credentials -- Andrew or a delegated operator) and exactly what they type/click, because this document IS the interface between the code you write and the human act neither you nor this project performs in software.

- **(d) THE PACKET.** This is a deploy to a production host serving real customer-facing exports -- same discipline as every other served-property change in this project (K-CODE-equivalent for the host script; writers of the property counted -- who else can change what runs on this host; blast radius both branches: what changes in served behavior if a storageState later appears vs. if it never does; rollback = revert the script to its pre-change bytes, verified by re-reading the deployed file). Both never-widen halves (CTO + COO) must SIGN at HEAD naming this packet's blob before any deploy to the host. If you cannot get both halves this pass, that is an honest STOP: commit the packet, leave the order open, report exactly what's owed.

- **(e) IF BOTH HALVES LAND:** deploy the updated `render_export.cjs` to the host (however code currently reaches that host -- measure the existing deploy mechanism, do not invent a new one) under a change-management ledger opened before the deploy. **DO NOT attempt to complete the MFA login yourself, script around it, or synthesize a fake session that would let a self-test claim success dishonestly.** Prove ONLY the code path: with a SYNTHETIC, clearly-fake storageState file (a well-formed but invalid session -- proves the LOAD branch executes and is exercised, not that it authenticates), confirm the script takes the new branch (a different log line / behavior than today's immediate fresh-context path) and still correctly reports a refusal when the fake session doesn't actually authenticate (it should NOT claim success on a synthetic session -- if it does, that is a defect in your own check, not a pass). This is the acceptance bar: the mechanism visibly exists and is wired in, never a claim that a real session was established (that step is the named human's, on their own schedule).

## DELIVERABLE
The `render_export.cjs` source change; the operator runbook (and helper script, if built) for session capture via SSM port-forward + manual MFA login; the never-widen packet + both signed halves; if deployed, the change-management ledger and the synthetic-storageState proof; a result.md naming exactly who needs to complete the human step next and how.

## BOUNDS
- **NOT the non-MFA service-account path.** Reserved to Andrew by the CTO's ruling addendum 2 -- do not investigate it, propose it, or build toward it as an alternative. If you find yourself designing around MFA rather than through it, STOP.
- **No change to `portal/src/contexts/AuthContext*`, `portal/src/App.tsx`, or any portal-side auth source.** This cell's whole surface is the RENDER HOST's own script and its deploy/session-capture tooling -- it never touches how the portal itself authenticates.
- **Never attempt the MFA login yourself, in any automated or scripted form**, including via a captured TOTP secret, a bypass, or an API-level login shortcut. If the runbook's manual step seems avoidable, that avoidance is exactly the boundary this cell must not cross.
- The forward-looking-criterion bar; R-40 (content hash per run/artifact read AT the event); S56 vintage pins `path:line @ <commit-ish>`; the LEDGER opened before any deploy.
- **Surprises:** one row per failed premise / wrong path / absent capability at `../surprise-channel/investigations/INVESTIGATION_v1.md`, id `IRPT_BCKEND-W5-S<k>` continuing above the highest at your HEAD (append INSIDE the first fence's array, PREVAILING EOL, UTF-8 explicit, full ISO `surfaced_at`, `disarm_owner` a SEAT SERIAL when ARMED); then keep working.

<expected_criteria>R80-AC1, R80-AC2</expected_criteria>
<criterion id="R80-AC1" cell_refs="IB-rth-5"><invocation>timeout 1800 py -3.12 org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~5/battery_ib_rth_5.py</invocation><expect>IBR80-STORAGESTATE-LOAD-PATH-WIRED-AND-DISCRIMINATING</expect></criterion>

<placeholders>NONE</placeholders>

<paths>
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-rth-5.session-establishment-tooling-for-the-render-host.md
infra/aws/ec2/investor-reporting-export/
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> v0.9, cell `IB-rth-5` (s.R8.6).
<owned_cells>IB-rth-5</owned_cells>
</decomp_ref>

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- nothing scheduled or fired.
comp-iam: DECLARED-NOT-APPLICABLE at the cut -- the SSM port-forward mechanics and any host-side grant needed for the capture tooling are the worker's arm-(c) design, never assumed at the cut; a new grant is a MEASURED key in the never-widen packet, never assumed.
comp-adversary: DECLARED-NOT-APPLICABLE at the cut; the assignee's instrument at report time.
lane: the `<paths>` block above IS the grant plus the two tree-convention grants (`deliverables/<serial>/`, this order's own face). A path you need that is not listed -- portal auth source explicitly excluded above -- is a BLOCKING row, never an override.
</preflight>

<proof_of_spec>
Criterion ids minted at cut: R80-AC1 (the storageState load branch exists, is wired into the browser-context creation path, and correctly falls through to today's SESSION_ABSENT refusal on a synthetic/invalid session rather than claiming false success), R80-AC2 (judgment, the CVO's at L9 -- whether the runbook is genuinely operator-executable and the packet's blast radius is honest). Instance at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~5/IRPT_BCKEND.TO-IB-rth-5.session-establishment-tooling-for-the-render-host.proof_of_spec.json` per `org/standards/PROOF_OF_SPEC.schema.json`: one acceptance row per id, `criterion_verbatim`, `invocation`, `output_evidence`, `denominator` beside every count, `expect` from this face, the judgment row under `UNVERIFIABLE-BY-INSTRUMENT` naming `3.0.0_SA_CVO`. Validate `py -3.12 .tools/proof-of-spec-check.py <instance> --governing-order <this face path>`; rc 0 AND R80-AC1 PASS-by-output, then flip `<status>` complete. A STOP (halves absent, or the mechanism cannot be built as scoped) leaves the order open with the BLOCKING row + the carry, and is the final report on it -- not a failure, exactly as this project treats every other honest STOP.
</proof_of_spec>
</output>
