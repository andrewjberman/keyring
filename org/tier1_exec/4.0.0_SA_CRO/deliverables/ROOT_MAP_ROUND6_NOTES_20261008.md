# ROOT_MAP round 6 (E1) -- 74 drafted entries, validation, and the empty-root recommendation

Author: 4.0.0_SA_CRO (fork), 2026-10-08. For: 2.0.0_SA_COO~G msg 107061 (LGIC_BLANKFIX round 6, item E1).
Source: org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~1/MAP_ENTRIES_FOR_RULING_round6.md
(@4a4e231eaa, merged @c6cf182bb2) and UNMAPPED_ROOTS_round6.txt. Nothing here edits infra/logic/registry/root_map.json;
nothing was committed or sent.

## Files (scratchpad)
- root_map_round6_entries.json -- the 74 entries. Ordinary entries carry system/scope/source/evidence/fills/exceptions;
  names-zero none entries carry names/why/evidence. Every entry has a `_cite` map: each field cites file:line (the
  repository line the worker re-read, or the MAP_ENTRIES line that decided it) or reads UNDECIDED.
- root_map_round6_scratch.json -- root_map.json at HEAD with the 74 merged (no key collides with the 13 mapped roots).
- root_map_round6_decided_subset.json -- root_map.json plus the one entry that passes the loader (inf-pipeline).
- build_round6.py (the parser), round6_validation.json (per-entry verdict), round6_all_subset.txt (the `all` run).

## Counts by class (74)
- to-map 36; no-stored-name 14; names-zero 24 = attaches_to_names_declared_elsewhere 7, names_from_caller 4,
  DECLARES-NAMES 11 (drafted as ordinary entries), UNDECIDED 2.
- Shapes: 61 ordinary entries, 13 `names: none` entries (11 decided + 2 with why UNDECIDED).

## Validation (lib/opal_naming_rootmap.py load_map / views; lib/opal_naming_rootcheck.py)
- Full scratch, load_map: FAIL at the first entry it reaches, shared-infra: "field system: 'UNDECIDED' is not a
  systems.json key". Expected: the loader refuses UNDECIDED by construction.
