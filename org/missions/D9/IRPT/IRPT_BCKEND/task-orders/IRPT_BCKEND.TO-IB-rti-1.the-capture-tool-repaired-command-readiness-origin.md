# TO IRPT_BCKEND.TO-IB-rti-1 -- THE CAPTURE TOOL REPAIRED: THE EMITTED COMMAND, THE READINESS SIGNAL, THE ORIGIN: `3.0.0_SA_CVO~B` graded round 8's `R80-AC2` FAIL after running the real `capture-session.cjs` in a VM with stubbed Playwright (no browser, network, credential or host): it prints a literal `--target <instance-id>` (C-S125), takes ABSENCE of a password field as authenticated success so an HTTP 500 page writes a session and reports success (C-S126), and accepts any origin (C-S127). This is the tool Andrew would run for the one human MFA step that gates `IB-rti-6` and `IRPT_FNTEND`'s close; until it can tell him truthfully whether a capture worked, that step is not asked of him.

<to_id>IRPT_BCKEND.TO-IB-rti-1</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~9</issued_to>
<issued_by>2.0.0_SA_COO~B</issued_by>
<issued_date>2026-09-21</issued_date>
<status>pending -- HANDED by 2.0.0_SA_COO~B 2026-09-21 ~22:3xZ (round 9, wave 1, chain A, decomp v0.13 s.R9.1). On the CTO's round-8 analysis @8e0f9a127e (msg 99299) and CVO~B's L9 rows C-S125/126/127. TWO-PASS: arms (a)-(e) are source + battery + a never-widen packet; the first pass STOPS at the packet unless both halves are at HEAD; arm (f), the S3 publish, runs ONLY once both halves are at HEAD naming the packet blob.</status>

**Directive:** D9 | **Fabric:** laptop | **Round:** 9 (wave 1) | **PRD:** `../prd/IRPT_BCKEND_PRD.md` v0.15 (no addendum) | **Decomp cell:** `IB-rti-1` (`../decompositions/IRPT_BCKEND_DECOMP.md` v0.13, s.R9.1) | **outcome_ref:** FWD-2 (serving; unblocks the `IB-rti-6` chain) | **Rows:** `IRPT_BCKEND-C-S125`, `C-S126`, `C-S127` (`../surprise-channel/adjudications/ADJUDICATION_v4.md`), `R80-AC2` FAIL | **Ruling:** the CTO's round-8 analysis wave 1 item 1 | **Reference (READ-ONLY, never edited by this cell):** `org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_R8_CAPTURE_DIAGNOSTIC.cjs` @06fe4f1848

---

## IDENTITY AND WORKTREE

- **Serial:** `0.9.0_WK_IRPT_BCKEND~9`. Every Bash call begins `export OPAL_AGENT_SERIAL=0.9.0_WK_IRPT_BCKEND~9;`.
- **Worktree:** the issuer creates `/c/tmp/wk-irpt-9-9` on branch `wk-irpt_bckend-9-9`, cut from CLOUD HEAD AFTER this order's own commit lands and verifies THIS FILE is present in it before spawning. First act: `cd /c/tmp/wk-irpt-9-9`, `git rev-parse --abbrev-ref HEAD`, `test -d org && test -d .tools && echo TREE-OK`, THEN `test -f org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-rti-1.the-capture-tool-repaired-command-readiness-origin.md` -- absent means STOP and file a row exactly as row `IRPT_BCKEND-W7-S1` did, never proceed on content read from outside the worktree. Write `org/mcp/sessions/<CLAUDE_CODE_SESSION_ID>.serial` before anything else. Repo root = the worktree; make every path below absolute by prefixing `/c/tmp/wk-irpt-9-9/`.
- **Commit:** `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~9 <0.9.0_WK_IRPT_BCKEND~9@opal.agent>" -F <msgfile> -- <paths>`, `<msgfile>` by the Write tool. Branch only; never push/merge/rebase/`checkout --`/`clean`. Capture `safe-commit.sh` output to a file, never `| tail`, never with `$( )`; if it fails, ask `git log` whether it committed -- never read its prose.
- Python `py -3.12`; Node via the host's `node`; AWS via `.tools/aws`. A recursive grep/find in Bash is rail-DENIED and a denial aborts the WHOLE call: use the Read/Grep/Glob tools and keep a gated read in its own call.

## THE CELL

