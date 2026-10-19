# NFRA_MCPORTAL task order -- `MP-z-8` -- WORKSTREAM GWZ ROUND 1: a Gateway segment table lists only the indexes of its own vendor and firm (defect P1)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D6/NFRA/NFRA_MCPORTAL/decompositions/NFRA_MCPORTAL_DECOMP.md</decomp_doc>
<owned_cells>MP-z-8</owned_cells>
</decomp_ref>
<to_id>NFRA_MCPORTAL.TO-MP-z-8</to_id>
<issued_to>0.9.0_WK_NFRA_MCPORTAL~41</issued_to>
<issued_by>2.0.0_SA_COO~MP</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a front-end bundle; no cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- a front-end bundle; no IAM.
comp-adversary: DECLARED-NOT-APPLICABLE -- the named tests plant a foreign index in every segment and assert it does not show; that is the adversary arm.
EGRESS CLASS, declared: none. Make no network call.
</preflight>

## 1. THE CELL -- `MP-z-8` (workstream GWZ round 1, decomposition sections GWZ1.1 and GWZ1.3)

You work in the same two worktrees as your first order `MP-z-7` (`C:/tmp/mp-gwz-41` on branch `wk-NFRA_MCPORTAL-41`, and its nested `C:/tmp/mp-gwz-41/mcportal` on branch `wk-NFRA_MCPORTAL-41-mcportal`), on top of what `MP-z-7` committed. `node_modules` is linked; no `bun install`. Begin each shell call with `cd C:/tmp/mp-gwz-41 &&`. Code changes are committed in the mcportal worktree with plain `git commit`, author `0.9.0_WK_NFRA_MCPORTAL~41 <0.9.0_WK_NFRA_MCPORTAL~41@opal.agent>`; your proof-of-spec instance and any surprise row are committed in the workspace worktree via `.tools/safe-commit.sh --author "0.9.0_WK_NFRA_MCPORTAL~41 <0.9.0_WK_NFRA_MCPORTAL~41@opal.agent>" -F <msgfile> -- <paths>` (message file written with a non-shell writer). Never push either repo. Make NO network call of any kind.

**The defect.** On the Gateway page a bucket's tools are grouped into segments by (vendor, firm). `SegmentSection` in `src/pages/gateway/GatewayView.tsx` hands each tool to `ToolRow`, and `ToolRow` prints `listOrNone(tool.indexes)` unchanged. A tool that serves several pairs therefore lists ALL its indexes under EVERY segment: `client_get_holdings` shows 13 indexes under "Schwab / 49 Financial" of which 6 are Schwab's, 2 Black Diamond's, 2 Commonwealth's, 1 Orion's and 2 SmartX's. The payload carries no pair per index today; the breakdown handler (another project) will add one. This cell builds the page side against the agreed shape.

**The interface (the payload shape the page reads).** `GatewayTool` in `src/api/admin.ts` gains an OPTIONAL field
`index_pairs?: GatewayIndexPair[]`, with a new exported `interface GatewayIndexPair { index: string; vendor: string; firm: string }`: one entry per (index, pair) the index serves, in the server's own order; `vendor` and `firm` are the same strings a `segments[]` entry carries.

