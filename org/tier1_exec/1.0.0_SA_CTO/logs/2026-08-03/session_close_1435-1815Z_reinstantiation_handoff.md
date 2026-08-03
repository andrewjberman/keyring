# SESSION CLOSE (1435-1815Z) — Andrew-directed reinstantiation for the RCG drive

**archetype:** SCRIBE
**secondary_archetypes:** COORDINATE

Final log of this session, Andrew-direct: *"write a /log I am going to reinstantiate you and the
other agents because I am going to proceed RCG work with 4.0.0_SA_CRO and I want to bring you
back online with fresh context for some targeted architectural work."* Delta since
`mdlp_closeout_rcg_grant_and_drive_staging_1705-1815Z.md` @bc5ba58c0a is small (the closeout
correction landed @2ad3477648; nothing else moved); this log is the REINSTANTIATION HANDOFF.

## What this session did (one paragraph, for the successor's first read)

Fresh-boot 1435Z into an MSTR-relayed Andrew-direct: order the ST Model Portfolio manifest
silent-regression fix. By 1815Z: **MDLP_MONPUB found-live -> spec'd -> CVO-validated -> 9 work
items executed across 4 Lambdas + portal + CloudFront edge -> every one witnessed -> CLOSED
COMPLETE AND ACCURATE on Andrew's visual smoke** (@dc2826c11c + correction @2ad3477648). Along
the way: the ETFS July final deliverables package built + delivered (workbook/deck/CSVs,
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ETFS_JULY_2026_FINAL/`); NFRA_VELOCITY suspended
(temporary, Andrew-direct x2) with the RCG PRD landed canonically; the C3L.1 loop honestly
closed to ~B ("not yet"); three owned-paths arch-gates + the RCG_OPERATOR grant landed; the
"known-good is a CONTENT claim" lesson banked fabric-wide after 3 agents + CVO carried an unread
07-30 into a republish order.

## FOR THE SUCCESSOR — the live state you inherit

**THE NEXT WORK IS THE RCG DRIVE** (NFRA_REPOCOHERENCEGRAPH, Andrew proceeding with 4.0.0_SA_CRO):
- PRD: `docs/architecture/NFRA_REPOCOHERENCEGRAPH_PRD.md` (READ IT END-TO-END FIRST — the
  phasing, safety spine, and needs-Andrew list are all there).
- Entry gate at Andrew: spec GO + two defaults (git rm vs archive-move; folder name `rcg/`) +
  review-session cadence. Suspension record + PRD landing + rcg/** grant (RCG_OPERATOR,
  @56ef220877, CRO sole member) are ALREADY DONE — do not redo.
- CTO's P0 items when the drive starts: arch-gate + wiring of the rcg/ MANIFEST pre-commit gate
  (extend the commit-gate chain; exercise BOTH directions as first acceptance), the
  sweep-mechanics ruling record, arch-gates on MIGRATE executions as they come.
- Andrew's stated intent: surgical, step-by-step, cogent — one step at a time, his ratification
  sessions are the rate limiter. Then a VELOCITY rescope HE will define.

**CLOSED, do not reopen:** MDLP_MONPUB (all evidence in the TOs + project JSON; live-occasion
legs W6-full/W8-traversal ride the next genuine rollback, COO-tracked, NON-blocking).
NFRA_VELOCITY_CORE/_ESTATE are ON-HOLD (never closed) with open-work ledgers in their JSONs.

**PARKED AT ANDREW (surface when relevant, do not push):** ETFS AVGCAP aggregation confirmation
(gates final certainty on every July figure in the delivered package) · Orion label
normalization build + restatement decisions (spec @8f0e32a642 held) · C3L.1 issuance (0.7.0~B
idle at gate on it, fence stands).

**STANDING ITEMS ELSEWHERE:** ~B instrument TOs (R4-A trigger fix + source-map sweep fix) await
0.8.0_AE_CloudComp~B spawn, COO chases · CF instrument gaps (comp-routes cache-policy blindness,
comp-blast CF path-pattern absence) in CVO's register, register-only · comp-blast cp1252 crash
(workaround PYTHONIOENCODING=utf-8) unrouted · SURFACE_ACK unauditable-diligence gate candidate
banked · Yang's PARSEKEYABLE_DES pin held at HIS request — NO AGENT PUSHES.

**MECHANICAL NOTES THAT SAVE THE SUCCESSOR TIME:** /watcher arm needs /cygdrive/c prefix on this
box · Excel/PowerPoint COM are the working substitutes for the document-skills' LibreOffice
tooling (AF_UNIX broken) · pptx validate.py needs PYTHONUTF8=1 · lanes commit, MSTR pushes
(CLOUD was ~30 ahead of origin at close, integrator leg at MSTR).

## Compiler Tools (session totals)

| tool | result |
|---|---|
| comp-estate, comp-blast (x3), comp-surface-check, comp-grep | PASS (one cp1252 tool defect found + worked around) |
| owned-paths-validate (x2 grants) | PASS with positive+negative membership controls |
| live AWS primitives (head-object/body x8, lambda get-function-configuration, s3 ls) | PASS — every GO and every acceptance was live-grounded before ruling |
| Excel COM recalc, PowerPoint COM export, pptx validate | PASS — deliverables QA |

**Gap found this session:** comp-blast cp1252 crash on HOLD-banner render; comp-routes does not
surface cache-policy identities (both registered, unbuilt).

## The lines worth carrying

1. **"Known-good" is a CONTENT claim** — read the values before you republish anything.
2. **Understatement is the same record-drift class as overstatement**, pointed the other way.
3. **A pinned expectation nobody can read is not pinned** — route the artifact, not its name.
4. **The membership grant without the path rule** recurred 3x in one family in one day — when
   granting, check BOTH halves.
5. **86400 was dead config on the designed path and a trap on any unstamped one** — config that
   disagrees with its runtime stamp is a latent amplifier wherever the stamp fails.
