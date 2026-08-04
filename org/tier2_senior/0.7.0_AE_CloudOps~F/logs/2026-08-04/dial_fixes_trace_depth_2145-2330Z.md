# ADHOC.comp-trace-depth-fixes: the trace+depth dial-fix set landed -- T0/T1/T3/T5/T6 + DEPTH-0/DEPTH-1, T2 walled off

**archetype:** IMPLEMENT
**secondary_archetypes:** VALIDATE, COORDINATE

**Serial:** `0.7.0_AE_CloudOps~F` -- Window: 2026-08-04T21:45Z -> ~23:30Z
**Commits this window (mine):** @ffb41a849 (the fix set, 4 files, STRUCTURAL-TWOPHASE/rule-bank
override audited). Follow-up T0-restore commit pending ~B's ACK (see Current State).
**Deploys/mutations:** 0 (workspace tooling only; no AWS surface touched)

---

## Summary

Andrew GO'd the staged TO (COO-issued P1 under the ~1900Z spine-tool fan-out @fc42aacc5). Read both
CVO dial records in full, reproduced EVERY named item pre-fix with true rc (no-pipe discipline --
first probe round had captured `head`'s rc and was redone), then landed:

- **T1**: trace rc=3 NOT-FOUND now prints denominator (2252 nodes, per-type counts) + universe
  declaration (naming what is OUT: AWS config planes, silver tier -> comp-kuzu/comp-blast pointers)
  + two-tier difflib near-matches labeled UNVERIFIED DUPLICATE/LEGACY candidates. CVO's exercised
  pair now discriminates: `A_00.accounts_dimension.py` suggests `gold:A_00.accounts_dimension`
  first.
- **T3**: `=== comp-trace provenance ===` stderr header on EVERY walk incl. --json (stdout stays
  parseable, exercised): built_at+age AND sha-drift-at-load + served=cache|rebuilt with head-pin
  semantics stated. Facts recorded on the load path (`_LOAD_PROVENANCE`), never recomputed.
  Engine PRINTING only -- vintage FIELD declaration = ~A's registration seam, cited to them 2321Z.
- **T5**: trace subparser `prog=comp-trace` + `_require_query` errors on the subparser -- the cold
  user's first output now teaches the shim form. comp-blast bare output verified byte-identical.
- **T6**: `--exact` self-selection flag (exact id walks alone; --exact miss = rc=3 naming the
  mode) + multi-match NOTE when the query IS an exact id in its own prefix set.
- **DEPTH-1**: out-of-enum grain now rc=2 REFUSE naming the closed enum + size, enum DERIVED AT
  CALL TIME from grain_contract.node_type_grain (predicate, never a roster); applied to
  scope/drill/rollup/blast grain args; contract-unreadable path WARNs UNVALIDATED; in-enum-empty
  stays honest 0 (`scope file` byte-identical pre/post). **CTO ACCEPTED 232056Z.**
- **T0/DEPTH-0**: both output-contract entries authored, moved out of pending_declaration.
  manifest-check first BLOCKED on `grain=function` (out of ONTOLOGY2 canon) -> re-declared
  `grain=field` per family refs (comp-blast/kuzu), enum growth deliberately left to ~C's LAW-2
  lane. Completeness PASS post-fix.
- **T2 UNTOUCHED** (PRD-gated by design): diff grepped for the family form -- absent.

**Shared-file interleave (the finding of the window):** ~B lifted my uncommitted comp-trace T0
block from the tree for their K3 commit on the same YAML (their 231159Z hold message), and my
safe-commit @ffb41a849 landed MID-LIFT -- so HEAD momentarily carries comp-trace neither declared
nor pending (completeness invariant violated at HEAD until restore). Surfaced to ~B same turn
(231825Z) with the sequence facts + plan: I commit the restored block on their ACK. Their backup
sha1 739bcb477f7 is the recovery anchor.

**LD-0367 integration window**: COO's :55 cascade arrived mid-verification; seam not committable
by :55 -> held :55-:00, files named to MSTR (225548Z), committed after :00. No stash, no .runtmp.

## Compiler Tools

| Run | Result | Note |
|---|---|---|
| comp-trace (bare-miss / true-absent / prefixed-id / bare / trace-subcmd triple) pre-fix | rc=3/3/0/1/1/0 | All five dial-record controls reproduced verbatim (redone with true rc after a piped-rc first pass) |
| comp-depth scope zz-bogus-grain / scope file pre-fix | rc=0 / rc=0 | DEPTH-1 control reproduced: bogus grain read as empty-but-valid |
| comp-trace post-fix battery (T1/T3/T5/T6 + --json parse + comp-blast bare stability) | PASS | rc=3 w/ denominator+near-match; header both axes every walk; usage shim-form rc=1; --exact walks single node; blast byte-identical; JSON stdout parses |
| comp-depth post-fix (bogus rc=2 REFUSE naming 14-value enum; valid byte-identical) | PASS | Both directions: fails pre-fix shape, passes post-fix; honest-0 preserved |
| .tools/commit-gate.sh (cli.py + comp_depth_cli.py) | PASS | Rule 14 pre-commit |
| .tools/comp-manifest-check completeness | 1 BLOCKED -> PASS | Caught out-of-canon grain=function (working gate); re-declared field; registration + output-contract invariants PASS |
| comp-which "how do I grep the repo" (A.3 exercise) | PASS | Forwarder ran (banner produced), not merely resolved |

## MCP traffic

Inbound 4 handled same-turn: COO integration-window cascade (held, files named), ~B shared-file
hold (honored + interleave surfaced back), CTO DEPTH-1 acceptance, COO wave context. Outbound 8:
MSTR hold ACK w/ file list, COO cascade ACK, CVO per-item verify-on-landing report, COO landing
report, CTO DEPTH-1/T5 note, ~A T3 seam citation, ~B interleave surface, broker summary updates.

## Blockers

- **T0 completion commit**: waiting on ~B's restore ACK (their stated <2min has run long; will
  nudge if silent much longer -- their K3 commit has not landed on the file yet either).
- **STRUCTURAL-TWOPHASE override discharge** (comp-system recompile): BLOCKED-ON-PEER-LANDING per
  the gate (uncommitted `.tools/comp-heat` + DS OVP_WS1 files). Discharge the moment peers land;
  surfaced to COO 231942Z so it does not die silently with the session.

## Current State (zero-context handoff)

- All named dial items code-complete + exercised + committed @ffb41a849; CTO accepted DEPTH-1;
  CVO verify-on-landing pending (their re-dial triggers 2/3/5-adjacent now consumable).
- comp-output-contracts.yaml at HEAD: comp-depth DECLARED; comp-trace entry ABSENT-in-flight
  (~B lift interleave) -- restore + follow-up commit = the one open edit at this seat.
- TO status: `pending` (flip to complete after T0 restore lands + CVO verify).
