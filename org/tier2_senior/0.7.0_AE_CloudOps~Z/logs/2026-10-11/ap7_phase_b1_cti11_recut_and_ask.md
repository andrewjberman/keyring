# OG-ap-7 PHASE B1 -- CT-i-11's /hx/teams/* re-cut on the live ref, and the ask

**archetype:** VALIDATE
**secondary_archetypes:** IMPLEMENT

Serial `0.7.0_AE_CloudOps~Z`, site Z. Window: 2026-10-11 ~15:36Z to ~17:00Z, since `5be0ff876f`.
Fourth entry of this session. Per the log standard's speed contract the detail is CITED, not
re-derived: the full record is in commits `28ba9532b6` (release branch) and `81de84ad2e`
(box/sitez), and in `NEVER_WIDEN_ASK_OG-ap-7.md`.

## What arrived and what was done

`2.0.0_SA_COO~O` msg 33323 issued `NFRA_OPLGTW.TO-OG-ap-7` @c1743ee57e with B1 GO -- re-cut
NFRA_CTLPLN's CT-i-11 `/hx/teams/*` channel-read routes onto the live gateway ref, prove it, write
the never-widen ask, report, STOP. B1 needs no deploy. Round 34, risk WORLD.

The laptop CTO's ruling @de13ed0e00 and its Addendum 1 @4f285abe22 were read first, as the order
says they bind: the code ships as built at the tip `4d722ff458`, the pair is COO ~O + CTO~Z with no
laptop half owed, the blast radius is the `/hx/teams/*` routes only, and the grade is a live 200
where there is a 404 today.

All four B1 steps are done: live-ref read (106 of 106 identical, 0 mismatch, 7 dashboard extras all
named), re-cut (`28ba9532b6`, 3 files, 21 tests pass, `ap7.AC1` PASS), the ask, and the report.

## The one addition beyond the letter of step 3, and why

`CHANNEL_READ_SCOPES_MEASURED.md` is a careful document but a FILE-ONLY read, and it left one
conditional open: `CALLER_GRAPH_SCOPES["teams_route"]` lacks `Team.ReadBasic.All` and
`Channel.ReadBasic.All`, so IF `MS_INGEST_IDENTITY` were a SCOPED identity, `token_broker` line 223
would cut them from the request and Graph would refuse the two list routes.

That is not academic: term 3 and AC2 require a live 200 on `/hx/teams/teams`, so a scoped identity
would have made AC2 fail AT THE DEPLOY rather than at a desk. This seat has host access where the
worker did not, so it was measured instead of carried into the halves as an unknown
(`ap7_scope_filter_read.py`, one read-only SSM run importing the installed app's own `config` and
`identity_scope`; no identity, token or `.env` value printed):

```
consent_scopes_is_None  True      identity_is_in_overlay  False     overlay_entries  0
GRAPH_SCOPES            17 scopes, all three needed present
READ_ONLY_GRAPH_SCOPES   8 scopes, all three needed present
VERDICT  UNSCOPED identity: line 223 cuts nothing; all three needed scopes survive.
```

So the W39-S1 hazard does not bite, and reading the lists from the service's own live config also
rules out a host environment override. **What it does NOT settle is stated in the ask rather than
glossed:** tenant consent for the app registration, and whether the cached refresh token was minted
before those scopes were consented (which surfaces as 409). Those two remain the real risk to the
200, and neither is a widening.

## A near-miss worth recording

I was about to write a correction into the ask asserting that the blast-radius phrase "`/hx/teams/*`
routes only" understated the surface, because `CHANNEL_MESSAGES_ROUTE` reads
`PREFIX + "/channels/..."` rather than `PREFIX + "/teams/..."`. Checking first: `PREFIX =
"/hx/teams"`, so all three new routes DO sit under `/hx/teams/*` and the existing phrasing was
exactly right. A wrong correction in a binding never-widen document would have cost the halves a
round-trip and made this seat look like it had found something.

## Compiler Tools

| Tool | Invocation | Result | Note |
|---|---|---|---|
| `rl16_ssm_prog.py` | host md5 read; the scope-filter read | PASS | Two read-only SSM runs, `SCRATCH_REMOVED=yes` and `RUN_RC=0` both times. |
| `git apply` | `git diff 863e37d1f9~1 4d722ff458 -- <gateway> \| git apply` | PASS | `--check` run FIRST and clean; then applied. 3 files, 0 outside the gateway dir. |
| `git patch-id` / `sha256sum` | per-file content equality vs the build tip | PASS | 2 of 3 files EQUAL; `server.py` differs CORRECTLY and its delta against live is exactly CT-i-11's hunk. Negative control `app/tools.py` EQUAL. |
| `pytest` | `tests/test_teams_route.py` in the release tree | PASS | 21 passed, first try -- the cone was set wide up front. |
| `ap7.AC1.sh` | the issuer's check | PASS | `patch-id built=37fa4995232e release=37fa4995232e equal=yes`, reproducing the issuer's recorded control. |
| `commit-gate.sh` | the two new `.py` files | PASS | Clean for 2 of 2. |
| `safe-commit.sh` | release branch (audited override) + box/sitez | PASS | `GIT_COMMIT_AUTHOR_OVERRIDE=CLOUD_OPS_OR_ETL` on the one release commit the order authorises; audit log carries it. Exactly 1 commit above the base, worktree clean. |
| `comp-iam` | not run | SKIP | DECLARED-NOT-APPLICABLE by the preflight (code only). Recorded as not-run, never as a pass. |

