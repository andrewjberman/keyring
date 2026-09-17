# SOURCE -- the GPT thread Andrew supplied, 2026-09-17 ~16:00Z, saved as supplied

**Status of every claim below: SUPPLIED.** This is third-party assistant output that Andrew pasted as context. It is
not Anthropic documentation and it has not been verified by `4.0.0_SA_CRO~Z`. The report cites it as SUPPLIED and
marks which of its numbers were re-measured or cross-checked locally. Text below the rule is unchanged from the
message, including its formatting as pasted.

---

The biggest difference is that Enterprise/API turns your relationship with Anthropic from a consumer privacy relationship into a commercial data-processing relationship. That matters even if you have training disabled on your personal account.

Here’s the practical distinction as of September 2026:

    Personal Claude, training OFF    Anthropic API    Claude Enterprise
Used for general model training    No    No by default    No by default
Who controls submitted data    You under consumer terms    Customer/org    Customer/org
Anthropic's role    Consumer service provider/controller relationship    Commercial processor    Commercial processor
Default backend retention    Consumer retention rules    ≤30 days for normal API I/O    Conversation history retained; org can configure retention
Zero Data Retention    No    Available by agreement/approval    Available for Claude Code by agreement/approval
Organizational admin controls    No    Workspace/org controls    Extensive
Custom retention policy    Limited consumer controls    API policy / contractual    Yes
Auditability    Consumer-level    Org/workspace-level    Audit logs + admin controls
Contract governing company data    Consumer terms    Commercial terms    Commercial terms

Anthropic explicitly says that for commercial customers, the customer is the controller and Anthropic acts as the processor, processing submitted data on the customer's behalf. It also says commercial data isn't used to train its generative models unless the customer explicitly participates in programs that permit it.

API is particularly interesting for your use case

Suppose you ran Claude Code locally exactly as you do now, except instead of authenticating it with your personal Claude account, you authenticated against an Anthropic API organization.

Your architecture becomes roughly:

Your workstation
│
├── proprietary repo
│   ├── foo.py
│   ├── bar.py
│   └── proprietary_data.parquet
│
├── Claude Code
│   │
│   ├── grep/find/bash happen locally
│   ├── files remain locally
│   │
│   └── selected context
│          ↓
│
└──────── Anthropic API
              │
              ├── inference
              ├── response
              └── default API I/O retention ≤30 days

Anthropic says standard API inputs and outputs are automatically deleted from its backend within 30 days, subject to exceptions such as separately retained Files API content, abuse enforcement, legal requirements, or a different contractual arrangement.

And importantly, API data isn't used for model training by default.

So this is materially stronger than merely flipping the consumer training toggle. You're operating under a commercial data-handling regime from the outset.

Then there's Zero Data Retention

This is the substantial step beyond ordinary API usage.

Anthropic offers qualifying API and Claude Code Enterprise organizations Zero Data Retention (ZDR) arrangements. Under ZDR, Anthropic says it does not store the inputs or outputs, except where necessary for legal compliance or misuse/harm prevention; safety-classifier results are still retained.

Conceptually:

LOCAL                              ANTHROPIC

foo.py
   │
   └── Claude reads 80 lines
              │
              ├───────────────► inference
              │                     │
              │◄──────────────── response
              │
              │                  no ordinary
              │                  I/O storage
              ▼
        Claude continues
        working locally

That's a very different security proposition from:

"Anthropic promises not to train on my data."

It's closer to:

"Anthropic needs to transiently process this information to perform inference, but isn't ordinarily retaining the input/output afterward."

There are exceptions. Anthropic says ZDR requires approval and isn't universal across every product. Additionally, certain designated high-capability "Covered Models" can require 30-day retention for safety purposes even for organizations that otherwise have ZDR, depending on the model/platform arrangement.

Enterprise adds governance around the humans

Enterprise isn't primarily about making inference more private than an appropriately configured API.

It's about controlling an organization.

Your company becomes the owner/controller of the workspace. A Primary Owner can manage accounts, determine accessible services/features, and export organizational data.

Enterprise also provides centrally managed retention. For example, an Enterprise owner can establish retention periods for chats and projects; Anthropic currently documents a 30-day minimum for these configurable policies. Changes to retention settings and deletion events are recorded in audit logs.

That gives you something like:

                    COMPANY
                       │
             ┌─────────┴─────────┐
             │                   │
          Identity          Data policy
             │                   │
       users / access       retention
             │              deletion
             │              audit logs
             │
        Claude Enterprise
             │
           Anthropic
          = processor

