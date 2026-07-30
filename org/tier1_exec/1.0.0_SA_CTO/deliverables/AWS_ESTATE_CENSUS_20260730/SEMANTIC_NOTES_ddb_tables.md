# Semantic notes — DynamoDB tables, in Andrew's words
(same capture protocol as s3_buckets.md)


---

# DynamoDB layer — Batch 1 (2026-07-30, cards 1-7 of 37)

## 1/37 opal-sessions — DECOMMISSION THE WHOLE SYSTEM (destructive step pending permission GO)

**Verbatim:** "Get rid of opal-sessions completely, i dont caare about this its a deprecated
system that is no longer in use and all opal-sessions analytics, which was essentially a UI
analysis schema for the portal, should be decommissioned and deleted. its useful only to see
what is connected to it so we know what else should be deleted."
**Connected-system enumeration (the 'what else'):** opal-session-analytics LAMBDA (sole env
ref) + 4 API routes (POST /analytics/ingest, GET /analytics/session, GET /analytics/sessions,
GET /analytics/summary) + portal-side ingest calls (frontend posts) + the table (675K items,
373MB). Shared opal-portal-lambda-role is NOT part of the kill (shared role).
**Execution state:** delete-table attempt DENIED at the permission layer (destructive gate).
Package staged as Q-23; backup-capture precedes the table delete whenever the GO lands.

## 2/37 opal-news-articles — investigation VERDICT: it IS the news pipeline's article store. KEEP.

**Verbatim (the ask):** "need to investigate this one to make sure this is not actually our
entire news pipeline data source, id be hesitant to delete it either way..."
**Verdict:** 9 lambdas name it in live env, spanning the ENTIRE news family INCLUDING the live
trending vein (news-trending-analysis) and the keyword-intel chain ruled essential (cards 5/7):
news-ingestion-scheduler, sentiment, semantic-clustering, layer3-curation, keyword-intelligence-
generator, keyword-drilldown, both seeking-alpha scrapers. Andrew's hesitation validated at
source: KEEP.

## 3/37 nessie tables — KEEP + "all globgrph resources need to be summarily terraformed" -> Q-24

## 4/37 opal-assets-daily-aua — ANALYZED (Andrew ordered). HYPOTHESIS NOT CONFIRMED.

**The ask:** "i suspect this is the canonical source for ETFS tracking but need that validated."
**Finding:** it is NOT ETF tracking. It is the COHORT-AUA DAILY RECORD -- key (run_date,
cohort_id) + cohort_history GSI; rows carry cohort_name ('49F Dividend SMA'), value_class=
model_value, derivation=smartx_closing_equity, overlap_of=49f_schwab_custody, full vintage
discipline (vintage_state/coverage_state, staleness sentinel contract shared with the 14
mdpf-cohort-freshness alarms; rows even carry the T-1 doctrine in prose). History depth to
2020-12-15. Writer: opal-assets-daily-emitter (sole, rule opal-assets-daily-emitter-daily,
1 invocation/day exercised across 14d + ONE 6,423-invocation day on 2026-07-23 = backfill
burst, flagged not chased). Emitter env: reads ETFS_BUCKET + MONOLITH_BUCKET, writes
PLATINUM_BUCKET (portal-v2) + this table. ETF ownership tracking lives elsewhere
(opal-etfs-ownership-daily + opal-data-etfs). VERDICT: essential AUA/MDPF-adjacent infra, KEEP.

## 5/37 opal-news-trending-daily — KEEP ("essential infra for the news pipeline")
## 6/37 opal-portal-market-data — KEEP ("essential infra for portal market intelligence")
## 7/37 opal-keyword-intelligence — KEEP ("essential infra for news pipeline and portal topic cloud")


---

# DynamoDB layer — Batch 2 (2026-07-30, cards 8-14 of 37)

## 8/37 seeking-alpha-article-urls — "we almost certainly dont need" -> rides the Q-15 kill
0.7.0's same-hour reader census upgraded the WHOLE seeking-alpha channel to CONFIRMED-KILLABLE:
the channel DIED 2026-04-14 and has written zero-content receipts daily for 107 days. This table
(chain-private dedup ledger) dies in step 2 of their 5-step sequence.

