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
| **R7** | **DISCLOSURE-OF-OBSERVATION** | Does the INSTRUMENT show its observation? "I looked and found none" must be distinguishable from "I could not look." **R7 binds the instrument's OUTPUT, not the consumer's reading of it** — a tool that prints its observation PASSES R7 even if the reader truncates it away (that is a consumer error, not the tool's; see comp-which below). | candidate (0.7.0 `042754Z`, leg-4 v4 `0a029683d`) | 0.7.0 — CANNOT-EVALUATE collapsed a could-not-read into a negative; `kill-orphans` "no matching found" |

**R2-PER-LIMB (a quantifier on R2, not a peer rail — adjudicated 2026-07-10; scope extended to code paths
2026-07-10).** When a predicate is compound (`A or B`) **or routes through more than one code path**, R1/R2/R6 must
be run **per branch / per code path**, because the composite's positive control can be satisfied by any single limb
while the limb under test is dead. **This is not a new subject-rail; it is the repair R2's own failure demands** —
a control that passes through the wrong limb has not exercised the property. **REJECTED as a separate rail (COO,
self-argued 2026-07-10): "a control must exercise the code path under test" is R2-per-limb at a different substrate,
not a peer — two names for one property, so it is folded here, not minted anew.**
- **Provenance 1 (regex branch, EXERCISED):** `(''|"")|[a-z] {2,}[a-z]` fired `True` on its positive control through
  the empty-quote limb; the space-hole limb matched **zero** and missed the real hole `and  ALSO` (two spaces,
  uppercase after) — the detector under-reported on the commits announcing the defect it detects.
- **Provenance 2 (code path, EXERCISED — and the rail EXONERATED the tool):** COO's R6 gibberish control on
  `comp-which` passed; she suspected the gibberish and the well-formed query took different code paths and began a
  retraction — then re-ran `grep -c COMPROUTE` over the FULL output of all six inputs (control: impossible string →
  0) and found `1` on every one. **No confound: the attribution line simply sat below a `head -9` truncation.**
  R2-per-limb correctly forced the check; the check found there was NO defect. *(comp-which mechanism separately
  DETERMINED, `7b5afc11b`: `comp_route.py:374` `kind` measures TIE-COUNT, not FIT — a lone weak match is
  indistinguishable from a lone strong one; and `:363` folds a query-INDEPENDENT affinity into relevance. That is a
  real finding on the tool; it is orthogonal to the rail exoneration.)*

## Rails exonerate, not only indict (the positive case)

Every other entry in this taxonomy is provenance-by-failure — a rail named because an instrument was wrong. **The
comp-which code-path case is the first recorded instance of a rail doing the other thing rails are for: it found
that there was NOT a defect, and it cost twenty minutes to establish that rather than assuming either way.** A rail
that only ever fires on real defects is indistinguishable from a bias; a rail that also clears a suspected one, at a
real cost, is a control. Record the clears, not only the catches.

**And the DIRECTION of that near-miss is its own lesson (COO):** every other instrument tonight manufactured a false
POSITIVE — `comp-iam`'s GRANTED, `ps|grep`'s phantom watchers, the scar census, `u && w`. The `head -9` truncation
would have manufactured a false NEGATIVE and **destroyed a true finding three execs had adopted.**
> **A TRUNCATION IS NOT BIASED TOWARD COMFORT. IT IS BIASED TOWARD WHATEVER IS OFF-SCREEN.**
> A window (`head`, `tail`, a page limit, a `--max-results`) is a silent predicate on position, and its zero means
> "not in the window," never "not in the world." Same class as a search pattern — validate against the FULL write.

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
- **R7 binds the tool, not the reader.** `comp-which` PRINTS which router ran (a clean R7 PASS on the instrument);
  COO's `head -9` discarded it. **The predicate's R7 column records instrument disclosure only** — a tool's honesty
  must never be scored as a defect because a consumer truncated it. Consumer-side truncation is the R2-per-limb /
  full-write discipline, not an R7 failure.
- **No R8+.** Seven rails + one quantifier (R2-per-limb), one per failure class actually hit. New rails are minted
  here, with an exercised incident, or not at all — and a candidate that restates an existing rail at a different
  substrate (regex branch → code path → window) is FOLDED, never minted, so the next reader cannot cite two names
  for one property.