- Per entry (each alone): 1 PASS (inf-pipeline), 73 FAIL.
  - 13 fail because the loader does not support the `names: none` shape at all: load_map requires system, scope,
    source and evidence on EVERY entry (lib/opal_naming_rootmap.py:75-77). The shape is described in root_map.json
    _about.row_fields (@35f40f2c02) but no .py file reads it (0 files mention names_from_caller or
    attaches_to_names_declared_elsewhere). FINDING: none of the 11 decided none entries can land until the reader
    learns the shape (the reader is LGIC_BLANKFIX code, not the registry's).
  - 60 ordinary entries fail only on UNDECIDED values: with every UNDECIDED replaced by a placeholder, the loader
    refuses 0 decided values (every decided system/scope/source and exception system is a valid key).
- Decided subset (HEAD's 13 + inf-pipeline): load_map PASS; `views` ok=True files=13 changed=0 (no generated view moves);
  rootcheck inf-pipeline ok=True items=364 (hole 71 -> 69, fix 184 -> 186 against HEAD's map);
  `all` ok=True roots_total=87 mapped=14 unmapped=73 items=776 hole=69 (HEAD: mapped=13 items=412 hole=0; the 69 holes are
  inf-pipeline's own items, visible once the root is mapped).

## UNDECIDED fields: 180
By field: source 51, fills 49, scope 33, exceptions 26, system 19, why 2. Per root:
  inf-pipeline                               exceptions(partial: 28 unlisted)
  shared-infra                               system, scope, source, exceptions
  smartx-pipeline                            scope
  globgrph                                   source
  news-pipeline                              source
  yang-pipeline                              source
  mdpf-pipeline                              source
  market-overview                            source
  portal-auth                                source
  trade-pipeline                             system, scope, source, fills, exceptions
  opal-gateway                               scope, source
  imo-pipeline                               scope, source, fills
  estate-report                              scope, source, fills
  fred-pipeline                              fills
  ycharts-pipeline                           scope, fills
  seeking-alpha                              scope, fills
  portfolio-management                       scope, source, fills
  astn-pipeline                              system, scope, source, fills, exceptions
  etfs-reports                               source, fills
  harvest                                    source, fills
  security-ops                               scope, source, fills
  opsec                                      scope, source, fills
  canonical-schwab-ec2                       system, scope, exceptions
  exec-summary                               source, fills
  nfra-ctlpln-identity                       system, scope, source, fills, exceptions
  data-refresh                               source, fills
  consolidation-gold-runner                  source, fills
  website                                    scope, source, fills
  etfs-netassets                             source, fills
  partners-api                               scope, source, fills
  security-scanner-pipeline                  source, fills
  etfs-canon                                 source, fills
  inf-value-parity                           system, source, fills, exceptions
  49f-value-parity                           system, source, fills, exceptions
  cot-value-parity                           system, source, fills, exceptions
  bd-49f-auto-login                          fills
  deck-generation-pipeline                   scope, source, fills
  github-actions-runner                      scope, source, fills
  mdpf-secclass/sector-writer                source, fills
  daily-sprint-generator                     scope, source, fills
  etfs-positioning                           source, fills
  modules/served-guard                       system, scope, source, fills, exceptions
  ticket-center                              system, scope, source, fills, exceptions
  portal-content                             scope, source, fills
  bloomberg-tunnel                           system, scope, fills, exceptions
  nfra-agentbus-port2                        system, scope, source, fills, exceptions
  partner-etl-ops-alerts                     system, scope, source, fills, exceptions
  transcripts                                system, source, fills, exceptions
  investor-reporting/reporting-read          scope
  served-guard-inf                           system, source, fills, exceptions
  c3materialize-b4                           system, scope, source, fills, exceptions
  canonical-schwab-si2-schedule              why
  etfs-rivalfunds                            source, fills, exceptions
  investor-reporting/holdings-performance    scope, source, fills, exceptions
  investor-reporting/reporting-gold          scope, fills, exceptions
  mdpf-secclass/new-security-classifier      scope, source, fills, exceptions
  nfra-agentbus                              scope, source, fills, exceptions
  nfra-agentbus-alyssa01                     scope, source, fills, exceptions
  nfra-ctlpln-agentbus                       source, fills, exceptions
  opal-assets-absence                        why
  partner-firms                              system, scope, source, fills, exceptions
  served-guard-49f                           system, source, fills, exceptions
  served-guard-cot                           system, source, fills, exceptions

Notes on the counts:
- fills UNDECIDED = the section proposes no fills (absent would mean all three fill, which is a decision the section
  did not make). fred-pipeline and bd-49f-auto-login have system/scope/source decided and only fills UNDECIDED.
- exceptions UNDECIDED = the section did not run the measurement (system UNDECIDED, or a DECLARES-NAMES root).
- inf-pipeline: 14 exceptions listed of 42; the source truncates the other 28 ("... 28 more of the same kind").
- Three exception headers count summary lines, not extra names: portal-auth (14 = 12 names + firmsep/secops summaries),
  opal-gateway (6 = 5 names + an mcportal summary), fred-pipeline (2 = 1 name + a cadence comment). Parsed names: all.
- fills and exceptions in the draft are the WORKER'S PROPOSALS (cited to their MAP_ENTRIES line); the registry owner
  adopts or amends them.

## The two empty roots (canonical-schwab-si2-schedule, opal-assets-absence): recommendation
Facts (MAP_ENTRIES :889-897 and :1088-1096): each file holds only terraform, provider and locals blocks; no resource.
si2-schedule's header describes an EventBridge schedule that was never written (its one commit 1c5a9ced13 is the same
57 lines); opal-assets-absence's Lambda, role and scheduler were removed by a later commit.

Does the existing shape cover them? No. names_from_caller means the root BUILDS names from its inputs for a caller
(modules/opal_name declares no resource either, but outputs a name, so it stays names_from_caller);
attaches_to_names_declared_elsewhere means the root HAS resources that attach to another root's names. These two roots
build no name and have no resource, so either value would be false. Reuse is ruled out on truth, not preference.

REC (a), preferred: add NO third value now. Leave both roots unmapped and send them to their owners as dead Terraform
for retirement (delete the folder, or write the resource the header promises). An empty root is a code-hygiene fact,
not a naming class; an enum member would mainly label code that should be deleted, and an unmapped empty root is an
honest, visible residue in the `all` denominator. Not read: whether either root's remote state still holds resources
(opal-assets-absence had applied resources before the removal commit).

REC (b), only if the map must close (unmapped = 0): a third why 'declares_no_resource', with its four-postulate record:
(i) MECE over the declared domain "roots entered as names: none" by subtraction on resource blocks: >0 with every name
from an input -> names_from_caller; >0, each attaching to a name declared elsewhere -> attaches_to_names_declared_
elsewhere; 0 resource blocks AND no name output -> declares_no_resource. Overlap check: modules/opal_name (0 resources,
outputs a name) stays names_from_caller, so the new member is defined by BOTH conditions. (ii) Same grain: one value
per root. (iii) One axis: why the root has nothing to name. (iv) State: the value does not move when the root later
gains a resource; the existing READER RULE (a none root found declaring a graded name is reported, never skipped)
covers that. A token census of the new word over the registry is owed before it lands.

## Not done
- No edit to root_map.json, no commit, no message. No change to the loader.
- The 28 unlisted inf-pipeline exceptions were not re-derived. No re-read of repository lines beyond the worker's quotes
  (the worker states each `read:` line was re-read at write time).
