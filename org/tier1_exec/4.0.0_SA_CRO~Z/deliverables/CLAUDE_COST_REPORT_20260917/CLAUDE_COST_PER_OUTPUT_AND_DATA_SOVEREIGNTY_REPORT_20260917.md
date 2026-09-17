# The true cost per output of Claude at Opal -- and what the personal subscription trades away

**Prepared by** `4.0.0_SA_CRO~Z` for Andrew, 2026-09-17. **Scope:** site Z (the Bloomberg-terminal box and every
Claude Code seat that ran on it) over the 30 days its local session records cover. **Request:** record
`ANDREW_DIRECT_20260917_160xZ_CLAUDE_COST_PER_OUTPUT_REPORT_AND_DECK.md`.

**How to read every number here.** Each carries one of four evidence labels.

| label | meaning |
|---|---|
| MEASURED | read on this box: Claude Code's own session records, git history, local settings, `claude auth status` |
| REFERENCE | the in-environment Claude API reference shipped with Claude Code (model table cached 2026-06-24; caching and retention sections) |
| SUPPLIED | the GPT thread Andrew pasted (saved verbatim beside this report). Not Anthropic documentation and not verified here: no web page was fetched, because this session holds no egress word |
| STATED | Andrew's own statement, not checkable from this box (for example, that usage sharing is off) |

---

## 1. The answer

1. **Site Z consumed $8,329.75 of Claude at API list prices in 30 days** (MEASURED, repriced at REFERENCE rates). On a
   Max subscription that work cost a fixed monthly fee, not $8,330.
2. **Per unit of output, at API prices:** $1.72 per commit, $44.54 per completed task order, $297 per active day.
   On one $200 Max plan the same outputs cost about $0.04, $1.07 and $7.
3. **72% of the bill is re-reading context.** The average response re-read about 453,000 tokens of cached context.
   Context size, not prompt length, is what drives Claude Code's cost.
4. **Training is not the exposure; retention and governance are.** With usage sharing off, the supplied policy says
   sessions are not used for training. What the personal plan gives up is a commercial contract, defined deletion,
   zero-retention options, admin control and audit.
5. **Buying that governance means paying for the tokens.** Enterprise is a seat plus 100% of usage at API rates
   (SUPPLIED), which at site Z's measured usage is at least $8,330 a month before the seat fee.

---

## 2. What was measured

| item | value | label |
|---|---|---|
| Account on this box | `andrew@opalinvest.com`, auth method claude.ai, subscription `max` (tier not reported), no API-key or provider override | MEASURED |
| Records read | 110 transcript files, 203,316 lines, 63,941 usage lines deduplicated to 28,259 priced responses | MEASURED |
| Window | 2026-08-18 16:29Z to 2026-09-17 16:14Z, 28 days with usage | MEASURED |
| Unpriced | 39 `<synthetic>` records with no model | MEASURED |
| Price table | Fable 5.1 $10 in / $50 out / $0.25 cache read; Opus 5 $5 / $25 / $0.50; Sonnet 5 $2 / $10 / $0.20; Haiku 4.5 $1 / $5 / $0.10; cache write 1.25x input (5-minute) or 2x (1-hour) | REFERENCE |

**Method.** Claude Code writes the same usage block once per content block, so a naive sum double-counts. The parser
keeps one record per response (message id + request id), prices each token class separately, and attributes each
session to its seat through `org/mcp/sessions/<session>.serial`, charging subagent work to its parent session.
Reproduce with `measure_claude_usage.py` in this folder; its output is `usage_summary.json`.

---

## 3. The bill we did not pay

### What 30 days of site Z would cost on the API

| token class | tokens | USD | share |
|---|---|---|---|
| cache reads | 12,812,330,931 | $6,036.68 | 72.5% |
| cache writes, 1-hour | 126,693,754 | $1,416.15 | 17.0% |
| output | 32,017,652 | $828.04 | 9.9% |
| cache writes, 5-minute | 18,330,515 | $47.84 | 0.6% |
| fresh input | 145,343 | $1.04 | 0.0% |
| **total** | **12,989,518,195** | **$8,329.75** | |

The last 7 days (2026-09-11 to 2026-09-17) alone come to $2,187.97. (MEASURED)

### Against the subscription

The box reports a Max plan but not its tier, and accounts changed several times during the month, so the
denominator is a range, not a number.

| what paid for the month | monthly fee | API-equivalent multiple | effective discount |
|---|---|---|---|
| one Max 5x | $100 | 83.3x | 98.8% |
| one Max 20x | $200 | 41.6x | 97.6% |
| two Max 20x accounts | $400 | 20.8x | 95.2% |
| three Max 20x accounts | $600 | 13.9x | 92.8% |

