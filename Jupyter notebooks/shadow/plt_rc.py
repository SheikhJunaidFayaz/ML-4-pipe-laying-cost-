from cycler import cycler

def get_Params_():
    return {'_internal.classic_mode': False,
           'agg.path.chunksize': 0,
           'animation.bitrate': -1,
           'animation.codec': 'h264',
           'animation.convert_args': [],
           'animation.convert_path': 'convert',
           'animation.embed_limit': 20.0,
           'animation.ffmpeg_args': [],
           'animation.ffmpeg_path': 'ffmpeg',
           'animation.frame_format': 'png',
           'animation.html': 'none',
           'animation.writer': 'ffmpeg',
           'axes.autolimit_mode': 'data',
           'axes.axisbelow': 'line',
           'axes.edgecolor': 'black',
           'axes.facecolor': 'white',
           'axes.formatter.limits': [-7, 7],
           'axes.formatter.min_exponent': 0,
           'axes.formatter.offset_threshold': 4,
           'axes.formatter.use_locale': False,
           'axes.formatter.use_mathtext': True,
           'axes.formatter.useoffset': True,
           'axes.grid': False,
           'axes.grid.axis': 'both',
           'axes.grid.which': 'both',
           'axes.labelcolor': 'black',
           'axes.labelpad': 4.0,
           'axes.labelsize': 20.0,
           'axes.labelweight': 'bold',
           'axes.linewidth': 1.5,
           'axes.prop_cycle': ((cycler('color', ['blue', 'red', 'green', 'purple', 'brown']) + cycler('linestyle', ['-', '-', '-', '-', '-'])) + cycler('marker', ['', '', '', '', ''])),
           'axes.spines.bottom': True,
           'axes.spines.left': True,
           'axes.spines.right': True,
           'axes.spines.top': True,
           'axes.titlepad': 6.0,
           'axes.titlesize': 20.0,
           'axes.titleweight': 'bold',
           'axes.unicode_minus': True,
           'axes.xmargin': 0.05,
           'axes.ymargin': 0.05,
           'axes3d.grid': True,
           'backend': 'module://ipykernel.pylab.backend_inline',
           'backend_fallback': True,
           'boxplot.bootstrap': None,
           'boxplot.boxprops.color': 'black',
           'boxplot.boxprops.linestyle': '-',
           'boxplot.boxprops.linewidth': 1.0,
           'boxplot.capprops.color': 'black',
           'boxplot.capprops.linestyle': '-',
           'boxplot.capprops.linewidth': 1.0,
           'boxplot.flierprops.color': 'black',
           'boxplot.flierprops.linestyle': 'none',
           'boxplot.flierprops.linewidth': 1.0,
           'boxplot.flierprops.marker': 'o',
           'boxplot.flierprops.markeredgecolor': 'black',
           'boxplot.flierprops.markerfacecolor': 'none',
           'boxplot.flierprops.markersize': 10.0,
           'boxplot.meanline': False,
           'boxplot.meanprops.color': 'C2',
           'boxplot.meanprops.linestyle': '--',
           'boxplot.meanprops.linewidth': 1.0,
           'boxplot.meanprops.marker': '^',
           'boxplot.meanprops.markeredgecolor': 'C2',
           'boxplot.meanprops.markerfacecolor': 'C2',
           'boxplot.meanprops.markersize': 10.0,
           'boxplot.medianprops.color': 'C1',
           'boxplot.medianprops.linestyle': '-',
           'boxplot.medianprops.linewidth': 1.0,
           'boxplot.notch': False,
           'boxplot.patchartist': False,
           'boxplot.showbox': True,
           'boxplot.showcaps': True,
           'boxplot.showfliers': True,
           'boxplot.showmeans': False,
           'boxplot.vertical': True,
           'boxplot.whiskerprops.color': 'black',
           'boxplot.whiskerprops.linestyle': '-',
           'boxplot.whiskerprops.linewidth': 1.0,
           'boxplot.whiskers': 1.5,
           'contour.corner_mask': True,
           'contour.negative_linestyle': 'dashed',
           'date.autoformatter.day': '%Y-%m-%d',
           'date.autoformatter.hour': '%m-%d %H',
           'date.autoformatter.microsecond': '%M:%S.%f',
           'date.autoformatter.minute': '%d %H:%M',
           'date.autoformatter.month': '%Y-%m',
           'date.autoformatter.second': '%H:%M:%S',
           'date.autoformatter.year': '%Y',
           'docstring.hardcopy': False,
           'errorbar.capsize': 3.0,
           'figure.autolayout': False,
           'figure.constrained_layout.h_pad': 0.04167,
           'figure.constrained_layout.hspace': 0.02,
           'figure.constrained_layout.use': False,
           'figure.constrained_layout.w_pad': 0.04167,
           'figure.constrained_layout.wspace': 0.02,
           'figure.dpi': 72.0,
           'figure.edgecolor': (1, 1, 1, 0),
           'figure.facecolor': 'w',
           'figure.figsize': [6.0, 6.0],
           'figure.max_open_warning': 20,
           'figure.subplot.bottom': 0.125,
           'figure.subplot.hspace': 0.2,
           'figure.subplot.left': 0.125,
           'figure.subplot.right': 0.9,
           'figure.subplot.top': 0.88,
           'figure.subplot.wspace': 0.2,
           'figure.titlesize': 20.0,
           'figure.titleweight': 'bold',
           'font.cursive': ['Apple Chancery',
                            'Textile',
                            'Zapf Chancery',
                            'Sand',
                            'Script MT',
                            'Felipa',
                            'cursive'],
           'font.family': ['Arial'],
           'font.fantasy': ['Comic Sans MS',
                            'Chicago',
                            'Charcoal',
                            'Impact',
                            'Western',
                            'Humor Sans',
                            'xkcd',
                            'fantasy'],
           'font.monospace': ['DejaVu Sans Mono',
                              'Bitstream Vera Sans Mono',
                              'Computer Modern Typewriter',
                              'Andale Mono',
                              'Nimbus Mono L',
                              'Courier New',
                              'Courier',
                              'Fixed',
                              'Terminal',
                              'monospace'],
           'font.sans-serif': ['DejaVu Sans',
                               'Bitstream Vera Sans',
                               'Computer Modern Sans Serif',
                               'Lucida Grande',
                               'Verdana',
                               'Geneva',
                               'Lucid',
                               'Arial',
                               'Helvetica',
                               'Avant Garde',
                               'sans-serif'],
           'font.serif': ['DejaVu Serif',
                          'Times New Roman',
                          'Bitstream Vera Serif',
                          'Computer Modern Roman',
                          'New Century Schoolbook',
                          'Century Schoolbook L',
                          'Utopia',
                          'ITC Bookman',
                          'Bookman',
                          'Nimbus Roman No9 L',
                          'Times New Roman',
                          'Times',
                          'Palatino',
                          'Charter',
                          'serif'],
           'font.size': 20.0,
           'font.stretch': 'normal',
           'font.style': 'normal',
           'font.variant': 'normal',
           'font.weight': 'bold',
           'grid.alpha': 1.0,
           'grid.color': '#b0b0b0',
           'grid.linestyle': '-',
           'grid.linewidth': 0.8,
           'hatch.color': 'black',
           'hatch.linewidth': 1.0,
           'hist.bins': 10,
           'image.aspect': 'equal',
           'image.cmap': 'viridis',
           'image.composite_image': True,
           'image.interpolation': 'nearest',
           'image.lut': 256,
           'image.origin': 'lower',
           'image.resample': True,
           'interactive': True,
           'keymap.back': ['left', 'c', 'backspace'],
           'keymap.copy': ['ctrl+c', 'cmd+c'],
           'keymap.forward': ['right', 'v'],
           'keymap.fullscreen': ['f', 'ctrl+f'],
           'keymap.grid': ['g'],
           'keymap.grid_minor': ['G'],
           'keymap.help': ['f1'],
           'keymap.home': ['h', 'r', 'home'],
           'keymap.pan': ['p'],
           'keymap.quit': ['ctrl+w', 'cmd+w', 'q'],
           'keymap.quit_all': ['W', 'cmd+W', 'Q'],
           'keymap.save': ['s', 'ctrl+s'],
           'keymap.xscale': ['k', 'L'],
           'keymap.yscale': ['l'],
           'keymap.zoom': ['o'],
           'legend.borderaxespad': 0.5,
           'legend.borderpad': 0.4,
           'legend.columnspacing': 2.0,
           'legend.edgecolor': '0.8',
           'legend.facecolor': 'inherit',
           'legend.fancybox': True,
           'legend.fontsize': 20.0,
           'legend.framealpha': 0.8,
           'legend.frameon': False,
           'legend.handleheight': 0.7,
           'legend.handlelength': 2.0,
           'legend.handletextpad': 0.8,
           'legend.labelspacing': 0.5,
           'legend.loc': 'best',
           'legend.markerscale': 1.0,
           'legend.numpoints': 1,
           'legend.scatterpoints': 1,
           'legend.shadow': False,
           'legend.title_fontsize': 20.0,
           'lines.antialiased': True,
           'lines.color': 'C0',
           'lines.dash_capstyle': 'butt',
           'lines.dash_joinstyle': 'round',
           'lines.dashdot_pattern': [6.4, 1.6, 1.0, 1.6],
           'lines.dashed_pattern': [3.7, 1.6],
           'lines.dotted_pattern': [1.0, 1.65],
           'lines.linestyle': '-',
           'lines.linewidth': 2.0,
           'lines.marker': 'None',
           'lines.markeredgecolor': 'auto',
           'lines.markeredgewidth': 1.0,
           'lines.markerfacecolor': 'auto',
           'lines.markersize': 10.0,
           'lines.scale_dashes': True,
           'lines.solid_capstyle': 'projecting',
           'lines.solid_joinstyle': 'round',
           'markers.fillstyle': 'full',
           'mathtext.bf': 'sans:bold',
           'mathtext.cal': 'cursive',
           'mathtext.default': 'default',
           'mathtext.fallback': 'cm',
           'mathtext.fontset': 'custom',
           'mathtext.it': 'sans:italic',
           'mathtext.rm': 'sans',
           'mathtext.sf': 'sans',
           'mathtext.tt': 'monospace',
           'patch.antialiased': True,
           'patch.edgecolor': 'black',
           'patch.facecolor': 'C0',
           'patch.force_edgecolor': False,
           'patch.linewidth': 1.0,
           'path.effects': [],
           'path.simplify': True,
           'path.simplify_threshold': 0.1111111111111111,
           'path.sketch': None,
           'path.snap': True,
           'pdf.compression': 6,
           'pdf.fonttype': 3,
           'pdf.inheritcolor': False,
           'pdf.use14corefonts': False,
           'pgf.preamble': "",
           'pgf.rcfonts': True,
           'pgf.texsystem': 'xelatex',
           'polaraxes.grid': True,
           'ps.distiller.res': 6000,
           'ps.fonttype': 3,
           'ps.papersize': 'letter',
           'ps.useafm': False,
           'ps.usedistiller': False,
           'savefig.bbox': 'tight',
           'savefig.directory': '~',
           'savefig.dpi': 'figure',
           'savefig.edgecolor': 'white',
           'savefig.facecolor': 'white',
           'savefig.format': 'png',
           'savefig.orientation': 'portrait',
           'savefig.pad_inches': 0.1,
           'savefig.transparent': False,
           'scatter.marker': 'o',
           'svg.fonttype': 'path',
           'svg.hashsalt': None,
           'svg.image_inline': True,
           'text.antialiased': True,
           'text.color': 'black',
           'text.hinting': 'auto',
           'text.hinting_factor': 8,
           'text.latex.preamble': '\\boldmath',
           'text.usetex': False,
           'timezone': 'UTC',
           'tk.window_focus': False,
           'toolbar': 'toolbar2',
           'xtick.alignment': 'center',
           'xtick.bottom': True,
           'xtick.color': 'black',
           'xtick.direction': 'in',
           'xtick.labelbottom': True,
           'xtick.labelsize': 18.0,
           'xtick.labeltop': False,
           'xtick.major.bottom': True,
           'xtick.major.pad': 3.5,
           'xtick.major.size': 10,
           'xtick.major.top': True,
           'xtick.major.width': 1.5,
           'xtick.minor.bottom': True,
           'xtick.minor.pad': 3.4,
           'xtick.minor.size': 6,
           'xtick.minor.top': True,
           'xtick.minor.visible': True,
           'xtick.minor.width': 1.5,
           'xtick.top': True,
           'ytick.alignment': 'center_baseline',
           'ytick.color': 'black',
           'ytick.direction': 'in',
           'ytick.labelleft': True,
           'ytick.labelright': False,
           'ytick.labelsize': 18.0,
           'ytick.left': True,
           'ytick.major.left': True,
           'ytick.major.pad': 3.5,
           'ytick.major.right': True,
           'ytick.major.size': 10,
           'ytick.major.width': 1.5,
           'ytick.minor.left': True,
           'ytick.minor.pad': 3.4,
           'ytick.minor.right': True,
           'ytick.minor.size': 6.0,
           'ytick.minor.visible': True,
           'ytick.minor.width': 1.5,
           'ytick.right': True}
