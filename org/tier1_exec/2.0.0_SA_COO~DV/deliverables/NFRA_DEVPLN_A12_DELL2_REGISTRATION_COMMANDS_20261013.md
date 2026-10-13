# NFRA_DEVPLN act A12 -- register the three IRPT_ANLREQ merges as approval rows on dell2's list (for 1.0.0_SA_CTO~DELL2's seat)

Ground: CTO ruling `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_RULING_20261013_213xZ_LAPTOP_E846_7D95_BB8B.md` (call bb8b): the three IRPT_ANLREQ merges that reached portal DEV before the route existed are re-registered as one approval row each, client-facing, for Andrew. DEV is not rewritten.
Why dell2 runs it: a row for `cand/dell2/<slug>` lives on dell2's own open-calls list and `add` refuses another box's list.
Issuer: `2.0.0_SA_COO~DV`, 2026-10-13. Decomposition: `org/missions/D0/NFRA/NFRA_DEVPLN/decompositions/NFRA_DEVPLN_DECOMP.round3.md` act A12.

## Already done by the issuer (verified with ls-remote on portal origin)

| ref on origin | points at | commits over PROD |
|---|---|---|
| `cand/dell2/anlreq-90-held-submit` | `794b7df495d2baa3d2f887f148f4389e729ca07d` | 2 (`923f7d69`, `794b7df4`) |
| `cand/dell2/anlreq-88-advisory-fee` | `9ef6a359b80750cff51e18369d68035f73a046af` | 1 |
| `cand/dell2/anlreq-87-model-order` | `62d455f57525b9037a6bc7377a6f13e24ad86c05` | 1 |

Each is a feature head that DEV already merged (`73d8d3a4`, `0101dd66`, `a577cba5`). The refs only name existing commits; no commit was created or moved.

## Precondition

`.tools/open-calls.py` on dell2 must carry the waiver flags (`add --kind approval --waive-overlap`, cell `DP-d-1`, not yet merged at this writing). Check: `python .tools/open-calls.py add --help | grep waive-overlap` prints a line. If it prints nothing, stop and wait for the box-sync that brings it; do not register without the waiver (the DEV-overlap refusal would stop it).

## The three commands (run from the dell2 workspace root, on dell2, with the portal checkout at `portal`)

```
python .tools/open-calls.py add --kind approval --project NFRA_DEVPLN --box dell2 --branch cand/dell2/anlreq-90-held-submit --purpose "Analysis Request submit says in words what stopped it (a held or failed submit); the held-reason block takes the 4px radius. Already on DEV via merge 73d8d3a4." --pages "src/pages/TicketCenter (AnalysisRequestParts, TicketCenter, analysisRequest)" --class client-facing --how "git -C portal diff origin/PROD...origin/cand/dell2/anlreq-90-held-submit; the page is Ticket Center, New Analysis Request" --portal portal --waive-overlap 923f7d69,794b7df4 --waiver-ref org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_RULING_20261013_213xZ_LAPTOP_E846_7D95_BB8B.md --asked-by <your serial> --source org/tier1_exec/2.0.0_SA_COO~DV/deliverables/NFRA_DEVPLN_A12_DELL2_REGISTRATION_COMMANDS_20261013.md --context "Re-registration of a feature that reached DEV before the approval route existed (CTO ruling on call bb8b). Client-facing, so Andrew rules it. Approved: it stays on DEV and may ship in the next chosen-set promote. Declined: it needs a decision on DEV (not a rewrite)."

python .tools/open-calls.py add --kind approval --project NFRA_DEVPLN --box dell2 --branch cand/dell2/anlreq-88-advisory-fee --purpose "The Analysis Request form no longer shows the Advisory fee field. Already on DEV via merge 0101dd66." --pages "src/pages/TicketCenter (AnalysisRequestParts, analysisRequest)" --class client-facing --how "git -C portal diff origin/PROD...origin/cand/dell2/anlreq-88-advisory-fee; Ticket Center, New Analysis Request form" --portal portal --waive-overlap 9ef6a359 --waiver-ref org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_RULING_20261013_213xZ_LAPTOP_E846_7D95_BB8B.md --asked-by <your serial> --source org/tier1_exec/2.0.0_SA_COO~DV/deliverables/NFRA_DEVPLN_A12_DELL2_REGISTRATION_COMMANDS_20261013.md --context "Re-registration of a feature that reached DEV before the approval route existed (CTO ruling on call bb8b). Client-facing, so Andrew rules it. Approved: it stays on DEV and may ship in the next chosen-set promote. Declined: it needs a decision on DEV (not a rewrite)."

python .tools/open-calls.py add --kind approval --project NFRA_DEVPLN --box dell2 --branch cand/dell2/anlreq-87-model-order --purpose "The Analysis Request model checkboxes list in canonical order and colors. Already on DEV via merge a577cba5." --pages "src/pages/TicketCenter (AnalysisRequestParts)" --class client-facing --how "git -C portal diff origin/PROD...origin/cand/dell2/anlreq-87-model-order; Ticket Center, New Analysis Request, model checkboxes" --portal portal --waive-overlap 62d455f5 --waiver-ref org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_RULING_20261013_213xZ_LAPTOP_E846_7D95_BB8B.md --asked-by <your serial> --source org/tier1_exec/2.0.0_SA_COO~DV/deliverables/NFRA_DEVPLN_A12_DELL2_REGISTRATION_COMMANDS_20261013.md --context "Re-registration of a feature that reached DEV before the approval route existed (CTO ruling on call bb8b). Client-facing, so Andrew rules it. Approved: it stays on DEV and may ship in the next chosen-set promote. Declined: it needs a decision on DEV (not a rewrite)."
```

Each command prints `APPROVAL-REGISTER result=OK row=<id> head_sha=<sha> commits=<n> waived=<n>` (waived 2, 1, 1) and `ADDED id=...`. A refusal prints its reason; do not retry with a wider waiver. The waiver names commits, never a count or range.
Afterwards `python .tools/open-calls.py approval-status --branch cand/dell2/anlreq-90-held-submit` (and the other two) reads `state=OPEN class=client-facing`. The rows are then Andrew's to rule on the open-calls list. Report the three row ids to `2.0.0_SA_COO~DV`.
