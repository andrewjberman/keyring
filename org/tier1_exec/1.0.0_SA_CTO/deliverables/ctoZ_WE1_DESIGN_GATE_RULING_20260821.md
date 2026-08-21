# WE-1 DESIGN GATE -- RULED: transport + sender. AND A BLOCKING PRECONDITION NOBODY IN THE CHAIN HAD SURFACED: SES IS IN THE SANDBOX.

**Gate owner:** `1.0.0_SA_CTO~Z` - **Date:** 2026-08-21 ~02:05Z - **TO:** `D7_TICKETING.WE-SITEZ` (`org/tier2_senior/0.5.0_AE_OpalETL/task_orders/`)
**Authority for the feature:** Andrew-direct 2026-08-20 ~20:45Z @`11d274f8c2`, VERBATIM: *"That is why the email needs to be the first instantaneous line of attack, the agent is just making it more convenient and teams-friendly."* (This is also the `# andrew-asked` marker text; the 2026-07-28 notification moratorium is satisfied by explicit ask.)
**Vintage of every measurement below:** HEAD @`d79d073c94`, live AWS reads 2026-08-21 ~02:00-02:04Z.

---

## 0. WHAT THIS RULING DOES AND DOES NOT DISCHARGE

WE-1 as written is **two claims joined by an `and`**: *"transport + sender identity ruled by `1.0.0_SA_CTO~Z`, recorded before any build act; **the DL address exists and its creating actor is named** in the record."*

Applying the TO's own cut test -- *"IF A TASK'S OUTPUT WOULD BE BYTE-IDENTICAL UNDER EITHER AUDIENCE ANSWER, IT IS NOT BLOCKED AND MUST NOT BE WRITTEN AS BLOCKED"*:

| WE-1 half | State | Owner |
|---|---|---|
| **transport + sender identity** | **RULED HERE.** Byte-identical under either audience answer -- SES-from-Lambda is the same code and `opalinvest.dev` is the same sender whether the DL is internal or client-facing. | this gate -- **DISCHARGED** |
| **DL exists + creating actor named** | **NOT DISCHARGED.** Tenant-admin act, and its recipient composition is the audience question. | Andrew / tenant admin |

> **I am ruling the half that is mine and saying so, rather than holding both on a question that touches only one.** My predecessor corrected this exact wrong-grain error three times in ten minutes on this same TO and wrote the reason into it: **A DEPENDENCY STATED AT THE WRONG GRAIN DOES NOT LOOK LIKE AN ERROR -- IT LOOKS LIKE CAUTION**, and a hold wider than its cause is a manufactured gate on the excess. Holding transport on audience would be that error a fourth time, in the file that names it.

**AND I AM STILL NOT RULING THE AUDIENCE.** It is carded to Andrew because it decides what a client sees. Unblocking W-F's delivery leg is not a reason to take that decision back from him -- that discipline is my predecessor's and it stands unchanged.

---

## 1. TRANSPORT -- RULED: **SES, invoked from the CREATE Lambda write path.** The gateway is DISQUALIFIED.

**Criterion (1) -- does the send path depend on an agent-session-refreshed credential?**

- **Gateway: YES -> DISQUALIFIED.** Source-confirmed, and the finding is **structural, not probabilistic**: the gateway Bearer is fully validated *before any tool name is dispatched* (`server.py:15`, `:92-98`), so a call that cannot present a live bearer never reaches a tool. **Every** gateway-mediated send inherits the ~1h agent-session dependency by construction and **no per-tool exception is possible.** Measured live 2026-08-20 21:04-21:06Z: a scheduled fire exited 2 (`pinned gateway token expired`); one agent read moved expiry out an hour and the runner immediately returned `INTAKE PASS OK`.
- **The disqualification rests on ENTANGLEMENT, not impossibility** -- the corrected form, and the honest one. The credential store carries `refreshToken` + `clientId` + `redirectUri` + `scope` on 4 of 4 records, so a server-to-server `refresh_token` grant is materially available. It is not used **by design**: the engine's own docstring says *"Claude Code owns the refresh (rotating tokens), so this never refreshes itself -> no refresh-token fight."* Making a gateway DL work unattended would mean **a second refresher racing Claude Code on rotating tokens** -- trading a predictable hourly gap for unpredictable mutual invalidation that would take down the agent's own connectivity.
  > **THE DURABLE PRINCIPLE: A BACKSTOP MUST NOT BE ENTANGLED WITH THE CREDENTIAL OF THE SYSTEM IT COVERS.** A gateway-mediated DL would fail in exactly the window it exists to cover, and fail **silently from the DL's own point of view** -- a 401 is a clean, well-formed refusal.
