# ANDREW_DIRECT 2026-10-08 ~22:0xZ -- the laptop's one Codex applier may hold apply orders on every project

**Channel:** laptop terminal, to 1.0.0_SA_CTO. **Recorded by:** 1.0.0_SA_CTO, same turn.

**Asked** (on 3.0.0_SA_CVO's verdict msg 107388, "(a) NARROWED"): "Should the laptop's single Codex deploy agent
(0.7.0_AE_CloudOps) be allowed to keep handling deploy jobs for every project, as a permanent exception? Normally an agent at its
level works on only one project." REC yes. Second card: the Black Diamond client report he was recorded as sending dell2.

**Andrew, verbatim:** "1.) Yes. 2.) Dont know what this is"

**Placement:**
1. A standing, named exception to CLAUDE.md rule 27's one-project seating (`.tools/to-decomp-ref-lint.py` gate2): the laptop's
   apply seat `0.7.0_AE_CloudOps` may hold apply task orders on any project; each order names its project and its never-widen
   pair on its face. gate2's WARN on those orders is the known, owned consequence. No other Tier-2 seat is covered.
2. He does not recognise the BD Taildrop item; it is explained to him (record `38c34d7821`, dell2, 2026-10-07), not closed.

## Addendum ~22:0xZ -- every box deploys through its own CloudOps seat

Verbatim, same terminal, minutes later:

> "Regarding item 1, the dells need to be able to deploy. It is far more logical for the dell boxes and sitez box to simply spawn
> 0.7.0_AE_CloudOps on their own box to handle deploys through the customary pattern versus having to reroute deploys over here
> because then it holds up their whole workflow and then it pushes too much activity on the laptop and bottlenecks the work that
> is already driving on here as well as bottlenecks whole other boxes."

**Placement:**
1. Each box's manager seats its own `0.7.0_AE_CloudOps~<box>` lane (site Z, dell1, dell2); a box's COOs cut apply orders to their own
   box's CloudOps seat. The laptop's `0.7.0_AE_CloudOps` applies laptop-placed projects only. The item-1 exception above stands for
   the laptop seat within that scope.
2. Where a Dell's identity still refuses a deploy (today: IAM writes, item 4, cell 3 not cut; dell1 denied `ssm:GetParameter` on
   `/mdpf/custody_source`, so it cannot plan mdpf-pipeline), the control plane cuts the grant cell; the laptop applies for a Dell only
   until that grant lands, and only for that refusal.
3. Orders already GO'd tonight (MDPF_STRATID.TO-APPLY-D2, IRPT_BCKEND.TO-APPLY-Y68, NFRA_CTLPLN.TO-APPLY-18 leg C) finish where cut.
