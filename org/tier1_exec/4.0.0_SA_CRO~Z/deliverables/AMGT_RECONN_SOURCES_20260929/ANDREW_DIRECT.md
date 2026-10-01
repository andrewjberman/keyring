# Andrew-direct: holdings sourcing research

**Author:** 4.0.0_SA_CRO~Z
**Channel:** direct Codex user messages, thread 01a0ede4-6907-7d81-9f8a-089141d6cdf6.
**Recorded:** September 29, 2026, approximately 15:23 ET. Exact receipt times were not exposed in the turn.

## Research instruction, verbatim

> Ok I want to discuss with you how we could develop a lightweight version of this that we progressively build out. The first thing we need to do is figure out a solution where we can get day over day holdings/ETF Composition per each of those tickers, and what is our backfill ability to that end. BBG may do this but I dont remember if we didnt have the necessary entitlements to do so. Another angle would be seeing what data the ETF providers release, and if it can be constructed retroactively over a 2 year period. That is the first research task I need you on, assessing where we would get the information for each of these; if we need bespoke pipelines or if it can just be done via BBG.

## Ticker confirmation, verbatim

In response to the question naming WCMG, GQGU, TSEL, BASG, ETFT and PCLG:

> Yes those are all correct

## Scope clarification, verbatim

> Yeah if they have less than 2Y of history, then we just get as much as we can up to that threshold. Also, if BQL is really just for all the "characteristics", and we can get holdings data every day just no beta/etc., that is fine. Most of that stuff can be derived after the fact if we really need it based on the holdings. All we need is daily holdings. If all we can get is weekly, fine, if all we can get is quarterly, less good, but fine.

The paired assessment records the live read-only Bloomberg probes, issuer-source retrievals, available historical examples and proposed lightweight collection approach. No other seat was dispatched.

## Bloomberg documentation follow-up, verbatim

Recorded September 29, 2026, 15:36 ET, direct Codex user channel. Receipt timestamps were not exposed.

> Ok Im interested. First of all, are you saying there might be another BBG endpoint that we can go around for this purpose?

> Check these out: "C:\Users\Opal Bloomberg\Downloads\BLPAPI-Core-User-Guide.pdf" "C:\Users\Opal Bloomberg\Downloads\BLPAPI-Core-Developer-Guide.pdf", they are docs on BBG API, maybe a clue in here

The follow-up is recorded in `BBG_GUIDES_FOLLOWUP.md`; it covers document review and read-only live API tests, with no account configuration changes or external correspondence.

## Option 1 selected, verbatim

Recorded September 29, 2026, approximately 16:03 ET; direct Codex user channel, receipt timestamp not exposed.

> Go on option 1 to start.

The selected next-calls option was to check remaining Terminal/Excel and portfolio-ID possibilities in one bounded research session, ending with a demonstrated full-holdings route or a precise support question. `BBG_EXCEL_ACCESS_VERIFIED.md` records the successful Excel route and remaining limitations. No support message, build dispatch, purchase or production schedule change was authorized or performed.

## Historical granularity question, verbatim

Recorded September 29, 2026, approximately 16:48 ET; direct Codex user channel, receipt timestamp not exposed.

> Just went through this, my question is, what granularity of dates do we have for these? Can it be retrieved daily every single day back to the start date or what?

`DAILY_COVERAGE_CENSUS.md` answers from a complete trading-date scan of the established sources, distinguishing dated source reports from Bloomberg's carried-forward responses. No production collector was installed.

## L1 brief direction, verbatim

Recorded September 29, 2026, during the approximately 17:32–17:46 ET research/brief session; direct Codex user channel, exact receipt timestamp not exposed.