## 9/37 bd-securities — portal-consumption check: NOT CONFIRMED (denominator: 2 of 28)
**Verbatim:** "we need to check if the portal consumes this in any way, I suspect that it does,
but it could also be a deprecated source for transaction engine security ID for the now
deprecated process in bd-gold pipeline runner."
**Gate result:** env refs across 192 lambdas: NONE. Deployed-code grep of the 2 strongest
portal-critical modeled readers (portfolio-version-get, pm-optimization-loader): NONE. The 28
modeled reader edges look like attribution inflation. LEANS the bd-gold-deprecated-source
hypothesis; full reader census (0.7.0's recipe) closes it -> folded into DDB handoff (Q-26).

## 10/37 opal-pii-lookup — "dont care about this, delete" -> EXECUTE-READY, permission-staged
delete-table DENIED by my session's permission profile (2nd occurrence; destructive gate).
Staged execute-ready in Q-23 alongside opal-sessions: backup-capture -> delete -> verify, 0.7.0
lane. PII note: the backup itself holds identity mappings; its retention is part of the ruling.

## 11/37 opal-data-smartx — KEEP-for-now, expected deprecated by assets/smartx (rides Q-13)
## 12/37 opal-trade-submissions — KEEP (trade product C4 interactive-products)

## 13/37 semantic-news-trending-daily — twin check: NOT a live twin; a FROZEN EXPERIMENT SIBLING
Same key schema (date, topic_rank) but different generation: cluster_synthesis/curation_method
schema, sample content Feb-vintage crypto news; 113 rows vs the product's 4,300. Matches the
semantic_clusters/ freeze (02-24) and the unmapped semantic-news-layer3-curation lambda. Fate
couples to the news-experiment teardown, NOT to the live trending product.

## 14/37 opal-etfs-ownership-daily — P0 CANONICALITY INVESTIGATION (Q-25)
**Verbatim:** "this definitely needs to be investigated, there are so many ETFS ownership tables
now, one of them is canonical and complete, i just dont know which, and that is a P0
investigation matter for 0.7.0 when we hand off the investigation report for DDB assets."
Post-Aug-1-fire only (C-5).


---

# DynamoDB layer — Batch 3 (2026-07-30, cards 15-22 of 37): the identity/authz cluster

## 15/37 opal-users — DEPRECATED (Andrew 90%; CONFIRMED at source the same turn)
**Verbatim:** "opal-users i am 90% sure is deprecated"
**Confirmation:** single-key (email HASH), no GSI, created 2025-12-29, 12 items -- but its rows
ALREADY CARRY PK/SK attributes, i.e. written into the v2 shape then left behind. Neither live
consumer names it. Deprecation RULED; deletion NOT yet authorized (auth-surface caution).

## 16/37 opal-users-v2 — ** THE OFFICIAL USER DATABASE ** (log wherever possible)
**Verbatim:** "opal-users-v2 is the official user database (very important to note and log
wherever possible)."
**Confirmed:** trade-auth-handler + opal-partners-data both carry USERS_TABLE=opal-users-v2 in
DEPLOYED env; PK/SK composite + firmId-index + email-index GSIs; created 2026-01-08; 72 items;
richer schema (firstName/lastName/lastLogin/passwordChangedAt).
**Logged to:** this file, RULINGS_LEDGER, and a durable memory entry
(memory/project_opal_users_v2_is_the_official_user_database.md) so it survives sessions.

## 17/37 user-permissions — INVESTIGATE (Q-27)
"definitely needs further investigation." Double-silent (0 graph edges, 0 env refs) on the AUTHZ
surface -- the dangerous kind of silence; auth code hardcodes table names.

## 18-21/37 opal-partner-{49financial,inflection,cottonwood,demo} — KEEP, purpose recorded
**Verbatim:** "the opal-partner tables are scoped-permissions for the partner views, essentially
because the advisor intelligence function varies in depth/scope based on the advisor, there may
be different interfaces / designs which require different forms of access gating, the idea
behind these opal-partner-* tables was so that we could design those scoped permissions for the
various firms specifically based on those design choices and their organizations needs."
**Normalized:** per-firm SCOPED-PERMISSION registries for Advisor Intelligence access gating;
existence is deliberate design, not duplication. (PORTAL_AUTHHARD lineage: the latent
user@cottonwood.com row lives in this family -- deprecated as a QUESTION per Andrew 07-29, the
ROW itself still exists.)

