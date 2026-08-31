# 1.0.0_SA_CTO~Z -- D12 + D7 from cold scoping to a live build lane, and four errors of my own (1800-2355Z)

**archetype:** IMPLEMENT
**secondary_archetypes:** DIAGNOSE, COORDINATE

**Seat:** `1.0.0_SA_CTO~Z` (lane ~Z; base folder -- no `1.0.0_SA_CTO~Z/` folder exists)
**Window:** 2026-08-31 ~18:00Z -> 23:55Z. Prior log `a6ef263f57` covered 1737-1800Z (startup).
**Device:** site Z, 4 seats by close (MSTR~Z, CTO~Z, COO~Z, AE_CloudOps~Z).

---

## Summary

Andrew placed three jobs here and narrowed them to D12 first, D7 staged, D4 later. Both active jobs
went from unscoped to a **live build lane** inside the window: purpose-level PRDs, an architecture
gate ruled, stage-3 decomps by COO~Z, placement ruled and set, first TO cut, lane seated. I also made
four errors, one of which reached Andrew as a false claim.

---

## Andrew-direct instructions received (7 in the window)

All recorded verbatim; two carry durable records committed under this seat.

| ~Time | VERBATIM (or first clause) | Recorded |
|---|---|---|
| 22:0xZ | "Have MSTR~Z run the pull, then start the vNext read ... D12 first and foremost, and D7 in parallel somewhat staged behind ... sitez will own it" | relayed 17151 |
| 23:15Z | "All recs approved" + SES / DNS-DKIM-DMARC / 2FA-on-my-account | **`efcfa8cc5b`** |
| 23:3xZ | "We can do it from auth.opalinvest.com" -> reversed to **"I think it's better we handle this from opalinvest.dev"** | `5ea66f3a4c` |
| 23:4xZ | "use the same dmarcian mailbox as .com" -> **reversed** below | superseded |
| 23:5xZ | "I want our system for this op to be independent and in our control" | `db29f8a2e5` |
| 23:5xZ | **"D12 first."** | `db29f8a2e5` (Part C) |

⛔ **TWO OF HIS INSTRUCTIONS REVERSED EARLIER ONES OF HIS OWN WITHIN THE HOUR** (the sending domain,
then the DMARC target). Both handled as *the later word binds*, with the superseded one preserved
rather than deleted. Neither is a contradiction -- he reversed himself on new information both times.

---

## Delivered

| Artifact | Commit |
|---|---|
| `docs/architecture/D12_PLATFORM_OPS_PRD.md` (207 lines) | `2da36986f6` |
| `docs/architecture/D7_TICKET_VNEXT_PRD.md` (194 lines) | `c2837692bc` |
| D12 PRD Amendment 1 -- his ruling + the arch-gate | `5ea66f3a4c` |
| Andrew-direct record (Parts A/B/C) | `efcfa8cc5b`, appended `db29f8a2e5` |
| D12 cells 2.3 + 2.4 findings | `db29f8a2e5` |
| `seed-etf-constituents` recovery patch + README | `7a1269f198` |

