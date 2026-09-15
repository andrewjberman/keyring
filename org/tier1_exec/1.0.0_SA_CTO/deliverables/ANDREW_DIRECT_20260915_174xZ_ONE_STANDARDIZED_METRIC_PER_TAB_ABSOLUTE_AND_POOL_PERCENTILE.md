# Andrew-direct 2026-09-15 ~17:4xZ, at the `1.0.0_SA_CTO~W` terminal: every tab centers on one standardized metric, carried as an absolute figure and a percentile within the pool; Posture's case starts from them

**Recorded by:** `1.0.0_SA_CTO~W`. **Channel:** direct message in this Claude Code session; exact arrival timestamp unavailable
(after 17:29Z by the surrounding tool reads). **Project:** AMGT_RESAPP (the `~W` fabric's only focus, Andrew ~16:3xZ @`de60858372`).

## Verbatim, entire

> Something id clarify here is that we need to standardize some kind of metric per tab. the metric will be an absolute figure but
> also a relative figure (percentile based in the pool). this gives a clear jumpoff point for the AI Rec in posture when it makes
> its case. I think average mgmt tenor (and maybe average tenor of mgmt at the co in general, even not in mgmt role) is a obvious one
> for mgmt tab. We dont necessarily need to know what all the others will be, but I think its important to design the tabs with that
> in mind, that they are going to center around a relative/absolute value on some standardized score, as that will inform frontend
> and probably also "Posture" wiring.

## Read narrowly

- **THE PRINCIPLE (ruled):** each tab of the Security Analysis page centers on a standardized metric. The metric is carried two ways:
  an ABSOLUTE figure, and a RELATIVE figure that is the company's PERCENTILE within the pool. The tabs are designed around that
  pair; it informs the frontend and, in his words, "probably also" the Posture wiring.
- **WHY (his):** the pair gives Posture's AI recommendation "a clear jumpoff point" when it makes its case.
- **THE ONE METRIC NAMED:** the Exec Management tab -- average management tenure. **Hedged ("maybe"):** average tenure of the
  company's people in general, not only those in management roles. Recorded as a candidate, not ruled.
- **NOT RULED:** the metric for Thesis, Peers, Model and Posture ("We dont necessarily need to know what all the others will be");
  the definition of "the pool" beyond the page's own usage (read here as the set of companies the page covers, the union universe
  C-UNION-UNIVERSE names and C-EXEC-MANAGEMENT already averages tenure over -- a reading, stated so it can be corrected); the
  percentile method; and whether Posture must consume the pair (his "probably").
- **WHERE IT LANDS:** AMGT_RESAPP's specification is frozen mid-round (round 11 EXECUTING). The principle becomes a PRD addendum
  contract at the round-11 L10 read -- the canonical place a design direction enters an admitted PRD -- and reaches the frontend and
  Posture cells through the round-12 cut. Whether any round-11 cell still unspawned absorbs part of it earlier is `2.0.0_SA_COO~W`'s
  call as issuer, not this record's.
- **UNCHANGED:** the ten contracts of PRD v0.8 until the addendum; the canonical flow's owners and order; PORTAL FROZEN; the site-Z
  push hold; the harvest collection reservation.

## Broadcast

One message to `2.0.0_SA_COO~W`, `3.0.0_SA_CVO~W`, `4.0.0_SA_CRO~W` and `0.0.0_AB_MSTR~Z`, quoting the word entire. Push state: LOCAL.

---

## THREE CLARIFICATIONS, minutes later at the same terminal (~17:5xZ), verbatim and entire, in order

> percentile is relative to the pool of analyzed companies in the Security Analysis database

> all of this stuff should be storeed in opal-data-harvest

> and essentially appended over time

## Read narrowly, and what they correct

- **THE POOL (ruled; SUPERSEDES this record's reading above).** The percentile is relative to the companies ANALYZED in the Security
  Analysis database -- not the 256-name union universe this record first read it as. So a metric's pool is the set of companies that
  have been through the analysis and carry that metric, and it grows as companies are analyzed. Today that is the five QA names for
  management tenure (BA, COST, HD, SAP, BABA), four of which carry a tenure.
- **THE STORE (ruled).** The metrics, their percentiles and their pools live in `s3://opal-data-harvest` -- consistent with
  C-ONE-STORE, where every Security Analysis product already lives.
- **APPEND OVER TIME (ruled).** Records are appended as analyses run, not overwritten: a company's metric history and each dated
  pool are both kept, so a percentile is always read against a named pool vintage and a company's percentile over time is readable.
- **NOT ADJUDICATED WIDER:** "all of this stuff" is read as the per-tab metrics, percentiles and pools this thread is about. The wider
  reading -- every Security Analysis output appended over time -- is recorded as plausible; measured against the pool's key shapes at
  ~17:5xZ, it already holds for `crosswalk/v1/{as_of}`, `universe/v1/{as_of}`, `filings/v1/{key}/{accession}`,
  `peers/v1/{key}/{as_of}`, `management/v1/{key}/{as_of}` and `posture/v1/{key}/{as_of}`, and does NOT hold for two keys:
  `drafting/v1/{key}.json` (no date, so a re-analysis overwrites it; bucket versioning keeps the prior bytes but not an appended record)
  and `social/v1/_measurement/{as_of}.json` (no security coordinate, row W22-S6).

---

## A FOURTH CLARIFICATION, at the same terminal (~18:0xZ), verbatim and entire

> no its not employee wide its exec-mgmt specific. also we can use lusha/linkedin too for this, even though id prioritize the filings.

## Read narrowly, and what it corrects

- **THE SECOND TENURE METRIC IS EXECUTIVE, NOT EMPLOYEE-WIDE (ruled; SUPERSEDES this record's "employee-wide" reading and the
  pre-read's `employee_tenure_avg_years`).** His first message's *"average tenor of mgmt at the co in general, even not in mgmt role"*
  means the executives' tenure AT THE COMPANY -- their total time with the company, including the years before they took the current
  management role -- beside their tenure IN the current role. So the Exec Management tab carries two executive tenure measures:
  average tenure in role, and average tenure at the company, over the same executives. It says nothing about the wider workforce.
- **SOURCES, IN HIS PRECEDENCE (ruled):** the filings first; Lusha / LinkedIn also usable. A value carries which source it came from,
  and a filing value wins where both exist.
- **UNCHANGED:** Lusha contact data (emails, phones) stays unstored and contact reveal stays off; a person's job history is not contact
  data. Whether and how many Lusha calls a cell makes is the cut's, under the session's egress word. The pool, the store and
  append-over-time stand as clarified above.
