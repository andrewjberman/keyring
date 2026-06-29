# CVO Finding + Verified Patch — comp-freshness firm-shorthand routing + comp-which cot-hint drift

**archetype:** VALIDATE
**secondary_archetypes:** IMPLEMENT
**Agent:** 3.0.0_SA_CVO | **Date:** 2026-06-29 | **Issued to:** 0.6.2_AE_PartnerETL (commit, comp-tool lane) · cc 1.0.0_SA_CTO (comp-tool arch-gate owner) + 2.0.0_SA_COO
**Origin:** Andrew-direct ("fix that and issue to 0.6.2_AE") after an agent hit `comp-freshness bd` dead-ending during a deploy verify.

## Friction (reproduced)
`comp-freshness bd` -> `error: argument command: invalid choice: 'bd' (choose from chain, script, artifact, ddb, all)` (exit 2). The firm name is a SECOND-level arg; canonical is `comp-freshness chain bd`. The firm-first form (`comp-freshness <firm>`) is the single most common intent (the tool's own usage examples lead with `chain bd`) and the TO shorthand + muscle-memory both reach for it, but it dead-ends on a raw argparse error. comp-which DOES route it correctly (`comp-which "check bd freshness"` -> `comp-freshness chain bd`), so only a direct bare-tool call bites.

NOTE for any consumer: that exit-2 is a USAGE error ("config error or AWS unreachable"), NOT a freshness FAIL (exit 1). It carries zero signal about artifact freshness -- never read a `comp-freshness bd` exit as a STALE/FAIL verdict.

## Part A — comp-freshness firm-shorthand (VERIFIED in scratch)
Insert immediately BEFORE `args = parser.parse_args()` (currently `.tools/comp-freshness:1112`):

```python
    # Firm-shorthand convenience (Andrew-direct via CVO 2026-06-29): accept a bare
    # bd|inf|cot as a top-level alias that dispatches to `chain <firm>` so the
    # firm-first form never dead-ends on a raw argparse 'invalid choice'. Only fires
    # when the FIRST token is exactly a firm shorthand; chain/ddb/all/--list unaffected.
    if len(sys.argv) > 1 and sys.argv[1] in ("bd", "inf", "cot"):
        sys.argv.insert(1, "chain")

    args = parser.parse_args()
```

Also add a self-documenting line to the epilog Examples block (after `comp-freshness chain inf`):
```
  comp-freshness bd            # shorthand for: chain bd
```

**Verification (scratch copy, this session):** py_compile OK. `comp-freshness bd` output changed from `invalid choice: 'bd'` -> reached the BD chain handler (`cmd_chain("bd")`, attempted BD config load) = routed correctly. Regressions clean: `chain inf` and `--list` unaffected. (The only scratch-side error was a cwd-relative config-not-found, an artifact of running outside the repo -- in `.tools/` the config resolves and the chain runs.)

## Part B — comp-which / manifest stale cot-hint (added 2026-06-26, 8e1de0fd0; hints never updated)
comp-freshness now covers cot (5 silver tables, partition-key mode), but two routing strings still say `{bd|inf}`:
1. `.tools/comp-which:144` -> `["comp-freshness chain <bd|inf>", ...]`  ==>  `<bd|inf|cot>`
2. `org/modules/graph/graph-call-manifest.yaml:363` -> `canonical_call: "comp-freshness chain {bd|inf} ; ..."`  ==>  `{bd|inf|cot}`
3. (completeness, optional) `graph-call-manifest.yaml:737` tools_index `subcommands: [chain, script, artifact]`  ==>  `[chain, script, artifact, ddb, all]` (ddb+all were also missing).

## Lane + asks
- comp-freshness + comp-which are canonical CTO-arch-gated comp-tools = AE/owner commit lane; I authored + verified the patch but do NOT commit the canonical tool myself (CVO verifier-not-fixer). 0.6.2 commits via the standard ds-commit-gate; CTO cc'd as arch-gate owner.
- After commit: re-run `comp-freshness bd` (expect it routes to `chain bd`) + `comp-which "check cot freshness"` (expect the hint now shows cot). Ping me to re-verify map==territory.
- Priority: P2 (papercut; comp-which already routes the intent, functional verdicts unaffected).

## Compiler Tools
| Tool | Run | Result | Note |
|---|---|---|---|
| comp-freshness (scratch-patched) | `bd` / `chain inf` / `--list` post-patch | PASS | routing proven; regressions clean |
| comp-which | `"check bd freshness"` route | PASS | routes to chain; exposed the stale `<bd|inf>` (no cot) hint |
| grep (manifest/comp-which) | locate the 3 stale-hint sites | PASS | comp-which:144 + manifest:363/:737 |

— 3.0.0_SA_CVO
