# NFRA_DEVPLN -- ROUND-4 ANALYSIS (1.0.0_SA_CTO, 2026-10-13 ~23:3xZ)

**On:** the issuer's drain end `org/tier1_exec/2.0.0_SA_COO~DV/deliverables/NFRA_DEVPLN_ROUND4_DRAIN_END_20261013.md` (3 of 3 orders,
MAY-CLOSE; no SERVED or WORLD order, so no CVO packet). **PRD:** v0.3, unchanged. **Next:** round 5 in ONE issuance on section 3.

## 1. What round 4 moved

- **DP-e-1:** a `withdrawn` decision for an OPEN approval row, with `approval-status` ignoring withdrawn rows.
- **DP-e-3:** the merge-base warning is gone, with the verdict unchanged (and controlled).
- **DP-e-2:** `approval-status` reads another box's list from its freshest source. The laptop now reads dell2's four rows live.
- **S03 and the refusal arm (A7):** the gate blob `fcdbc6e1` is identical on all four box branches and on CLOUD. A direct DEV push
  from a box seat is refused, run from a scratch worktree so it is the refusal and not a HEAD false positive.
- **dell2 registered its rows** under the four-commit waiver: `8500`, `7b45` and `fde0`. It also registered its first organic
  client-facing feature (`cand/dell2/irpt-ytd-from-first-day-and-wider-export-modal`), twice.

## 2. Rulings

- **The duplicate `cffa` / `3635`: withdraw the OLDER row, `cffa`,** with `close --decision withdrawn` (DP-e-1), on dell2. This
  supersedes my earlier relay, which said `declined` and was sent before `withdrawn` existed. The newest row, `3635`, then carries
  the feature, and Andrew rules only `3635`. The issuer's relay `NFRA_DEVPLN_A13_DELL2_WITHDRAW_DUPLICATE_20261013.md` goes through
  `0.0.0_AB_MSTR`, naming `cffa`.
- **The pre-push payload limb's exempt routes are RIGHT:** an approved merge, a test-only change, a PROD-into-DEV back-merge, and a
  live FAST lease's seat. These keep both CLAUDE.md law routes (FAST and test-only) exactly as written while that law-edit card
  (`laptop-...-3d7e`) waits on Andrew. Every other push to `refs/heads/DEV` fails closed, scripted or typed. Installing it is the
  hook's lane owner's act (`install.sh`), named in the cell.

## 3. ENRICHMENT LIST for round 5

1. **The pre-push payload limb, FIRST** (`.tools/portal-hooks/pre-push` plus a separate checker; carrier `NFRA_DEVPLN-S3`; draft
   `deliverables/drafts/ROUND5_DRAFT_dev-push-payload-limb.md`). It must show three things:
   - a typed or scripted direct push of an unapproved commit to DEV is refused;
   - an approved merge passes;
   - each exempt route passes.
2. **After Andrew rules the dell2 rows:** the integrator's merge-forward of each approved feature, then the DT's chosen-set promote
   naming only what he approved. This is FWD-1's client-facing close (a DT order at that time).
3. **One repair batch:** W1-S14 (one test seam variable, not two) and W2-S11 (exit checks on the self-test fixture writes). W1-S13,
   the gitlink drift, is read and recorded only, with no cell unless it breaks a read.
EOF
python -c "
import sys
open(sys.argv[1],'w',newline='\n').write('''analysis(NFRA_DEVPLN round 4, 1.0.0_SA_CTO): ROUND-4 ANALYSIS -- S03 identical on all four boxes and refusing; dell2 rows registered; duplicate cffa withdrawn (supersedes the declined relay); pre-push limb's exempt routes ruled right (keep the CLAUDE.md FAST and test-only routes); round-5 list: the limb first, then the dell2 features' merge-forward and chosen-set promote after Andrew rules, one repair batch

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01HrgHgTgkFFWYWaFwdqXHyn
''')" "C:/Users/ANDREW~1/AppData/Local/Temp/claude/C--Users-AndrewBerman-Desktop-ajb-workspace/983d694c-448d-4cc5-85bd-31b593bb5b52/scratchpad/msg_dv4.txt" && bash .tools/safe-commit.sh --author "1.0.0_SA_CTO <1.0.0_SA_CTO@opal.agent>" -F /cygdrive/c/Users/ANDREW~1/AppData/Local/Temp/claude/C--Users-AndrewBerman-Desktop-ajb-workspace/983d694c-448d-4cc5-85bd-31b593bb5b52/scratchpad/msg_dv4.txt -- org/missions/D0/NFRA/NFRA_DEVPLN/ledger/ROUND_ANALYSIS.round4.md > /tmp/sc.out 2>&1; echo rc=$?; git log -1 --format='%h~%an'