> Ok i think we have enough to $brief-create now. Here are the main points: 1.) We need bronze/silver/gold structure within opal-data-etfs set up, bronze raw csv or whatever we can get daily holdings with as much info as is available, silver is typed parquet, gold first foundational table being the "Canonical Shape", where we level everything out to one Opal-defined format for all tickers/channels. 2.) We need to create a BBG daily script that gets tagged onto the morning run and a lambda script that pulls daily from the issuer sites. This can actually be tested now because if the issuer sites post daily and we only need BBG for the backfill, then it is much preferable to not needlessly use quota on BBG; that should be explored and rec be featured in brief if feasible. 3.) We need to spec out some Gold Tables and AI analysis prompts for said tables. I think the "Canonical Shape" table should effectively be a denormalized base table with all info that we'd want. Every holding, every subasset class and GICS industry tag in fields, anything we can get, put it all in there. Then we make downstream gold tables maybe per ETF that cover top 10 performer bottom 10 performer weights and summary sector delta day over day, stuff like that so that we can then give a prompt to the AI to reverse engineer their trading behavior, tilts, etc. in order to ultimately derive summary outputs that cover where they were really right where they were wrong, what trends we're seeing in their trading in order to predict where they're going based off past trades/activity (projecting trends outward in their holdings), and so on.

## LGIC naming constraint, verbatim

Same active brief session, direct Codex user channel; exact receipt timestamp not exposed.

> Yes also keep in mind that you should be following LGIC NAMING standards for all of this

Carried into `docs/briefs/etf-holdings-research-20260929.md` and this folder's `GOLD_TABLES_AND_PROMPTS.md`. The brief uses the actual LGIC registry and grader, records the measured bronze/silver placement-builder mismatch with the explicit bucket direction, and does not treat existing legacy prefixes as the standard. This invocation authors the brief and supporting design; it does not dispatch or deploy production work.

## Client assets versus outside research, verbatim

Recorded September 29, 2026, approximately 20:59 ET (September 30, 00:59 UTC); direct Codex user channel, exact receipt timestamp not exposed.

> only client assets go through that route to opal-data-assets. outside research, public info, etc (e.g. opal-data-harvest, opal-data-transcript, etc) are managed in their own buckets.

This reaffirms the existing R4 in `infra/logic/02_DOCTRINE.md`, read during this correction. The brief and supporting specification now explicitly identify `opal-data-etfs` bronze/silver/gold as the existing policy's application to outside ETF research. The observed builder output is an implementation/placement-metadata mismatch, not a new policy exception or an open decision. No global registry edit, production migration or peer dispatch was performed for this correction.

## Six-step build order and gap pass, verbatim

Recorded September 29, 2026, approximately 23:2x ET (September 30, 03:2x UTC); Claude Code terminal, `4.0.0_SA_CRO~Z` session a3a51db9. Exact receipt timestamp not exposed.

> Let's just do a pass on the current state of the brief and any associated evidence and make sure that there are no holes in any processes here. The way I see it, there are the following steps that have to be executed essentially in this order. 1.) Bucket structure createdin opal-data-etfs with bronze/silver folders for bloomberg and issuers respectively, as I expect they will be in different shapes. Gold folder will be unified shape that can accrue from either channel. 2.) Backfill from Bloomberg pulled ad hoc per ETF into bronze. 3.) lambda designed to activate on bronze ingestion completion to type/dedup silver parquets. 4.) lambda designed to activate on silver completion that runs gold foundational shape + any other gold tables. 5.) Lambda runs at completion to generate presentation worksheet with relevant chart views and AI analyses, probably hosted on mcp.opalinvest.dev/activefunds (can borrow a lot for this from /daily-sprint cloud process). 6.) Schedules set up for daily csv ingestion and parsing that goes to the issuer bronze/silver folder path. Bloomberg exists as backup retry if issuer fails. These run daily.

Step 5 (a hosted presentation page with AI analyses) is new relative to the brief, whose O1 said a dashboard was not required. The gap pass is reported in-session; no brief text, build or dispatch was changed by this record.

## Rulings on the 14-item gap pass, verbatim

Recorded September 29, 2026, approximately 23:4x ET (September 30, 03:4x UTC); Claude Code terminal, `4.0.0_SA_CRO~Z` session a3a51db9. Exact receipt timestamp not exposed. Numbers answer the gap-pass items in order.

