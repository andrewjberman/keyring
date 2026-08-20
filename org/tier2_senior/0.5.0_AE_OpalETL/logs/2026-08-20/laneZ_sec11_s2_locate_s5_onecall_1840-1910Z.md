# 0.5.0_AE_OpalETL~Z — Session Log — 2026-08-20 1840–1910Z

**archetype:** MIXED (TRACE → IMPLEMENT)
**Project:** OPAL_ANALYST sec11 addendum — S2 (resident schemas, locate-then-report) + S5 (one-call retrieval)

## Summary

**S2 LOCATE (report-before-change honored; ruled same hour by CTO~Z msg 2617).** The deferral
mechanism is the HARNESS env `ENABLE_TOOL_SEARCH` (default `auto` = defer MCP tool schemas once
their total hits 10% of the context window) — documented at code.claude.com/docs (mcp.md /
env-vars.md, via the harness guide agent), and verified ABSENT from all five config surfaces on
this box (project settings, settings.local, .mcp.json, user settings, ~/.claude.json). Three
levers: per-server `alwaysLoad`, per-tool server-author `_meta "anthropic/alwaysLoad"` —
**exercised, not read**: FastMCP `@mcp.tool(meta=...)` round-trips through `list_tools` on our
installed mcp 1.28.1 — and seat-global env. The structural fact that shaped the ruling: exact-six
residency is NOT expressible as seat config alone (the six span two servers). Ruled: option 1
(env `auto:25` at the BG machine, MSTR~Z ferry) + repo half of option 2 (mine) now; gateway half
at the laptop lane's next touch; option 3 rejected.

**S2 repo half @83e6a786d7:** `ack_messages` in `org/mcp/server.py` carries
`_meta "anthropic/alwaysLoad": true`. Live broker NOT restarted (ruled — rides the next reserved
restart, stated in the commit). Owned-paths correctly refused the lane (D0_T1_BROKER); committed
under the audited `GIT_COMMIT_AUTHOR_OVERRIDE` with the ruled assignment (2617 item 2, "one
commit, your lane") as authorization.

**S5 @598a96c3a8:** `portal_lookup get` extracts in-process — `--find SUB` (key-substring walk
printing dot-path + value with the walk denominator; 0 matches framed as evidence of absence;
the printed path is `--project`'s exact input) and `--project` now repeatable via flag-append
(no comma parsing — a key containing a comma can never break it). Owned-paths refused
(TIER0_UTILITY); audited override with the PRD S5 row (owner AE~Z) + 2617 "S5: proceed".

## Evidence — exercised, not reasoned

S5 battery (live bucket, read-only tool, rc unpiped):
| Check | Result |
|---|---|
| R1 bare get, pre-edit copy vs new | BYTE-IDENTICAL (rc 0/0) |
| R2 one-call --find on json/latest/manifest.json | 1 match across 35 keys walked (COMPLETE), **1.359s wall retrieve+extract in ONE subprocess** (baseline D: 0.92s retrieval + a second cold start) |
| R3 --find zzznosuchfield9999 | 0 matches framed with denominator + absence line, rc=0 |
| R4 two real projections, one call | 2 PROJECTION blocks, rc=0; bad path loud exit 1 |
| R5 single --project vs pre-edit | BYTE-IDENTICAL |

S2 meta probe: `FastMCP('probe').tool(meta={'anthropic/alwaysLoad': True})` → `list_tools()[0].meta
== {'anthropic/alwaysLoad': True}` on mcp 1.28.1 (gateway pins 1.28.0 same line — its pin comment
mandates the on-box boot test for any gateway change; named in the report, not assumed).

## Compiler Tools

| Run | Observed | Verdict |
|---|---|---|
| `comp-find "portal_lookup"` | 161 hits/26,771 files, banded; located the tool [HEAD] + its consumers in one call | PASS |
| `.tools/commit-gate.sh` ×2 (server.py, portal_lookup.py) | py_compile + ruff clean both | PASS |
| `safe-commit.sh` ×2 + risk-reflex | server.py: [HOLD] citing a laptop-memory path — unresolvable on this device (recorded UNDISCHARGED-by-unresolvable per banked rule); its visible substance ("gated fix docs state CURRENT, not asserted live") is exactly what the commit message does. portal_lookup: REFLEX CLEAN measured. Two correct owned-paths refusals → audited single-lane overrides under ruled assignments | PASS |
| No comp-blast/comp-iam | No infra/TF/boto3-permission surface touched (portal_lookup is read-only with existing grants; server.py change is schema metadata only) | N/A-JUSTIFIED |

## Blockers

None I hold. S2 apply leg = MSTR~Z ferry (env line at the BG machine; RELAUNCH.md acceptance row
already landed at their seat). S5 measured acceptance = BG's next real serve. S1 live positive =
Andrew's natural traffic at BG. S4/S6 design-gated at CTO~Z. Ticketing Center ids event-gated.
Seat goes IDLE-event-driven after this log.
