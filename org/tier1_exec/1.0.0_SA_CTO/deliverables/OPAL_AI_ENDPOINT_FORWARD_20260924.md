# /endpoint --forward -- opal_ai V1: the Opal Analyst as a product, built in the workspace, running on its own

**Phase 0, greenfield.** Emitted 2026-09-24 ~20:1xZ by `1.0.0_SA_CTO~O`, which holds the program on Andrew-direct
(record `ANDREW_DIRECT_20260924_193xZ_OPAL_AI_CALLS_1_2_4_YES_ANALYST_SEPARATION.md` @489fbcd6e0, card 1).

**Inputs read, whole:**
- `docs/briefs/opal-ai-microproduct-repo-brief-20260923.md` (RCN-0014) @a47993af9c, 521 lines, author `4.0.0_SA_CRO~X`.
- `docs/briefs/opal-ai-gitops-split-brief-20260923.md` (RCN-0015) @40b964f616, 428 lines, author `4.0.0_SA_CRO~X`.
- Andrew's rulings since the briefs: cards 1, 2, 4 (@489fbcd6e0); card 3 direction (@45ce8406fc record); R1 and R2
  (@11881eb192), which settle the design in `OPAL_AI_RUNTIME_ISOLATION_DESIGN_20260924.md` @45ce8406fc.

**NOT READ, deliberately:** the task-order register and project JSONs. The stand-up assessment
(`OPAL_AI_STANDUP_ASSESSMENT_20260924.md` @30d6c89685) read some of them, and nothing here is drawn from those reads.

**The tag is `DONE WHEN`**: the bar an outcome must reach, never its current state. `FWD-n` ids are permanent. A new
outcome takes the next unused number, and a retired one leaves its number vacant. **No outcome is a wait.** Each one
names an act a seat can take on demand.

**Where this lands:** the ENDPOINT section of the program's PRD at L4. The program code and its directive are set at
L3 (section 3 below). **NOT YET LANDED in a PRD.**

---