> 1.) This is a separate function, the lambda you list is for a different purpose; conflating the two would be messy. this should be etfs-rivalfunds-daily, that makes it extra clear what it is. 2.) That naming tool needs to be adjusted, that should only apply for client assets and this is not a client assets issue. I believe that fix is already in production in the cloud; it should be how buckets like opal-data-harvest have been allowed to operate. 3.) That's fine, you can propose a solution to that which I will review. 4.) No that is not how it would work. What would be more logical is a platinum folder in opal-data-etfs that has the served files archived by day. Look at how mcp.opalinvest.dev/sprint/archive does it, where are those stored? I would use a similar pattern. Lastly, regarding the new gateway route, that's fine, let's use /rivalfunds though to keep up with the lambda title as i think its a more unique and specific token. We definitely can use OpenAI on this; OpenAI relationship with BBG is entirely out of our scope. Moving onto 5.) Ok go with your recommendation on how to structure this, i was not being 100% literal, just largely being chronological in terms of getting this off the ground in short time without a ton of process overhead and bullshit. 6.) Trigger on batch complete works. 7.) Great point, have to ad hoc those then from the outset. 8.) That is a good point, I am ok with using canonical flow process instead, I just made these comments to be very explicit about nonnegotiable steps that need to happen so that the agents responsible dont have a giant hole and forget that there needs to be a served output, or forget to bridge silver and gold, etc. as this happens when one is not specific in planning sometimes. 9.) Ok then we do the issuer at 7a ET and BBG has a fallback opportunity for ETFs that do appear on BBG at that 8:03 time. 10.) There should be guardrails to check on that pre-publishing. 11.) Yes that has to be done. 12.) This will require some testing over a few days, not a big deal. 13.) I am fine with using BBG for this. May be a good time to look into AMGT_HARVST and how all the resolutions worked there. 14.) Didnt think it would, we expect them to be different in bronze/silver, thats why there is a gold accrual table that coalesces the various shapes into one master shape.

OpenAI use for the analyses is authorized by this word. The ruling on item 3 asks for a proposal Andrew reviews; it is not a ruling on the trigger design itself.

## S9 approved, registry row, CTO handoff, verbatim

Recorded September 30, 2026, approximately 00:0x ET (04:0x UTC); Claude Code terminal, `4.0.0_SA_CRO~Z` session a3a51db9. Exact receipt timestamp not exposed.

> S9 looks fine, add the registry row and send to CTO

This approves the S9 trigger-chain proposal and pre-publish guardrails in `GOLD_TABLES_AND_PROMPTS.md` revision 2, authorizes the `rivalfunds` scope row in `infra/logic/registry/scopes.json`, and directs the brief to 1.0.0_SA_CTO for L2.

`python lib/opal_naming.py validate` refused the `rivalfunds` scope row (*"'opal-data-etfs': a data bucket is opal-data-{scope}, LONG form"*); the row was reverted uncommitted. Andrew's answer, same session, verbatim:

> no that is ok , we can use etfs scope

Landed accordingly: the `etfs` scope moves to GENERAL tenancy, and a `rivalfunds` system key is the source of the derived tiers (validate 0 refusals; generated targets content-identical).

## Project name, verbatim

Recorded September 30, 2026, approximately 00:2x ET (04:2x UTC); Claude Code terminal, `4.0.0_SA_CRO~Z` session a3a51db9. Exact receipt timestamp not exposed.

> I like it, lets call this ETFS_RIVALS

The project code is `ETFS_RIVALS`. Registering it (L3) is 1.0.0_SA_CTO's; this seat records the name and relays it. The product and resource token stays `rivalfunds` (`etfs-rivalfunds-daily`, `/rivalfunds`); a project code is never a system token.

## Trade schedule as the foundation of the analysis, verbatim

Recorded September 30, 2026, approximately 00:3x ET (04:3x UTC); Claude Code terminal, `4.0.0_SA_CRO~Z` session a3a51db9, in reply to the CTO's nine-outcome endpoint. Exact receipt timestamp not exposed.

> Yeah this is pretty good but i have one idea that may be foundatinal for the AI Analysis. We need to reverse engineer their actual trades. What I'm thinking is, if we have their changing values at market close each day, and we also track all the performance of the individual securities every single day, cross-referencing that with the portfolios, couldn't we assess more or less when and where they made trades (i say approximately because not sure how well cash is tracked)? If we can engineer a shape for this, then we can have a gold table for each active etf that is effectively their trade schedule. THe premise here is that the whole point of doing this is not to throw a huge amont of data at research team; that is useless. It is to get one really, really clear signal on competitive intelligence and reverse engineering the other funds processes and activity.

