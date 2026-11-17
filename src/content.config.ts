import { defineCollection, z } from 'astro:content';
import {validDate} from './lib/library-filters.mjs';
import {stampMissingPresentationDates,stampPresentationDate} from './lib/stamp-presentation-dates.mjs';
import { glob } from 'astro/loaders';
const internalPath = z.string().startsWith('/');
const catalogueLoader=glob({ pattern: '**/*.json', base: './src/content/presentations' });
let watching=false;
const presentations = defineCollection({
 loader: {name:'dated-presentations', async load(context) {
  stampMissingPresentationDates();
  if(context.watcher && !watching){context.watcher.on('add',file=>stampPresentationDate(file));watching=true;}
  await catalogueLoader.load(context);
 }},
 schema: ({ image }) => z.object({
  title: z.string().min(1), topic: z.string().min(1), format: z.string().min(1),
  summary: z.string().min(1), author: z.string().min(1),
  href: internalPath, pdf: internalPath.optional(), downloadLabel: z.string().optional(),
  tags: z.array(z.string().min(1)).min(1), thumbnail: image().optional(),
  published: z.string().regex(/^\d{4}-\d{2}-\d{2}$/).refine(v => validDate(v), 'Use a valid publication date').optional(),
  order: z.number().int().nonnegative().default(0), draft: z.boolean().default(false)
 })
});
export const collections = { presentations };
