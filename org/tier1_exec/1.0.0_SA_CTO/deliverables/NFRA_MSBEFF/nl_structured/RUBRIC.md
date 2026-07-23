# NFRA_MSBEFF NL-corpus structured-analysis RUBRIC (fanout contract v1)

**Purpose (Andrew-direct 2026-07-23):** convert 2,218 session-log `## Compiler Tools` sections into a
structured log of what was working and what was not, with a rubric across relevant axes, full
granularity, and provenance to the original log.

## Input
One `chunk_NN.txt` file. Sections are delimited by `===== SOURCE: <path> =====` lines; the path IS the
provenance (agent serial and date are recoverable from it: `.../{serial}/logs/{YYYY-MM-DD}/{file}.md`).

## Unit of analysis
One FINDING = one evaluative statement about a tool or the tool framework (a thing that worked, failed,
was missing, misrouted, substituted, or caused friction). A section may yield 0..N findings. Routine
"ran X: PASS" rows with no evaluative content yield NOTHING — do not pad. A section with a mandated
"no tools run because <reason>" sentence yields one finding only if the reason is itself signal
(e.g. "pure org-record edit" = skip; "no tool covers this" = a GAP finding).

## Output: one JSON object per line (JSONL), schema exactly:
```json
{
  "source": "<the SOURCE path verbatim>",
  "serial": "<agent serial from path>",
  "date": "YYYY-MM-DD",
  "tool": "<canonical comp-* name, or 'framework'|'rail'|'graph'|'gate' for non-tool-specific findings>",
  "verdict": "WORKED | FAILED_TOOL | FAILED_COVERAGE | STALE_SOURCE | MISROUTE | SUBSTITUTED | FRICTION | GAP_NAMED | FIXED_IN_FLIGHT",
  "layer": "mechanical | semantic | behavioral",
  "signal": 1,
  "quote": "<VERBATIM quote from the section, <=280 chars — never paraphrase>",
  "gist": "<<=140 chars your plain-English summary>",
  "remedy": "<verbatim or tight paraphrase of any fix the agent proposed, else ''>"
}
```

## Verdict definitions
- WORKED — tool answered the question; include only when the agent SAYS something evaluative
  (speed, replaced manual work, caught something). Bare PASS is not a finding.
- FAILED_TOOL — crash/wrong answer/charmap/timeout: the tool malfunctioned (mechanical).
- FAILED_COVERAGE — tool ran fine but its graph/manifest/config doesn't cover the target
  ("not in graph", dynamically-keyed I/O missed, shell callers unresolved) (mechanical).
- STALE_SOURCE — tool answered from a stale vintage (graph/cache/canonical behind live) (mechanical).
- MISROUTE — comp-which/HUD routed to the wrong tool, near-tie noise, or a natural question no
  tool answers (semantic).
- SUBSTITUTED — agent bypassed a fitting tool (manual read/raw grep/"already knew") (behavioral).
- FRICTION — usable but costly: noise, no PATH launcher, awkward flags, false positives (mixed; pick layer).
- GAP_NAMED — agent explicitly names a missing tool/capability (semantic if "no tool answers X",
  mechanical if "tool X should also do Y").
- FIXED_IN_FLIGHT — a tool defect found AND fixed in the same session (counts as mechanical signal).

## Layer: pick the PRIMARY layer per the project frame — mechanical (does the tool get its data fast
and reliably), semantic (does the right tool get found for the query), behavioral (does the agent
reach for the tool at all).

## signal: 1 = routine observation · 2 = clear reusable signal · 3 = load-bearing (names a defect
class, quantifies impact, or proposes a concrete remedy). Reserve 3s; a chunk with everything at 3
is miscalibrated.

## Hard rules
1. **quote is VERBATIM from the chunk** — it must be findable by exact substring search in the source
   file (this is the audit control on the whole fanout; a quote that does not match is a fabricated
   row). ASCII-transliterate only non-ASCII characters.
2. **Every finding carries source path** — no aggregation rows, no section-less findings.
3. Do not deduplicate across sections — the same complaint appearing in 30 logs is the FREQUENCY
   signal; emit all 30.
4. Emit NOTHING for sections with zero evaluative content. Expected yield is roughly 1-3 findings
   per section on average; both 0-yield sections and 10-finding sections are normal.

## Delivery
Write your JSONL to `chunk_NN.findings.jsonl` next to your input chunk. Final message: counts only
(sections read / findings emitted / verdict histogram / anything that did not fit the rubric).
