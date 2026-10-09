# NFRA_OPALAI task order -- `OA-f-15` -- DIRECT ACT: port the post-move Teams fixes (oid pin, 29.5-minute bound, Andrew's sender gate) into the Analyst's opal_ai copies

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D6/NFRA/NFRA_OPALAI/decompositions/NFRA_OPALAI_DECOMP.md</decomp_doc>
<owned_cells>OA-f-15</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_OPALAI~25</issued_to>
<issued_by>2.0.0_SA_COO~AI</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- two markdown files; no cron, alarm, monitor or cadence is created.
comp-iam: DECLARED-NOT-APPLICABLE -- nothing reaches AWS.
comp-adversary: DECLARED-NOT-APPLICABLE -- AC2 is byte-equality against the ruled source text.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `OA-f-15` (issuer repair inside round 2, rows Z-S67 and Z-S68)

The Teams Analyst (`opal_ai`, run by the `Opal_Agent` account) was moved out of the workspace on 2026-10-01. After the
move, five commits changed the WORKSPACE copies of two moved files, for the old Bloomberg concierge seat. The Analyst's
copies in `opal_ai` never received them:
- `16fb949b5b`, `8dc1796e31`: the Teams watcher's identity pin. `--identity opalbloomberg` can never match: since the
  2026-10-08 reauth the `opal-gateway-bbg` token's `sub` is `<tenant>/<oid>`, with no UPN. The pin is the Opal Bloomberg
  account's Entra object id, `517aa5ee-b4d0-425a-b493-5a22ff77ac4f`.
- `8773f12204`: the watcher has no exit of its own, so its arm line runs under `timeout 1770` (29.5 minutes).
- `ef8c4e57a1` + `0c9fbd0876`: step **0b. SENDER GATE**, Andrew-direct 2026-10-09 ~03:3xZ: reply to no one whose
  identity is not shown as an Opal user.

Your nested base is opal_ai `c9983bd2ac` (origin PROD). Build there, changing exactly two files:

1. **`opal_ai/opal/agent/skills/bbg-teams-assist/SKILL.md`.**
   - Every `--identity opalbloomberg` becomes `--identity 517aa5ee-b4d0-425a-b493-5a22ff77ac4f`.
   - The step-0 arm line becomes
     `timeout 1770 python opal/agent/teams_watch/teams-watch.py --server opal-gateway-bbg --identity 517aa5ee-b4d0-425a-b493-5a22ff77ac4f`.
     Directly above it, add the workspace copy's two explanations, with the paths adapted to `opal/agent/teams_watch/`:
     why the `timeout 1770` prefix ends the python, and why the pin is the oid.
   - Insert step **0b** between step 0 and step 1: the block that starts with the line `**0b. SENDER GATE` and ends just
     before the line starting `**1. ACK`. Copy it BYTE-FOR-BYTE from the workspace skill at
     `git show 33837fdea8:.claude/skills/bbg-teams-assist/SKILL.md`, lines 51-70, AMENDMENT 1 bullet included. Change no
     word of it.
2. **`opal_ai/opal/agent/refs/RELAUNCH.md`.** Every `--identity opalbloomberg` becomes the oid. Next to the arm line, add
   the workspace copy's "Pin form = Opal Bloomberg's Entra object id" paragraph, and change the verification rows that
   name `identity=opalbloomberg` to the oid form. Take this text from `git show
   33837fdea8:org/tier0_utility/0.0.3_BG_BBGTerminal/refs/RELAUNCH.md`. Leave this copy's P3 row exactly as it is: in the
   runtime the fence stays wired, so the workspace's P3 retirement does not apply here.

## 2. BOUNDS

1. **`opal_ai` is a nested repository** at `<worktree>/opal_ai`, on its own branch off `c9983bd2ac`. Commit with
   `git -C opal_ai commit --author "0.9.0_WK_NFRA_OPALAI~25 <0.9.0_WK_NFRA_OPALAI~25@opal.agent>" -F <msgfile> --
   <nested paths>`, the msgfile written with the Write tool. The parent `opal_ai` gitlink is NOT yours.
2. Read the workspace copies only through `git show 33837fdea8:<path>`. Never edit them.
3. Never run the launcher, teams-watch.py, or any process as `Opal_Agent`. No push, no install, no vendor call. REFUSE a
   criterion you cannot meet as written and report the refusal with its measurement. Never repair a criterion, widen it,
   or meet it by a route this face does not name.

## 3. SURFACES