That's much more appropriate if, say, five Opal developers are working against proprietary repositories. You don't want each developer independently deciding whether their personal "Help improve Claude" switch happens to be enabled.

You want the company controlling the policy.

One other subtle difference: geographic processing

Commercial customers also have some traffic-routing controls. Anthropic says commercial customer data is stored in the U.S. by default, while processing may occur across specified regions unless otherwise agreed or configured. API/Enterprise customers have options for selecting traffic-routing locations in supported configurations.

There are also contractual/compliance mechanisms that simply don't exist in the same way for a consumer account—for example, Anthropic offers BAAs for certain qualifying HIPAA-eligible API deployments, generally associated with eligible/ZDR configurations.

For your particular question, I'd separate three threat models

1. "Will Anthropic train Claude on my proprietary code?"

Personal + training OFF: Anthropic says no.

API: No by default.

Enterprise: No by default.

So there isn't an enormous practical difference on that one dimension.

2. "How much of my proprietary code sits on Anthropic infrastructure after Claude has processed it?"

Now there is a significant difference:

Personal < standard API < ZDR API/Enterprise, in terms of how strongly you can minimize and contractually govern retention.

Standard API already gives you a defined ≤30-day normal I/O deletion window. ZDR can substantially reduce ordinary persistence further.

3. "Can I responsibly allow employees to use this against company IP?"

That's where Enterprise/API is qualitatively different.

It's not dependent upon Andrew remembering to toggle a privacy setting. The company controls the relationship, Anthropic is contractually processing company data, training is off by default, retention is defined, access can be administered, and Enterprise adds organizational retention/auditing controls.

So if you're currently using Claude Code personally against proprietary source code, turning training off addresses the specific training concern surprisingly well. Moving Claude Code to an API/commercial organization becomes compelling when the requirement changes from "don't train on this" to "I need a defensible corporate control around where our IP goes, why it's processed, how long it's retained, and who controls that policy."

I need a very clear understanding of what is saved where and for how long if i have shared usage turned off.

Yes. For your exact setup — personal Claude account + Claude Code running locally + “Help Improve our AI models” OFF — there are really three different places data can exist, and Anthropic's documentation is fairly clear about two of them.

1. Your computer — the actual repository

Your repository/files remain on your machine.

Claude Code's local tools can read foo.py, grep the repo, execute commands, inspect git, etc. Anthropic does not automatically receive a persistent copy of your entire repository merely because Claude Code has access to the directory.

However, anything Claude Code places into the model context is transmitted to Anthropic for inference. So:

LOCAL MACHINE

/proprietary-repo/
    foo.py          ← remains here
    bar.py          ← remains here
    secrets.env     ← remains here

Claude Code reads foo.py
        │
        │ relevant file contents/context
        ▼
ANTHROPIC
        │
        │ inference
        ▼
Claude response

If Claude Code reads all 800 lines of foo.py into context, those 800 lines have gone to Anthropic's servers for processing.

That does not mean Anthropic now has an independently stored foo.py file. The contents are part of the coding-session/model input.

That's an important distinction.

2. Anthropic's normal consumer backend

With model improvement OFF, Anthropic explicitly says it does not use your new or previously stored Claude Code sessions for future general model training.

But training OFF does not mean zero retention.

Anthropic's current consumer policy says the default retention period is 30 days. It specifically says this policy covers:

Free, Pro, Max and when accounts from those plans use Claude Code.

So the easiest mental model for your Claude Code usage is:

YOUR COMPUTER
──────────────────────────────────────────

Entire repo
foo.py
bar.py
data/
etc.

Persistent until YOU delete it.


              selected context
                    │
                    ▼


ANTHROPIC INFERENCE / BACKEND
──────────────────────────────────────────

Prompt
+ conversation/context
+ file contents Claude Code sent
+ tool results sent to Claude
+ Claude output

Normal retention:
~ up to 30 days

Training:
NO
(with model improvement OFF)

There is an important wrinkle concerning saved conversations/session history: Anthropic says consumer prompts/conversations remain available in your history until you delete them; when you delete a conversation, it disappears from your history immediately and is deleted from backend storage within 30 days.

So I would not interpret "30-day default retention" as:

Every Claude Code session automatically vanishes exactly 30 days after I use it.

Anthropic distinguishes between product-visible conversation history and backend deletion. If a conversation/session is persisted in your account, deletion is the mechanism that starts the explicit backend-deletion process.

3. Anthropic's training pipeline

This is the part your switch changes most dramatically.

