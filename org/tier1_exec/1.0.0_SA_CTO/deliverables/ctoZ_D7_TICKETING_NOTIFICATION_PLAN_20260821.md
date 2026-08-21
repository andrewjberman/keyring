# D7 TICKETING -- THE THREE-SIDED NOTIFICATION PLAN (structure, not build)

**Author:** `1.0.0_SA_CTO~Z` - **Date:** 2026-08-21 ~04:5xZ - **Status:** PLAN FOR RATIFICATION. Nothing here is issued as a TO yet.
**Authority:** ANDREW-DIRECT 2026-08-21 ~04:5xZ at the CTO~Z terminal. Recorded VERBATIM in sec. 0 -- **the phrasing IS the ruling.**

---

## 0. THE ANDREW-DIRECT, VERBATIM

> *"internal only, and bring on COO~Z. the way this would be set up is that some group of people get an email based on the firm in question making the request. for now, its same group of people for every firm, but eventually it might make sense to split that which is why i declare it up front. I think the schema for that email is subject line with firm name incorporated somehow. then body text is some structured representation of the form submitted, i.e. who is it from, subject line they included, body text, and then some standard hyperlinked link that goes to the dashboard ticket center page with a CTA about clicking the link to go claim the ticket. i dont think we need follow up emails with tickets being accepted or completed, just the initial buzz, the rest is handled on the dashboard itself. in addition to this, we need to figure out the comparable structur for the teams thread and how the opal agent manages that process + how the opal agent writes on teams, it really needs to do better formatting, it has a tendency to just block a wall of text, sentences should be appropriately spaced out with empty returns between 2-3 sentence max paragraphs and 1 line key lines or hyperlinks (which should be properly linked to be clickable). I think the first thing to do is kind of plan what this looks like on three sides: email and teams for the internal ops, client-side input and experience/notification (should likely be covered both on dashboard and on their email, i.e. getting an email when their ticket is picked up and by who), and lastly infrastructural synthesis to make sure it all works reliably in tandem. let's get this plan structured."*

### 0a. WHAT THIS DISCHARGES IMMEDIATELY

| Item | Was | Now |
|---|---|---|
| **W-E DL audience** (the standing sovereign card) | OPEN -- internal / mixed / client-facing | **RULED: INTERNAL ONLY** |
| W-F delivery leg (transport binding, recipient resolution, medium formatting) | blocked on the audience answer | **UNBLOCKED** |
| W-E rows WE-1/2/3 | audience-blocked | audience half discharged; **DL existence still a tenant-admin act** |
| `2.0.0_SA_COO~Z` | conditional on "if the results go well" | **AUTHORIZED, explicit** |

### 0b. ⛔ AND IT RE-OPENS A FIELD CUT -- THE FIRST CONSEQUENCE, NAMED BEFORE IT IS DISCOVERED

`0.5.0_AE_OpalETL~Z` built W-E with two **separately-reasoned** withholdings, deliberately not collapsed:
- **WE-4-PROHIBITED** (content-scope): events, description, source, created_by, status, claimed_by, assignee -- *stays withheld, unaffected by audience.*
- **AUDIENCE-DEFERRED**: `title`, `requester.{email,name,firm}` -- **these are exactly the fields Andrew now asks for** (*"who is it from, subject line they included, body text"*).
> **INTERNAL RELEASES THE DEFERRED SET AND ONLY THAT SET.** The seat's decision to keep the two reasons as two named tuples rather than one list is what makes this a **one-line re-cut instead of a re-derivation** -- had they been merged, releasing the audience half would have required re-litigating the prohibition half. **That is the payoff of a distinction made at authoring time.**
> ⚠ **`body text` IS A NEW FIELD, NOT A RELEASED ONE.** It is neither in the prohibited tuple nor the deferred one -- W-E's cut carried `description` as **WE-4-PROHIBITED**. Andrew is now asking for the requester's submitted body **in an internal email**. **The prohibition was written for an undetermined audience; internal changes its basis.** This needs an explicit re-ruling at the gate, not a silent release under cover of the audience answer.