**The rule (in a segment section; `tool.indexes` and the channel-level Indexes paragraph stay as they are):**
- if the tool has an `index_pairs` array: show the `index` values of the entries whose `vendor` AND `firm` equal the segment's, each name once, in the order sent; show `none` (the page's own `listOrNone` empty word) if there are none; an EMPTY `index_pairs` array therefore shows `none` under every segment;
- if the tool has NO `index_pairs` key (an older payload): show `tool.indexes` unchanged, exactly as today;
- the tools table of a channel WITHOUT segments keeps listing `tool.indexes` as today.
Make the smallest change: pass the segment into the row (or filter the tool's indexes before the row), keep every existing class and `data-` attribute, and change no styling.

Build (in `mcportal/src/`):
1. `api/admin.ts`: the interface and the optional field above.
2. `pages/gateway/GatewayView.tsx`: the rule above.
3. FIVE tests in `pages/gateway/gateway.test.tsx`, each by its exact name (bun 1.3.x prints a name only on FAILURE, so the check reads the names from your sources; put each as the literal first argument of its `test(...)`). Use SYNTHETIC index names (`idx-sch-1`, `idx-bd-1`, ...), never a real index name:
   - `a segment table lists only the indexes whose vendor and firm are that segment's`: a bucket with two segments, one tool serving both, `index_pairs` giving each segment two indexes; under each segment section the tool row shows its own two and NOT the other segment's two (assert on the section of that segment, e.g. by its `data-segment` attribute).
   - `a tool serving two pairs shows each pair its own indexes`: one index served by both pairs shows under both; an index served by one pair shows under that one only.
   - `a tool with no index_pairs keeps listing its indexes unchanged`: the existing shape (no `index_pairs`) lists all of `tool.indexes` under its segment.
   - `a tool with an empty index_pairs lists none under any segment`: `index_pairs: []` with a non-empty `indexes` shows the empty word under each segment.
   - `the audit case: client_get_holdings shows 6 of its 13 indexes under Schwab / 49 Financial`: a tool named `client_get_holdings` with 13 synthetic indexes split 6 Schwab, 2 Black Diamond, 2 Commonwealth, 1 Orion, 2 SmartX across five segments (the Schwab segment's firm key is the one the existing fixtures use for 49 Financial); the Schwab / 49 Financial section shows exactly 6 names and none of the other 7.
All existing tests keep their names and still pass (the first order's new test included). `bun test src` now reads 79 or more pass and 0 fail. Do not change an existing fixture; add new ones.

## 2. BOUNDS

1. Write surface: exactly the paths in section 3. Do not change `package.json`, `bun.lock`, any gateway (Python) file, Terraform or the manifest. Make no deploy and no network call.
2. Do NOT flip this order's `<status>`: the order file is outside your `<paths>` and the issuer flips it. (This face overrides the worker rule that says to flip.)
3. If a criterion cannot be met without a file outside section 3, REFUSE it with what you measured and file a BLOCKING row. Never repair a criterion; the check script and the proof line are the issuer's.
4. Standing rules: no push and no vendor call; commit as above, each with your serial as author (CLAUDE.md 14a). Do not print or screenshot any real index name.

## 3. SURFACES

<paths>
mcportal/src/pages/gateway/
mcportal/src/api/admin.ts
org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.9.0_WK_NFRA_MCPORTAL~41/**
org/missions/D6/NFRA/NFRA_MCPORTAL/surprise-channel/investigations/**
</paths>

Read, never write: every other mcportal file, `C:/Users/Opal Bloomberg/Desktop/ajb_workspace/portal/DESIGN.md`, and `org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~MP/gwz/checks/`.

Rows go to `org/missions/D6/NFRA/NFRA_MCPORTAL/surprise-channel/investigations/INVESTIGATION_v1.Z.md`, with id `NFRA_MCPORTAL-Z-W41-S<k>` (the next free k for W41). APPEND ONLY: add your row after the last one and leave every earlier byte untouched (the file carries some Windows line endings; do not rewrite or normalise them).
`surfaced_at` = `date -u +%FT%TZ` at filing. `disarm_owner` on an ARMED row is `2.0.0_SA_COO~MP`.

## 4. PROOF OF SPEC (literal; run after your commits)

<proof_of_spec>
  <criterion id="AC1" cell_refs="MP-z-8"><invocation>cd C:/tmp/mp-gwz-41 && bash org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~MP/gwz/checks/z8.AC1.sh; echo "exit=$?"</invocation><expect>named tests present in sources 5 of 5.*fail=0.*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the instance at `org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.9.0_WK_NFRA_MCPORTAL~41/NFRA_MCPORTAL.TO-MP-z-8.segment-table-own-indexes-only.proof_of_spec.json`,
run `proof-of-spec-check.py` on it as the worker rules say, and report once, with:
- the check output of AC1;
- the mcportal commit hash or hashes, and the workspace commit hash;
- every existing assertion you had to change (file, test, old, new), or none;
- `tsc --noEmit -p tsconfig.app.json` in the nested worktree (rc) and `bun run build` (rc);
- any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** cut at the GWZ round-1 issuance (decomposition v19) from the CTO's round analysis `ledger/ROUND_ANALYSIS.z-round1.md` @11c572fef9, item 1 (defect P1, class display). Queued second on slot ~41 behind MP-z-7 (same files; one chain).
The `index_pairs` shape is the issuer's contract (decomposition GWZ1.1), sent to `2.0.0_SA_COO~O` for NFRA_OPLGTW round 47; if that round lands a different shape, the issuer amends this order and the check, not the worker. Fixtures only: no seam probe against the real handler is possible until the field is live (owner-gated). The change reaches the host only with the next mcportal bundle release AND the handler's field; nothing in this order deploys. The status flip is the issuer's.
z8.AC1 base: FAIL as expected (`bun test src` 73 pass, 0 fail; named tests present in sources 0 of 5; min 79), run in the provisioned slot-41 worktree at mcportal 59e802a, 2026-10-19 ~20:1xZ.

<status>pending</status>
<round>1</round>
<workstream>GWZ</workstream>
<slot>~41</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