- **SES: NO.** Invoked from the CREATE Lambda, it authenticates with the **Lambda's own IAM role**. No interactive client, no session, no rotating token, no agent.

**The ordering claim also falls out of the architecture rather than being asserted:** the CREATE Lambda write *is* the instantaneous moment; the agent buzz rides the 5-minute scheduled runner. So an email sent from the write path is **instantaneous by construction** and the agent stays the convenience layer **by construction** -- which is precisely what Andrew described. **Ruled as design, per the TO's flag that the decomposition's read needed this gate's word.**

---

## 2. SENDER IDENTITY -- RULED: **`opalinvest.dev`.** Measured, not cited.

NEVER#23 binds absolutely and admits no fallback sender. Verified live at this seat:

```
aws sesv2 get-email-identity --email-identity opalinvest.dev
  -> Verified: true | DkimStatus: SUCCESS | DkimSigning: true | Type: DOMAIN
NEGATIVE CONTROL  zzz-no-such-domain-9999.example -> NotFoundException
  -> the read DISCRIMINATES; "true" is not an undiscriminating yes.
```

`opalinvest.com` remains address-verified only (nondeterministic EOP quarantine -- a silent coin-flip, not a clean fail), and **`opalcapital.com` is not ours and is not a verification TODO.** Graph `sendMail` as the gateway identity would have sent as `opalbloomberg@opalinvest.com` -- a different domain with a different posture -- and is disqualified by criterion (1) regardless.

> ### A RETRIEVAL CORRECTION, RECORDED BECAUSE IT NEARLY BECAME A FINDING
> My first read was `list-email-identities --query '...Verified:VerifiedForSendingStatus'` and it returned **`None` for all 25 identities, `opalinvest.dev` included.** That reads as *nothing in this account is verified* -- a fabric-wide alarm.
> **It was a wrong-field-name artifact.** `list-email-identities` returns `VerificationStatus`; `VerifiedForSendingStatus` exists only on `get-email-identity`. **JMESPath does not error on a field that is not there -- it returns `None`, once per row, in a clean well-formed table.** The raw one-record dump (`--page-size 1`, no `--query`) shows `"VerificationStatus": "SUCCESS"` and settles it.
> **THE CLASS, and it is the sixth of this night: an ABSENCE rendered by a retrieval that could not have returned presence.** Same family as the rail log with no write path and the binary search for a package. A `--query` naming a field the API does not return is indistinguishable, in the output, from a field that is genuinely empty.

---

## 3. BUILD LADDER RUNG 2 -- **THE ESTATE ALREADY HAS THIS PATTERN. REUSE IT; DO NOT AUTHOR A SECOND ONE.**

`comp-find EMAIL_FROM` -- **DENOMINATOR: 77 hits / 27,212 files, 1 UNREADABLE. BANDS: DEF=7 SURFACED=30 CONFIG=6 DOC=34.**

A complete, live SES-from-Lambda implementation exists at `infra/aws/lambda/trade-pipeline/`:

| Layer | Artifact |
|---|---|
| send call | `trade-submission-handler/src/email_utils.py:113-118` -- `ses.send_raw_email(Source=EMAIL_FROM, ...)` |
| sender config | `src/config.py:13` -- `EMAIL_FROM = os.environ.get('EMAIL_FROM', 'trades@opalinvest.dev')` |
| TF env wiring | `infra/aws/terraform/trade-pipeline/lambdas.tf:208`, `:243` |
| SES resources | `infra/aws/terraform/trade-pipeline/ses.tf` -- configuration set + bounce/complaint SNS + event destinations |
| enforcement | `org/modules/graph/ses_sender_lint_cli.py` + `.tools/commit_gate_runner.py:350-351` -- NEVER#23 is **already gate-enforced** on `Source=` literals and `EMAIL_FROM`/`SES_SENDER` env defaults, Python **and** Terraform |

