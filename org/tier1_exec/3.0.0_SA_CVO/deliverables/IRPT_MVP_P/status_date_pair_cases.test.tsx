import { expect, test } from 'bun:test'
import { renderToStaticMarkup } from 'react-dom/server'
import { parseIrEnvelope } from './src/pages/InvestorReporting/contracts/envelope'
import { ProspectSourceDates } from './src/pages/InvestorReporting/tabs/ProspectSourceDates'
import dates from './actual-owned-dates.json'
import outer from './actual-owned-outer.json'

test('fresh actual producer output survives parser and static shared date rendering', () => {
  for (const response of Object.values(dates.cases)) {
    const parsed: any = parseIrEnvelope('status-job', response)
    expect(parsed.refused).toBe(false)
    expect(parsed.data.producerState).toBe(response.data.state)
    expect(parsed.data.correlationId).toBe(null)
    const html = renderToStaticMarkup(<ProspectSourceDates reading={parsed.data.sourceDate} />)
    const source: any = response.data.source_dates
    for (const row of source.section_dates ?? []) {
      expect(html).toContain(row.section_id)
      expect(html).toContain(row.as_of_date ?? 'Undated section')
    }
    if (source.business_date) expect(parsed.data.sourceDate.businessAsOf).toBe(source.business_date)
    expect(html).not.toContain('internal_correlation_id')
  }
})

const mutations: Record<string, (wire: any) => void> = {
  outer_unknown: w => { w.unknown = true },
  outer_operation: w => { w.operation = 'status-summary' },
  grant_missing: w => { delete w.unprojected_grant },
  inner_operation: w => { w.data.operation.operation_kind = 'performance_report' },
  null_business: w => { w.data.source_dates.business_date = null },
  null_basis: w => { w.data.source_dates.date_basis = null },
  wrong_input: w => { w.data.source_dates.prospect_analysis.input_id = 'portfolio_' + '0'.repeat(64) },
  wrong_request: w => { w.data.operation.operation_id = 'REQ-' + '0'.repeat(24) },
  mutable: w => { w.data.source_dates.prospect_analysis.immutable = false },
  numeric_revision: w => { w.data.source_dates.prospect_analysis.report_revision = 111 },
  wrong_lane: w => { w.data.source_dates.prospect_analysis.source_lane = 'CUSTODY' },
  date_unknown: w => { w.data.source_dates.other = '2026-09-22' },
  invalid_date: w => { w.data.source_dates.section_dates[0].as_of_date = '2026-02-30' },
  missing_section: w => { delete w.data.source_dates.section_dates[0].section_id },
  duplicate_section: w => { w.data.source_dates.section_dates.push(w.data.source_dates.section_dates[0]) },
}
for (const [name, mutate] of Object.entries(mutations)) {
  test('actual wire rejects ' + name, () => {
    const wire = structuredClone(dates.cases.per_section)
    mutate(wire)
    expect(() => parseIrEnvelope('status-job', wire)).toThrow()
  })
}

for (const [kind, pair] of Object.entries(outer.cases)) {
  test('actual ' + kind + ' success/refusal discrimination remains closed', () => {
    const success = parseIrEnvelope(pair.success.operation, pair.success)
    const refusal = parseIrEnvelope(pair.refusal.operation, pair.refusal)
    expect(success.refused).toBe(false)
    expect(refusal.refused).toBe(true)
    expect(refusal.data).toBe(null)
    expect(refusal.publicReasonCode).toBe('CONTRACT_VERSION')
    expect(() => parseIrEnvelope(pair.refusal.operation, { ...pair.refusal, data: pair.success.data })).toThrow()
  })
}