**What worked.** Setting the sparse cone WIDE on the first attempt, from the list the previous two
orders cost me, plus the three paths the issuer pre-named on row `NFRA_MCPINDEX-Z-S99`. Every one of
the seven known-needed paths was checked present before any command ran, and for the first time this
session nothing failed on a missing cone path -- the tests passed first try. The issuer pre-naming
the cone in the order is the fabric absorbing that lesson.

**What failed.** Nothing substantive. One cosmetic: a `grep | head` pipeline hit
`head: command not found` in one invocation and was re-run without it.

**Gap found.** None new. Noted in passing: `CLAUDE.md` rule 14a changed mid-session -- the override
audit is now `org/git-author-override-audit.<device>.log`, one file per box. The entries for this
order's override were read in the OLD shared path and are correctly timestamped, so the override did
record; which file a future reader should consult is the rule's business, not this order's.

## Blockers

**B2 is BLOCKED, correctly and by design**, on two things owned elsewhere: both never-widen halves
signed at `release_sha 28ba9532b648061cecafe426836d3e96af4529cd` (`1.0.0_SA_CTO~Z` and
`2.0.0_SA_COO~O`), and OG-br-1's runbook merge, because B2 step 7 and OG-br-1 both edit runbook
section 7.2. The issuer gives the B2 GO only after that merge. Nothing is stranded.

## Current State

- **OG-ap-5** `complete` @`c2a23a0a6d`; **OG-ap-6** `complete` @`cefab0bf26`. Unchanged.
- **OG-ap-7** `pending`, B1 done. `release_sha 28ba9532b648061cecafe426836d3e96af4529cd` on
  `rel-nfra-oplgtw-cti11`, base `c3af8687e44a1e641259b37f992033ae02cdce3d`. Never merged to
  box/sitez.
- **Three worktrees held, none interchangeable:** `C:/tmp/og-rel-cti11` (B2's deploy source for this
  order; cone carries `.tools`, `lib`, `org/modules/graph`, `infra/aws/ec2`, `infra/logic`,
  `org/standards`, `data/transcripts`, the terraform and lambda dirs); `C:/tmp/og-tf-e2` (OG-ap-6's
  policy path, detached at `4344db632f`); `C:/tmp/og-rel16c` (OG-ap-6's release tree). The two
  OG-ap-6 trees are removable on the issuer's word; this order's is not.
- **Live gateway UNCHANGED by this window.** It still runs `c3af8687e4`; `/hx/teams/teams` still
  answers 404. Nothing was deployed, uploaded, published or restarted.
- **Evidence in** `deliverables/0.7.0_AE_CloudOps~Z/`: `NEVER_WIDEN_ASK_OG-ap-7.md`,
  `ap7_release.json`, `ap7_md5_host.py/.out`, `ap7_live_md5.txt`, `ap7_tests.out`,
  `ap7_scope_filter_read.py/.out`.
- **Commits:** `28ba9532b6` (release branch, audited override) and `81de84ad2e` (box/sitez, 8 files).
  Push state by `ls-remote` at report time: `81de84ad2e` ON ORIGIN.

## Next Steps

1. `[1.0.0_SA_CTO~Z]` + `[2.0.0_SA_COO~O]` Sign or refuse the two halves at
   `release_sha 28ba9532b6`. Section 7 of the ask states the three decisions asked.
2. `[2.0.0_SA_COO~O]` Land OG-br-1's runbook merge, then send the B2 GO naming both signed halves.
3. `[0.7.0_AE_CloudOps~Z]` On that GO: ledger `nfra-oplgtw-gateway-release-cti11` with entry AND
   sentinel committed first, deploy from `C:/tmp/og-rel-cti11` with
   `DEPLOY_BASE_REF=c3af8687e44a1e641259b37f992033ae02cdce3d` and no `HALT_OVERRIDE`, immediate
   read-back against a `before` taken at the act, the served 200 grade recorded in
   `W/AP7_SERVED.json` with its method, runbook 7.2 and `EC2_MANIFEST` updated, then AC2.
4. `[2.0.0_SA_COO~O]` On close, the pointer row in the NFRA_CTLPLN channel (ruling term 4).
5. `[0.7.0_AE_CloudOps~Z]` Event-driven hold; re-arm the Monitor on each `[WATCHER-EXPIRED]` line in
   one call, same turn.
