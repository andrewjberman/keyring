# TO NFRA_OPLGTW.TO-OG-r-1 -- the first release: the integrated build, the OAuth cutover, the Schwab flag off

<to_id>NFRA_OPLGTW.TO-OG-r-1</to_id>
<project>NFRA_OPLGTW</project>
<issued_to>0.9.0_WK_NFRA_OPLGTW~2</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<issued_date>2026-09-15</issued_date>
<status>pending</status>

**Directive:** D9 | **Fabric:** laptop | **PRD:** `org/missions/D9/NFRA/NFRA_OPLGTW/prd/NFRA_OPLGTW_PRD.md` v0.2 @f0aa50dbc0 (ADMITTED) | **Contract:** `org/standards/NFRA_OPLGTW_CONTRACT.json` v1.0 | **Decomp cell:** `OG-r-1` | **outcome_ref:** FWD-1, FWD-7, FWD-8 | **depends_on:** `OG-p-1`, `OG-i-1`, `OG-i-2`, `OG-v-2` (and notice N-1 before the spawn) | **slot:** ~2, queue position 2

---

## WORKER FACE

### THE CELL

`OG-r-1` -- **the first release.** Deploy the integrated Gateway build at your worktree's base (every Gateway code cell
merged, the local acceptance run `OG-v-2` all PASS) through `infra/aws/ec2/safe-ec2-deploy.sh`, with the Schwab
integration's enablement OFF and no principal profile active. This release carries the OAuth cutover the PRD requires.

The PRD, verbatim:
- *"Legacy refresh tokens cannot be safely upgraded without a new authenticated connection. Cutover rejects them with
  invalid_grant, preserves registered Code client callbacks, and tells existing users to reconnect once."*
- *"Feature flag defaults off and new grants default pending. Before rollout, record existing Gateway release/config
  digests and client journeys. Enable a controlled identity first, then the approved employee profile. Rollback disables
  the integration and keeps the restricted-profile denial and durable token revocation shim active; do not roll back to a
  binary that reopens the email-only path or accepts legacy refresh tokens."*
- *"Pin Terraform, dependency lock and EC2 release artifacts using the existing Gateway release manifest/process. Measure
  declared/deployed parity on-instance via the normal SSM inspection."*

The baselines you compare against are `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~2/BASELINE.json`
(your own queue's first cell, `OG-p-1`: parity method, error baseline, client inventory). The table and the reader roles
are live (`OG-i-1`, `OG-i-2`); `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~1/SCHWAB_IDENTITIES.json`
names them. `OG-r-1` also sets the environment variable `SCHWAB_ACCOUNT_REF_SECRET_ID` in the release configuration
to that secret's name, read from `SCHWAB_IDENTITIES.json` and never typed (amended before hand-off by
`2.0.0_SA_COO~O`, on row `NFRA_OPLGTW-W3-S25`). Unset, `OG-z-3`'s `app/account_ref.py` answers `UNAVAILABLE` for
every account reference, so no Schwab account is presentable even under a later grant. The runbook's rollback section (`infra/aws/ec2/opal-gateway/runbooks/SCHWAB_PILOT_RUNBOOK.md`, `OG-o-2`) is
what AC10 checks the recorded previous release against.

**You do not enable anything.** No Schwab tool is reachable after this release, for any principal. Enabling a controlled
identity is a later act, under gate G-C.

**The authority check before the deploy (amended before hand-off, on `1.0.0_SA_CTO`'s ruling msg 97114; rows
`NFRA_OPLGTW-W3-S9` and `NFRA_OPLGTW-S8`).** The pre-existing tier, per-identity tool allowlist and integration
min-tier gate still resolve by email; re-keying them is a round-2 cell. This release ships in round 1 only if:
- the Schwab data path's authority is the tid/oid-keyed grant (`OG-z-1`), and
- the email-keyed min-tier gate can only ADD a restriction, never grant alone.
AC11 proves it on your release base, locally, BEFORE the deploy. Run it with the Schwab integration enabled in the
probe's own process only, against emulated AWS. An identity carrying a predecessor's email and that email's tier,
but no tid/oid grant, is denied every Schwab tool; the same request under an active tid/oid grant is allowed. If AC11
fails, nothing deploys: file a BLOCKING row and stop.

