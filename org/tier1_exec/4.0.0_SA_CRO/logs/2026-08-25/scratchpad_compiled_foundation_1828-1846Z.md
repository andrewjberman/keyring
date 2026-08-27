# 4.0.0_SA_CRO — scratchpad compiled foundation, 2026-08-25 18:28–18:46Z

**archetype:** BUILD  
**secondary_archetypes:** ARCHITECT, VALIDATE, SCRIBE

Andrew directed creation of `C:/Users/AndrewBerman/Downloads/scratchpad_tmp` as the beginning of
the new repository. He established three controlling constraints: no Markdown; documentation is
structured JSON or XML; and every document declares its exact home and lifecycle semantics from
the outset. He further narrowed the old `ajb_workspace/org` migration to pared-down mechanics,
runtime operations, and functionality only, especially MCP and agent fabric. Logs, databases,
inboxes, message/session history, telemetry, data, archives, and deliverables are not relevant and
must not migrate.

## Result

A new Git repository was initialized on `main` and committed:

- repository: `C:/Users/AndrewBerman/Downloads/scratchpad_tmp`
- commit: `09e807c18622534665fbff74e80601caafbbf2b7`
- subject: `foundation: establish compiled schema-first repository`
- tracked foundation denominator: 28 files
- compiled input digest: `1c331c8c6c2bde5c061993d51af19656ce6689cc945a051ca5f1cd6b6de49a34`

No old runtime source was copied. The repository contains source identities, destination contracts,
and explicit `admit/adapt/rebuild/exclude/defer` decisions only.

## Foundation

- `repo.json` declares every permitted zone, root file, extension, authority, and build command.
- `contracts/schemas/document-envelope.schema.json` and `document-envelope.xsd` establish JSON and
  XML primitives.
- Every structured document declares `mutation_mode`, `temporal_mode`, `authority_mode`, exact
  `home`, `version`, `retention`, and `supersedes`.
- `org/policy/repository_policy.v1.json` makes Markdown a compile failure and limits `/org` to agent
  fabric, MCP, runtime launch/bootstrap, policy enforcement, and minimal runtime registries.
- Proposal A-F component homes are under `platform/`; Proposal G is under `company/constitution`,
  not `/org`.
- Current A-G source identities and hashes are in `sources/proposals.v1.json`.
- The old-workspace admission map is in `sources/migration_candidates.v1.json`; default decision is
  exclusion.
- Internal, external, and lens tools have separate typed catalogs.
- The compiler generates a deterministic catalog and compile receipt under ignored `build/`.

## Old `/org` boundary

Candidate mechanics from `org/mcp` include broker, argument guards, stateless server code, Codex
monitor/bridge/heartbeat mechanics, launchers, and their tests. Explicit exclusions include
`*.db*`, `*.log`, JSONL streams, inboxes, message archives, sessions, telemetry, watcher/process
state, caches, and all work products.

`org/tier0`, `org/tier0_exec`, and `org/tier1_exec` are not copied. Active executable laws, roles,
authority edges, and routing mechanics must be rebuilt into small structured runtime contracts;
historical prose, logs, tasks, and deliverables remain excluded.

## Validation

- Initial compile: PASS, 28 files, exact digest above.
- Generated-output check: PASS.
- Unit tests: 8/8 PASS, including negative controls for Markdown, lifecycle-less documents, and
  `/org` log/data paths.
- Python compileall: PASS.
- Git whitespace check: PASS after LF policy was added.
- Clean detached worktree: compile PASS with identical digest, generated check PASS, tests 8/8;
  worktree removed afterward.
- Repository state after commit: clean `main`.
- Markdown files inside the new repository: zero.

## Compiler Tools

`python .tools/comp-find codex-inbox-turn-bridge org/mcp --limit 10` executed successfully against
the old workspace. It measured 7 hits across a denominator of 131 files, with 3 binary files
explicitly unsearched. The result supported the bounded MCP candidate set but did not authorize a
copy.

## Next bounded step

The first migration slice should be MCP mechanics only. Before any file is copied, produce an exact
file denominator and classify each candidate as source, configuration, test, generated state, or
runtime state. Admit only a dependency-closed, secret-free set with JSON configuration schemas,
health probes, positive tests, and negative tests. Agent instruction compatibility must be injected
by launchers or generated ephemerally outside the repository; committed `AGENTS.md`, `CLAUDE.md`,
and `SKILL.md` files remain forbidden.
