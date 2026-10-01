# SELF-DRIVE OPALAI_MCP_SITEZ -- tick 13 -- 1.0.0_SA_CTO~O

**archetype:** COORDINATE
**Arming record:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261001_04xxZ_SELF_DRIVE_OPALAI_MCP_SITEZ.md` @80102ed73d
**Ticks covered:** inter-tick 14:2xZ-15:2xZ and tick 13 (15:24Z). Cron 84d0ab03.
**state:** ARMED

## Driver acts since the tick-12 log

1. **OG-rl-2 (train slot 5, the `/hx/mail` listing release): CTO never-widen half SIGNED** @0441fe60b4 (msg 27878).
   Independent reads:
   - live e3567ce5f7; release 0a1d9079c6 = 2 commits, 5 gateway files;
   - `ms_ingest.py`, `tools.py` and `transcript_route.py` unchanged (a whole-file census);
   - C5 absent;
   - sender table 3 (counted, never printed);
   - caps per PRD v1.4.
   The **unsigned page token was analysed and accepted**: it is honored only on an exact sender/window/flag match and
   carries only a continuation, while `$filter` is rebuilt server-side from a quote-free table sender and rows are
   re-checked, so a forged token stays in its own window. The residual is named: the Graph filter and continuation have
   run on stubs only, so live AC1 is their first run, failing closed and rolling back.
2. **Relay** of `3.0.0_SA_CVO~O`'s OG-rl-2 second half (@ce3c650623, msg 27887) to `2.0.0_SA_COO~O`, verbatim, with
   L1-L3:
   - L1: a host-side sender-table set hash before and after;
   - L2: rollback mandatory after a post-extract refusal;
   - L3: the rollback shell supplies the table.
   Both halves are in, so PHASE B is GO.
3. **MS-dn-1 (train Terraform act #3) VERIFIED LIVE** on `2.0.0_SA_COO~MS` msg 27908 (complete @08772a9c10):
   - `gateway-firm-deny-policy` on `opal-gateway-role` = Deny `s3:GetObject` on
     `opal-data-portal-v2/platinum/mdpf/{49financial,inflection,cottonwood}/*`;
   - `simulate-principal-policy` by this seat: 3 firm keys `explicitDeny`; the global key
     `json/benchmarks/model_portfolio_timeseries.json` `allowed`;
   - the issuer's AC1-AC4 PASS (AC3 9 of 9); no void condition met.
   **All four train Terraform acts (#1, #2, #2b, #3) are done.** NFRA_MCPMSP round 2 waits only on G-MSPID.

## Grades and signatures received

- `3.0.0_SA_CVO~O` L4-R: NFRA_OPLGTW **PRD v1.4 ratified-text half SIGNED** @c3a2cccd6d.
- `3.0.0_SA_CVO~O` L8/L9 NFRA_MCPINDEX round 6 @c5710a5111: 27 rows dispositioned, 7 graduated OPEN into
  `REMEDIATION_v5.md`, 20 dismissed; MXV7-J1 PASS, MXV7-J2 NOT_EVALUATED (Alyssa's cold run). **No slug message yet.**
  The round is not fully terminal (MX-s-16 closes on its scheduled fire), so this seat's round-6 analysis waits on the
  slug.

## Measurement (15:24Z)

Inbox 0 new (27878 acked; it had been acted on at signing). Sequence: no flags on the 5. Served e3567ce5f7; the
manifest agrees. Space-safe sentinel census over 110 worktrees, in scope: only `nfra-mcpindex-r6-bd-merge-retire`
(MX-s-16, open by design). MS-dn-1's ledger is closed, and OG-rl-2's is not yet opened.

## Calls

No open calls in scope OPALAI_MCP_SITEZ (tick 13). Owed, event-gated:
- the NFRA_MCPINDEX round-6 analysis, on the slug;
- the NFRA_OPLGTW L10 analysis, on its slug.

## Acts only Andrew can perform

Unchanged from the tick-10 log (83271415ba), as amended in the tick-11 log (the 8194 apply is its own falsifier). G-MSPID
is now the ONLY gate on NFRA_MCPMSP round 2.

## Completion test

NOT DONE: 0 of 5 complete. REACHABLE 3 (OPLGTW, MCPINDEX, MCPMSP); UNREACHABLE 2 (MCPORTAL: G-CLOSE, G-2ND; OPALAI:
G-PUSH plus the 8194 apply).

## Compiler Tools

| Tool | Command | Result | Note |
|---|---|---|---|
| aws (read-only) | `iam get-role-policy gateway-firm-deny-policy`; `simulate-principal-policy` x4 | 3 explicitDeny, 1 allowed | MS-dn-1 verified independently |
| git | `diff --quiet` on 3 files; `show` of the listing code and the sender file (count only) | unchanged; caps match; 3 | OG-rl-2 sign-off |
| git worktree census | Python porcelain, 110 worktrees | 1 in-scope sentinel, expected | |
