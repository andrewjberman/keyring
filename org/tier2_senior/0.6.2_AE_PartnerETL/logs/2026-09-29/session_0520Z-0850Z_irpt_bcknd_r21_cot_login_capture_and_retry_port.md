# The cot login script gets a build input it never had, and a retry it was refused twice — 0.6.2_AE_PartnerETL~S

**Date:** 2026-09-29
**Task Order:** IRPT_BCKEND.TO-IB-m21-211 (COMPLETE) + IRPT_BCKEND.TO-IB-m21-212 Part 1 (DIFF READY)
**Status:** COMPLETE for 211; 212 Part 1 COMPLETE and Part 2 BLOCKED-ON-GO
**archetype:** MIXED

---

## Objective

Round 21 workstream ~M, two orders in sequence. TO-IB-m21-211: the cot login box runs
`/opt/bd-cot-auto-login/bd_49f_auto_login.js` but `infra/aws/ec2/bd-cot-auto-login/` held no `.js` at all, so
an S3 -> box redeploy could not reproduce the running script (row `IRPT_BCKEND-S166`). TO-IB-m21-212: that box
has no in-run login retry, so one transient failure froze the COT chain 09-24..09-27 (row `IRPT_BCKEND-S165`).
Both orders were re-shaped mid-session by three issuer amendments and a CTO ruling.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| comp-which | `comp-which "how do I get an exemption from the commit-time LGIC naming gate for a verbatim legacy file"` | WARN | Printed its own NO-CURATED-RULE banner and three sub-band guesses rather than a routing decision. The banner is the useful part: it stopped me treating rank 1 as an answer. |
| comp-find | `comp-find "bd-cot-auto-login" --limit 40` | PASS | DENOMINATOR 575 hits across 205,712 files. Surfaced the canonical S3 deploy path (`s3://opal-313476888478-lambda-artifacts/ec2/bd-cot-auto-login/`) from a 06-26 inbox record — the fact the order asked me to establish. Slow: ~2 min, backgrounded twice. |
| comp-read | `comp-read .tools/safe-commit.sh --for "how the naming limb is invoked, what makes it ENFORCE vs WARN, and every documented bypass"` | PASS | Went straight to the ENFORCE window (`org/mcp/naming-gate.enforce` or `NAMING_GATE_ENFORCE=1`) in one call. |
| comp-read | `comp-read .tools/naming-gate.py --for "per-path exemption, allowlist, verbatim or legacy capture escape"` | PASS | Named `load_legacy_reads` / `legacy_read_ok` / `waivers_for`, which is how I established the waiver is consumed in exactly ONE branch and is structurally unreachable for a NEW literal. That read is what made row S198 a grounded refusal instead of a guess. |
| comp-schedule | `comp-schedule` (cot filter) | SKIPPED | Gated by the comp-tool rail for piping into `grep`. Answered the same question from the EventBridge scheduler directly (`aws scheduler get-schedule --name cot-bd-session-daily-et`). |
| comp-pipescript deployed | — | SKIPPED | No gold/silver/bronze script touched; this order's artifacts are an EC2 login script and its env file. |
| comp-iam | — | SKIPPED | Declared not applicable by both orders' preflight: no policy change. The port keeps the debug S3 prefix VALUE unchanged precisely so the existing PutObject grant still matches. |
| comp-blast | — | SKIPPED | The write surface is one box directory plus `.gitattributes`; blast radius is stated per-key in the diff document's section 8 instead. |

**What worked:** `comp-read --for` on two gate implementations. Both answers were load-bearing: one established
that ENFORCE was a deliberate tracked flip (so not mine to remove), the other that no waiver was reachable (so
the refusal was real). `comp-find`'s printed denominator is what let me assert the S3 deploy source finding as
measured rather than remembered.

**What failed:** nothing returned a wrong answer. `comp-which` had no curated rule for a gate-exemption
question and said so loudly, which is the correct failure.

