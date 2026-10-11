# Andrew-direct 2026-10-11 ~18:1xZ -- four questions at the 1.0.0_SA_CTO terminal (laptop)

VERBATIM: "Everything looks good here, just a couple questions. 1.) How does the sequencing of ADVI_FRMBKT and MDPF_CANON work,
considering that we want to be retiring some older buckets but bringing in new firm buckets, while also reorganzing some of these
pathways? We need to make sure that sequencing/dependency order does not cause breaks or is otherwise illogical. Also, I recommend
the CTO agents working on these projects to be employing /legacy-transform to be sure they do not miss any adapters or otherwise
misunderstand true current state. 2.) I Brought CVO online on this device (laptop, aka "cloud-local"), you should instruct them to
proceed as needed to unblock work on here. 3.) Do we need to bring COO~C online or any other agents to be working on this device?
4.) I want to understand if Dell1 and the haiku worker, sonnet COO/MSTR, and opus CTO/CVO/CRO strategy is working. I want to
compare the work on the Dell1 Box to the Dell2 box and gauge if this has been proceeding effectivel."

## 1. FIRMBKTS / CANON sequencing

Relayed verbatim to `1.0.0_SA_CTO~DELL1` through `0.0.0_AB_MSTR` at 18:1xZ with the instruction: run `/legacy-transform` on both
projects before the next cutover or retirement act; answer with the cross-project chain. This seat's own read of both PRDs and
latest rounds: section 5 (addendum, same hour).

## 2. CVO online on the laptop

