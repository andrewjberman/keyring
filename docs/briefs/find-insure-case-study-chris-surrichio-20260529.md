# FIND_INSURE — End-to-End Case Study: Chris Surrichio (Lincoln Investment)

**For:** Sales walkthrough — how the enrichment process turns a company name into a fully-qualified, warm-ready prospect, using only free + low-cost public sources.
**Date:** 2026-05-29

---

## The punchline

Starting from nothing but a list of insurance/IMO company names, we ended up with a **named, ranked, fully-credentialed prospect** — title, direct contact info, professional credentials, and verified regulatory licenses — at **near-zero cost**. Chris Surrichio was our first end-to-end proof.

**Who he is:** Chris Surrichio — VP of Investment Management & Research at **Lincoln Investment** (Fort Washington, PA). CFA charterholder. FINRA-registered with Series 7, 24, and more. FINRA CRD #2473601.

---

## The process — step by step (this is the part to walk through)

### Step 1 — Start with the company (web scrape)
We scraped Lincoln Investment's public website and classified the language on it. The site is dense with the signals we care about — it reads like a real advisory/asset-management firm, not a pure insurance-marketing shop:
- **Investment-management / advisory language** is everywhere: "Financial Planning, Investment Management, Mutual Funds, Individual Securities," advisory services, asset allocation, model portfolios.
- It explicitly states it operates **"through Lincoln Investment Broker-Dealer, Member FINRA / SIPC"** — a registered broker-dealer.
- It names a **Chief Investment Officer** (Shashi Mehrotra) and a Deputy CIO — a genuine investment operation.
- The site even advertises licensed staff ("FINRA Series 6, 7, 24, 26, and 63 registered").

**Takeaway for sales:** the website language alone tells you whether a firm is an actual asset manager or just an annuity marketer. Lincoln scored heavy on advisory + fiduciary + core-asset-management language.

### Step 2 — Pull the org chart (Lusha)
We pulled Lincoln's leadership roster from Lusha — names, titles, departments. Chris surfaced as **VP of Investment Management & Research** (Finance department, senior). This is how we go from "a company" to "the specific decision-relevant people."

### Step 3 — Get the contact info (Lusha contact-reveal)
One reveal call returned Chris's **direct phone and email**, plus his LinkedIn profile URL. (Across our first 25 contacts: 100% had a phone, 88% had an email — ~6 cents-worth of credits per contact.)

### Step 4 — Enrich the person (Bright Data — LinkedIn profile)
A LinkedIn profile scrape filled in the human picture:
- **CFA charterholder** — CFA Institute, issued Aug 2024, verifiable credential (ID 113018247).
- An **active, on-topic LinkedIn presence** — he engages with Lincoln Investment's own content (advisor-independence, the firm's $60B+ in client assets, executive appointments), comments at industry events. He's a real, engaged investment professional, not a dormant profile.
- His "people also viewed" network is wall-to-wall investment/wealth professionals (Goldman, Merrill, BBR Partners) — confirming the domain.

### Step 5 — Verify the licenses (FINRA BrokerCheck — FREE)
This is the one that makes the prospect *real*. FINRA's public BrokerCheck confirmed Chris's actual securities registrations — **at zero cost**:
- **Series 7** (General Securities Representative)
- **Series 24** (General Securities Principal — i.e., he's a supervisor/principal, not just a rep)
- **Series 6, Series 6TO, Series 87, SIE**
- CRD #2473601 — a real, verifiable regulatory identity.

We match on **firm + name together**, so it's genuinely him at Lincoln, not a same-name coincidence.

**At the company level too:** Lincoln Investment is registered as **both** an SEC investment adviser (RIA) **and** a FINRA broker-dealer (BD) — the mark of a real, regulated investment firm.

---

## How Lincoln stacked up against the field

We ranked 24 insurance/IMO companies by how much they look like real asset-management-transition firms.

- **Before** the FINRA licensing data was layered in, scores were compressed and hard to separate — Lincoln sat mid-pack (~#4, score 0.33).
- **After** we activated the FINRA series-license signal, the rankings separated cleanly and Lincoln jumped to **0.79 — #2 in the field** (behind only PMA at 0.86), with **26 licensed reps** identified.
- The pure-annuity-marketing firms with zero licensed reps stayed at the bottom (~0.25) — correctly flagged as *not* asset-management targets.

**The point:** the licensing data is what separates a real investment firm (licensed professionals you can sell to) from an insurance-marketing org. Lincoln is firmly in the first group.

**One honest note on size:** Lincoln's SEC-registered RIA reports ~**$22B** in regulatory assets (≈$60B in total client assets under representation, per their own materials; ~1,200 advisory staff, 1,000+ financial professionals). That's a large, established firm — bigger than our ideal target band — but it's the cleanest illustration of the full process end-to-end.

---

## Why this matters (the sales pitch)

From a **company name** we produced, automatically and for pennies:
1. Whether the firm is a real asset manager (site language + SEC/FINRA registration),
2. The **specific people** who matter (org chart),
3. Their **direct contact info** (phone, email, LinkedIn),
4. Their **professional credentials** (CFA),
5. Their **verified securities licenses** (FINRA Series 7/24/etc. — confirming they're a licensed investment professional, not an admin),
6. A **relevance ranking** so you call the best firms first.

Three of those five enrichment sources (web scrape, FINRA BrokerCheck firm + individual, SEC Form ADV) are **completely free**. Lusha (org chart + contact reveal) is the only paid piece, and it's cheap. No expensive data subscription required.

---

### Quick-reference card — Chris Surrichio
| | |
|---|---|
| Name / Title | Chris Surrichio — VP, Investment Management & Research |
| Firm | Lincoln Investment (Fort Washington, PA) |
| Firm type | SEC RIA + FINRA BD; ~$22B reg. AUM (~$60B client assets) |
| FINRA CRD | 2473601 |
| Series licenses | 7, 24 (principal), 6, 6TO, 87, SIE |
| Credential | CFA Charterholder (Aug 2024) |
| Contact | Direct phone + email on file; LinkedIn confirmed |
| Firm rank | #2 of 24 (0.79) after licensing signal applied |