**Gap found:** no comp-tool answers "what does this commit-time gate refuse, and what is the lawful escape".
I reached it by reading `safe-commit.sh` and `naming-gate.py` directly. Given how much of this session was
spent there, a `comp-gate <path>` that prints which limbs will grade a path and each limb's documented escape
would have saved roughly an hour.

---

## Deployment Sequence

Nothing was deployed. Both orders are pre-deploy by construction: 211 is read-only on the box and in S3, and
212 Part 2 is the deploy and runs only on a written GO. The box was **started** to reach SSM and returns to
stopped by the standing `ec2-auto-shutdown-enforcer`.

| Step | Action | Result |
|------|--------|--------|
| 1 | `aws ec2 start-instances i-0643a5bee8a8feabf` (stopped-when-idle batch runner) | pending -> SSM `PingStatus: Online` |
| 2 | ONE read-only SSM command: `md5sum` + `wc -c` + `gzip -c -n \| base64 -w0` of the running `.js` | CommandId `ea2016dd-1284-4a9e-9322-5497c80dd905`, Status **Success**, ResponseCode 0, stderr empty |
| 3 | Reconstruct the bytes locally and re-verify | md5 `28dd27a054b826cc3a87f6b4498d3b5a`, 35,049 B; `---END---` marker present, so not truncated |
| 4 | Second, independent read: `s3api head-object` on the deploy source | ContentLength 35,049, single-part ETag = the same md5; downloaded and compared byte-for-byte: identical |
| 5 | Commit the capture + read-back JSON + `.gitattributes` | `bda0189898`, `fc609ed209` |
| 6 | `r21_s166_capture.py` | `RUNNING-CAPTURE 28dd27a054b8` rc=0 |
| 7 | proof-of-spec + `<status>complete</status>` | `29a88dd377`, checker **VALID rc=0** |
| 8 | Drain 211 to CLOUD | `9de7952c93` |
| 9 | Build the deployable port from the capture; naming limb on the staged file | `NAMING-GATE: WARN 7 graded` rc=0, **ZERO REFUSE** |
| 10 | Commit + drain 212 Part 1 | `6a0ce7fe65`, `fdf12eadb1`, drained `b07049f44a` + `8b20b75d63` |
| 11 | Part 2 (S3 upload, box deploy, ledger `cot-login-retry-s165-m-20260929`) | NOT STARTED — awaits the GO |

---

## Verification

**211, at CLOUD, blobs read with return codes checked:**

```
infra/aws/ec2/bd-cot-auto-login/bd_49f_auto_login.js.running-capture.txt  35049 B  md5 28dd27a054b8  CR=0
infra/aws/ec2/bd-cot-auto-login/bd_49f_auto_login.js                      40333 B  md5 7d37465ba68e  CR=0
infra/aws/ec2/bd-cot-auto-login/secret-ids.env                             2525 B  md5 8e879af5e8e7  CR=0
```

`r21_s166_capture.py` -> `RUNNING-CAPTURE 28dd27a054b8` rc=0, run **twice**: once in the worktree and again in
the shared tree after the drain. The second run is the one that matters — it is what proves the `-text`
attribute survives a different checkout, which is the whole failure mode amendment 1 was written against.

**Planted mutant (the load-bearing control):** one space appended to the committed capture ->
`NO-CAPTURE: repo md5 0659b4331ba8f538f0f2f17731d78324 / 35050 B, want 28dd27a0... / 35049 B` rc=1; restored
-> PASS. Fired against both the pre-amendment and the amended checker. The order's own recorded base
(file absent) only proves the checker sees a missing path, not wrong bytes at the right path.

**212 Part 1, three instruments, no vendor request anywhere:**

1. **Naming limb** on the staged candidate: `WARN 7 graded` rc=0. The same bytes as a `.js` before the naming
   hunks returned `REFUSE 15 graded` and aborted the commit twice. The 7 are 2 CONFORMANT + 5 RAISE, every
   RAISE a `{x}` placeholder already present in the captured bytes.