With:

Settings → Privacy → Help Improve our AI models = OFF

your data does not enter future general Claude training runs. Anthropic explicitly says this includes coding sessions.

So you effectively eliminate this path:

                         ┌──► inference
                         │
Your Claude Code data ───┤
                         │
                         X──► general model-training dataset

Contrast that with having the switch ON:

Your Claude Code data
       │
       ├────► inference
       │
       └────► potentially selected for
              model improvement
                    │
                    ▼
          de-identified training data
                    │
                    ▼
              up to 5 YEARS

Anthropic explicitly states that if model improvement is enabled, consumer chats/coding sessions selected for that purpose may be retained in de-identified form in training pipelines for up to five years.

With your setting OFF, that five-year training retention does not apply.

There are three exceptions you should know about

These are important if we're trying to make the description precise rather than simply saying "30 days."

Safety flagging. If Anthropic's automated systems flag a session as potentially violating its Usage Policy, Anthropic says it can retain the associated inputs and outputs for up to two years, and trust-and-safety classification scores for up to seven years. The content may also be used for safety research/enforcement and Safeguards-model improvement.

Feedback. Don't hit thumbs-up/down or submit a bug report containing sensitive code unless you're comfortable with the consequences. Anthropic says feedback can cause the entire associated conversation to be retained for five years, and it may be used for research/model improvement.

Legal requirements. Anthropic reserves the ability to retain data when legally required or necessary for disputes/policy enforcement.

So the full picture is:

Data    Where    Normal duration    Training?
Your complete repo    Your computer    Until you delete it    No
Files Claude never reads/sends    Your computer    Until you delete them    No
File contents Claude sends as context    Anthropic backend    Consumer retention regime    No general training
Prompts    Anthropic backend    Consumer retention regime    No general training
Claude responses    Anthropic backend    Consumer retention regime    No general training
Saved conversation/session    Anthropic + your account history    Until deleted; backend deletion within 30 days afterward    No general training
Deleted conversation    Anthropic backend temporarily    ≤30 days after deletion    No
Training copy    Training infrastructure    None for future training with setting OFF    No
Explicit feedback    Anthropic    Up to 5 years    Potentially yes
Safety-flagged I/O    Anthropic    Up to 2 years    Safety purposes potentially
Safety classification scores    Anthropic    Up to 7 years    Safety purposes
One subtle but very important example

Suppose you have a proprietary 100 MB database dump:

customer_dump.csv
100 MB

You tell Claude:

Run a Python script locally and tell me how many duplicate customer IDs there are.

If Bash/Python processes that locally and returns:

Duplicate customer IDs: 1,842

then, assuming Claude Code hasn't separately read or included the file, the model needs to receive 1,842, not the 100 MB CSV.

But if you say:

Read customer_dump.csv and analyze every customer.

Claude Code may put substantial portions of the CSV into model context. Those portions are transmitted to Anthropic.

That's why Claude Code can actually provide a meaningful privacy advantage over uploading a file to Claude.ai: the execution environment is local, and you can architect workflows where raw data never needs to enter model context.

What I would consider your actual exposure

Given your setting is OFF, I would not be particularly concerned about Anthropic training Claude on your source code. Their published policy is explicit that they won't do that.

The remaining issue is data retention/processing, not training.

If you're working with valuable proprietary company IP, the distinction I'd focus on is:

Personal Claude Code + opt-out

Anthropic temporarily processes proprietary context under its consumer data regime, with training disabled.

versus

Claude Code + Anthropic API

Anthropic processes proprietary context under its commercial data regime, doesn't train on it by default, automatically deletes normal API I/O from its backend within 30 days, and can potentially offer ZDR.

Anthropic explicitly guarantees the standard API deletion behavior: inputs/outputs are automatically deleted from the backend within 30 days, subject to the enumerated exceptions.

So if what you're ultimately trying to decide is "Is my personal Claude Code setup with sharing OFF sufficiently private for working on Opal's proprietary repository, or should I move my Claude Code authentication to the API?", that's the distinction worth examining next. It is considerably narrower than "Anthropic might train on my whole repo."

Today 11:50 AM
I also want to get a better understanding of cost per token as it pertains to enterprise/api access versus via the subscription model. I know the subscription model is significantly cheaper so I want to understand if there is any prior art either in ANthropic documents or in the web in general where there is  a viable source that covers the divergence in price as of september 2026

Yes. I found unusually good prior art on exactly this question, and the divergence is much larger than I would have guessed from Anthropic's plan names alone.