The DONE WHEN lines are not yet confirmed by this word ("pretty good but"). Feasibility measured the same hour: `TRADE_INFERENCE_FEASIBILITY.md`.

## Trade floor and dividends, verbatim

Recorded September 30, 2026, approximately 00:2x-00:3x ET; Claude Code terminal, `4.0.0_SA_CRO~Z` session a3a51db9, three consecutive messages. Exact receipt timestamps not exposed.

> Trades can be 0.2% or more, not 0.5%.

> Also probably need to account for dividends on thes

> bbg should have dividend calendar for the holdings

Applied: the trade floor is 0.2% of prior shares (probe re-run; `TRADE_INFERENCE_FEASIBILITY.md`), and dividends enter the method from Bloomberg's per-holding dividend calendar (S6).

## 0.2% confirmed, verbatim

Recorded September 30, 2026, approximately 00:4x ET; Claude Code terminal, `4.0.0_SA_CRO~Z` session a3a51db9, after the 0.2% / 0.5% comparison. Exact receipt timestamp not exposed.

> ok stick with 0.2%, send it to CTO when committed

Already in force: rev 3 committed at 2a1f275a78 with the 0.2% floor, sent to 1.0.0_SA_CTO~Z (msg 26910), and the endpoint amended at 33c1d096a3 (msg 26913).

## Five open calls answered, verbatim

Recorded September 30, 2026, approximately 01:5x ET (05:5x UTC); Claude Code terminal, `4.0.0_SA_CRO~Z` session a3a51db9, answering this seat's `/open-calls` cards 1-5. Exact receipt timestamp not exposed.

> 1.) Yes approved. 2.) Agreed . 3.) No we're not doing this, im fine with "fragile", just need to run the tests and see how it goes day over day. 4.) any signed in account. 5.) remove them

The cards, as asked:

1. Confirm the nine ETFS_RIVALS DONE WHEN lines as written (`ENDPOINT_FORWARD_RIVALFUNDS_20260930.md` @33c1d096a3): **APPROVED**.
2. Bloomberg pulls for ETFS_RIVALS under (a) per-use word or (b) R-21 scripted grant; REC (b), scripted pulls only (backfill script, 8:03 fallback leg, dividend/price enrichment): **AGREED (b)**.
3. Send the drafted Bloomberg support question (GQGU coverage, direct BQL): **NO**. The unattended-Excel route stays, proven by day-over-day tests.
4. /rivalfunds viewers: **any signed-in account**.
5. Remove the 09-29 crash dumps: **remove**. Applied 01:53 ET elevated: `C:\Windows\MEMORY.DMP` REMOVED (18,686,448,893 bytes). The Sentinel dump (`C:\ProgramData\Sentinel\CrashDumps\af142cfc-....dmp`) was REFUSED even elevated; its folder is owned by `NT SERVICE\SentinelHelperService` (SentinelOne tamper protection) and was not forced. `C:\dedicateddump.sys` is the live reserved capture target configured in `HKLM\...\CrashControl` (`DedicatedDumpFile`, `DumpFileSize=32768`), so it is held for Andrew's word on disabling crash capture.

## Dedicated dump file, verbatim

Recorded September 30, 2026, approximately 03:2x ET; Claude Code terminal, `4.0.0_SA_CRO~Z` session a3a51db9, answering whether to switch off crash capture and delete `C:\dedicateddump.sys`. Exact receipt timestamp not exposed.

> keep crash capture, but delete the 32gb .sys

Means: `CrashDumpEnabled` (kernel dump) and `DumpFile` stay; the `DedicatedDumpFile` and `DumpFileSize` values are removed so the dump goes through the system-managed page file; `C:\dedicateddump.sys` is deleted (at reboot if the system holds it).

