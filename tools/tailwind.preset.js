// OsoolExit Tailwind preset. Colors point at the CSS variables in theme.css,
// so light/dark switching and the RTL defaults live in one place.
// Usage: presets: [require('./tailwind.preset.js')]   (and import theme.css)
module.exports = {
  theme: {
    extend: {
      colors: {
        primary: { DEFAULT: 'var(--primary)', hover: 'var(--primary-hover)', fg: 'var(--on-primary)' },
        accent: { DEFAULT: 'var(--accent)', hover: 'var(--accent-hover)', fg: 'var(--on-accent)', deep: 'var(--accent-deep)', text: 'var(--accent-text)' },
        bg: 'var(--bg)',
        surface: { DEFAULT: 'var(--surface)', sunken: 'var(--surface-sunken)' },
        ink: { DEFAULT: 'var(--ink)', muted: 'var(--ink-muted)' },
        line: { DEFAULT: 'var(--border)', strong: 'var(--border-strong)' },
        verified: { fg: 'var(--verified-fg)', bg: 'var(--verified-bg)' },
        review: { fg: 'var(--review-fg)', bg: 'var(--review-bg)' },
        declared: { fg: 'var(--declared-fg)', bg: 'var(--declared-bg)' },
        unknown: { fg: 'var(--unknown-fg)', bg: 'var(--unknown-bg)' },
        danger: { fg: 'var(--danger-fg)', bg: 'var(--danger-bg)' },
      },
      fontFamily: {
        sans: ['var(--font-ar)', 'var(--font-en)', 'sans-serif'],
        latin: ['var(--font-en)', 'sans-serif'],
      },
      borderRadius: { DEFAULT: '12px', sm: '8px', pill: '999px' },
      boxShadow: { card: 'var(--shadow-1)', raised: 'var(--shadow-2)' },
      spacing: { 1: '4px', 2: '8px', 3: '16px', 4: '24px', 5: '32px', 6: '48px', 7: '64px' },
    },
  },
  plugins: [],
};