## 22/37 etf-classifications — KEEP, canonical (widest read-fan in the layer: 42 readers)
"almost certainly key infra for various portfolio analytics on the yang pipeline" -- matches
CLAUDE.md's Architecture Decisions entry (ETFClassifier = canonical system, new tickers go to
DynamoDB directly). Distinct from the Q-25 ETFS-OWNERSHIP canonicality question (classification
!= ownership) -- noted so the P0 does not conflate them.

## CROSS-CUTTING FINDING (batch 3)
Five of eight tables in the identity/authz cluster have ZERO graph edges AND ZERO env refs --
auth code hardcodes table names. **The graph is blindest exactly where the security surface
lives.** Q-6 adjacency, sharper; feeds the DDB handoff report.


---

# DynamoDB layer — Batch 4 (2026-07-30, cards 23-29 of 37)

**PROVENANCE NOTE, and it matters for how these rows should be read.** Andrew delegated this
batch: *"ok annotate according to your recs"* -- so cards 23-28 carry **CTO recommendations
adopted under explicit sovereign delegation**, NOT sovereign verbatims. Card 29 is his own
words. The ledger `basis` field distinguishes the two on every row; a later reader must not
promote a delegated annotation into a ruling Andrew made himself. (This is the first delegated
batch in the program -- the distinction is now part of the capture protocol.)

## 23/37 opal-data-refresh-executions — KEEP (delegated)
Live run-ledger for the portal's data-refresh + time-machine. Writers/readers env-confirmed
(opal-data-refresh-api, portal-time-machine, yang-varflag-check). Historical note: this is the
table behind CLAUDE.md Rule-22a's resource-style blindness specimen (comp-iam reported 0
dynamodb ops on opal-data-refresh-api while it executed 5) -- instrument since fixed; the table
is the evidence that produced the fix.

