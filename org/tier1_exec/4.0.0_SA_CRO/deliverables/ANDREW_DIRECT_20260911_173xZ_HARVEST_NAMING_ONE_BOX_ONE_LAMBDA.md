# ANDREW-DIRECT 2026-09-11 ~17:3xZ -- HARVEST NAMING, ONE BOX AND ONE LAMBDA

**Channel:** direct to `4.0.0_SA_CRO~Z` at this terminal, mid-turn, while that seat was measuring the
publisher estate for a `/draw` he had asked for.
**Recorded by:** `4.0.0_SA_CRO~Z`. **Broadcast:** same turn, to `1.0.0_SA_CTO~Z`, `2.0.0_SA_COO~ZZZ`,
`0.0.0_AB_MSTR~Z`.

## VERBATIM AND ENTIRE

> dont mind the preexisting stuff, this should be one box and one lambda titled as "harvesters" using
> harvest language. buckets would be opal-data-harvest, and so on

## CONTEXT IT ARRIVED IN, so the next reader knows what he was answering

He had asked (same turn, immediately prior) for a `/draw` of "the current state of the 4 publisher
ec2/lambda/bucket resources and arrangement and how it feeds the portal", then a `/draw` of the data
to start backfilling, and said **"backfilling should be handled on this local box rather than
delegated to a cloud process."**

This seat's measurement in progress had just surfaced a large PRE-EXISTING publisher estate:
`astn-wsjft-scraper` (EC2, DECLARED, project ASTN_WSJFT) plus an UNDECLARED Seeking Alpha estate
(2x EC2 `seeking-alpha-scraper`, 7 Lambdas, `seeking-alpha-article-urls` + `opal-news-articles`
tables, role and SG, all `tf_managed: false`). **"dont mind the preexisting stuff" is read as
scoping THE REPORT he asked for** -- see the NOT-ADJUDICATED list.

## WHAT IS PLAINLY DIRECTED

1. **ONE BOX and ONE LAMBDA**, not a fleet and not one per publisher.
2. **Titled "harvesters", using HARVEST LANGUAGE** throughout.
3. **Buckets take the `opal-data-harvest` shape**, "and so on" -- the naming generalises.

## ⛔ NOT ADJUDICATED BY THIS SEAT -- SURFACE, DO NOT ADJUDICATE (CLAUDE.md s.2)

Each of these is a real fork his sentence admits and this seat does NOT pick one. They matter because
**AMGT_RESAPP round 5 is ISSUED AND SPAWNED** (`@dcbebda22c`) and three of them touch landed or
imminent work.

| # | the fork | why it is not this seat's to settle |
|---|---|---|
| 1 | Does the harvest naming reach the **ALREADY-LANDED** `rd-1`/`rd-2` stores -- live DynamoDB tables `opal-amgt-articles` and `opal-amgt-security-metrics`, both complete and merged? | A DynamoDB rename is a DESTROY/RECREATE, not an edit. Retroactive vs prospective is his call, and the cells are terminal. |
| 2 | He said **"buckets"**; `rd-1`/`rd-2` built **TABLES**. Is `opal-data-harvest` a NEW S3 bucket, or is "buckets" loose for "stores"? | Substrate choice, not naming. Changes what `rd-3`/`rd-4` write to. |
| 3 | Does it reach the **live, versioned** `opal-data-research` bucket, which ALREADY HOLDS this project's round-1 output under `derived/model_block/`? | An S3 rename is create-copy-delete on a bucket with data in it. Never inferred. |
| 4 | `rd-4` is cut as **"four harvesters"**; he says **ONE lambda**. Does ONE LAMBDA supersede `rd-4`'s shape? | `rd-4` is STAGED and next-but-one in chain A. Mid-round the spec and decomposition are FROZEN (Rule 27) -- a reshape is an L10 addendum or a recut, the CTO's and COO's, never a seat's. |
| 5 | "dont mind the preexisting stuff" -- scope THE REPORT, or also **leave the pre-existing estate alone** (neither reuse nor retire it)? | Read here as scoping the report. A wider read would authorise a retirement nobody asked for. |

## WHY THIS IS TIME-CRITICAL, stated once

Round 5's CHAIN A is `rd-1` (COMPLETE) -> **`rd-3` harvester box + its own IAM role (STAGED, NEXT)**
-> `rd-4` four harvesters (STAGED). `rd-3` can spawn at any drain tick. **A box and an IAM role cut
under the old naming is infrastructure to rename afterwards, and an IAM role rename is not free.**
That is the whole reason this record and its broadcast are same-turn rather than queued behind the
`/draw` he asked for.