2. **Retry loop** lifted verbatim into a local harness, `attemptLogin` stubbed, `setTimeout` recorded not
   awaited: `RETRY-LOOP OK: 7 of 7 arms passed` rc=0 — including the A+B interaction arm (a persist failure
   is retried, not broken on) and the equivalence arm (`BD_MAX_LOGIN_ATTEMPTS=1` = today's single attempt).
3. **The real candidate run**, `BD_PW_PATH` pointed at a stub browser module and a stub `aws` on `PATH`:
   `BD_FIRM_ID` unset -> **rc=3** `FATAL naming` before any secret read; cookie names unset -> **rc=3**;
   all config present -> **rc=2** at the normal secret path with `partner=cot` resolved. The third arm is the
   control: it proves the two new guards do not fire spuriously.

`node --check` OK. 0 CR, 0 non-ASCII. Every hunk applied by a builder that asserts each anchor occurs exactly
once and re-verifies the base md5 first.

---

## Decisions Made

1. **Started the box to do the read, and did not stop it.** The box is a stopped-when-idle batch runner that
   the daily trigger Lambda starts anyway. Before starting it I checked user-data and the trigger Lambda to
   confirm nothing runs the login on boot — so no vendor sign-in could be provoked. I did **not** issue
   `StopInstances`: CLAUDE.md reserves that for human confirmation, and CloudTrail shows a standing
   `ec2-auto-shutdown-enforcer` returns this instance to stopped on its own (it did so on 09-28).
2. **Carried the bytes out through the SSM read itself** (`gzip | base64`, ~17.8 KB of base64, under the
   24,000-char invocation cap) rather than writing SSM output to S3. The order said no upload; the marker
   check proves the stream was not truncated, and the md5 re-verify is the real oracle.
3. **Did not weaken anything to get past the naming limb.** Editing the captured bytes would have broken the
   order's own byte-for-byte criterion; patching the gate to admit my own commit is not this seat's act;
   removing `org/mcp/naming-gate.enforce` would disable a fabric-wide gate that a recorded issuer act turned
   on. Filed row S198 and let the CTO rule, which is what re-shaped both orders.
4. **Used the audited lane override on `.gitattributes`, three times, each stated in its own commit message.**
   The path is lane BASE_EXEC and my serial is not in its permitted_agents, but the issuer put
   `.gitattributes` in both orders' `<paths>` block, and the block IS the write grant. One lane and one path
   per override commit so the whole-staged-set exit covered nothing else. Both the issuer and the CTO were
   told and can revert in their own lane.
5. **Kept 211's capture and 212's port as separate files.** Before amendment 2 they collided: the port at the
   `.js` path made `IBM21-211-AC1` read FAIL, because that checker md5s the WORKING file. I held the port out
   of the tree and raised the sequencing conflict; amendment 2 resolved it by making the capture a `.txt`.
6. **Vendor cookie names are configuration, not a firm lookup.** The registry itself flags the short vendor
   spelling as a REFUSED alias of `49financial`, stating the vendor is `blackdiamond` and the firm is not —
   so routing a vendor cookie name through a firm builder would assert something the registry denies.
7. **Included two hunks the orders did not literally ask for, each named and strikeable.** C6 removes a
   *second* `|| '49f'` default in `getOtpCode` that the limb does not even grade (it hides inside a template
   placeholder); C7 fixes the header comment that described the default C1 removed.

---

## Files Modified

| File | Commit | What |
|------|--------|------|
| `infra/aws/ec2/bd-cot-auto-login/bd_49f_auto_login.js.running-capture.txt` | `fc609ed209` | the running bytes, verbatim (35,049 B) |
| `org/tier2_senior/0.6.2_AE_PartnerETL/deliverables/IRPT_BCKEND_R21_S166_RUNNING_VS_REPO_20260929.json` | `fc609ed209` | read-back JSON; AC1 re-queries its `command_id` live |
| `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.6.2_AE_PartnerETL~S/IRPT_BCKEND.TO-IB-m21-211....proof_of_spec.json` | `29a88dd377` | instance, VALID rc=0 |
| `org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-m21-211....md` | `29a88dd377` | `<status>` -> complete |
| `infra/aws/ec2/bd-cot-auto-login/bd_49f_auto_login.js` | `6a0ce7fe65` | the deployable port (retry + F2 + naming), 40,333 B |
| `infra/aws/ec2/bd-cot-auto-login/secret-ids.env` | `6a0ce7fe65`, `fdf12eadb1` | 3 required config lines; normalized to LF |
| `org/tier2_senior/0.6.2_AE_PartnerETL/deliverables/IRPT_BCKEND_R21_S165_PORT_DIFF_20260929.md` | `6a0ce7fe65`, `fdf12eadb1` | the Part 1 diff document (29,817 B) |
| `.gitattributes` | `bda0189898`, `626033ace0`, `2a4c589512` | `*.js -text`, `*.running-capture.txt -text`, `*.env text eol=lf`, then a bare-CR repair |
| `org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md` | `036fa7193b`, `cb1c14472a` | rows S198 and S199 |

**Drains to CLOUD:** `9de7952c93` (211), `b07049f44a` + `8b20b75d63` (212 Part 1).
**Push state:** LOCAL. `origin/CLOUD` read `15655f4a25` by `git ls-remote` at 08:5xZ; local CLOUD is ahead.
Tier-2 seats commit and do not push shared branches.

---

## Blockers

**TO-IB-m21-212 Part 2 — BLOCKED-ON-GO, which is the order's own two-stop design, not a fault.** It runs only
on `2.0.0_SA_COO~M`'s written GO naming my diff commit and `1.0.0_SA_CTO`'s read (amendment 2). Both were sent
the DIFF READY at 08:4xZ (ids 102672 / 102673). Nothing else in this lane is waiting on anything.

Not a blocker, recorded: `AUTH_SELFHEAL.TO-A1` is addressed to the bare base `0.6.2_AE_PartnerETL`, a
different project, and the spawn message says so explicitly. It is not this lane's work.

---

## Current State

211 is closed and drained. 212's deployable script, its env lines and its diff document are on CLOUD and the
naming limb passes them with no waiver and no override — the thing the CTO's ruling required and the reason
the order was re-shaped twice. Row S198 is ruled. Row S199 is ARMED and disarms at Part 2's V1 read (running
md5 = the committed port). The worktree `wk-irpt-m21-s-211` is kept deliberately, clean of this order's paths,
because Part 2's deploy ledger has to sit on a worker branch until its own drain.

