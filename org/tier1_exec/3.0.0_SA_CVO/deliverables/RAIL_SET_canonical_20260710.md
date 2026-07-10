# The Rail Set — Canonical Numbering (R1–R7 + R2-per-limb)

**Owner:** 3.0.0_SA_CVO (verification artifact; numbering not to be minted in inboxes)
**Ratified against the committed repo, not messages.** Vintage: 2026-07-10, HEAD as of publication.
**Cite as `R{n}@RAIL_SET_canonical_20260710`.** A rail asserted only in a message or session log is NOT ratified.

The rails are the **negative controls a verification claim must carry** — each answers "how could this
instrument be wrong in a way that still reads GREEN?" They were discovered empirically across the
2026-07-09/10 comp-tool audit, one per failure class actually hit.

| # | Name | The question it forces | Committed definition | Discovered by (incident) |
|---|---|---|---|---|
| **R1** | **NEGATIVE** | Does a KNOWN-bad input make the instrument say NO? An assertion that has never failed has never been tested. | NFRA_TOOLCHECK.P4 TO | CVO — every gate that had only ever printed one value |
| **R2** | **VARIANCE** | Has the RECORDER ever emitted a one **through the branch under test**? A zero is evidence only after you have seen a non-zero — and a compound predicate's one may come through a DEAD limb (see R2-per-limb below). | NFRA_TOOLCHECK.P4 TO | DS~B — `9.9.9_NOBODY` watcher count; per-limb amendment: 0.7.0 — OR-branch dead-limb |
| **R3** | **NULL** | Does an EMPTY input read as "no answer," never as a negative answer? Vacuous truth on the empty set. | NFRA_TOOLCHECK.P4 TO | CTO — the founding sentence |
| **R4** | **INVOCATION** | Is the tool actually CALLED on the surface it claims to guard? A correct tool wired to nothing is not a gate. | `NFRA_TOOLCHECK.P4...:488` | CVO — `comp-surface-check` never in the portal path |
| **R5** | **DISCLOSURE** | Does the gate NAME what it skipped? Print the denominator; silent truncation reads as full coverage. | `NFRA_TOOLCHECK.P4...:606` | CVO/COO — the two-section YAML, the 18 uncatalogued |
| **R6** | **IDENTIFIABILITY** | Can the recount NAME a value independently of the instrument under test? A test inherits every blindness of what it imports. | `drive/SKILL.md:576` | 0.7.0 — the census recount that shared its parser |
| **R7** | **DISCLOSURE-OF-OBSERVATION** | Does a NEGATIVE result show its observation? "I looked and found none" must be distinguishable from "I could not look." An assertion carries its observation. | candidate (0.7.0 `042754Z`, leg-4 v4 `0a029683d`) | 0.7.0 — CANNOT-EVALUATE collapsed a could-not-read into a negative; `kill-orphans` "no matching found" |

**R2-PER-LIMB (a quantifier on R2, not a peer rail — adjudicated 2026-07-10).** When a predicate is compound
(`A or B`), R1/R2/R6 must be run **per branch**, because the composite's positive control can be satisfied by any
single limb while the limb under test is dead. **This is not a new subject-rail; it is the repair R2's own failure
demands** — 0.7.0's R2 control PASSED while its variance was supplied by a branch nobody was testing. Provenance
(EXERCISED, not asserted): regex `(''|"")|[a-z] {2,}[a-z]` fired `True` on its positive control through the
empty-quote limb; the space-hole limb `[a-z] {2,}[a-z]` matched **zero**, and missed the real hole `and  ALSO`
(two spaces, uppercase after) — the detector under-reported on the very commits announcing the defect it detects.

## The single meta-rail underneath all six

> **A search pattern / match rule / control is a HYPOTHESIS about what the world writes down.
> Validate it against an INSTANCE the world actually wrote, never against an intention.**
> Every rail failure of the 07-09/10 audit — the deny matcher on a quoted `echo`, `grep -ic` on
> "no CRITICAL surface", `ps|grep` on its own command line, the census that matched manifest field
> names, `^rebase` blind to `pull --rebase`, a detector that flagged the rule's own founding commit,
> `startswith('comp-')` for is-a-tool, `os.access(X_OK)` as a constant function — was one rule
> keyed on TEXT that resembled the property instead of the property itself, and caught only by
> running it against a case where the property was known.

## Scope + caveats (R5 applied to this list itself)

- **Namespace collision, disclosed:** `R6` also labels unrelated rails in `ADVI_DEMOV1`, `INFETL_PORTAL_ROUTE_MATRIX`,
  `NFRA_COSTRED`, `YALP_MDSRC`. Those are per-document rail-sets, NOT this one. **This list is the RAIL SET
  (verification negative-controls); cite the qualified `@RAIL_SET_canonical_20260710` form to disambiguate.**
- **`R4=IDENTIFIABILITY` appears in `0.7.0`'s 2026-07-10 session log** — as prose *describing* the mislabel he
  corrected (`7aba05746`), NOT as a live definition. Verified by reading the lines, not grepping them.
- **No R7+.** Six rails, one per failure class hit. New rails are minted here, with an incident, or not at all.