<paths>
opal_ai/opal/agent/skills/bbg-teams-assist/SKILL.md
opal_ai/opal/agent/refs/RELAUNCH.md
org/missions/D6/NFRA/NFRA_OPALAI/deliverables/0.9.0_WK_NFRA_OPALAI~25/**
org/missions/D6/NFRA/NFRA_OPALAI/surprise-channel/investigations/**
</paths>

Rows: `org/missions/D6/NFRA/NFRA_OPALAI/surprise-channel/investigations/INVESTIGATION_v1.Z.md`, id
`NFRA_OPALAI-Z-W25-S<k>` (none exist at the cut; the first is S1). `surfaced_at` = `date -u +%FT%TZ` at filing.

## 4. PROOF OF SPEC (literal; run from your worktree root, after the nested commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OA-f-15"><invocation>bash org/missions/D6/NFRA/NFRA_OPALAI/deliverables/2.0.0_SA_COO~AI/round2/checks/f15.AC1.sh; echo "exit=$?"</invocation><expect>name pins left=0; skill oid pins>=2; RELAUNCH oid pins>=1; bounded skill arm line=1; sender gate before ACK=yes; other files changed vs c9983bd2ac=0 -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OA-f-15"><invocation>bash org/missions/D6/NFRA/NFRA_OPALAI/deliverables/2.0.0_SA_COO~AI/round2/checks/f15.AC2.sh; echo "exit=$?"</invocation><expect>sender-gate block: workspace@33837fdea8 lines=19, opal_ai@HEAD lines=19, byte-equal (CR-stripped)=yes -- RESULT: PASS -- exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D6/NFRA/NFRA_OPALAI/deliverables/0.9.0_WK_NFRA_OPALAI~25/NFRA_OPALAI.TO-OA-f-15.analyst-teams-pin-and-sender-gate-port.proof_of_spec.json`,
committed on your parent branch. Report once: the nested commit hash, both criteria's output verbatim, the parent commit
hash, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (2.0.0_SA_COO~AI, 2026-10-09 ~11:5xZ):** a direct act cut by the issuer inside its own decomposition
(`/canonical-drive` obligation 7), from the cutover pre-check that UB-20261009T111704Z-fafc item 2 ordered (CTO fold
@6d0e23e25f). `git merge-tree HEAD wk-NFRA_OPALAI-12` read modify/delete on the two moved files (row Z-S67). Per-commit
ruling on the five post-move edits:
- PORTED: `16fb949b5b` (oid pin), `8773f12204` (29.5-minute bound), `ef8c4e57a1` (sender gate, Andrew-direct),
  `0c9fbd0876` (AMENDMENT 1, the field to read), and `8dc1796e31` RELAUNCH pin half.
- RETIRED: `8dc1796e31` P3 row. LD-0580 unwired the fence in the WORKSPACE. OA-t-3 moves the fence into the runtime and
  wires it there by design, so the runtime's P3 row stays.
Row Z-S68: the Analyst's watcher pin `--identity opalbloomberg` matches 0 token records (measured by `1.0.0_SA_CTO~Z` on
2026-10-09 for the same `opal-gateway-bbg` record). The organic serve is therefore broken until this cell lands.

Dry-run at base (`OA_F15_REF=c9983bd2ac`): f15.AC1 FAIL as expected (`name pins left=3; skill oid pins=0; RELAUNCH oid
pins=0; bounded skill arm line=0; sender gate before ACK=no; other files changed=0`); f15.AC2 FAIL as expected
(`workspace@33837fdea8 lines=19, opal_ai lines=0, byte-equal=no`). The controls hold: the workspace block is non-empty and
other files 0.

Release: the nested commit reaches opal_ai DEV and PROD by `0.0.0_AB_MSTR~Z`'s push. After this lands, the OA-t-1 r2
cutover merge keeps the HEAD side of the two workspace files out of the cutover. The ported content now lives in opal_ai,
so the deletions lose nothing. Re-run the merge dry-run to confirm.

SPAWN ONLY WHEN: at the cut. Slot `~25`, worker-light, nested `opal_ai=c9983bd2ac`.

**DRAIN (issuer, 2026-10-09 ~12:3xZ):** worker `~25` nested `13bc631` (2 files, +43/-7), proof @be2fa80dfb, drained
@ad6682bc89. Issuer re-grade from the worker tree: AC1 PASS (`name pins left=0; skill oid pins=3; RELAUNCH oid pins=1;
bounded skill arm line=1; sender gate before ACK=yes; other files 0`), AC2 PASS (19 of 19 lines byte-equal); the P3 row
is untouched. Release: `13bc631` (parent `c9983bd`, a fast-forward) to opal_ai DEV and PROD by `0.0.0_AB_MSTR~Z`.

<status>pending</status>
<status>complete</status>
<direct_act>true</direct_act>
<slot>~25</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
