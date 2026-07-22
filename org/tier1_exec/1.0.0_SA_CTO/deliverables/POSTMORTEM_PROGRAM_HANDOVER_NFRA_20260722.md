# POSTMORTEM PROGRAM HANDOVER -- MDPF postmortem items -> NFRA group (~Z) + 0.8.0_AE

**Authority (Andrew-direct, VERBATIM, at the 1.0.0_SA_CTO terminal, 2026-07-22 ~22:0xZ):**

> "Yes all the postmortem stuff should be handled by ~Z lane and 0.8.0_AE, hand those various
> items for that over to them now"

Context: MSTR's MDPF postmortem (circulated by Andrew this session) + CTO's assessment and
5-item proposal, discussed with Andrew in-session immediately prior. Scope of this handover =
the POSTMORTEM PROGRAM (estate infrastructure / comp tooling / ontology / doctrine). The
MDPF_3FIRMS dispatch itself stays on the main fabric unchanged.

## The postmortem's finding, one line (context for the receiving lanes)

Every expensive MDPF defect was a structure that HARDCODED THE FIRM SET -- ~6+ independent
sites (8 counting tonight's F-1 CF flip set), each internally consistent, each green -- and
every detector we own answers AGREEMENT (drift), none answers COMPLETENESS (cardinality over
the world). comp-constants named the exact defect 2026-05-08, eleven weeks early, as a NOTE
that could stop nobody. The gap is the TRIGGER layer, not the detector count.

## Item division

### To the ~Z lane (1.0.0_SA_CTO~Z ontology lead; 3.0.0_SA_CVO~Z verification)

- **P1 -- FIRM REGISTRY as estate SSoT + enumeration-completeness gate (design/ontology half).**
  One canonical firm enumeration; a declaration convention (every firm-keyed structure in the
  estate declares itself firm-keyed); a commit-time gate asserting CARDINALITY AGAINST THE
  REGISTRY, never agreement between sites. Onboarding firm #4 must fail LOUD at commit in every
  unhandled place. Working exemplars already live (built tonight, main fabric):
  `.tools/mdpf-preflip-check` identity-1 (@8ec253b34, exercised w/ real-artifact negative
  control) and 3F-G2's Control-5 synthetic-firm spec. The build halves may ride 0.8.0 or main
  lanes at ~Z's discretion; the DESIGN + registry placement decision is ~Z's.
- **P2 -- ONTOLOGY FIX: firm becomes a COMPLETENESS dimension** (a set that structures must be
  complete over), not only a variance dimension for comparison. /ontology is CTO~Z's charter.
- **P3 -- TRIGGER-LAYER DOCTRINE + GATE:** *"a structural finding lands as a GATE or an OWNED
  BLOCKING ITEM -- never as a note."* Doctrine text + an enforcement mechanism (a structural
  finding from any comp-tool opens an owned/blocking item rather than a log line). This is the
  fix for the 05-08 eleven-week silence and tonight's 207h-stale danger map (an honest flag
  nobody owns is halfway to no flag).
- **CVO~Z:** independent verification of the above per the NFRA/SYSPARITY charter; the
  postmortem's own standard applies (exercised controls, printed denominators, no seeded lists).

### To 0.8.0_AE_CloudComp (joins the existing 6-item tool-gap bundle; sequencing theirs)

- **Item 7 -- comp-constants POLYGLOT + `--complete-over <registry>`.** Parse JS/TS (the
  deferred v2; the multifirm lane's sites are .mjs/.ts and the extractor is ast.parse
  Python-only) and add completeness mode: a uniformly-incomplete set is a FAILURE, not
  zero-drift. Highest leverage-to-cost in the estate -- the tool already found the firm-map
  defect once with no help. Interface: `--complete-over` binds to ~Z's P1 registry when it
  lands; build the flag against a stub registry meanwhile.
- **Item 8 -- comp-vendor (vendor-surface census).** Enumerate what a vendor endpoint/template
  OFFERS vs what we SELECT; diff on a schedule. Seed: `dump_enriched_templates.py` (existing,
  80% of the tool) + 3F-B5's dumped template catalog (landing at
  `s3://opal-data-cot/code/bronze/templates_enriched/`). Exhibit: RF-14 (portfolio-vs-account
  template selection, four months of an empty column that read as a vendor gap).
- **Item 9 -- LAYER-GRAMMAR GATE:** assert no gold/silver producer reads from a served
  artifact. Cheap, closes a zero-coverage class (the B7 legacy-chain family; CVO's
  opal-assets-daily-aua finding).

### Explicitly NOT in this handover

- **No new detectors** (postmortem's own boundary, CTO-endorsed, Andrew-circulated).
- **MDPF_3FIRMS TOs stay main-fabric**: 3F-G2's CONSUMER RETROFITS (G2b -- the eight sites
  incl. the CF layer) remain an MDPF TO that BINDS to ~Z's registry when it lands; the
  preflip-check identity-2 gets its one-line path update then (probe locations documented in
  the script). The MDPF dispatch, gates, and flip are untouched by this handover.

## Standing constraints carried over

~Z group works off-main-channel (Andrew 07-20); spawns route via MSTR; main-channel
coordination via MSTR. LD-0333's single path governs anything main-fabric. Rule-21/22/22a
discipline as everywhere. The count-vs-throw doctrine (CONTROLS_OVER_CARE III-c) and the
deployed-vs-committed / applied-vs-declared re-check axes (PRD v1.15 note) are input reading.

-- 1.0.0_SA_CTO, 2026-07-22 ~22:1xZ, on Andrew's word above
