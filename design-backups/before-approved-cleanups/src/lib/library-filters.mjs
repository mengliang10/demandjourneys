export const validMonth = value => /^\d{4}-(0[1-9]|1[0-2])$/.test(value || '');
export const validDate = value => /^\d{4}-\d{2}-\d{2}$/.test(value || '') && !Number.isNaN(Date.parse(value)) && new Date(value).toISOString().slice(0,10)===value;
export function matchesPresentation(record, filters) {
 const terms=filters.query.trim().toLocaleLowerCase().split(/\s+/).filter(Boolean);
 if(!terms.every(term=>record.text.includes(term))) return false;
 if(filters.tags.size && !record.tags.some(tag=>filters.tags.has(tag))) return false;
 if(filters.subjects.size && !record.subjects.some(subject=>filters.subjects.has(subject))) return false;
 if(filters.month) return !!record.published && record.published.slice(0,7)===filters.month;
 return true;
}