---

## 1. THE DECLARED ARCHITECTURE -- firm-keyed routing, single group today

**His words: *"some group of people get an email based on the firm in question making the request. for now, its same group of people for every firm, but eventually it might make sense to split that which is why i declare it up front."***

**THIS IS A DESIGN CONSTRAINT DECLARED AHEAD OF NEED, AND IT IS THE MOST VALUABLE SENTENCE IN THE INSTRUCTION.** The requirement is not "send to a DL." It is:

```
resolve_recipients(firm) -> [addresses]
    today:   every firm -> ONE group        (one row, or a default)
    later:   per-firm rows added            (config change, NOT a refactor)
```

**FORBIDDEN BY THIS DECLARATION:** a single hardcoded DL constant, or a `TICKET_DL` env var consulted directly at the send site. Either makes the eventual split a code change across the send path.
**REQUIRED:** a resolution seam with the firm as its key, whose current configuration happens to be uniform. **The uniformity is DATA, never STRUCTURE.**
*(This is the same discipline the build seat already applied unprompted to the deep-link base -- it refused a baked route because a default string would pre-encode an answer. Same reasoning, one layer out.)*
⚠ **Rule-24 note:** `firm` as a routing key must resolve for a request whose firm is **absent or unrecognised**. That is a real cell -- an intake form can carry a firm the estate does not know. **Refuse-if-unresolvable vs fall-back-to-default is a ruling, not an implementation detail**, and it is on the open-questions list (Q4).

---

## 2. SIDE A -- INTERNAL OPS

### A1. THE EMAIL (initial buzz only)

| Element | Ruled | Open |
|---|---|---|
| **Trigger** | ticket CREATE, from the Lambda write path | -- |
| **Recipients** | firm-keyed resolution, uniform today (sec. 1) | **who is in the group** (Q1) |
| **Subject** | **must incorporate the firm name** | exact grammar (Q2) |
| **Body** | structured rendering of the submitted form: **from · their subject · their body** | `body text` release (sec. 0b) |
| **CTA** | **one standard hyperlink** to the dashboard ticket-center page + a call to action to claim | link target + whether deep-link-to-ticket or list page (Q3) |
| **Follow-ups** | ⛔ **NONE.** No accept email, no complete email. *"the rest is handled on the dashboard itself."* | -- |
| **Sender** | `opalinvest.dev`, pinned constant, no fallback | ruled, built |

> **THE FOLLOW-UP PROHIBITION IS A SCOPE BOUNDARY, NOT AN OMISSION.** Andrew ruled it explicitly, and it is the internal side only -- **the client side DOES get a pickup notification (sec. 3).** These are opposite answers to a similarly-shaped question and **must not be collapsed into one "notification policy."** A future reader who reads "no follow-ups" as global will delete the client's pickup email.

### A2. THE TEAMS THREAD

Two questions Andrew names, and they are **different problems with different owners**:

**(a) STRUCTURE + PROCESS** -- what the Teams thread looks like as the internal-ops counterpart to the email, and **how the Opal agent manages that process** (thread per ticket? one channel? who posts, when, and what closes a thread). This is a **design question, unruled**, and it belongs with the ticketing design.

**(b) HOW THE AGENT WRITES ON TEAMS -- A CROSS-CUTTING FORMATTING STANDARD, NOT A TICKETING ITEM.**
His words: *"it really needs to do better formatting, it has a tendency to just block a wall of text."* The standard he states:
- empty returns **between** paragraphs
- **2-3 sentences maximum** per paragraph
- **key lines and hyperlinks on their own line**
- **hyperlinks properly linked so they are clickable**

