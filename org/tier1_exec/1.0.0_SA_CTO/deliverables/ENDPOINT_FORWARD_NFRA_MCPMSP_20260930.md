# ENDPOINT (step 2, /endpoint --forward) -- NFRA_MCPMSP, the Opal MSP Analyst

**Author:** 1.0.0_SA_CTO~O (site Z), 2026-09-30 ~04:3xZ. **Limb:** L2 (CTO only).
**Input:** `docs/briefs/nfra-mcpmsp-msp-analyst-brief-20260930.md` @77ddde1d13 (13,475 bytes; 4.0.0_SA_CRO~O, 04:15Z;
no `generated` line). **Andrew's record:** `org/tier1_exec/4.0.0_SA_CRO~O/deliverables/ANDREW_DIRECT_20260930_0315Z_MSP_ANALYST_CHANNEL_PILOT_FEDERATED_PROD_BOT_SENDER_DOMAIN_ALLOWLIST.md`
through @6cc12c2e06.

**LANDING STATE: NOT YET LANDED in a PRD.** No PRD exists. This block belongs verbatim under the section
`ENDPOINT (step 2, /endpoint --forward)` of `org/missions/D6/NFRA/NFRA_MCPMSP/prd/NFRA_MCPMSP_PRD.md`, written at L4
once Andrew confirms the DONE WHEN lines (his 2026-09-03 word: "i will confirm CTO's 'DONE WHEN' from their /endpoint
--forward") and the project is registered (L3). The directive home D6 is this seat's proposal at L3, not yet an act.

`FWD-n` ids are permanent: a new outcome takes the next unused number, a retired one leaves its number vacant, and no
list is ever renumbered.

---

## Outcomes

```
  FWD-1  An Inflection advisor asks the Opal Analyst a question in Teams and gets the answer from Inflection's own data
         DONE WHEN  EXERCISED -- one live conversation, read end to end
         ACCEPT     a named Inflection advisor asks a real question in a one-to-one Teams chat and gets an answer in
                    that chat; the answer matches what the Opal portal shows Inflection for the same thing and says how
                    current the data is; every step on the way is the real one, with no stand-in data and no faked
                    sign-in
         SOURCE     brief O1 (candidate thread); Part III bullet 1

  FWD-2  A Cottonwood advisor does the same, and neither firm can see the other's clients
         DONE WHEN  EXERCISED -- one live conversation per firm, plus one cross-firm attempt each way
         ACCEPT     a Cottonwood advisor gets an answer from Cottonwood's figures; when an advisor at either firm asks
                    about the other firm's clients they learn nothing about them, and Opal can show the refusal came
                    from the access controls rather than from the Analyst choosing not to answer; bringing Cottonwood
                    on took setting it up, not building a second system
         SOURCE     brief O2; Part III bullets 2 and 5

  FWD-3  A message from anyone outside the four allowed email domains gets no reply, and Opal can see that they tried
         DONE WHEN  EXERCISED -- a real refused message found afterwards in Opal's record
         ACCEPT     a message from an address outside opalinvest.com, 49financial.com, inflectionwealth.com and
                    cottonwoodmail.com gets no answer at all; a message using an allowed domain but coming from an
                    organization Opal does not recognize is treated the same; an Opal operator can later find each
                    attempt with who sent it and when
         SOURCE     brief O3; Part III bullet 3

  FWD-4  An advisor at a partner firm who has no access yet is turned away, and one Opal approval lets them in
         DONE WHEN  EXERCISED -- one advisor taken from refused to answered
         ACCEPT     an advisor at an allowed firm with no access writes in, gets no answer, and appears in Opal's list of
                    people who were turned away; after one Opal approval their next question is answered; the first
                    time anyone from a firm writes in, that same approval is how Opal comes to recognize the firm, with
                    no looking it up anywhere else
         SOURCE     brief O4

  FWD-5  Opal can replay any conversation: what was asked, what the Analyst looked at, what it was allowed or refused
         DONE WHEN  EXERCISED -- one past conversation reconstructed from the record alone
         ACCEPT     for a conversation picked after the fact, an Opal operator can show what the advisor asked, what the
                    Analyst looked up, what it was allowed and refused, and what it answered, without asking the advisor
         SOURCE     brief O5; Part III bullet 4

  FWD-6  Every day, a sample of the Analyst's answers is checked against the figures Opal publishes
         DONE WHEN  EXERCISED -- one day's check read, with its results
         ACCEPT     on a normal day, a sample of that day's answers is compared with the figures the portal shows, by
                    someone other than the Analyst, and any answer that does not match is named with the reason
         SOURCE     brief O6

  FWD-7  Andrew can read one page a day per firm: what was asked, what was turned away, what it cost
         DONE WHEN  EXERCISED -- Andrew has read one day's pages
         ACCEPT     for each live firm there is a daily page Andrew can open that says what advisors asked, who was
                    turned away, and what that firm's use cost that day
         SOURCE     brief O7

  FWD-8  Opal can switch off one firm without touching the others, and each firm's spending is separate and capped
         DONE WHEN  EXERCISED -- one firm switched off and back on while the other keeps working
         ACCEPT     when an Opal operator switches one firm off, its advisors stop getting answers while the other
                    firm's advisors carry on; each firm's spending shows on its own and stops at the limit set for that
                    firm
         SOURCE     brief O8; Part III bullet 6

  FWD-9  Partner advisors reach the Analyst through an Opal app their firm's IT has allowed, with no window kept open
         DONE WHEN  EXERCISED -- one partner advisor served through the app
         ACCEPT     an advisor at a partner firm talks to the Analyst through the Opal app their firm allowed; their
                    questions are answered whether or not anyone at Opal has a session running, and one question going
                    wrong does not stop the next one from being answered
         SOURCE     brief O9

  FWD-10 A partner's own administrator gives their advisors access, but never beyond the limit Opal set for the firm
         DONE WHEN  EXERCISED -- one grant made by a partner administrator, and one over-the-limit attempt refused
         ACCEPT     a partner's administrator gives an advisor access and that advisor then gets answers; when the
                    administrator tries to give more than Opal allowed that firm, it does not take effect
         SOURCE     brief O10

  FWD-11 No advisor at a new firm is served until Andrew has said the firm may go live and the checks are already running
         DONE WHEN  EXERCISED -- one firm brought live this way
         ACCEPT     an advisor at a newly added firm gets no answer until Andrew has approved that firm, and by the time
                    the first answer goes out, replay, the daily check and the daily page already cover that firm
         SOURCE     brief O11
```

---

## What is NOT settled here (carried to L4, owner named)

| Open item | Brief | Owner |
|---|---|---|
| Which firm's data an Opal staff member or a 49 Financial advisor reads under (49F has two live buckets) | Part VII | 1.0.0_SA_CTO~O at L4, a design fork (CRO pattern research first) |
| Who at Opal approves an entry in the turned-away list (FWD-4) | Part VII | 1.0.0_SA_CTO~O at L4 |
| Where the turned-away log lives and what each entry carries (FWD-3, FWD-4) | Part VII | 1.0.0_SA_CTO~O at L4 |
| Which published data the FWD-1 question reads | Part VII | 1.0.0_SA_CTO~O at L4; proposal: Inflection's model-portfolio figures the portal already serves (`platinum/mdpf/inflection/`) |
| The gateway audit's coverage of the new tool (row NFRA_OPALAI-Z-W2-S2) | Part VII | the L5 decomp (2.0.0_SA_COO) |

## Reachability: what the fabric cannot finish by working

**Reachable by working: 6 of 11** (FWD-3, FWD-5, FWD-6, FWD-7, FWD-8 and FWD-10 are buildable and testable inside
Opal once a firm is live). **Blocked on an act nobody in the fabric can perform: 5.**

- **FWD-1 and FWD-2 need each partner's IT to allow chats with outside organizations**, and need a named advisor at each
  firm. Both are external; the IT contacts are not yet identified (brief Part V; Andrew: "easy enough to figure out").
- **FWD-1 also needs Andrew's word to bring Inflection live** (FWD-11; the identity spine: "a new firm is his word").
- **FWD-9 needs each partner's IT to allow the Opal app** in their Teams admin center.
- **FWD-4's first live case needs a real partner advisor to write in.**

**Unverified and load-bearing for FWD-1:** whether Opal's Teams reader can see cross-organization one-to-one chats at
all (brief Part V). If it cannot, the pilot channel fails before any build matters, so it is the first thing round 1
must prove.

## Provenance

- **READ:** the brief in full (199 lines); Andrew's record sections 1-10 as quoted in the brief and read directly
  (section 10 at @6cc12c2e06); the primer (this seat's own, @9dc713f359).
- **NOT READ:** the task-order register (no NFRA_MCPMSP orders exist, and Phase 0 must not blend in-flight work);
  sibling projects' task orders (NFRA_OPALAI, NFRA_MCPORTAL, NFRA_OPLGTW); any project JSON; the gateway code the brief
  cites (brief Part IV is taken as the CRO's measurement, not re-measured here).
