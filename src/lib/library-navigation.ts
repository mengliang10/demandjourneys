import menu from '../data/library-menu.json';

const base = '/hospitality-presentations/';
const slug = (text: string) => text.toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/-$/, '');

export const groups = Object.entries(menu).map(([label, topics]) => ({
  label,
  href: base + 'browse/' + slug(label) + '/',
  topics: topics.map(name => ({
    label: name,
    href: base + 'browse/' + slug(label) + '/' + slug(name) + '/'
  }))
}));
export const latest = { label: 'Latest', href: base, topics: [
  {label: 'All presentations', href: base + 'browse/all/'}
]};