**DIRECTION TO THE BUILD SEAT: port this shape.** The sender constant, the env-var indirection and the `send_raw_email` call are settled patterns with a live commit-time lint behind them.
⚠ **Two scope guards.** (a) The existing `ses.tf` carries **SNS bounce/complaint topics**; those exist for the trade pipeline's production-access packet. **Do NOT clone them for W-E** -- that is notification/monitoring machinery and the moratorium is untouched for everything he did not ask for. He authorized a **notification feature**, not a feedback-topic estate. (b) `EMAIL_FROM` here has a **baked default**; **WE-5 requires refuse-if-unset for the DL address**, so the *recipient* config must NOT copy the `os.environ.get(..., default)` shape. **Copy the sender pattern; invert the recipient one.**

---

## 4. BLOCKING PRECONDITION -- ~~**SES IS IN THE SANDBOX**~~ **DISCHARGED 2026-08-21 ~03:0xZ. PRODUCTION ACCESS REQUESTED AND GRANTED.**

> ### ⛔ THIS SECTION IS RESOLVED. IT IS KEPT IN FULL BECAUSE THE REASONING BELOW IS STILL HOW THE PROBLEM WAS FOUND.
> **Andrew-direct, ~02:5xZ, VERBATIM: *"Update the packet and send it."*** -- path (C) executed the same
> hour it was surfaced. Packet updated to his framing (*"internal operations and agentic tooling for our
> back office... internal ticketing and associated uses"*) @`2b97a0165e`, submitted via
> `sesv2 put-account-details`, and **GRANTED ON SUBMISSION -- no review queue.**
>
> | | before | after |
> |---|---|---|
> | `ProductionAccessEnabled` | `false` | **`true`** |
> | `Max24HourSend` | 200 | **50,000** |
> | `MaxSendRate` | 1.0/s | **14.0/s** |
> | `ReviewDetails` | absent | **`Status: GRANTED`, `CaseId: 178727932800843`** |
>
> **The status string alone would be weak evidence; the ENFORCED QUOTA MOVED ON THE SAME READ**, which is
> the account's behaviour rather than its self-report. Two independent fields agree.
>
> **WHAT THIS CHANGES FOR W-E:**
> - **The recipient restriction is gone.** An Opal DL on `@opalinvest.com` is reachable with no
>   per-address verification. **WE-2/WE-3 can now be EXERCISED** once the DL exists.
> - **Paths (A) and (B) below are MOOT.** The DL no longer has to sit on `opalinvest.dev`, and nobody has
>   to hand-verify its address. ⚠ **AND THAT DECOUPLES THE DL's DOMAIN FROM THE AUDIENCE QUESTION** -- path
>   (A) was audience-coupled, which was my reason for not choosing it. That coupling is now dissolved, and
>   **the audience question itself is untouched and still Andrew's.**
> - **The 12 FAILED identities stop mattering as recipients.** They were sandbox artefacts. They would
>   still matter for any *sending* identity -- none are; all sending is from the `opalinvest.dev` domain.
>
> **WHAT DID NOT CHANGE:** sections 1, 2 and 3. Transport, sender and the reuse direction are unaffected --
> production access was never an argument for or against SES-from-Lambda.

**The original finding, preserved:** SES was in the sandbox, and it was not a DKIM problem.

```
aws sesv2 get-account
  -> SendingEnabled: true | ProductionAccessEnabled: FALSE | EnforcementStatus: HEALTHY
```

**In the SES sandbox an account may send only to VERIFIED identities** (plus a capped daily volume). `ses.tf`'s own header states the config set and topics were built so that **Andrew** could submit the production-access Console form; `ProductionAccessEnabled: false` says that has **not been granted.**

> ### CORRECTED ~02:10Z -- MY IDENTITY COUNT WAS A PAGE, AND "VERIFIED" WAS THE WRONG WORD FOR MOST OF IT
> This paragraph read: *"the account currently holds `opalinvest.dev` as a verified DOMAIN and **24 individually-verified EMAIL_ADDRESS identities**."* **Wrong twice, and the correction makes the finding stronger, not weaker.**
> **(i) IT WAS A PAGE.** `list-email-identities` defaults to a page size of **25** and my table returned **exactly 25 rows** -- *a result that exactly equals the page size is a page, not a total*, and that was the tell sitting in my own output. Flagged by `0.0.0_AB_MSTR~Z`, then re-derived here by an **explicit token walk** (`--page-size 100`, materialised client-side). ⚠ **AND `--output json` PIPED TO A PARSER DID NOT SAVE ME EITHER: it returned 25 with `NextToken` STILL PRESENT in the response.** The CLI did not merge the pages, so a read I had labelled "auto-paginated" was **also a page.** Only the explicit walk was correct.
> **(ii) "INDIVIDUALLY-VERIFIED" WAS FALSE OF MOST OF THEM.** Verification *state* is not identity *existence*.
>
> **THE MATERIALISED CENSUS -- 1 page walked, TRUE TOTAL 26:**
>
> | | count |
> |---|---|
> | DOMAIN identities | **1** (`opalinvest.dev`, `SUCCESS`) |
> | EMAIL_ADDRESS identities | **25** |
> | `VerificationStatus: SUCCESS` | **14** total -- the domain + **13** addresses |
> | **`VerificationStatus: FAILED`** | **12 of 26 -- 46%** |
>
> FAILED: `jeanette@` `info@` `jim@` `wayne@`(opalinvest.com) - `mike@hirst.digital` - `patrick@` `noel@`(inflectionwealth.com) - `christa.bass@` `stephen.shipley@` `jay.rubottom@`(cottonwoodmail.com) - `support@` `noreply@`(opalinvest.dev).
> ⛔ **CORRECTED AGAIN ~02:08Z -- I RECORDED A DELTA THAT DID NOT EXIST, AND I ATTRIBUTED MY OWN TRUNCATION TO A PEER.**
> This line read: *"`0.0.0_AB_MSTR~Z` independently walked to 26 and read 11 FAILED; I read 12. The one-row delta is immaterial and I have not chased it."*
> **`0.0.0_AB_MSTR~Z` NEVER MEASURED VERIFICATION STATUS.** Their walk reported pages, total, by-type, the domain list and the `@opalinvest.com` address count -- **the word FAILED appears nowhere in anything they sent.**
> **THE `11` WAS MY OWN PAGE-1 COUNT.** My truncated read printed `SUCCESS 14 / FAILED 11` over 25 rows; the full walk gives `14 / 12` over 26. **So the page did not merely hide an identity -- it hid a FAILED one, and understated the decay rate itself (11/25 = 44% vs 12/26 = 46%).** The page-vs-total error, one layer up, inside the paragraph correcting the page-vs-total error.
> **INDEPENDENTLY RE-DERIVED at `0.0.0_AB_MSTR~Z` on request: 12 of 26, MEMBER SETS IDENTICAL** -- and derived on a *different field* (`SendingEnabled` false) than mine (`VerificationStatus` FAILED), which makes it corroboration across two attributes rather than a repeat of one query.
> **WHY THIS IS WORTH A CORRECTION WHEN THE NUMBER DID NOT MOVE (their argument, and it is right): A PHANTOM DELTA IS WORSE IN A RECORD THAN A REAL ONE.** "Two seats got 11 and 12" tells the next reader that two independent instruments diverged, inviting the inference that the read is noisy near the boundary -- quietly discounting the 46%. The truth is the opposite: **one seat measured, the other had not, and when it did it landed on the same twelve.** A real disagreement gets chased; a phantom one gets *"noted and not chased"* -- durable, unfalsifiable, and it attaches doubt to a number that has none.

> ### ⛔ THE CONSEQUENCE FOR W-E, STATED PLAINLY
> **An Exchange distribution group lives on the TENANT domain -- `@opalinvest.com` -- which is NOT a verified DOMAIN identity in this account.** So in the current sandbox posture, **SES -> that DL is REJECTED.**
> **THIS IS A DIFFERENT AXIS FROM THE ONE THE TO IS WATCHING.** The TO's criterion (3) is *DKIM state*, and DKIM is **fine** -- `opalinvest.dev` is SUCCESS/signing. **DKIM governs the SENDER; the sandbox governs the RECIPIENT.** A gate that checked only criterion (3) would have passed this build straight into a send that cannot be delivered.
> And by the TO's own standard -- *"a first instantaneous line that lands in quarantine is worse than no first line, because it reads as sent"* -- a sandbox rejection is **worse still**: it is not a coin-flip, it is a deterministic failure of the exact feature, on every ticket.

**THREE RESOLUTION PATHS. NAMING THE ACTOR FOR EACH, NOT ASSUMING ONE, and NOT picking for him:**

| # | Path | Actor | Note |
|---|---|---|---|
| **A** | **Put the DL on `opalinvest.dev`** (the already-verified domain) | tenant admin, with Andrew's word | Sandbox-clean **today**, no AWS request, no waiting. **Cheapest by a wide margin, and the census below strengthens it: a verified DOMAIN identity covers EVERY address on it, so this path needs no per-address act now or ever.** Trades against whatever the DL address is supposed to *look* like to its readers -- which is the **audience** question, so this path is audience-coupled and I am not choosing it. |
| **B** | **Individually verify the DL address** as an SES EMAIL_ADDRESS identity | tenant admin + whoever holds the DL mailbox (verification is a click-through on a mail to that address) | Works in the sandbox, and **it is the estate's ESTABLISHED PRACTICE, not a proposal -- 15 `@opalinvest.com` addresses have been verified this way** (`0.0.0_AB_MSTR~Z`'s delta). ⛔ **But the fragility is no longer hypothetical: 12 of 26 identities are ALREADY `FAILED` -- 46%, measured, right now.** Per-address verification in this account has demonstrably decayed on nearly half of what it was applied to. **A DL is exactly the kind of address that changes, and nobody re-verifies.** |
| **C** | **Request SES production access** (Console form) | **ANDREW** -- explicitly his, per `ses.tf`'s own header | Removes the constraint permanently and for the whole estate. Not instantaneous: AWS review. `ses.tf`'s prerequisites (config set + bounce/complaint topics) are **already built**, so the packet's blocker is discharged. Packet: `infra/aws/ses/trade-pipeline-prod-access-request.md`. |

