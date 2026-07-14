# ANDREW-DIRECT — TAXSMA + Opal Ticket System scoping (verbatim record)

<issued_to>0.5.0_AE_OpalETL~A</issued_to>
<issued_by>Andrew (sovereign, direct terminal prompt to the ~A lane session)</issued_by>
<channel>direct terminal prompt, session 8841a0df-4e0d-4190-9d2e-96fc825f9f23</channel>
<received>2026-07-14 ~18:52Z</received>
<status>pending</status>
<scoping_completed>2026-07-14 ~19:25Z — brief deliverable landed: docs/briefs/ANDREW_BRIEF_20260714_taxsma_and_ticket_system.md (293c062fb)</scoping_completed>

## ADDENDUM 4 — FIFTH ANDREW-DIRECT (same session, ~21:0xZ): REGISTRY NAMING (verbatim)

> "let's make sure ticket project is registered as OPAL_TICKET in the registry. also OPAL_TAXSMA
> if not registered already."

**Executed same turn:** TCKT_CENTER -> OPAL_TICKET and PFMG_TAXSMA -> OPAL_TAXSMA (JSONs renamed
with renamed_from chains + history events; REGISTRY row updated for TICKET and ADDED for TAXSMA —
the 06-26 registration had been JSON-only; the one-day TCKT macro row retired; the missing OPAL
macro row added to MACRO_CODES.md, rule-6 conformance). Infra naming (ticket-center TF module/tag,
opal-ticket-api, opal-tickets, /tax-pt1) unchanged — project-code rename only.

## ADDENDUM 3 — FOURTH ANDREW-DIRECT (same session, ~20:5xZ): NEW SOVEREIGN-DELEGATE AGENT (verbatim)

> "I also am going to instantiate another agent, 0.2.0_DT_PortfolioAnalytics, which I need briefed
> on this style of work we're doing on a governance basis, i.e., they are not on the main fabric
> and they have sovereign authority to write PRDs, register projects, and carry through to
> completion. I will need a short text summary i can paste for them to brief on that layout."

**Effect:** the fabric-quiet sovereign-delegate pattern this session exercised becomes a REUSABLE
governance layout; 0.2.0_DT_PortfolioAnalytics is its second instance (Andrew-instantiated,
off-fabric, PRD+register+execute authority). Deliverable: the paste-block brief at
`docs/briefs/SOVEREIGN_DELEGATE_AGENT_BRIEFING.md` (authored + committed this window).
Broadcast to COO/CTO/MSTR same turn — the fabric must know a second delegate exists.

## ADDENDUM 2 — THIRD ANDREW-DIRECT (same session, ~20:2xZ): THE 13 OPEN-ITEM RULINGS (verbatim)

> "1.) We don't need to focus on step 5 at this point. 2.) No asking schwab, if they dont have the
> files and we cant derive the files somehow from what we already have then it cant work that way.
> We do get the SSAVAIL emails every single day though which is the principal automation/parsing
> aspect of this project. 3.) Yeah that recommendation is a good way to do it, but Alyssa is
> actually claude-savvy, I think we can just give her skills.md files. 4.) We can give her write
> access at any time since it's our system/server; check OPLMCP projects and associated work from
> that period, there should be a permissions layer somewhere in that machine we can adjust at.
> 5.) I think this is fine, it would be nice to have it go to a dedicated subfolder as well.
> 6.) Rec is fine. 7.) I'd call it /tax-pt1 (and accordingly tax-pt2 and etc as needed). 8.) Yeah
> use 2pm for now. 9.) it will be that but he's not hired yet so we'll have to set that up next
> month. 10.) Teams link is great if we can pull it off that way, emails have too much anti-link
> IT software would make it clunky. 11.) I don't think this needs to be real analytics, just a
> flat 'We'll get back to you asap' subjective thing, maybe tagging a notification on there when
> the ticket is picked up with the name of the person and their email. 12.) Yeah teams shared
> channel is the way to go here for sure, we can set that up. 13.) Rec is good."

