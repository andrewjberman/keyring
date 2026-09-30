# NFRA_MCPMSP -- the Opal MSP Analyst: one Opal-hosted Teams agent serving partner firms (L1 brief)

**Author:** 4.0.0_SA_CRO~O (site Z), 2026-09-30 ~04:15Z. **Mode:** NEW (nothing of this project is built).
**Consumer:** `/endpoint --forward` at L2 (1.0.0_SA_CTO). Cite sections by their numbers (`O3`, `II.2`, `IV.4`).
**Grounding (Andrew's words, verbatim, sections 1-10):**
`org/tier1_exec/4.0.0_SA_CRO~O/deliverables/ANDREW_DIRECT_20260930_0315Z_MSP_ANALYST_CHANNEL_PILOT_FEDERATED_PROD_BOT_SENDER_DOMAIN_ALLOWLIST.md`
(last section at @6cc12c2e06). **Background:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/PRIMER_MSP_ANALYST_FOR_CRO_O_20260930.md`
(@9dc713f359). Where this brief and the record differ, the record's quotes win.

---

## PART I -- THE OUTCOME TERRITORY

### O1 -- CANDIDATE THREAD: an Inflection advisor asks the Opal Analyst a question in Teams and gets an answer from Inflection's data
One firm (Inflection), one advisor with a grant, one 1:1 federated Teams chat with the Opal-owned "Opal Analyst"
user (pilot channel, record s.2), one question about data Opal already serves for Inflection. The answer comes back
in the same chat, carries its data vintage, and was read under Inflection's firm scope only. This is the journey
round 1 builds end to end: advisor's Teams -> Opal Analyst -> the one gateway -> Inflection's firm role -> Inflection
data -> answer in the thread. Every other outcome enriches it.

### O2 -- A Cottonwood advisor does the same, and cannot reach Inflection's data (nor the reverse)
Adding the second firm is a row of configuration on the same server and the same agent, not a second server (record
s.7). The isolation holds on AWS: each request runs under the asking firm's own role, and the server's own identity
reads no firm data (record s.8). An advisor of one firm who asks about another firm's data is refused.

### O3 -- A sender outside the allowed domains and tenants gets no reply, and an Opal operator can see that they tried
Allowed sender domains: `opalinvest.com`, `49financial.com`, `inflectionwealth.com`, `cottonwoodmail.com` (record
s.2). The check is on the sender's domain AND, where the message surfaces one, its tenant ID (record s.6). A refused
message gets no response and leaves a log entry (record s.5). The check holds at the gateway as well as at the agent
(record s.6).

### O4 -- An Opal operator turns a refused advisor into a granted one from the refusal log
An advisor from an allowed firm with no grant is refused and logged with their tenant ID and user ID; the log is the
onboarding queue, and one approval turns an entry into a grant (record s.9). The same act learns each firm's tenant ID
the first time one of its people writes in, with no outside lookup (record s.10, card 3). Pilot grants are
Opal-administered per advisor (record s.9).

### O5 -- An Opal operator replays any conversation: what was asked, which tools ran, what the gateway allowed or refused
Every run's transcript, tool calls and gateway audit, tagged by firm and advisor, stored on Opal's side (record s.10,
card 2). Replay is the supervision surface; a live tail is not required (same card).

### O6 -- The CVO grades a daily sample of the Analyst's answers against the data Opal serves
Part of the go-live bar (record s.10, cards 2 and 6).

### O7 -- Andrew reads a daily per-firm report: what was asked, what was refused, what it cost
Part of the go-live bar (record s.10, card 2); spend is per firm because each firm has its own key (O8).

### O8 -- An Opal operator stops one firm without touching the others, and sees and caps each firm's spend
Each firm has its own API key with its own spend cap, held in AWS Secrets Manager "with a clear structure" (record
s.10, card 4). Disabling one firm's key or role stops that firm alone.

### O9 -- A partner advisor reaches the Analyst through the production channel: one Opal multi-tenant Teams bot
Production channel is option 3, a multi-tenant bot whose messages carry a Microsoft-signed tenant ID and user ID
(record s.1-s.2). The partner's IT allows the app in their Teams admin center. Production runs a fresh background
session per message (record s.10, card 2).

### O10 -- A partner's own admin assigns access for their advisors, within a ceiling Opal sets for the firm
Production grants model (record s.9, option C).

### O11 -- Andrew brings a new partner firm live on his word, and it passes the same bar before its first advisor is served
Onboarding a firm stays Andrew's word (record s.10, card 6; also `infra/logic/05_IDENTITY_SPINE.md` line 41, "a new
firm is his word"). The bar is O5 + O6 + O7 in place for that firm. No partner-facing SLA during the pilot (card 6).

---

## PART II -- WHERE THE BOUNDARY SITS

### II.1 -- This project OWNS
- the tenant-to-firm router and the sender allowlist (domain + tenant ID), with the refusal log (O3, O4);
- the per-firm AWS role assumed per request, and the one server's own identity holding no firm read (O2);
- per-firm API keys and their Secrets Manager structure (O8);
- the agent harness for partner traffic: the supervised pilot session and the production background session per
  message (O1, O9);
- the replay store, the daily per-firm report, and the graded-sample feed to the CVO (O5-O7);
- the pilot federated-chat channel and the production multi-tenant bot (O1, O9);
- the partner-admin grant ceiling as it applies to partner advisors (O10).

### II.2 -- This project RELIES ON, and does not own
- **The Opal gateway** (`infra/aws/ec2/opal-gateway/`): one server, extended rather than duplicated (record s.7).
  Its scoping modules are shared with the internal Analyst; changes land in them, not in a fork.
- **NFRA_OPALAI** (D6): the internal Opal Analyst (runtime under the `Opal_Agent` account, the `/bbg-teams-assist`
  serve loop). NFRA_MCPMSP serves partner firms; OPALAI serves Opal staff. Shared harness pieces are reused, not
  re-owned.
- **NFRA_MCPORTAL** (D6): the Entitlements surface and the grant handlers (`app/admin_grants.py`). O10 uses it; this
  project does not rebuild it.
- **NFRA_OPLGTW** (D9): the gateway's prior project home. Named so the decomp does not re-open its scope.
- **Firm data and its pipelines**: `opal-data-inf`, `opal-data-cot` (current buckets for now, record s.10 card 5). The
  successor buckets arrive through their own LGIC migration projects (R19), never as a rider here.
- **The Teams to portal UI graduation** (primer s.4): out of scope. The router, roles, grants, audit and console are
  built so a portal chat panel could call them later; the panel is not this project's.

### II.3 -- Directive home
Not decided here. Candidate: D6 "Opal AI" (holds NFRA_OPALAI and NFRA_MCPORTAL). Registration is the CTO's act (L3).

---

## PART III -- THE QUALITATIVE BAR

- An Inflection advisor gets an answer in Teams that they would otherwise have asked an Opal person for, and it
  carries the date of the data it came from.
- No advisor ever reads another firm's data, and a scoping bug surfaces as an AWS refusal, not as a leak.
- A stranger's message is never answered, and the attempt is visible to Opal afterwards.
- Opal can answer "what did the Analyst tell this advisor last Tuesday, and from what data" from the record alone,
  without asking the advisor.
- Bringing on the next firm is a configuration act plus Andrew's word, not a build.
- One firm's outage, runaway spend or revoked access leaves every other firm working.

---

## PART IV -- THE SUBSTRATE (findings, each with what was measured)

### IV.1 -- The gateway already binds a read to the Teams message's sender, by tenant ID and user ID
Measured: `infra/aws/ec2/opal-gateway/app/asker_scope.py` `resolve_asker` / `resolve_asker_message` (lines 151-167)
resolve the asker from a cited Teams message; a principal is `make_principal(tid, oid)` (line 125-129). Grants key on
`POLICY#<tid>#<oid>` (`app/access_state.py`, per surprise row `NFRA_MCPORTAL-Z-W2-S1`). A partner advisor's tenant ID +
user ID fits this key shape unchanged.

### IV.2 -- The gateway today REFUSES every non-Opal tenant, and has no tenant-to-firm registry
Measured: `asker_scope.py` docstring lines 62-65, verbatim: "Opal's own tenant (context.tenant_authorized) is
opal-internal, any other tenant is refused `asker_tenant_denied` before a catalog lookup. There is no tenant-to-firm
registry, so no firm is ever returned." So O1 needs the router this project owns (II.1); the refusal code path that
O3 needs already exists for the non-Opal case.

### IV.3 -- Group chats are scoped to the intersection of every human member
Measured: `asker_scope.py` lines 70-73: a chat that is not 1:1 is refused if any member fails tenant, profile or query
checks. A chat mixing an Opal person and a partner advisor is therefore served at the narrower of the two. O1 names a
1:1 chat deliberately.

### IV.4 -- Firm identity and data homes exist and are recorded
Measured: `infra/logic/05_IDENTITY_SPINE.md` lines 67-68: `inflection` -> `opal-data-inf` (four tiers, LIVE; the
router's target), tenant `F-INF`; `cottonwood` -> `opal-data-cot` (LIVE), `F-COT`; no `opal-data-inflection` or
`opal-data-cottonwood` exists. `49financial` has two live buckets (`opal-data-bd`, `opal-data-49financial`, line 21).

### IV.5 -- Secrets have a naming grammar in the estate's builders
Measured: `lib/opal_naming.py` grades `SECRET` names segment by segment (lines 588-589, `_OTHER_GRAMMAR` "S" at line
1064); `infra/logic/registry/resources.json` holds SECRET rows. So "a clear structure in AWS Secrets Manager" (record
s.10) has a builder to come from; per CLAUDE.md rule 30 the names are builder output, never hand-typed.

### IV.6 -- The internal Analyst is already a Claude Code harness, but interactive and crash-fragile
From the primer s.2 (measured by 1.0.0_SA_CTO~O 2026-09-29/30, not re-measured here): `launcher.ps1` starts one
interactive `claude.exe` as `Opal_Agent`; one crash takes it down; it polls one Opal user in Opal's tenant; it cannot
commit logs. This is the pilot shape (O1) and the reason production runs a background session per message (O9).

---

## PART V -- WHAT MUST BE TRUE, WITHOUT SCOPING IT NOW (named, not sequenced)

- Whether Opal's Teams reader can see federated (cross-organization) 1:1 chats at all. UNVERIFIED; O1 depends on it.
- Whether Inflection's and Cottonwood's Teams allow chats with outside organizations. UNKNOWN; their IT contacts are
  not yet identified (Andrew: "easy enough to figure out", record s.2).
- A registry row per firm for the tenant-to-firm router, and per-firm AWS roles, named by the LGIC builders.
- Per-firm Anthropic API keys with spend caps, stored under the builder-named Secrets Manager structure.
- A replay store on Opal's side, and an agent-side record that the internal Analyst cannot write today (IV.6).
- For O9: an Opal-owned multi-tenant Entra app + Teams app package, and each partner's admin allowing it.
- For O10: the Entitlements surface accepting partner-tenant principals within a firm ceiling.
- Andrew's word to bring each firm live (O11).

---

## PART VI -- STATUS (NOT OUTCOME-BEARING; measured 2026-09-30 ~04:10Z)

- No `NFRA_MCPMSP` folder, PRD or registry row exists (`org/missions/D6/NFRA/NFRA_MCPMSP`: absent).
- Gateway app last changed at `1243bad923` (2026-09-29 14:58 ET, `git log -1 -- infra/aws/ec2/opal-gateway/app/`).
- The record commits (@e62c14116d .. @6cc12c2e06) are LOCAL on CLOUD; origin/CLOUD was `fd3b3b7bf2` at 03:4xZ and had
  diverged from local.

---

## PART VII -- WHAT THIS BRIEF DOES NOT CLAIM

- **Opal staff and 49 Financial senders.** `opalinvest.com` and `49financial.com` are allowed sender domains (record
  s.2), but which firm scope an Opal staff member or a 49F advisor reads under is NOT decided. 49F's data sits in two
  buckets (IV.4). Named as open, not answered.
- **Who at Opal approves an onboarding-queue entry** (O4). Not decided.
- **Where the refusal log lives and what each entry carries.** Not decided (record s.5).
- **Which data the pilot question reads.** O1 says "data Opal already serves for Inflection"; which served surface is
  the candidate is left to L2.
- **The gateway's audit covering the new tool** (`asker_scope.py` lines 55-59 note an `_ARGS_ALLOWLIST` gap, row
  `NFRA_OPALAI-Z-W2-S2`). Not re-measured.
- **Nothing on the gateway's live deployment** (EC2, release, tool count) was re-measured; primer figures are cited
  as the primer's.
- **No Microsoft or vendor endpoint was called** in writing this brief; the domain-to-tenant lookup is not authorized
  and not needed (record s.10, card 3).
- **No numbers are set** for spend caps, sample sizes, report timing or latency.

---

## REFS TO CARRY

```
  BRIEF PATH        docs/briefs/nfra-mcpmsp-msp-analyst-brief-20260930.md
  PROJECT           NFRA_MCPMSP (Andrew's code, record s.10); not yet registered -- L3 is the CTO's
  EXISTING PRD      NONE
  SIBLING PROJECTS  NFRA_OPALAI (D6), NFRA_MCPORTAL (D6), NFRA_OPLGTW (D9); LGIC R19 bucket migrations
  PRIOR ART         infra/aws/ec2/opal-gateway/app/{asker_scope,identity_scope,access_state,admin_grants,audit}.py;
                    infra/logic/05_IDENTITY_SPINE.md; lib/opal_naming.py (SECRET grammar); primer s.2-s.4
  ANDREW RECORD     org/tier1_exec/4.0.0_SA_CRO~O/deliverables/ANDREW_DIRECT_20260930_0315Z_MSP_ANALYST_CHANNEL_PILOT_FEDERATED_PROD_BOT_SENDER_DOMAIN_ALLOWLIST.md
  MEASURED AT       2026-09-30 ~04:10Z (Part IV lines, Part VI)
```
