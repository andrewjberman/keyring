# Andrew-direct — OPAL_ANALYST atom-decomp completion program (2026-08-11 ~1020Z, MSTR~Z terminal)

Channel: direct at the 0.0.0_AB_MSTR~Z terminal. VERBATIM (the phrasing IS the ruling):

> "alright let's get this thing back online, bring your fabric on, just 0.5.0_AE_OpalETL~Z and
> CTO~Z and CVO~Z. The premise of how I want to finish the work 0.5.0 was doing on the BG agent
> yesterday is as follows. CVO~Z validates and provides the relevant semantics that I would have
> done, I think it's fairly obvious what they'd be, and for the first run only on "Model
> Portfolios" i want CVO~Z to run atom_decomp on that so that we validate every little thing.
> Moving forward from there, 0.5.0 runs atom decomp page by page, generates the outputs, hands
> it off to CVO~Z to provide the semantics, and they go back and forth like that until the whole
> Portal is done. Then we just need to develop some cool trend-based analyses concepts for the
> news, when we get to that have CVO~Z come up with some concepts for that. The news definitely
> has to be atom_decomped and validated closely because theres some archival/unused stuff laying
> around that we still have to clean up. Once all that is done, need to get the yaml rigged up
> properly and the tools set up with relevant tags/fuzzy match for user queries. also will want
> to review guardrails. also might as well bring COO~Z on too with a drive loop just to check on
> the fabric every 10m and make sure this gets done. Last thing, before you do all of this, I
> want you to run a /git-pull because there is a lot of work that was done on the main fabric
> last night and one of the cooler features that would come in handy here would be the
> machine-readable deliverable that we are making mandatory with all TOs. So after you do the
> git pull and relay all of this to CTO (so they can make a PRD of it all) it should be made
> clear that all these TOs that are issued to 0.5.0_AE_OpalETL~Z should have that
> machine-readable deliverable attached so we know everything is done completely and
> comprehensively. Ok go."

## Operative decomposition (MSTR~Z read; CTO~Z owns the PRD)

1. **Fabric up:** 0.5.0_AE_OpalETL~Z + 1.0.0_SA_CTO~Z + 3.0.0_SA_CVO~Z; COO~Z also, carrying a
   **/drive loop @10m** scoped to this program (Andrew-authorized here — the scoped re-arm his
   standing zero-crons law requires; stop condition: program complete or Andrew stands down).
2. **Semantics authority delegated:** CVO~Z provides the semantics Andrew would have provided
   (his word: "fairly obvious what they'd be") and validates.
3. **First run — Model Portfolios ONLY: CVO~Z itself runs atom_decomp** on MP so every little
   thing is validated (this validates both the MP vertical and the atom_decomp method).
4. **Steady-state loop:** 0.5.0 runs atom_decomp PAGE BY PAGE, generates outputs, hands to
   CVO~Z for semantics; back-and-forth until the WHOLE PORTAL is done.
5. **News:** must be atom_decomped and validated CLOSELY (known archival/unused residue to
   clean up — cf. the 08-10 census F2: 720 orphaned history keys, dead drilldown leg). When
   reached, CVO~Z develops trend-based analyses CONCEPTS for the news.
6. **Then:** the yaml (tool-call registry) rigged up properly; tools set up with relevant
   tags/fuzzy match for user queries; guardrails review.
7. **TO contract:** every TO issued to 0.5.0_AE_OpalETL~Z under this program carries the
   machine-readable deliverable (proof-of-spec, standing law @ the 08-11 laptop ratification;
   stage-8 lint wired on site Z this session) — "so we know everything is done completely and
   comprehensively."

Pre-work completed before spawns: /git-pull run (SITEZ ff + origin/CLOUD merged @b8e9f8a3aa);
proof-of-spec installer executed (stage 8 live on this box).