**The browser-login withholding (amended before hand-off, on `1.0.0_SA_CTO`'s ruling msg 97251; row
`NFRA_OPLGTW-W3-S22`).** Five browser routes (`/login` and the four `/sprint` paths) and the legacy-consent branch of
`/callback` still authorize by the ALB login email, not by tid/oid; closing that is a round-2 cell. So in this
release, no principal whose email can complete the ALB browser login (the Entra app's assignment) holds a restricted
profile. AC12 prints the set of principals holding a restricted profile at release and, for each, whether its email
can complete that login. Every one that can is withheld, so the printed count is 0.

**THE HALT-GATE IDENTITY FIX (granted on the re-hand; row `NFRA_OPLGTW-W2-S5`, which you filed and which is
correct).** `1.0.0_SA_CTO` ruling R-53 (msg 97843 @e5b20926ff) GRANTS `infra/aws/ec2/safe-ec2-deploy.sh` to this
order **for the identity-resolution lines ONLY** -- any other change to that file is a fresh call -- and CORRECTS
the one-line fix this issuer proposed, which was wrong two files away:
- `.tools/halt-gate-check.sh:71-77` ALREADY loops over TWO sessions directories (`repo_root`'s, then
  `HALT_GATE_SHARED_ROOT`'s) and its own comment names this exact case. `safe-ec2-deploy.sh:41` collapses
  `repo_root` ONTO the shared root, so both iterations read the same directory and your worktree is never
  consulted. A two-place lookup defeated by a caller that pre-set both places to one place.
- The wrapper's `:25-30` comment justifies the redirect as fixing the worktree serial-unresolved failure. That was
  TRUE and is NOW FALSE: the gate's own repair is dated 2026-09-15. **The workaround outlived its bug and became
  the bug**, invisible because its comment still reads as a correct explanation.
- A BARE `--show-toplevel` FLIP IS UNSAFE. `halt-gate-check.sh:56-57` also roots `HALT_GATE_CONTEXT_FILE`
  (`.comp-graph/.agent_context`) and `HALT_GATE_AUDIT_LOG` (`org/halt-gate-override-audit.log`) at
  `HALT_GATE_REPO_ROOT`, single-place with no fallback. A bare flip would point the OVERRIDE AUDIT TRAIL at a
  worktree deleted at drain, and a main-tree control passes straight through that.

**THE GRANTED EDIT, BOTH HALVES OR NEITHER** (R-53): (1) `HALT_GATE_REPO_ROOT` = the CALLING worktree via
`git rev-parse --show-toplevel`; (2) `HALT_GATE_CONTEXT_FILE` and `HALT_GATE_AUDIT_LOG` EXPLICITLY pinned to
`$MAIN_TREE`; (3) the `:25-30` comment rewritten, not left standing. AC15-AC18 grade it, and **AC18 is the arm
this issuer's own control set could not produce** -- it is the one that keeps the override audit trail in the main
tree. Then continue the deploy: AC2 and everything downstream are unblocked by this fix.

**THE THREE OPEN FAILS, RULED (R-56, msg 97864 @853a37edd1). Read this before touching anything.**

**(a) THE LEDGER DISAGREES WITH ITSELF -- fix it THROUGH THE TOOL ONLY.** `deploy_ledger.py check` reads
**DRIFT-DANGEROUS**: this entry says terminal (`CLOSED -- nothing stranded`) while legs `L1`, `L2` and `L3` carry
NO proof, and it still reads OPEN stranded on those three. The tool's own words: *a NEVER#6 bypass wearing a
compliance mask; the .md is a RENDERING of the sentinel -- never hand-edit it.* Record per-leg proof with
`py -3.12 .tools/deploy_ledger.py close-leg` for each of L1, L2 and L3 from the evidence you already gathered --
for the baked asset that is the ON-HOST md5 of the RUNNING path, never an S3 ETag, per the tool's own leg-kind
rule -- then `close` through the tool. **A HAND-EDIT OF EITHER FILE MAKES RECORD AND SENTINEL AGREE BY FIAT,
WHICH IS THE DEFECT RATHER THAN ITS REPAIR.** AC20 grades this.

**(b) THE ROLLBACK TARGET WOULD REMOVE THE ENTITLEMENT GUARD, and the replacement needs TWO properties.** Row
`W2-S7` is verified at the bytes by `1.0.0_SA_CTO` with a positive control: at
`infra/aws/ec2/opal-gateway/app/`, commit `7bd89b5d71` (the runbook s7.2 target) has `data_entitlement.py`
ABSENT while `revocation.py` and `identity_scope.py` are PRESENT; HEAD has all three. **A commit that merely
carries the guard is NOT enough**: the guard entered at `d88cd32d0c`, whose own subject ends "-- not deployed",
and *a rollback target that was never deployed is not a rollback -- it is an untested forward deploy performed
during an incident.* So the replacement must (i) carry `app/data_entitlement.py` AND (ii) be a state actually
DEPLOYED and PROVEN on the host, with that proof cited. **IF NO SUCH COMMIT EXISTS, THAT IS THE FINDING: this
release has NO VALID ROLLBACK, and s7.2 must say so IN THOSE WORDS** rather than name a target that cannot
serve. AC19 grades it either way, and the census that decides it prints its denominator.

**(c) AC4 STAYS FAILED AS WRITTEN. Do not re-cut it and do not fix the class here.** The nine CRLF files are
enumerated and CARDED with their "no functional break found" basis (row `W2-S8`). R-56 REFUSED both the
`.gitattributes` class fix and the normalised re-cut: those eight extensions cover a large fraction of the repo,
so an `eol=lf` rule renormalises every matching file while five seats and multiple workers hold live linked
worktrees -- a diff storm with an unprinted blast radius -- and `.gitattributes` is gate-adjacent
(`LGIC_ENFORCE` S42: a one-line entry VOIDS THE NAMING GATE AT ANY SETTING). **AN ACCEPTANCE CRITERION IS NOT
RE-CUT TO FIT A RESULT IT CORRECTLY REFUSED.** The class fix becomes its own act with its own printed blast
radius, in daylight, and is NOT this cell's.

**(d) AC9 IS GRADED NOT-EVALUATED** with its reason recorded: `OG-p-1`'s baseline never captured an error count
for the stated window, so there is no referent. A PASS would be vacuous and a FAIL would measure the wrong
thing. Record it that way in the proof instance; do not manufacture a verdict.

**Read:** the PRD's "C1", "C6" and "Operator journey, audit and release"; `infra/aws/ec2/safe-ec2-deploy.sh` and
`infra/aws/ec2/opal-gateway/deploy-to-ec2.sh` (the release process); `infra/aws/ec2/EC2_MANIFEST.json`; the baseline.

**The probe** for every criterion is `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~2/probes/og_r1.py`,
taking the short id, printing its measurement with vintage and denominator, then exactly one line
`VERDICT: PASS-OGR1-AC<n>` or `VERDICT: FAIL-OGR1-AC<n> <reason>`.

### ACCEPTANCE

<placeholders>WS</placeholders>

<criterion id="OGR1-AC1" cell_refs="OG-r-1"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~2/probes/og_r1.py AC1</invocation><expect>(?m)^VERDICT: PASS-OGR1-AC1(?![0-9])</expect></criterion>
`OGR1-AC1` -- the ledger entry is opened and its sentinel committed before the deploy.

<criterion id="OGR1-AC2" cell_refs="OG-r-1"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~2/probes/og_r1.py AC2</invocation><expect>(?m)^VERDICT: PASS-OGR1-AC2(?![0-9])</expect></criterion>
`OGR1-AC2` -- the deploy runs through `infra/aws/ec2/safe-ec2-deploy.sh` with the Schwab feature flag off.

<criterion id="OGR1-AC3" cell_refs="OG-r-1"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~2/probes/og_r1.py AC3</invocation><expect>(?m)^VERDICT: PASS-OGR1-AC3(?![0-9])</expect></criterion>
`OGR1-AC3` -- no principal profile is active in the state store after the deploy.

<criterion id="OGR1-AC4" cell_refs="OG-r-1"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~2/probes/og_r1.py AC4</invocation><expect>(?m)^VERDICT: PASS-OGR1-AC4(?![0-9])</expect></criterion>
`OGR1-AC4` -- on the host, every deployed file's digest equals the build input's, file by file, denominator printed.

<criterion id="OGR1-AC5" cell_refs="OG-r-1"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~2/probes/og_r1.py AC5</invocation><expect>(?m)^VERDICT: PASS-OGR1-AC5(?![0-9])</expect></criterion>
`OGR1-AC5` -- an unauthenticated `/mcp` returns 401 with the advertised resource challenge (asserted, not printed).

<criterion id="OGR1-AC6" cell_refs="OG-r-1"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~2/probes/og_r1.py AC6</invocation><expect>(?m)^VERDICT: PASS-OGR1-AC6(?![0-9])</expect></criterion>
`OGR1-AC6` -- the discovery metadata advertises exactly the resource, issuer, endpoints, scope and S256 behaviour the running configuration enforces.

<criterion id="OGR1-AC7" cell_refs="OG-r-1"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~2/probes/og_r1.py AC7</invocation><expect>(?m)^VERDICT: PASS-OGR1-AC7(?![0-9])</expect></criterion>
`OGR1-AC7` -- on the host, the registry loaded with the live configuration enumerates zero Schwab tools.

<criterion id="OGR1-AC8" cell_refs="OG-r-1"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~2/probes/og_r1.py AC8</invocation><expect>(?m)^VERDICT: PASS-OGR1-AC8(?![0-9])</expect></criterion>
`OGR1-AC8` -- the ledger entry is closed and committed before the grading reads.

<criterion id="OGR1-AC9" cell_refs="OG-r-1"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~2/probes/og_r1.py AC9</invocation><expect>(?m)^VERDICT: PASS-OGR1-AC9(?![0-9])</expect></criterion>
`OGR1-AC9` -- the Gateway's error count over the first stated window after the deploy does not exceed `OG-p-1`'s baseline for the same window length.

<criterion id="OGR1-AC10" cell_refs="OG-r-1"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~2/probes/og_r1.py AC10</invocation><expect>(?m)^VERDICT: PASS-OGR1-AC10(?![0-9])</expect></criterion>
`OGR1-AC10` -- the previous release artifact is recorded and restorable by the runbook's rollback section, and its CONTENT HASH is recorded beside its identity at the moment the record is written (`git hash-object` for a tracked file, the packaging tool's own digest otherwise), so a later artifact at the same path FAILS this criterion instead of silently satisfying it; the probe prints the recorded hash and the hash it reads back (R-40).

<criterion id="OGR1-AC11" cell_refs="OG-r-1"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~2/probes/og_r1.py AC11</invocation><expect>(?m)^VERDICT: PASS-OGR1-AC11(?![0-9])</expect></criterion>
`OGR1-AC11` -- (difference) on the release base, locally and before the deploy, an identity carrying a predecessor's email and tier but no tid/oid grant is denied every Schwab tool, while the same request under an active tid/oid grant is allowed; the Schwab tool count is printed.

<criterion id="OGR1-AC12" cell_refs="OG-r-1"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~2/probes/og_r1.py AC12</invocation><expect>(?m)^VERDICT: PASS-OGR1-AC12(?![0-9])</expect></criterion>
`OGR1-AC12` -- at release, the set of principals holding a restricted profile is printed and, for each, whether its email can complete the ALB browser login (the Entra app's assignment); the count of principals that hold a restricted profile AND can complete that login is 0.

<criterion id="OGR1-AC13" cell_refs="OG-r-1"><invocation>cd <WS> && timeout 300 .venv-og/Scripts/python org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~2/probes/og_r1.py AC13</invocation><expect>(?m)^VERDICT: PASS-OGR1-AC13(?![0-9])</expect></criterion>
`OGR1-AC13` -- (difference, live) from the Gateway host through the released build, an assume of EACH renamed reader role (`gateway-schwab-read-role`, `gateway-schwab-catalog-read-role`) succeeds with that role's re-keyed ExternalId while the same assume with the OTHER role's ExternalId is denied, the denominator 2 of 2 roles printed and no ExternalId value in the evidence.

<criterion id="OGR1-AC14" cell_refs="OG-r-1"><invocation>cd <WS> && timeout 300 .venv-og/Scripts/python org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~2/probes/og_r1.py AC14</invocation><expect>(?m)^VERDICT: PASS-OGR1-AC14(?![0-9])</expect></criterion>
`OGR1-AC14` -- (mutant control for AC13) with the assume call site disabled in a scratch copy of the released build, AC13's success arm FAILS, and the probe prints both outcomes and leaves no tracked file modified.

<criterion id="OGR1-AC15" cell_refs="OG-r-1"><invocation>cd <WS> && timeout 300 .venv-og/Scripts/python org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~2/probes/og_r1.py AC15</invocation><expect>(?m)^VERDICT: PASS-OGR1-AC15(?![0-9])</expect></criterion>
`OGR1-AC15` -- from THIS worktree, `safe-ec2-deploy.sh`'s halt-gate root resolves to the CALLING worktree (`git rev-parse --show-toplevel`) and the gate RESOLVES this worker's own session serial, printing the resolved serial path and the serial it read.

<criterion id="OGR1-AC16" cell_refs="OG-r-1"><invocation>cd <WS> && timeout 300 .venv-og/Scripts/python org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~2/probes/og_r1.py AC16</invocation><expect>(?m)^VERDICT: PASS-OGR1-AC16(?![0-9])</expect></criterion>
`OGR1-AC16` -- (positive control for every OTHER caller) invoked from the MAIN tree, the same script resolves the main tree's own serial exactly as it does today, printing both the pre-edit and post-edit resolved paths as equal; a fix that serves only workers FAILS this criterion.

<criterion id="OGR1-AC17" cell_refs="OG-r-1"><invocation>cd <WS> && timeout 420 .venv-og/Scripts/python org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~2/probes/og_r1.py AC17</invocation><expect>(?m)^VERDICT: PASS-OGR1-AC17(?![0-9])</expect></criterion>
`OGR1-AC17` -- (mutant control) with the main-tree override restored in a scratch copy, AC15 FAILS there while AC16 still passes; the probe prints both outcomes and leaves no tracked file modified.

<criterion id="OGR1-AC18" cell_refs="OG-r-1"><invocation>cd <WS> && timeout 300 .venv-og/Scripts/python org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~2/probes/og_r1.py AC18</invocation><expect>(?m)^VERDICT: PASS-OGR1-AC18(?![0-9])</expect></criterion>
`OGR1-AC18` -- (the arm that protects the audit trail) from THIS worktree, `HALT_GATE_AUDIT_LOG` and `HALT_GATE_CONTEXT_FILE` still resolve UNDER THE MAIN TREE, both absolute paths echoed; a fix that moved either into a worktree deleted at drain FAILS this criterion even though AC15 and AC16 would pass.

<criterion id="OGR1-AC19" cell_refs="OG-r-1"><invocation>cd <WS> && timeout 300 .venv-og/Scripts/python org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~2/probes/og_r1.py AC19</invocation><expect>(?m)^VERDICT: PASS-OGR1-AC19(?![0-9])</expect></criterion>
`OGR1-AC19` -- the runbook's s7.2 rollback target EITHER names a commit that (i) carries `infra/aws/ec2/opal-gateway/app/data_entitlement.py` and (ii) is a state PROVEN DEPLOYED on the host, with that proof cited, OR states in those words that this release has NO VALID ROLLBACK; the probe prints the candidate census with its DENOMINATOR (every commit considered, and for each whether the guard is present and whether it was ever deployed) so the conclusion is a subtraction rather than a choice.

<criterion id="OGR1-AC20" cell_refs="OG-r-1"><invocation>cd <WS> && timeout 300 .venv-og/Scripts/python org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~2/probes/og_r1.py AC20</invocation><expect>(?m)^VERDICT: PASS-OGR1-AC20(?![0-9])</expect></criterion>
`OGR1-AC20` -- `py -3.12 .tools/deploy_ledger.py check` prints NEITHER `DRIFT-DANGEROUS` NOR `OPEN` for slug `nfra-oplgtw-og-r-1-first-release`, every leg carrying its proof; the probe quotes the tool's own lines, and a `git diff` of the sentinel and the record over this pass shows ONLY tool-authored changes -- any hand-edit of either file FAILS this criterion.

<expected_criteria>OGR1-AC1, OGR1-AC2, OGR1-AC3, OGR1-AC4, OGR1-AC5, OGR1-AC6, OGR1-AC7, OGR1-AC8, OGR1-AC9, OGR1-AC10, OGR1-AC11, OGR1-AC12, OGR1-AC13, OGR1-AC14, OGR1-AC15, OGR1-AC16, OGR1-AC17, OGR1-AC18, OGR1-AC19, OGR1-AC20</expected_criteria>

`<WS>` is your worktree's absolute path, given in your identity line.

## BOUNDS

- **Grant.** Your write surface is the `<paths>` block below, plus `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~2/` and this order's own file (for the `<status>` flip). Nothing else. A path you need that is not named is a BLOCKING surprise row on that criterion -- never an override.
- **Branch.** You work in the worktree named in your identity line, cut from `CLOUD` at hand-off, after every Gateway code cell and `OG-v-2` merged. Deploy exactly that base. Never push, merge, rebase, `checkout --` or `clean`.
- **Interpreter.** Your venv `.venv-og` (`cd <WS> && py -3.12 -m venv --system-site-packages .venv-og && .venv-og/Scripts/python -m pip install -r infra/aws/ec2/opal-gateway/requirements.txt msal moto pytest`) serves every invocation. Never commit `.venv-og/` or `.scratch/`.
- **Deploy discipline (spine L7).** Open the entry with `py -3.12 .tools/deploy_ledger.py open --slug nfra-oplgtw-og-r-1-first-release ...` and COMMIT its sentinel `org/critical_paths/.open_deploys/nfra-oplgtw-og-r-1-first-release.json` and entry BEFORE the deploy; close the legs and the entry and COMMIT BEFORE the grading reads. NEVER leave the deploy half-landed: finish it in-session, or roll back by the runbook and file an ARMED row naming yourself as disarm owner.
- **The Gateway only through `infra/aws/ec2/safe-ec2-deploy.sh`.** No hand copy, no direct SSM install, no `aws lambda update-function-code`, no Terraform in this cell.
- **Nothing enabled.** The Schwab integration stays disabled and no profile is activated. No grant for any person. AC11's local arm enables the integration in the probe's own process only, against emulated AWS; it reaches neither the host nor the live state store.
- **No egress off Opal infrastructure.** Unauthenticated GETs to `https://mcp.opalinvest.dev` are Opal infrastructure; no call to Claude, Anthropic, an interactive Entra sign-in or any vendor API. You do not reconnect any client.
- **No secret in evidence.** No token or secret value enters a committed file.
- **`mcp==1.28.0` is not raised.**
- **Commits.** `.tools/safe-commit.sh` under your serial; every `.py` you touch passes `.tools/commit-gate.sh`.
- **Spec frozen; REFUSE what you cannot meet as written.** A criterion you cannot satisfy as written is refused and reported with its measurement -- never repaired, widened or satisfied by a route this order does not name. Anything off-spec is one surprise row, and you keep working.
- **Surprises** go to `org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md` as ONE row each, id `NFRA_OPLGTW-W2-S<k>`. Keep working after filing.
- **The preloaded context.** Judge from the files this order names, and cite them, never the preloaded text.
- **Numbers** in this order are context, never acceptance values, except where a criterion prints one.

<paths>
infra/aws/ec2/EC2_MANIFEST.json
infra/aws/ec2/safe-ec2-deploy.sh
infra/aws/ec2/opal-gateway/runbooks/SCHWAB_PILOT_RUNBOOK.md
org/critical_paths/change_management/
org/critical_paths/.open_deploys/nfra-oplgtw-og-r-1-first-release.json
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc> v1 @8768f46770, cell `OG-r-1`, round 1 (section 3, S9; section 6 N-1).
<owned_cells>OG-r-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `OGR1-AC1` .. `OGR1-AC20` (20). Instance at
`org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~2/NFRA_OPLGTW.TO-OG-r-1.first-release-cutover.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`, spec_ref.doc the PRD @f0aa50dbc0, decomp_ref.doc the
decomposition @8768f46770, decomp_ref.to_ref this order's path), validated with
`py -3.12 .tools/proof-of-spec-check.py <instance> OGR1-AC1,OGR1-AC2,OGR1-AC3,OGR1-AC4,OGR1-AC5,OGR1-AC6,OGR1-AC7,OGR1-AC8,OGR1-AC9,OGR1-AC10,OGR1-AC11,OGR1-AC12,OGR1-AC13,OGR1-AC14,OGR1-AC15,OGR1-AC16,OGR1-AC17,OGR1-AC18,OGR1-AC19,OGR1-AC20`
BEFORE the `complete` flip. Result file `first-release-cutover.result.md` beside it. **Flip `complete` only when every
MECHANICAL criterion PASSES by output.**
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape. You cannot send or receive messages; anything you would ask is a surprise row.

---

## RECORD FACE

<preflight>
comp-schedule: RUN at L5 -- --budget 540, 5 of 5 carriers scanned (C1 230, C2 8, C3 12, C4 21, C5 334), 27 gates armed, none naming NFRA_OPLGTW. Binding on this cell: the no-half-landed-deploy moratorium. Notice N-1 (the cutover's client inventory to 0.0.0_AB_MSTR and 1.0.0_SA_CTO) precedes the spawn; it is a notice, not a gate.
comp-iam: RUN at L5 -- comp-iam service opal-gateway, DESIRED plane, 473 .tf files scanned, 3 operations all UNRESOLVABLE-RESOURCE, 27 policy blocks NOT ATTACHED, 2 deny statements unparsed. This release is the first time the Gateway's code carries the new operations (DynamoDB, sts:AssumeRole twice); the instance records the lens re-run over the released source.
comp-adversary: RUN at L5 on the PRD v0.2 (@f0aa50dbc0) -- 4 of 4 cited commits verified; 7 cited paths, 6 stable, 1 GONE (an external RFC URL parsed as a repo path). Blindness stated: T11, filesystem adjacency stands as its neighborhood. comp-blast (L4, EC2, 47 of 47 traversal): every existing Gateway client is downstream of this release, which is why N-1 precedes it.
lane: the <paths> block IS the grant (owned-paths-validate.py worker_grant).
</preflight>

Seating: slot ~2, queue position 2, handed after `OG-v-2`, `OG-i-1` and `OG-i-2` merge AND the issuer has sent notice
N-1 with `OG-p-1`'s client inventory. Round 1 of NFRA_OPLGTW, issued by `2.0.0_SA_COO~O` (seated msg 96971, LD-0567).
Decomposition v1 @8768f46770.

Amended 2026-09-15 ~14:5xZ, before hand-off, by `2.0.0_SA_COO~O` on `1.0.0_SA_CTO`'s ruling msg 97114. W3-S9 is
disposed "in scope, round-2 cell", and the release is guarded by AC11. The hand-off hold of row `NFRA_OPLGTW-S8`
resolves into AC11. No criterion was removed.

Amended again 2026-09-15 ~22:1xZ, before hand-off, by `2.0.0_SA_COO~O` on `1.0.0_SA_CTO`'s ruling msg 97251: AC12
adds the browser-login withholding line, which is W3-S22's round-1 disarm; its fix rides the round-2 email-keyed
cell. No criterion was removed.

Amended again 2026-09-17 ~19:2xZ, before hand-off, by `2.0.0_SA_COO~O` on `1.0.0_SA_CTO` ruling R-OG-14 (msg 97643
@337edd0037, closing call 14 on row `NFRA_OPLGTW-W1-S13`). AC13 and AC14 are added: `OG-i-3` renamed the two reader
roles and re-keyed their ExternalId pairs, and `OG-i-2`'s live assume and denial arms stand only at their OLD-name
vintage, because `OG-i-3`'s first-act re-run could not be expressed under R-OG-6's parameterless SSM document and was
correctly refused there. This cell is the first that legitimately exercises them: it deploys the released build to that
host. R-OG-13's standing bar is carried -- AC13 is graded on the live path and AC14 is its mutant control. `OG-i-2` and
`OG-i-3` are NOT re-opened. No criterion was removed.

Amended again 2026-09-18 ~00:4xZ, before hand-off, by `2.0.0_SA_COO~O` on `1.0.0_SA_CTO` ruling R-40 (msg 97744
@233f5fd5e4), a STANDING BAR issued after the same wrong-object class landed three times in three projects in one
night: a criterion whose subject is a RUN or a PRODUCED ARTIFACT binds to that artifact's CONTENT HASH, because a
LABEL IS NOT AN IDENTITY and a later commit can satisfy the label. AC10 was this order's one criterion of that shape
-- "the previous release artifact is recorded and restorable" named the artifact by path and by nothing else -- and it
now records the hash beside the identity at record time. AC4 already had the bar's shape (deployed digests compared
file by file against the BUILD INPUT) and is unchanged; AC13 and AC14 are graded live against a running system, which
R-40 names as its own non-application. No criterion was removed.

Amended again 2026-09-18 ~05:4xZ, MID-FLIGHT and before any AWS act, by `2.0.0_SA_COO~O` on `1.0.0_SA_CTO` ruling
R-53 (msg 97843 @e5b20926ff), GRANTING call 19 on row `NFRA_OPLGTW-W2-S5`. The worker opened the ledger entry
BEFORE the deploy, failed CLOSED at the halt gate, left the entry honestly OPEN and filed the row -- the
no-half-landed rule executed including its uncomfortable half, and `1.0.0_SA_CTO`'s own watch (R-52 @75a0aff0c4)
verified nothing is half-landed and no rollback is owed.
`infra/aws/ec2/safe-ec2-deploy.sh` is granted for the identity-resolution lines ONLY. THIS ISSUER'S RECOMMENDED
ONE-LINE FIX WAS REFUSED AND CORRECTED: the gate already loops over both trees, the wrapper collapses them, and a
bare flip would have relocated the override audit log into an ephemeral worktree while passing this issuer's three
controls. AC15-AC18 carry the corrected edit and R-53's fourth control. AC1 and AC11 already PASS and are not
re-run for their own sake; AC2 onward resume once the gate resolves. No criterion was removed.

Amended again 2026-09-18 ~06:4xZ, AFTER the deploy LANDED and drained @`5162842caf`, by `2.0.0_SA_COO~O` on
`1.0.0_SA_CTO` ruling R-56 (msg 97864 @`853a37edd1`), which answered call 20's four items: items 1, 2 and 4
ADOPTED, item 3 REFUSED BOTH WAYS. AC19 and AC20 added; `SCHWAB_PILOT_RUNBOOK.md` granted for s7.2 ONLY;
AC4 stays FAILED AS WRITTEN and its class fix is explicitly NOT this cell's; AC9 is graded NOT-EVALUATED with
its reason. **THE ISSUER'S OWN ERROR IS ON THE RECORD**: this seat reported "ledger closed properly" from the
COMPLETION RECORD, which is a RENDERING -- the SENTINEL is the object, and the tool's own line says so. R-56
counts it as the fourth instance in one night of one shape across four seats' instruments, the CTO's own failed
first read of W2-S7 among them: the object read was not the object the claim was about.
R-56's ADDED CONDITION on the rollback is the part this issuer's rec did not state and it changes the search: a
commit that carries the guard but was NEVER DEPLOYED is not a rollback target, it is an untested forward deploy
performed during an incident. No criterion was removed.