One thing a later reader should not have to rediscover: the naming limb has no builder-call escape for
JavaScript (`js_literals` grades every string literal on an added line; `py_literals` skips literals inside
`key`/`address`/`name`/`lookup`). Any future `.js` in a firm-scoped tree has to keep firm names out of the
file entirely, and `secret-ids.env` is the only box-side carrier in this tree that the limb does not grade.

---

## Next Steps

1. **[2.0.0_SA_COO~M]** Issue the Part 2 GO naming diff commit `fdf12eadb1` and the CTO's read, or return the
   diff with changes. Section 5a of the diff document is a measured Part 2 precondition.
2. **[1.0.0_SA_CTO]** Read the diff (ruling S198). Section 2 carries the reasoning; hunk C6 is strikeable on
   its own if the extra naming fix is unwanted.
3. **[0.6.2_AE_PartnerETL~S, me]** On the GO: open ledger `cot-login-retry-s165-m-20260929`, deploy **both**
   the `.js` and `secret-ids.env` (the coupling is stated in section 5), close V1 on the SSM read-back, close
   V2 on the next scheduled `opal-cot-bd-session-fetch` Success (cron 07:30 America/New_York), then close the
   ledger and disarm S199. Confirm the uploaded env file has 0 CR bytes before leg A1.
4. **[1.0.0_SA_CTO]** Optional, from the S198 evidence: `naming-gate.py` `judge()` gives RAISE literals a
   carried-at-HEAD escape citing CLAUDE.md Rule 30 and gives the hand-kept-carrier branch none. That asymmetry
   is why a byte-exact capture of an existing pipeline's script could not be committed as a `.js` at all.
