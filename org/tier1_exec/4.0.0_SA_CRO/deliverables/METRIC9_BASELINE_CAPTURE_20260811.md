# METRIC-9 PRODUCT-GRADE BASELINE -- CAPTURED AT DECOMPOSITION, PRE-BUILD

**Author:** 4.0.0_SA_CRO · **2026-08-11 ~0815Z** · **archetype:** VALIDATE (measurement record)
**Commission:** COO act B-8 (dispatched 080421Z on my own L-6 time-bound trigger, fired by the
build decomposition @36881fc6be). **CAPTURE != KEEP: this record preserves Andrew's option on
metric 9; the metric's disposition remains HIS** (L-6 call 5). Hand-tagged per the metric's own
definition (NFRA_VELOCITY_PROGRAM §5.9) -- "hand-tagged is fine; it is a baseline, not a gate."
**Provenance of the catch:** my L-6 trigger (030649Z) + MSTR's watch + COO's fire -- three seats,
one written record; any link missing and the baseline would have been struck by nobody.

## THE PRODUCT STATE AT CAPTURE (the "before", pinned)

Build TOs B-1..B-8 dispatched @36881fc6be this hour; **NO emitter or format change has landed**
(B-4/B-5 fresh at DS). The pre-build state: mdpf gold = the THREE-WRITER JSON form
(consolidator + accrual + aum-metrics into `portal/gold/mdpf/*.json`); the 49F production path =
the `runners_49f` corpus (a00/a01 + c00-c04); the feeds plane live at `opal-data-mdpf`
(3 cron-fed, 3 frozen-since-08-06); publisher family mid-wo2; INF chain on the allowlist +
sentinel form; capture vintage = repo @93c21ab37a-era, all cited runs certified.

## THE FOUR SERIES (measured specimens from the decomposition window, 2026-08-11 02:40-08:05Z)

**(a) Archaeology-vs-build wall-clock + agent-context.** Establishing ground truth BEFORE building
consumed the decisive share of tonight's exec hours -- and was MANDATORY, not overhead: RECON-1
(mdpf colocation, ~40min single-seat + cert) found **6 of 10 record-beliefs FALSE**; RECON-4
(~15min + 3 delta-certs); the GIPS feasibility (~15min); task-1 classification (~20min full-series);
the cot custody dig (~A, hours). Baseline marker: **pre-framework, a build could not start until a
multi-hour multi-seat archaeology pass inverted the record** -- the post-framework hypothesis under
test is that contract-at-creation makes this pass shrink toward zero.

**(b) "Which artifact is canonical / who writes this / is it live" questions.** Hand-tagged count
this window: **12 distinct canonicity questions requiring resolution**, each with its pointer --
the four-vs-two runtime paths; three-writers-one-gold-prefix; the publisher FAMILY-of-two
(wo2 egress found by CVO); the gold-root naming fork (A-vs-B); the two program-file copies; the
gold `_` vs served `-` spelling families; the mdpf_revamp staging home; the partner_roster
config-in-code home; the feeds-vs-smartx-silver duplication; the 08335338 flat-root twins; the
dead-sentinel liveness question; the "runner ran" leg conflation. **Every one cost a measurement
to resolve; none was answerable from the record alone.**

**(c) Rail-override count.** **5 audited `# rail-checked` overrides at this seat this window**
(drill-in line-site greps after comp-tool localization; device-local audit at
`org/mcp/comp-which-rail.log`), plus routine HUD advisories. Small against the fabric's 187/mo
baseline -- the comp-tool-first discipline held; the overrides were the sanctioned drill-in class.

**(d) Rework waves caused by a wrong denominator.** **5 denominator-driven rework events, all
caught by controls in-window** (the catch mechanism named per the log discipline): the day-sample
code universe (21 -> 157, forced the full-series rebuild); the 99.8% leg-label correction
(map-leg quoted as end-to-end; propagated to COO's register and corrected same-window); the
hand-stated census drift (CVO catch -> derive-from-cells rule); the len-2-4 cell (actual 2-14);
my at-rest equivalence method REFUSED (same-state pair does not exist at rest -> M1/M8 redesign).
Baseline marker: **pre-framework, every denominator was discovered at use-time; the post-framework
hypothesis is that declared contracts move these to authoring-time.**

## READING THIS BASELINE LATER

Compare the same four series at the ADVI/MDPF builds' mid-point and completion. The metric's
question is not "was tonight expensive" -- it is **"did the framework make the NEXT product faster
and cleaner"**: (a) should shrink toward contract-reads; (b) should approach zero because
canonicity is declared at creation; (c) should stay flat-or-down as coverage grows; (d) should
move from use-time catches to authoring-time refusals. **If they do not move, the framework failed
its own objective function -- which is exactly what metric 9 exists to be able to say.**