## TWO FURTHER DIRECTIVES, SAME CHANNEL, MINUTES LATER -- VERBATIM AND ENTIRE

> just want to make sure everything is canonical and self-contained in this harvest estate

> that is something I need you to oversee and execute, you have full egress and override authority to
> realize it. just /draw me your intended architecture and i can approve/revise.

### What these plainly direct

4. **CANONICAL AND SELF-CONTAINED** is the acceptance property of the harvest estate.
5. **`4.0.0_SA_CRO~Z` OVERSEES AND EXECUTES IT**, with **full egress authority** and **override
   authority** to realize it. This is a sovereign assignment and it supersedes Rule 27's ordinary
   role exclusivity for this scope; it is recorded here rather than inferred.
6. ⭐ **HE SET HIS OWN GATE AND IT IS NOT THIS SEAT'S TO SKIP: "just /draw me your intended
   architecture and i can approve/revise."** The DRAW COMES FIRST AND HE APPROVES IT. Nothing is
   built, applied, renamed or egressed before that approval. **The authority granted in (5) does not
   fire until the gate in (6) clears** -- reading a grant of authority as permission to start is
   exactly the over-reach this record exists to prevent.

## A FOURTH DIRECTIVE, SAME CHANNEL, MINUTES LATER -- VERBATIM AND ENTIRE

> also I see COO~ZZZ workers looking into terraforming things, all of that is going to need to go
> into the harvester tf here

### What this plainly directs

7. **ALL OF `2.0.0_SA_COO~ZZZ`'s WORKERS' TERRAFORM CONSOLIDATES INTO THE HARVESTER TF.** One module
   for the harvest estate. This is the operational half of "canonical and self-contained".

⭐ **THIS NARROWS THE COLLISION BELOW:** the terraform DESTINATION is now settled by his word -- one
harvester module -- even though WHO WRITES each resource is not. A round-5 worker's terraform is not
refused; it is REDIRECTED into the harvester module rather than landing in a module of its own.

⚠ **MEASURED, AND IT IS ALREADY TWO MODULES, NOT ONE:** this project's terraform is TODAY split
across `infra/aws/terraform/research/` (`s3.tf` the `opal-data-research` bucket, `sqs.tf` the pull
queue, `api-gateway.tf` the enqueue Lambda + portal route; state key `research/tfstate`) AND
`infra/aws/terraform/amgt-resapp/` (`dynamodb.tf`, `security-metrics-table.tf`, its own backend).
**Consolidating them is a TERRAFORM STATE MOVE across two backends, not a file move** -- `state mv`
or `import`, with the live resources unchanged underneath. Named here so nobody treats it as a
copy-paste. NOT ADJUDICATED: whether consolidation is retroactive over both existing modules or
prospective for new resources only.

### ⛔ THE OPERATIONAL COLLISION THIS CREATES, surfaced immediately and NOT adjudicated

**AMGT_RESAPP round 5 is ISSUED AND SPAWNED (`@dcbebda22c`) and `2.0.0_SA_COO~ZZZ` holds it.**
Chain A is `rd-1` (COMPLETE) -> **`rd-3` harvester box + its own IAM role (STAGED)** -> **`rd-4` four
harvesters (STAGED)**. Those two cells cover THE SAME SURFACE Andrew has just assigned to this seat.

⛔ **TWO BUILDERS ON ONE WRITE SURFACE IS THE COLLISION `ONE ISSUER PER ROUND` EXISTS TO PREVENT.**
If `rd-3` spawns a worker while this seat builds the same box, the estate gets two boxes, two IAM
roles, or a half-built one of each. **This seat will NOT touch that surface until the routing is
settled**, whichever way it settles:
  (a) round 5's `rd-3`/`rd-4` are PARKED or superseded and this seat builds; or
  (b) this seat specifies and `2.0.0_SA_COO~ZZZ` cuts it as the round holder.
Andrew's "override authority" ADMITS (a). It does not make (a) automatic, and it is not this seat's
to declare unilaterally against a live round holder. **Routed to `2.0.0_SA_COO~ZZZ` and
`1.0.0_SA_CTO~Z` in the same broadcast as this record.**

## A FIFTH DIRECTIVE, SAME CHANNEL -- VERBATIM AND ENTIRE

> the harvester tf is basically the primary feeder resources for the Security Analysis application.

### What this plainly directs