**Any extra-usage credits bought this month belong in the fee column too.** The fabric hit a usage-credits block
this week, so that amount is a real input this seat cannot read locally.

### Against the published prior art (SUPPLIED)

The supplied thread cites repriced Claude Code logs of 12x to 21x on Max 5x and 15x to 40x on Max 20x, with a
reported stress-test ceiling near $8,000 a month for one Max 20x account. Site Z's $8,330 sits at that ceiling for
a single account, which is consistent with the month having been spread across more than one account.

---

## 4. Cost per output

| output (site Z, same window) | count | at API list price | on one $200 Max 20x | label |
|---|---|---|---|---|
| commit authored by a site-Z seat or site-Z worker | 4,843 | $1.72 | $0.041 | MEASURED |
| task order completed on a site-Z project | 187 | $44.54 | $1.07 | MEASURED |
| active day | 28 | $297.49 | $7.14 | MEASURED |

**What counts as a site-Z commit.** Lane serials recorded in this box's session map, the terminal seat, and worker
subagents of the six site-Z projects (AMGT_RESAPP, POSN_ASTTAX, POSN_AGGFIX, NFRA_REPORT, NFRA_IAMROLES202609,
NFRA_OPSEC202609). Base serials are excluded because the laptop fabric authors under them. Worker commits are 396 of
the 4,843. **A task order counts** when a diff inside the window added `<status>complete</status>` to it.

**Why per-output is the right unit.** A cheaper request that needs more turns is not cheaper. The fabric's real
product is merged, verified work, so dollars per commit and per completed order are the numbers to manage.

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
| `0.0.0_AB_MSTR~Z` (integrator) | 13,131 | $4,820.52 | 57.9% |
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