> ⛔ **AND THE CENSUS CARRIES ITS OWN PROOF OF (A) OVER (B), which I record because it is measurement rather than preference:** `support@opalinvest.dev` and `noreply@opalinvest.dev` both sit in the FAILED list **as ADDRESS identities -- and it does not matter**, because the **DOMAIN** identity `opalinvest.dev` is `SUCCESS` and covers every address on it. **Those two rows are harmless residue of doing (B) where (A) already applied.** The account therefore contains a worked example of both paths side by side: the domain identity has needed no maintenance, and 46% of the per-address ones have lapsed.

**GATE POSITION: A or B unblocks W-E without waiting on AWS; C is worth doing regardless and is his call.** I am **not** requesting production access, **not** creating identities, and **not** choosing the DL's domain -- all three are outside a design gate's authority and (A) is entangled with the audience decision that is his.

---

## 5. WHAT REMAINS OPEN, AND WHOSE IT IS

| Item | Owner | State |
|---|---|---|
| **DL audience** -- internal / mixed / client-facing (criterion 2) | **ANDREW** | carded, unresolved. Gates W-F's *transport binding, recipient resolution, medium formatting* -- **and nothing else.** W-F's trigger, detection and invariant payload are FREE and already built. |
| ~~**SES sandbox** (sec. 4)~~ | ~~ANDREW / tenant admin~~ | ✅ **DISCHARGED ~03:0xZ -- production access GRANTED, case `178727932800843`, quota 200 -> 50,000/day.** Surfaced and closed within the hour on his direct word. WE-2/WE-3 are now exercisable once the DL exists. |
| **DL creation + address reported** | tenant admin (the "Opal Client Tickets" channel precedent -- Andrew created it by hand) | not started. Address is CONFIG, refuse-if-unset, never a baked default. |
| **transport + sender** | this gate | **DISCHARGED** by this document. |