Applied 2026-09-30 03:33-03:35 ET, elevated (log `.runtime/crash-investigation-20260929/remove-dedicated-dump-elevated.log`; key backup `CrashControl-backup-before-dedicated-removal.reg` beside it): `DedicatedDumpFile` and `DumpFileSize` removed; `CrashDumpEnabled=2` (kernel dump) and `DumpFile=C:\windows\MEMORY.DMP` unchanged, through the system-managed page file. `C:\dedicateddump.sys` (34,359,738,368 bytes) is held open by the system, so its deletion is scheduled for the next reboot (MoveFileEx delay-until-reboot returned true; PendingFileRenameOperations names it).

## IDVZ rival group, verbatim

Recorded September 30, 2026, approximately 11:0x ET; Claude Code terminal, `4.0.0_SA_CRO~Z` session a3a51db9. Exact receipt timestamp not exposed. Andrew's instruction to this seat, quoting the message he sent 2.0.0_SA_COO~RV:

> Below is a message I just sent to COO~RV. I want you to check out the email as well, however on your side you are going to have to actually check the various pipes and identify if we can run the same BBG strategy for these or if we need to find their issuer pages and run it down that way. The premise is that this is simply an expansion on the initial tracked group. However, if you read my response in the thread, there is clarity on the insights i believe should be presented. Accordingly, that will inform how we structure the gold tables and AI sysprompt that will provide analyses on those tables. Please review, analyze, and when ready to write the brief, ping me on high level findings and let's discuss; Please check my email from Adam, adam@opalinvest.com writing me to my email andrew@opalinvest.com. He gave us a list of tickers for IDVZ which we are going to want to incorporate into this pipeline. The structure could be flat if youve already designed buckets and etc. to be flat, but if not, we should group these rivaletfs in folders based on what opal etf they are rivals to. The ones we've been working on thus far are all for PFOE, these will be for IDVZ. I am going to have CRO~Z go do some digging and bring you a brief but keep this in mind..

Source thread (Opal mailbox, read via the Opal gateway): Adam Muller to Andrew, 2026-09-29 23:19 UTC, "right comp funds for IDVZ": IDVZ, TXUE, BIDD, CGIC, INEQ, SCHY. Andrew's reply of 2026-09-30 14:42 UTC names the summary views: trading outperformance/underperformance by sector and security; forward projected trading activity based on observable trends across sectors/securities; a "hand-on-the-door wildcard analysis from the AI"; and notes that at a 20bps tolerance "it's immediately clear who is discretionary and who is systematic". Findings: `IDVZ_GROUP_SOURCE_CENSUS.md`.

## IDVZ group: three decisions and the dividend question, verbatim

Recorded September 30, 2026, approximately 11:5x ET; Claude Code terminal, `4.0.0_SA_CRO~Z` session a3a51db9, answering this seat's three discussion points. Exact receipt timestamp not exposed.

> It sounds like bbg is better for this group if the issuers are not as hq, so yes, agreed with point 1. On point 2, yes agreed. On point 3, yeah it might be helpful to include the Opal Funds like IDVZ and PFOE into this list so we have them on the same analysis plane, that is a good idea. Regarding the threshold for trading, did we already account for dividend/interest income? That should be covered if we want to tighten up trade identification.

Decisions: (1) Bloomberg is the primary daily source for the IDVZ group; (2) flat storage keyed by fund plus an Opal-fund-to-rivals mapping, not folders; (3) each Opal fund (IDVZ, PFOE) joins its own group as the home member. On dividends: not yet accounted for; measured the same hour, cash and currency lines are 4.7-59.2% of the preview's add/trim events (see `IDVZ_GROUP_SOURCE_CENSUS.md` section 4).

## Addendum A DONE WHEN lines, verbatim

Recorded September 30, 2026, approximately 12:0x ET (16:0x UTC); Claude Code terminal, `4.0.0_SA_CRO~Z` session a3a51db9, answering whether the DONE WHEN lines of `ENDPOINT_FORWARD_RIVALFUNDS_ADDENDUM_A_PEER_GROUPS_IDVZ_20260930.md` @bd6effc4f3 are confirmed as written. Exact receipt timestamp not exposed.

> fwd 1 should include idvz and pfoe right as the two opal etfs, with their respective peer groups. otherwise, yes, all of these are fine.

Means: FWD-1's live trace covers both Opal ETFs, IDVZ and PFOE, each with its own peer group; every other DONE WHEN line of Addendum A is approved as written.
