# Andrew-direct 2026-09-15 ~05:04Z at the 2.0.0_SA_COO~W terminal -- "key management" = executive managers; a Lusha integration for their LinkedIn data; opal-data-harvest as the pool every frontend and external workflow runs off

**Recorded by:** `2.0.0_SA_COO~W` | **Project:** AMGT_RESAPP (D5) | **Round at the time:** 10, EXECUTING (ri-1, ri-2, ri-4 drained; ri-3 closing)
**Class:** DIRECTION-IN-FORMATION, given in conversation while reading the data-plane diagram of Adam Muller's five asks. Relayed verbatim; nothing here is a cell, an outcome id, or an egress word until the owning limb lands it.

## Verbatim

> "I think there is another part in here we may want to add to the mix. Key management i would define as executive managers. I think we should build in a lusha integration here to pull linkedin data for these people as well. My goal is to essentially pool all teh relevant data in this opal-data-harvest bucket and then we can build whatever frontend and external workflows that run off that data."

## What it touches, read narrowly

1. **Adam's limb 5** ("a bio of key management, usually the CEO", email 2026-09-10T13:18Z) is REDEFINED by Andrew as **executive managers** -- the named executive officers of a covered company, not the CEO alone. That is a scope statement on the L2 endpoint's territory; no FWD carries it today (FWD-1..FWD-15 at PRD @HEAD). Landing it is `1.0.0_SA_CTO~W`'s (an L10 addendum or a new outcome; FWD ids are permanent, the next unused number is the CTO's to assign).
2. **A Lusha integration** to pull LinkedIn-side data (profile URL, title, seniority, tenure as Lusha carries them) for those people. Lusha is an EXTERNAL VENDOR API: CLAUDE.md's vendor-egress rule means this sentence is DESIGN INTENT, not the per-use word; the per-use word for the first pull, the account/key to use, and the field set to persist are Andrew's to state before any seat calls it.
3. **The pool:** `s3://opal-data-harvest` (versioned, no lifecycle) is named as the system of record that every frontend and external workflow reads. Today it already holds `raw/bloomberg/`, `raw/seekingalpha/`, `publications/v1`, `publication-links/v1`, `derived/model_block/`, `derived/model_block_fye/`, `packs/<key>/` (one page of 61 keys read 2026-09-15 04:5xZ); the two DynamoDB tables (`opal-harvest-articles`, `opal-harvest-security-metrics`) are indexes and daily derivations beside it, not a second pool. A Lusha lane fits the existing grammar as `raw/lusha/<security_key>/...` (the vendor's own response, untouched) and `derived/management/<security_key>.json` (the executive roster with provenance), which is `C-RAW-BEFORE-DERIVED` as the PRD already binds it.

## Where it goes, and who owns each part

| part | owner | carrier |
|---|---|---|
| the outcome (executive managers as a limb; its DONE WHEN / ACCEPT) | `1.0.0_SA_CTO~W` (L2/L4) | PRD addendum at the round-10 L10, or a new brief limb via `4.0.0_SA_CRO~W` |
| the substrate (Lusha account, key, egress word, field set, retention) | Andrew | his per-use word; a substrate card (Rule 28) before any cell builds on it. MEASURED in the estate: a Lusha key ALREADY EXISTS in Secrets Manager under `find-insure/lusha-ai/*` (the find-insure project's; `.claude/skills/cloud-ops/SKILL.md:289`), so the account is not the gap -- whether AMGT reuses that key or gets a research-scoped copy is Andrew's call, and availability is not authorization |
| the collection lane (raw pull into `raw/lusha/`, one canonical record per person identity, idempotent, readback) | `4.0.0_SA_CRO~W`'s harvest estate (PRD s.8) | the same loop discipline Andrew set at ~04:3xZ for articles |
| the roster identity (which humans ARE the executives of `<security_key>`) | S12 identity layer | Bloomberg management fields and the filings class are the candidate rosters; Lusha enriches a resolved person, it does not decide who the executives are |
| the page and the print pack (a management block beside the model block; the bio limb of Adam's pack) | round 11+ cells, this seat's cut | after the CTO's round-10 analysis |

## What this record does NOT do

It cuts no cell (round 10 is mid-flight and the decomposition is frozen), calls no vendor, creates no prefix in the bucket, and assigns no FWD number. Push state of this file: LOCAL.
