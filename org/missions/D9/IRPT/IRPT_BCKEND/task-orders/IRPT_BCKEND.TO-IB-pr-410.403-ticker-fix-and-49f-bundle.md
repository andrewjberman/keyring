# TO IRPT_BCKEND.TO-IB-pr-410 -- IB-pr-403 fixed (SmartX CUSIP nodes keep `ticker=` for display and classification) and the 49F narrow bundle rebuilt with dell1's e56; supersedes IB-pr-406

<to_id>IRPT_BCKEND.TO-IB-pr-410</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~273</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-09</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>111</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** row D2-W269-S1 (IB-pr-406's replay: on real 49F inputs the FWD-14 gate REFUSES), disposed by D2-S53; CTO ruling D1-S8 AMENDMENT 2 @b58f09e1b8 | **Decomp cell:** `IB-pr-410` (decomposition section 104) | **outcome_ref:** FWD-2

---

## WORKER FACE

**The defect.** IB-pr-403 (code `dfa9b72cc9`) gives 115,412 49F SmartX SECURITY nodes `security_id {CUSIP, ...}` in place of
`{TICKER, ...}`. `holdings_snapshot.fill_display_from_facts` reads the symbol from a `ticker=` fact, or from a TICKER `security_id`
(`holdings_snapshot.py:803`), so those nodes lose `display.symbol`. 13,892 then lose their class, and the FWD-14 publish gate refuses
49F (`classified_security_lost` 53, `new_unclassified` 6). Worker ~269 measured this in
`C:/dev/wk-irpt-bckend-273/org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~269/` (read its packet, census, replay
and scripts first). Custody rows already carry a `ticker=` fact for exactly this reason (`holdings_49f.py`, the Schwab position loop).

**1. Fix** `data/assets/scripts/gold/investor_reporting/holdings_49f.py`:
- In the SmartX `model_positions` loop, every SECURITY node whose row has a ticker carries the classification fact `ticker=<ticker>`. This
  holds whether its `security_id` is CUSIP or TICKER.
- Keep IB-pr-403's CUSIP rule, its `cusip_basis` fact and its listing unchanged.
- Test, in `tests/test_holdings_49f.py`, named with `smartx_cusip` and `keeps_ticker`: a SmartX node carrying a CUSIP still gets
  `display.symbol` == its ticker after `fill_display_from_facts`. IB-pr-403's three `smartx_cusip` tests still pass.

**2. Rebuild the 49F narrow bundle** exactly as ~269 did. Write the census to
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~273/IB111-1_49f_bundle_census.json`, same shape as IB107-1's.
- The base is IB-pr-402's built 49F bytes, sha256 `3f2e738f83aa415a2b56cf506d54368f9d2f86f7ded8f19202fc373ef6a28901`. It is live since
  IB-pr-404: verify the live object hashes to it.
- `holdings_snapshot.py` is the narrow member plus `01e843ce2e` (blob `e39636c5a8`).
- `holdings_49f.py` is the base member plus the diff of `dfa9b72cc9` plus your fix.
- Use python 3.12 and LF bytes, pack twice to byte-identical output, and upload nothing.

**3. Replay** on real 49F inputs (AWS reads only, scratch outside the worktree, deleted file by file). Write
`IB111-1_49f_bundle_replay.json` `{arms:[{name, verdict, negative_control, detail}]}`, with verdicts exactly `identical` or `expected-diff`:
- `fwd14_gate_unchanged`, **identical**: the gate outcome and conditions are the same on both trees.
- `smartx_class_parity`, **identical**: no SmartX node is classified on base and unclassified on built. Give the counts.
- `symbol_miss_cusip_fallback`, expected-diff.
- Custody e56 arm, expected-diff: newly classified via CUSIP, 0 lost.
- At least one negative control: the ~269 build, with the unfixed 403, still refuses.

**4. Packet** `NEVER_WIDEN_SIGNOFF_PACKET_IB-pr-410.md`: ONE S3 key and two members, the served change in counts, the landing path as in
the 402 packet (digest-gated, never a mint), Branch A, and Branch B (copy back `irUPjpfrDLoM2zhnhunbBtIG9fP275kI`, the 404-landed version;
re-read it at apply). Name the base and built sha256 and the pair: ~P2's COO half, dell1 `2.0.0_SA_COO~M1`'s COO half for the e56 member
(via MSTR), and the CTO half. Print the ADDENDUM 18 red list and show your members touch none of its targets. Note row W269-S2 (e56's
uncached CUSIP misses: runtime).

<criterion id="IB111-1-AC1" cell_refs="IB-pr-410"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r111/p111_cells.py" . IB111-1-AC1</invocation><expect>IB111-1-AC1 PASS</expect></criterion>
<criterion id="IB111-1-AC2" cell_refs="IB-pr-410"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r111/p111_cells.py" . IB111-1-AC2</invocation><expect>IB111-1-AC2 PASS</expect></criterion>
<criterion id="IB111-1-AC3" cell_refs="IB-pr-410"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r111/p111_cells.py" . IB111-1-AC3</invocation><expect>IB111-1-AC3 PASS</expect></criterion>

<expected_criteria>IB111-1-AC1, IB111-1-AC2, IB111-1-AC3</expected_criteria>

## BOUNDS

- **Grant:** the `<paths>` block and nothing else. Code, tests, BUILD_ONLY and offline replays; no upload, apply or deploy. AWS reads only.
- **Do NOT touch `holdings_snapshot.py`** in the tree; it is dell1's. The e56 member is composed only in the bundle.
- **Every `.py` edit passes `.tools/commit-gate.sh`**; safe-commit runs it.
- **Client data:** extracted trees and node files stay OUTSIDE the worktree and are deleted at the end (file-by-file, never a recursive delete).
- **Refusal clause:** if a criterion cannot be met as written, stop, file a row, and report. Never weaken a check or a test.
- **Row ids** are `IRPT_BCKEND-D2-W273-S<k>`; `surfaced_at` is the real time; check the id is still free just before you commit.
- **Commit with** `GIT_COMMITTER_NAME="0.9.0_WK_IRPT_BCKEND~273" GIT_COMMITTER_EMAIL="0.9.0_WK_IRPT_BCKEND~273@opal.agent" bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~273 <0.9.0_WK_IRPT_BCKEND~273@opal.agent>" -F <msgfile> -- <paths>`. Write the message file with the Write tool, OUTSIDE the worktree; do NOT pre-`git add`. ASCII only.
- **Search:** raw recursive grep/find in Bash is gated; use the native Grep/Glob/Read tools.

<paths>
data/assets/scripts/gold/investor_reporting/holdings_49f.py
data/assets/scripts/gold/investor_reporting/tests/test_holdings_49f.py
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~273/
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-410.403-ticker-fix-and-49f-bundle.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 104 (round 111, workstream ~P), cell `IB-pr-410`.
<owned_cells>IB-pr-410</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB111-1-AC1, IB111-1-AC2, IB111-1-AC3. The instance goes at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~273/IRPT_BCKEND.TO-IB-pr-410.403-ticker-fix-and-49f-bundle.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE the flip to complete.
</proof_of_spec>

**REPORT:** in your final message, give the fix, the test names, the base and built sha256, the replay verdicts and counts, each criterion's last line and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: RUN -- holdings_49f.py's SmartX loop gains a ticker= fact (display/classification only; security_id rule unchanged); ONE S3 key (49financial bundle), two members; nothing uploaded by this cell.
comp-iam: DECLARED-NOT-APPLICABLE -- no permission change.
comp-routes: DECLARED-NOT-APPLICABLE -- no route change.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- p111_cells.py dry-run at base box/dell2 on dell2 2026-10-09 ~13:3xZ: AC1 FAIL (no keeps_ticker test), AC2 + AC3 FAIL (no census/replay); 0 control bytes; ruff clean.
lane: the <paths> block IS the grant; ~P's (IB-pr-403's defect, row D2-W269-S1).
</preflight>
