# Andrew-direct 2026-10-11 ~16:1xZ -- four open-call answers (at the 1.0.0_SA_CTO terminal, laptop)

VERBATIM: "Open Calls: 1.) Yes I did receive the text. 2.) I need more clarity/context on what is going on here. 3.) No for
now, I would need to visual smoke that + want a breakdown of the changes in the DEV build not yet on PROD. 4.) Yes sure."

The four, in the order this seat listed them to him (cluster-lead ticks 12-16):

1. **dell1-20261011T113148Z-c290** (ADVI_FIRMBKTS, SEV1 alert texts): the one test text from the registered toll-free number
   ARRIVED. Reading: the number works; the fault is SNS routing to it, not the number. Row closes on this record; the row's
   own REC proceeds (route SNS to the number, no cost; no AWS Support case). Relayed to dell1 through `0.0.0_AB_MSTR`.
2. **dell1-20261011T053810Z-fe9b** (MDPF_CANON, X2 global fold (a)/(b)): NOT decided. He wants more clarity and context. This
   seat answers in plain words in the same turn (below) and the row stays OPEN at Andrew.
3. **dell1-20261011T033643Z-e7f2** (AMGT_RESAPP, portal PROD promote): NO for now. He needs a visual smoke of the DEV build and
   a breakdown of the DEV-not-on-PROD changes first. Breakdown measured this turn (section A). Row stays OPEN, held at Andrew;
   dell1 told through `0.0.0_AB_MSTR` that nothing promotes.
4. **CLAUDE.md rule 14a** names the per-box git-author override audit log as the instrument: YES. Law edit under this record
   (`ANDREW_LAW_EDIT_ORDER`), one line, same turn, broadcast same turn.

## A. Portal: what is on DEV and not on PROD (measured 16:0xZ, `git log origin/PROD..origin/DEV` after fetch)

PROD `37aa1247`, DEV `00cbfdb3`: 121 commits, 124 files, +5,789 / -477 lines. Files per page (product files, tests excluded):

| page | product files | class | what changed (headline) |
|---|---|---|---|
| InvestorReporting | 36 (90 incl. tests) | CLIENT-FACING (partner logins open it) | DSGN_IRPTV1 rounds IV-e-89..105: Opal report opened on the page reads Opal wording not the vendor's (print/export too); Holdings opens on the picked account's Models/SMAs/Client split; history reader admits the contract page; trading calendar regenerated from `lib/trading_calendar.py`; Prospect upload opens with no client in header; header display-name carriers regenerated; IRPT_ANLREQ reason-code set regenerated |
| TicketCenter | 4 (13 incl. tests) | CLIENT-FACING (unsure = client-facing) | Analysis Request form offers catalogue Opal models and the caller's allowed firms; one-step filing records the request id on the ticket; Open report opens the finished report; package files open through IRPT's reader; Trade Request form (NFRA_OPSWKF) |
| SecurityAnalysis | 8 | OPAL-INTERNAL | Model tab renders the team sheet rows (AMGT_CORPUS); peers table Mkt Cap headings/dates; description empty-state line; news feed pillar filter |
| AdvisorIntelligence | 3 | CLIENT-FACING | ADVI_BILLING: AdvisorBookFeePanel (one billed quarter's fee vs Schwab debit) mounted below household panels; empty-state lines for flows/exclusions |
| ModelPortfolios.tsx | 1 | CLIENT-FACING | MDPF_CANON CN-d-3: the two additive SMA series drawn as their own bands on the Global trend |
| src/api, src/lib | 4 | shared | endpoints advi-billing, investor-reporting, tickets; pairedProvenanceRead |
| package.json, bun.lock | 2 | build | happy-dom held at 20.14.5 |

Visual smoke: there is no standing DEV preview host named in `docs/deployment/` or `portal/README.md` (measured: 0 hits for
a dev opalinvest URL; PROD is `https://portal.opalinvest.com` / `www.opalinvest.dev`). The DEV build is viewed locally:
`cd portal && bun install && bun run dev --port 5174` on origin/DEV, or this seat stands one up on request.

## B. fe9b in plain words (no decision taken)

See the reply of this turn; summarised: the combined "Global" (all-firms) MDPF figure lists per-model lines; 21 of its 41
per-model entries are held at ONE firm only (mostly Cottonwood, a few Inflection), so a reader of Global can see one firm's
book by model. X2 (the Global view) was granted on 2026-09-15 on the basis "aggregate counts only". (A) folds those one-firm
lines into one "other models" line in Global only; headline sums and each firm's own page are untouched. (B) keeps them as
they are and re-signs the endpoint to say Global shows per-model lines down to one firm. The page keeps working either way;
(A) is a served-JSON change under never-widen sign-off with every Global leaf read before and after.
