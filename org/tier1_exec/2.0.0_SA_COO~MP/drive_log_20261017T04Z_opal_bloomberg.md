# Drive log -- 2.0.0_SA_COO~MP, NFRA_MCPORTAL, 2026-10-17 ~04:3xZ to ~05:3xZ (host opal_bloomberg, site Z)

Substantive ticks only; the runtime file is `org/mcp/drive_ticks/2.0.0_SA_COO~MP.md` (gitignored). Push state, measured by `git fetch origin box/sitez` then `merge-base --is-ancestor` against origin/box/sitez d074d34726: 68b0364acd (the Z-S74 ruling) is ON origin; b3176d53a8 (Andrew's word "they are all clear + go") is ON origin.

| time (Z) | limb | outcome | act |
|---|---|---|---|
| ~04:27 | wait | WAIT | 02Z-04Z log committed (31e3e8f697); no mail; manifest d3ae88be46 / mcportal 59e802a |
| ~04:45 | Andrew-direct | DRIVE FORWARD | Andrew: "they are all clear + go" (the three-route close run and the go for the MP-v-2 window, call f0d2); relayed to COO~O for Z-S312; record file committed (b3176d53a8); pre-checks (admin_api.py Route census 12 = the check's denominator; deny guard None, None, 403); spawned worker ~3 (headed Edge, 10-minute wait for the Opal Bloomberg sign-in) |
| ~04:57 | measure | DRIVE FORWARD | the window opened 04:52:43Z and a sign-in completed 04:55:48Z; the first request GET / answered 200 and the worker stopped per bound 2 (1 of 13 sent); issuer read of the code: the owner roster may hold only andrew@, a non-owner answers 403; one read-only GET /api/admin/whoami through the window's own profile, headless: status 200, the email IS the dashboard owner: the window signed in as the owner, not Opal Bloomberg |
| ~05:12 | rule | DRIVE FORWARD | worker ~3's report: AC1 FAIL (refused=0 of 13, admitted=1), AC2 PASS (/sprint 200=2 of 2), rows Z-W3-S4 (BLOCKING) and Z-W3-S5; issuer re-ran both checks (identical); drained ba2f0a86cf; Z-S74 adjudicates S4 (its premise, a non-owner session, is false) and S5 (a non-defect), 68b0364acd; armed in the project 7, the issuer's two carried on purpose; MP-v-2 stays open for a redo as Opal Bloomberg on a fresh profile |
| ~05:27 | wait | WAIT | no mail, manifest unchanged; owed from Andrew: his word "again" and his presence for the second window |

Open: the second MP-v-2 window as Opal Bloomberg (call f0d2; needs Andrew at the screen, a fresh profile, the account chosen explicitly); calls 8ed7 and def4 are his acts; `~O`'s Z-S312 disarm on his three-route answer is COO~O's ruling; PD held by the CTO until OG-cp-1 and Andrew's sitting; MP-pd-7 staged to ~NFRA1 (MSTR~Z told at the GO); Z-W28-S1 and Z-W32-S1 are the issuer's two armed rows, carried on purpose (Z-S73).
