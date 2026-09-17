# The true cost of Claude at Opal -- and what our subscription setup trades away

**Prepared by** `4.0.0_SA_CRO~Z` for Andrew, 2026-09-17. **Scope:** both machines that run agents over the 30 days their
local session records cover, 18 Aug to 17 Sep 2026: the Bloomberg-terminal computer (site Z), measured here, and the
laptop, measured there with these same instruments. Sections 2 to 4 are site Z; section 4a is both.
**Requests:** records `ANDREW_DIRECT_20260917_160xZ_CLAUDE_COST_PER_OUTPUT_REPORT_AND_DECK.md` and
`ANDREW_DIRECT_20260917_174xZ_DECK_FOR_NONTECHNICAL_MANAGERS_AND_AUGUST_PAID_VS_COST.md` (the second asks for the
deck, and this report's framing, to be written for managers with no technical background, and for Anthropic's
extra-usage charges to be counted in what we paid).

**How to read every number here.** Each carries one of four evidence labels.

| label | meaning |
|---|---|
| MEASURED | read on this computer: Claude Code's own session records, git history, local settings, `claude auth status`; or, for the payment rows, the Anthropic payment notices in Andrew's mailbox, read by the main-fabric seat that holds that mailbox identity |
| REFERENCE | the in-environment Claude API reference shipped with Claude Code (model table cached 2026-06-24; caching and retention sections) |
| SUPPLIED | the GPT thread Andrew pasted (saved verbatim beside this report). Not Anthropic documentation and not verified here: no web page was fetched, because this session holds no egress word |
| STATED | Andrew's own statement, not checkable from this computer (that five Max accounts are in use at $200 each, and that usage sharing is off) |

---

## 0. In plain terms

**What we buy.** Claude is an AI model made by Anthropic. Claude Code is the program that lets it work directly on
our computers: open files, run commands, save its work. We run several of those sessions at once, each with a job,
which is what this report calls agents or seats.

**How AI is priced.** Everything is counted in *tokens*, a word or part of a word. Three things are charged at
different rates: text sent in, text the model writes back (the most expensive), and text re-read from a recent
*cache* (much cheaper than reading it fresh, but saving it to the cache costs extra). A model has no memory between
answers, so every answer re-reads the whole conversation so far, which is why re-reading dominates the bill.

**The two ways to buy it.** A *subscription* is a flat monthly fee per account with usage limits, on consumer
terms. *Pay-as-you-go through the API* is metered per token on business terms, with company controls. We use
subscriptions. This report prices our work at the pay-as-you-go rates to show what the same work would cost billed
by the token, and calls that the standard price.

**The answer.** In 30 days we paid about $1,110 for work that would cost $43,283 at standard prices across both
machines: roughly $39 of work for every $1 paid. Of that standard price, $8,330 is the Bloomberg terminal
computer and $34,953 the laptop. Nothing is trained on our data, on any of the options, with sharing off. What
the subscription setup gives up is company control: a contract in Opal's name, defined deletion, admin controls
and audit records.

---

## 1. The answer

1. **The two machines consumed $43,282.97 of Claude at API list prices in 30 days** (MEASURED on each, repriced at
   REFERENCE rates): $8,329.75 here and $34,953.22 on the laptop.
2. **We paid about $1,110 for it:** five Max accounts at $200 (STATED) plus $110.04 of extra usage. That is 39x,
   or 97% below the standard price. The extra-usage figure is Andrew's own record; section 3 gives the mailbox
   evidence, which disagrees with it and is not reconciled here.
3. **Per unit of output across both machines, at standard prices:** $3.13 per commit, $124 per completed task
   order, $1,546 per working day. On what we actually pay those are about $0.08, $3.19 and $40.
3a. **On the Bloomberg terminal computer alone,** the same units are $1.72, $44.54 and $297 at standard prices.
4. **Almost three-quarters of the bill is re-reading context.** The average response re-read about 453,000 tokens.
   Context size, not prompt length, is what drives Claude Code's cost.
