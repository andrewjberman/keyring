# Claude takeover: IRPT direct review, two live verifications, two GOs - 1.0.0_SA_CTO
**archetype:** COORDINATE

**Date:** 2026-09-23 (into 2026-09-24 00:0xZ)
**Task Order:** Andrew-direct IRPT /closer master control (runtime successor to the Codex CTO session closed 22:42Z, log session_close_IRPT_1859-2242Z.md @e124553a33)
**Status:** IN PROGRESS
**Window:** 2026-09-23 22:43Z (takeover) to 2026-09-24 00:05Z.
**Commits this session (LOCAL, origin/CLOUD b475b96309 by ls-remote at 00:02:24Z):** d78fdb2f1c (rulings batch 1 + org/XXX.md Step 1b-F rows), 066dd4b88b (CONTROL.md + install review evidence; message overstated its content), 9baf67bb5f (rulings batch 2, .owned-paths.yaml +7 rows, manifest extension; carries what 066dd4b88b's message named).

## Objective

Complete the Claude startup, consume the Codex handoff, independently verify the two already-approved Holdings acts (P's schema-repair apply, M's 841-account COT publication), adjudicate the Analysis current-authority research, review P's Performance install candidate and the two seats' plans, and keep COO~P/M/Y driving under their Andrew-directed 20-minute loops.

## Compiler Tools

| Tool | Command | Result | Note |
|---|---|---|---|
| comp-which | ec2-auto-shutdown-enforcer definition/exemption | NO CURATED RULE | Fuzzy list only; answered by downloading the enforcer's own code from Lambda. |
| comp-find | 'ec2-auto-shutdown-enforcer' --files --limit 30 | PASS | Located infra/aws/lambda/ec2-auto-shutdown-enforcer/main.tf; a first call was aborted by the rail for a trailing pipe (correct denial, rerun with --limit). |
| naming-gate | scratch diffs at HEAD and at ddfc91b11f~1 / ae754f525f~1 | PASS | LD-0609 and LD-0610 arms; one LD-0610 positive arm was invalid (stale base) and was rerun from a detached scratch worktree. |
| owned-paths-validate | run without args | USAGE only | Called wrong; the pre-commit hook validated the file at commit instead. |
| safe-commit | three commits | PASS | Output captured to files; commit-gate checked 0 of N (no .py in any commit). |
| Lambda runtime emulator (docker) | public.ecr.aws/lambda/python:3.12 @5f188ce6104a, --network none | PASS | Candidate package + both layers INIT success and guarded refusal; deployed v4 as control. |

**What worked:** Different instruments from the executing seats: the deployed Holdings zip downloaded from the function's own Code.Location and hashed; the Cottonwood index read at its exact version; CloudTrail for the host; the runtime emulator for the cold start.
**What failed:** A plain-python cold-import harness (only /var/task on sys.path) produced a false AttributeError on the Performance package; the emulator run with the real bootstrap and the v4 control retracted it before it reached a ruling. The batch-2 apply script asserted on an existing grant row and the commit ran anyway with an overstated message (corrected in 9baf67bb5f). RULINGS.md was not valid UTF-8 (six cp1252 em-dash bytes); repaired.
**Gap found:** The always-on YCharts host has two writers holding it stopped (enforcer tag and Terraform declared state); the reopen pointer in retained.py is bound to directory revision and principal (P-REOPEN-01); intake/ and ops/ files the accepted Y batch depends on were outside the 31-path grant.

## Work Completed

1. Startup: /watcher armed (re-armed twice on expiry), session serial file, audit-archive 0 findings, 104 of 104 comp-tools resolve, 41 queued broker messages read in full and acked, 15 inbox files read.
2. Holdings apply verified: deployed irpt-holdings zip sha256 97f190ac... == approved artifact; CodeSha l/GQrFcE... at 23:00:52Z; no parents[4]; P's ledger closed on its publish branch.
3. COT publication verified: index grwnbLkeu -> revision 93f930c265, 18 objects, 841 accounts / 13,793 positions / USD 548,412,662.59 reconciled, both Anna accounts present, prior index retained. M's deployed-reader library matrix accepted (reader bytes == deployed).
4. Analysis current authority adjudicated (CRO 99773 accepted with four bounds); P's profile-field change and Y's consumer module accepted; IAM/host-tag plan 1de76039 GO.
5. Performance: source review f04d1e71bd + 068e9ccd85 PASS bounded with P-REOPEN-01; install plan f0a18919 GO after hashing package/layers, decoding IAM and proving cold start at the real layout; X10 sequencing ruled.
6. Host: stopped by ec2-auto-shutdown-enforcer at 21:21:18Z (CloudTrail), not a seat; two writers named; tag plan GO, state flip sequenced with the resident cutover.
7. LD-0609 and LD-0610 naming-gate changes accepted on CTO arms. Step 1b-F rows landed for P/M/Y loops. Y integration grant extended by seven exact rows at Y c4564aad17.

## Decisions Made

See RULINGS.md sections "Claude CTO takeover batch" and "Claude CTO batch 2". All three products remain INCOMPLETE; no journey PASS is claimed.

## Blockers

Andrew's acts: the signed-in Anna Holdings retest on localhost:5174 (both fixes live); 49F/INF report-currency attestations; SmartX and Orion per-use words; the AutoShutdown tag veto. Nothing else at this seat is blocked.

## Next Steps

1. [1.0.0_SA_CTO] Review M's 49F meshed candidate 1d0b700b + snapshot overlay; review P's NOT_READY vocabulary addendum 2cdbe2bd60 text; identify the infra/logic/registry lane holder for the "smartx/platform/silver/" RAISE.
2. [2.0.0_SA_COO~P] Apply f0a18919 and 1de76039 exactly; integrate the seven Y files and three-way-merge the diverged ones with Y's confirmation; build the resident factory/package/cutover receipt.
3. [2.0.0_SA_COO~M] Andrew's screen retest, then 49F/INF candidates under the attestation.
4. [2.0.0_SA_COO~Y] Confirm P's merges; run the real-login 12.03 journey once the cutover receipt lands.
5. [0.0.0_AB_MSTR] Shared pushes (local CLOUD is 5 CTO/MSTR commits ahead of origin) and P's Codex driver retirement.