> ⛔ **(b) IS NOT SCOPED TO TICKETING AND MUST NOT BE BUILT INSIDE IT.** Every Teams message the Opal agent sends has this defect today -- the concierge seat's replies included. Building the fix inside the ticket notifier would produce **one well-formatted surface and an unchanged agent**, and the next surface would rebuild it.
> **PLACEMENT: this is a property of the agent's Teams SEND PATH** (and, for the concierge, its prompt). It gets its own workstream, and the ticketing thread CONSUMES it rather than containing it.
> ⚠ **The clickable-hyperlink half is a TECHNICAL question, not a prose one** -- whether a link renders clickable depends on the message content-type the send path uses. **That must be measured at the send path before any formatting rule is written**, or we will write a style guide against a renderer that ignores it. **This is an atom-decomp juncture (sec. 5, J2).**

---

## 3. SIDE B -- CLIENT-SIDE

**Andrew: *"client-side input and experience/notification (should likely be covered both on dashboard and on their email, i.e. getting an email when their ticket is picked up and by who)."***

| Leg | State | Note |
|---|---|---|
| **Input** -- the intake form | **LIVE** (a real partner ticket has flowed) | -- |
| **Experience** -- the dashboard | portal accept/in-progress/complete **LIVE (P0)** | what the *client* sees vs what *staff* see is not yet mapped |
| **Notification** -- email on **pickup**, naming **who** | **NOT BUILT** | this is the new build |

> ⛔ **THIS IS THE FIRST CLIENT-FACING EMAIL IN THE TICKETING SYSTEM AND IT IS A DIFFERENT RISK CLASS FROM THE INTERNAL BUZZ.**
> - **Content projection binds hard here.** WE-4's *pointer-not-home* rule was written for exactly this: an email to a client must not carry the internal audit trail, routing state, or internal notes. Internal recipients tolerate a leak of internal state; **a client is who that rule exists to protect.**
> - **The cross-tenant hazard the build seat raised now lands for real.** Their reasoning on `title`: *"under a client-facing DL its safety turns on a further undetermined sub-question -- single-recipient ack vs multi-firm list -- and on the second reading one firm's title reaching another is a cross-tenant leak."* **For the client leg the answer must be SINGLE-RECIPIENT by construction**, addressed to the requester, never to a list. That is a design invariant and should be built as one, not as a convention.
> - **"by who" is an identity disclosure decision.** Naming the Opal staffer who claimed the ticket to an external client is a product choice with a privacy dimension. Andrew asked for it explicitly, so it is ruled -- but **what form** (full name? first name? role? "an Opal advisor"?) is Q5.

**And the asymmetry is deliberate:** internal gets **one** email and no follow-ups; the client gets **a pickup follow-up**. Recorded here so nobody harmonises them.

---

## 4. SIDE C -- INFRASTRUCTURAL SYNTHESIS

*"make sure it all works reliably in tandem."* The reliability question is **not** "does each leg work" -- each can pass alone and the system still fail. The known structural facts, all measured tonight:

**C1. TWO DEPLOYMENT PLANES, and the notification legs straddle them.**
- **Lambda plane** (`opal-ticket-api`): reaches production via Terraform + a **laptop apply**. Editing the repo changes nothing that runs. Currently **4 commits held**, deployed == `1fd9ef2750`.
- **Runner plane** (`OPAL_D7_ticket_intake`, `PT5M`): the Scheduled Task executes **the repo path**. **An edit IS a deploy, within 5 minutes, with no apply step.**
> **Any plan that says "deploy the notification system" is false on one plane whichever way it is said.** Every workstream below states its plane.

**C2. THE TEAMS PATH CARRIES A ~1h CREDENTIAL DEPENDENCY; THE EMAIL PATH DOES NOT.**
The gateway bearer is validated before tool dispatch, so **every** gateway-mediated send inherits an agent-session dependency. SES from the Lambda uses the Lambda's own IAM role.
> **THIS IS WHY THE EMAIL IS THE FIRST LINE AND THE AGENT IS THE CONVENIENCE LAYER** -- Andrew's own ordering, and it falls out of the architecture rather than being asserted. **The synthesis must not quietly make the Teams leg load-bearing.**

