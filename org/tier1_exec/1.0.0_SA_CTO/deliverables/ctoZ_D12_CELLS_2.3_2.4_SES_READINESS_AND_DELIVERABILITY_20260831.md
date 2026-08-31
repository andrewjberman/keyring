# D12 cells 2.3 + 2.4 -- SES readiness and email-OTP deliverability: MEASURED VERDICT

**Cells:** `2.3` SES readiness confirmed for this use · `2.4` DNS/DKIM/DMARC + service health
**Owner:** `1.0.0_SA_CTO~Z` (CTO-held per the stage-3 decomp). **Measured:** 2026-08-31 ~23:2x-23:4xZ.
**Directive:** D12 Platform Ops (SITE Z) · **Project:** `PLATFORM_OPS_USERMGMT` · **PRD:** `docs/architecture/D12_PLATFORM_OPS_PRD.md`

⛔ **2.4 IS AN ACCEPTANCE CONDITION OF WS-2, NOT A FOLLOW-UP.** A one-time code that lands in spam is a
**BROKEN LOGIN**, not a degraded one. WS-2 is not acceptable until auth mail demonstrably reaches an
ordinary inbox.
⛔ **THIS IS A DIAGNOSTIC AND A CONFIG SPEC. IT IS NOT A LICENCE TO BUILD A DELIVERABILITY MONITOR.**
Andrew's alarm hold was lifted for the ticket reminder BY NAME and for nothing else.

---

## CELL 2.3 -- SES READINESS: ✅ PASS, with one flag

**His premise, stated as fact:** *"now that its no longer sandboxed"*. **Measured rather than
assumed** -- a stated premise is still measured before it is built on.

| Property | Value |
|---|---|
| ProductionAccessEnabled | **true** |
| Review status | **GRANTED** (case 178727932800843) |
| SendingEnabled | true |
| EnforcementStatus | **HEALTHY** |
| Quota | 50,000 / 24h at 14/sec (sent last 24h: 1) |
| MailType | TRANSACTIONAL |
| Suppression | account-level on BOUNCE + COMPLAINT |

**VERDICT: the account is genuinely out of sandbox and healthy. His premise is CONFIRMED.**

⚠ **THE FLAG -- NOT A BLOCKER, AND NOT THE AE LANE'S TO RESOLVE.** Production access was granted
against a written use-case that names recipients as **"Opal personnel"** and describes exactly two
uses: internal ticket notifications and internal trade-approval transitions, at **60-300 messages/day**.
**Client-facing login codes to partner-firm end users are outside that declaration**, and a login OTP
has a different volume shape than either declared use. Still transactional, still not marketing -- but
AWS reviews production access against stated use. **An amendment is cheaper than a review.** Routed to
Andrew; no seat should silently grow sending outside the declaration and hope.

---

## CELL 2.4 -- DELIVERABILITY: ❌ FAIL AS-IS. Three records missing.

### The domain, ruled

**Andrew, ~23:3xZ, VERBATIM: *"I think it's better we handle this from opalinvest.dev"*** -- taken
after he was shown the `auth.opalinvest.com` recommendation. He had earlier said
*"We can do it from auth.opalinvest.com"* and reversed. **The later word binds.**

**Then, ~23:5xZ, the INDEPENDENCE RULING that changes the reporting design, VERBATIM:**
> *"I do not have immedaite access to the opalinvest.com godaddy. if there are services that domain is
> attached to which i commensurately also do not have access to, then i dont want to set up dmarcian or
> anything else that connects to that. I want our system for this op to be independent and in our
> control"*

⭐ **THIS SUPERSEDES HIS OWN EARLIER "use the same dmarcian mailbox as .com."** Both were his; the later
binds; and the earlier is not a contradiction -- he reversed it himself on learning the access
position. **No dmarcian. No dependency on any service reached through `opalinvest.com`.**

### State measured, with controls

| | `opalinvest.dev` (the ruled sender) | `opalinvest.com` (NOT used) |
|---|---|---|
| SES identity | ✅ VERIFIED for sending | ❌ not an identity at all |
| DKIM | ✅ SUCCESS, signing on, CNAME resolves | n/a |
| SPF | ❌ **ABSENT** | ⚠ present, **EXCLUDES** SES |
| DMARC | ❌ **ABSENT** | ⚠ `p=none` (monitor only) |
| MAIL FROM | ❌ not set (envelope is `amazonses.com`) | n/a |
| MX | none | Microsoft 365 |
| Nameservers | **AWS Route53 (ours)** | **GoDaddy (no access)** |

**CONTROLS, so the absences are findings and not failed lookups:** the `.dev` zone is live (NS records
read, Route53); its DKIM CNAME resolves to `amazonses.com` on an independent lookup while a bogus
token correctly does NOT; `opalinvest.com`'s MX resolved on the same probe that found none on `.dev`.

