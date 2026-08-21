# 0.5.0_AE_OpalETL~Z — TO-F failure matrix (+ E-2 rebuild, WA-6 annotation, D-HTML) 0910–1015Z

**Serial** `0.5.0_AE_OpalETL~Z` · **2026-08-21** · site Z

## What landed

| commit | what |
|---|---|
| `429730ef7f` | E-2 rebuilt on the ruling: "An Opal advisor" + a three-way discriminating log; Rule 26 supersession annotated across 5 artifacts, zero evidence rows touched |
| `734ff16fc9` | WA-6 takes the **(c)** criterion-clause form — and needs more than the ruling's wording, because that wording was written for a PASS row |
| `7b7b0004a9` | **D-HTML built, not wired**: the html renderer beside the text one, one shared standard, battery 14 -> 35; the 4-line wiring diff recorded unapplied with the deploy cost read at source |
| *(this commit)* | **TO-F F-1 + F-2**: the four-leg failure matrix (20 cells) and the runner-plane exercises |

## The three things worth carrying forward

**1. I used a tiebreaker that could not break the tie.** On E-2 I rejected "An Opal advisor" as *an
answer Andrew did not give* — without noticing that refusing to send is **equally** an answer he did
not give. The argument I used could not have selected between the two options, and I ran it as
though it had. That is not a bad measurement; it is a **non-discriminating argument**, and it is the
rhetorical form of an instrument that could not have said otherwise.

**2. My own instrument failed before the code did, and it failed toward a false alarm.** The
D-HTML conservation test reported content loss on a correct renderer, because my test-side HTML
stripper deleted tags instead of substituting a space — so two paragraphs fused into one token. The
estate's own reader (`tools.py:692`) already substitutes a space. **The instrument was wrong, not the
renderer**, and I only found that by asking what the recipient actually sees rather than trusting
the red.

**3. Checking reachability changed a finding's severity, and it was the check that mattered.** The
buzz-leg wedge (below) looked like a live vulnerability until I traced `created_at` and found it
**server-generated** (`lambda_function.py:389`) — a client cannot reach it. Then the live runner log
showed **169 exits, no `rc=1`**, which is positive evidence it has never fired. Same defect, honestly
much smaller, and reported at the size the evidence supports.

## TO-F findings

- **FINDING 1 — the buzz leg has a PERMANENT WEDGE mode.** `row_contract` validates `created_at` by
  **shape** (`len >= 20 and endswith("Z")`); `buzz.received_eastern` needs it to **parse**. A row in
  that gap raises out of `compose_buzz`, which sits **outside** `run_once`'s try. Exercised: passes
  1/2/3 die identically, the cursor never advances, everything sorted after it is never buzzed, and
  the process exits **1** — outside the declared `0/2/3/4/5` contract. Latent (server-generated
  input, 0 occurrences in 169 passes). Remedy: make the contract **parse** the stamp, which routes
  it into the existing `REFUSED` outcome. **Not applied — live-production file, 5-minute fuse.**
- **FINDING 3 — L2/M2 is the leg's dominant real failure, and it is now a number.** Live log,
  denominator printed: **169 passes / 110 OK / 59 IDENTITY-FAIL (34.9%)**, 6 windows, longest **26
  consecutive passes ~= 130 minutes**, overnight. Nothing lost (cursor discipline), everything
  delayed. The design's "the next 5-minute fire retries" is true and reads as though the exposure
  were five minutes.
- **F-2 is recorded FAIL**, not PASS-with-a-footnote: three of four legs hold the expensive-direction
  property, L4 is unexercisable by construction (F-0 holds the wiring), and **L2/M3 was exercised and
  does not hold it.** A FAIL with a named remedy is worth more than a PASS with an asterisk.

## Open / next

- **APPLY A** (Lambda, 9 commits / 8 deployable) and **APPLY B** (gateway, 3 commits) — request
  written at `deliverables/laneZ_APPLY_REQUEST_20260821_ticket_center_and_gateway.md`, routed to
  `1.0.0_SA_CTO~Z`. Both need Andrew's word; Rule 26 puts the apply on this device.
- **F-3** stays UNCOMPUTABLE-BY-CONSTRUCTION — the wiring is held by F-0.
- **The Finding-1 repair** is a decision for the gate owner, not an initiative for this seat.
