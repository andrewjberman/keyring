# ADVI_FIRMBKTS task order -- `FB-g-15` -- THE DISPATCHER REFUSES A QA INVOCATION THAT ARRIVES WITH THE PLATINUM MODE PRESET TO CANONICAL (THE CTO'S CONDITION ON ACT 2)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_FIRMBKTS/decompositions/ADVI_FIRMBKTS_DECOMP_R4.md</decomp_doc>
<owned_cells>FB-g-15</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_ADVI_FIRMBKTS~38</issued_to>
<issued_by>2.0.0_SA_COO~B1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- repository source only; no cron, rule, schedule or cadence is added or changed and nothing is deployed (the object reaches `code/gold/` in act 2's permitted set).
comp-iam: DECLARED-NOT-APPLICABLE -- repository files only: no AWS act and no grant.
comp-adversary: RUN by the issuer -- at base `r4_dispatch.py --arm export` reads 9 of 12 (the eight round-3 cases and the legacy-preset QA case PASS as controls; the three QA-with-canonical-preset cases FAIL as expected: the block passes the preset through). Blindness: the harness runs the block, not the whole dispatcher; `bash -n` is the syntax control.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `FB-g-15` (round 4, workstream `QAGUARD`; the CTO's act-0 sign-off, msg 3895, carried to act 2)

The producers' role is shared by the QA runner, and act 0 grants that role the canonical prefix. The CTO's condition for
act 2: show (a) a QA invocation prints legacy, and (b) a QA invocation with `BD_PLATINUM_MODE=canonical` PRE-SET is
refused by the dispatcher or cannot reach it. (a) holds already (the block never sets canonical on a QA invocation).
(b) does not: the block "never overrides a value already set", so a preset `canonical` passes through a QA run and would
write served keys at the canonical home with the shared role. You add the refusal.

### 1a. Behavior (the whole spec)

In `data/black_diamond/scripts/gold/gold_dispatch.sh`, INSIDE the existing marked block `# >>> PLATINUM-MODE (ADVI_FIRMBKTS FB-f-9) >>>` ... `# <<< PLATINUM-MODE
(ADVI_FIRMBKTS FB-f-9) <<<` (the markers stay exactly as they are; the existing `if ... export BD_PLATINUM_MODE=canonical;
fi` stays byte for byte), add BEFORE it one guard:

```
if { [ "${GOLD_KEEP_ALIVE:-0}" = "1" ] || [ -f "${GOLD_QA_MARKER:-/tmp/GOLD_QA_REBUILD}" ]; } \
   && [ "${BD_PLATINUM_MODE:-}" = "canonical" ]; then
    echo "ERROR: BD_PLATINUM_MODE=canonical is set on a QA invocation (GOLD_KEEP_ALIVE or the QA rebuild marker); the QA runner never writes the served home" >&2
    exit 2
fi
```

(a QA invocation is `GOLD_KEEP_ALIVE=1` or the QA rebuild marker file; a hand run with the preset and neither is not a QA
invocation and is not refused). Nothing else in the file changes.

## 2. BOUNDS

1. One file changes: `data/black_diamond/scripts/gold/gold_dispatch.sh`. No other file; no deploy; no AWS call.
2. The two marked blocks' markers, the export condition and the gate-read block are untouched (the check reads them).
3. ASCII only; LF endings. If something cannot be met within your paths, file a surprise row and stop.

## 3. SURFACES

<paths>
data/black_diamond/scripts/gold/gold_dispatch.sh
org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~38/
org/missions/D8/ADVI/ADVI_FIRMBKTS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the rest of the repository, the checks under `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round4/checks/`.

## 4. PROOF OF SPEC (literal)

<proof_of_spec>
Instance at `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~38/ADVI_FIRMBKTS.TO-FB-g-15.dispatch-qa-guard.proof_of_spec.json`.
  <criterion id="AC1" cell_refs="FB-g-15"><invocation>cd /c/dev/wk-firmbkts-38 &amp;&amp; timeout 100 python org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round4/checks/r4_dispatch.py --arm export --root /c/dev/wk-firmbkts-38; echo "exit=$?"</invocation><expect>ROUND 4 DISPATCH EXPORT: ALL CASES PASS</expect></criterion>
  <criterion id="AC2" cell_refs="FB-g-15"><invocation>cd /c/dev/wk-firmbkts-38 &amp;&amp; timeout 100 python org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round4/checks/r4_dispatch.py --arm gate --root /c/dev/wk-firmbkts-38; echo "exit=$?"</invocation><expect>ROUND 4 DISPATCH GATE: ALL CASES PASS</expect></criterion>
  <criterion id="AC3" cell_refs="FB-g-15"><invocation>cd /c/dev/wk-firmbkts-38 &amp;&amp; timeout 60 python org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round4/checks/r4_scope.py --root /c/dev/wk-firmbkts-38 --allow data/black_diamond/scripts/gold/gold_dispatch.sh --allow org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~38/ --allow org/missions/D8/ADVI/ADVI_FIRMBKTS/surprise-channel/investigations/INVESTIGATION_v1.md --require data/black_diamond/scripts/gold/gold_dispatch.sh; echo "exit=$?"</invocation><expect>ROUND 4 SCOPE: OK</expect></criterion>
  <criterion id="AC4" cell_refs="FB-g-15"><invocation>cd /c/dev/wk-firmbkts-38 &amp;&amp; bash -n data/black_diamond/scripts/gold/gold_dispatch.sh &amp;&amp; echo SYNTAX-OK</invocation><expect>^SYNTAX-OK$</expect></criterion>
</proof_of_spec>

AC1 runs the block under twelve environments (the eight round-3 cases, a QA run with the mode preset to canonical by
keep-alive and by the marker, the same with the mode preset to legacy, and a QA single run with canonical preset). AC2 is a
difference control (the gate-read block is unchanged). AC3 is the write-surface bound. A fourth criterion, AC4, because a
syntax error in the deployed dispatcher stops the whole gold chain. Each invocation terminates inside its bound.

## 5. WHEN YOU ARE DONE

Instance at `D/ADVI_FIRMBKTS.TO-FB-g-15.dispatch-qa-guard.proof_of_spec.json`, `D` = `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~38`.
Commit the file and your rows, then the instance second. **Do not flip this order's `<status>`** (the issuer drains it).
Row ids: `ADVI_FIRMBKTS-D1-W38-S<k>`, `k` from 1, `surfaced_at` from `date -u +%FT%TZ`. Report once: AC1 to AC4 outputs and
the commit hash.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** cut on the CTO's act-0 sign-off condition (`ledger/NEVER_WIDEN_ROUND4_ACT0_GRANT_CTO_HALF.md`); workstream
`QAGUARD`; the dispatcher is one of act 2's 20 permitted objects, so the permitted set is unchanged in count and the block
that act 2 deploys is larger by this guard (act 2's pair addendum names it). Class WORLD like its sibling FB-f-9 phases.

<status>complete</status>
<round>4</round>
<workstream>QAGUARD</workstream>
<to_id>ADVI_FIRMBKTS.TO-FB-g-15</to_id>
<slot>~38</slot>
<fabric>dell1</fabric>
<risk>WORLD</risk>
<worker_class>worker-light</worker_class>