5. **Training is not the exposure; retention and governance are.** With usage sharing off, the supplied policy says
   sessions are not used for training. What the subscription setup gives up is a commercial contract, defined
   deletion, zero-retention options, admin control and audit.
6. **Buying that governance means paying for the tokens.** Enterprise is a seat fee plus 100% of usage at API rates
   (SUPPLIED), which at both machines' measured usage is at least $43,283 a month before the seat fee.

---

## 2. What was measured

| item | value | label |
|---|---|---|
| Account on this computer | `andrew@opalinvest.com`, auth method claude.ai, subscription `max` (tier not reported), no API-key or provider override | MEASURED |
| Records read | 110 transcript files, 203,316 lines, 63,941 usage lines deduplicated to 28,259 priced responses | MEASURED |
| Window | 2026-08-18 16:29Z to 2026-09-17 16:14Z, 28 days with usage | MEASURED |
| Unpriced | 39 `<synthetic>` records with no model | MEASURED |
| Price table | Fable 5.1 $10 in / $50 out / $0.25 cache read; Opus 5 $5 / $25 / $0.50; Sonnet 5 $2 / $10 / $0.20; Haiku 4.5 $1 / $5 / $0.10, all per million tokens; cache write 1.25x input (5-minute) or 2x (1-hour) | REFERENCE |

**Method.** Claude Code writes the same usage block once per content block, so a naive sum double-counts. The parser
keeps one record per response (message id + request id), prices each token class separately, and attributes each
session to its seat through `org/mcp/sessions/<session>.serial`, charging subagent work to its parent session.
Reproduce with `measure_claude_usage.py` in this folder; its output is `usage_summary.json`.

---

## 3. What we paid, and what the same work costs

### What Anthropic actually charged (MEASURED)

Read from the Anthropic payment notices in `andrew@opalinvest.com` by the main-fabric seat holding that mailbox
identity, relayed 2026-09-17 18:00Z (msg 23553). Site Z's own gateway identities are `opalbloomberg@opalinvest.com`
and cannot read that mailbox; three independent full-text queries agreed on the same set, so an absent fourth row is
a measured absence rather than a failed search.

