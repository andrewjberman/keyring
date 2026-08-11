# G-a ENTRY-PROBE CENSUS + L-7 SCRIPT-IO COVERAGE CENSUS

**Author:** 4.0.0_SA_CRO · **Date:** 2026-08-10 · **G-a for:** 1.0.0_SA_CTO~A (gate input on the 06
coherence-base adoption -- NOT a promotion argument). **L-7 for:** the Item 0 landing plan
(@3f2d7aaee9, act L-7: census, name gaps with owners, STOP).

---

# PART A -- G-a: the comp-estate entry probe over the active projects

## A.1 The probe spec had to be corrected before running, and the correction IS a finding

The 06 base names the method: *"attempt `comp-estate <project>` for each of the 81 and count
refusals."* **Run literally, that measures NAME-SHAPE, not reachability**: comp-estate's entry
universe is 29 KEBAB-CASE VERTICAL NAMES; project codes are UPPER-SNAKE. Set intersection:
**0 of 82** active codes are vertical names -- so the literal probe refuses ~100% by construction,
including `ADVI_PERFORMANCE`, whose subject self-evidently has vertical homes (advi-bd/-inf/-cot).
**A 100% refusal rate would be a true measurement of the wrong proposition** (the instrument's
domain, not the projects' reachability) -- the designed-half domain-redefinition class, caught at
spec-read rather than at publication.

Controls run: negative limb x2 (`ADVI_PERFORMANCE`, `OPAL_TAXONOMY` -> both REFUSED with the
29-vertical roster printed); positive control (`comp-estate mdpf` -> ENTERED, 2 chains, rc=0). The
instrument discriminates; the probe as specified does not.

## A.2 The honest census: SUBJECT-resolves-to-vertical, three buckets

**DENOMINATOR: 82 strictly-active projects** (org/projects/*.json, status=="active"; 304 total,
0 unreadable). Prefix distribution: NFRA 29 · OPAL 17 · ADVI 11 · MDPF 7 · DATA 3 · others 15.

**Method honesty: the mapping below is JUDGED by this seat, printed so it can be corrected.** A
row's bucket is a claim about subject-to-vertical correspondence, not a measurement -- confidence is
marked, and the mapping table itself is the checkable artifact.

| Bucket | n | Projects |
|---|---|---|
| **HOME (confident)** | ~48 | all ADVI_* (advi-bd/-inf/-cot, model-portfolios) · all MDPF_* (mdpf, model-portfolios) · MKOV_* (market-overview) · ETFS_* (etf-reports) · BD_SCHWABCONV (canonical-schwab) · SSCN_PRICOL + SCTY* (security-scanner) · PORTAL_AUTHHARD (portal-infra) · NFRA_MSGRAPH (m365-mcp) · NFRA graph family: EDGES, GRAPHFEED, GRAPHS, KUZUSPLIT, NERVES, TOOLGRAPH, REPOCOHERENCEGRAPH, WORLDMODEL (graph-platform) · NFRA_AGENTBUS, OPAL_SQSCHAT, OPAL_TICKET (ops-internal / ticketing) · OPAL_PORTALREFRESH (data-refresh) · OPAL_KIMIPIPELINE (graph-platform/data-refresh) · WSE_COTMDL (advi-cot/model-portfolios) |
| **HOME-UNCERTAIN** | ~23 | comp-tooling family (COMPASSURANCE, COMPSIMILAR, COMPTEAM, TOOLCHECK, TOOLHEALTH, INSTDRILL -> ops-internal?) · NFRA_COSTAWS, TERRAFORM, WRKFLW, SYSPARITY, PASSCRAFT, WEBSITE, LOCALROOT · OPAL_ALERTS, BBGTML (positioning?), CONSOLIDATION, GLDRNS, LCLRPO, PRISTINE · OPAL_TAXSMA x3 (Tax SMAs live on 49F SmartX -> smartx, plausibly) · DATA_ANALYTICS, DATA_PLATFORM · ADHC_PREFLT · ASTN_WSJFT (news?) · FIND_DUALBIZ (partners?) · UIUX_DESIGN · YALP_YCUTVR |
| **HOMELESS-CANDIDATE** (the class the 06 base predicted: estate-wide standards/naming/grammar/governance with no business-function home) | **~11** | **OPAL_TAXONOMY** (the type specimen) · **OPAL_SCHEDULE** · **OPAL_VENDORPROVENANCE** · **OPAL_ALTRESEARCH** · **DATA_SSOTMG** · **NFRA_ONTOLOGY** · **NFRA_GENESIS** · **NFRA_NESTEDABSTRACT** · **NFRA_PYFIELD** · **NFRA_PSTMRT** · (+1 borderline: NFRA_LOCALROOT) |

## A.3 The G-a answer, in CTO~A's requested form

- **attempted:** 82 (denominator stated) · **literally entered:** 0 (name-shape, by construction) ·
  **subject-reaches-a-vertical:** ~48 confident + ~23 plausible = **~71 of 82**
- **THE GENUINELY UNREACHABLE CLASS: ~11 of 82 = ~13%** -- consistent with the 06 base's own
  corrected bound (*"narrower than 37%"*), now sized. Its members are exactly the predicted shape:
  standards / taxonomy / governance / research work with no `standards` or `taxonomy` vertical among
  the 29.
- **Gate-relevant statement:** the 06 base's two-class finding STANDS and its cost is MODERATE-LOW:
  ~87% of active projects can enter the estate through comp-estate by subject; the residual is a
  COHERENT class (governance-grain), which argues the fix is ONE new entry surface (a
  standards/governance vertical or an explicit "no-vertical" entry answer), not per-project patches.

---

# PART B -- L-7: comp-pipescript / comp-dataflow coverage vs the script corpus

## B.1 Frames first (the prior "386" is a DIFFERENT frame -- do not reconcile them)

| Frame | n |
|---|---|
| all .py under data/ (excl. __pycache__) | **678** |
| .py in any gold/ path | 318 |
| tiered medallion corpus: data/*/scripts/{gold,silver,bronze}/*.py | **273** (gold 194 / silver 53 / bronze 26) |
| NFRA_PYFIELD's "386" | a different, pyfield-defined corpus -- cited here only to say it is NOT this census's denominator |

## B.2 comp-pipescript's universe is DERIVED-FROM-DECLARED and covers FOUR trees

`safe_deploy_core.CODE_TREES` -> `{black_diamond, cot, inf, mdpf}`, all deploy-gated;
`PIPELINE_MAP` derives from it (the predicate-not-roster law honored -- consumers derive from one
declared authority). Tiered files INSIDE the universe: inf 76 + cot 48 + mdpf 23 (+ black_diamond's
home, which is NOT `data/bd` -- that dir holds ZERO .py; its scripts live under the bd bucket's own
layout) (+ data/assets shared homes 25, covered under the Rule-13 S3-membership guard:
key-exists=update, 404=loud-skip).

## B.3 The gaps, named with owners -- and then STOP (per the plan: no tool building)

| Outside the universe | .py count | Owner (existing lane) | Note |
|---|---|---|---|
| `data/find/` (dualbiz) | 74 | DS (find/deck work) | non-tiered layout; not deploy-gated |
| `data/smartx/` | 36 | **AE** (the 49-schwab-conv skill names AE explicitly; DS is IAM-blocked on that bucket) | non-tiered; conversion scripts |
| `data/etfs/` | 9 (2 tiered) | DS | small; partially tiered |
| `data/assets/` non-tiered residue | ~52 of 77 | DS/AE per Rule 13 | the 25 tiered are guard-covered |

**comp-dataflow** has no universe to census: it is PER-INVOCATION (`origin` = value-origin trace of
one script; `gate` = layer-grammar over a tree you name). Its "coverage" is a usage question --
whether lanes RUN it -- not a registry question. No gap to name; no tool to build.

**Census verdict: comp-pipescript's declared universe is coherent and honest (4 gated trees +
guarded shared homes); the out-of-universe mass is 3 non-tiered trees whose owners exist. STOP** --
extending the universe is a policy act (deploy-gating a tree changes who may deploy it, Rule 13),
not a coverage patch, and nobody has asked for it.

---

## Instrument notes (both parts)

G-a's probe-spec correction is the census's most important line: the exact method a document names
can be a true measurement of the wrong proposition, and checking the instrument's entry DOMAIN
against the question's domain cost one `--list` read. L-7's denominator carries three frames
deliberately -- a count quoted without its frame is how 386-vs-273 becomes a phantom discrepancy.