**THE BUILD SEAT MAY NOW START** the transport-and-sender-dependent work: the SES call site in the CREATE Lambda write path, the `opalinvest.dev` sender wiring, WE-5's refuse-if-unset recipient handling, and WE-6's no-regression isolation (**the email leg erroring must still yield a 201 and a buzz** -- the runner and CREATE Lambda are live production infrastructure). ~~**WE-2/WE-3 cannot be exercised until section 4 resolves**~~ -- **section 4 RESOLVED ~03:0xZ; WE-2/WE-3 are exercisable as soon as the DL exists.** The only remaining prerequisite for exercise is the DL itself (tenant-admin act).

⚠ **HONEST BOUND, carried forward unchanged: SES has still not been exercised from this estate's ticket path.** The trade-pipeline implementation makes the pattern **proven in-estate**, which is stronger than the "architecture, not an exercised send" the TO recorded -- but it is still not *this* Lambda, *this* role, *this* recipient. **WE-2/WE-3 remain the exercised proof and nothing here substitutes for them.** The `comp-iam` floor read on the sending principal is a build-time step per the TO's compiler-tools mandate and a **new SES action on a new principal needs the live `simulate-principal-policy` primitive with ONE `--resource-arns` and a separately-invoked positive control** (Rule 22a) -- `comp-iam` models `(action)`, never `(action, resource)`.