As of September 17, 2026, the cleanest way to think about Anthropic's pricing is:

Personal Max is a heavily subsidized, rate-limited bundle. API and new Enterprise are metered at list token prices.

Anthropic does not publish an official conversion such as “Max 20x contains $X of API tokens,” because the subscription isn't denominated in tokens and the amount you can consume depends on model mix, caching, conversation length, and rolling limits. But several people have reconstructed the API-equivalent value from actual Claude Code session logs, and the measurements consistently show a roughly 10–40× gap for heavy Claude Code users.

The official prices today

For individuals, Anthropic currently charges $20/month Pro, $100/month Max 5x, and $200/month Max 20x. Those plans include usage up to rolling/session/weekly limits rather than charging per token.

API pricing, by contrast, is explicit. Current major models are:

Model    Input / 1M    Cache read / 1M    Cache write / 1M    Output / 1M
Fable 5.1    $10    $0.25    $12.50    $50
Opus 5    $5    $0.50    $6.25    $25
Sonnet 5    $2    $0.20    $2.50    $10
Haiku 4.5    $1    $0.10    $1.25    $5

The new Enterprise model is especially relevant to your question: the Enterprise seat itself includes zero token allowance. Every token used in Claude, Claude Code, or Cowork is charged at standard API rates on top of the seat fee. Anthropic says that explicitly.

So if you're comparing your personal Max account with a newly purchased Enterprise seat, the economic difference can be enormous.

There is actual measured prior art

Probably the best compilation I found is an August 11 analysis from Quesma. The author collected several real-world measurements in which people took their Claude Code logs and repriced the exact token consumption at Anthropic API list prices.

Observed user    Subscription    Paid    API-equivalent usage    Implied multiplier
Quesma author, June    Max 5x    $100    $2,092    20.9×
Quesma author, July    Max 20x    $200    $2,986    14.9×
Simon Willison    Max 5x    $100    ~$1,200    ~12×
SemiAnalysis stress test    Max 20x    $200    ~$8,000    ~40×

Quesma's author explicitly says his own numbers came from parsing his local Claude Code transcripts and pricing each API call at Anthropic's list prices. That's much more meaningful than estimating from prompts/hour.

Simon Willison's result is independently useful because he's a well-known developer who actually measured his own usage. His Claude Code consumption over roughly a month priced out to $1,199.79 at API rates, while the relevant subscription cost was $100.

And there is a striking recent community measurement from July: one Max 20x user wrote a script that pulled the token counts recorded in Claude Code's session logs and repriced them using the API schedule. Their $200 subscription generated $7,470 of API-equivalent usage that month—a 37.4× ratio. This is a user report rather than an independently audited benchmark, so I'd treat the exact number cautiously, but the methodology is straightforward.

That $7,470 result is remarkably close to the approximately $8,000/month ceiling SemiAnalysis reportedly obtained by deliberately running long-horizon coding tasks until a Max 20x account exhausted its weekly quota.

So the rough empirical range is not 2× or 3×

It's something more like this for a person who actually uses Claude Code heavily:

                       Monthly cost
                       ────────────

Max 5x                $100
                        │
                        └── observed API-equivalent:
                            ~$1,200–$2,100
                            ≈ 12–21×

Max 20x               $200
                        │
                        └── observed API-equivalent:
                            ~$3,000–$8,000+
                            ≈ 15–40×

This does not mean everyone gets $8,000 of usage. The Max plans have rolling and weekly restrictions, different models consume quota differently, and normal users leave a great deal of their theoretical allowance unused. Anthropic itself describes the plans in terms of usage capacity rather than token allotments.

But it establishes that the price discrepancy you're noticing is real.

Why on earth would Anthropic price it this way?

This part requires separating documented fact from economic inference.

I have not found an Anthropic document that says:

“We intentionally subsidize Max users by 20× so we can charge enterprises more later.”

So I would not present that as Anthropic's stated strategy.

What we can observe is that the two products have fundamentally different pricing mechanics.

A subscription is effectively:

$200 fixed revenue
        │
        ▼
Rate-limited capacity

User consumes:
little ──────────────── lots

Anthropic bears the variance

The API is:

tokens consumed
      ×
published rate
      =
customer bill

Customer bears the variance

Most subscription customers will not run Claude Code at the theoretical maximum every waking hour. That's the standard economics of bundled services: light users subsidize very heavy users, while limits prevent truly unconstrained consumption.

