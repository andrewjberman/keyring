# Andrew-direct 2026-09-24 ~03:0xZ at the 1.0.0_SA_CTO terminal -- Anna's Holdings table renders; two new findings

Seat: 1.0.0_SA_CTO (Claude). Context: Andrew retested Anna (****9237) Holdings at localhost:5174 after the
fence exemption (02:04Z) and the success-status deploy (02:45Z).

## VERBATIM

"Just tested out Anna, what is interesting is she didn't show up under the "Global" view, which is bullshit
because *EVERYONE* should show up under "Global" view (default view for Opal users), because its global. She
did however show up underneath the "Cottonwood" Drop down; i became suspicious and had to check if it was a
dropdown issue. IT doesn't show her model holdings, her opal model breakdown, her opal asset taxonomy class
breakdown, but it does show a dollar value that is real and some UI taking shape so thats a start"

Screenshot (transcribed): Current value USD 26,303,302.17 | Unique accounts 1 | Source dates Business
2026-09-22, Observed 2026-09-24T00:28:11Z | Model coverage 0 of 1 accounts. ASSET CATEGORY VIEWS / ALL
CATEGORIES: Total Assets $26.30M, one slice "acc_0698a3de842dbe7b3d48c787:models" $26.30M, 100% of total.
Node table: acc_0698a3de842dbe7b3d48c787:models | basis observed custody | USD 26,303,302.17 | denominator
26,303,302.172 | 100.00% | 100.00% | Supervision withheld | Advisory withheld | Prove(nance) holdi... (cut).
Footer: September 22nd, 2026, 5:00p ET | Source: Opal Capital Analysis.

## WHAT IT ESTABLISHES

1. EXERCISED: the served Holdings request for an Opal user now returns READY and the portal renders the
   table. Both fixes of this window are exercised end to end: the firm-bucket fence exemption for
   irpt-holdings-role (IRPT-HOLDINGS-NOT-READY-ROOT-CAUSE-20260924) and the success status
   (IRPT-HOLDINGS-SUCCESS-STATUS-20260924). The first request that rendered a table is Andrew's own.
2. NEW FINDING A -- GLOBAL VIEW MEMBERSHIP: Anna appears under the Cottonwood dropdown and NOT under the
   Global view. Standing authority (takeover handoff, restated here): Opal users have all functions for any
   firm / client / account; Global is the default view for Opal users; everyone appears under Global.
   Routed to 2.0.0_SA_COO~P (100044): measure what resolve-scope / directory-browse / directory-search
   return for an Opal principal at context GLOBAL, which firms' directories the GLOBAL union reads and from
   which artifacts, and whether cottonwood's directory is in it at all. The CTO rules the fix on the fact.
3. NEW FINDING B -- MODEL / TAXONOMY BREAKDOWN: for acc_0698 the screen shows one "models" node at 100%
   with observed-custody basis, "Model coverage 0 of 1 accounts", no model holdings, no Opal model
   breakdown, no asset-taxonomy class breakdown, and Supervision / Advisory "withheld". Routed to
   2.0.0_SA_COO~M (100043): what the accepted COT publication carries for 0698 (node kinds, model leaves,
   holdout status), the same for d486 and the combined selection, which coverage field the portal reads,
   and whether "withheld" is the data's attribution/drill projection, the server's authority projection
   (P answers that half, 100044 item 3), or the portal's rendering of an absent field.

## NOTHING WIDER IS INFERRED

The word states two facts and one standing rule. No new project, no scope change to the resident cutover,
no change to the fence or status rulings. Records: RULINGS.md batch 19/20 under
IRPT_MVP_COMPLETION_20260922/; push state LOCAL at write (origin/CLOUD f96a0b9dd4 per MSTR 99987).
