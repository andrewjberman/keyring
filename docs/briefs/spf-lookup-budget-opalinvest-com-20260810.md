# Brief: `opalinvest.com` SPF lookup budget — 8 of 10 spent, vendors control the spend

**Author:** 4.0.0_SA_CRO~Z · **Date:** 2026-08-10 · **Trigger:** Andrew question during the website mail-failure review (companion: `org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/WEBSITE_MAIL_ASSESSMENT_20260810.md`)
**Status:** FINDING + recommendation. No change made; no change is authorized by this brief. Any edit to this record touches live firm mail (M365) and is Andrew-gated per `infra/website/RUNBOOK.md` §"GRADUATE".

## The mechanism (why there is a budget at all)

RFC 7208 imposes two distinct limits, both terminating in the same failure:

1. **Exactly ONE SPF TXT record per domain.** Two or more (an *appended* record) = `permerror`: receivers evaluate none of them — the domain has no SPF at all. This is the known single-record hazard the RUNBOOK already fences.
2. **At most 10 DNS lookups per evaluation.** Every `include:`, `a`, `mx`, `redirect` counts, **recursively** — a vendor's include costs itself plus its whole subtree. Lookup #11 = `permerror`, same consequence.

`permerror` is silent: no bounce to us, no console warning — mail just starts failing SPF firm-wide, and with DMARC `p=none` it presents only as degraded deliverability/spam-foldering.

## The measured state (live DNS expansion, 2026-08-10)

```
opalinvest.com  v=spf1 ...                                   lookups
├─ include:_spf.mlsend.com        (MailerLite)                 1   flat IPs, terminal
├─ include:mailgun.org                                         2
│   ├─ include:_spf.mailgun.org                                3
│   │   ├─ include:_spf1.mailgun.org                           4   terminal
│   │   └─ include:_spf2.mailgun.org                           5   terminal
│   └─ include:_spf.eu.mailgun.org                             6   terminal
├─ include:spfa.cpmails.com                                    7   terminal
└─ include:spf.protection.outlook.com  (Microsoft 365)         8   terminal
                                                     TOTAL: 8 / 10
```

## The finding, stated precisely

- **We are at 8/10, not 10/10.** One more flat include (SMTP2Go = 1, `amazonses.com` = 1) would land at 9/10 and would NOT break email the day it is added.
- **But the margin is not ours to rely on.** 4 of the 8 lookups are Mailgun's internal subtree; all sub-includes are vendor-controlled and change without notice. At 9/10, ONE vendor adding ONE nested include pushes the domain to `permerror` with nobody having touched our DNS — a break with no local cause, no warning, and a failure mode (silent spam-foldering) that takes days to notice.
- **The two limits compound:** the correct response to "record is near budget" is never "publish a second record" — that is the instant version of the same permerror.

## Recommendation (owner: Andrew decision; executor: whoever holds GoDaddy DNS, per `infra/website/GODADDY_DNS_REQUEST_opalinvest.md` discipline)

1. **Reclaim before adding.** Audit whether Mailgun (4 lookups), cpmails (1), and MailerLite (1) still send for the firm. The old website's Mailgun SMTP config was found dead/empty at migration (RUNBOOK §4a) — if nothing else sends via Mailgun, removing its include frees 4 slots (8 → 4). Each unused include is also a standing third-party authorization to send as `opalinvest.com` — attack surface, not just budget.
2. **Sequence the SES graduation against this.** The planned `no-reply@opalinvest.com` graduation needs `include:amazonses.com` (1 lookup). At today's 8/10 it fits; after any other vendor add it may not. Do the reclaim audit first.
3. **Verification discipline for ANY edit:** one record, edited never appended; afterwards send a test and read `spf=pass` + `dkim=pass` + `dmarc=pass` in received headers (config-read is not an exercise).
4. **No monitor is to be built for this** (alarm moratorium, Andrew-direct 2026-07-28). The control is the pre-change audit + this brief as the recorded ceiling, re-measured (`nslookup -type=TXT`, expand includes, count) before any SPF-touching change.

## Non-scope

The website contact form is unaffected: it sends as `noreply@opalinvest.dev`, a separate domain with its own SPF record and budget. This ceiling binds only senders-as-`opalinvest.com`.
