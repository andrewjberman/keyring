# 1.0.0_SA_CTO~Z — the D7 gate, second window 21:50–22:50Z

**archetype:** COORDINATE
**secondary_archetypes:** VALIDATE, DIAGNOSE

14 commits. **The window's headline is that a build was DELETED rather than approved**, and the reasoning
that deleted it was corrected four times on the way — three of those corrections mine.

---

## What was decided

| Item | Outcome |
|---|---|
| **W-A build leg** | **ACCEPTED.** WA-6 is a real IAM finding, found with the full Rule-22a protocol incl. an isolated positive control. All four WA-9 decisions ratified — **two improved on my own rulings.** |
| **W-B** | **AWS half HELD → then RECOMMENDED DELETED.** The stream's last arrow had no mechanism; then the numbers showed its marginal benefit ≈ the wake hop it cannot touch. |
| **`lastModifiedDateTime`** | **RULED into the next gateway touch**, batched with S2. Built @`90d526c199`, not applied. |
| **Ruling 3 (the "now watching" post)** | **RETRACTED** — prohibited by the ~2135Z Andrew-direct, not deferred. |
| **The comp-rail override standard** | **RULED**: an override justification is a **TESTED claim**, not an assumed one. No gate. |
| **"A readback is not a record"** | **RULED AS DOCTRINE** after the TAC-2' buzz changed under four seats. |

## The W-B arc, because it is the window

1. `0.5.0_AE_OpalETL~Z` **stopped before writing** — the chain ended `notifier Lambda → "BG's nudge"` and
   **that arrow had no mechanism.** A Lambda cannot write a local inbox and can never hold the gateway
   credential.
2. I held the AWS half — **and two of the reasons were mine**: my scoping's *"zero new infrastructure"* was
   false (that queue is coordination-only by charter), and **I had cleared past my own sequencing ruling**
   that the wake hop must be measured before funding a transport build.
3. The wake hop **had** been measured — at 21:32Z, **48 minutes before I called it unmeasured.**
4. The arithmetic: **first step buys ~135s, second buys ~13s.**
5. `0.0.3_BG_BBGTerminal` sensitivity-tested it **in the direction that would hurt their own preferred
   option** — ordering survives at 9.5:1.
6. `2.0.0_SA_COO~Z` challenged the 30s premise; **I settled it: the engine REFUSES `PT30S`**, `PT1M`
   accepts on the identical path, positive control passing, zero residue.
7. `3.0.0_SA_CVO~Z` closed it for decision purposes — **right-side-up at every floor below ~180s**, three
   times the settled value.

**Final: 4.3:1 at the established 1-minute floor. Recommendation — take the schedule change, drop the
stream.** Carded to Andrew as a *preference* call, since he asked for no polling at all.

## My errors this window — four, and three reached the sovereign's card

| Error | Caught by |
|---|---|
| `"0 gaps"` answers **presence**; the damage was **fidelity** — my own 5th instance is invisible to my own check | `3.0.0_SA_CVO~Z` |
| `"comp-find is case-sensitive"` **without qualification** — true of content, **false of `--name`** | `0.4.0_DT_ClientPlatform~Z` |
| **"10:1" and "13s < the wake hop"** — both rested on a **30s schedule I never verified** | `2.0.0_SA_COO~Z` |
| **"The wake hop is still unmeasured"** — it had been measured 48 min earlier | `0.5.0_AE_OpalETL~Z` |

**THE PATTERN, and it is one pattern:** *a claim about a mechanism's capability, made without consulting
the mechanism.* The `--name` one is **failure shape 3 from my own artifact, committed in the urgent
broadcast about that artifact.**

⛔ **And the bias I banked at 21:0xZ produced its fifth and sixth instances after I banked it** — including
in the message adopting a phrase *about* the bias. **Knowing a failure mode by name does not immunise you
against writing it.** The one thing that fired was a *reflex* built by repeated exposure (re-run a zero
before reporting it), not a rule I had written down.

## What the other seats did that is worth copying

- **AE~Z** offered the option that **deletes their own lane's centrepiece** — the rung-1 question a builder
  is least incentivised to ask. Also self-reported that their W-A test stub *shared the code's wrong
  assumption*: **22/22 green on a call that could never have worked.**
- **BG** measured the wake hop by hand on real traffic, stated its warm-schema bound unprompted, then
  **ran the sensitivity that could have overturned their own preference.**
- **COO~Z** found a defect in their own TOs prompted by a line of mine, and **declined two empty reads as
  an answer** — which is what produced the 30s catch.
- **CVO~Z** timed a schema read **before** the cut, then caught that my card would have **closed a question
  that is actually open** (~88% of the stream's best case is the agent layer, not transport).

## Compiler Tools

| Tool | Result | Note |
|---|---|---|
| `comp-find` (content + `--name`, with and without `-i`) | PASS | **and found against itself** — case-sensitive by default in content mode |
| `comp-find` (WA-10 token at source) | PASS | took it after the rail blocked a raw grep; returned band + denominator the grep would not have |
| `Get/Register/Unregister-ScheduledTask` | PASS | `PT30S` **refused by the engine**, `PT1M` accepted, positive control, 0 residue |
| `ToolSearch` (`get_delivery_state` schema) | PASS | the check I should have run before carding "unexecutable" |
| risk-reflex | PASS ×14 | denominator printed each commit |

**What worked:** running the decisive test myself instead of routing it, once a refuted premise had reached
three seats' artifacts.
**What failed:** a case-sensitive census — **the same defect I had adopted a ruling against an hour
earlier.**
**Gap found:** `comp-find` is case-sensitive by default **in content mode**; `--name` is not. Not a defect —
an undocumented asymmetry now recorded.

## Blockers

**None.** Event-gated: A1 · W-A's apply (WA-6's grant first, §6a print confirmed) · the gateway touch ·
Andrew on W-B, item 3, the W-D collision, which-thread, the DL actor, and the ack primitive.

## Current State

D7 intake live producer-side; consumer limb landed, unproven until A1. **W-B's stream recommended
deleted**, nudge semantics retained. `closure_reason` adopted (6 values). W-D limb (1) held, limb (2) free.
**S2's repo half is LIVE and self-deploying** — confirmed at three seats by tool-manifest evidence with
both a cross-tool and a cross-time control, no code read. The gateway deploy path is
`/opt/m365-mcp-gateway/app/` — **not** the repo's `opal-gateway/`.

## Next Steps

- **[1.0.0_SA_CTO~Z]** A1 read; W-A apply verification; Andrew's answers.
- **[0.5.0_AE_OpalETL~Z]** W-A apply prep; the deploy-path fact into the gateway deploy record.
- **[2.0.0_SA_COO~Z]** W-B re-cut on option (ii) if Andrew agrees.
- **[0.0.0_AB_MSTR~Z]** the card is with him, complete.
- **[ANDREW]** six carded calls, none held.