---

## 6. Compiler Tools

| Tool | Result | Note |
|---|---|---|
| `comp-find EMAIL_FROM` | **PASS** | 77 hits / 27,212 files, DEF=7 -- the DEF band went straight to the four `config.py` sender constants and the TF literals. Rung-2 reuse found in one call. |
| `comp-find validation_context_declaration` | PASS | 13 / 27,212, bands separated generator from real declarations |
| `aws sesv2 get-account` | **PASS -- the finding** | rail-checked; no comp-tool models SES account posture (`comp-iam` is TF-DESIRED and `(action)`-only) |
| `aws sesv2 get-email-identity` + negative control | **PASS** | `NotFoundException` on a bogus domain proves the read discriminates |
| `aws sesv2 list-email-identities --query VerifiedForSendingStatus` | **FAIL -- caught** | wrong field for that API; returned a clean `None` column that reads as a fabric-wide alarm. Corrected by dumping one raw record. |
| `aws sesv2 list-email-identities` (count) | **FAIL -- caught by a peer, then twice more by me** | **Three reads, three pages, one true total.** The default page returned **exactly 25** -- the page size, which was the tell. `--output json` into a parser ALSO returned 25 **with `NextToken` still present** (the CLI did not merge). Only an **explicit `--starting-token` walk** gave the true **26** -- and only that read surfaced the **12 FAILED**, which is the finding. Flagged by `0.0.0_AB_MSTR~Z`. |

**Gap:** `comp-kuzu`/`comp-blast` hang on this box -- named at every use, never a false clean.

---

## 7. Reporting

Per the TO: completion -> `2.0.0_SA_COO~Z` (validation), cc `1.0.0_SA_CTO~Z` (acceptance) + `0.0.0_AB_MSTR~Z` (ferry).
**This ruling routes to:** `0.5.0_AE_OpalETL~Z` (build seat -- sections 1/2/3 are your direction, section 4 is why WE-2 cannot close yet), `2.0.0_SA_COO~Z` (TO status: the design gate is half-discharged, not fully), `0.0.0_AB_MSTR~Z` (ferry -- **section 4 is an Andrew card**).
**No seat is dispatched by this document.** No `~Z` build seat is live; this is the gate clearing its own blocking item so nothing waits on me when they come up.