8. **THE HARVESTER TF'S SCOPE IS "THE PRIMARY FEEDER RESOURCES" for the Security Analysis
   application** (AMGT_RESAPP: *"an analyst opens a covered name and the model block, company
   description and segment breakdown are already there"*). This is the module's BOUNDARY, and it is
   the sentence that decides what belongs in it and what does not.

**How this seat reads the boundary in the draw, stated so he can revise it:** IN = everything that
puts data in front of the application -- the harvest box, the harvest Lambda, the harvest stores, the
request queue and the enqueue path. OUT = the application's own presentation surface (the `.tsx`
lead panel and tabs, `rd-8`), which CONSUMES the feed rather than being part of it. ⚠ **That is this
seat's reading of "primary feeder", offered for approval, NOT a ruling** -- the line between feeder
and app is exactly the kind of boundary he may want drawn differently, and it is cheap to move now
and expensive to move after the module exists.

## THE APPROVAL AND THE SIXTH DIRECTIVE, 2026-09-11 ~18:3xZ -- VERBATIM AND ENTIRE

Answering `/open-calls` (3 cards: harvest box location; GO on the architecture; portal route rename).

> all recs approved aside from the local box comment. this box is sitez. it is a local server at Opal,
> not an aws cloud box. accordingly it is not terraformed nor included in the aws resource cloud.

### WHAT IS NOW SETTLED

9. ⭐ **THE DRAW IS APPROVED. The GO is given** (card 2's REC approved): execute module consolidation
   and renames FIRST while both stores are empty, then the backfill, then the box and lambda.
10. **Card 3 approved: the portal hold STANDS and the route rename is DEFERRED.**
    `/api/private/research/pull` keeps its path; the estate is canonical everywhere else. No portal
    promote, PROD or DEV.
11. **The lane-override decision was put to him as DECIDED-not-asked and drew no objection** --
    terraform commits go under an audited `GIT_COMMIT_AUTHOR_OVERRIDE`, one per lane, naming his
    grant as the reason. No permanent lane amendment to `.owned-paths.yaml`.
12. ⛔ **CARD 1'S REC IS REJECTED, AND THE REASON IS THE CORRECTION THAT MATTERS:** site-Z is a
    **LOCAL SERVER AT OPAL**, not an AWS cloud box -- **NOT terraformed and NOT part of the AWS
    resource estate.**

### THIS SEAT'S READING OF (12), STATED AS A READING SO HE CAN STOP IT

He rejected the local box WITH A REASON THAT RULES IT OUT rather than merely preferring EC2: a
harvester box on site-Z could not be terraformed and could not sit inside the harvest estate, which
would defeat directive 2's "canonical and self-contained" outright and directive 8's "the harvester tf
is the primary feeder resources". **So the harvester box is an EC2 INSTANCE, declared in the harvest
module.** Site-Z keeps the BACKFILL, which is unchanged and uncontradicted -- his earlier word
*"backfilling should be handled on this local box rather than delegated to a cloud process"* describes
a one-shot operator PROCESS, not a provisioned resource, so it never needed to be in the estate.

⚠ **THIS SEAT'S OWN ERROR, NAMED:** card 1 recommended site-Z as THE harvest box on IP-reputation
evidence. That reasoning was sound about bot walls and WRONG about the estate -- it would have put the
feeder's compute outside terraform while the whole directive was to make the estate canonical and
self-contained. **A correct local fact (residential IP clears PerimeterX) was allowed to decide a
question it does not govern.**

### ⚠ THE PROBLEM THAT MOVES RATHER THAN DISAPPEARS -- carried into the build, not re-litigated

The bot-wall evidence stands: this seat's own harvest screenshots show three consecutive `BOT_WALL`
steps before `LOGGED_IN` from a residential IP, and an EC2 datacenter range is a worse signal for
PerimeterX. **That is now an ENGINEERING PROBLEM INSIDE THE EC2 DESIGN, not a reason to move the
box.** Two routes exist and both are already in this estate's vocabulary: the proven
`press_and_hold_lib.py` mechanism with more retries, or routing sessions through the Bright Data Web
Unlocker path WSJ already uses.
⛔ **NOT ASSUMED: extending Web Unlocker from WSJ to the three SESSION harvesters is a NEW per-use
vendor question.** `C-VENDOR-WORD-HARVESTERS` covers egress TO Seeking Alpha, FT, Bloomberg and WSJ
for this project's harvesters; it does not silently authorise a new PROXY VENDOR for platforms that
did not use one. If the EC2 IP proves unworkable, that is a call for Andrew, not an inference.

## NOT DONE HERE

No PRD edit, no decomposition edit, no task-order edit, no rename, no gate. This seat holds L1 and
authored none of the round-5 cells. `1.0.0_SA_CTO~Z` owns the PRD/addendum; `2.0.0_SA_COO~ZZZ` owns
the decomposition and the issuance.

Push state: LOCAL at write; this seat does not push.
