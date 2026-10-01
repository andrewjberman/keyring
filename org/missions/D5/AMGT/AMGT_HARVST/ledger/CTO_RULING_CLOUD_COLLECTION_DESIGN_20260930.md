# AMGT_HARVST -- CTO RULING on the cloud collection design, and ENDPOINT addendum proposal FWD-10 -- `1.0.0_SA_CTO~Z`, 2026-09-30 ~17:4xZ

**The word:** Andrew-direct ~17:2xZ, record
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260930_172xZ_HARVST_CLOUD_HEADFUL_NOPECHA_REST_API_LONG_LIVED_TOKENS_TO_CRO.md`
@`79bc898865`.
**The research:** `4.0.0_SA_CRO~Z`, `org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/HARVST_CLOUD_COLLECTION_DESIGN_20260930.md` @`9473d06426`
(msg 27298, read to EOF).
**The routing:** a DESIGN FORK, ruled by the driver the tick the research landed (/self-drive Step 1).

## 0. SUPERSEDING (~17:5xZ): Andrew answered the CRO's four decisions directly

His answers are recorded verbatim by `4.0.0_SA_CRO~Z` in `HARVST_CLOUD_COLLECTION_DESIGN_20260930.md`, "Andrew's answers" @`f5c3b0dbc7`.
The bot-ops study is `HARVST_BOT_OPS_STUDY_20260930.md` @`f5c3b0dbc7` (msg 27308, read to EOF, 5,499 B).
- **(1) Bright Data:** *"If we can assign our existing bright data residential IP to an EC2 box to do this, then great."*
  - The residential egress on an EC2 host is APPROVED, conditional on its being assignable.
  - This replaces s.2's "NOT adopted" and s.5 item 2.
- **(2) Web Unlocker:** *"I dont love that idea, i think we just need better bot ops ... the issue needs to be studied."*
  - NO Web Unlocker.
- **(3) Consolidation with ASTN:** *"This is a last resort."*
  - s.2's shared-token-store line stands as the only consolidation.
  - Moving ASTN's box is off the table unless nothing else works.
- **(4) Licensed feeds:** *"Absolutley not."*
  - s.5 item 3 is WITHDRAWN.
  - This seat's REC for licensed access is withdrawn with it.
- **Where the job runs:** *"all harvest ops "could" just be a job that runs on the sitez box ... I prefer a cloud solution of course, but
  local has more visibility. Maybe its a local job until it matures in process"*.

**The study's finding (measured on bbg): volume is not the cause.**
- Pacing is about one request per 20 s.
- Rejections are cold first requests, carrying a valid login (to 2027-09-11) and PerimeterX trust cookies that expired about four
  minutes after the 09-11 capture.
- Retrying into a challenge makes it worse.
- **The remedy is ordinary bot operations, with no solver:**
  - warm the session in a real browser on the same egress, then run the REST pulls inside the trust window;
  - stop at the first challenge;
  - ramp from a page load to an article read before any search.

**RULING (supersedes s.2 and s.3; s.4 FWD-10 stands with one line added):**

1. **Phase 1 is LOCAL, on the site Z box. "Until it matures" is read as: until a warm-then-pull run collects from each publication
   with no challenge.**
   - The harvester gains:
     - a warm-up step (a headed browser loads an ordinary page on the box's own connection, and fresh trust cookies go to the REST
       pulls);
     - stop-at-first-challenge (already v0.10-v0.11);
     - the page -> article -> search ramp.
   - The REST shapes do not change.
2. **Phase 2 is the cloud host:** the design's host, token keeper and orchestrator, on the existing Bright Data residential IP (his
   answer 1). It is built once phase 1 has matured, so that no cloud path runs beside a proven local one (CLAUDE.md NEVER
   shadow pipelines). The residential IP's assignability is read now, from the existing ASTN and BD box configuration, with no vendor
   call.
3. **Round-31 cells replace s.3:**

   | # | cell | risk |
   |---|---|---|
   | 1 | **Token store:** wsj and barrons bundles into Secrets; ft's bundle expiry measured (as before) | WORLD, pair |
   | 2 | **The warm-up and ramp in the harvester** (warm-up step, cookie hand-off, page -> article -> search ramp), with a planted stale-trust bundle showing the warm-up replaces the trust cookies | LOCAL |
   | 3 | **One bounded warm-then-pull trial per publication on the site Z box**, one name each, each attempt classed per v0.11, stop at first challenge. This is the study's next step. | WORLD, pair + R-21 |
   | 4 | **Residential-IP assignability read:** from the ASTN and BD boxes' configuration, whether the existing Bright Data residential egress can be bound to an EC2 host | LOCAL read |

3a. **(~18:3xZ) Re-cut after the CRO's live trial 1** (`4.0.0_SA_CRO~Z` @`ca0eab4933`, on Andrew's "Yes do it" at that terminal).
   - **FT cleared:** after warm-up, the FT REST calls returned 200 for 12 minutes.
   - **bbg, wsj and barrons refused the OUTSIDE client:**
     - bbg answered 403 from PerimeterX; wsj and barrons answered 401 from DataDome;
     - this held even with seconds-old trust cookies;
     - after those refusals, a plain reload was challenged 12 minutes later.
   - So scoring follows the CLIENT, not only the cookie. The CRO's trial 2 (REST in the tab, the navigation, a consistent client last)
     is scheduled after a cool-down.
   - **Cell 3 is WITHDRAWN.** The trial runs under Andrew's word at the CRO seat, and a second trial from a COO worker would duplicate
     it and re-poison the sessions.
   - **Cell 2's shape waits on trial 2:**
     - if REST in the tab passes, the warm-up and pulls run INSIDE the browser session;
     - if it does not, the cell is re-scoped at the round-31 analysis.
   - **Cells 1 and 4 stand.**

3b. **(~19:5xZ) Recorded: the CRO's trials 2-3b and the bot-ops playbook** (`4.0.0_SA_CRO~Z` @`7bcc258369`, msg 27351, on Andrew's
   word that COO~H "goes through the motions").
   - **The flag sits on the site Z box's IP.** It was degraded during the day by refused automated requests. By 19:4xZ even an
     anonymous fresh browser was challenged.
   - **HARD STOP:** no traffic to bbg, wsj or barrons from this box until the playbook's 05:00 ET first-light test. That test decides,
     per publisher, between REST in the tab and page parsing.
   - The batch-1 retry (the ab-3 path) does not run before first light.
   - Round 31's cells 1 (the token store) and 4 (the residential-IP read) send no publisher traffic and stand.
   - The playbook `org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/HARVST_BOT_OPS_PLAYBOOK_20260930.md` is COO~H's step list.

4. **FWD-10 (s.4) gains:** "the run may be the site Z box until the local job matures (Andrew ~17:4xZ); the cloud host is the end state."

**The acts only Andrew can do (s.5) are now one:** confirm FWD-10's DONE WHEN. The Bright Data word is given (conditional). Licensed
feeds are refused by him.

*The sections below are kept as the record of the pre-answer ruling.*

## 1. WHAT THE RESEARCH ESTABLISHED (as measured by the CRO)

1. **NopeCHA is NOT an all-in-one captcha solution.** This answers his question.
   - It documents none of the three challenges the publishers actually serve:
     - DataDome (wsj, barrons);
     - PerimeterX/HUMAN press-and-hold (bbg);
     - Cloudflare's managed challenge (ft).
   - It covers FT's login hCaptcha only. The repo already solves that one another way.
2. **Long-lived tokens are necessary but NOT sufficient.** bbg's token is valid to 2027-09-11, and its REST call was still challenged
   at 04:40Z today with no credentials entered.
   - The challenge follows the CLIENT (IP reputation, TLS fingerprint, rate), not the token.
   - Andrew's model is right: long-lived tokens plus REST shapes, no crawler. It lacks one piece: an egress the publishers' scoring
     accepts.
3. **Where the tokens are held today:**
   - bbg and ft are in AWS Secrets;
   - wsj and barrons are only in an encrypted file on this Windows box, so no cloud host can use them today.
4. **One cloud route already returns WSJ daily:** ASTN_WSJFT's transient EC2 through Bright Data Web Unlocker, 12-18 articles a day,
   today included.

## 2. RULING -- the design, and the pieces that need a vendor or spend act

**ADOPTED (the CRO's s.4 items 1, 2 and 5; Andrew's shape, built from existing parts):**
- **One harvester host.** A small or nano EC2 per his word. It is transient, started, run and stopped by an orchestrator Lambda, the
  ASTN and YCharts shape.
- **Per publication, a token keeper:**
  - probe the stored token with the publication's own `auth_check` (`contracts.json`);
  - if the token is valid, go straight to the REST pulls through the per-publication shapes;
  - only if it is invalid, re-sign in on the SAME host (Xvfb and Playwright, credentials from Secrets) and write the bundle back.
- **All five bundles live in AWS Secrets.** wsj and barrons leave the local encrypted file.
- **A pull moves to Lambda only where a measured probe shows that egress unchallenged.** That is his "ideally entirely on a lambda",
  held to a measurement.
- **Every challenge is recorded under `C-HV-TRUST-TOKEN` v0.11** (`bot_check` / `unclassified`, never expiry). The leg parks with the
  publisher named and never loops.
- Every new resource name and address is builder output (`lib/opal_naming`; CLAUDE.md rule 30).

**Egress and challenge-passing (the CRO's s.4 items 3-4): NOT adopted by this seat.**
- This is a vendor use (Bright Data residential egress and Web Unlocker) that no word of Andrew's names for HARVST. ASTN holding the
  account is availability, not authorization.
- It is listed for him as an ACT, with the risk the CRO states plainly (s.5): unlockers get past the publishers' controls, so Opal's
  paid subscriber accounts could be flagged or closed, and the practice likely conflicts with the publishers' terms.

**Consolidation with ASTN (the CRO's s.4 item 6): RULED.**
- The TOKEN STORE is one store now: Secrets, written by the HARVST token keeper and readable by ASTN.
- Moving ASTN's box onto the harvester host is ASTN's own migration, never a rider on HARVST.
- No second store and no parallel host is stood up for the same publisher (CLAUDE.md NEVER shadow pipelines).

**Licensed access (the CRO's s.5 and s.6.4):** Factiva/DNA, FT's content API and Bloomberg news are spend and contracts. They are listed
for Andrew as an ACT. This seat's REC is that licensed access is the durable route, because it removes the challenge problem instead of
fighting it.

## 3. WHAT IS CUT NOW, with no vendor word needed (publisher egress under R-21 @b390c36444)

These are routed to `2.0.0_SA_COO~H` for round 31. Round 30 is in flight and its spec is frozen.

| # | cell | risk |
|---|---|---|
| 1 | **Token store:** wsj and barrons bundles into Secrets (builder-named), plus ft's bundle expiry measured and recorded. The local file stays until the cloud keeper has proven a read. | WORLD, pair |
| 2 | **Egress probe:** from a Lambda and from a plain EC2 in the account, one `auth_check` and one REST listing per publication with the stored token. Each attempt is classed per v0.11. | WORLD (read-only egress, R-21) |
| 3 | **The harvester host and orchestrator Lambda** (Terraform via `safe-apply`, builder names, stop-after-run). The keeper and pulls run the existing `publishers.py` shapes. | WORLD, pair |

- Cell 2's output is the measurement that decides Lambda vs host per publication, and whether any publication runs clean WITHOUT a
  managed egress. It is the evidence Andrew's egress decision rests on.
- The schedule stays Andrew's (PRD s.2 boundary). The host runs on demand until he words a cadence.

## 4. ENDPOINT ADDENDUM -- PROPOSAL (the CTO's L2; Andrew confirms DONE WHEN)

```
  FWD-10 Collection runs in Opal's cloud from a stored long-lived token,
         over each publication's REST shape -- no crawler, no login page,
         no desktop
         DONE WHEN  EXERCISED -- one on-demand run on the cloud harvester (a
                    small EC2, or a Lambda where a probe measured that
                    publication unchallenged) starts from each publication's
                    token in AWS Secrets, pulls the validation security's
                    articles for all five publications through their REST
                    shapes, and signs in -- on the same host -- only for a
                    publication whose token its probe showed not to work;
                    the run record names, per publication, the token source,
                    the host, and each attempt's class
         ACCEPT     No collection depends on Andrew's desktop or on anyone
                    signing in by hand; a lapsed token is renewed in the
                    cloud and written back to Secrets.
         SOURCE     Andrew-direct 2026-09-30 ~17:2xZ: "the mechanism for
                    drawing news is not using a crawler or going through login
                    page, its rest api pulls through dedicated shapes per
                    publication, ideally running entirely on a lambda. I don't
                    mind having a dedicated small or nano ec2 that is tasked
                    with handling all of this"
```

**Stated dependency, not hidden:** "all five publications" is reachable only if cell 2 shows clean egress, or Andrew words a managed
egress, or a licensed route replaces the challenged pull. This FWD is not graded REALIZED on fewer.

## 5. ACTS ONLY ANDREW CAN DO (cited)

1. **Confirm FWD-10's DONE WHEN** [Rule 27 L2; `/open-calls` self-adjudication clause: "i will confirm CTO's DONE WHEN"].
2. **A per-use word for Bright Data egress and Web Unlocker on HARVST's pulls** [CLAUDE.md "NEVER call an external vendor API without
   Andrew's explicit per-use word"]. The CRO's s.5 risk to the subscriber accounts is his to accept.
3. **Licensed-access pricing requests** (Factiva/DNA, FT content API, Bloomberg news) [spend and contracts beyond his grants].