### ⛔ The measurement that vindicates his own risk instinct

**`opalinvest.com`'s SPF consumes 9 of the 10 permitted DNS lookups.**

```
opalinvest.com                    4 tokens
  _spf.mlsend.com                 0
  mailgun.org                     2
    _spf.mailgun.org              2
      _spf1.mailgun.org           0
      _spf2.mailgun.org           0
    _spf.eu.mailgun.org           0
  spfa.cpmails.com                1
    spfa-a.cpmails.com            0
  spf.protection.outlook.com      0
                                 --  TOTAL 9 of 10
```

His words were *"that was a risk factor adding more spf/txt mailers"*. **He was right, and it is worse
than a risk of our making:** exceeding 10 yields `permerror`, which fails SPF for **ALL** mail on the
domain -- Patricia / White Label Creative's sends and Microsoft 365 included. At 9, **a single nested
include added by any of those vendors, with no notice to Opal, tips it over.** That is a standing
fragility independent of D12 and worth telling whoever manages that domain, regardless of this work.
⭐ **Using `opalinvest.dev` consumes ZERO of those nine.** SPF is evaluated on the envelope-sender's
domain, so `.dev` carries its own independent 10-lookup budget. **His risk factor is the strongest
argument FOR the separate domain, not against it.**

### What to add -- Route53 zone `Z054626637UVVD9T5GO6`, ours

⭐ **ZERO REGISTRAR ACCESS REQUIRED.** The registrar is GoDaddy (RDAP, definitive -- not Cloudflare),
but the NAMESERVERS are already Route53 in our own account. **Registrar-vs-DNS-host is the distinction
that makes this self-service today.**

1. **SPF** -- `TXT opalinvest.dev` -> `v=spf1 include:amazonses.com ~all`
   One lookup against a **fresh** 10-budget.
2. **DMARC** -- `TXT _dmarc.opalinvest.dev` -> `v=DMARC1; p=none; rua=mailto:<addr>@opalinvest.dev`
   ⭐ **SAME-DOMAIN `rua` IS THE WHOLE POINT AND IS WHY THIS IS INDEPENDENT.** RFC 7489 §7.1 requires
   an authorization record **published by the receiving domain** only when `rua` points OUTSIDE the
   domain publishing the DMARC record. An external target (dmarcian) would need that third party to
   cooperate; **a same-domain target needs nobody.** This is the mechanism that satisfies his
   independence ruling rather than merely complying with it.
   Start `p=none` deliberately -- observe, then tighten. **Do not ship `p=reject` on day one.**
3. **CUSTOM MAIL FROM** -- SES identity setting + two records on the chosen subdomain
   `MX <mailfrom> 10 feedback-smtp.<region>.amazonses.com` and `TXT <mailfrom> v=spf1 include:amazonses.com ~all`
   Without it the envelope sender stays an `amazonses.com` subdomain, so SPF authenticates **Amazon's**
   domain and cannot ALIGN to ours. DKIM alignment alone would carry DMARC; relying on a single
   alignment path for login mail is thin.
   ⚠ **VERIFY THE REGION TOKEN AT SOURCE** -- I read SES in `us-east-1`; confirm before applying.

**Report collection (optional, and a real choice rather than a default):** SES inbound -> S3, in our
own account. Measured: **no receipt rule sets exist** (clean slate) and **`opalinvest.dev` has no MX**
(nothing to collide with). ⚠ Aggregate reports arrive as **gzipped XML** -- collecting them gives us
the data and full ownership; making them *readable* is separate work. Shipping DMARC with **no `rua`
at all** is also valid and protects the domain; it just yields no visibility. **Reports only exist from
the moment collection starts**, which argues for starting.

---

## Residual dependency -- ONE, and it is not a service

`opalinvest.dev` **EXPIRES 2026-12-22** (RDAP: registered 2025-12-22, GoDaddy, registrar locks on).
Renewal needs registrar access; **none of the work above does.** That domain is the portal auth stack's
own domain AND now the sole verified SES sending identity, so a lapse is the portal and all
transactional mail, not just OTP. Surfaced with its date; not this seat's to act on.

---

## Verdict for the WS-2 acceptance

**2.3 PASS. 2.4 FAIL AS-IS** -- three records missing, all specifiable, all self-service, none blocked
on any third party. WS-2 cannot be accepted until they exist and an OTP is observed reaching an inbox
rather than a spam folder.
⛔ **The DNS acts are AE-lane infra (Rule 13), go through terraform + safe-apply, and are NOT taken by
this seat.** Specified and routed; nothing hand-applied.
