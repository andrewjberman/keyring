# Andrew-direct 2026-09-23 ~16:3xZ: the hold is off, and seven closer-design calls ruled

Recorded by `4.0.0_SA_CRO` at its own terminal. The rulings answer this seat's `/open-calls` frame, rendered on
Andrew's request of the same turn. That request asked for `/open-calls` on
`org/tier1_exec/4.0.0_SA_CRO/deliverables/BRIEF_CANONICAL_FLOW_SPEED_CLOSER_FLOW_SKILLS_PARITY_20260923.md`
@`ea031c3987` and on its implementation, spine v3.16 @`ddaf233a52`. It also asked to understand what `/closer` is
meant to do. The calls below are as put; the rulings are verbatim.

## Andrew's reply, VERBATIM

> 1.) Hold is off. 2.) Yes. 3.) Yes. 4.) Rec approved. 5.) That does apply for projects that have a frontend but needs
> to be considered in the event it's purely a backend/infrastructure product (e.g. NFRA_GLOBGRPH, NFRA_COMPEFFICACY,
> LGIC_NAMING, LGIC_LGCTFM, etc.). 6.) Yes. 7.) Yes.

## The calls as put, and what each ruling binds

| # | Call as put | Ruling (verbatim) | Binds |
|---|---|---|---|
| 1 | Is the overnight hold (MSTR 99652) over for EVERY agent? (a) yes, all / (b) only for the push of today's two commits / (c) no | "Hold is off." | (a). The hold is lifted for every agent on every machine. `0.0.0_AB_MSTR` relays it across both fabrics and pushes `ea031c3987` and `ddaf233a52`. |
| 2 | May the CRO (or any Tier-1 seat) run a read-only `/closer trace` on a product in flight WITHOUT Andrew's word, with his word needed only to START building? | "Yes." | A trace brief needs no word. Andrew's word gates only the build phase: contract, mandates, implementing and reviewing seats. The REC also said: the CTO may PROPOSE a closer when a project shows 2 or more rounds and 0 live journeys. |
| 3 | Do Codex COO seats count toward the three-COO limit on the laptop (Andrew 2026-09-14)? (a) yes / (b) no | "Yes." | (a). Codex `2.0.0_SA_COO*` seats count toward the three-COO limit. A closer is scheduled in SEQUENCE like any project. |
| 4 | `/closer` shape: (a) ONE skill with a form per role, adding `run` for implementing seats and `review` for CVOs / (b) split into `/closer-trace` and `/closer` | "Rec approved." | (a). One skill; `run` and `review` forms are added. |
| 5 | What counts as "live" for the thread? (a) real backend, real data and real login, the frontend may be local or DEV / (b) PROD only | "That does apply for projects that have a frontend but needs to be considered in the event it's purely a backend/infrastructure product (e.g. NFRA_GLOBGRPH, NFRA_COMPEFFICACY, LGIC_NAMING, LGIC_LGCTFM, etc.)." | (a) for any project with a frontend. For a purely backend or infrastructure product the definition is OPEN and is to be considered. The spine's current L2 non-application, "a pure infrastructure or governance project, which has no journey", is the text in question. `4.0.0_SA_CRO` owes the consideration. |
| 6 | When Investor Reporting hands back, is it ONE product project (first journey = the thread, the other two = enrichment), with the held IRPT_FNTEND and IRPT_BCKEND closed as superseded? | "Yes." | Yes, at hand-back. The CTO also rewords spine L4's "a new product is one journey in one project" to "one product = one project; its first outcome is one journey; never a frontend/backend split". |
| 7 | Codex's four machine-only skills: leave `drive`, `02check`, `yolo` in the machine's Codex folder untouched, and retire the duplicate `opencalls`? | "Yes." | Yes. `drive`, `02check` and `yolo` stay untouched in CODEX_HOME, since Anatomy stays off this workspace. The home-only `opencalls` is retired, because `open-calls` now installs from the repo. |

## Routing

- **`0.0.0_AB_MSTR`:**
  - Call 1: relay the hold lift to every agent on both fabrics, and push.
  - Call 3: the spawn-side count of live COO sessions must include Codex seats.
- **`1.0.0_SA_CTO~C`**, the implementer of the brief:
  - calls 2, 4, 5(a), 6 and 7, as `/closer` and spine edits;
  - the six non-sovereign fixes named in the same turn's `/open-calls` output:
    - the Codex CVO grading-evidence wording;
    - the project's state while a closer runs;
    - IRPT contract v1.3;
    - the ACK scope;
    - difference-control arms inside the three-check limit;
    - the pipeline thread's "person".
- **`4.0.0_SA_CRO`:** call 5's open half, the thread for a purely backend or infrastructure product. The proposal goes
  to `1.0.0_SA_CTO~C` the same turn.
