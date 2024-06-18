import adapter from '@sveltejs/adapter-vercel'
import { vitePreprocess } from '@sveltejs/vite-plugin-svelte'
import remarkMath from 'remark-math';
// import rehypeKatex from 'rehype-katex';
import rehypeKatexSvelte from 'rehype-katex-svelte';
import{mdsvex} from 'mdsvex'

/** @type {import('mdsvex').MdsvexOptions}**/
const mdsvexOptions = {
  extensions: ['.md'],
  remarkPlugins: [remarkMath],
  rehypePlugins: [rehypeKatexSvelte],
}
/** @type {import('@sveltejs/kit').Config}  */
const config = {
	// Consult https://kit.svelte.dev/docs/integrations#preprocessors
	// for more information about preprocessors
  extensions: ['.svelte', '.md'],
	preprocess: [vitePreprocess(), mdsvex(mdsvexOptions)],

kit: {
		adapter: adapter({
			fallback: '404.html'
		}),
		paths: {
			base: process.argv.includes('dev') ? '' : process.env.BASE_PATH
		}
	}
}

export default config