Anthropic can therefore offer an enormous marginal value to a power user without every subscriber costing Anthropic the API list price of their usage. API list price is a selling price, not Anthropic's marginal inference cost. A "$7,000 API-equivalent month" absolutely does not mean Anthropic incurred $7,000 in GPU costs to serve that person.

And there is evidence that Anthropic now wants to capture more of this value from organizations.

The strongest evidence is Anthropic's actual 2026 Enterprise pricing change. New Enterprise plans have moved away from bundled usage to:

seat fee + 100% of consumption at API rates

Anthropic even published a new Enterprise consumption-management guide explaining that Claude Code and Cowork can consume tokens much faster than normal chat and that administrators should impose budgets/spend controls.

That is an extraordinary contrast to Max 20x.

Here's the really consequential part for you

Imagine your own usage comes out to $2,500 API-equivalent/month.

Your choices would look approximately like:

Authentication / plan    Approx. monthly Claude usage cost
Max 20x, assuming you fit within its limits    $200
API    $2,500
New Enterprise    $2,500 + Enterprise seat fee
Enterprise + US-only inference    potentially $2,750 + seat fee

Anthropic says US-only inference is charged at 1.1× standard API rates for applicable newer models.

That's why moving from personal Max to Enterprise solely because you want the commercial data-governance treatment can be economically painful. You aren't buying the same $200 product with better privacy controls. You're changing billing models.

And we're starting to see that matter at large organizations. Business Insider reported today that JPMorgan has introduced $2,000 monthly spending limits for some engineers using Claude, alongside its secured internal environment. That number makes much more sense once you understand that Enterprise Claude Code is now metered usage rather than a $100–$200 all-you-can-eat-ish seat.

There's one particularly interesting wrinkle: caching

Claude Code is extremely cache-heavy.

An agent repeatedly carries the repository context, instructions, previous tool calls, edits, etc. through a long session. At API prices, Anthropic doesn't charge ordinary input price every time that cached context reappears—but it still charges for cache reads.

For Opus 5:

fresh input = $5/M
cache write = $6.25/M
cache read = $0.50/M
output = $25/M

For Fable 5.1, Anthropic has recently made cache reads dramatically cheaper:

fresh input = $10/M
cache write = $12.50/M
cache read = $0.25/M
output = $50/M

Quesma found that 82% of the API-equivalent cost in its measured Claude Code sessions was cache-related.

So ordinary intuition like:

“I only typed 300 tokens in that prompt”

is nearly useless for Claude Code economics.

A prompt can initiate an agentic sequence involving tens of millions of cached/context tokens, tool results, subagents, and outputs.

There is also a clean way to calculate your exact discount

This is probably more useful than any benchmark.

Claude Code records token usage in its local session data. Tools such as ccusage parse those records and calculate what your usage would have cost under Anthropic's API prices—the same basic technique used in several of the analyses above.

Then the calculation is simply:

$$ \text{Subscription advantage} = \frac{\text{API-equivalent cost of your actual usage}} {\text{subscription price}} $$

So, for example:

Your Max 20x             = $200

Your last 30 days,
repriced at API rates    = $3,840

$3,840 / $200            = 19.2×

Your effective subscription price for that consumption would therefore be about 5.2% of API list price, i.e. roughly a 94.8% effective discount.

That's the number I would want before making any decision about moving your development workflow onto commercial Anthropic authentication.

My read of the evidence

There are really two separate decisions hiding inside what we've been discussing:

Data: Personal Claude + model improvement OFF actually gives you substantially stronger protection against training than you originally thought.

Commercial governance: API/Enterprise gives you a much more defensible corporate data-processing arrangement, retention controls, contractual status, auditability, etc.

Economics: In exchange for that governance, moving a heavy Claude Code user from Max to new Enterprise/API can plausibly increase inference cost by an order of magnitude or more. The 12–40× observations are sufficiently consistent that I would take this seriously rather than treating it as internet folklore.

The Quesma analysis is probably the single most useful piece of prior art I found because it brings together actual measured users, the SemiAnalysis test, organizational experience, and Anthropic's new Enterprise pricing in one place:

Claude Code pricing: same tokens, same model, up to 40x the price — Quesma, Aug. 11 2026

And Anthropic's own Enterprise billing document confirms the key premise behind their analysis:

Anthropic — How Enterprise billing works

If you want to make this concrete for your actual Claude Code usage, we can inspect your local Claude Code token/session records and calculate what your last 7 or 30 days would have cost on API/Enterprise versus what you actually paid for Max. That would give you a defensible personal multiplier rather than relying on the 12–40× range.