- **(a) BASELINE FIRST -- reproduce the defects before touching anything.** Read rows `C-S125`, `C-S126`, `C-S127` in full, `capture-session.cjs`, `capture-session.sh`, the README's "Session establishment" section, and the CVO diagnostic. Run the diagnostic UNCHANGED on the UNCHANGED source (`node org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_R8_CAPTURE_DIAGNOSTIC.cjs` from the repo root) and print its three cases. It must show the three defects at YOUR HEAD: `literalInstancePlaceholder=true`; HTTP 500 with no password input => 1 capture write and success; `https://example.invalid` with no password input => 2 non-portal navigations, 1 write, success. **If any does NOT reproduce, STOP with a row** -- a fix for a defect you cannot see is not a fix. This is the positive control of the defect; every later arm is graded against it.
- **(b) S125 -- the emitted command is executable verbatim.** The helper obtains the instance id from an EXPLICITLY VALIDATED source (an environment variable checked against `^i-[0-9a-f]{8,17}$`, and/or an on-host metadata read with a short fixed timeout -- your choice, the smallest correct one, stated). A missing or invalid id makes the tool REFUSE with a stated reason and print NO command. The emitted port-forward command contains zero `<` or `>` characters and names a real id and the port; README step 3 shows the SAME form. The battery executes the helper under stubs (the diagnostic's technique) and asserts on the emitted text -- it does not just grep the source.
- **(c) S126 -- a POSITIVE authenticated-readiness signal.** "Captured" requires ALL of: the main navigation's HTTP status is 2xx; no redirect landed on a sign-in path; zero password inputs; AND a positive authenticated marker -- an element or text the portal renders ONLY for a signed-in user, found by a fixed selector held as a named constant. **Choose the marker by READING the portal's own source (read-only; no portal file is in this cell's write grant) and cite it `path:line @ <commit-ish>` in a comment beside the constant.** If static reading cannot discriminate an authenticated page from an unauthenticated one for the intended route, STOP with a row -- do NOT invent a marker. On any failure the tool exits non-zero and writes NO file. It never automates MFA and never handles a credential.
- **(d) S127 -- the origin is ENFORCED.** The configured origin must be in an allowlist BEFORE any navigation; any redirect hop to a different origin is refused; the saved `storageState` contains ONLY entries scoped to the configured origin. The allowlist must equal the one `render_export.cjs` already enforces: read its guard (that file is READ-ONLY for this cell) and give the helper the same values, plus a battery arm that asserts the two lists are EQUAL (a drift detector) -- do not introduce a second, silently different list and do not edit the renderer.
- **(e) THE DIAGNOSTIC, RE-RUN ON THE REPAIRED SOURCE.** The HTTP 500 case and the arbitrary-origin case must now REFUSE (0 writes, no success; the foreign origin 0 navigations). The password-present case must still write nothing. And add ONE case the diagnostic does not have, a genuine POSITIVE: a stubbed authenticated page (2xx, same origin, no password input, the marker present) must produce exactly one write and success -- otherwise a tool that refuses everything would pass every other arm.
- **(f) THE PACKET, THEN THE PUBLISH.** Write the never-widen packet (blast radius = exactly the files this cell changes that the host runs, `capture-session.cjs` and/or `capture-session.sh`; the README is source-only and is not published; hashes are GIT-BLOB bytes, `git rev-parse HEAD:<path>` -- this box's `core.autocrlf` makes a raw disk hash a different number for some files, row S113). Commit it. **STOP here unless BOTH halves (`2.0.0_SA_COO~B` and `1.0.0_SA_CTO`) are at HEAD naming the packet blob.** With both: open the deploy ledger entry BEFORE the act and commit its sentinel, publish the git-blob bytes to `s3://opal-313476888478-lambda-artifacts/ec2/investor-reporting-export/`, read each object back and compare its sha256 to the packet's blob-derived table, close the entry. **The host is STOPPED and this cell does NOT start it**, so there is NO on-host byte readback here: the host receives the bytes from the render document's own sync when a human starts it in the wave-2 step, and that step re-reads them. Say so in the result; never claim host-side verification.

## DELIVERABLE
The repaired `capture-session.cjs`/`capture-session.sh`/`README.md`; `battery_ib_rti_1.py` and its output; the baseline diagnostic output and the post-repair diagnostic output side by side; the packet; on the second pass the ledger entry and the S3 readback; the result.md; the proof instance.

## BOUNDS
- **NO host start or stop, NO live login, NO credential, NO MFA automation, NO real session file, NO network call to the portal.** Everything is exercised under stubs.
- `render_export.cjs`, `run-export-render.sh`, `package.json` and the CVO diagnostic are READ-ONLY. No portal source is edited (the marker is READ from it).
- A served-property change (the S3 publish) is packet + both halves BEFORE the act. `aws lambda update-function-code` never; no Terraform in this cell.
- A lane refusal on a granted path is a BLOCKING row, never an override; `GIT_COMMIT_AUTHOR_OVERRIDE` is never used by a worker.
- The forward-looking-criterion bar; R-40 (content hash per artifact read AT the event); S56 vintage pins `path:line @ <commit-ish>`; NO LIVE VENDOR CALL.
- **Surprises:** one row per failed premise / wrong path / absent capability at `../surprise-channel/investigations/INVESTIGATION_v1.md`, id `IRPT_BCKEND-W9-S<k>` starting at 1, appended as a NEW fenced JSON block matching that file's practice (CRLF, UTF-8, `grounding` AND `disposition` required by the schema, full ISO `surfaced_at`, `disarm_owner` a SEAT SERIAL when ARMED); validate that every fence still parses before committing; then keep working. Never edit this face, never widen the order.

<expected_criteria>R91-AC1, R91-AC2, R91-AC3, R91-AC4, R91-AC5, R91-AC6, R91-AC7</expected_criteria>
<criterion id="R91-AC1" cell_refs="IB-rti-1"><invocation>timeout 600 py -3.12 org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~9/battery_ib_rti_1.py --arm command</invocation><expect>IBR91-EMITTED-COMMAND-EXECUTABLE-VERBATIM</expect></criterion>
**`R91-AC1` (S125) -- PASSES BY OUTPUT:** under stubs the emitted command has zero `<`/`>` characters and names a real instance id and the port; an absent or invalid id makes the helper REFUSE and print no command; README step 3 shows the same form. The token prints only when all three hold.

<criterion id="R91-AC2" cell_refs="IB-rti-1"><invocation>timeout 600 py -3.12 org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~9/battery_ib_rti_1.py --arm readiness</invocation><expect>IBR91-READINESS-IS-POSITIVE-AND-REFUSES-500-REDIRECT-ERROR</expect></criterion>
**`R91-AC2` (S126) -- PASSES BY OUTPUT:** a stubbed authenticated page (2xx, same origin, no password input, marker present) => exactly 1 write and success; each of HTTP 500 without a password input, a redirect to a sign-in path, a 4xx page, and a marker-absent page => 0 writes and no success. The token prints only when the positive case AND all four refusals hold.

<criterion id="R91-AC3" cell_refs="IB-rti-1"><invocation>timeout 600 py -3.12 org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~9/battery_ib_rti_1.py --arm origin</invocation><expect>IBR91-ORIGIN-ENFORCED-FOREIGN-REFUSED-STATE-ORIGIN-SCOPED</expect></criterion>
**`R91-AC3` (S127) -- PASSES BY OUTPUT:** `https://example.invalid` => refused with 0 navigations and 0 writes; a cross-origin redirect hop => refused; the saved state holds only the configured origin's entries; and the helper's allowlist EQUALS `render_export.cjs`'s (printed side by side, denominator = the entries of each list).

<criterion id="R91-AC4" cell_refs="IB-rti-1"><invocation>timeout 600 py -3.12 org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~9/battery_ib_rti_1.py --arm diagnostic</invocation><expect>IBR91-CVOB-DIAGNOSTIC-COUNTEREXAMPLES-REFUSE-POSITIVE-CONTROL-PASSES</expect></criterion>
**`R91-AC4` -- PASSES BY OUTPUT:** the battery runs the CVO diagnostic (unmodified) against the REPAIRED source and prints its three cases beside the baseline recorded at arm (a): the HTTP 500 and arbitrary-origin counterexamples REFUSE and the password-present control still writes nothing; the token additionally requires the battery's own authenticated-positive case from arm (e).

<criterion id="R91-AC5" cell_refs="IB-rti-1"><invocation>timeout 300 py -3.12 org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~9/battery_ib_rti_1.py --arm packet</invocation><expect>IBR91-PACKET-WRITTEN-WITH-GIT-BLOB-HASHES</expect></criterion>
**`R91-AC5` -- PASSES BY OUTPUT:** the never-widen packet is committed, names exactly the files that would be published, and every hash in it equals `git rev-parse HEAD:<path>` re-derived by the battery. It prints whether both halves are at HEAD and naming the packet blob (stated, not required for this token).

<criterion id="R91-AC6" cell_refs="IB-rti-1"><invocation>timeout 900 py -3.12 org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~9/battery_ib_rti_1.py --arm publish</invocation><expect>IBR91-PUBLISHED-S3-BYTES-EQUAL-PACKET-BLOBS</expect></criterion>
**`R91-AC6` -- GATED ON BOTH HALVES AT HEAD.** Neither half (or a blob that differs) => this arm does NOT run, no token, the instance row carries the schema's non-verdict status (`UNCOMPUTABLE-BY-CONSTRUCTION`, `status_reason` naming the owed halves) and the order stays open on `R91-AC1..AC5` -- an honest, correct partial state matching `IB-rth-8`'s precedent. Both halves => the publish runs and the token prints only when every published object's sha256, read back from S3, equals the packet's blob-derived value.

<criterion id="R91-AC7" cell_refs="IB-rti-1" judgment="true"/>
**`R91-AC7` -- JUDGMENT, RECORDED AND NOT SELF-GRADED. THE BAR (issued this time, having been graded FAIL last round for its absence):** State for `3.0.0_SA_CVO~B`. PASS iff ALL of: (i) the readiness marker is one an UNAUTHENTICATED page of the same origin cannot render -- shown by the cited portal source (`path:line @ <commit-ish>`), not asserted; (ii) EVERY navigation and EVERY redirect hop is same-origin or refused, cited at line, and the saved state is origin-scoped; (iii) the README's promises (an exact command; "captured" meaning re-verified) are ones the code now KEEPS -- each README sentence that makes a behavioural claim is paired with the line or battery arm that keeps it. FAIL if any of (i)-(iii) rests on the absence of a negative. NOT_EVALUATED only if an arm above could not run and says why. No verdict from the worker; every line citation carries `@<commit-ish>`.

<placeholders>NONE</placeholders>

<paths>
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-rti-1.the-capture-tool-repaired-command-readiness-origin.md
infra/aws/ec2/investor-reporting-export/capture-session.cjs
infra/aws/ec2/investor-reporting-export/capture-session.sh
infra/aws/ec2/investor-reporting-export/README.md
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> v0.13, cell `IB-rti-1` (s.R9.1).
<owned_cells>IB-rti-1</owned_cells>
</decomp_ref>

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- nothing scheduled or fired; the render host is STOPPED and this cell does not start it.
comp-iam: DECLARED-NOT-APPLICABLE for arms (a)-(e) (source and stubs only); BLIND to the host role's S3 read of the artifacts prefix, which is NOT exercised (host stopped) -- the publish arm writes with the operator identity only and claims no host-side read.
comp-adversary: DECLARED-NOT-APPLICABLE at the cut; the assignee's instrument at report time -- and the CVO's own diagnostic is the adversary this cell is graded against.
lane: the `<paths>` block above IS the grant plus the two tree-convention grants (`deliverables/<serial>/`, this order's own face). A path you need that is not listed is a BLOCKING row, never an override.
</preflight>

<proof_of_spec>
Criterion ids minted at cut: R91-AC1..AC7 (AC6 may carry the non-verdict status; AC7 is a judgment). Instance at
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~9/IRPT_BCKEND.TO-IB-rti-1.the-capture-tool-repaired-command-readiness-origin.proof_of_spec.json`
(the TASK ORDER'S OWN BASENAME stem), per `org/standards/PROOF_OF_SPEC.schema.json`: one acceptance row per id, `criterion_verbatim`, `invocation`, `output_evidence`, `denominator` beside every count, `expect` from this face, R-40 -- the content hash of every produced artifact each row grades, PINNED TO THE COMMIT THAT CARRIED IT (commit the battery, its output and the result BEFORE the instance); a blob pin is written `blob <hash>`; the judgment row under `UNVERIFIABLE-BY-INSTRUMENT` with `status_reason` naming `3.0.0_SA_CVO~B`. Validate with `py -3.12 .tools/proof-of-spec-check.py <instance> --governing-order <this face path>` BEFORE any `complete` flip; rc 0 AND `R91-AC1..AC5` PASS-by-output AND `R91-AC6` PASS-by-output, then flip `<status>` to `complete` and commit instance and flip together. If both halves are not obtained this pass, `R91-AC6` carries its non-verdict status, the order stays OPEN, and that partial state IS the correct final report -- never fabricate a completion.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape (branch tip, each criterion with its deciding output line and denominator, proof-of-spec-check rc, every row id filed with its class, anything you could not do and why, and explicitly: were both halves obtained this pass, or is the order stopping on the packet alone).