`3.0.0_SA_CVO` (PID 19356) live here 18:0xZ. Instructed (msg to the CVO, 18:1xZ): NFRA_CTLPLN L8 channel compile (155
OBSERVATION rows) + the rounds 6-7 slug; re-sign MDPF_CANON v2.10's ratified half (both halves read "text CHANGED since signed",
ENDPOINT hash current -- a formality); NFRA_CTLPLN's half is SIGNED current, nothing owed there. dell2's compiles stay with dell2
until MSTR confirms whether a second `3.0.0_SA_CVO` session is live there (the base serial committed 83 times from dell2 today).
18:1xZ: MSTR~DELL2 measured YES (one dell2 session since 02:25Z, PIDs 28244/15564; it signed NFRA_OPSWKF's half today).
CTO~DELL2 (msg 5536) asked that the newer session take a lane. RULED: the laptop session re-registers as `3.0.0_SA_CVO~L`;
dell2 keeps the base string and every signature made under it; `.tools/prd_signoff_lib.py:53` strips a lane before
`permitted_signer`, so `~L` may sign the laptop's halves. Measured: the laptop session had committed and signed nothing.

## 3. COO~C or other seats on the laptop

Recommendation in the reply: YES to one COO (`2.0.0_SA_COO~C`) for NFRA_CTLPLN's E1-E8 enrichment in one issuance; NO other seat
(NFRA_SPMOVE stays parked on Andrew's placement; the CRO is already live for DSGN walks; no CloudOps needed beyond ~ANL/~FBL).
Seating waits on Andrew's word (usage-limit pacing is his lever).

## 4. Model policy read (dell1 treatment vs dell2 control), measured from origin/CLOUD commits since the policy landed
(2026-10-10T23:40Z -> 18:0xZ; 4,316 commits read; commits attributed to a box by the project code in the subject)

| signal | dell1 (haiku workers, sonnet COO/MSTR) | dell2 (sonnet workers, sonnet COO/MSTR) |
|---|---|---|
| commits naming the box's projects | 1,045 | 1,229 |
| worker commits | 256 | 286 |
| COO commits | 518 | 605 |
| worker commits that are AMENDMENTS (rework) | 41 (16.0%) | 52 (18.2%) |
| all AMENDMENT commits | 126 (12.1%) | 216 (17.6%) |
| SUPERSEDED orders | 9 | 5 |
| "repair" commits | 12 | 31 |
| surprise rows filed (subject mentions) | 69 | 19 |
| round analyses / MAY-CLOSE | 57 / 29 | 53 / 10 |
| task-order files created today: complete / pending / other | 132: 86 / 25 / 21 | 149: 140 / 2 / 7 |

Reading: throughput is at parity (worker commits within 11%); rework is not worse on dell1 (amendment share 16% vs 18%, repairs
12 vs 31); dell1 closes rounds at a higher rate (29 MAY-CLOSE vs 10) and files more surprise rows (69 vs 19 -- more defects found,
or more diligence; the subjects do not say which). dell2's order completion is higher today (94% vs 65%) because dell1 cut round
4 of FIRMBKTS and round 95 of RESAPP late in the day (25 pending). NOT measured: cost/usage (no token record reaches git; both
boxes hit usage limits overnight before the policy); the served worker model on dell1 (Claude Code 2.1.293 does not persist
subagent transcripts; the launch flags read 0 mismatch). The project mix differs (dell1: data pipelines + Security Analysis;
dell2: Investor Reporting stack), so this is a parity read, not a controlled trial.

What would make it a measurement: (a) dell1 upgraded to Claude Code >= 2.1.296 at a drain gap so `model-census.py` reads the
served model; (b) each MSTR reports its box's usage-limit hit times for 10-10 and 10-11 (the cost axis); (c) the same read
repeated on 10-13 after one full working day without a hold.

## 5. Addendum (18:2xZ) -- FIRMBKTS / CANON: the chain as read from both PRDs, and the CTO's sequencing ruling

Read (both PRDs, latest rounds, decompositions, `org/missions/D8/`): FIRMBKTS PRD v1.3 orders per firm ledger -> grants -> copy
-> compare -> router flip (never-widen) -> read-back -> old bucket untouched through a 45-day quiet window -> delete on Andrew's
word (`PRD:198-209`, `:160`); 49 Financial first. Round 4 window acts run Monday 2026-10-12 from ~06:30Z (acts 2, 3, 4b, 4c), the
flip ~13:45Z+ (f-11 dell1 leg, f-19 laptop leg, g-30 flip commit, g-31 eight re-pins). F8 Inflection waits on Andrew's FWD-7/8
rulings; F9 Cottonwood not cut; F12 retirements not started (no clock running). CANON PRD v2.10: M1 census done, M2 per-firm gold
already in `opal-data-49financial` (42 partitions), M8 bronze new-home PASS 10-11, M4 repoints in progress (CN-e-1 in round 5),
M5 publisher last among readers, M9 firm route/slice + M10 runner + M11/M12 retirements not started; the two trees CANON
retires (`opal-data-assets/gold/mdpf_revamp/`, `opal-data-assets/portal/gold/mdpf/`) are NOT the legacy firm buckets, so
CANON's retirement never depends on FIRMBKTS retiring `opal-data-bd/-inf/-cot`. CANON waits on FIRMBKTS per firm (`PRD:50`,
`:196`, `:351`, `:371`, `:451`).

**The chain, in order (break if inverted):**
1. FIRMBKTS acts 2/3/4b/4c (Mon ~06:30Z). Inverted: a producer writes the legacy home after the move.
2. MDPF gold fire Mon 13:30Z (CANON FWD-1's own read) into firm buckets whose policy acts 3b/3c already rewrote (4 -> 29
   statements). Break: a later FIRMBKTS bucket-policy apply that drops the scope-admitted gold-writer path -> AccessDenied.
3. FIRMBKTS act 4 flip (~13:45Z+) regenerates `data/mdpf/config/bronze_homes.json` and `firm-config.mjs` (g-30:66). Break:
   CANON's bronze reader/runner config mid-change -> the ~12:52Z dispatch reads a changed home.
4. FIRMBKTS grant `mdpf/{firm}/platinum/*` on 49Financial (PRD:156 says it is generated from consumers' declared prefixes; NOT
   found in the FIRMBKTS ledger or round-4 decomposition -- act 3b's OAI Allow is advi classes only). Skipped: M9's first
   slice read through CloudFront is 403.
5. CANON M9 (49 Financial) AFTER act 4 and its first-hour read. Before: M9 edits the same shared-advisor-router, guard and
   CloudFront behaviours the flip is about to swap -- the flip overwrites M9's mapping or M9 is proven against a router that
   is about to change.
6. M9 Inflection / Cottonwood after F8 / F9 (Inflection blocked on Andrew's rulings).
7. M10 runner any time after M9's grants. 8. M5 publisher last, then M11/M12 on their own 45-day clock.
9. FIRMBKTS F12 retires `opal-data-bd` last; it still serves two transitional live rows (49F bronze pin, the IRPT directory).

**Unstated or disagreeing (named):** CANON `ROUND_ANALYSIS.round4.md:31` says FIRMBKTS "round 3 holds the 49 Financial cutover"
-- wrong, the flip is round 4 and has not run. Three wordings of one wait (`PRD:50` cutover; `:196` bucket serves + grants; `:371`
reports serving) -- F4 "buckets serve" and F7-F9 "router flip" are different events. Window-start rules differ (FIRMBKTS
`PRD:160` after cutover; CANON `PRD:201`,`:304` once every reader is repointed). Both PRDs edit the shared router and guard with
no owner named; FIRMBKTS keeps a portal-auth WAF rider CANON's M9 apply may not name. **Joint census gap:** FIRMBKTS's censuses
(`deliverables/CENSUS.md`, `ledger/R3_ACT2_OUTSIDE_READERS_CENSUS.md` 464 hits / 5,868 files, 45 UNKNOWN sites; `PRODUCER_CENSUS.md`
14 writers) cover `data/black_diamond` and `infra/aws/lambda` for 49F advi prefixes; CANON's M1 covers its two trees, served key
and old bronze. No census counts MDPF readers of the legacy firm buckets -- unmeasured, not shown empty.

**Ruling (CTO, cluster lead; binds both projects, both on dell1):**
R1. The wait is the FLIP, not the bucket: CANON M9 for a firm runs only after FIRMBKTS's act-4 flip for that firm and its
    first-hour read; CANON amends `PRD:50/:196/:371` to one wording. M9 Inflection waits on F8 (Andrew's FWD-7/8), not on F4.
R2. Shared files have one owner until the flip lands: `shared-advisor-router`, the guard, the CloudFront behaviours,
    `bronze_homes.json`, `firm-config.mjs` and the portal-auth WAF rider are FIRMBKTS's write surface through act 4 + read-back;
    CANON touches none of them before that; after it, ownership passes per file by a line in FIRMBKTS's flip receipt.
R3. The `mdpf/{firm}/platinum/*` serving grant is a FIRMBKTS act (PRD:156) and is cut as a named cell before M9, not inferred.
R4. A joint reader census (MDPF readers of `opal-data-bd/-inf/-cot`, with denominator) is a precondition of FIRMBKTS F12's
    45-day clock for each legacy bucket; DEC-12 read logging is the instrument once the window counts, the static census the
    control. `/legacy-transform` on both products (Andrew's recommendation) is the method for it and for the 45 UNKNOWN sites.
R5. CANON `ROUND_ANALYSIS.round4.md:31` is corrected in round 5's analysis. Monday's acts 2/3/4b/4c and the 13:30Z fire are
    unchanged by this ruling.