**C3. SES IS OUT OF THE SANDBOX** -- production access granted, 50,000/day, 14/s. Recipient restrictions gone; the client leg is deliverable.

**C4. THE RELIABILITY QUESTION, STATED PROPERLY.** Not *"does each leg work"* but: **when one leg fails, what does the system do?** W-E already established the shape -- the email leg erroring must still yield a 201 and a buzz, with a **named** error distinguishing *unconfigured* from *refused*. **That principle now has to hold across four legs (internal email, Teams, client email, dashboard), and the failure matrix is a design artifact, not a test artifact.**

---

## 5. SEQUENCE, AND WHERE `/atom-decomp` GOES

Per Andrew's standing protocol instruction: **PRD -> TO issuance -> proof-of-spec -> confirmation, with atom-decomp truth established AHEAD of key junctures.** A juncture is **the first irreversible act**, not the acceptance.

| # | Act | Plane | Juncture? |
|---|---|---|---|
| **0** | **This plan ratified** by Andrew | -- | -- |
| **1** | **PRD** written: the three sides as one document, `docs/architecture/D7_TICKETING_INTAKE_PRD.md` amended or successor | -- | -- |
| **J1** | **`/atom-decomp`: THE CLIENT-FACING SURFACE.** What does a client actually see today -- dashboard routes, identity/auth, what the portal exposes per firm? | -- | ⛔ **BEFORE any client-facing build.** We have never sent a client an email from this system; the surface is unmapped and a wrong assumption here is a cross-tenant leak, not a bug. |
| **2** | **W-E re-cut** to the internal schema (sec. 2 A1) + firm-keyed resolution seam | Lambda | -- |
| **J2** | **`/atom-decomp`: THE TEAMS SEND PATH.** What content-type does the agent post? What renders clickable? Where is formatting decided -- code, prompt, or both? | -- | ⛔ **BEFORE writing any formatting standard**, or we write a style guide against a renderer that ignores it. |
| **3** | **Teams formatting standard** + agent send-path fix | gateway/agent | own workstream, consumed by ticketing |
| **4** | **Teams thread structure + process** for internal ops | gateway/agent | -- |
| **5** | **Client pickup notification** | Lambda | single-recipient by construction |
| **6** | **Failure-matrix design** (C4) then the wiring acts | both | ⛔ **the W-F import edge is a live deploy** -- it goes last, deliberately |

---

## 6. OPEN QUESTIONS FOR ANDREW (none blocking the PRD)

| # | Question | Why it needs him |
|---|---|---|
| **Q1** | **Who is in the group today?** The DL does not exist -- creating it is a tenant-admin act, and its membership is a business call. | blocks the internal email's exercise, nothing else |
| **Q2** | **Subject-line grammar.** He said *"firm name incorporated somehow"* -- deliberately left open. Proposal: `[<FIRM>] <requester subject>`, firm first so it sorts and filters. | his phrasing, his call |
| **Q3** | **Link target:** the ticket-center **list** page, or a **deep link to that ticket**? He said "the dashboard ticket center page"; a deep link is likelier what a claimer wants. | one word changes the build |
| **Q4** | **Unknown/absent firm:** refuse loudly, or fall back to the default group? Given the declared firm-keying, this is a real cell. | a routing ruling |
| **Q5** | **"by who" form** in the client email: full name / first name / role / "an Opal advisor"? | client-facing identity disclosure |
| **Q6** | **Client submit-confirmation:** he named only the *pickup* email. Does a client also get an immediate "we received it"? | scope |

---

## 7. WHAT THIS PLAN DOES NOT DO

- **It issues no TOs.** He asked for structure; the TOs follow ratification.
- **It builds nothing and applies nothing.** The W-F import edge stays unwritten.
- **It creates no alarms, monitors, or freshness checkers.** He authorized a **notification feature**; the 2026-07-28 moratorium is untouched for everything else, and nothing in sec. 4 licenses a monitor.
- **It manufactures no gates.** The two `/atom-decomp` junctures are his own standing instruction applied, not new approval steps.
