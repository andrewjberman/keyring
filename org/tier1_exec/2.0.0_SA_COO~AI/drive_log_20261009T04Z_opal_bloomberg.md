# /canonical-drive NFRA_OPALAI -- 2.0.0_SA_COO~AI -- 2026-10-09 03Z-04Z (site Z)

**archetype:** COORDINATE

## What happened

1. **Andrew-direct ~03:1xZ, the close run split.** Andrew runs the refusal arm now, as himself; the answer arm stays
   Alyssa's. Record: `org/missions/D6/NFRA/NFRA_OPALAI/deliverables/2.0.0_SA_COO~AI/round2/ANDREW_DIRECT_20261009_031xZ_CLOSE_RUN_SPLIT_ANDREW_RUNS_REFUSAL_ARM_NOW.md`
   @d54838c763. Copied to `1.0.0_SA_CTO~O` as a decision.
2. **The live launch, ~03:13Z.**
   - The runtime checkout fast-forwarded 9c0a80b8d0 -> de5ce25fa3 (read 0 porcelain).
   - The Analyst started as Opal_Agent: powershell pid 37104, claude.exe pid 27624.
   - The gateway sign-in succeeded (Andrew's screenshot shows `/mcp` -> "Connected to opal-gateway-bbg").
3. **Andrew's Teams message.** At 2026-10-09T03:14:32.592Z he sent the Opal Bloomberg account "I need the last days
   price of PFDE". There has been no reply through 04:0xZ (`poll_addressed_teams_messages`, cursor 03:14:33Z, 0 new).
4. **Row Z-S63 (ARMED, this seat) @122ed41826: the Analyst idles at its input prompt.**
   - `launcher.ps1:172` passes no first prompt, so prompt.md's On-launch steps (identity gate, Teams arm) never run.
   - Interim disarm: the operator types one first turn.
5. **Row Z-S62 (ARMED, `1.0.0_SA_CTO~O`), read late by this seat.**
   - `opal_asker_query` is refused `write_class_denied` for every tier on the live gateway.
   - So neither close-run arm grades as written until the next gateway release: a portal question reads
     `write_class_denied`, not `asker_no_profile`.
   - Told Andrew, with a correction of this seat's earlier claim that only Alyssa's half was missing.
6. **OA-f-9 A2 / AC4, the durable fix for Z-S63.**
   - Issued @7051b95d8a, addendum R2-A14. It rides OA-f-9 because round 2 already has its one issuance.
   - Check runs: base FAIL; scratch GREEN PASS; scratch RED FAIL.
   - Worker ~24 built the nested commit 8cdc7b9735, one line: a first prompt naming the On-launch steps. Proof @50c03c88a2.
   - Issuer re-grade: PASS. AC1-AC3 are content-equal.
   - Drained @242b73ad83.
   - Local `nfra-opalai-r2-dev` (C:/tmp/oa-dev) fast-forwarded de5ce25fa3 -> 8cdc7b9735; AC4 on r2-dev: PASS.
   - Worktrees and branches removed.
7. **Open call at Andrew (queued):** push opal_ai DEV and PROD, de5ce25fa3 -> 8cdc7b9735 (fast-forward, one file, one
   line). REC yes: the launcher pulls PROD at launch, so the fix reaches the Analyst only after the push. The push is
   `0.0.0_AB_MSTR~Z`'s on his word (the SHARED-BRANCH LAW in `org/XXX.md`).

## Inbox

Acked:
- 32298: law edit, egress open except Bloomberg.
- 32310: MSTR~Z asked every COO for its cron id; replied with cron 102d96c4, 30m, keep-driving tapped.

## Compiler Tools

| Tool | Target | Result | Note |
|---|---|---|---|
| `.tools/to-pipeline-gate.py` (via safe-commit) | OA-f-9 A2 | OK | GATE (viii) on a modify; LIMB 6 does not fire |
| `.tools/surprise-row-gate.py` | Z-S63 | OK | 1 new row of 110 |
| `.tools/safe-merge.sh` | wk-NFRA_OPALAI-24-a2 | MERGED @242b73ad83 | fast lane |
| `.tools/unstick.ps1 -Peek` | the Analyst window | REFUSED | it takes agent serials only, not a window title; Andrew's screenshot was the read |
| `comp-blast` / `comp-routes` / `comp-cache` | -- | NOT RUN | a one-line launcher change, no route, cache or infra edge |

**What failed:** a scratch nested commit under a non-lane author is refused by the nested repo's owned-paths hook. Use
the seat's own serial on a throwaway branch, then delete it.