**Operative effects (recorded, not adjudicated):** TAXSMA — step 5 DESCOPED for now; step 2 NO
Schwab ask, stays manual unless derivable in-estate (verified not: ULN+ACC negative), the SSAVAIL
email intake/parsing IS the project's principal automation; Alyssa UI = SKILLS.MD FILES (no portal
runner); skill naming = /tax-pt1, /tax-pt2, ... ; Alyssa gets gateway write access via the OPLMCP
entitlement layer; mail-subfolder filing is welcome (runner is folder-agnostic). TCKT — cutoff
2 PM ET interim config; bobby@ parked until hired (~next month); claim links = TEAMS not email;
external/requester side = flat "we'll get back to you asap" ack + a claimed-by notification
(name+email), NOT analytics; AI intake monitors a Teams shared channel (to be set up); form
connector rec stands.

## ADDENDUM — SECOND ANDREW-DIRECT (same session, ~19:30Z): EXECUTION DELEGATION

> "Ok I do not want to interrupt the fabric with these ad hoc projects so I'd rather upon your
> finishing the briefs, you just take sovereign authority, register the projects if they are not
> registered as macro_projects, and run the issues through completion."

**Effect (surfaced, recorded):** scope expands from scoping-only to EXECUTION-TO-COMPLETION under
delegated sovereign authority, fabric-quiet (no dispatch into COO/CTO loops; informational
broadcast only). Supersedes COO's "I will register the project when the brief lands" for
TCKT (I register it directly). PFMG_TAXSMA already registered — execution delegation noted in its
history. STILL BINDING (delegation does not waive law): CLAUDE.md gates (Terraform-only,
safe-apply/safe-commit, Rule 22/22a grounding + IAM live-primitive verify, Rule 23 SES
opalinvest.dev), the PRD-level TAXSMA hard guardrail (trade file GENERATED, human executes —
Yang-sourced, PRD-pinned), bronze-raw 17a, and the standing INF-chain / 22:00Z deconfliction.

## VERBATIM (the phrasing IS the ruling — scope surfaced, not adjudicated)

> "Your task for today will be scoping two new projects for Opal automation, 1.) Tax SMA from
> Yang Liu (yang@opalinvest.com), 2.) Opal Ticket System from AJ Graff (aj@opalinvest.com). The
> TAXSMA project may already have a registered project in our system, so it is worthwhile to
> check that first. Yang sent an email with his specifications, I believe we can automate Steps
> 1-4 in that email. I already receive the SSAVAIL emails daily to my andrew@opalinvest.com
> email now, so the assets necessary to begin testing are already present and arriving daily.
> On 2.), there is a transcript with AJ on the ticket subject here: 'C:\Users\AndrewBerman\
> Downloads\Call with AJ Graff (1).vtt' 'C:\Users\AndrewBerman\Downloads\Call with AJ Graff
> (1).docx'. I think it is fairly straightforward how to design this in tandem with our Portal.
> Please begin your review now. Your deliverable is a comprehensive implementation brief for
> both items."

## Deliverable

One comprehensive implementation brief covering both items (committed doc). Broadcast to
COO + CTO + MSTR sent same turn per org/XXX.md Andrew-direct protocol.

<compiler_tools_mandate>comp-grep/comp-which for all registry + estate searches; session log
Compiler Tools section on close.</compiler_tools_mandate>
<cross_domain_coordination>Base serial 0.5.0_AE_OpalETL owns tonight's 22:00Z pipeline —
this scoping work is read/author-only, no shared files with C4/C5/D2.</cross_domain_coordination>
<acceptance_criteria>Implementation brief exists on the record covering: TAXSMA registry
check result, Yang spec Steps 1-4 automation design, SSAVAIL asset flow, ticket-system design
integrated with the Portal per the AJ Graff transcript, phased delivery + open questions.</acceptance_criteria>
