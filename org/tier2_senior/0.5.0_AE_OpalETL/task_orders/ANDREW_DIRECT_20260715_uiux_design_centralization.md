# ANDREW-DIRECT #7 + #8 — UIUX centralization; TAXSMA intake guardrails (verbatim records)

## ANDREW-DIRECT #8 (same session, ~17:5xZ): TAXSMA CONTENT GUARDRAILS + DAILY SCHEDULE (verbatim)

> "We do need a daily schedule here but this is exactly why I want to analyze these files that
> are coming in so we understand exactly what type of content to expect and create a parsing
> strategy not only on the size of the file, but on the contents of the file, so we can make
> sure our outputs are robust, and if there is a data issue or something is off expectations,
> it is flagged at that point. We have to overengineer this to some extent, because Alyssa, who
> will be running the skill workflow, may or may not be able to assess/flag a 'suspicious' file,
> so we need to analyze everything that has come through in line with Yang's intent (which is
> also not beyond reproach), and build in guardrails accordingly. Logging everything in a shared
> cloud location is a good start. I think we also need a new folder for /flagged_files, or some
> kind of python-compiled report that establishes the flagged features (e.g. stub based on size)."

**Operative effects:** (1) daily schedule CONFIRMED as direction; (2) corpus content analysis of
every received SSAVAIL file -> derive the expected-content contract; (3) intake validation on
CONTENT, not just size -- deliberately overengineered because the operator (Alyssa) cannot be the
suspicious-file detector; (4) Yang's intent itself is validatable, not gospel; (5) run logging to
a shared cloud location; (6) a flagged_files quarantine folder AND/OR a python-compiled flag
report (flag taxonomy seeded with stub-by-size). **Execution finding at recon start:** gateway
`read_site_file`/`read_file` returned empty-success on ALL drive files -- httpx default
follow_redirects=False swallowed Graph's 302-to-download-URL as empty bytes (graph.py:39); never
detected because empty parses as valid. Fixed same turn + server-side `profile_site_file`
analysis tool built in the same deploy (content profiling without 12MB rides on the MCP channel).

---

# ANDREW-DIRECT #7 — UIUX macro + UIUX_DESIGN: centralized /design repository + process repoint (verbatim record)

<issued_to>0.5.0_AE_OpalETL~A</issued_to>
<issued_by>Andrew (sovereign, direct terminal prompt to the ~A lane session, appended to a /log order)</issued_by>
<channel>direct terminal prompt, session 8841a0df-4e0d-4190-9d2e-96fc825f9f23</channel>
<received>2026-07-15 ~15:4xZ</received>
<status>executing</status>

## VERBATIM (the phrasing IS the ruling)

> "I would also create a macro called UIUX which will be devoted to cross-platform client-facing
> product and design. The portal is the primary surface for this, however it will grow to other
> surfaces in time, particularly client-side integrations. I want a dedicated /design folder in
> the root where we create a centralized repository for all brand guideline materials, component
> design, archetypal patterns, and so on. The project that is designed to do this will be
> UIUX_DESIGN. This project will be in part infrastructural, assessing all relevant files and
> either duplicating or moving them to this location, with scalable folder design (do not want
> to design for markdown sprawl and deprecation). THe other part will be assessing any process
> architecture that relies on design functions and making sure that they are pointed at this
> location, e.g. all the tier 3 RD agents or any scripting work that adjusts design and
> client-side ux."

## Operative effects (recorded, not adjudicated)

1. **New macro `UIUX`** — cross-platform client-facing product + design. Portal = primary
   surface today; grows to other surfaces (particularly client-side integrations) over time.
2. **New project `UIUX_DESIGN`** — two parts:
   - **Part A (infrastructural):** workspace-root `/design` as THE centralized repository for
     brand guidelines, component design, archetypal patterns, etc.; assess all relevant files,
     duplicate-or-move them in; folder design must be SCALABLE and explicitly anti-sprawl
     ("do not want to design for markdown sprawl and deprecation").
   - **Part B (process):** audit every process architecture that relies on design functions
     (tier-3 RD agents, design/client-UX scripting, skills) and repoint them at `/design`.
3. Executed under the standing ~A sovereign-delegate pattern (register + execute,
   fabric-quiet, informational broadcast; CLAUDE.md gates binding). Same-turn sequence per
   Andrew: /log FIRST, then this.

## Execution record (same session)

- Registered: `UIUX` macro row (MACRO_CODES.md, rule-6 before-use), `org/projects/UIUX_DESIGN.json`,
  REGISTRY.md row. Broadcast to COO/CTO/MSTR same turn.
- Part A initial build: `/design` skeleton + charter (anti-sprawl law in `design/README.md`),
  canonical color-archetype law at `design/brand/COLOR_ARCHETYPES.md`, portal design system
  MOVED (canonical) to `design/systems/portal/` with tombstone-pointer stubs left at the old
  portal paths (one canonical copy, no divergence), living-code pointer register (tokens/themes
  stay code — pointed at, never copied).
- Part B initial pass: repointed portal/CLAUDE.md, panels/README.md, /frontend-dev skill;
  process-architecture audit of design-function references (RD agents, scripts, skills)
  recorded in the project JSON with the remainder as the next TO.
