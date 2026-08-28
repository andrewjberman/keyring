# 1.0.0_SA_CTO~D -- T1 grep rail LANDED + comp-find --corpus aws + mobile headline wrap -- 19:23-20:50Z
**archetype:** IMPLEMENT
**secondary_archetypes:** VALIDATE, COORDINATE

Delta since `ctoD_daily_sprint_web_client_and_grep_gate_audit_1722-1923Z.md`. Andrew-direct throughout,
seat off the fabric channel except the ONE broadcast he authorized.

## Summary

1. **Mobile headline wraps** (Andrew: "the main bold headline at the top ... needs to be fit properly so
   it wraps"; "Only the very top headline"): `.headline` nowrap -> wrap in the MOBILE template only;
   measured on the served page at 390x844 via Playwright (3 lines at 26px, no overflow); re-rendered +
   republished so the presigned Teams link picked it up. @48bc1e4698.
2. **/open-calls on comp-find + the grep gate -> six cards -> "All approved."** Recorded verbatim (audit
   s7). T1 block; corpus default -> all; one broadcast; T2 single-file after a week; native Grep/Glob
   keep nudge; comp-grep -> forwarder. Earlier: comp-find stays repo-only; AWS substrate via comp-kuzu.
3. **T1 LANDED.** Law @9ed33c473e (CLAUDE.md Rule 21 + cost/non-application clause). Mechanism
   @32d5967277: per-segment rail in `.tools/hooks/comp-tool-hud.sh` (emit_deny, fast path, ALLOW-SEARCH
   rows, aws segment classification), `.tools/comprail-gate1-fptest.sh` 43 cases (RED 25/43 vs the
   pre-T1 hook, GREEN 43/43; saves+restores the live marker; `COMPRAIL_HOOK=` control), comp-find
   default corpus `all`, comp-grep forwarder, regenerated infra/system/06. Broadcast to COO/CTO/MSTR
   3/3 DELIVERED (78994-78996), push state LOCAL at send.
4. **comp-find --corpus aws BUILT** @a13f7445a5 on the comp-kuzu surface (the graph's aws layer IS the
   live plane): 2,089 nodes, vintage from the DB's provenance header, bands = node_type, drift_class per
   hit. DRIFT census: DECLARED=1501, **LIVE-no-DECLARED=320** (in AWS, not declared in the repo),
   AWS_MANAGED=33, LIVE-INCREMENTAL=3, unset=232. Rule 21 corpus paragraph gains one clause (no second
   broadcast -- one was authorized).

## Deployment / verification (actual outputs)

- FP test: `comprail search-rail FP-test: 43/43 cases as expected (marker restored to ON) RESULT: PASS`;
  red-first control `COMPRAIL_HOOK=<HEAD hook>`: 25/43, 18 regressions.
- Hook latency (3 samples each, MSYS, COMPRAIL_NO_ROUTE=1): `git status` 1.8-2.5 s; `python x && echo`
  1.5-2.5 s; `grep -rn foo org/` (DENY) 3.0-4.6 s; `cd && aws iam get-role` (DENY) 5.1-5.6 s. Pre-T1
  single samples: 1.5 / 1.9 / 5.2 / 0.98 s -- the last one was the HOLE (exited at the lead verb).
- Gates: commit-gate clean; py_compile + ruff clean on the extensionless python; bash -n OK.
- --corpus aws exercised: `opal-gateway` 33/2089 over 14 types; `python3\.9 lambda` 3/198; `--name
  daily --files` 174; zero arm over 2089; `portal --band S3_BUCKET` 2.

## Compiler Tools

| tool | invocation | result | note |
|---|---|---|---|
| comp-find | ~20 (hook internals, rail log, comp-find/comp-grep plumbing) + the 5 aws exercises | PASS | default corpus now `all` -- denominators changed accordingly |
| comp-kuzu | --schema; aws census; 3 node dumps | PASS | node_type is UPPERCASE; `--json` preamble is on stderr |
| comp-system | compile x2 + --check | PASS | required by the safe-commit _SOURCE gate; 06 regenerated twice |
| comprail-gate1-fptest.sh | 3 runs (red control, green, green) | PASS | |
| commit-gate / ruff / py_compile | 3 | PASS | |

What failed: the pipescript-suite gate (dial F9) blocked every commit touching `.tools/comp-find` on
`test_pipescript_digest::test_all_arms_pass` -- DISCRIMINATED pre-existing (identical with the
committed comp-find restored); landed twice under the audited `PIPESCRIPT_SUITE_SKIP` with the
discrimination on the commit; routed to COO in the broadcast for the suite owner.

## MCP traffic

Outbound 1 (the authorized law-edit broadcast, 3/3 DELIVERED). Inbound: window 19 OPEN/CLOSE (acked).

## Blockers

None at this seat. External: LDT's App-1 redirect-URI fix (next week); the pipescript digest specimen
re-record (suite owner, routed).

## Current State

- T1 rail is LIVE on this device (hooks run from the working tree) and on every device at its next
  integration window. Kill switch: delete `org/mcp/comprail-gate1.enforce` (search deny off; aws tiers
  stay). ALLOW-SEARCH rows accumulate in `org/mcp/comp-which-rail.log` -- the T2 decision input (~09-04).
- comp-find: default corpus `all`; `--corpus aws` live; comp-grep forwards.
- Daily Sprint: presigned Teams link live (exp 09-04 19:20Z); mobile headline wraps; tonight's
  /daily-sprint publishes + presigns automatically.
- Commits this window (author CTO~D): 48bc1e4698, 9ed33c473e, 32d5967277, a13f7445a5 (+ this log).

## Next Steps

1. **[Andrew]** tonight's /daily-sprint; LDT call items (IT_CALL_LIST_20260828_LDT.md).
2. **[1.0.0_SA_CTO~D successor, ~2026-09-04]** T2 decision: census `ALLOW-SEARCH shape=single-file`
   rows in the rail log; pitch deny/keep to Andrew with the number.
3. **[2.0.0_SA_COO]** route the pipescript digest-specimen RED to its owner (broadcast 78994).
4. **[1.0.0_SA_CTO~D successor]** on LDT's fix: `az ad app show` byte-diff + a real sign-in to 200 on
   /sprint, then switch the Teams tab and delete `daily-reports/latest/`.

**state: IDLE, nothing gated at this seat** · push state of this log: LOCAL (origin/CLOUD @2afd4ddd4e, ls-remote read 20:5xZ)