**ARCH-GATE RULED (D12 cell 2.0, under the PRD's own CTO gate): BUILD IN `auth-handler`.**
Cognito rejected -- the bespoke RS256 token is read by ~8 surfaces including 2 at the CDN edge, and
Cognito changes issuer and shape for all of them to add a challenge in front of a working session
flow. **Entra rejected on POPULATION, not merit** -- the estate runs it with MFA built in, but portal
users are partner-firm clients outside Opal's tenant. Bound stated: 8 is a count of consumer
SURFACES, not a traced migration cost.

---

## Findings that changed scope

- **D12 smaller than the memo:** `POST/GET /auth/admin/users` **already exist**. "We should not be
  only adding accounts through the back-end" is a front-end + authorization gap, not a missing API.
- **D12 bigger than the memo:** MFA is **entirely greenfield**. `PORTAL_AUTHHARD` WS-3 was specified
  and never built.
- **D12 smaller again:** `ADVI_PRVSYS` already specifies the scoped admin page AND the exact control
  (`firmRole=admin` gates page AND API). Found by COO~Z doing stage 3.
- **`firmRole=admin` already exists** across 4 auth-stack surfaces -- WS-5's design cell became an
  adoption cell.
- **D7 smaller than the memo:** **3 of the 5** notification behaviours already ship; messaging has
  append-only prior art with caps.
- **SES:** production access GRANTED and healthy -- his premise measured, not assumed. One flag: the
  granted use case names recipients as "Opal personnel"; client OTP sits outside it.
- ⛔ **`opalinvest.com` SPF consumes 9 of 10 DNS lookups.** One vendor-side nested include tips it to
  `permerror`, failing SPF for **all** mail on that domain. Standing fragility independent of D12,
  and the sharpest form of Andrew's own stated risk factor.
- **`opalinvest.dev`:** DKIM healthy; **SPF, DMARC and MAIL FROM all absent** (true absences -- zone
  live on Route53, DKIM CNAME resolves, bogus token does not). Registrar GoDaddy per RDAP; **the
  nameservers are ours**, so all three records are self-service.
- ⭐ **Same-domain DMARC `rua` needs no third-party authorization record** (RFC 7489 s7.1). That
  mechanism -- not a preference -- is what satisfies his independence ruling.

---

## Compiler Tools

| tool | why | result |
|---|---|---|
| `comp-find` | ticket + auth surface location, MFA census | PASS (after the rail correctly gated two raw greps) |
| `comp-which` | ticket-system router | PARTIAL -- near-tie, took its own advice to comp-find |
| `comp-estate` | ticket thread | FAIL -- `ticket` is not a vertical; `ticketing` is |
| `.tools/aws sesv2 / route53 / route53domains` | cells 2.3 + 2.4 | PASS |
| `.tools/to-check.py` | TO rosters | see Gap found |
| `safe-commit.sh` | 6 commits | PASS; one lane REFUSAL, correctly not overridden |

**What worked:** carrying positive controls beside every zero. `aws_s3_bucket 0` against
`aws_dynamodb 8`; role-branching `0` against `ticket 55`; a bogus DKIM token that correctly failed to
resolve. Each turned a bare zero into a finding.

**What failed:** see Errors. Also `comp-estate ticket` (wrong vertical name) and a PowerShell probe
that invoked the bash `aws` shim in a pipeline and printed a false "DKIM CNAME did NOT resolve" -- a
broken probe I caught before reporting.

**Gap found:** `.tools/to-check.py --assignee` **substring-matches the ISSUER as well as the
assignee** -- found by `2.0.0_SA_COO~Z`, independently reproduced on the laptop. One question yielded
18/12, 17/11 and 10/5 on three instruments. **Unowned.** (My separate `--project` claim was FALSE --
see Errors.)

---

## Errors -- four, all mine, all corrected in-window

1. ⛔ **FALSE DEFECT REPORT: I claimed `to-check --project` does not filter. It does.** I had piped
   three runs through `tail`, and the tool appends an **unfiltered** trailing block to every run, so
   the tails matched while the filtered bodies differed. **I broke Rule 21 ("never `head` ANY census")
   and my own banked memory, while quoting that rule to other seats the same night.** Reached four
   surfaces including Andrew. Contained by `0.0.0_AB_MSTR~Z` **testing rather than relaying** and by
   `2.0.0_SA_COO~Z` never having used a TO count. Withdrawn in full; banked with the new form (a tail
   can MANUFACTURE a finding, not only hide one).
2. **ACKed msg 17178 from an id inferred by sequence, before opening it.** Right by luck. Disclosed.
3. **Overstated the blast radius of (2)** -- claimed I had polluted an instrument COO~Z was using,
   having measured nothing about whose rows were in whose result set. It could not have. Corrected by
   that seat.
4. **Repeated MSTR~Z's "REGRESSION" framing** about the nerves graph without measuring which capture
   matched its corpus.

⭐ **The common shape, and it is not about tools: a conclusion asserted one rung past what was
measured, travelling well because it was stated cleanly.** (2)-(4) all ran in the *self-critical*
direction, which is the direction nobody challenges. Banked check: **an unflattering claim gets the
same evidence bar as a flattering one**, and the tell is an ADJACENCY doing the work of a causal link.

---

## Blockers

**None at this seat.** Two items are gated elsewhere and named rather than assumed:
- **WS-2 acceptance** is not satisfiable until three DNS records exist -- specified, routed to
  `0.7.0_AE_CloudOps~Z`, AE-lane infra under Rule 13. Not blocked on work, only on that lane's turn.
- **D7** is PARKED by his "D12 first."

---

## Current State (for a reader with zero prior context)

- **Fabric:** site Z, 4 seats -- `0.0.0_AB_MSTR~Z`, `1.0.0_SA_CTO~Z`, `2.0.0_SA_COO~Z`,
  `0.7.0_AE_CloudOps~Z`. `3.0.0_SA_CVO~Z` still DEAD; surprise channel routes to MSTR~Z. Zero crons.
- **D12 EXECUTING.** Placed SITE Z (`18ec6d3f04`). Stage 2 + 3 done. `0.7.0_AE_CloudOps~Z` live on TO
  W1 (identity record + migration + email OTP leg). Arch-gate ruled, so WS-1 is unblocked.
- **D7 PARKED** by his ruling. Placed SITE Z, restated whole (its old placement string described the
  PRIOR ticketing workstreams and would have put half of vNext on the laptop).
- **D4** untouched. His transcript settles it: D4 gets **repurposed** to asset-class nomenclature once
  satellites closes -- five classes, canonical order, colours assigned. Register act, not started.
- **Push state:** `origin/SITEZ` at `db29f8a2e5` when last read; later commits are the integrator's
  leg. **Perishable.**

---

## Next Steps

- **[ANDREW]** SES use-case amendment (client OTP outside the granted declaration); `opalinvest.dev`
  **expires 2026-12-22** and renewal needs GoDaddy access; the `<=92` disposition; whether the
  08-25 sweep predicate can fire again; whole-register placement for D0-D6 / D8-D11.
- **[`0.7.0_AE_CloudOps~Z`]** the three DNS records (SPF / DMARC same-domain `rua` / custom MAIL
  FROM) in Route53 zone `Z054626637UVVD9T5GO6`, via terraform + safe-apply. **Report collection is a
  CHOICE, not a default -- surface it, do not build it unasked. No monitor either way.**
- **[`1.0.0_SA_CTO~Z`]** score **AC4** on `gold/holding/date=2026-08-31` after the **2026-09-01T13:00Z**
  fire (~13h out); `0.0.0_AB_MSTR` (laptop) holds named fallback. Needs no peer.
- **[open, unowned]** the `to-check --assignee` issuer-matching defect.
