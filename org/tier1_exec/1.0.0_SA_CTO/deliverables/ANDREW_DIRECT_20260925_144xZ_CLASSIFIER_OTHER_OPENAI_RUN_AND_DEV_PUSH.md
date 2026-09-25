# ANDREW-DIRECT 2026-09-25 ~14:4xZ -- held-away assets are "Other"; one OpenAI classification run; ~D's round 3 pushed to portal DEV

**Channel:** the 1.0.0_SA_CTO terminal. **Recorded by:** 1.0.0_SA_CTO, same turn. Sources:
- 2.0.0_SA_COO~M msg 100934: `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/CLASSIFIER_WIDENING_REQUEST_20260924.md`
  @`d8a88cef4b`, decisions 1-2;
- 2.0.0_SA_COO~D msg 100940: the round-3 candidate on portal DEV, `13b5356f..8242412d`.

## The questions and answers, verbatim

1. **Held-away assets.**
   - Asked: "Classifier, held-away assets: Cottonwood's $78M of unclassified holdings is mostly held-away and manual
     assets, e.g. Voya $26M, a client's home ($8.4M), a private LP ($6.2M). Should these get an asset class?"
   - Options: "Yes, add Real estate + Other (Recommended)", "No, label them held-away".
   - **Answer:** "Real estate is alternative, but only if investment oriented (e.g. a reit), personal and held away is
     all "Other""
2. **The OpenAI run.**
   - Asked: "Classifier run: the existing way to classify new securities calls OpenAI (vendor egress). May ~M run it
     once over the ~287 named unclassified securities (Cottonwood 101, 49F 78, Inflection 108)? The 49F ones first get
     their names from the Schwab security master."
   - **Answer:** "Yes, one run (Recommended)"
3. **The DEV push.**
   - Asked: "Push ~D's round-3 UI work (83 files) to the shared DEV branch? It includes the search box and paged client
     list, model and asset-class colours (cash now green, Positioning included), the header Export, the sample view,
     and the progressive-disclosure rule. Nothing goes to PROD."
   - **Answer:** "Yes, push to DEV (Recommended)"

## What it binds

- **Classification rule.**
  - Investment-oriented real estate (a REIT, for example) is `alternatives`.
  - Personal and held-away assets (a client's home, a manual asset, held-away holdings) are ALL a new class "Other"
    (`other`), which matches the `other` Positioning's `ASSET_CLASS` already has.
  - No separate real-estate class is added.
  - The classifier's enum gains `other`, and the portal colours it through the existing Positioning mapping.
- **One vendor call.** ONE OpenAI classification run (B_01b's method, secret `openai-api-key`) over the named
  unclassified rows only (COT 101, 49F 78, INF 108 distinct, after the 49F symbol and name fill).
  - This is a per-use word: no standing egress, no second run.
  - The results change the class every reader sees, Positioning included. The write to `bd-securities` therefore
    comes to the CTO as a never-widen half naming the flipped securities and their readers before it lands.
- **The DEV push.** 0.0.0_AB_MSTR fast-forwards portal DEV `13b5356f..8242412d`, with VALGATE on the push. DEV only;
  PROD stays on Andrew's word. The CTO's review found every file outside `pages/InvestorReporting/**` inside PRD v0.7
  PATHS.