## 1. The outcomes

  FWD-1  An Opal colleague asks the Opal Analyst a question in Teams about a figure Opal already
         shows, and gets the answer from the Analyst running in its own separate account
         DONE WHEN  EXERCISED -- one live exchange, traced from the colleague's message to the reply
         ACCEPT     a named colleague asks a real question; the reply gives the figure, its date,
                    where it came from and whose accounts it covers, and matches what the portal
                    shows for the same date; the Analyst that answered was the released copy
                    running on its own, and every step of the exchange was real, none simulated
         SOURCE     RCN-0014 Part I "the candidate thread"; RCN-0015 O6; design s.3 plane 2

  FWD-2  The Analyst notices every message sent to it and answers without anyone prodding it,
         including after it has sat idle for hours and including messages that carry pictures
         or pasted content
         DONE WHEN  EXERCISED -- messages sent at chosen times over a working day are all answered
         ACCEPT     a colleague sends messages after long quiet spells and one with a pasted image
                    or rich content; each is acknowledged and answered with no human stepping in;
                    a message it cannot read is answered with a plain statement that it could not
                    read it, never silence
         SOURCE     RCN-0014 O1 ("while the conversation is still live"); the watch blockers in the
                    Analyst's own log of 2026-09-24

  FWD-3  A colleague gets a routine answer while they are still in the conversation
         DONE WHEN  EXERCISED -- real exchanges timed stage by stage and compared with August
         ACCEPT     for a question about a figure Opal already serves, the colleague would not
                    have been quicker looking it up themselves; the timing shows where the time
                    went, and most of it went into answering, not into warming up
         SOURCE     RCN-0014 O1; Part III "Speed" and "Economy"; finding 3

  FWD-4  A colleague who does not know which system holds a fact is sent to the right place on
         the first try, and the questions the Analyst could not place come back as a list
         DONE WHEN  EXERCISED -- real questions asked cold by people who did not build it
         ACCEPT     a set of questions real colleagues asked, not questions written from the
                    catalogue's own descriptions, mostly lands on the right answer first time;
                    each question it could not place is listed with the reason
         SOURCE     RCN-0014 O2; finding 13; served by NFRA_MCPINDEX's completion

  FWD-5  A colleague gets the same answer whether they ask the Analyst in Teams or ask their own
         Claude directly
         DONE WHEN  EXERCISED -- the same questions asked both ways by one person
         ACCEPT     the figures, dates and refusals agree both ways, and a person refused
                    something one way is refused it the other way too
         SOURCE     RCN-0014 O3; Part VIII call 7

  FWD-6  Nobody can talk the Analyst out of its limits
         DONE WHEN  EXERCISED -- a colleague genuinely tries
         ACCEPT     urgency, seniority, or a message made to look like an instruction does not get
                    it to change anything, download from Bloomberg, contact an outside vendor
                    beyond Andrew's standing word, or widen what it will answer; each refusal gives
                    a reason the colleague can repeat
         SOURCE     RCN-0014 O4; Part III "Guardrails"

  FWD-7  The Analyst cannot reach the development workspace, Andrew's own identity, or the other
         agents, and it will not start if it ever could
         DONE WHEN  EXERCISED -- at every launch, and once deliberately broken
         ACCEPT     at launch the Analyst tries to open a workspace file and is refused, and it
                    carries no way to act as Andrew or to message the development agents; when
                    that separation is deliberately removed for a test, it refuses to start
         SOURCE     Andrew-direct 2026-09-24 card 3 and R1/R2; design s.3 plane 2 items 1-7

  FWD-8  Andrew admits a colleague, sets what they may ask about, and removes them again, and can
         explain any past answer after the fact
         DONE WHEN  EXERCISED -- one colleague admitted, used, narrowed and removed
         ACCEPT     each change takes effect without rebuilding or restarting anything; for any
                    past answer Andrew can see who asked, what was looked up and what data it
                    touched, without private figures sitting in that record
         SOURCE     RCN-0014 O5

  FWD-9  An engineering agent improves the Analyst or its data tools using the workspace's usual
         tools and checks, and the improvement reaches colleagues only through a release Andrew
         approved
         DONE WHEN  EXERCISED -- one real change followed from the edit to a colleague's answer
         ACCEPT     the change is checked by the same rules as any workspace change, it goes live
                    only when Andrew says so, and afterwards anyone can say which version the
                    Analyst is running and which version is approved
         SOURCE     Andrew-direct card 3 ("develop ... using the ajb_workspace tools"); RCN-0015 O2,
                    O7; design s.3 release flow

  FWD-10 Anyone who sets up the workspace fresh, on either machine, gets the Analyst's product code
         at the right version with one standard step, and nothing about it is quietly left out
         DONE WHEN  EXERCISED -- a fresh setup on each machine
         ACCEPT     the product code arrives at the version the workspace records; an empty or
                    missing copy is flagged loudly, never taken as fine; agents' work reports and
                    progress views count work done in it
         SOURCE     RCN-0015 O1, O4, O8, O10

  FWD-11 The data gateway is released from the product's own history with no loss of safety
         DONE WHEN  EXERCISED -- one real release of the gateway
         ACCEPT     a release refuses to go out with unsaved changes, the release record names
                    the product version actually running, and the gateway keeps its full history
                    so every older reference to it still leads somewhere
         SOURCE     RCN-0015 O5, O9; Part IV finding 8

  FWD-12 Adding a new kind of data for colleagues to ask about is one catalogue entry plus one
         tool, and a tool that has not been classified for safety cannot go live
         DONE WHEN  EXERCISED -- one new kind of data added; one unclassified tool refused
         ACCEPT     the new data is answerable after exactly those two additions; a deliberately
                    unclassified tool is stopped before it can reach anyone
         SOURCE     RCN-0014 O10; served by NFRA_MCPINDEX's completion

  FWD-13 The product can be picked up and checked on its own, without the workspace
         DONE WHEN  EXERCISED -- a copy taken alone passes its own checks
         ACCEPT     someone holding only the product repository can run its checks and they pass;
                    the checks also run automatically on every change to it
         SOURCE     RCN-0015 O3; Andrew-direct card 4 (CI yes)

---

## 2. Stated outside this endpoint (not promised by this program)

This is not a silent shrink. Each item below is a capability Andrew named, and it gets its own project when he starts it.

- **The template slice** (RCN-0014 O6, O7, O9; O8's playbook). Andrew's order: after "a proper V1, even V2". FWD-12
  keeps the one template property that must hold from V1 onward.
- **Client slices** (RCN-0014 O11, O12). They wait on a named first client, per his 2026-08-20 zero-partner ruling.
- **External agents hosted off this box.** The design names the shape, and nothing here builds it.
- **NFRA_OPLGTW's walkthrough grading.** It stays under his 2026-09-22 stop.

## 3. For L3 (not outcome-bearing)

- **Proposed code:** `NFRA_OPALAI`. It conforms to `^[A-Z]{4}_[A-Z0-9]{3,18}$`.
- **Proposed directive:** D6 "Opal AI". D6 has no ratified macro enum in `MACROS.yaml`. Registering there needs a
  Rule 24 record, a token census and Andrew's word to ratify D6 = [NFRA].
- **Proposed workstreams**, each with a disjoint write surface:
  - **W-REPO**: the submodule, gates, CI and fabric tooling (FWD-9, 10, 13);
  - **W-ANALYST**: the Teams exchange, the watch, speed, limits, the runtime account and the carve-out (FWD-1, 2, 3, 6,
    7, 8);
  - **W-GATEWAY**: the gateway move and its release path (FWD-5, 11).
- **Served by NFRA_MCPINDEX:** FWD-4 and FWD-12. MCPINDEX finishes as its own project and delivers into opal_ai.

## 4. Provenance

Every outcome's SOURCE line names the brief part, the finding or the ruling it comes from. No outcome is drawn from a
task order.
