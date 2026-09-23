/** Actual regenerated backend wires through pinned parser and mounted component functions.
 * Manual hook dispatcher/static markup: not browser or React scheduling evidence. */
import { afterAll, expect, test } from 'bun:test'
import { createHash } from 'node:crypto'
import { readFileSync, writeFileSync } from 'node:fs'
import { resolve } from 'node:path'
import { pathToFileURL } from 'node:url'

const root = process.env.IRPT_PORTAL_REVIEW_ROOT!
const backend = process.env.IRPT_DATE_BACKEND_EVIDENCE!
if (!root || !backend) throw new Error('Exact source snapshot and regenerated backend evidence required')
const load = (path: string) => import(pathToFileURL(resolve(root, path)).href)
const React = await load('node_modules/react/index.js')
const { renderToStaticMarkup } = await load('node_modules/react-dom/server.js')
const { ProspectJobStatus } = await load('src/pages/InvestorReporting/tabs/analysis/ProspectJobStatus.tsx')
const { parseIrEnvelope } = await load('src/pages/InvestorReporting/contracts/envelope.ts')
const { irBuildRequest } = await load('src/api/endpoints/investor-reporting.ts')
const { formatSourceAgeForState } = await load('src/pages/InvestorReporting/state/status.ts')
const evidence = JSON.parse(readFileSync(backend, 'utf8'))
const results: any[] = [], markup: Record<string, string> = {}
const tick = () => new Promise<void>((done) => setImmediate(done))

async function renderIssued(wire: any) {
  const parsed = parseIrEnvelope('status-job', wire)
  const slots: any[] = [], effects: any[] = []
  let cursor = 0
  const api = { getJobStatus: async (id: string) => {
    expect(id).toBe(wire.data.operation.operation_id)
    return parsed.data
  } }
  const internals = React.__CLIENT_INTERNALS_DO_NOT_USE_OR_WARN_USERS_THEY_CANNOT_UPGRADE
  function render() {
    cursor = 0
    const previous = internals.H
    internals.H = {
      useState(initial: any) {
        const i = cursor++
        if (!(i in slots)) slots[i] = initial
        return [slots[i], (value: any) => { slots[i] = typeof value === 'function' ? value(slots[i]) : value }]
      },
      useEffect(effect: () => any) {
        const i = cursor++
        if (!(i in slots)) { slots[i] = true; effects.push(effect) }
      },
    }
    try { return ProspectJobStatus({ api, requestId: wire.data.operation.operation_id }) }
    finally { internals.H = previous }
  }
  render()
  const cleanups = effects.map((fn) => fn())
  await tick()
  const html = renderToStaticMarkup(render())
  cleanups.forEach((fn) => fn?.())
  return { parsed, html }
}

function control(name: string, run: () => Promise<void> | void) {
  test(name, async () => {
    const oldFetch = globalThis.fetch
    globalThis.fetch = (() => { throw new Error('NETWORK_FORBIDDEN') }) as any
    try { await run(); results.push({ name, outcome: 'PASS' }) }
    catch (error) { results.push({ name, outcome: 'FAIL', error: String(error) }); throw error }
    finally { globalThis.fetch = oldFetch }
  })
}

for (const name of ['undated', 'empty', 'per_section', 'mixed']) {
  control(name + ' actual backend Entry bytes retain every source fact in issued status display', async () => {
    const wire = evidence.wires[name]
    const { parsed, html } = await renderIssued(wire)
    markup[name] = html
    expect(parsed.data.sourceDate.prospectDates.sections).toEqual(wire.data.source_dates.section_dates)
    expect(parsed.data.sourceDate.prospectDates.binding).toEqual(wire.data.source_dates.prospect_analysis)
    expect(html).toContain(name === 'undated' || name === 'empty' ? 'Undated prospect input' : 'Source dates vary by section')
    for (const row of wire.data.source_dates.section_dates) {
      expect(html).toContain(row.section_id)
      expect(html).toContain(row.as_of_date ?? 'Undated section')
    }
    expect(formatSourceAgeForState(parsed.data.state, parsed.data.sourceDate, () => { throw new Error('CLOCK_FORBIDDEN') }))
      .toBe(name === 'undated' || name === 'empty' ? 'Undated prospect input' : 'Source dates vary by section')
    expect(parsed.data.correlationId).toBe(null)
  })
}