| date | amount | what it is |
|---|---|---|
| 2026-08-26 | $10.04 | extra usage beyond the plan limits (the one non-$200 charge, per Andrew's rule) |
| 2026-08-30 | $200.00 | one monthly subscription |
| 2026-09-06 | $200.00 | one monthly subscription |
| **total charged inside the window** | **$410.04** | three payments |

**Why the window total is not the run rate.** The five accounts renew on different dates, so only two renewals fall
inside these 30 days; four more $200 notices sit just before the window (07-31 x2, 08-06, 08-07). This report uses
Andrew's stated five-account rate, $1,000 a month, plus $110.04 of extra usage = **$1,110**.

**TWO PAYMENT FACTS THAT DISAGREE, AND NEITHER IS DISCARDED.** The mailbox scan measured $10.04 on 26 August and,
on three independent queries, nothing between 7 and 17 September. Andrew's own record, written into his edit of
the deck, is $110.04 dated 16 September. His figure is the one the deck and this report carry, because he reads
the card statement directly and the mail record is only a notice stream. Whether the 26 August charge is a
separate fourth payment, which would make extra usage $120.08, is HIS call and is not assumed here.
**Open item for Andrew:** two of the five accounts show no renewal notice inside the window on either side of it
being due, so either those accounts bill on another instrument or the count has changed; the notices alone cannot
tell which.

### The comparison

| what | 30 days |
|---|---|
| what we paid | $1,110 (STATED rate + Andrew's extra-usage record) |
| the same work at API list prices, both machines | $43,282.97 (MEASURED) |
| of which the Bloomberg terminal computer | $8,329.75 (MEASURED) |
| multiple | 39x |
| effective discount | 97% |

The last 7 days (2026-09-11 to 2026-09-17) alone come to $2,187.97 at standard prices. (MEASURED)

### Against the published prior art (SUPPLIED)

The supplied thread cites repriced Claude Code logs of 12x to 21x on Max 5x and 15x to 40x on Max 20x, with a
reported stress-test ceiling near $8,000 a month for one Max 20x account. Site Z's $8,330 sits at that ceiling for
a single account, consistent with the month having been spread across several accounts.

### Where the standard price goes

| token class | tokens | USD | share |
|---|---|---|---|
| cache reads (re-reading saved context) | 12,812,330,931 | $6,036.68 | 72.5% |
| cache writes, 1-hour (saving context for an hour) | 126,693,754 | $1,416.15 | 17.0% |
| output (text written back) | 32,017,652 | $828.04 | 9.9% |
| cache writes, 5-minute | 18,330,515 | $47.84 | 0.6% |
| fresh input (new instructions) | 145,343 | $1.04 | 0.0% |
| **total** | **12,989,518,195** | **$8,329.75** | |

---

## 4. Cost per output

A **commit** is one saved, recorded change to our code or documents. A **task order** is an assigned piece of work
that must pass set checks.

| output (site Z, same window) | count | at API list price | at what we paid | label |
|---|---|---|---|---|
| commit authored by a site-Z seat or site-Z worker | 4,843 | $1.72 | $0.04 | MEASURED |
| task order completed on a site-Z project | 187 | $44.54 | $1.14 | MEASURED |
| active day | 28 | $297.49 | $7.63 | MEASURED |

The "what we paid" column now prices each unit at 2.6% of its standard price, which is what we pay across both
machines ($1,110 of $43,283). Section 4a gives the same units counted fabric-wide.

**What counts as a site-Z commit.** Lane serials recorded in this computer's session map, the terminal seat, and
worker subagents of the six site-Z projects (AMGT_RESAPP, POSN_ASTTAX, POSN_AGGFIX, NFRA_REPORT,
NFRA_IAMROLES202609, NFRA_OPSEC202609). Base serials are excluded because the laptop fabric authors under them.
Worker commits are 396 of the 4,843. **A task order counts** when a diff inside the window added
`<status>complete</status>` to it.

**Why per-output is the right unit.** A cheaper request that needs more turns is not cheaper. The fabric's real
product is merged, verified work, so dollars per commit and per completed order are the numbers to manage.

---

## 4a. Both machines, and what each project cost

The figures above are site Z alone. The deck covers ALL work in the window (Andrew-direct ~18:5xZ), which means both
machines that run agents. The laptop's half was measured on the laptop, by `0.0.0_AB_MSTR~Z`'s relay, running THIS
folder's own `measure_claude_usage.py` and `per_project_cost.py` unmodified, so one instrument produced both halves.

| | Bloomberg terminal computer | laptop | both |
|---|---|---|---|
| standard price, 30 days | $8,329.75 | $34,953.22 | **$43,282.97** |
| responses | 28,259 | 96,626 | 124,885 |
| tokens | 13.0B | 45.5B | 58.4B |
| projects with attributed spend | 18 | 52 | -- |

(MEASURED on each machine. The laptop's per-project run totals $35,001.18 rather than $34,953.22: the two runs bound
the window by calendar date and by exact timestamp. The difference is 0.1% and is not a second measurement.)

**Fabric-wide output, one rule over the shared git history** (`fabric_outputs.py`, this folder): 13,829 commits
authored by agent seats in the window, of which 4,872 match the site-Z rule, and 348 task orders completed across
every project. **WARN: the laptop counts the same history by a different rule and gets 13,999 commits (10,004 laptop /
3,995 site Z) and 363 task orders (183 + 180).** Neither count is asserted over the other; the deck carries this
seat's, and both are recorded here. The gap is the attribution rule, not the history.

### Attributed cost per project

Method: price every response, total per SEAT, then split each seat's spend across the projects that seat committed to
in the window, in proportion to those commits. Project code from the commit subject prefix `type(CODE, ...)`, else
from an `org/missions/D*/<MACRO>/<CODE>/` path. Seats with spend and no commits are held on their own line, never
spread. "What it cost us" is the attributed standard price times (what we paid / the combined standard price).

| grouped product | standard price | what it cost us |
|---|---|---|
| ETF work: positioning, ownership guardrail, the data behind them | $3,612 | $93 |
| Investor reporting product (both halves) | $3,450 | $88 |
| Cloud map of our systems | $3,029 | $78 |
| Analyst tooling: research pack, Bloomberg dashboard | $2,705 | $69 |
| everything else, both machines | $30,488 | $782 |

Largest single projects behind those groups -- laptop: NFRA_CLDGRPH $2,828, NFRA_C3MATERIALIZ $2,728,
NFRA_SUBSTRATECAR $2,464, NFRA_COMPEFFICACY $2,117, IRPT_BCKEND $2,003, ETFS_GUARDRAIL $1,965, IRPT_FNTEND $1,447,
LGIC_NAMING $1,312, with $3,560 in seats that committed nothing. Site Z: OPAL_BGFALLBACK $1,409, ETFS_POSITIONING
$1,325, AMGT_RESAPP $1,296, NFRA_OPSEC202609 $1,083, POSN_ASTTAX $812, with $652 uncommitted.

**Three qualifiers on this table, none of them small.** (1) Commits are a PROXY for effort, not a measure of it: a
seat that thinks for an hour and commits once is charged like a seat that commits ten times. (2) Some codes
(NFRA_C3MATERIALIZ, NFRA_SUBSTRATECAR, AUTH_SELFHEAL, ADVI_PERFRP, ADVI_49FSRC) are retired or predate the current
register; they appear because attribution reads the commit message, not registry membership. (3) Exactly one commit
crosses fabrics, inside NFRA_CLDGRPH's history, authored by `0.0.0_AB_MSTR~Z`; every other project on both sides is
clean, so double-counting is one commit wide.

---

## 5. Where the money goes

### By model (MEASURED)

| model | responses | USD | share |
|---|---|---|---|
| Opus 5 | 19,493 | $6,321.15 | 75.9% |
| Fable 5 | 1,324 | $842.79 | 10.1% |
| Fable 5.1 | 1,470 | $560.02 | 6.7% |
| Sonnet 5 | 5,616 | $460.79 | 5.5% |
| Opus 4.8 | 356 | $145.01 | 1.7% |

### By seat (MEASURED; attribution through session files, so approximate)

| seat | responses | USD | share |
|---|---|---|---|
| `0.0.0_AB_MSTR~Z` (the main coordinating agent) | 13,131 | $4,820.52 | 57.9% |
| `1.0.0_SA_CTO~Z` | 2,563 | $858.91 | 10.3% |
| `2.0.0_SA_COO~Z` | 2,179 | $681.59 | 8.2% |
| `2.0.0_SA_COO~ZZZ` | 3,548 | $415.60 | 5.0% |
| `0.0.3_BG_BBGTerminal` | 1,770 | $395.11 | 4.7% |
| `3.0.0_SA_CVO~Z` | 1,115 | $293.62 | 3.5% |
| all other seats and unmapped sessions | 3,953 | $864.40 | 10.4% |

### By effort and by agent type (MEASURED)

- Effort `xhigh` carries $7,699.07 (92.4%); `high` $422.33; `max` $208.35.
- Main seats carry $8,062.95; subagents $266.80 (3.2%).
- Every one of the 28,259 responses records service tier `standard` and inference geography `not_available`.

---

## 6. How to get the most out of Claude

On subscriptions these levers buy **throughput** (more work inside the plan's limits). On the API or Enterprise
they buy **dollars**. The measured what-ifs reprice the same tokens, which assumes the work would not change shape.

| lever | measured basis | effect |
|---|---|---|
| **Keep carried context small.** Restart long-lived agents through hand-over notes; do not let one conversation accumulate the whole fabric. | 453,389 tokens re-read per response; the main coordinating seat alone is 57.9% of spend | cache reads are 72.5% of cost and scale with carried context |
| **Put long-context readers on Fable 5.1, not Opus 5.** | same 30 days of tokens: Fable 5.1 $7,568.43 vs Opus 5 $8,588.84 | about 12% cheaper despite double base prices, because Fable 5.1 reads cache at $0.25 vs $0.50 (REFERENCE) |
| **Match the cache timer to the gap between turns.** | 1-hour writes cost $1,416.15; at the 5-minute rate they would be $885.09 | saves up to $531 a month, but only where turns start less than 5 minutes apart; a miss re-sends the whole prefix |
| **Send reading and bulk work to Sonnet subagents.** | the same 30 days on Sonnet 5 would be $3,435.53 against Opus 5's $8,588.84 | about 60% less for the same tokens |
| **Compute locally; send results, not raw data.** | 29,511 tool calls, 63% of them Bash | a script's answer enters context, the data set does not (a cost win and a sovereignty win) |
| **Spend the top effort settings only where they measurably help.** | `xhigh` is 92.4% of spend | lower effort means fewer and shorter turns for routine seats (REFERENCE guidance) |

Haiku 4.5 would reprice the month at $1,717.77, but it is not a real option for these seats: its context window is
200,000 tokens, under half the average context carried (REFERENCE).

---

## 7. Data sovereignty: what is saved where, and for how long

Setup: personal Max accounts, Claude Code running locally, "Help improve Claude" OFF (STATED).

| data | where | how long | used for training? | label |
|---|---|---|---|---|
| the repositories and data files | this computer | until deleted | no | MEASURED (local) |
| files Claude never reads | this computer only | until deleted | no | SUPPLIED |
| **full session transcripts, including every file excerpt and tool output Claude saw** | this computer, `~/.claude/projects` | **30-day local cleanup** (no override set) | no | MEASURED: 110 files, 0.46 GB, oldest 2026-08-18 |
| tool output that entered context | this computer's transcripts **and** Anthropic | 58.4 MB on disk here; consumer retention there | no general training | MEASURED (local) / SUPPLIED (Anthropic) |
| prompts, context and responses | Anthropic backend | consumer retention, default 30 days | no, with sharing off | SUPPLIED |
| saved conversation history | Anthropic, visible in the account | until deleted, then within 30 days | no | SUPPLIED |
| thumbs-up/down or bug-report content | Anthropic | up to 5 years | possibly | SUPPLIED |
| sessions flagged by safety systems | Anthropic | inputs/outputs up to 2 years; classifier scores up to 7 years | safety use | SUPPLIED |
| legal holds | Anthropic | as required | no | SUPPLIED |

**Two findings from the local side that the supplied thread does not cover.**

1. **Claude Code keeps its own copy of everything it saw, on this computer.** Transcripts hold the file excerpts and
   command output that went into context, for 30 days, readable by anyone with access to the user profile. On a
   shared terminal computer that is an IP exposure independent of Anthropic.
2. **Passwords and keys can pass through context.** 47 transcript lines contain the fabric's secret-reveal command.
   This seat did not inspect whether a value followed each one, deliberately. Any revealed value would sit in the
   local transcript and would have been sent to Anthropic as context.

**What the setup does well.** Execution is local: 63% of tool calls are Bash, so data sets can be processed here and
only answers sent. Training is off. No data leaves the computer except what enters a model request.

---

## 8. What the subscription setup gives up

| capability | personal Max, sharing off | API organization | Claude Enterprise | label |
|---|---|---|---|---|
| training on our data | no | no by default | no by default | SUPPLIED |
| governing terms | consumer | commercial | commercial | SUPPLIED |
| Anthropic's role | consumer service provider | processor for Opal | processor for Opal | SUPPLIED |
| default retention of inputs and outputs | consumer rules, 30 days | automatic deletion within 30 days | org-configurable, 30-day minimum | SUPPLIED |
| zero data retention | no | by agreement | for Claude Code, by agreement | SUPPLIED |
| **Fable 5.1 under zero retention** | not applicable | **not available** unless expressly authorized; 30-day retention required | same | REFERENCE |
| admin and user control | none | workspace/org controls | extensive | SUPPLIED |
| audit logs | none | org/workspace level | yes | SUPPLIED |
| choice of country where data is processed | not recorded (`not_available` on 28,259 of 28,259 responses) | selectable where supported (`inference_geo` parameter) | selectable where supported | MEASURED / REFERENCE |
| policy owner | each account holder's own toggle | the company | the company | SUPPLIED |

**The practical difference is who holds the control.** On subscriptions, Opal's IP posture depends on each account
holder's privacy toggle and on one computer's transcript folder. On a commercial plan the company owns the contract,
the retention policy and the audit trail.

**One constraint worth knowing before any move:** zero data retention and Fable-class models do not combine.
Fable 5 and 5.1 carried $1,402.81 (16.8%) of site Z's month (MEASURED) and require 30-day retention on the API
(REFERENCE).

---

## 9. What the move would cost

| option | monthly cost at site Z's measured usage | label |
|---|---|---|
| today's subscriptions | $1,000 stated, plus $110.04 of extra usage (Andrew's record) | STATED |
| API organization, list price, both machines | $43,282.97 | MEASURED |
| API organization, list price, this computer only | $8,329.75 | MEASURED |
| API with the 1-hour writes moved to 5-minute where it fits | from $7,798.70 | MEASURED what-if |
| Claude Enterprise | $8,329.75 plus the seat fee | SUPPLIED billing model |
| Enterprise with US-only processing | about $9,162.73 plus the seat fee, at 1.1x | SUPPLIED multiplier |

The laptop fabric is not in these figures; its records live on the other device, and its measurement was requested
from `0.0.0_AB_MSTR~Z` at 17:45Z and is still running there.

**The decision, in the supplied thread's own three questions.**

1. *Will Anthropic train on our code?* No on all three setups, with sharing off.
2. *How long does our code sit on Anthropic's infrastructure?* Least controlled on subscriptions; defined at 30 days
   on the API; nothing kept under a zero-retention agreement, where available.
3. *Can employees responsibly use this against company IP?* Only a commercial plan makes that a company control
   rather than a personal setting.

Subscriptions are the right economics while one principal runs the fabric. The trigger to move is a governance
requirement (more users, a client or regulatory demand, an audit), not a training concern. When that trigger
arrives, the monthly bill moves from a subscription to roughly site Z's API-equivalent, so the levers in section 6
become the budget.

---

## 10. Limits and open inputs

- **Two accounts show no renewal in the window.** Section 3 names it; the notices cannot say whether they bill on
  another instrument or no longer exist.
- **List price is not Anthropic's cost** and not what Opal would spend on the API: metered billing would change how
  the fabric works.
- **Two machines, measured separately.** The laptop's transcripts live on the other device and were measured
  there with this folder's own instruments; no third machine is on record, which is absence of evidence
  rather than evidence of absence.
- **Seat attribution is approximate.** Session-serial files are last-writer-wins, and 1,289 responses ($208.80) map
  to no seat.
- **SUPPLIED claims are unverified.** Checking the retention, Enterprise billing and US-only figures against
  Anthropic's live pages needs an egress word for this session.
- **The 30-day window is set by local cleanup.** Older usage is already deleted from this computer.
- **Cache-write split.** Summed across records, the 5-minute and 1-hour write split exceeds the recorded
  cache-creation total by 19,450 tokens (0.01%). Pricing uses the split.

## 11. Reproduce

```bash
python org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/CLAUDE_COST_REPORT_20260917/measure_claude_usage.py \
  --projects "C:/Users/Opal Bloomberg/.claude/projects/C--Users-Opal-Bloomberg-Desktop-ajb-workspace" \
  --sessions org/mcp/sessions --repo . \
  --out org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/CLAUDE_COST_REPORT_20260917/usage_summary.json
```

Run at 2026-09-17T16:30:06Z. Re-running later moves the window, because the local cleanup rolls forward.