On the subscription these levers buy **throughput** (more work inside the plan's limits). On the API or Enterprise
they buy **dollars**. The measured what-ifs reprice the same tokens, which assumes the work would not change shape.

| lever | measured basis | effect |
|---|---|---|
| **Keep carried context small.** Recycle long-lived seats through handoffs; do not let an orchestrator accumulate the whole fabric. | 453,389 tokens re-read per response; the integrator seat alone is 57.9% of spend | cache reads are 72.5% of cost and scale with carried context |
| **Put long-context readers on Fable 5.1, not Opus 5.** | same 30 days of tokens: Fable 5.1 $7,568.43 vs Opus 5 $8,588.84 | about 12% cheaper despite double base prices, because Fable 5.1 reads cache at $0.25 vs $0.50 (REFERENCE) |
| **Match cache TTL to the gap between turns.** | 1-hour writes cost $1,416.15; at the 5-minute rate they would be $885.09 | saves up to $531 a month, but only where turns start less than 5 minutes apart; a miss re-sends the whole prefix |
| **Send reading and bulk work to Sonnet subagents.** | 5,616 Sonnet 5 responses cost $460.79 in total | the same tokens on Opus 5 would cost roughly 2.5x |
| **Compute locally; send results, not raw data.** | 29,511 tool calls, 63% of them Bash | a script's answer enters context, the data set does not (a cost win and a sovereignty win) |
| **Spend `max` effort only where it measurably helps.** | `xhigh` is 92.4% of spend | lower effort means fewer and shorter turns for routine seats (REFERENCE guidance) |

Haiku 4.5 would reprice the month at $1,717.77, but it is not a real option for these seats: its context window is
200,000 tokens, under half the average context carried (REFERENCE).

---

## 7. Data sovereignty: what is saved where, and for how long

Setup: personal Max account, Claude Code running locally, "Help improve Claude" OFF (STATED).

| data | where | how long | used for training? | label |
|---|---|---|---|---|
| the repositories and data files | this box | until deleted | no | MEASURED (local) |
| files Claude never reads | this box only | until deleted | no | SUPPLIED |
| **full session transcripts, including every file excerpt and tool output Claude saw** | this box, `~/.claude/projects` | **30-day local cleanup** (no override set) | no | MEASURED: 110 files, 0.46 GB, oldest 2026-08-18 |
| tool output that entered context | this box's transcripts **and** Anthropic | 58.4 MB on disk here; consumer retention there | no general training | MEASURED (local) / SUPPLIED (Anthropic) |
| prompts, context and responses | Anthropic backend | consumer retention, default 30 days | no, with sharing off | SUPPLIED |
| saved conversation history | Anthropic, visible in the account | until deleted, then within 30 days | no | SUPPLIED |
| thumbs-up/down or bug-report content | Anthropic | up to 5 years | possibly | SUPPLIED |
| sessions flagged by safety systems | Anthropic | inputs/outputs up to 2 years; classifier scores up to 7 years | safety use | SUPPLIED |
| legal holds | Anthropic | as required | no | SUPPLIED |

**Two findings from the local side that the supplied thread does not cover.**

1. **Claude Code keeps its own copy of everything it saw, on this box.** Transcripts hold the file excerpts and
   command output that went into context, for 30 days, readable by anyone with access to the user profile. On a
   shared terminal box that is an IP exposure independent of Anthropic.
2. **Secrets can pass through context.** 47 transcript lines contain the fabric's secret-reveal command. This seat did
   not inspect whether a value followed each one, deliberately. Any revealed value would sit in the local transcript
   and would have been sent to Anthropic as context.

**What the setup does well.** Execution is local: 63% of tool calls are Bash, so data sets can be processed on the box
and only answers sent. Training is off. No data leaves the box except what enters a model request.

---

## 8. What the personal plan gives up

| capability | personal Max, sharing off | API organization | Claude Enterprise | label |
|---|---|---|---|---|
| training on our data | no | no by default | no by default | SUPPLIED |
| governing terms | consumer | commercial | commercial | SUPPLIED |
| Anthropic's role | consumer service provider | processor for Opal | processor for Opal | SUPPLIED |
| default retention of I/O | consumer rules, 30 days | automatic deletion within 30 days | org-configurable, 30-day minimum | SUPPLIED |
| zero data retention | no | by agreement | for Claude Code, by agreement | SUPPLIED |
| **Fable 5.1 under zero retention** | not applicable | **not available** unless expressly authorized; 30-day retention required | same | REFERENCE |
| admin and user control | none | workspace/org controls | extensive | SUPPLIED |
| audit logs | none | org/workspace level | yes | SUPPLIED |
| inference geography | not recorded (`not_available` on 28,259 of 28,259 responses) | selectable where supported (`inference_geo` parameter) | selectable where supported | MEASURED / REFERENCE |
| policy owner | the individual's own toggle | the company | the company | SUPPLIED |

**The practical difference is who holds the control.** On the personal plan, Opal's IP posture depends on one person's
privacy toggle and on one box's transcript folder. On a commercial plan the company owns the contract, the retention
policy and the audit trail.

**One constraint worth knowing before any move:** zero data retention and Fable-class models do not combine.
Fable 5 and 5.1 carried $1,402.81 (16.8%) of site Z's month (MEASURED) and require 30-day retention on the API
(REFERENCE).

---

## 9. What the move would cost

| option | monthly cost at site Z's measured usage | label |
|---|---|---|
| personal Max 20x, if one account covers it | $200 plus any extra-usage credits | MEASURED usage / SUPPLIED price |
| API organization, list price | $8,329.75 | MEASURED |
| API with the 1-hour writes moved to 5-minute where it fits | from $7,798.70 | MEASURED what-if |
| Claude Enterprise | $8,329.75 plus the seat fee | SUPPLIED billing model |
| Enterprise with US-only inference | about $9,162.73 plus the seat fee, at 1.1x | SUPPLIED multiplier |

The laptop fabric is not in these figures; its records live on the other device.

**The decision, in the supplied thread's own three questions.**

1. *Will Anthropic train on our code?* No on all three setups, with sharing off.
2. *How long does our code sit on Anthropic's infrastructure?* Personal least controlled; API defined at 30 days;
   zero retention strongest, where available.
3. *Can employees responsibly use this against company IP?* Only a commercial plan makes that a company control
   rather than a personal setting.

The personal plan is the right economics for one principal running the fabric. The trigger to move is a governance
requirement (more users, a client or regulatory demand, an audit), not a training concern. When that trigger arrives,
the monthly bill moves from a subscription to roughly site Z's API-equivalent, so the levers in section 6 become the
budget.

---

## 10. Limits and open inputs

- **Subscription denominator.** The tier and the number of accounts used this month are not recorded locally, and
  extra-usage credits are not visible here. Section 3 shows the range.
- **List price is not Anthropic's cost** and not what Opal would spend on the API: metered billing would change how
  the fabric works.
- **Site Z only.** The laptop fabric's transcripts are on the other device.
- **Seat attribution is approximate.** Session-serial files are last-writer-wins, and 1,289 responses ($208.80) map to
  no seat.
- **SUPPLIED claims are unverified.** Checking the retention, Enterprise billing and US-only figures against
  Anthropic's live pages needs an egress word for this session.
- **The 30-day window is set by local cleanup.** Older usage is already deleted from this box.
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
