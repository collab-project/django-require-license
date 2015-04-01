// Copyright Collab 2013-2015
/*
* Build profile for tests.
* 
* This supports all the normal configuration available to a r.js build profile.
* The only gotchas are:
*
* - 'baseUrl' will be overidden by django-require during the build process.
* - 'appDir' will be overidden by django-require during the build process.
* - 'dir' will be overidden by django-require during the build process.
* 
* Check r.js docs for options: http://requirejs.org/docs/optimization.html#options
*/
({
    // By default all the configuration for optimization happens from the command
    // line or by properties in the config file, and configuration that was
    // passed to requirejs as part of the app's runtime "main" JS file is *not*
    // considered. However, if you prefer the "main" JS file configuration
    // to be read for the build so that you do not have to duplicate the values
    // in a separate configuration, set this property to the location of that
    // main JS file. The first requirejs({}), require({}), requirejs.config({}),
    // or require.config({}) call found in that file will be used.
    mainConfigFile: "app.js",

    // If you only intend to optimize a module (and its dependencies), with
    // a single file as the output, you can specify the module options inline,
    // instead of using the 'modules' section. 'exclude',
    // 'excludeShallow', 'include' and 'insertRequire' are all allowed as siblings
    // to name. The name of the optimized file is specified by 'out'.
    name: "app",

    // An alternative to "include". Normally only used in a requirejs.config()
    // call for a module used for mainConfigFile, since requirejs will read
    // "deps" during runtime to do the equivalent of require(deps) to kick
    // off some module loading.
    //
    // This can be necessary when some of the templates aren't picked up due to
    // the fact that they're dynamically loaded, eg:
    //
    //   var templateName = 'text!templates/portfolio/filters/type.html';
    //   require([templateName], _.bind(this.onTemplateLoaded, this));
    //
    // Also see: https://github.com/jrburke/almond/issues/50
    //
    //deps: [
    //          "text!templates/lab/filters/category.html"
    //],

    // If it is not a one file optimization, scan through all .js files in the
    // output directory for any plugin resource dependencies, and if the plugin
    // supports optimizing them as separate files, optimize them. Can be a
    // slower optimization. Only use if there are some plugins that use things
    // like XMLHttpRequest that do not work across domains, but the built code
    // will be placed on another domain.
    optimizeAllPluginResources: false,

    // Finds require() dependencies inside a require() or define call. By default
    // this value is false, because those resources should be considered dynamic/runtime
    // calls. However, for some optimization scenarios, it is desirable to
    // include them in the build.
    // Introduced in 1.0.3. Previous versions incorrectly found the nested calls
    // by default.
    findNestedDependencies: true,

    // Inlines the text for any text! dependencies, to avoid the separate
    // async XMLHttpRequest calls to load those dependencies.
    inlineText: true,

    // If set to true, any files that were combined into a build bundle will be
    // removed from the output folder.
    removeCombined: false,

    // Used to inline i18n resources into the built file. If no locale
    // is specified, i18n resources will not be inlined. Only one locale
    // can be inlined for a build. Root bundles referenced by a build layer
    // will be included in a build layer regardless of locale being set.
    // locale: "en-us",

    // How to optimize all the JS files in the build output directory.
    // Right now only the following values
    // are supported:
    // - "uglify": (default) uses UglifyJS to minify the code.
    // - "uglify2": in version 2.1.2+. Uses UglifyJS2.
    // - "closure": uses Google's Closure Compiler in simple optimization
    // mode to minify the code. Only available if running the optimizer using
    // Java.
    // - "closure.keepLines": Same as closure option, but keeps line returns
    // in the minified files.
    // - "none": no minification will be done.
    optimize: "uglify2",

    // If using UglifyJS2 for script optimization, these config options can be
    // used to pass configuration values to UglifyJS2.
    // For possible `output` values see:
    // https://github.com/mishoo/UglifyJS2#beautifier-options
    // For possible `compress` values see:
    // https://github.com/mishoo/UglifyJS2#compressor-options
    uglify2: {
        output: {
            beautify: false
        },
        compress: {
            // Pass true to discard calls to console.* functions.
            //drop_console: true,
            // Pass an array of names and UglifyJS will assume that those
            // functions do not produce side effects
            //pure_funcs: ['console.log', 'console.error', 'console.warn', 'console.debug'],
            // Display warnings when dropping unreachable code or unused declarations etc.
            warnings: false
        }
    },

    // By default, comments that have a license in them are preserved in the
    // output. However, for a larger built files there could be a lot of
    // comment files that may be better served by having a smaller comment
    // at the top of the file that points to the list of all the licenses.
    // This option will turn off the auto-preservation, but you will need
    // work out how best to surface the license information.
    preserveLicenseComments: false,

    // Allow CSS optimizations. Allowed values:
    // - "standard": @import inlining, comment removal and line returns.
    // Removing line returns may have problems in IE, depending on the type
    // of CSS.
    // - "standard.keepLines": like "standard" but keeps line returns.
    // - "none": skip CSS optimizations.
    // - "standard.keepComments": keeps the file comments, but removes line
    // returns. (r.js 1.0.8+)
    // - "standard.keepComments.keepLines": keeps the file comments and line
    // returns. (r.js 1.0.8+)
    optimizeCss: "standard",

    // The default behaviour is to optimize the build layers (the "modules"
    // section of the config) and any other JS file in the directory. However, if
    // the non-build layer JS files will not be loaded after a build, you can
    // skip the optimization of those files, to speed up builds. Set this value
    // to true if you want to skip optimizing those other non-build layer JS
    // files.
    skipDirOptimize: true
})