## 24/37 trade-security-identifiers — KEEP (delegated) + PAIR WITH CARD 9 IN THE CENSUS
Security-ID lookup for the Trade Submission product (C4 interactive-products), read+written by
the 7-lambda trade family, table name code-hardcoded (0 env refs -- that family's pattern).
**Not ruled blind:** it and bd-securities (card 9) are two securities-reference tables serving
two different products; whether that is correct separation or a consolidation opportunity is
folded into Q-26 rather than guessed here.

## 25/37 find-insure-cost-state — RIDES THE imo KEEP-PARKED RULING (delegated)
The FIND_INSURE quartet's cost/state tracker; idle since 06-01, exactly like the imo bucket
Andrew ruled KEEP-parked (prospecting asset -- dormancy is the wrong axis, C-7). Same estate,
same fate, no separate ruling needed.

## 26+27/37 opal-portfolio-sessions + opal-portfolio-exports — KEEP AS A PAIR (delegated)
One mechanism split across two tables: the PM export pipeline's session state (16 items) and
export records (6 items). Same two writers (excel-generator, export-download), env-confirmed.
Ruled as a unit because they fail and live as a unit.

## 28/37 opal-globgrph-nessie-_refs — RIDES Q-24 (delegated)
The Nessie branch/ref store (52 refs incl. 'main'), sibling of card 3 (_objs). Zero graph edges
again -- the same ECS->DDB derive gap; the graph cannot see its own catalog's branch pointers.
Covered by Andrew's standing ruling that ALL globgrph resources be summarily terraformed.

## 29/37 opal-tickets — KEEP, DEFERRED POST-CLEANUP (Andrew verbatim)
**Verbatim:** "the ticket center will be proceeded, but it is a nice to have, something we will
have to address after comprehensive cleanup."
**Normalized:** business_function = Ticket Center store (shipped product, 2 records = adoption
not yet pursued); target_state = KEEP; priority = EXPLICITLY DEFERRED until after the
comprehensive cleanup completes. Not a prune candidate at any point; do not re-surface it as
one on the strength of its row count.


---

# DynamoDB layer — Batch 5 FINAL (2026-07-30, cards 30-37 of 37). THE DDB LAYER IS COMPLETE.

## 30/37 trade-users — TEARDOWN with the parquet leg, investigate first
**Verbatim:** "I think 30 was a proto version of what became the trade submission product, i
dont believe any of that is necessary and should be gotten rid of alongside the deprecated
parquet output trade submission resource we noticed earlier in the session, that should be
investigated though."
**Normalized:** target_state=TEARDOWN, coupled to the Q-7 parquet-batch-export leg (dead since
01-21); gate=investigation. NOTE the discrimination required: opal-trade-submissions (27 items,
Andrew KEPT it card 12) and trade-security-identifiers (KEPT card 24) are the LIVE product;
trade-users is the proto's user roster. A teardown must not sweep the family by name prefix
(C-15 applies to resource families, not just keys).

## 31/37 market-updates — "probably a tear down"; rides Q-16
1 row, written/read by market-update-{data-aggregator,exporter,generator} -- the same family as
the fred/market-update teardown package. Fate couples to Q-16.

## 32/37 opal-inf-launch-locks — INVESTIGATED: HEALTHY BY DESIGN, KEEP
**The ask:** "looks potentially suspicious to me, id want to know what this is connected to and
its function."
**Answer:** it is an EC2 LAUNCH-RETRY MUTEX for the inf pipeline. Key
(instance_id HASH, attempt_window_start RANGE); **TTL ENABLED on expires_at**; owner
inf-ec2-retry-launch (env LAUNCH_LOCKS_TABLE + SNS inf-otp-alert), partner inf-jwt-trigger
(EXPORTER_INSTANCE_ID=i-081ae6aafb394fb1a). It prevents duplicate/racing EC2 launch attempts
inside a window and lets the rows self-expire. **ZERO ITEMS IS THE SUCCESS STATE** -- no launch
contention in flight. Nothing suspicious; a well-built small control. KEEP.

## 33/37 opal-portal-auth-throttle — NOT RULED (flagged, not assumed)
Andrew ruled 30/31/32/34/35/36/37 and did not name 33. CTO rec (NOT a ruling): same shape as 32
-- login-throttle counters for opalinvest-auth-handler, empty because nobody is currently
throttled; live auth-surface mechanism, KEEP. Awaiting his word.

## 34/37 opal-pm-snapshots — INVESTIGATED: NEVER ADOPTED (not ephemeral). Delete-candidate.
**The ask:** same investigation as 32.
**Answer, and the discriminator is clean:** key snapshot_id HASH, **TTL DISABLED**, 0 items,
sole env owner opal-pm-snapshot-handler. TTL disabled + zero rows means the rows are NOT
expiring -- they were **never written**. Contrast card 32 where TTL-enabled emptiness is by
design. So: built, wired to a live handler, never used. Its S3 twin (the handler also writes
opal-data-pm) carries the real snapshots. Delete-candidate, gated on the handler's code path
(deleting the table under a live handler creates errors -- C-13 ordering: producer first).

## 35/36/37 opal-firms + opal-offices + opal-invitations — ANDREW'S INCLINATION CONFIRMED,
## AND IT CORRECTS THE CTO'S OWN PRIOR LEAN
**Verbatim:** "the cards for 35 36 37 i do not know what these are, my inclination is they are
unused resources."
**CTO's prior card said the opposite** -- I wrote they were "likely load-bearing for auth" (the
org structure user rows point at). **MEASURED, AND I WAS WRONG:**
- opal-firms holds ONE fictional firm: firmSlug "smith-wealth" / "Smith Wealth Management",
  enabledPages [model-portfolios, benchmarks, peers, macro, clients].
- opal-offices holds ONE fictional office: "Boston Office", 123 State St, FIRM#smith-wealth.
- opal-invitations is EMPTY (scan returns []).
- **The real users do NOT reference them:** opal-users-v2 rows carry firmId "49financial" and
  "opal-capital" -- neither appears in opal-firms. The join does not resolve.
These are an unused org-structure SCAFFOLD populated with sample data, and they are the
estate's ONLY PROVISIONED-billing tables (paying reserved capacity for 3 rows total).
Delete-candidates + a billing-mode fix if any are kept. **The instrument that settled it was
reading the CONTENTS (C-14 applied to a table): the row count said 'small', the enabledPages
list said 'plausible', and only the actual firmSlug values said 'fictional'.**