control('ordinary single business date remains visible in actual issued status display', async () => {
  const { parsed, html } = await renderIssued(evidence.wires.single_date)
  markup.single_date = html
  expect(parsed.data.sourceDate.businessAsOf).toBe('2026-09-01')
  expect(parsed.data.sourceDate.prospectDates).toBe(undefined)
  expect(html).toContain('2026-09-01')
})

control('old and unknown consumers do not receive an extension or an undated label', async () => {
  for (const name of ['old_consumer', 'unknown_capability', 'duplicate_capability', 'comma_capability']) {
    const { parsed, html } = await renderIssued(evidence.wires[name])
    expect(parsed.data.state).toBe('UNAVAILABLE')
    expect(parsed.data.sourceDate.prospectDates).toBe(undefined)
    expect(html).not.toContain('Undated prospect input')
    expect(html).not.toContain('Source dates vary by section')
  }
})

control('all ten malformed regenerated source bindings are refused by actual envelope parser', () => {
  for (const data of Object.values(evidence.malformed_wires)) {
    const wire = { ...evidence.wires.mixed, data }
    expect(() => parseIrEnvelope('status-job', wire)).toThrow()
  }
})

control('non-status-job operations cannot carry the prospect extension', () => {
  for (const operation of ['status-summary', 'analysis-report', 'performance-report']) {
    expect(() => parseIrEnvelope(operation, { ...evidence.wires.mixed, operation })).toThrow()
  }
})

control('only status-job requests advertise exact prospect-v1 capability', () => {
  const id = evidence.wires.mixed.data.operation.operation_id
  expect(irBuildRequest('status-job', { pathParams: { jobId: id } }).headers['X-IRPT-Status-Dates']).toBe('prospect-v1')
  expect(irBuildRequest('status-summary').headers['X-IRPT-Status-Dates']).toBe(undefined)
  expect(irBuildRequest('analysis-report', { pathParams: { jobId: id } }).headers['X-IRPT-Status-Dates']).toBe(undefined)
})

control('generated public and internal status type hashes match paired backend source schemas', () => {
  for (const name of ['PublicStatusEnvelope', 'StatusEnvelope']) {
    const type = readFileSync(resolve(root, `src/pages/InvestorReporting/contracts/wire/${name}.ts`), 'utf8')
    const relative = `docs/contracts/investor-reporting/v1/${name}.schema.json`
    const source = readFileSync(resolve(process.env.IRPT_DATE_BACKEND_ROOT!, relative))
    expect(createHash('sha256').update(source).digest('hex')).toBe(evidence.source_sha256[relative])
    // gen-wire.ts explicitly normalizes checkout CRLF before citing schema text hashes.
    const normalized = createHash('sha256').update(source.toString('utf8').replace(/\r\n/g, '\n')).digest('hex')
    expect(type).toContain(normalized)
  }
})

afterAll(() => {
  const output = process.env.IRPT_PORTAL_REVIEW_OUTPUT
  if (!output) throw new Error('Evidence output required')
  const source = JSON.parse(readFileSync(resolve(root, 'review-source-hashes.json'), 'utf8'))
  writeFileSync(output, JSON.stringify({ portal_pin: source.pin, backend_pin: evidence.pin,
    backend_evidence_sha256: createHash('sha256').update(readFileSync(backend)).digest('hex'),
    source_sha256: source.hashes, controls: results, markup,
    limitations: ['Manual React hooks and static markup, no real browser or React scheduling',
      'Actual backend Entry wires use synthetic reports/offline retained storage; no vendor or runtime acceptance',
      'No actual export/render bundle or PDF tested'] }, null, 2) + '\n')
})
